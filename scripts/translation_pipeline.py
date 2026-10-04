#!/usr/bin/env python3
"""Strict sequential paired translation: exact golden coverage and complete endnotes."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
FORMATS={'prose','verse','h1','h2','h3'}
ROLE_MAP={'source_metadata':{'blank','metadata'},'source_heading':{'heading'},'source_annotation':{'annotation'},'work_colophon':{'colophon'},'restored_main_text':{'main_text'}}
CATEGORIES={'adzom_difference','transcript_correction','source_omission','source_layer','uncertain_reading','presentation','golden_uncertainty','translation_issue','terminology_provisional'}
AUDIT_TYPES={'adzom_difference','source_omission','source_layer','uncertain_reading','presentation'}
OUTPUTS=('reading.md','bilingual.md','machine.json','coverage.json')
END='<!-- endnotes -->'
MARK=re.compile(r'^<!-- pair: ([A-Za-z0-9-]+)(.*?) -->$',re.M)
REF=re.compile(r'\[\^([A-Za-z0-9-]+)\]')
CLAIMS={'automated_semantic_certification':False,'independent_human_certification':False}
class Error(ValueError):pass
def need(test,message):
    if not test:raise Error(message)
def sha(data):return hashlib.sha256(data).hexdigest()
def digest(path):return sha(path.read_bytes())
def load(path):return json.loads(path.read_text())
def encoded(value):return (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data if isinstance(data,bytes) else encoded(data))
def safe(root,rel):
    p=(root/rel).resolve();need(p.is_relative_to(root.resolve()),'Path outside repository: '+str(rel));return p
def git(root,*args):
    p=subprocess.run(['git','-C',str(root),*args],capture_output=True)
    need(p.returncode==0,'Git check failed: '+p.stderr.decode(errors='replace'));return p.stdout
def directory(root,n):return root/'translations/chapters'/f'{n:02}'
def unique(rows,key,label):
    ids=[r[key] for r in rows];need(len(ids)==len(set(ids)),'Duplicate '+label);return {r[key]:r for r in rows}

def baseline(root,n):
    need(1<=n<=8,'Chapter outside 1..8');p=load(root/'translations/PLAN.json')
    need(p['source_tag']=='golden-v1','Wrong golden edition')
    commit=git(root,'rev-parse','refs/tags/golden-v1^{commit}').decode().strip()
    need(commit==p['source_commit'],'Golden tag moved')
    body=git(root,'show',commit+':golden/reading.json')
    need(body==(root/'golden/reading.json').read_bytes() and sha(body)==p['source_reading_sha256'],'Golden source bytes changed')
    for file,key in [('glossary','glossary_sha256'),('standard','standard_sha256')]:need(digest(safe(root,p[file]))==p[key],file+' changed')
    reading=json.loads(body);b=reading['chapter_boundaries'][n-1]
    need(b['chapter']==n,'Golden chapter boundary mismatch')
    allrows=reading['objects'];ids=[r['id'] for r in allrows]
    rows=allrows[ids.index(b['first_object']):ids.index(b['last_object'])+1]
    changes=json.loads(git(root,'show',commit+f':diplomatic/chapters/{n:02}/changes.json'))['changes']
    pins={k:p[k] for k in ('source_tag','source_commit','source_reading_sha256','glossary','glossary_sha256','standard','standard_sha256')}
    return pins,rows,changes

def segmentation(root,n,rows):
    seg=load(directory(root,n)/'segmentation.json');need(isinstance(seg,list) and seg,'Empty segmentation')
    unique(seg,'id','pair ID');amap={r['id']:r for r in rows};seen=[]
    for p in seg:
        need(re.fullmatch(r'[A-Za-z0-9-]+',p['id']), 'Invalid pair ID')
        need(p['format'] in FORMATS and p.get('rationale'),'Missing format/rationale')
        need(p['golden_ids'] and all(x in amap for x in p['golden_ids']),'Unknown/empty golden references')
        roles={amap[x]['role'] for x in p['golden_ids']}
        need(roles<=ROLE_MAP.get(p['role'],{p['role']}),'Pair crosses source-role boundary')
        seen.extend(p['golden_ids'])
    need(seen==[r['id'] for r in rows],'Golden objects omitted, duplicated or reordered')
    return seg

def golden_obligations(rows,changes):
    result={}
    for c in changes:result['golden-change:'+c['id']]={'golden_ids':[c['anchor_id']],'kind':'change','changed_text':c['old']!=c['new']}
    for r in rows:
        for i,_ in enumerate(r['uncertainty']):result[f'golden-uncertainty:{r["id"]}:{i}']={'golden_ids':[r['id']],'kind':'uncertainty'}
    return result

def fixed_prior(root,k,ref):
    """Check the complete prior chapter and its inputs against an immutable ref."""
    d=directory(root,k);prefix=d.relative_to(root).as_posix()+'/'
    paths=git(root,'ls-tree','-rz','--name-only',ref,'--',prefix).split(b'\0')
    needed={prefix+x for x in (*OUTPUTS,'build-manifest.json','source.md','translation.md','signoff.json','qc.json')}
    actual={x.decode() for x in paths if x};need(needed<=actual,'Prior release files missing')
    current={p.relative_to(root).as_posix() for p in d.rglob('*') if p.is_file()}
    need(current==actual,'Prior released file inventory changed')
    for rel in actual:need(safe(root,rel).read_bytes()==git(root,'show',ref+':'+rel),'Prior released bytes changed: '+rel)
    for rel,expected in load(d/'build-manifest.json')['input_sha256'].items():
        need(digest(safe(root,rel))==expected,'Prior released input changed: '+rel)
        tagged=git(root,'show',ref+':'+rel)
        lfs=re.fullmatch(rb'version https://git-lfs.github.com/spec/v1\noid sha256:([0-9a-f]{64})\nsize ([0-9]+)\n',tagged)
        need((lfs.group(1).decode() if lfs else sha(tagged))==expected,'Prior tagged input differs: '+rel)
    final_gate(root,k)

def unsigned_saved_prior(root,record):
    """Freeze an explicitly acknowledged incomplete predecessor; never approve it."""
    k=record['chapter'];ref=record['commit'];d=directory(root,k);prefix=d.relative_to(root).as_posix()+'/'
    paths=git(root,'ls-tree','-rz','--name-only',ref,'--',prefix).split(b'\0')
    actual={x.decode() for x in paths if x}
    needed={prefix+x for x in (*OUTPUTS,'build-manifest.json','source.md','translation.md','segmentation.json',
        'contract.json','contract.sha256','note-map.json','pair-status.json','adzom-audit.json','audit-contract.json','audit-contract.sha256')}
    need(needed<=actual,'Unsigned saved draft files missing')
    need(not ({prefix+'qc.json',prefix+'signoff.json'}&actual),'Unsigned saved draft unexpectedly has final review records')
    current={p.relative_to(root).as_posix() for p in d.rglob('*') if p.is_file()}
    need(current==actual,'Unsigned saved draft file inventory changed')
    for rel in actual:need(safe(root,rel).read_bytes()==git(root,'show',ref+':'+rel),'Unsigned saved draft bytes changed: '+rel)
    manifest=load(d/'build-manifest.json')
    for rel,expected in manifest['input_sha256'].items():
        need(digest(safe(root,rel))==expected,'Unsigned saved draft input changed: '+rel)
        tagged=git(root,'show',ref+':'+rel)
        lfs=re.fullmatch(rb'version https://git-lfs.github.com/spec/v1\noid sha256:([0-9a-f]{64})\nsize ([0-9]+)\n',tagged)
        need((lfs.group(1).decode() if lfs else sha(tagged))==expected,'Unsigned saved draft committed input differs: '+rel)
    need(set(manifest['output_sha256'])==set(OUTPUTS),'Unsigned saved draft output inventory mismatch')
    for name,expected in manifest['output_sha256'].items():need(digest(d/name)==expected,'Unsigned saved draft output hash mismatch: '+name)

def draft_authorization(root,n,commit):
    """Explicit chapter 3/4/5/6/7/8 working exceptions; never publication receipts."""
    need(n in {3,4,5,6,7,8},'Draft continuation is authorized only for chapters 3, 4, 5, 6, 7 and 8')
    need(isinstance(commit,str) and re.fullmatch(r'[0-9a-f]{40}',commit),'Draft prior commit must be a full commit SHA')
    rel=f'translations/draft-authorizations/ch{n:02}.json';path=safe(root,rel);a=load(path)
    need(path.read_bytes()==git(root,'show','HEAD:'+rel),'Draft authorization must be committed unchanged')
    need(a.get('schema_version')=={3:1,4:2,5:3,6:4,7:5,8:6}[n] and a.get('chapter')==n and a.get('prior_chapter')==n-1 and a.get('prior_commit')==commit,'Draft authorization scope/commit mismatch')
    instruction={3:'excellent, move to chapter 3 then',4:'excellent, next chapter',5:'cool, then move on to next chapter',
        6:'So make sure that everything is in github up to date, and move on to the next chapter.',7:'go on',
        8:'great, next chapter then...how many do we have left?'}[n]
    need(a.get('authorized_scope')=='working_draft_only' and a.get('user_instruction')==instruction and a.get('date') and a.get('reason'),'Incomplete working-draft authorization')
    if n==3:
        records=[{'chapter':2,'commit':commit,'build_manifest_sha256':a.get('prior_build_manifest_sha256')}]
    else:
        records=a.get('reviewed_priors')
        chapters={4:[2,3],5:[2,3],6:[2,3,5],7:[2,3,5,6],8:[2,3,5,6,7]}[n]
        need(isinstance(records,list) and all(isinstance(x,dict) for x in records) and [x.get('chapter') for x in records]==chapters,
            'Draft authorization must pin exactly chapters '+{4:'2 and 3',5:'2 and 3',6:'2, 3 and 5',7:'2, 3, 5 and 6',8:'2, 3, 5, 6 and 7'}[n]+' in order')
        if n==4:
            need(records[-1].get('commit')==commit,'Draft authorization latest prior commit mismatch')
            legacy=draft_authorization(root,3,records[0].get('commit'))
            previous=load(safe(root,legacy['path']))
            need(records[0].get('build_manifest_sha256')==previous['prior_build_manifest_sha256'],'Draft chapter 2 pin differs from chapter 3 authorization')
        elif n==5:
            legacy=draft_authorization(root,4,records[-1].get('commit'))
            previous=load(safe(root,legacy['path']))
            need(records==previous['reviewed_priors'],'Chapter 5 reviewed priors differ from chapter 4 authorization')
            unsigned=a.get('unsigned_prior')
            need(isinstance(unsigned,dict) and unsigned.get('chapter')==4 and unsigned.get('commit')==commit
                and unsigned.get('review_state')=='unsigned_saved_draft','Chapter 5 requires the acknowledged unsigned chapter 4 snapshot')
            need(isinstance(unsigned.get('snapshot_tree_sha'),str) and re.fullmatch(r'[0-9a-f]{40}',unsigned['snapshot_tree_sha']),
                'Unsigned saved draft tree must be a full tree SHA')
            need(git(root,'rev-parse',commit+':translations/chapters/04').decode().strip()==unsigned['snapshot_tree_sha'],
                'Unsigned saved draft tree pin mismatch')
            records=records+[unsigned]
        elif n==6:
            need(records[-1].get('commit')==commit,'Draft authorization latest prior commit mismatch')
            unsigned=a.get('unsigned_prior')
            need(isinstance(unsigned,dict) and unsigned.get('chapter')==4 and unsigned.get('review_state')=='unsigned_saved_draft',
                'Chapter 6 requires the acknowledged unsigned chapter 4 snapshot')
            legacy=draft_authorization(root,5,unsigned.get('commit'))
            previous=load(safe(root,legacy['path']))
            need(records[:2]==previous['reviewed_priors'],'Chapter 6 reviewed priors differ from chapter 5 authorization')
            need(unsigned==previous['unsigned_prior'],'Chapter 6 unsigned prior differs from chapter 5 authorization')
            records=records+[unsigned]
        else:
            need(records[-1].get('commit')==commit,'Draft authorization latest prior commit mismatch')
            unsigned=a.get('unsigned_prior')
            need(isinstance(unsigned,dict) and unsigned.get('chapter')==4 and unsigned.get('review_state')=='unsigned_saved_draft',
                f'Chapter {n} requires the acknowledged unsigned chapter 4 snapshot')
            legacy=draft_authorization(root,n-1,records[-2].get('commit'))
            previous=load(safe(root,legacy['path']))
            need(records[:-1]==previous['reviewed_priors'],f'Chapter {n} reviewed priors differ from chapter {n-1} authorization')
            need(unsigned==previous['unsigned_prior'],f'Chapter {n} unsigned prior differs from chapter {n-1} authorization')
            records=records+[unsigned]
    for record in records:
        ref=record.get('commit');k=record['chapter']
        need(isinstance(ref,str) and re.fullmatch(r'[0-9a-f]{40}',ref),'Draft prior commit must be a full commit SHA')
        need(git(root,'cat-file','-t',ref).strip()==b'commit','Draft prior reference is not a commit')
        git(root,'merge-base','--is-ancestor',ref,commit)
        git(root,'merge-base','--is-ancestor',ref,'HEAD')
        need(sha(git(root,'show',ref+f':translations/chapters/{k:02}/build-manifest.json'))==record.get('build_manifest_sha256'),'Draft prior manifest pin mismatch')
    return {'path':rel,'sha256':digest(path),'prior_commit':commit,'scope':'working_draft_only'}

def prior(root,n,draft_prior_commit=None):
    reviewed={};unsigned=None
    if draft_prior_commit is not None:
        authorization=draft_authorization(root,n,draft_prior_commit)
        a=load(safe(root,authorization['path']))
        reviewed={2:draft_prior_commit} if n==3 else {x['chapter']:x['commit'] for x in a['reviewed_priors']}
        if n in {5,6,7,8}:unsigned=a['unsigned_prior']
    for k in range(1,n):
        if unsigned is not None and k==unsigned['chapter']:
            unsigned_saved_prior(root,unsigned)
            continue
        if k in reviewed:
            fixed_prior(root,k,reviewed[k])
            continue
        d=directory(root,k);r=load(root/f'translations/publication/ch{k:02}-v1.json');tag=f'translate-ch{k:02}-v1'
        need(r['chapter']==k and r['tag']==tag,'Prior translation receipt identity mismatch')
        need(git(root,'cat-file','-t',f'refs/tags/{tag}').strip()==b'tag','Prior tag is not annotated')
        need(git(root,'rev-parse',f'refs/tags/{tag}').decode().strip()==r['remote_tag_object'],'Prior tag object changed')
        need(git(root,'rev-parse',f'refs/tags/{tag}^{{commit}}').decode().strip()==r['release_commit']==r['remote_peeled_commit']==r['remote_main_at_release'],'Prior release commit changed')
        need(digest(d/'build-manifest.json')==r['build_manifest_sha256'],'Prior manifest changed')
        fixed_prior(root,k,tag)

def contract(root,n):
    pins,rows,changes=baseline(root,n);seg=segmentation(root,n,rows);d=directory(root,n);c=load(d/'contract.json')
    need(digest(d/'contract.json')==(d/'contract.sha256').read_text().strip(),'Contract changed')
    need(c['chapter']==n and c['pins']==pins,'Contract source pins changed')
    need(c['segmentation_sha256']==digest(d/'segmentation.json'),'Frozen segmentation changed')
    need(c['golden_ids']==[r['id'] for r in rows],'Contract range changed')
    need(c['known_obligations']==sorted(golden_obligations(rows,changes)),'Contract golden obligations changed')
    if 'draft_continuation' in c:
        need(c['draft_continuation']==draft_authorization(root,n,c['draft_continuation']['prior_commit']),'Frozen draft authorization changed')
    return pins,rows,changes,seg

def plan(root,n,draft_prior_commit=None):
    prior(root,n,draft_prior_commit);pins,rows,changes=baseline(root,n);segmentation(root,n,rows);d=directory(root,n)
    c={'schema_version':1,'chapter':n,'pins':pins,'golden_ids':[r['id'] for r in rows],
       'segmentation_sha256':digest(d/'segmentation.json'),'known_obligations':sorted(golden_obligations(rows,changes)),
       'audit_gate':'Complete adzom-audit.json and audit-contract hash seal required before candidate build; every later finding adds a mandatory note obligation.','claims':CLAIMS}
    if draft_prior_commit is not None:c['draft_continuation']=draft_authorization(root,n,draft_prior_commit)
    data=encoded(c)
    if (d/'contract.json').exists():need((d/'contract.json').read_bytes()==data,'Refusing to replace frozen contract')
    write(d/'contract.json',data);write(d/'contract.sha256',(sha(data)+'\n').encode())
    return {'chapter':n,'source_objects':len(rows),'known_note_obligations':len(c['known_obligations'])}

def header(pins,first,last,english=False):
    fields={'schema':'paired-text/2','text-id':'MTP'}
    fields.update({'source-edition':'golden-v1','translation-edition':'translation-v1'} if english else {'edition':'golden-v1'})
    fields.update({'language':'en' if english else 'bo','source-commit':pins['source_commit'],'source-sha256':pins['source_reading_sha256'],
                   'glossary-sha256':pins['glossary_sha256'],'standard-sha256':pins['standard_sha256'],
                   'scope-first-chapter':str(first),'scope-last-chapter':str(last)})
    return '---\n'+'\n'.join(k+': '+v for k,v in fields.items())+'\n---\n\n'

def parse(text,english=False):
    need(text.startswith('---\n'),'Missing front matter');end=text.find('\n---\n',4);need(end>=0,'Unterminated front matter')
    fm={}
    for line in text[4:end].splitlines():
        key,sep,val=line.partition(':');need(sep and key not in fm,'Malformed/duplicate front matter');fm[key]=val.strip()
    body=text[end+5:];notes={};has_endnotes=END in body
    need(body.count(END)<=1,'Duplicate endnotes boundary')
    if END in body:
        need(english,'Source contains endnotes');body,tail=body.split(END)
        matches=list(re.finditer(r'^\[\^([A-Za-z0-9-]+)\]:[ \t]*(.*)$',tail,re.M))
        need(not tail[:matches[0].start()].strip() if matches else not tail.strip(),'Unexpected endnote content')
        for i,m in enumerate(matches):
            ident=m.group(1);need(ident not in notes,'Duplicate endnote')
            raw=tail[m.start():matches[i+1].start() if i+1<len(matches) else len(tail)].strip('\n')
            parts=raw.splitlines();need(all(not x.strip() or x.startswith('    ') for x in parts[1:]),'Endnote continuation needs four spaces')
            value=m.group(2)+'\n'+'\n'.join(x[4:] if x.startswith('    ') else x for x in parts[1:]);need(value.strip(),'Empty endnote');notes[ident]={'text':value.rstrip('\n'),'raw':raw}
    need(not re.search(r'^\[\^[^\]]+\]:',body,re.M),'Footnote definition inside pair body')
    matches=list(MARK.finditer(body));need(matches and not body[:matches[0].start()].strip(),'No pairs or unpaired content')
    pairs=[]
    for i,m in enumerate(matches):
        meta={}
        for bit in m.group(2).split('|'):
            if not bit.strip():continue
            k,sep,v=bit.strip().partition(':');need(sep and k not in meta,'Malformed/duplicate pair metadata');meta[k]=v.strip()
        need(set(meta)==(set() if english else {'golden','role','format'}),'Incorrect pair metadata')
        raw=body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)]
        trailing='\n\n' if i+1<len(matches) or has_endnotes else '\n'
        need(raw.startswith('\n\n') and raw.endswith(trailing),'Pair framing requires blank line after marker and between pairs')
        content=raw[2:-len(trailing)]
        need('<!-- pair:' not in content and END not in content,'Malformed nested pair marker')
        pairs.append({'id':m.group(1),'metadata':meta,'text':content})
    unique(pairs,'id','pair ID');return fm,pairs,notes

def check_header(fm,pins,first,last,english=False):
    expected=parse_header(header(pins,first,last,english))
    need(fm==expected,'Front matter pin/scope mismatch or unset value')
def parse_header(text):
    return {k:v.strip() for k,v in (x.split(':',1) for x in text.split('---\n')[1].splitlines() if x)}
def source_content(rows,seg):
    amap={r['id']:r for r in rows};parts=[]
    for p in seg:parts.append(f'<!-- pair: {p["id"]} | golden: {" ".join(p["golden_ids"])} | role: {p["role"]} | format: {p["format"]} -->\n\n'+'\n'.join(amap[x]['text'] for x in p['golden_ids']))
    return '\n\n'.join(parts)+'\n'

def validate_source(root,n):
    pins,rows,changes,seg=contract(root,n);text=(directory(root,n)/'source.md').read_text();fm,pairs,notes=parse(text);check_header(fm,pins,n,n)
    need([p['id'] for p in pairs]==[p['id'] for p in seg],'Source pair order differs from segmentation')
    amap={r['id']:r for r in rows}
    for p,s in zip(pairs,seg):
        need(p['metadata']=={'golden':' '.join(s['golden_ids']),'role':s['role'],'format':s['format']},'Source marker differs from frozen segmentation')
        need(p['text']=='\n'.join(amap[x]['text'] for x in s['golden_ids']),'Source text differs from pinned golden: '+p['id'])
    return pins,rows,changes,seg,pairs

def source(root,n,draft_prior_commit=None):
    prior(root,n,draft_prior_commit);pins,rows,_,seg=contract(root,n);d=directory(root,n);data=(header(pins,n,n)+source_content(rows,seg)).encode()
    if (d/'source.md').exists():need((d/'source.md').read_bytes()==data,'Existing authored source differs; inspect instead of overwriting')
    write(d/'source.md',data);assemble(root,n,source_only=True,draft_prior_commit=draft_prior_commit);return {'chapter':n,'source_objects':len(rows),'pairs':len(seg)}

def assemble(root,n,source_only=False,draft_prior_commit=None):
    prior(root,n,draft_prior_commit);released_prefix_guard(root,n);pins=contract(root,n)[0];sources=[];english=[];notes={}
    for k in range(1,n+1):
        validate_source(root,k);d=directory(root,k);st=(d/'source.md').read_text();sources.append(st[st.find('\n---\n',4)+5:].strip('\n'))
        if not source_only:
            et=(d/'translation.md').read_text();fm,ep,en=parse(et,True);check_header(fm,pins,k,k,True)
            need(not set(notes)&set(en),'Endnote ID reused across chapters');notes.update(en)
            english.append(et[et.find('\n---\n',4)+5:].split(END)[0].strip('\n'))
    write(root/'paired/source.md',(header(pins,1,n)+'\n\n'.join(sources)+'\n').encode())
    if not source_only:write(root/'paired/translation.md',(header(pins,1,n,True)+'\n\n'.join(english)+'\n\n'+END+'\n\n'+'\n\n'.join(x['raw'] for x in notes.values())+'\n').encode())
    return {'scope_chapters':[1,n],'source_only':source_only}

def prefix(root,n,english=False):
    pins=contract(root,n)[0];filename='translation.md' if english else 'source.md';fm,pairs,notes=parse((root/'paired'/filename).read_text(),english);check_header(fm,pins,1,n,english)
    expected=[];en={}
    for k in range(1,n+1):
        sf,sp,sn=parse((directory(root,k)/filename).read_text(),english);check_header(sf,pins,k,k,english)
        expected+=sp;need(not set(en)&set(sn),'Duplicate notes across chapters');en.update(sn)
    need(pairs==expected and notes==en,'Canonical prefix differs from chapter snapshots')
    need(len({p['id'] for p in pairs})==len(pairs),'Duplicate prefix pair IDs')

def audit(root,n,rows):
    a=load(directory(root,n)/'adzom-audit.json');ids=[r['id'] for r in rows];amap={r['id']:r for r in rows}
    need(a['chapter']==n and a.get('inspector') and a.get('scope') and a.get('limits') is not None,'Incomplete native audit')
    checks=unique(a['anchor_checks'],'anchor_id','audit anchor');need(set(checks)==set(ids),'Native audit omits/adds golden objects')
    images=unique(a['images'],'image_index','audit image');pages=[r['page_hint'] for r in rows if r.get('page_hint') is not None]
    need(pages and set(images)==set(range(min(pages)+10,max(pages)+11)),'Native audit page/image coverage incomplete')
    findings=unique(a['findings'],'id','audit finding');hashes={}
    for im in images.values():
        need(set(im['anchor_ids'])<=set(ids) and im.get('status') and isinstance(im['unresolved'],list),'Invalid native image allocation')
        path=safe(root,im['path']);need(digest(path)==im['sha256'],'Native image hash mismatch');hashes[im['path']]=im['sha256']
    for ident,c in checks.items():
        need(c['status'] in {'agrees','differs','uncertain','metadata','blank'},'Invalid native check status')
        if amap[ident]['role'] not in {'blank','metadata'}:need(c['image_indices'],'Substantive source lacks native allocation')
        for i in c['image_indices']:need(i in images and ident in images[i]['anchor_ids'],'Audit image not allocated to anchor')
        need(set(c['findings'])<=set(findings),'Unknown audit finding reference')
        need(all(ident in findings[x]['anchor_ids'] for x in c['findings']),'Finding attached to unrelated anchor')
        if c['status'] in {'differs','uncertain'}:need(c['findings'],'Unresolved/differing audit lacks finding')
    obligations={}
    for f in findings.values():
        need(f['type'] in AUDIT_TYPES and f['anchor_ids'] and set(f['anchor_ids'])<=set(ids),'Invalid finding type/anchors')
        need(f.get('explanation') and f.get('english_consequence') and f.get('evidence'),'Incomplete native finding')
        need(isinstance(f['golden_reading'],str) and (f['adzom_reading'] is None or isinstance(f['adzom_reading'],str)),'Invalid exact reading fields')
        for aid in f['anchor_ids']:need(f['id'] in checks[aid]['findings'],'Finding absent from anchor check')
        allocated=set()
        need(f['golden_reading'] in '\n'.join(amap[x]['text'] for x in f['anchor_ids']),'Finding golden reading is not an exact selected span')
        for e in f['evidence']:
            need(e.get('allocation_reason') and e.get('rows_or_crop') is not None,'Evidence allocation missing')
            need(e['image_index'] in images,'Finding evidence image outside audit')
            need(set(f['anchor_ids'])&set(images[e['image_index']]['anchor_ids']),'Finding evidence misallocated')
            allocated.update(images[e['image_index']]['anchor_ids'])
            need(digest(safe(root,e['path']))==e['sha256'],'Finding evidence hash mismatch');hashes[e['path']]=e['sha256']
        need(set(f['anchor_ids'])<=allocated,'Finding evidence does not cover affected anchors')
        obligations['adzom:'+f['id']]={'golden_ids':f['anchor_ids'],'kind':'audit','type':f['type']}
    return a,obligations,hashes

def seal_audit(root,n,draft_prior_commit=None):
    if draft_prior_commit is not None:prior(root,n,draft_prior_commit)
    _,rows,changes,_=contract(root,n);d=directory(root,n);a,extra,hashes=audit(root,n,rows)
    obligations=golden_obligations(rows,changes)|extra
    obj={'chapter':n,'audit_sha256':digest(d/'adzom-audit.json'),'required_obligations':sorted(obligations),'evidence_sha256':dict(sorted(hashes.items()))}
    if (d/'audit-contract.json').exists():
        old=load(d/'audit-contract.json');need(set(old['required_obligations'])<=set(obj['required_obligations']),'Cannot remove sealed obligations')
        if (d/'signoff.json').exists():need(old==obj,'Cannot reseal signed chapter')
    write(d/'audit-contract.json',obj);write(d/'audit-contract.sha256',(digest(d/'audit-contract.json')+'\n').encode());return {'chapter':n,'obligations':len(obligations),'native_anchors':len(a['anchor_checks'])}

def notes_and_status(root,n,seg,english,definitions,obligations):
    d=directory(root,n);mapping=load(d/'note-map.json');nm=unique(mapping,'id','note ID');pm={p['id']:p for p in seg};em={p['id']:p for p in english}
    states=unique(load(d/'pair-status.json'),'id','pair status');need(set(states)==set(pm),'Pair status coverage mismatch')
    need(set(nm)==set(definitions),'Note definitions/map mismatch')
    refs={p['id']:set(REF.findall(em[p['id']]['text'])) for p in seg};covered={}
    for note in mapping:
        ident=note['id'];need(note['category'] in CATEGORIES,'Unknown note category')
        need(note['pair_ids'] and set(note['pair_ids'])<=set(pm),'Unknown/empty note pair allocation')
        need(note['golden_ids'] and set(note['golden_ids'])<=set(x for p in seg for x in p['golden_ids']),'Unknown/empty note golden allocation')
        affected={p['id'] for p in seg if set(p['golden_ids'])&set(note['golden_ids'])}
        need(affected<=set(note['pair_ids']),'Note does not link every affected pair')
        need(all(set(pm[p]['golden_ids'])&set(note['golden_ids']) for p in note['pair_ids']),'Note pair unrelated to source')
        need(all(ident in refs[p] for p in note['pair_ids']),'Required note marker missing from affected pair')
        for obligation in note['obligations']:
            need(obligation in obligations and obligation not in covered,'Unknown/duplicate note obligation')
            required=obligations[obligation];need(set(required['golden_ids'])<=set(note['golden_ids']),'Obligation source not covered by note')
            if required['kind']=='audit':need(note['category']==required['type'],'Audit finding misclassified in reader notes')
            if required['kind']=='change' and required['changed_text']:
                need(note['category'] in {'transcript_correction','adzom_difference','uncertain_reading'},'Transcript correction confused with presentation/source layer')
            covered[obligation]=ident
    need(set(covered)==set(obligations),'Required golden/audit endnote obligations missing')
    for ident,state in states.items():
        text=em[ident]['text'];need(text.strip(),'Empty English pair: '+ident)
        need(not re.search(r'\b(?:TODO|TBD|PLACEHOLDER|UNSET)\b',text,re.I),'Placeholder English pair: '+ident)
        need(re.search(r'[A-Za-z]',text),'English or explicit English treatment missing')
        need(state['status'] in {'translated','unresolved','nontranslatable'} and state.get('reason'),'Invalid pair treatment')
        need(set(state['note_ids'])==refs[ident],'Pair status note references mismatch')
        need(refs[ident]<=set(nm),'Undefined footnote reference')
        need(all(ident in nm[x]['pair_ids'] for x in refs[ident]),'Footnote reference outside note allocation')
        if state['status']!='translated':
            if pm[ident]['role'] in {'blank','metadata','source_metadata'}:need('[' in text and ']' in text,'Metadata requires explicit nontranslatable label')
            else:need(refs[ident],'Unresolved/nontranslatable substantive pair lacks local endnote')
    return mapping,states

def released_prefix_guard(root,n):
    if n==1:return
    for filename,english in [('source.md',False),('translation.md',True)]:
        _,current,notes=parse((root/'paired'/filename).read_text(),english)
        expected=[];oldnotes={}
        for k in range(1,n):
            _,pairs,defs=parse((directory(root,k)/filename).read_text(),english);expected+=pairs;oldnotes.update(defs)
        need(current[:len(expected)]==expected,'Previously released canonical pair content changed')
        need(all(notes.get(i)==v for i,v in oldnotes.items()),'Previously released canonical endnote changed')

def candidate(root,n,draft_prior_commit=None):
    prior(root,n,draft_prior_commit);pins,rows,changes,seg,sp=validate_source(root,n);prefix(root,n);prefix(root,n,True);d=directory(root,n)
    fm,ep,defs=parse((d/'translation.md').read_text(),True);check_header(fm,pins,n,n,True)
    need([p['id'] for p in sp]==[p['id'] for p in ep],'Source/English pair symmetry mismatch')
    native,extra,evidence_hashes=audit(root,n,rows);obligations=golden_obligations(rows,changes)|extra
    seal=load(d/'audit-contract.json');need(digest(d/'audit-contract.json')==(d/'audit-contract.sha256').read_text().strip(),'Audit contract changed')
    need(seal['chapter']==n and seal['audit_sha256']==digest(d/'adzom-audit.json') and seal['required_obligations']==sorted(obligations) and seal['evidence_sha256']==dict(sorted(evidence_hashes.items())),'Native findings/evidence changed after seal')
    note_map,states=notes_and_status(root,n,seg,ep,defs,obligations)
    english={p['id']:p['text'] for p in ep};objects=[];amap={r['id']:r for r in rows}
    reader=[f'# String of Pearls — chapter {n}', '', 'English working translation of fixed `golden-v1`. Source uncertainties and Adzom comparisons are explained in the endnotes. Mechanical validation does not certify semantic accuracy.','']
    bilingual=[f'# String of Pearls — chapter {n}: paired reading','']
    for p,s in zip(sp,seg):
        ident=p['id'];text=english[ident];fmt=s['format'];role=s['role'];objects.append({'id':ident,'golden_ids':s['golden_ids'],'golden_objects':[amap[x] for x in s['golden_ids']],'role':role,'format':fmt,'source':p['text'],'translation':text,'status':states[ident]['status'],'reason':states[ident]['reason'],'note_ids':states[ident]['note_ids']})
        reader.append(f'<a id="{ident.lower()}"></a>')
        display=('#'*int(fmt[1])+' '+text) if fmt.startswith('h') else (text.replace('\n','  \n') if fmt=='verse' else text)
        if role in {'annotation','source_annotation','colophon','work_colophon','chapter_colophon','metadata','source_metadata','blank'}:display=f'> [{role}] '+display.replace('\n','\n> ')
        reader.extend([display,''])
        bilingual.extend([f'<!-- pair: {ident}; format: {fmt}; role: {role} -->',p['text'],'',text,''])
    endnotes=['## Endnotes','']+[v['raw'] for v in defs.values()]+['']
    reader+=endnotes;bilingual+=endnotes
    coverage={'chapter':n,'scope':'Only this chapter; canonical paired files cover the contiguous released/active prefix.',
              'pairs':len(seg),'golden_objects':len(rows),'source_objects_remaining_in_chapter':0,'paired_prefix_last_chapter':n,
              'formats':dict(Counter(p['format'] for p in seg)),'statuses':dict(Counter(x['status'] for x in states.values())),
              'note_count':len(defs),'obligations_required':len(obligations),'obligations_covered':len(obligations),'obligations_remaining':0,
              'native_anchor_checks':len(native['anchor_checks']),'native_images':len(native['images']),'native_findings':len(native['findings']),
              'golden_uncertainty_statements':sum(len(r['uncertainty']) for r in rows),'golden_changes':len(changes),
              'source_roles':dict(Counter(r['role'] for r in rows)),'closing_objects':sum(r['role'] in {'colophon','chapter_colophon'} for r in rows),
              'supporting_records':{name:(d/name).exists() for name in ('usage.json','glossary-proposals.json')},'claims':CLAIMS}
    machine={'chapter':n,'source_pins':pins,'pairs':objects,'endnotes':[{'id':i,**v} for i,v in defs.items()],'note_map':note_map,'claims':CLAIMS}
    outputs={'reading.md':('\n'.join(reader)+'\n').encode(),'bilingual.md':('\n'.join(bilingual)+'\n').encode(),'machine.json':encoded(machine),'coverage.json':encoded(coverage)}
    names=['source.md','translation.md','segmentation.json','contract.json','contract.sha256','note-map.json','pair-status.json','adzom-audit.json','audit-contract.json','audit-contract.sha256']
    names += [x for x in ('usage.json','glossary-proposals.json','translation-note-map.json','translation-draft.md') if (d/x).exists()]
    inputs={str((d/name).relative_to(root)):digest(d/name) for name in names};inputs.update(evidence_hashes)
    continuation=load(d/'contract.json').get('draft_continuation')
    if continuation:inputs[continuation['path']]=continuation['sha256']
    inputs.update({'golden/reading.json':pins['source_reading_sha256'],pins['glossary']:pins['glossary_sha256'],pins['standard']:pins['standard_sha256']})
    manifest={'chapter':n,'source_pins':pins,'input_sha256':dict(sorted(inputs.items())),'output_sha256':{name:sha(outputs[name]) for name in OUTPUTS},
              'builder':'scripts/translation_pipeline.py; deterministic chapter outputs; canonical pair blocks and endnotes are mirrored exactly.','claims':CLAIMS}
    outputs['build-manifest.json']=encoded(manifest);return outputs

def build(root,n,draft_prior_commit=None):
    outputs=candidate(root,n,draft_prior_commit);d=directory(root,n)
    if (d/'signoff.json').exists():need(all((d/k).is_file() and (d/k).read_bytes()==v for k,v in outputs.items()),'Refusing to alter signed translation')
    for name,data in outputs.items():write(d/name,data)
    return {'chapter':n,'outputs':len(outputs),'build_manifest_sha256':digest(d/'build-manifest.json')}

def final_gate(root,n):
    d=directory(root,n);need((d/'signoff.json').exists(),'Unsigned translation: final signoff missing')
    q=load(d/'qc.json');s=load(d/'signoff.json');m=load(d/'build-manifest.json')
    need(q['chapter']==n and q['independent'] is True and q['reviewer'] and q['translator'] and q['reviewer']!=q['translator'],'Independent QC identity missing')
    need(q['source_sha256']==digest(d/'source.md') and q['translation_sha256']==digest(d/'translation.md') and q['build_manifest_sha256']==digest(d/'build-manifest.json'),'QC bound to obsolete draft')
    need(q['coverage']=='complete' and q['disposition'] in {'ready_for_human_editing','ready_with_explicit_review_flags'} and q['open_blockers']==[],'QC incomplete or blockers open')
    need(digest(safe(root,q['review_path']))==q['review_sha256'],'QC review hash mismatch')
    need(s['chapter']==n and s['approved'] is True and s['reviewer'],'Incomplete signoff')
    need(s['build_manifest_sha256']==digest(d/'build-manifest.json') and s['output_sha256']==m['output_sha256'] and s['qc_sha256']==digest(d/'qc.json'),'Signoff hash binding mismatch')
    need(digest(safe(root,s['review_path']))==s['review_sha256'],'Final review hash mismatch')

def validate(root,n,source_only=False,final=False,draft_prior_commit=None):
    need(not (source_only and final),'Source-only and final modes are incompatible')
    need(not (final and draft_prior_commit is not None),'Draft continuation cannot be used for final validation or release')
    prior(root,n,draft_prior_commit)
    if source_only:
        pins,rows,_,seg,_=validate_source(root,n);prefix(root,n)
        return {'chapter':n,'mode':'draft-source' if draft_prior_commit else 'source','passed':True,'pairs':len(seg),'golden_objects':len(rows),'english_required':False}
    expected=candidate(root,n,draft_prior_commit);d=directory(root,n)
    for name,data in expected.items():need((d/name).is_file() and (d/name).read_bytes()==data,'Output corruption/nonreproducible translation: '+name)
    if final:final_gate(root,n)
    if n==8:
        _,ps,_=parse((root/'paired/source.md').read_text());need(sum(len(p['metadata']['golden'].split()) for p in ps)==2053,'Whole-book coverage is not 2,053')
    return {'chapter':n,'mode':'final' if final else 'draft-candidate' if draft_prior_commit else 'candidate','passed':True,'read_only':True,'build_manifest_sha256':digest(d/'build-manifest.json'),'claims':CLAIMS}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('command',choices=['plan','source','seal-audit','assemble','build','validate']);p.add_argument('--chapter',type=int,required=True);p.add_argument('--source-only',action='store_true');p.add_argument('--final',action='store_true');p.add_argument('--draft-prior-commit',help='Chapter 3, 4, 5, 6, 7 or 8 working continuation under its committed authorization; forbidden with --final');a=p.parse_args()
    try:
        need(not (a.final and a.draft_prior_commit is not None),'Draft continuation cannot be used for final validation or release')
        if a.command=='validate':result=validate(a.root,a.chapter,a.source_only,a.final,a.draft_prior_commit)
        elif a.command=='assemble':result=assemble(a.root,a.chapter,a.source_only,a.draft_prior_commit)
        else:result={'plan':plan,'source':source,'seal-audit':seal_audit,'build':build}[a.command](a.root,a.chapter,a.draft_prior_commit)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (Error,OSError,KeyError,TypeError,json.JSONDecodeError) as exc:print('TRANSLATION VALIDATION ERROR: '+str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
