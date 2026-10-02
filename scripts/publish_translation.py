#!/usr/bin/env python3
"""Publish an already committed, reviewed working translation chapter; root only."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import translation_pipeline as t
R=Path(__file__).resolve().parents[1]
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True).strip()
def call(*args):subprocess.run(args,cwd=R,check=True)
def dump(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def update_state(n):
    p=R/'translations/PLAN.json';plan=json.loads(p.read_text())
    covers=[json.loads((R/f'translations/chapters/{k:02}/coverage.json').read_text()) for k in range(1,n+1)]
    count=sum(x['golden_objects'] for x in covers)
    contract=json.loads((R/f'translations/chapters/{n:02}/contract.json').read_text())
    audit=json.loads((R/f'translations/chapters/{n:02}/adzom-audit.json').read_text())
    plan.update(current_chapter=n,current_source_range=[contract['golden_ids'][0],contract['golden_ids'][-1]],current_native_images=[x['image_index'] for x in audit['images']],source_objects_translated=count,source_objects_remaining=2053-count,chapter_publications_complete=n)
    dump(p,plan)
    next_task=f'Freeze chapter {n+1} source pairs, translate, audit and release.' if n<8 else 'Build, review and publish the complete English/paired edition.'
    handoff=f'''# Translation handoff\n\nPhase: annotated English working translation of fixed `golden-v1`; completed chapter releases {n}/8.\nSource objects represented in translated chapters: {count}/2053; remaining: {2053-count}.\nCurrent chapter {n}: all source pairs represented; native main-text comparison completed with explicit source uncertainties and untranscribed annotation limits.\nEndnote obligations: {sum(x['obligations_covered'] for x in covers)} covered, 0 remaining in released chapters.\nIndependent agent QC and structural final gates passed for each released chapter; no independent human certification or exhaustive witness collation claimed.\nGolden and canonical glossary unchanged. Exact per-chapter coverage, usage, open review flags, evidence and publication receipts are in chapters/NN and publication/.\nNext finite task: {next_task}\nThe next chapter has not started.\n'''
    (R/'translations/HANDOFF.md').write_text(handoff)
    (R/'translations/WORK-STATUS.md').write_text(handoff)
    p=R/'PROJECT-STATUS.md';s=p.read_text();import re
    s=re.sub(r'- Phase: .*',f'- Phase: English translation with Adzom endnotes; golden v1 fixed; translated chapters {n}/8',s,count=1)
    s=re.sub(r'translation/paired releases:[^\n]*',f'translation/paired chapter releases: {n}/8',s)
    s=re.sub(r'translated pairs:\d+',f'translated pairs:{sum(x["pairs"] for x in covers)}',s)
    s=re.sub(r'- Full scan proofreading, exhaustive witness collation and independent translation QC: .*',f'- Main-text Adzom comparison and independent agent translation QC: chapters 1–{n}; unreadable/source-layer limits remain explicit. Exhaustive witness collation and independent human certification: not performed.',s)
    marker='Golden editorial/source queues are closed.'
    if marker in s:s=s[:s.index(marker)]+f'{marker} English working translation releases {n}/8 complete; {count}/2053 source objects represented. Next finite task: {next_task} See translations/HANDOFF.md. Unresolved witness-research leads remain outside this bounded edition.\n'
    p.write_text(s)
def publish(n):
    t.need(git('branch','--show-current')=='main','Publication requires main')
    t.need(not git('status','--porcelain'),'Commit all reviewed project work before publication')
    t.validate(R,n,final=True)
    receipt=R/f'translations/publication/ch{n:02}-v1.json';t.need(not receipt.exists(),'Receipt already exists; inspect rather than republish')
    tag=f'translate-ch{n:02}-v1';head=git('rev-parse','HEAD')
    t.need(head==git('ls-remote','origin','refs/heads/main').split()[0],'Remote main differs')
    # Verify every prior chapter against the fresh remote before extending the edition.
    for k in range(1,n):
        prior=json.loads((R/f'translations/publication/ch{k:02}-v1.json').read_text());ref='refs/tags/'+prior['tag']
        found={line.split()[1]:line.split()[0] for line in git('ls-remote','origin',ref,ref+'^{}').splitlines()}
        t.need(found.get(ref)==prior['remote_tag_object'] and found.get(ref+'^{}')==prior['release_commit'],'Prior remote translation tag changed')
    call('git','tag','-a',tag,'-m',f'String of Pearls English working translation, chapter {n}; fixed golden-v1; Adzom endnotes; independent agent QC with explicit review flags.')
    call('git','push','origin','refs/tags/'+tag)
    refs={line.split()[1]:line.split()[0] for line in git('ls-remote','origin','refs/heads/main','refs/tags/'+tag,'refs/tags/'+tag+'^{}').splitlines()}
    t.need(refs.get('refs/heads/main')==head and refs.get('refs/tags/'+tag+'^{}')==head and refs.get('refs/tags/'+tag)==git('rev-parse',tag),'Remote release verification failed')
    d=R/f'translations/chapters/{n:02}'
    dump(receipt,{'chapter':n,'tag':tag,'release_commit':head,'remote_tag_object':refs['refs/tags/'+tag],'remote_peeled_commit':head,'remote_main_at_release':head,'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage_sha256':t.digest(d/'coverage.json'),'publication_note':'Agent-produced working translation for human review. Receipt committed after fixed annotated tag; tag not moved.'})
    update_state(n)
    call('git','add',str(receipt.relative_to(R)),'translations/PLAN.json','translations/HANDOFF.md','translations/WORK-STATUS.md','PROJECT-STATUS.md')
    call('git','commit','-m',f'Confirm remote publication of English chapter {n}')
    call('git','push','origin','main')
    new=git('rev-parse','HEAD');t.need(new==git('ls-remote','origin','refs/heads/main').split()[0],'Receipt remote verification failed')
    t.need(not git('status','--porcelain'),'Unpublished project work remains')
    print(json.dumps({'chapter':n,'tag':tag,'release_commit':head,'receipt_commit':new,'remote_main_verified':True,'clean_tree':True},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--chapter',type=int,required=True);publish(p.parse_args().chapter)
