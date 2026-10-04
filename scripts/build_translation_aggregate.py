#!/usr/bin/env python3
"""Build/verify the complete translation only from eight fixed chapter releases."""
from __future__ import annotations
import argparse
from collections import Counter
import copy
import json
from pathlib import Path
import re
import sys
import translation_pipeline as t

ROOT=Path(__file__).resolve().parents[1]
CHAPTERS=8
OBJECTS=2053
OUTPUTS=('reading.md','bilingual.md','machine.json','coverage.json')
LIMITS=[
    'Agent-produced English working translation for human review; no independent human certification.',
    'All golden objects are represented; represented does not mean every reading or interpretation is resolved.',
    'Native main-text audits retain local unreadable and untranscribed source-layer limits; complete commentary decipherment is not claimed.',
    'Mechanical validation proves structure and provenance, not semantic correctness.',
    'The fixed golden Tibetan and canonical glossary remain unchanged; provisional usages do not amend the glossary.',
]

def required_releases(root):
    for n in range(1,CHAPTERS+1):
        d=t.directory(root,n)
        t.need(d.is_dir(),f'Missing translation chapter {n}')
        for name in ('source.md','translation.md','machine.json','coverage.json','build-manifest.json','qc.json','signoff.json'):
            t.need((d/name).is_file(),f'Chapter {n}: missing {name}')
        t.need((root/f'translations/publication/ch{n:02}-v1.json').is_file(),f'Chapter {n}: publication receipt required')

def tagged_hash(root,tag,rel):
    path=t.safe(root,rel);raw=t.git(root,'show',tag+':'+rel)
    lfs=re.fullmatch(rb'version https://git-lfs.github.com/spec/v1\noid sha256:([0-9a-f]{64})\nsize ([0-9]+)\n',raw)
    if lfs:
        t.need(t.digest(path)==lfs.group(1).decode() and path.stat().st_size==int(lfs.group(2)),'Changed released LFS bytes: '+rel)
    else:t.need(path.read_bytes()==raw,'Changed released bytes: '+rel)
    return t.digest(path)

def chapter(root,n):
    pins,rows,changes,seg,source=t.validate_source(root,n);d=t.directory(root,n)
    fm,english,definitions=t.parse((d/'translation.md').read_text(),True);t.check_header(fm,pins,n,n,True)
    t.need([x['id'] for x in source]==[x['id'] for x in english],f'Chapter {n}: pair symmetry mismatch')
    native,additional,evidence=t.audit(root,n,rows);obligations=t.golden_obligations(rows,changes)|additional
    seal=t.load(d/'audit-contract.json')
    t.need(t.digest(d/'audit-contract.json')==(d/'audit-contract.sha256').read_text().strip(),'Audit seal hash changed')
    t.need(seal=={'chapter':n,'audit_sha256':t.digest(d/'adzom-audit.json'),'required_obligations':sorted(obligations),'evidence_sha256':dict(sorted(evidence.items()))},'Audit seal/obligations changed')
    mapping,states=t.notes_and_status(root,n,seg,english,definitions,obligations)
    machine=t.load(d/'machine.json');coverage=t.load(d/'coverage.json');manifest=t.load(d/'build-manifest.json')
    t.need(machine['chapter']==coverage['chapter']==manifest['chapter']==n,'Chapter payload identity mismatch')
    t.need(machine['source_pins']==manifest['source_pins']==pins,'Chapter source pins differ')
    amap={r['id']:r for r in rows};expected=[]
    for sp,ep,p in zip(source,english,seg):
        ident=sp['id'];state=states[ident]
        expected.append({'id':ident,'golden_ids':p['golden_ids'],'golden_objects':[amap[x] for x in p['golden_ids']],
                         'role':p['role'],'format':p['format'],'source':sp['text'],'translation':ep['text'],
                         'status':state['status'],'reason':state['reason'],'note_ids':state['note_ids']})
    t.need(machine['pairs']==expected,'Released machine pair differs from canonical source/English')
    t.need(machine['endnotes']==[{'id':i,**v} for i,v in definitions.items()] and machine['note_map']==mapping,'Released machine note differs from canonical endnote/map')
    counters={'pairs':len(seg),'golden_objects':len(rows),'source_objects_remaining_in_chapter':0,
              'note_count':len(definitions),'obligations_required':len(obligations),'obligations_covered':len(obligations),'obligations_remaining':0,
              'native_anchor_checks':len(native['anchor_checks']),'native_images':len(native['images']),'native_findings':len(native['findings']),
              'golden_uncertainty_statements':sum(len(r['uncertainty']) for r in rows),'golden_changes':len(changes),
              'closing_objects':sum(r['role'] in {'colophon','chapter_colophon'} for r in rows)}
    for key,value in counters.items():t.need(coverage[key]==value,'Coverage mismatch: '+key)
    for key,actual in [('formats',Counter(p['format'] for p in seg)),('statuses',Counter(s['status'] for s in states.values())),('source_roles',Counter(r['role'] for r in rows))]:
        t.need(coverage[key]==dict(actual),'Coverage category mismatch: '+key)
    t.need(machine['claims']==coverage['claims']==manifest['claims']==t.CLAIMS,'Unsupported certification claim')
    for name,value in manifest['input_sha256'].items():t.need(t.digest(t.safe(root,name))==value,'Changed manifest input: '+name)
    t.need(set(manifest['output_sha256'])==set(OUTPUTS),'Chapter output manifest incomplete')
    for name,value in manifest['output_sha256'].items():t.need(t.digest(d/name)==value,'Changed manifest output: '+name)
    t.final_gate(root,n)
    return {'chapter':n,'pins':pins,'source_pairs':source,'english_pairs':english,'pairs':machine['pairs'],'endnotes':machine['endnotes'],
            'note_map':mapping,'coverage':coverage,'native':native,'obligations':sorted(obligations)}

