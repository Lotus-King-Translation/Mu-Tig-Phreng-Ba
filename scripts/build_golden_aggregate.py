#!/usr/bin/env python3
"""Deterministically aggregate eight signed, receipted, immutable chapter releases."""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote
import golden_pipeline as gp

ROOT = Path(__file__).resolve().parents[1]
FILES = ('reading.md', 'reading.json', 'coverage.json', 'README.md')
CHAPTERS = 8
ORIGINAL_ANCHORS = 2053
REPO = 'https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba'
LICENSE = 'https://creativecommons.org/licenses/by-sa/4.0/'
TIBETAN_REVISION = 'https://wikisource.org/w/index.php?oldid=1028862'
WYLIE_REVISION = 'https://wikisource.org/w/index.php?oldid=274319'
LIMITS = [
    'Maintained reading of the selected Adzom printing; not an eclectic reconstruction or an infallible text.',
    'Targeted governing-scan checks were performed; full scan proofreading was not performed.',
    'The Tibetan and Wylie e-texts belong to one transcription family; their mechanical equivalence is not independent witness agreement.',
    'Exhaustive witness collation and independent human palaeographic certification were not performed.',
    'Visible source gaps, unresolved annotations and other uncertainties remain explicit. No unattested wording is silently restored.',
    'Untargeted source punctuation and decorative signs are not silently supplied or normalized.',
    'No English translation is included in this release.',
]


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gp.require(result.returncode == 0, 'Git verification failed: '+result.stderr.decode('utf-8','replace').strip())
    return result.stdout


def receipt_path(root, chapter):
    path = root/'diplomatic/publication'/f'ch{chapter:02}-v1.json'
    gp.require(path.is_file(), f'Chapter {chapter}: publication receipt required')
    return path


