#!/usr/bin/env python3
"""Build/verify the Phase D working text; never bypass or approve a release gate.

Reuses the existing parser, source-audit/notes validators and reader renderer.
Historical contracts, QC, signatures, publication receipts and tags are read-only.
The review report, not this structural build, assesses translation correctness.
"""
from __future__ import annotations
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import sys
import translation_pipeline as t
import build_translation_aggregate as a

ROOT = Path(__file__).resolve().parents[1]
INPUT = '46110acd02a6caa14a00f91605c1a478eda72bcd'
PLAN_COMMIT = 'fe4f6c343f1472cc18952c4b57a716feb2b05ba8'
POLICY_COMMIT = '882454cb2576d0b2529296bd7a3a7c87371ab4cf'
GOLDEN_COMMIT = '4d6ba07e1b3379183633127cd387d98d8195eb95'
GOLDEN_SHA = 'dc371e71f4eb0fa842963eebf3ebb0bb7c60e9623a038cf1cdcd3339855be2c1'
POLICY = {
    'guidelines/tibetan_translation_standard_v2.md': 'dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f',
    'glossary/expanded_tibetan_english_glossary.csv': 'f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7',
}
MODE = 'post-translation-review-working-text'
REVIEW_URL = ('https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/blob/'
              'review/phase-d-20261005/translations/FINAL-REVIEW.md#phase-d-review')
LIMITS = [
    'Working revision of translation-v1, not a new or approved formal release.',
    'Pair/object coverage includes explicitly unresolved and nontranslatable material.',
    'Native-audit evidence is preserved and structurally verified; this build does not inspect images or certify source readings.',
    'Mechanical validation proves structure/provenance/reproducibility, not semantic correctness or human certification.',
    'See FINAL-REVIEW.md for the independent original-text review and separate repair self-check.',
    'Historical QC/signoff records apply only to their original pinned release bytes.',
]

def frozen(root: Path, rel: str) -> str:
    """Check a protected file against the current-review input, not an old audit."""
    body = t.git(root, 'show', INPUT + ':' + rel)
    path = t.safe(root, rel)
    t.need(path.read_bytes() == body, 'Protected input changed: ' + rel)
    return t.sha(body)


def authority(root: Path) -> tuple[dict, dict]:
    t.need(t.git(root, 'rev-parse', 'golden-v1^{commit}').decode().strip() == GOLDEN_COMMIT,
           'Golden tag moved')
    body = (root / 'golden/reading.json').read_bytes()
    t.need(t.sha(body) == GOLDEN_SHA and
           body == t.git(root, 'show', GOLDEN_COMMIT + ':golden/reading.json'),
           'Fixed golden Tibetan changed')
    inputs = {}
    for rel in ('AGENTS.md', 'FORMAT.md', 'translations/PLAN.json', 'paired/source.md',
                'golden/reading.json', 'golden/reading.md',
                'scripts/translation_pipeline.py', 'scripts/build_translation_aggregate.py'):
        inputs[rel] = frozen(root, rel)
    for rel, digest in POLICY.items():
        t.need(t.digest(root / rel) == digest, 'Active policy version changed: ' + rel)
        inputs[rel] = digest
    with (root / 'glossary/expanded_tibetan_english_glossary.csv').open(newline='') as stream:
        rows = list(csv.reader(stream))
    t.need(len(rows) == 284 and all(len(row) == 8 for row in rows), 'Glossary must have 283 eight-column data rows')
    # Existing release identities remain historical; none authorizes this build.
    for receipt in sorted((root / 'translations/publication').glob('*.json')):
        rel = receipt.relative_to(root).as_posix(); inputs[rel] = frozen(root, rel)
        data = t.load(receipt)
        if 'tag' in data and 'remote_tag_object' in data:
            t.need(t.git(root, 'rev-parse', 'refs/tags/' + data['tag']).decode().strip() ==
                   data['remote_tag_object'], 'Historical tag moved: ' + data['tag'])
    pins = {'source_tag': 'golden-v1', 'source_commit': GOLDEN_COMMIT,
            'source_reading_sha256': GOLDEN_SHA,
            'glossary': 'glossary/expanded_tibetan_english_glossary.csv',
            'glossary_sha256': POLICY['glossary/expanded_tibetan_english_glossary.csv'],
            'standard': 'guidelines/tibetan_translation_standard_v2.md',
            'standard_sha256': POLICY['guidelines/tibetan_translation_standard_v2.md']}
    return pins, inputs