def verify_sequence(chapters,golden,source_pairs,english_pairs,definitions):
    t.need([c['chapter'] for c in chapters]==list(range(1,CHAPTERS+1)),'Missing/reordered chapters')
    pairs=[p for c in chapters for p in c['pairs']];ids=[p['id'] for p in pairs]
    t.need(len(ids)==len(set(ids)),'Duplicate aggregate pair ID')
    t.need(ids==[p['id'] for p in source_pairs]==[p['id'] for p in english_pairs],'Aggregate canonical pair order mismatch')
    original=[g for p in pairs for g in p['golden_objects']]
    t.need(original==golden and len(original)==OBJECTS,'Golden objects changed, missing, duplicated or reordered')
    t.need([i for p in pairs for i in p['golden_ids']]==[r['id'] for r in golden],'Golden object references differ')
    t.need(len({r['id'] for r in original})==OBJECTS,'Duplicate golden object ID')
    for pair,sp,ep in zip(pairs,source_pairs,english_pairs):
        t.need(pair['source']==sp['text'] and pair['translation']==ep['text'],'Changed canonical pair text')
        t.need(sp['metadata']=={'golden':' '.join(pair['golden_ids']),'role':pair['role'],'format':pair['format']},'Changed canonical pair metadata')
    notes=[n for c in chapters for n in c['endnotes']];nids=[n['id'] for n in notes]
    t.need(len(nids)==len(set(nids)),'Duplicate aggregate endnote ID')
    t.need(nids==list(definitions),'Canonical endnote order differs from fixed chapters')
    for note in notes:t.need({k:v for k,v in note.items() if k!='id'}==definitions[note['id']],'Changed canonical endnote definition')
    return pairs,notes