def receipt_identity(root, chapter):
    path = receipt_path(root, chapter)
    receipt = gp.load(path)
    gp.require(receipt.get('chapter') == chapter, f'Receipt chapter mismatch: {chapter}')
    tag = receipt.get('tag')
    gp.require(isinstance(tag,str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._/-]*',tag), 'Invalid receipt tag')
    gp.require('..' not in tag and not tag.endswith('/'), 'Unsafe receipt tag')
    tag_object = receipt.get('remote_tag_object')
    peeled = receipt.get('remote_peeled_commit')
    gp.require(isinstance(tag_object,str) and re.fullmatch(r'[0-9a-f]{40,64}',tag_object), 'Receipt lacks tag object SHA')
    gp.require(isinstance(peeled,str) and re.fullmatch(r'[0-9a-f]{40,64}',peeled), 'Receipt lacks peeled commit SHA')
    gp.require(receipt.get('release_commit') == peeled == receipt.get('remote_main_at_release'), f'Chapter {chapter}: receipt remote/release commit mismatch')
    directory = gp.chapter_dir(root,chapter)
    gp.require(receipt.get('build_manifest_sha256') == gp.file_hash(directory/'build-manifest.json'), f'Chapter {chapter}: receipt build manifest mismatch')
    gp.require(receipt.get('coverage') == gp.load(directory/'coverage.json'), f'Chapter {chapter}: receipt coverage mismatch')
    local_object = git(root,'rev-parse','--verify',f'refs/tags/{tag}').decode().strip()
    local_peeled = git(root,'rev-parse','--verify',f'refs/tags/{tag}^{{commit}}').decode().strip()
    gp.require(git(root,'cat-file','-t',local_object).strip() == b'tag', f'Chapter {chapter}: release tag is not annotated')
    gp.require(local_object == tag_object and local_peeled == peeled, f'Chapter {chapter}: tag differs from verified publication receipt')
    return {'chapter': chapter, 'tag': tag, 'tag_object': tag_object, 'peeled_commit': peeled,
            'receipt': gp.relative(root,path), 'receipt_sha256': gp.file_hash(path),
            'url': REPO+'/tree/'+quote(tag,safe='')}


def verify_tagged_file(root, tag, rel):
    path = gp.safe_path(root,rel)
    tagged = git(root,'show',f'refs/tags/{tag}:{rel}')
    # LFS stores a content-addressed pointer in Git. Compare working bytes with that
    # exact object's hash and size; do not compare a native image to pointer text.
    match = re.fullmatch(rb'version https://git-lfs.github.com/spec/v1\noid sha256:([0-9a-f]{64})\nsize ([0-9]+)\n',tagged)
    if match:
        gp.require(gp.file_hash(path) == match.group(1).decode() and path.stat().st_size == int(match.group(2)), f'Released LFS content changed: {rel}')
    else:
        gp.require(path.read_bytes() == tagged, f'Released bytes changed: {rel}')
    return gp.file_hash(path)


def collect(root):
    # Gate the whole operation before validating any partial-book content.
    for chapter in range(1,CHAPTERS+1):
        directory = gp.chapter_dir(root,chapter)
        gp.require(directory.is_dir(), f'Missing chapter: {chapter}')
        gp.require((directory/'signoff.json').is_file(), f'Missing chapter signoff: {chapter}')
        receipt_path(root,chapter)
    releases, chapters, inputs = [], [], {}
    for chapter in range(1,CHAPTERS+1):
        release = receipt_identity(root,chapter)
        directory = gp.chapter_dir(root,chapter)
        result = gp.validate(root,chapter,final=True)
        gp.require(result['passed'] is True, f'Chapter {chapter} final validation failed')
        prefix = gp.relative(root,directory)
        tagged_paths = git(root,'ls-tree','-rz','--name-only',f'refs/tags/{release["tag"]}','--',prefix+'/').split(b'\0')
        tagged_paths = [p.decode() for p in tagged_paths if p]
        gp.require(tagged_paths, f'No chapter files in tag: {chapter}')
        required = {prefix+'/'+name for name in (*gp.OUTPUTS,'build-manifest.json','signoff.json')}
        gp.require(required <= set(tagged_paths), f'Tag omits required chapter files: {chapter}')
        manifest = gp.load(directory/'build-manifest.json')
        paths = set(tagged_paths) | set(manifest['inputs'])
        paths.add(gp.load(directory/'signoff.json')['review_path'])
        for evidence in gp.load(directory/'evidence.json'):
            paths.add(evidence['path'])
        paths.update({gp.BASE,gp.COMPARE,'editions/scans/adzom-1973/image-manifest.json',
                      'diplomatic/GOVERNING-WITNESS.json'})
        for rel in sorted(paths):
            if rel in {prefix+'/PUBLICATION-RECEIPT.json',prefix+'/publication-receipt.json'}:
                continue  # The receipt is intentionally committed after its fixed tag.
            digest = verify_tagged_file(root,release['tag'],rel)
            if rel in inputs:
                gp.require(inputs[rel] == digest, f'Conflicting shared input across releases: {rel}')
            inputs[rel] = digest
        inputs[release['receipt']] = release['receipt_sha256']
        reading = gp.load(directory/'reading.json')
        coverage = gp.load(directory/'coverage.json')
        gp.require(reading['chapter'] == chapter and coverage['chapter'] == chapter, 'Chapter payload identity mismatch')
        gp.require(coverage['claims'] == gp.CLAIMS, f'Chapter {chapter} makes unsupported coverage claims')
        gp.require(coverage['required_decisions_remaining'] == 0 and coverage['source_checks_remaining'] == 0, 'Open chapter queues')
        chapters.append({'chapter':chapter,'objects':reading['objects'],'coverage':coverage,
                         'apparatus':prefix+'/apparatus.json','reading':prefix+'/reading.json'})
        releases.append(release)
    verify_sequence(chapters)
    return chapters,releases,inputs


def verify_sequence(chapters):
    gp.require([c['chapter'] for c in chapters] == list(range(1,CHAPTERS+1)), 'Chapters missing, duplicated or reordered')
    originals, restoration_ids, all_ids = [], set(), set()
    previous_anchor = None
    for chapter in chapters:
        count = 0
        previous_anchor = None
        for row in chapter['objects']:
            oid = row['id']
            gp.require(oid not in all_ids, f'Duplicate reading/restoration ID: {oid}')
            all_ids.add(oid)
            gp.require(row['role'] in gp.ROLES, f'Unknown role: {oid}')
            gp.require(isinstance(row['text'],str) and isinstance(row['layers'],list) and isinstance(row['uncertainty'],list), f'Invalid text/layers/uncertainty: {oid}')
            if row['source_anchor'] is not None:
                gp.require(row['source_anchor'] == oid and re.fullmatch(r'MTP-S\d{6}',oid), f'Invalid original anchor: {oid}')
                originals.append(oid); count += 1; previous_anchor = oid
            else:
                gp.require(re.fullmatch(r'MTP-R\d{6}',oid) and oid not in restoration_ids, f'Invalid/duplicate restoration: {oid}')
                gp.require(row.get('after_anchor') == previous_anchor, f'Restoration misplaced: {oid}')
                restoration_ids.add(oid)
        gp.require(chapter['coverage']['anchor_count'] == count == chapter['coverage']['accounted_original_anchors'], 'Chapter anchor coverage mismatch')
        gp.require(chapter['coverage']['restoration_count'] == sum(r['source_anchor'] is None for r in chapter['objects']), 'Chapter restoration coverage mismatch')
    gp.require(originals == [f'MTP-S{i:06}' for i in range(1,ORIGINAL_ANCHORS+1)], 'Original anchors must be exactly MTP-S000001..MTP-S002053, ordered without gaps or overlap')
    return {'original_anchors':len(originals),'restorations':len(restoration_ids),'reading_objects':len(all_ids)}


def reading_markdown(chapters,releases):
    lines = ['# མུ་ཏིག་ཕྲེང་བ་ — String of Pearls', '',
             'Bounded golden Tibetan edition, v1. The Adzom printing governs this maintained reading.', '',
             'Targeted scan review only; full scan proofreading and exhaustive witness collation were not performed. '
             'Unresolved readings and untranscribed source material remain visible in the notes.', '',
             'Electronic page/chapter markers are labelled metadata. Annotations and colophons retain their separate roles. '
             'Every original anchor is present in [the machine reading](reading.json).', '',
             'Source attribution and reuse: [Wikisource contributors](../editions/research/etexts-translations/wikisource/README.md), '
             'transcription attributed to Jim Valby, f69; [CC BY-SA 4.0]('+LICENSE+'). Changes are documented in each chapter apparatus.', '']
    footnotes = []
    labels = {'metadata':'Electronic metadata', 'heading':'Source heading', 'chapter_colophon':'Chapter colophon',
              'colophon':'Colophon', 'annotation':'Source annotation', 'graphic':'Graphic', 'unresolved':'Unresolved source layer'}
    for chapter,release in zip(chapters,releases):
        n=chapter['chapter']
        lines.extend([f'## Chapter {n}', '', f'[Fixed chapter release]({release["url"]}) · [Apparatus](../{chapter["apparatus"]})', ''])
        for row in chapter['objects']:
            oid=row['id']; role=row['role']; text=row['text']
            lines.append(f'<a id="{oid.lower()}"></a>')
            marker = f'[^{oid}]' if row['uncertainty'] else ''
            if role == 'blank':
                if text:
                    lines.append(text+marker)
                else:
                    lines.append(f'<!-- {oid}: preserved blank source anchor -->'+marker)
            elif role in labels:
                lines.append(f'> [{labels[role]}] {text}{marker}')
            else:
                lines.append(text+marker)
            for layer in row['layers']:
                lines.extend(['',f'> [{labels.get(layer["role"],layer["role"])}] {layer["text"]}'])
            lines.append('')
            if row['uncertainty']:
                note = '; '.join(row['uncertainty'])
                footnotes.append(f'[^{oid}]: {note} [Evidence and decision](../{chapter["apparatus"]}); [return to text](#{oid.lower()}).')
    if footnotes:
        lines.extend(['## Source-linked uncertainty notes','',*footnotes,''])
    return ('\n'.join(lines)+'\n').encode('utf-8')


def generate(root):
    chapters,releases,inputs = collect(root)
    counts = verify_sequence(chapters)
    objects = [copy.deepcopy(row) for c in chapters for row in c['objects']]
    boundaries = [{'chapter':c['chapter'],'first_object':c['objects'][0]['id'],'last_object':c['objects'][-1]['id'],
                   'object_count':len(c['objects']),'chapter_reading':c['reading'],
                   'chapter_reading_sha256':inputs[c['reading']]} for c in chapters]
    additive = ('anchor_count','accounted_original_anchors','restoration_count','changed_text_anchors',
                'layer_or_text_changed_anchors','editorial_decisions_completed','required_decisions_completed',
                'required_decisions_remaining','source_checks_completed','source_checks_remaining',
                'electronic_loci_compared','electronic_difference_count','retained_unreviewed_transcript_anchors',
                'accepted_evidence_records','excluded_evidence_records')
    coverage = {'schema_version':1,'scope':'Whole-book bounded golden v1; aggregation of eight fixed chapter releases',
                'chapters_released':8,**counts,
                'totals':{key:sum(c['coverage'][key] for c in chapters) for key in additive},
                'claims':copy.deepcopy(gp.CLAIMS),'limits':LIMITS,
                'unresolved':[{'chapter':c['chapter'],**copy.deepcopy(u)} for c in chapters for u in c['coverage']['unresolved']],
                'chapter_coverage':[{'chapter':c['chapter'],'path':f'diplomatic/chapters/{c["chapter"]:02}/coverage.json',
                                     'sha256':inputs[f'diplomatic/chapters/{c["chapter"]:02}/coverage.json']} for c in chapters],
                'count_note':'Evidence records are summed per chapter; the same source image may support multiple chapters. Counts are not accuracy percentages.'}
    reading = {'schema_version':1,'work':'MTP','title':'མུ་ཏིག་ཕྲེང་བ་','edition':'bounded-golden-v1',
               'governing_source':'adzom-1973 / W1KG892 / I1KG895',
               'license':LICENSE,'attribution':'Wikisource contributors; underlying transcript attributed to Jim Valby, f69. Coordinating editorial changes documented in chapter apparatus.',
               'source_revisions':{'tibetan':TIBETAN_REVISION,'wylie':WYLIE_REVISION},
               'chapter_boundaries':boundaries,'objects':objects}
    readme = ['# Golden Tibetan edition — bounded v1','',
              '[Read the Tibetan text](reading.md) · [Machine reading](reading.json) · [Coverage and uncertainty](coverage.json) · [Build manifest](build-manifest.json)','',
              'This whole-book edition preserves eight individually signed and published chapter readings. '
              'Every one of the 2,053 original electronic anchors remains ordered and accounted for; any restorations retain separate IDs. '
              'Roles, source layers, exact selected strings and uncertainty notes are copied unchanged from those releases.','',
              '## Source and attribution','',
              'The governing printing is the Sanje Dorje Adzom reproduction (1973–1977), BDRC W1KG892, image group I1KG895, printed pages 417–537. '
              'See the [selection record](../diplomatic/GOVERNING-WITNESS.json) and [source register](../editions/REGISTER.csv).','',
              'The electronic base is [Wikisource Tibetan revision 1028862]('+TIBETAN_REVISION+'); '
              'the same-family comparator is [Wylie revision 274319]('+WYLIE_REVISION+'). '
              'Both are attributed by their archived talk pages to Jim Valby, f69. Attribute Wikisource contributors; '
              'their [page histories and provenance](../editions/research/etexts-translations/wikisource/README.md) are preserved in the repository. '
              'This adapted text is shared under [Creative Commons Attribution–ShareAlike 4.0]('+LICENSE+'). '
              'The chapter apparatus identifies editorial changes; scan-source rights remain separately recorded.','',
              '## Scope and limits','',*['- '+item for item in LIMITS],'','## Fixed chapter releases','',
              '| Chapter | Release | Publication receipt |','| --- | --- | --- |']
    for r in releases:
        readme.append(f'| {r["chapter"]} | [{r["tag"]}]({r["url"]}) | [Receipt](../{r["receipt"]}) |')
    readme.extend(['','## Reproduction','',
                   '`python scripts/build_golden_aggregate.py build` requires all eight chapter signoffs and receipts, '
                   'runs each final validator, and compares released file contents with their annotated Git tags. '
                   '`verify` regenerates the aggregate in memory and compares exact output bytes without writing. '
                   'The build is deterministic; `golden/` files above are generated, not hand-edited. '
                   'Aggregate final review, signoff, release tag and publication receipt are authored and published separately.',''])
    outputs = {'reading.md':reading_markdown(chapters,releases),'reading.json':gp.serialized(reading),
               'coverage.json':gp.serialized(coverage),'README.md':('\n'.join(readme)+'\n').encode()}
    inputs['scripts/build_golden_aggregate.py'] = gp.file_hash(Path(__file__))
    inputs['scripts/golden_pipeline.py'] = gp.file_hash(Path(gp.__file__))
    manifest = {'schema_version':1,'edition':'bounded-golden-v1','input_sha256':dict(sorted(inputs.items())),
                'chapter_releases':releases,'output_sha256':{name:gp.sha(outputs[name]) for name in FILES},
                'claims':gp.CLAIMS,'method':'Exact concatenation of validated, immutable chapter reading objects; no editorial rewriting or Unicode normalization.'}
    outputs['build-manifest.json'] = gp.serialized(manifest)
    return outputs


def build(root):
    outputs = generate(root)
    dest=root/'golden'
    if (dest/'signoff.json').exists():
        for name,data in outputs.items():
            gp.require((dest/name).is_file() and (dest/name).read_bytes() == data,'Refusing to alter signed aggregate: '+name)
    for name,data in outputs.items():
        gp.write(dest/name,data)
    return {'outputs':len(outputs),'chapters':8,'original_anchors':ORIGINAL_ANCHORS,
            'build_manifest_sha256':gp.file_hash(dest/'build-manifest.json')}


def verify(root):
    outputs=generate(root)
    for name,data in outputs.items():
        path=root/'golden'/name
        gp.require(path.is_file() and path.read_bytes()==data,'Aggregate corruption or nonreproducible output: '+name)
    return {'passed':True,'read_only':True,'chapters':8,'original_anchors':ORIGINAL_ANCHORS,
            'build_manifest_sha256':gp.file_hash(root/'golden/build-manifest.json')}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('command',choices=['build','verify'])
    args=parser.parse_args()
    try:
        result=build(args.root) if args.command=='build' else verify(args.root)
        print(json.dumps(result,ensure_ascii=False,indent=2)); return 0
    except (gp.ValidationError,FileNotFoundError,KeyError,json.JSONDecodeError) as exc:
        print('AGGREGATE VALIDATION ERROR: '+str(exc),file=sys.stderr); return 1

if __name__=='__main__':
    raise SystemExit(main())
