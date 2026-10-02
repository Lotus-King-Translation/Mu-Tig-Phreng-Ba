#!/usr/bin/env python3
"""Attach recorded source apparatus to a translation draft, preserving that draft.

This formats authored golden/audit records; it does not infer Tibetan readings,
translate uncertain source text, or certify that the notes are semantically right.
The coordinator must review the resulting canonical English and note allocations.
"""
import argparse
import json
from pathlib import Path
import re
import translation_pipeline as tp

ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/blob/'

def run(n):
    d=tp.directory(ROOT,n)
    original=d/'translation-draft.md'
    tp.need(not original.exists(),'Draft archive already exists; revise canonical notes explicitly instead of regenerating')
    draft=(d/'translation.md').read_text()
    fm,pairs,definitions=tp.parse(draft,True)
    seg=json.loads((d/'segmentation.json').read_text())
    rows=json.loads((ROOT/f'diplomatic/chapters/{n:02}/reading.json').read_text())['objects']
    changes=json.loads((ROOT/f'diplomatic/chapters/{n:02}/changes.json').read_text())['changes']
    evidence={e['id']:e for e in json.loads((ROOT/f'diplomatic/chapters/{n:02}/evidence.json').read_text())}
    audit=json.loads((d/'adzom-audit.json').read_text())
    mapping=json.loads((d/'translation-note-map.json').read_text())
    texts={p['id']:p['text'] for p in pairs}
    source={r['id']:r for r in rows}
    byanchor={aid:p['id'] for p in seg for aid in p['golden_ids']}
    def append(ident,aids,category,obligations,body):
        tp.need(ident not in definitions,'New note ID collides with translator note')
        pids=list(dict.fromkeys(byanchor[x] for x in aids))
        for pid in pids: texts[pid]+='[^'+ident+']'
        definitions[ident]={'raw':f'[^{ident}]: '+body.replace('\n','\n    ')}
        mapping.append({'id':ident,'pair_ids':pids,'golden_ids':aids,'category':category,'obligations':obligations})
    def link(e,version):
        return f'[Adzom p. {e["image_index"]-10}, image {e["image_index"]}]({BASE}{version}/{e["path"]})'
    bychange={c['anchor_id']:c for c in changes}
    for row in rows:
        aid=row['id'];c=bychange.get(aid);uncertainty=row['uncertainty']
        if not c and not uncertainty: continue
        ident=f'CH{n:02}-G{int(aid[-6:]):06}'
        obligations=[];parts=[f'Golden editorial record, {aid}.']
        if c:
            obligations.append('golden-change:'+c['id'])
            if c['old']!=c['new']:
                category='transcript_correction'
                parts += [f'Transcript correction: `{c["old"]}` → `{c["new"]}`.',
                          'Golden v1 recorded this as a scan-supported correction to the electronic transcript, intended to follow Adzom. The current local Adzom audit note, where present, records any newly observed difference or uncertainty.',c['reason']]
            else:
                category='source_layer'
                parts += [f'Unchanged Tibetan: `{c["new"]}`.',f'Editorial treatment: {c["treatment"]}; source role: {c["role"]}.',c['reason']]
            parts.append('Evidence: '+', '.join(link(evidence[x],'golden-v1') for x in c['evidence_ids'])+'.')
        else:
            category='golden_uncertainty';parts.append(f'Golden Tibetan: `{row["text"]}`.')
        for i,u in enumerate(uncertainty):
            obligations.append(f'golden-uncertainty:{aid}:{i}');parts.append('Retained source qualification: '+u)
        if uncertainty: parts.append('Working treatment: translate only the fixed golden wording; do not silently supply the untranscribed layer. See the local Adzom audit notes for newly examined evidence. Review action: resolve the stated source or allocation question before a critical edition.')
        append(ident,[aid],category,obligations,' '.join(parts))
    for f in audit['findings']:
        ident=f['id'];aids=f['anchor_ids']
        label=f['type'].replace('_',' ')
        parts=[f'{label.capitalize()}; source anchors '+', '.join(aids)+'.']
        if f['type']!='presentation':
            parts.append(f'Golden reading: `{f["golden_reading"]}`.' if f['golden_reading'] else 'Golden reading: no corresponding text.')
            parts.append(f'Adzom reading: `{f["adzom_reading"]}`.' if f['adzom_reading'] is not None else 'Adzom wording: not fully transcribed or not securely resolved.')
        parts += [f['explanation'], 'English consequence: '+f['english_consequence']]
        refs=[]
        for e in f['evidence']:
            refs.append(link(e,'main')+'; '+str(e['rows_or_crop']))
        parts.append('Evidence: '+'; '.join(refs)+'.')
        append(ident,aids,f['type'],['adzom:'+f['id']],' '.join(parts))
    body='\n\n'.join(f'<!-- pair: {p["id"]} -->\n\n'+texts[p['id']] for p in pairs)
    result=tp.header(tp.contract(ROOT,n)[0],n,n,True)+body+'\n\n'+tp.END+'\n\n'+'\n\n'.join(v['raw'] for v in definitions.values())+'\n'
    states=json.loads((d/'pair-status.json').read_text())
    for state in states:state['note_ids']=list(dict.fromkeys(tp.REF.findall(texts[state['id']])))
    original.write_text(draft)
    (d/'translation.md').write_text(result)
    tp.write(d/'note-map.json',mapping);tp.write(d/'pair-status.json',states)
    return {'chapter':n,'pairs':len(pairs),'endnotes':len(definitions),'draft_archive':str(original.relative_to(ROOT))}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--chapter',type=int,required=True)
    print(json.dumps(run(ap.parse_args().chapter),indent=2))
