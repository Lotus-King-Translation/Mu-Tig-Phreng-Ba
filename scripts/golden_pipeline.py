#!/usr/bin/env python3
"""Source-exact, bounded golden edition builder. Never performs editorial repair."""
from __future__ import annotations
import argparse
import copy
import difflib
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = 'editions/research/etexts-translations/wikisource/tibetan-raw.wiki'
COMPARE = 'editions/research/etexts-translations/wikisource/wylie-raw.wiki'
BASE_HASH = '3d888d525c101b879a5d866b63090b6e5aac91ba5a613d58328ccdb86d66f00b'
COMPARE_HASH = 'd26075bd2a164238d3c68a47a68e821a58d10092f9943350b4fefa8b6c5e3cdb'
PREPARED = ('source-anchors.json', 'electronic-collation.json', 'chapter-map.json', 'anomalies.json')
OUTPUTS = ('reading.md', 'reading.json', 'apparatus.json', 'changes.json', 'coverage.json')
ROLES = {'main_text', 'heading', 'chapter_colophon', 'colophon', 'annotation', 'graphic', 'metadata', 'blank', 'unresolved'}
TREATMENTS = {'retain_base', 'retain_with_uncertainty', 'scan_supported_correction', 'separate_source_layer', 'classify_layer', 'display_only', 'defer_outside_scope'}
CLAIMS = {'full_scan_proofreading': False, 'exhaustive_witness_collation': False,
          'independent_witness_electronic_collation': False, 'independent_human_certification': False}

class ValidationError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise ValidationError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_hash(path):
    return sha(path.read_bytes())