def collect(root):
    required_releases(root)  # Nothing is generated until all eight gates exist.
    t.prior(root,CHAPTERS+1)  # Annotated tags, receipts, all tagged bytes/inputs and final QC/signoffs.
    t.prefix(root,CHAPTERS);t.prefix(root,CHAPTERS,True)
    _,sp,_=t.parse((root/'paired/source.md').read_text());_,ep,defs=t.parse((root/'paired/translation.md').read_text(),True)
    chapters=[chapter(root,n) for n in range(1,CHAPTERS+1)]
    t.need(all(c['pins']==chapters[0]['pins'] for c in chapters),'Chapters use different source/glossary versions')
    golden=t.load(root/'golden/reading.json')['objects'];pairs,notes=verify_sequence(chapters,golden,sp,ep,defs)
    gr=t.load(root/'diplomatic/publication/golden-v1.json');pins=chapters[0]['pins']
    t.need(gr['tag']==pins['source_tag'] and gr['release_commit']==gr['remote_peeled_commit']==gr['remote_main_at_release']==pins['source_commit'],'Golden receipt identity mismatch')
    t.need(t.git(root,'cat-file','-t','refs/tags/golden-v1').strip()==b'tag','Golden tag is not annotated')
    t.need(t.git(root,'rev-parse','refs/tags/golden-v1').decode().strip()==gr['remote_tag_object'],'Golden tag object differs from publication receipt')
    inputs={};releases=[]
    for c in chapters:
        n=c['chapter'];d=t.directory(root,n);receipt_path=root/f'translations/publication/ch{n:02}-v1.json';receipt=t.load(receipt_path);tag=receipt['tag']
        t.need(receipt['coverage_sha256']==t.digest(d/'coverage.json'),'Receipt coverage hash changed')
        manifest=t.load(d/'build-manifest.json');prefix=d.relative_to(root).as_posix()+'/'
        paths={p.decode() for p in t.git(root,'ls-tree','-rz','--name-only',tag,'--',prefix).split(b'\0') if p}
        paths.update(manifest['input_sha256'])
        for name in ('qc.json','signoff.json'):paths.add(t.load(d/name)['review_path'])
        for rel in sorted(paths):
            value=tagged_hash(root,tag,rel)
            t.need(rel not in inputs or inputs[rel]==value,'Shared release input mismatch: '+rel);inputs[rel]=value
        inputs[receipt_path.relative_to(root).as_posix()]=t.digest(receipt_path)
        releases.append({'chapter':n,'tag':tag,'tag_object':receipt['remote_tag_object'],'peeled_commit':receipt['release_commit'],
                         'receipt':receipt_path.relative_to(root).as_posix(),'receipt_sha256':t.digest(receipt_path),
                         'build_manifest_sha256':t.digest(d/'build-manifest.json'),'qc_sha256':t.digest(d/'qc.json'),'signoff_sha256':t.digest(d/'signoff.json')})
    for name in ('paired/source.md','paired/translation.md','diplomatic/publication/golden-v1.json'):
        inputs[name]=t.digest(root/name)
    return chapters,pairs,notes,releases,inputs

def display(text,fmt,role):
    shown='#'*int(fmt[1])+' '+text.replace('\n',' ') if fmt.startswith('h') else (text.replace('\n','  \n') if fmt=='verse' else text)
    if role in {'annotation','source_annotation','colophon','work_colophon','chapter_colophon','metadata','source_metadata','blank'}:
        shown=f'> [{role}] '+shown.replace('\n','\n> ')
    return shown

def render(chapters,notes,bilingual=False):
    title='String of Pearls — Tibetan and English' if bilingual else 'String of Pearls — English working translation'
    lines=['# '+title,'','Eight fixed chapter releases, translated from `golden-v1`. All source comparisons and unresolved readings remain in the endnotes.','',
           'This is an agent-produced working translation for human review. [Fixed Tibetan source and attribution](../golden/README.md); [coverage and limits](coverage.json).','']
    for c in chapters:
        n=c['chapter'];lines += [f'## Chapter {n}','',f'[Fixed chapter release](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch{n:02}-v1)','']
        for p in c['pairs']:
            lines.append(f'<a id="{p["id"].lower()}"></a>')
            if bilingual:
                lines.extend([f'<!-- pair: {p["id"]}; format: {p["format"]}; role: {p["role"]} -->','',
                              display(p['source'],p['format'],p['role']),''])
            lines.extend([display(p['translation'],p['format'],p['role']),''])
    lines.extend(['## Endnotes',''])
    for note in notes:lines.extend([note['raw'],''])
    return ('\n'.join(lines)+'\n').encode()