def render(chapters: list[dict], notes: list[dict], bilingual: bool, chapter: int | None = None) -> bytes:
    """Use the established display function; change provenance labels only."""
    text = a.render(chapters, notes, bilingual).decode()
    text = text.replace(
        'Eight fixed chapter releases, translated from `golden-v1`. All source comparisons and unresolved readings remain in the endnotes.',
        'Post-translation-review working revision of `translation-v1`, from fixed `golden-v1`. '
        'This is not a new formal release. All source comparisons and unresolved readings remain in the endnotes.')
    text = text.replace('[Fixed chapter release]', '[Historical chapter release — not the current working text]')
    text = text.replace('This is an agent-produced working translation for human review.',
                        'This is an agent-produced working translation for human review. '
                        f'[Current review and unresolved decisions]({REVIEW_URL}).')
    if chapter is not None:
        text = text.replace('# String of Pearls — ', f'# String of Pearls — chapter {chapter}: ', 1)
        text = text.replace('(../golden/README.md)', '(../../../golden/README.md)')
    return text.encode()


def generate(root: Path) -> tuple[dict[str, bytes], dict]:
    root = root.resolve(); pins, global_inputs = authority(root)
    golden = t.load(root / 'golden/reading.json'); allrows = golden['objects']
    index = {row['id']: i for i, row in enumerate(allrows)}
    chapters = []; outputs = {}; source_pairs = []; english_pairs = []; definitions = {}; bodies = []
    for n in range(1, 9):
        d = t.directory(root, n); prefix = d.relative_to(root).as_posix() + '/'; inputs = dict(global_inputs)
        for name in ('source.md', 'segmentation.json', 'contract.json', 'contract.sha256',
                     'adzom-audit.json', 'audit-contract.json', 'audit-contract.sha256',
                     'qc.json', 'signoff.json', 'FINAL-REVIEW.md', 'translation-draft.md'):
            if (d / name).exists(): inputs[prefix + name] = frozen(root, prefix + name)
        boundary = golden['chapter_boundaries'][n - 1]
        rows = allrows[index[boundary['first_object']]:index[boundary['last_object']] + 1]
        seg = t.segmentation(root, n, rows); amap = {row['id']: row for row in rows}
        _, sp, _ = t.parse((d / 'source.md').read_text())
        text = (d / 'translation.md').read_text(); fm, ep, defs = t.parse(text, True)
        t.check_header(fm, pins, n, n, True)
        t.need([p['id'] for p in sp] == [p['id'] for p in seg] == [p['id'] for p in ep], 'Pair order/symmetry mismatch')
        for p, s in zip(sp, seg):
            t.need(p['metadata'] == {'golden': ' '.join(s['golden_ids']), 'role': s['role'], 'format': s['format']}, 'Source role/format changed')
            t.need(p['text'] == '\n'.join(amap[i]['text'] for i in s['golden_ids']), 'Tibetan changed: ' + p['id'])
        changes = json.loads(t.git(root, 'show', GOLDEN_COMMIT + f':diplomatic/chapters/{n:02}/changes.json'))['changes']
        native, extra, evidence = t.audit(root, n, rows)
        obligations = t.golden_obligations(rows, changes) | extra
        seal = t.load(d / 'audit-contract.json')
        t.need(t.digest(d / 'audit-contract.json') == (d / 'audit-contract.sha256').read_text().strip(), 'Audit seal changed')
        t.need(seal == {'chapter': n, 'audit_sha256': t.digest(d / 'adzom-audit.json'),
                       'required_obligations': sorted(obligations), 'evidence_sha256': dict(sorted(evidence.items()))}, 'Audit obligations/evidence changed')
        mapping, states = t.notes_and_status(root, n, seg, ep, defs, obligations)
        pairs = []
        for s, e, p in zip(sp, ep, seg):
            state = states[p['id']]
            pairs.append({'id': p['id'], 'golden_ids': p['golden_ids'], 'golden_objects': [amap[i] for i in p['golden_ids']],
                          'role': p['role'], 'format': p['format'], 'source': s['text'], 'translation': e['text'],
                          'status': state['status'], 'reason': state['reason'], 'note_ids': state['note_ids']})
        t.need(not definitions.keys() & defs.keys(), 'Duplicate chapter note IDs')
        definitions.update(defs); source_pairs += sp; english_pairs += ep
        bodies.append(text[text.find('\n---\n', 4) + 5:].split(t.END)[0].strip('\n'))
        notes = [{'id': i, **v} for i, v in defs.items()]
        coverage = {'chapter': n, 'mode': MODE, 'pairs': len(pairs), 'golden_objects': len(rows),
                    'source_objects_remaining_in_chapter': 0, 'note_count': len(notes),
                    'statuses': dict(Counter(p['status'] for p in pairs)),
                    'formats': dict(Counter(p['format'] for p in pairs)),
                    'obligations_required': len(obligations), 'obligations_covered': len(obligations), 'obligations_remaining': 0,
                    'native_anchor_checks': len(native['anchor_checks']), 'native_images': len(native['images']),
                    'native_findings': len(native['findings']), 'golden_uncertainty_statements': sum(len(r['uncertainty']) for r in rows),
                    'golden_changes': len(changes), 'source_roles': dict(Counter(r['role'] for r in rows)),
                    'limits': LIMITS, 'claims': t.CLAIMS}
        machine = {'chapter': n, 'mode': MODE, 'source_pins': pins, 'pairs': pairs, 'endnotes': notes, 'note_map': mapping, 'claims': t.CLAIMS}
        c = {'chapter': n, 'pins': pins, 'pairs': pairs, 'endnotes': notes, 'note_map': mapping,
             'coverage': coverage, 'native': native, 'obligations': sorted(obligations)}
        chapters.append(c)
        for name in ('translation.md', 'note-map.json', 'translation-note-map.json', 'pair-status.json', 'usage.json', 'glossary-proposals.json'):
            if (d / name).exists(): inputs[prefix + name] = t.digest(d / name)
        inputs.update(evidence)
        products = {'reading.md': render([c], notes, False, n), 'bilingual.md': render([c], notes, True, n),
                    'machine.json': t.encoded(machine), 'coverage.json': t.encoded(coverage)}
        manifest = manifest_for(root, pins, inputs, products, chapter=n)
        products['build-manifest.json'] = t.encoded(manifest)
        outputs.update({prefix + k: v for k, v in products.items()})
    # Source prefix is never regenerated: it must remain byte-for-byte fixed.
    _, fixed_sp, _ = t.parse((root / 'paired/source.md').read_text())
    t.need(fixed_sp == source_pairs, 'Frozen source prefix differs from chapters')
    pairs, notes = a.verify_sequence(chapters, allrows, source_pairs, english_pairs, definitions)
    paired = (t.header(pins, 1, 8, True) + '\n\n'.join(bodies) + '\n\n' + t.END + '\n\n' +
              '\n\n'.join(v['raw'] for v in definitions.values()) + '\n').encode()
    _, ap, an = t.parse(paired.decode(), True)
    t.need(ap == english_pairs and an == definitions, 'Assembled English/notes changed')
    outputs['paired/translation.md'] = paired
    totals = {key: sum(c['coverage'][key] for c in chapters) for key in
              ('pairs', 'golden_objects', 'note_count', 'obligations_required', 'obligations_covered', 'obligations_remaining',
               'native_anchor_checks', 'native_findings', 'golden_uncertainty_statements', 'golden_changes')}
    coverage = {'edition': 'translation-v1', 'mode': MODE, 'chapters_represented': 8, 'source_objects_represented': len(allrows),
                'source_objects_remaining': 0, 'totals': totals, 'pair_statuses': dict(Counter(p['status'] for p in pairs)),
                'chapter_coverage': [{'chapter': c['chapter'], 'coverage': c['coverage']} for c in chapters],
                'limits': LIMITS, 'claims': t.CLAIMS, 'count_note': 'Representation is not resolution or an accuracy percentage.'}
    machine = {'edition': 'translation-v1', 'mode': MODE, 'source_pins': pins,
               'chapter_boundaries': [{'chapter': c['chapter'], 'first_pair': c['pairs'][0]['id'], 'last_pair': c['pairs'][-1]['id'], 'pair_count': len(c['pairs'])} for c in chapters],
               'pairs': pairs, 'endnotes': notes, 'note_map': [m for c in chapters for m in c['note_map']],
               'chapter_obligations': [{'chapter': c['chapter'], 'obligations': c['obligations']} for c in chapters], 'claims': t.CLAIMS}
    products = {'reading.md': render(chapters, notes, False), 'bilingual.md': render(chapters, notes, True),
                'machine.json': t.encoded(machine), 'coverage.json': t.encoded(coverage)}
    inputs = dict(global_inputs)
    for path, value in outputs.items(): inputs[path] = t.sha(value)
    products['build-manifest.json'] = t.encoded(manifest_for(root, pins, inputs, products))
    outputs.update({'translations/' + k: v for k, v in products.items()})
    summary = {'mode': MODE, 'files': len(outputs), 'chapters': 8, 'pairs': len(pairs), 'golden_objects': len(allrows),
               'notes': len(notes), 'unresolved_pairs': coverage['pair_statuses'].get('unresolved', 0),
               'obligations_covered': totals['obligations_covered'], 'claims': t.CLAIMS}
    return outputs, summary


