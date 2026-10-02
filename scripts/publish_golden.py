#!/usr/bin/env python3
"""Coordinator-only publisher for already reviewed, signed bounded chapter releases."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(*args):return subprocess.check_output(args,cwd=ROOT,text=True).strip()
def call(*args):subprocess.run(args,cwd=ROOT,check=True)
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def update_status(chapter,coverage):
 receipts=list((ROOT/'diplomatic/publication').glob('ch*-v1.json')) if (ROOT/'diplomatic/publication').exists() else []
 finished=len(receipts)
 state={'chapter':chapter,'completed_chapters':finished,'target_chapters':8,'phase':'golden Tibetan edition','governing_scan':'adzom-1973 / W1KG892 / I1KG895','current_coverage':coverage,'full_scan_proofreading':False,'exhaustive_witness_collation':False,'translation_started':False,'next_task':f'Freeze chapter{chapter+1} contract' if chapter<8 else 'Build aggregate golden v1'}
 dump(ROOT/'diplomatic/WORK-QUEUE.json',{'schema_version':1,'scope':'eight sequential golden chapters','state':state,'tasks':[] if chapter==8 else [{'chapter':chapter+1,'status':'not_started','task':'freeze contract; inspect finite loci; publish release'}]})
 text=f'''# Golden edition state\n\nGoverning scan: Adzom1973 W1KG892/I1KG895. Electronic base: preserved Tibetan Wikisource; Wylie comparison is the same transcript family.\n\n- Current chapter: {chapter}; completed chapter publications: {finished}/8.\n- Anchors in current release: {coverage['anchor_count']}; changed text anchors: {coverage['changed_text_anchors']}; restorations: {coverage['restoration_count']}.\n- Decisions completed/remaining: {coverage['editorial_decisions_completed']}/0.\n- Targeted source checks completed/remaining: {coverage['source_checks_completed']}/0.\n- Current deliverable groups: 6/6 built; bounded validation/signoff passed before publication.\n- Unresolved records: {len(coverage['unresolved'])}; exact loci in chapters/{chapter:02}/coverage.json.\n- Full scan proofreading, exhaustive witness collation and independent human certification: false.\n- Publication receipts: diplomatic/publication/. Prior chapter files remain fixed at their annotated tags.\n- Next finite task: {state['next_task']}. Translation has not begun.\n'''
 (ROOT/'diplomatic/WORK-STATUS.md').write_text(text)
 (ROOT/'diplomatic/HANDOFF.md').write_text(text+'\nRead RELEASE-POLICY.md, GOVERNING-WITNESS.json and the next chapter contract before substantive work. Never infer physical agreement from electronic equality.\n')
 p=ROOT/'PROJECT-STATUS.md';s=p.read_text();import re
 s=re.sub(r'- Phase: .*',f'- Phase: golden Tibetan edition; {finished}/8 chapter publications complete',s,count=1)
 s=re.sub(r'golden chapter releases\d/8',f'golden chapter releases{finished}/8',s)
 s=re.sub(r'- Editorial anchors, reading decisions, restorations and translated pairs: .*',f'- Golden source anchors:2053; current chapter{chapter} details in diplomatic/WORK-STATUS.md; translated pairs:0',s)
 p.write_text(s)
def main():
 p=argparse.ArgumentParser();p.add_argument('--chapter',type=int,required=True);args=p.parse_args();n=args.chapter
 assert 1<=n<=8
 d=ROOT/f'diplomatic/chapters/{n:02}';tag=f'golden-ch{n:02}-v1';receipt=ROOT/f'diplomatic/publication/ch{n:02}-v1.json'
 if n>1:assert (ROOT/f'diplomatic/publication/ch{n-1:02}-v1.json').exists(),'Previous chapter not published'
 call(sys.executable,str(ROOT/'scripts/golden_pipeline.py'),'validate','--chapter',str(n),'--final')
 assert not receipt.exists(),'Release already has receipt; inspect instead of republishing'
 cov=json.loads((d/'coverage.json').read_text());update_status(n,cov)
 stage=[str(d.relative_to(ROOT)),f'evidence/golden/{n:02}','diplomatic/WORK-STATUS.md','diplomatic/HANDOFF.md','diplomatic/WORK-QUEUE.json','PROJECT-STATUS.md']
 call('git','add',*stage);call('git','diff','--cached','--check')
 call('git','commit','-m',f'Release bounded golden chapter {n}: {cov["changed_text_anchors"]} changed anchors')
 commit=run('git','rev-parse','HEAD');call('git','tag','-a',tag,'-m',f'Golden Tibetan chapter{n} v1; Adzom governing; targeted review; see exact coverage and uncertainty.')
 call('git','push','origin','main',f'refs/tags/{tag}')
 tag_object=run('git','rev-parse',tag);remote=run('git','ls-remote','origin','refs/heads/main',f'refs/tags/{tag}',f'refs/tags/{tag}^{{}}')
 mapping={line.split()[1]:line.split()[0] for line in remote.splitlines()}
 assert mapping.get('refs/heads/main')==commit and mapping.get(f'refs/tags/{tag}')==tag_object and mapping.get(f'refs/tags/{tag}^{{}}')==commit,remote
 dump(receipt,{'chapter':n,'tag':tag,'release_commit':commit,'remote_tag_object':tag_object,'remote_peeled_commit':commit,'remote_main_at_release':commit,'build_manifest_sha256':hashlib.sha256((d/'build-manifest.json').read_bytes()).hexdigest(),'coverage':cov,'publication_note':'Receipt committed after fixed tag; tag not moved.'})
 update_status(n,cov)
 call('git','add',str(receipt.relative_to(ROOT)),*stage[2:]);call('git','commit','-m',f'Confirm remote publication of golden chapter {n}')
 call('git','push','origin','main');head=run('git','rev-parse','HEAD');remote_main=run('git','ls-remote','origin','refs/heads/main').split()[0];assert head==remote_main
 dirty=run('git','status','--porcelain');assert not dirty,'Unpublished work remains: '+dirty
 print(json.dumps({'chapter':n,'tag':tag,'release_commit':commit,'receipt_commit':head,'remote_main_verified':True,'clean_tree':True}))
if __name__=='__main__':main()
