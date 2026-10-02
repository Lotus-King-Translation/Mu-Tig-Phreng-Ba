"""Coordinator publication, after explicit aggregate review and signoff."""
import json,hashlib,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def run(*a): return subprocess.check_output(a,cwd=root,text=True).strip()
def call(*a): subprocess.run(a,cwd=root,check=True)
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,o): p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
tag='golden-v1';g=root/'golden';rpath=root/'diplomatic/publication/golden-v1.json'
assert not rpath.exists(),'Already published; inspect instead'
paths=['golden','README.md','PROJECT-STATUS.md','diplomatic/WORK-STATUS.md','diplomatic/HANDOFF.md','diplomatic/WORK-QUEUE.json','scripts/publish_golden_aggregate.py']
def allowed(path):return path.startswith('golden/') or path in paths[1:]
assert not run('git','diff','--cached','--name-only'),'Index must be empty before publication'
dirty=run('git','diff','--name-only').splitlines()+run('git','ls-files','--others','--exclude-standard').splitlines()
assert all(allowed(p) for p in dirty),'Unrelated dirty files: '+str([p for p in dirty if not allowed(p)])
assert run('git','branch','--show-current')=='main'
assert run('git','rev-parse','HEAD')==run('git','ls-remote','origin','refs/heads/main').split()[0]
s=json.loads((g/'signoff.json').read_text());m=json.loads((g/'build-manifest.json').read_text())
assert s['approved'] is True and s['edition']=='bounded-golden-v1'
assert s['build_manifest_sha256']==h(g/'build-manifest.json')
assert s['review_sha256']==h(root/s['review_path'])
assert s['output_sha256']==m['output_sha256']
assert s['claims']==m['claims'] and not any(m['claims'].values())
for n,d in m['output_sha256'].items():assert h(g/n)==d
assert len(m['chapter_releases'])==8
refs=[ref for c in m['chapter_releases'] for ref in ['refs/tags/'+c['tag'],'refs/tags/'+c['tag']+'^{}']]
remote_chapters={line.split()[1]:line.split()[0] for line in run('git','ls-remote','origin',*refs).splitlines()}
for c in m['chapter_releases']:
 assert remote_chapters.get('refs/tags/'+c['tag'])==c['tag_object'],'Remote chapter tag changed: '+c['tag']
 assert remote_chapters.get('refs/tags/'+c['tag']+'^{}')==c['peeled_commit'],'Remote chapter commit changed: '+c['tag']
dump(g/'remote-chapter-verification.json',{'passed':True,'remote':'origin','refs':remote_chapters,'method':'Fresh git ls-remote comparison with all eight signed chapter release identities before aggregate publication.'})
v=subprocess.run([str(root/'.venv/bin/python'),'scripts/build_golden_aggregate.py','verify'],cwd=root,capture_output=True,text=True)
assert v.returncode==0,v.stdout+v.stderr
validation=json.loads(v.stdout);validation.update({'mode':'final','signoff_hash_binding':True,'signoff_sha256':h(g/'signoff.json'),'review_hash_binding':True,'fresh_remote_chapter_refs':True,'remote_chapter_verification_sha256':h(g/'remote-chapter-verification.json'),'claims':s['claims'],'final_gate_method':'Coordinator assertions in scripts/publish_golden_aggregate.py, following read-only aggregate verification.'})
dump(g/'validation.json',validation)
call('git','add',*paths)
staged=run('git','diff','--cached','--name-only').splitlines()
assert staged and all(allowed(p) for p in staged),'Unexpected staged publication paths'
call('git','-c','core.whitespace=-blank-at-eof','diff','--cached','--check')
call('git','commit','-m','Release complete bounded golden Tibetan edition v1')
commit=run('git','rev-parse','HEAD');call('git','tag','-a',tag,'-m','String of Pearls golden Tibetan v1: eight fixed chapters; targeted Adzom scan review; all original anchors preserved. See coverage and explicit uncertainty.')
call('git','push','origin','main','refs/tags/'+tag)
remote={l.split()[1]:l.split()[0] for l in run('git','ls-remote','origin','refs/heads/main','refs/tags/'+tag,'refs/tags/'+tag+'^{}').splitlines()}
assert remote['refs/heads/main']==remote['refs/tags/'+tag+'^{}']==commit
assert remote['refs/tags/'+tag]==run('git','rev-parse',tag)
dump(rpath,{'edition':'bounded-golden-v1','tag':tag,'release_commit':commit,'remote_tag_object':remote['refs/tags/'+tag],'remote_peeled_commit':commit,'remote_main_at_release':commit,'build_manifest_sha256':h(g/'build-manifest.json'),'signoff_sha256':h(g/'signoff.json'),'coverage_sha256':h(g/'coverage.json'),'chapter_releases':m['chapter_releases'],'publication_note':'Receipt committed after fixed tag; tag not moved.'})
call('git','add',str(rpath.relative_to(root)));call('git','commit','-m','Confirm remote publication of complete golden v1');call('git','push','origin','main')
head=run('git','rev-parse','HEAD');assert head==run('git','ls-remote','origin','refs/heads/main').split()[0]
assert not run('git','status','--porcelain'),'Unpublished work remains'
print(json.dumps({'tag':tag,'release_commit':commit,'receipt_commit':head,'remote_main_verified':True,'clean_tree':True},indent=2))