def manifest_for(root: Path, pins: dict, inputs: dict, outputs: dict, chapter: int | None = None) -> dict:
    inputs = dict(inputs)
    inputs['scripts/review_working_text.py'] = t.digest(root / 'scripts/review_working_text.py')
    result = {'edition': 'translation-v1', 'mode': MODE, 'source_pins': pins,
              'review_input_commit': INPUT, 'pre_edit_evidence_commit': PLAN_COMMIT,
              'policy_commit': POLICY_COMMIT, 'standard_version': '2.1.0',
              'review_evidence': 'translations/FINAL-REVIEW.md#phase-d-review',
              'input_sha256': dict(sorted(inputs.items())), 'output_sha256': {k: t.sha(v) for k, v in outputs.items()},
              'method': 'Current authored English; unchanged fixed Tibetan; existing pure validators and display renderer. No release gate bypass or signature update.',
              'claims': t.CLAIMS, 'formal_release_approved': False}
    if chapter is not None: result['chapter'] = chapter
    return result


def run(root: Path, command: str) -> dict:
    products, summary = generate(root)
    if command == 'build':
        for rel, body in products.items(): t.write(t.safe(root, rel), body)
    else:
        for rel, body in products.items():
            t.need(t.safe(root, rel).is_file() and t.safe(root, rel).read_bytes() == body,
                   'Working output is stale or corrupted: ' + rel)
    return {'passed': True, 'command': command, 'read_only': command == 'verify', **summary}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('build', 'verify')); parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.root.resolve(), args.command), indent=2)); return 0
    except (t.Error, OSError, KeyError, TypeError, ValueError) as error:
        print('WORKING REVIEW ERROR: ' + str(error), file=sys.stderr); return 1

if __name__ == '__main__':
    raise SystemExit(main())