def generate(root):
    chapters,pairs,notes,releases,inputs=collect(root)
    counters=('pairs','golden_objects','source_objects_remaining_in_chapter','note_count','obligations_required','obligations_covered','obligations_remaining','native_anchor_checks','native_images','native_findings','golden_uncertainty_statements','golden_changes','closing_objects')
    totals={key:sum(c['coverage'][key] for c in chapters) for key in counters}
    images={};objects_by_status=Counter()
    for c in chapters:
        for image in c['native']['images']:
            ident=image['image_index'];value=image['sha256'];t.need(ident not in images or images[ident]==value,'Native image identity differs across chapters');images[ident]=value
    for p in pairs:objects_by_status[p['status']]+=len(p['golden_ids'])
    coverage={'edition':'translation-v1','chapters_released':CHAPTERS,'source_objects_represented':OBJECTS,
              'source_objects_remaining':0,'source_objects_by_pair_treatment':dict(objects_by_status),'totals':totals,
              'pair_statuses':dict(Counter(p['status'] for p in pairs)),'formats':dict(Counter(p['format'] for p in pairs)),
              'unique_native_images':len(images),'chapter_coverage':[{'chapter':c['chapter'],'coverage':c['coverage']} for c in chapters],
              'limits':LIMITS,'claims':t.CLAIMS,
              'count_note':'Represented objects include explicitly unresolved and nontranslatable pairs. Native-image and evidence counts may overlap between chapters; no accuracy percentage is inferred.'}
    machine={'edition':'translation-v1','source_pins':chapters[0]['pins'],
             'chapter_boundaries':[{'chapter':c['chapter'],'first_pair':c['pairs'][0]['id'],'last_pair':c['pairs'][-1]['id'],'pair_count':len(c['pairs'])} for c in chapters],
             'pairs':copy.deepcopy(pairs),'endnotes':copy.deepcopy(notes),'note_map':[copy.deepcopy(n) for c in chapters for n in c['note_map']],
             'chapter_obligations':[{'chapter':c['chapter'],'obligations':c['obligations']} for c in chapters],'claims':t.CLAIMS}
    outputs={'reading.md':render(chapters,notes),'bilingual.md':render(chapters,notes,True),'machine.json':t.encoded(machine),'coverage.json':t.encoded(coverage)}
    inputs['scripts/build_translation_aggregate.py']=t.digest(Path(__file__))
    inputs['scripts/translation_pipeline.py']=t.digest(Path(t.__file__))
    manifest={'edition':'translation-v1','source_pins':chapters[0]['pins'],'input_sha256':dict(sorted(inputs.items())),
              'chapter_releases':releases,'output_sha256':{name:t.sha(outputs[name]) for name in OUTPUTS},'claims':t.CLAIMS,
              'method':'Exact fixed-chapter/canonical pair and note identity; display-only Markdown projection; no editorial rewriting. Fresh remote-ref verification is a separate final publication gate.'}
    outputs['build-manifest.json']=t.encoded(manifest);return outputs

def build(root):
    outputs=generate(root);dest=root/'translations'
    if (dest/'signoff.json').exists():t.need(all((dest/k).is_file() and (dest/k).read_bytes()==v for k,v in outputs.items()),'Refusing to change signed translation aggregate')
    for name,data in outputs.items():t.write(dest/name,data)
    return {'outputs':len(outputs),'chapters':CHAPTERS,'source_objects_represented':OBJECTS,'build_manifest_sha256':t.digest(dest/'build-manifest.json')}

def verify(root):
    expected=generate(root)
    for name,data in expected.items():t.need((root/'translations'/name).is_file() and (root/'translations'/name).read_bytes()==data,'Aggregate corruption/nonreproducible output: '+name)
    return {'passed':True,'read_only':True,'chapters':CHAPTERS,'source_objects_represented':OBJECTS,'build_manifest_sha256':t.digest(root/'translations/build-manifest.json')}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('command',choices=['build','verify']);a=p.parse_args()
    try:print(json.dumps(build(a.root) if a.command=='build' else verify(a.root),indent=2));return 0
    except (t.Error,OSError,KeyError,TypeError,json.JSONDecodeError) as exc:print('TRANSLATION AGGREGATE ERROR: '+str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