def serialized(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def write(path, data, frozen=False):
    blob = data if isinstance(data, bytes) else serialized(data)
    if frozen and path.exists():
        require(path.read_bytes() == blob, f'Refusing to alter frozen file: {path}')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(blob)

def relative(root, path):
    return str(path.resolve().relative_to(root.resolve()))

def safe_path(root, rel):
    path = (root / rel).resolve()
    require(path.is_relative_to(root.resolve()), f'Path escapes repository: {rel}')
    require(path.is_file(), f'Missing evidence/input: {rel}')
    return path

def payload(root, rel, expected):
    path = root / rel
    raw = path.read_bytes()
    require(sha(raw) == expected, f'Archival source changed: {rel}')
    source = raw.decode('utf-8')
    require(source.count('<poem>') == 1 and source.count('</poem>') == 1, f'Nonunique payload: {rel}')
    start = source.index('<poem>') + len('<poem>')
    end = source.index('</poem>', start)
    return source, start, end, source[start:end].splitlines(keepends=True)

def unline(value):
    text = value.rstrip('\r\n')
    return text, value[len(text):]

def opcode_records(a, b):
    return [{'tag': tag, 'base_start': i, 'base_end': j, 'comparison_start': k,
             'comparison_end': l, 'old': a[i:j], 'new': b[k:l]}
            for tag, i, j, k, l in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()]

def reconstruct(a, ops):
    out, pos, comp_pos = [], 0, 0
    for op in ops:
        require(op['base_start'] == pos and op['comparison_start'] == comp_pos, 'Noncontiguous comparison opcodes')
        require(a[op['base_start']:op['base_end']] == op['old'], 'Opcode old slice mismatch')
        require(op['base_end'] >= pos and op['comparison_end'] >= comp_pos, 'Reversed opcode')
        require(op['comparison_end'] - op['comparison_start'] == len(op['new']), 'Opcode comparison extent mismatch')
        require(op['tag'] in {'equal', 'replace', 'delete', 'insert'}, 'Unknown opcode tag')
        if op['tag'] == 'equal':
            require(op['old'] == op['new'], 'False equality opcode')
        out.append(op['new']); pos = op['base_end']; comp_pos = op['comparison_end']
    require(pos == len(a), 'Opcodes fail to cover base')
    return ''.join(out)

def preparation(root):
    import pyewts
    require(importlib.metadata.version('pyewts') == '0.2.0', 'Use pinned pyewts==0.2.0')
    base, bs, be, blines = payload(root, BASE, BASE_HASH)
    wylie, ws, we, wlines = payload(root, COMPARE, COMPARE_HASH)
    require(len(blines) == len(wlines), 'Unequal line counts require authored alignment')
    converter = pyewts.pyewts(fix_spacing=False)
    anchors, loci, anomalies, boundaries = [], [], [], []
    bpos, wpos, page = bs, ws, None
    for number, (braw, wraw) in enumerate(zip(blines, wlines), 1):
        aid = f'MTP-S{number:06}'
        text, ending = unline(braw)
        wt, _ = unline(wraw)
        warnings = []
        derived = converter.toUnicode(wraw, warnings)
        if not wt.strip():
            role = 'blank'
        elif wt.isdecimal():
            role = 'metadata'; page = int(wt)
        elif re.fullmatch(r'@\d+', wt):
            role = 'metadata'
        elif "le'u ste" in wt:
            role = 'chapter_colophon'; boundaries.append(number)
        else:
            role = 'main_text'
        anchors.append({'id': aid, 'index': number, 'text': text, 'line_ending': ending,
                        'raw_text': braw, 'raw_start': bpos, 'raw_end': bpos + len(braw),
                        'payload_start': bpos-bs, 'payload_end': bpos-bs+len(braw),
                        'wylie_raw_text': wraw, 'wylie_start': wpos, 'wylie_end': wpos+len(wraw),
                        'mechanical_role': role, 'page_hint': page,
                        'scan_image_hint': page+10 if page else None})
        locus = {'id': f'MTP-L{number:06}', 'anchor_id': aid, 'base': braw,
                 'wylie': wraw, 'derived_tibetan': derived, 'warnings': warnings,
                 'equal': braw == derived, 'opcodes': opcode_records(braw, derived)}
        loci.append(locus)
        if warnings and wt.strip():
            anomalies.append({'id': f'MTP-A{number:06}-EWTS', 'anchor_id': aid,
                              'kind': 'conversion_warning', 'details': warnings,
                              'meaning': 'Derived conversion warning; not evidence of an error in the source.'})
        if re.search(r'[A-Za-z@+]', text):
            anomalies.append({'id': f'MTP-A{number:06}-ASCII', 'anchor_id': aid,
                              'kind': 'non_tibetan_payload', 'details': [text]})
        if re.fullmatch(r'@\d+', wt):
            anomalies.append({'id': f'MTP-A{number:06}-GRAPHIC', 'anchor_id': aid,
                              'kind': 'electronic_chapter_marker', 'details': [f'{wt} -> {text}; electronic control token, not presumed printed body text.']})
        bpos += len(braw); wpos += len(wraw)
    require(len(boundaries) == 8, f'Expected eight chapter endings; found {boundaries}')
    pages = [(a['index'], a['page_hint']) for a in anchors if a['wylie_raw_text'].strip().isdecimal()]
    for (i, previous), (j, current) in zip(pages, pages[1:]):
        if current != previous + 1:
            anomalies.append({'id': f'MTP-A{j:06}-PAGE', 'anchor_id': f'MTP-S{j:06}',
                              'kind': 'page_marker_gap', 'details': [previous, current],
                              'meaning': 'E-text locator gap; does not by itself imply omitted text.'})
    chapters, first = [], 1
    for num, end in enumerate(boundaries, 1):
        last = len(anchors) if num == 8 else end
        section = anchors[first-1:last]
        chapters.append({'chapter': num, 'first_index': first, 'last_index': last,
                         'first_anchor': section[0]['id'], 'last_anchor': section[-1]['id'],
                         'closing_anchor': f'MTP-S{end:06}', 'anchor_count': len(section),
                         'raw_start': section[0]['raw_start'], 'raw_end': section[-1]['raw_end'],
                         'page_hints': sorted({a['page_hint'] for a in section if a['page_hint']}),
                         'boundary_status': 'Mechanical colophon locator; requires authored scan review.',
                         'includes_post_chapter_colophon': num == 8})
        first = last + 1
    exact = ''.join(a['raw_text'] for a in anchors)
    converted = ''.join(l['derived_tibetan'] for l in loci)
    require(exact == base[bs:be], 'Source extraction not exact')
    for locus in loci:
        require(reconstruct(locus['base'], locus['opcodes']) == locus['derived_tibetan'], 'Failed opcode reconstruction')
    return {
        'source-anchors.json': {'schema_version': 1, 'source': BASE, 'source_sha256': BASE_HASH,
            'comparison_source': COMPARE, 'comparison_sha256': COMPARE_HASH,
            'offset_unit': 'Unicode code points in exact UTF-8-decoded raw source; no normalization',
            'payload_start': bs, 'payload_end': be, 'payload_sha256': sha(exact.encode()),
            'anchor_count': len(anchors), 'anchors': anchors},
        'electronic-collation.json': {'schema_version': 1, 'source_roles': {
            'governing_scan': 'adzom-1973 / W1KG892 / I1KG895',
            'base_transcript': 'valby-tibetan', 'comparison_transcript': 'valby-wylie',
            'relationship': 'Two electronic renditions of the same Valby/Adzom transcription family; not independent witnesses.'},
            'conversion': {'package': 'pyewts', 'version': '0.2.0', 'options': {'fix_spacing': False},
                           'label': 'Derived EWTS conversion, not an independent textual witness'},
            'base_payload_sha256': sha(exact.encode()), 'derived_payload_sha256': sha(converted.encode()),
            'difference_count': sum(not l['equal'] for l in loci), 'loci': loci},
        'chapter-map.json': {'schema_version': 1, 'chapters': chapters},
        'anomalies.json': {'schema_version': 1, 'anomalies': anomalies},
    }

def prepare(root):
    data = preparation(root)
    for name, item in data.items():
        write(root/'diplomatic'/name, item, frozen=True)
    return {'anchors': data['source-anchors.json']['anchor_count'],
            'chapters': len(data['chapter-map.json']['chapters']),
            'differences': data['electronic-collation.json']['difference_count'],
            'anomalies': len(data['anomalies.json']['anomalies'])}

def verify_prepared(root):
    expected = preparation(root)
    for name, obj in expected.items():
        require((root/'diplomatic'/name).read_bytes() == serialized(obj), f'Prepared source artifact changed: {name}')
    return expected

def chapter_dir(root, chapter):
    require(1 <= chapter <= 8, 'Chapter must be 1..8')
    return root/'diplomatic'/'chapters'/f'{chapter:02}'

def plan(root, chapter, checks=None):
    data = verify_prepared(root)
    spec = data['chapter-map.json']['chapters'][chapter-1]
    section = data['source-anchors.json']['anchors'][spec['first_index']-1:spec['last_index']]
    ids = {a['id'] for a in section}
    differences = [l for l in data['electronic-collation.json']['loci'] if l['anchor_id'] in ids and not l['equal']]
    anomalies = [a for a in data['anomalies.json']['anomalies'] if a['anchor_id'] in ids]
    first_text = next(a['id'] for a in section if a['mechanical_role'] == 'main_text')
    targets = [first_text, spec['closing_anchor']]
    targets.extend(a['anchor_id'] for a in anomalies)
    targets.extend(l['anchor_id'] for l in differences)
    if chapter == 8:
        targets.append(spec['last_anchor'])
    targets = list(dict.fromkeys(targets))
    source_checks = [{'id': f'MTP-C{chapter:02}-CHECK-{i:03}', 'anchor_ids': [aid],
                      'question': 'Inspect governing scan for frozen boundary/anomaly/difference; record allocation and remaining uncertainty.'}
                     for i, aid in enumerate(targets, 1)]
    if checks:
        custom = load(checks)
        require(isinstance(custom, list), 'Additional checks must be a JSON array')
        source_checks.extend(custom)
    require(len({c['id'] for c in source_checks}) == len(source_checks), 'Duplicate source-check IDs')
    for check in source_checks:
        require(check['anchor_ids'] and set(check['anchor_ids']) <= ids, 'Source-check anchors outside chapter')
        require(check.get('question'), 'Source-check question missing')
    required = sorted(set(targets) | {a for c in source_checks for a in c['anchor_ids']})
    contract = {'schema_version': 1, **spec, 'source_files': {f'diplomatic/{n}': file_hash(root/'diplomatic'/n) for n in PREPARED},
                'difference_ids': [d['id'] for d in differences], 'anomaly_ids': [a['id'] for a in anomalies],
                'required_decision_anchors': required, 'source_checks': source_checks,
                'scope': 'Bounded governing-Adzom reading; same-family electronic comparison and targeted scan checks.',
                'required_outputs': list(OUTPUTS) + ['build-manifest.json'], 'claims': CLAIMS,
                'outside_scope': ['Full scan proofreading', 'Exhaustive witness collation', 'Unattested repair', 'Translation'],
                'freeze_note': 'No timestamp in deterministic contract. Exact bytes fixed by contract.sha256; changes require a new edition contract.'}
    dest = chapter_dir(root, chapter)
    write(dest/'contract.json', contract, frozen=True)
    write(dest/'contract.sha256', (file_hash(dest/'contract.json')+'\n').encode(), frozen=True)
    for name in ('decisions.json', 'evidence.json', 'source-checks.json', 'restorations.json'):
        if not (dest/name).exists():
            write(dest/name, [])
    return {'chapter': chapter, 'anchors': len(section), 'differences': len(differences),
            'anomalies': len(anomalies), 'required_decision_anchors': len(required), 'source_checks': len(source_checks)}

def evidence_validation(root, evidence, ids):
    require(isinstance(evidence, list), 'Evidence must be an array')
    index = {}
    for item in evidence:
        eid = item['id']
        require(eid not in index, 'Duplicate evidence ID')
        require(item['status'] in {'accepted', 'excluded', 'mislocated'}, f'Invalid evidence status: {eid}')
        require(item.get('allocation_reason'), f'Evidence allocation reason missing: {eid}')
        require(item.get('anchor_ids') and set(item['anchor_ids']) <= ids, f'Evidence anchors outside chapter: {eid}')
        require(file_hash(safe_path(root, item['path'])) == item['sha256'], f'Evidence hash mismatch: {eid}')
        if item['status'] == 'accepted':
            require(item.get('inspection') == 'native_image_direct', f'Accepted evidence not direct image inspection: {eid}')
            require(item.get('source_id') == 'adzom-1973', f'Accepted governing evidence has wrong source: {eid}')
            require(isinstance(item.get('image_index'), int), f'Image index missing: {eid}')
            manifest = load(root/'editions/scans/adzom-1973/image-manifest.json')
            sources = {i['image_index']: i for i in manifest['images']}
            require(item['image_index'] in sources, f'Image absent from governing manifest: {eid}')
            original = sources[item['image_index']]
            if item.get('crop'):
                require(item.get('original_sha256') == original['sha256'], f'Crop original hash missing/mismatched: {eid}')
                crop = item['crop']
                require(len(crop) == 4 and all(isinstance(v, int) for v in crop), 'Crop must be [left,top,right,bottom]')
                require(0 <= crop[0] < crop[2] <= original['width'] and 0 <= crop[1] < crop[3] <= original['height'], 'Invalid crop coordinates')
            else:
                require(item['sha256'] == original['sha256'], f'Evidence not governing image bytes: {eid}')
        index[eid] = item
    return index

def candidate(root, chapter):
    data = verify_prepared(root)
    dest = chapter_dir(root, chapter)
    contract = load(dest/'contract.json')
    require(file_hash(dest/'contract.json') == (dest/'contract.sha256').read_text().strip(), 'Frozen contract hash mismatch')
    require(contract['chapter'] == chapter and contract['claims'] == CLAIMS, 'Invalid contract chapter/claims')
    for name, expected in contract['source_files'].items():
        require(file_hash(safe_path(root, name)) == expected, f'Frozen source changed: {name}')
    spec = data['chapter-map.json']['chapters'][chapter-1]
    for key in ('first_index','last_index','first_anchor','last_anchor','anchor_count','closing_anchor'):
        require(contract[key] == spec[key], f'Contract boundary mismatch: {key}')
    anchors = data['source-anchors.json']['anchors'][spec['first_index']-1:spec['last_index']]
    ids = {a['id'] for a in anchors}; amap = {a['id']: a for a in anchors}
    loci = [l for l in data['electronic-collation.json']['loci'] if l['anchor_id'] in ids]
    require(contract['difference_ids'] == [l['id'] for l in loci if not l['equal']], 'Frozen differences changed')
    anomalies = [a for a in data['anomalies.json']['anomalies'] if a['anchor_id'] in ids]
    require(contract['anomaly_ids'] == [a['id'] for a in anomalies], 'Frozen anomalies changed')
    decisions = load(dest/'decisions.json'); evidence = load(dest/'evidence.json')
    checks = load(dest/'source-checks.json'); restorations = load(dest/'restorations.json')
    eindex = evidence_validation(root, evidence, ids)
    dindex, decision_ids = {}, set()
    for dec in decisions:
        aid = dec['anchor_id']
        require(aid in ids and aid not in dindex, f'Duplicate/outside decision anchor: {aid}')
        require(dec['id'] not in decision_ids, 'Duplicate decision ID'); decision_ids.add(dec['id'])
        require(dec['old'] == amap[aid]['text'], f'Decision old string mismatch: {aid}')
        require(isinstance(dec['new'], str), f'Decision new must be string: {aid}')
        require(dec['role'] in ROLES, f'Unknown reading role: {aid}')
        require(dec['treatment'] in TREATMENTS, f'Unknown treatment: {aid}')
        require(isinstance(dec['uncertainty'], list) and dec.get('reason'), f'Incomplete decision: {aid}')
        require(isinstance(dec.get('evidence_ids'), list), f'Decision evidence IDs missing: {aid}')
        for eid in dec['evidence_ids']:
            require(eid in eindex and eindex[eid]['status'] == 'accepted' and aid in eindex[eid]['anchor_ids'], f'Unallocated evidence: {aid}/{eid}')
        if dec['old'] != dec['new']:
            require(dec['treatment'] in {'scan_supported_correction','separate_source_layer','display_only'}, f'Changed reading lacks correction treatment: {aid}')
            require(dec['evidence_ids'], f'Changed reading lacks governing scan evidence: {aid}')
        if dec['treatment'] in {'retain_base','retain_with_uncertainty','classify_layer','defer_outside_scope'}:
            require(dec['old'] == dec['new'], f'Retention/classification unexpectedly changes text: {aid}')
        if dec['treatment'] == 'retain_with_uncertainty':
            require(dec['uncertainty'], f'Uncertainty disposition lacks uncertainty: {aid}')
        if dec['treatment'] == 'separate_source_layer':
            require(dec.get('layers'), f'Layer separation lacks layer contents: {aid}')
            require(all(x.get('role') in ROLES and isinstance(x.get('text'), str) for x in dec['layers']), f'Invalid separated layers: {aid}')
        dindex[aid] = dec
    require(set(contract['required_decision_anchors']) <= set(dindex), 'Frozen editorial queue still open: '+','.join(sorted(set(contract['required_decision_anchors'])-set(dindex))))
    cindex = {c['id']: c for c in checks}
    require(len(cindex) == len(checks), 'Duplicate source check')
    require(set(cindex) == {c['id'] for c in contract['source_checks']}, 'Frozen source-check queue mismatch')
    for target in contract['source_checks']:
        result = cindex[target['id']]
        require(result.get('status') == 'closed', f'Source check remains open: {target["id"]}')
        require(result.get('finding') and isinstance(result.get('uncertainty'), list), 'Source check finding/uncertainty missing')
        require(result.get('evidence_ids'), 'Source check evidence missing')
        supported = set()
        for eid in result['evidence_ids']:
            require(eid in eindex and eindex[eid]['status'] == 'accepted', 'Source check uses excluded/unknown evidence')
            supported.update(eindex[eid]['anchor_ids'])
        require(set(target['anchor_ids']) <= supported, f'Source check allocation incomplete: {target["id"]}')
    rids, placed = set(), {}
    for item in restorations:
        rid = item['id']
        require(re.fullmatch(r'MTP-R\d{6}', rid) and rid not in rids, 'Duplicate/invalid restoration ID')
        require(item.get('after_anchor') in ids, 'Restoration placement outside chapter')
        require(item.get('text') and item.get('role') in ROLES and item.get('reason'), 'Incomplete restoration')
        require(isinstance(item.get('uncertainty'), list) and item.get('evidence_ids'), 'Restoration uncertainty/evidence missing')
        for eid in item['evidence_ids']:
            require(eid in eindex and eindex[eid]['status'] == 'accepted' and item['after_anchor'] in eindex[eid]['anchor_ids'], 'Restoration evidence allocation invalid')
        rids.add(rid); placed.setdefault(item['after_anchor'], []).append(item)
    readings = []
    for anchor in anchors:
        aid = anchor['id']; dec = dindex.get(aid)
        readings.append({'id': aid, 'source_anchor': aid, 'text': dec['new'] if dec else anchor['text'],
                         'role': dec['role'] if dec else anchor['mechanical_role'],
                         'source_text': anchor['text'], 'source_line_ending': anchor['line_ending'],
                         'page_hint': anchor['page_hint'], 'decision_id': dec['id'] if dec else None,
                         'review_status': 'targeted_editorial_review' if dec else 'retained_unreviewed_transcript',
                         'uncertainty': dec['uncertainty'] if dec else [],
                         'layers': dec.get('layers', []) if dec else []})
        for item in placed.get(aid, []):
            readings.append({'id': item['id'], 'source_anchor': None, 'after_anchor': aid,
                             'text': item['text'], 'role': item['role'], 'source_text': None,
                             'source_line_ending': None, 'page_hint': anchor['page_hint'],
                             'decision_id': item['id'], 'review_status': 'scan_attested_restoration',
                             'uncertainty': item['uncertainty'], 'layers': []})
    changes = [d for d in decisions if d['old'] != d['new'] or d['role'] != amap[d['anchor_id']]['mechanical_role'] or d.get('layers')]
    unresolved = [{'id': r['id'], 'uncertainty': r['uncertainty']} for r in readings if r['uncertainty']]
    coverage = {'schema_version': 1, 'chapter': chapter, 'anchor_count': len(anchors),
                'accounted_original_anchors': len(anchors), 'restoration_count': len(restorations),
                'changed_text_anchors': sum(d['old'] != d['new'] for d in decisions),
                'layer_or_text_changed_anchors': len(changes), 'editorial_decisions_completed': len(decisions),
                'required_decisions_completed': len(contract['required_decision_anchors']), 'required_decisions_remaining': 0,
                'source_checks_completed': len(checks), 'source_checks_remaining': 0,
                'electronic_loci_compared': len(loci), 'electronic_difference_count': len(contract['difference_ids']),
                'retained_unreviewed_transcript_anchors': len(anchors)-len(decisions),
                'accepted_evidence_records': sum(e['status'] == 'accepted' for e in evidence),
                'excluded_evidence_records': sum(e['status'] != 'accepted' for e in evidence),
                'unresolved': unresolved, 'claims': CLAIMS,
                'comparison_scope': data['electronic-collation.json']['source_roles']['relationship']}
    md = [f'# String of Pearls — chapter {chapter}', '',
          'Bounded golden reading of the Adzom printing. Original source anchors are electronic locators, not manuscript line numbers.', '',
          'Targeted source review only; full scan proofreading and exhaustive witness collation were not performed.', '',
          'Page markers and blank anchors remain in the machine reading. Source punctuation is not silently supplied.', '']
    for row in readings:
        if row['role'] in {'metadata','blank'}:
            continue
        md.append(f'<!-- {row["id"]}; {row["role"]} -->')
        if row['role'] in {'heading','chapter_colophon','colophon','annotation','graphic','unresolved'}:
            md.append(f'[{row["role"]}] {row["text"]}')
        else:
            md.append(row['text'])
        for layer in row['layers']:
            md.append(f'[{layer["role"]}] {layer["text"]}')
        if row['uncertainty']:
            md.append('> Uncertainty: ' + '; '.join(row['uncertainty']))
        md.append('')
    objects = {
        'reading.json': {'schema_version': 1, 'chapter': chapter, 'objects': readings},
        'apparatus.json': {'schema_version': 1, 'chapter': chapter, 'source_roles': data['electronic-collation.json']['source_roles'],
                           'electronic_loci': loci, 'decisions': decisions, 'restorations': restorations,
                           'evidence': evidence, 'source_checks': checks, 'anomalies': anomalies},
        'changes.json': {'schema_version': 1, 'chapter': chapter, 'changes': changes, 'restorations': restorations},
        'coverage.json': coverage,
    }
    outputs = {name: serialized(obj) for name, obj in objects.items()}
    outputs['reading.md'] = ('\n'.join(md)+'\n').encode()
    inputs = {relative(root, dest/n): file_hash(dest/n) for n in ('contract.json','contract.sha256','decisions.json','evidence.json','source-checks.json','restorations.json')}
    inputs.update(contract['source_files'])
    witness = root/'diplomatic/GOVERNING-WITNESS.json'
    if witness.exists():
        inputs[relative(root, witness)] = file_hash(witness)
    manifest = {'schema_version': 1, 'chapter': chapter, 'inputs': inputs,
                'outputs': {name: sha(outputs[name]) for name in OUTPUTS},
                'build_method': 'scripts/golden_pipeline.py; deterministic UTF-8 JSON/Markdown; no Unicode normalization',
                'conversion': data['electronic-collation.json']['conversion'], 'claims': CLAIMS}
    outputs['build-manifest.json'] = serialized(manifest)
    return outputs

def build(root, chapter):
    outputs = candidate(root, chapter)
    dest = chapter_dir(root, chapter)
    if (dest/'signoff.json').exists():
        for name, data in outputs.items():
            require((dest/name).is_file() and (dest/name).read_bytes() == data, 'Refusing to alter signed output: '+name)
    for name, data in outputs.items():
        write(dest/name, data)
    return {'chapter': chapter, 'outputs': len(outputs), 'build_manifest_sha256': file_hash(dest/'build-manifest.json')}

def validate(root, chapter, final=False):
    expected = candidate(root, chapter)
    dest = chapter_dir(root, chapter)
    for name, data in expected.items():
        require((dest/name).exists() and (dest/name).read_bytes() == data, f'Output corruption or nonreproducible build: {name}')
    apparatus = load(dest/'apparatus.json')
    # Whole-locus and opcode paths independently reconstruct exact comparison strings.
    for locus in apparatus['electronic_loci']:
        require(reconstruct(locus['base'], locus['opcodes']) == locus['derived_tibetan'], 'Opcode reconstruction failure')
        whole_locus = locus['base'] if locus['equal'] else locus['derived_tibetan']
        require(whole_locus == locus['derived_tibetan'], 'Whole-locus reconstruction failure')
    if final:
        require((dest/'signoff.json').exists(), 'Unsigned candidate: final signoff missing')
        signoff = load(dest/'signoff.json')
        require(signoff.get('approved') is True and signoff.get('reviewer') and signoff.get('review'), 'Incomplete signoff')
        require(signoff.get('chapter') == chapter, 'Signoff chapter mismatch')
        require(signoff.get('build_manifest_sha256') == file_hash(dest/'build-manifest.json'), 'Signoff manifest mismatch')
        require(signoff.get('output_sha256') == load(dest/'build-manifest.json')['outputs'], 'Signoff output hash mismatch')
        require(signoff.get('claims') == CLAIMS, 'Signoff overclaims work performed')
        review_path = signoff.get('review_path')
        require(review_path and file_hash(safe_path(root, review_path)) == signoff.get('review_sha256'), 'Final review hash mismatch')
    return {'chapter': chapter, 'mode': 'final' if final else 'candidate', 'passed': True,
            'build_manifest_sha256': file_hash(dest/'build-manifest.json'),
            'reproducible_build': True, 'source_preservation': True,
            'whole_locus_reconstruction': True, 'opcode_reconstruction': True,
            'evidence_hashes_and_allocation_fields': True,
            'limits': 'Structural validation cannot independently verify a reviewer’s palaeographic reading or image-to-locus assertion.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('prepare')
    p = sub.add_parser('plan'); p.add_argument('--chapter', type=int, required=True); p.add_argument('--checks', type=Path)
    p = sub.add_parser('build'); p.add_argument('--chapter', type=int, required=True)
    p = sub.add_parser('validate'); p.add_argument('--chapter', type=int, required=True); p.add_argument('--final', action='store_true')
    sub.add_parser('test')
    args = parser.parse_args()
    try:
        if args.command == 'prepare': result = prepare(args.root)
        elif args.command == 'plan': result = plan(args.root, args.chapter, args.checks)
        elif args.command == 'build': result = build(args.root, args.chapter)
        elif args.command == 'validate': result = validate(args.root, args.chapter, args.final)
        else:
            import subprocess
            return subprocess.call([sys.executable, str(Path(__file__).with_name('test_golden_pipeline.py'))])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValidationError, KeyError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f'VALIDATION ERROR: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
