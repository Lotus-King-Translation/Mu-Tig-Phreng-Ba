#!/usr/bin/env python3
"""Synthetic eight-tag aggregate tests; no source/translation semantic claims."""
import copy
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import build_translation_aggregate as a
import translation_pipeline as t


def git(root,*args):
    return t.git(root,*args).decode().strip()


def fixture(root):
    ends=[97,221,341,635,1051,1427,1769,2053]
    rows=[];boundaries=[];chunks=[];first=1
    for n,last in enumerate(ends,1):
        chunk=[]
        for i in range(first,last+1):
            role='blank' if i==first else 'metadata' if i==first+1 else 'heading' if i==first+2 else 'chapter_colophon' if i==last else 'main_text'
            text='' if role=='blank' else '༤༡༨' if role=='metadata' else 'ཀ'
            chunk.append({'id':f'MTP-S{i:06}','source_anchor':f'MTP-S{i:06}','text':text,'role':role,'source_text':text,'source_line_ending':'\n','page_hint':418,'uncertainty':['Synthetic retained uncertainty.'] if i==first+3 else [],'layers':[{'role':'synthetic_source_note','text':'Preserve exact synthetic layer.'}] if i==first+3 else []})
        rows+=chunk;chunks.append(chunk)
        boundaries.append({'chapter':n,'first_object':chunk[0]['id'],'last_object':chunk[-1]['id']})
        t.write(root/f'diplomatic/chapters/{n:02}/changes.json',{'changes':[{'id':f'D{n}','anchor_id':chunk[3]['id'],'old':'ཁ','new':'ཀ'}]})
        first=last+1
    t.write(root/'golden/reading.json',{'objects':rows,'chapter_boundaries':boundaries})
    t.write(root/'glossary.csv',b'Fixed synthetic glossary.\n');t.write(root/'standard.md',b'Fixed synthetic standard.\n')
    git(root,'init','-q');git(root,'config','user.name','Synthetic');git(root,'config','user.email','synthetic@example.invalid')
    git(root,'add','.');git(root,'commit','-qm','Synthetic golden source');git(root,'tag','-a','golden-v1','-m','Synthetic')
    commit=git(root,'rev-parse','HEAD')
    pins={'source_tag':'golden-v1','source_commit':commit,'source_reading_sha256':t.digest(root/'golden/reading.json'),'glossary':'glossary.csv','glossary_sha256':t.digest(root/'glossary.csv'),'standard':'standard.md','standard_sha256':t.digest(root/'standard.md')}
    t.write(root/'translations/PLAN.json',pins)
    t.write(root/'diplomatic/publication/golden-v1.json',{'tag':'golden-v1','release_commit':commit,'remote_peeled_commit':commit,'remote_main_at_release':commit,'remote_tag_object':git(root,'rev-parse','golden-v1')})
    t.write(root/'evidence/synthetic.png',b'Synthetic evidence bytes; not an inspected scan.')
    # Avoid repeatedly checking already constructed releases while preparing the fixture.
    # The tests themselves use the real prior-release checks, annotated tags and signoffs.
    with patch.object(t,'prior',return_value=None):
        for n,chunk in enumerate(chunks,1):
            d=t.directory(root,n);ids=[r['id'] for r in chunk]
            seg=[{'id':f'MTP-{n:02}-{i}','golden_ids':selected,'role':role,'format':fmt,'rationale':'Synthetic grouping.'} for i,(selected,role,fmt) in enumerate([(ids[:2],'source_metadata','prose'),(ids[2:3],'source_heading','h1'),(ids[3:-1],'main_text','verse'),(ids[-1:],'chapter_colophon','prose')],1)]
            t.write(d/'segmentation.json',seg);t.plan(root,n);t.source(root,n)
            image={'image_index':428,'printed_page':418,'path':'evidence/synthetic.png','sha256':t.digest(root/'evidence/synthetic.png'),'anchor_ids':ids,'status':'synthetic_fixture','unresolved':[]}
            finding={'id':f'A{n}','type':'uncertain_reading','anchor_ids':[ids[3]],'golden_reading':'ཀ','adzom_reading':None,'explanation':'Synthetic unresolved source.','english_consequence':'Retain local note.','evidence':[{'path':image['path'],'sha256':image['sha256'],'image_index':428,'printed_page':418,'rows_or_crop':'synthetic row','allocation_reason':'Synthetic test allocation.'}]}
            audit={'chapter':n,'scope':'Synthetic entire chapter','inspector':'Synthetic fixture','images':[image],'anchor_checks':[{'anchor_id':r['id'],'status':'uncertain' if i==3 else r['role'] if r['role'] in {'blank','metadata'} else 'agrees','image_indices':[428],'findings':[finding['id']] if i==3 else []} for i,r in enumerate(chunk)],'findings':[finding],'limits':['Synthetic bytes; no palaeographic claim.']}
            t.write(d/'adzom-audit.json',audit);t.seal_audit(root,n)
            note=f'N{n}';main=seg[2]['id']
            t.write(d/'note-map.json',[{'id':note,'pair_ids':[main],'golden_ids':[ids[3]],'category':'uncertain_reading','obligations':[f'golden-change:D{n}',f'golden-uncertainty:{ids[3]}:0',f'adzom:A{n}']}])
            t.write(d/'pair-status.json',[{'id':p['id'],'status':'nontranslatable' if i==0 else 'unresolved' if i==2 and n==2 else 'translated','reason':'Synthetic explicit disposition.','note_ids':[note] if i==2 else []} for i,p in enumerate(seg)])
            texts=['[Electronic metadata preserved.]',f'Synthetic chapter {n}',f'Synthetic first line.\nSynthetic second line.[^{note}]','Synthetic colophon.']
            english=t.header(pins,n,n,True)+'\n\n'.join(f'<!-- pair: {p["id"]} -->\n\n'+text for p,text in zip(seg,texts))+'\n\n'+t.END+f'\n\n[^{note}]: Synthetic uncertainty and transcript correction.\n    Preserve this continuation exactly.\n'
            t.write(d/'translation.md',english.encode());t.assemble(root,n);t.build(root,n)
            t.write(d/'QC.md',b'Synthetic independent review.\n');t.write(d/'FINAL.md',b'Synthetic final review.\n')
            t.write(d/'qc.json',{'chapter':n,'reviewer':'Independent reviewer','translator':'Translator','independent':True,'source_sha256':t.digest(d/'source.md'),'translation_sha256':t.digest(d/'translation.md'),'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage':'complete','disposition':'ready_with_explicit_review_flags','open_blockers':[],'review_path':f'translations/chapters/{n:02}/QC.md','review_sha256':t.digest(d/'QC.md')})
            t.write(d/'signoff.json',{'chapter':n,'approved':True,'reviewer':'Coordinator','build_manifest_sha256':t.digest(d/'build-manifest.json'),'output_sha256':t.load(d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(d/'qc.json'),'review_path':f'translations/chapters/{n:02}/FINAL.md','review_sha256':t.digest(d/'FINAL.md')})
            t.validate(root,n,final=True)
            git(root,'add','.');git(root,'commit','-qm',f'Synthetic chapter {n}')
            tag=f'translate-ch{n:02}-v1';git(root,'tag','-a',tag,'-m','Synthetic released chapter');commit=git(root,'rev-parse','HEAD')
            t.write(root/f'translations/publication/ch{n:02}-v1.json',{'chapter':n,'tag':tag,'release_commit':commit,'remote_peeled_commit':commit,'remote_main_at_release':commit,'remote_tag_object':git(root,'rev-parse',tag),'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage_sha256':t.digest(d/'coverage.json')})
    git(root,'add','.');git(root,'commit','-qm','Synthetic last receipt')


class AggregateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-aggregate-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)
        cls.data=a.collect(cls.base)
        a.build(cls.base)
    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mtp-translation-aggregate-test-');self.r=Path(self.tmp.name)/'repo';shutil.copytree(self.base,self.r)
    def tearDown(self):self.tmp.cleanup()
    def fails(self,pattern):
        with self.assertRaisesRegex(t.Error,pattern):a.verify(self.r)
    def change(self,relative,old,new):
        p=self.r/relative;p.write_text(p.read_text().replace(old,new))
    def test_complete_identity_and_readonly(self):
        before={str(p.relative_to(self.r)):(p.stat().st_mtime_ns,t.digest(p)) for p in self.r.rglob('*') if p.is_file() and '.git' not in p.parts}
        self.assertTrue(a.verify(self.r)['read_only'])
        self.assertEqual(before,{str(p.relative_to(self.r)):(p.stat().st_mtime_ns,t.digest(p)) for p in self.r.rglob('*') if p.is_file() and '.git' not in p.parts})
        machine=t.load(self.r/'translations/machine.json');coverage=t.load(self.r/'translations/coverage.json')
        self.assertEqual([g for p in machine['pairs'] for g in p['golden_objects']],t.load(self.r/'golden/reading.json')['objects'])
        self.assertEqual(coverage['source_objects_represented'],2053);self.assertEqual(coverage['totals']['obligations_covered'],24)
        self.assertEqual(sum(coverage['source_objects_by_pair_treatment'].values()),2053)
        self.assertEqual(coverage['claims'],t.CLAIMS);self.assertEqual(len(machine['endnotes']),8)
        for note in machine['endnotes']:
            for name in ('reading.md','bilingual.md'):self.assertIn(note['raw'],(self.r/'translations'/name).read_text().split('## Endnotes\n')[1])
    def test_bilingual_verse_display_preserves_raw_pairs(self):
        pair={'id':'MTP-DISPLAY-1','format':'verse','role':'main_text',
              'source':'ཀ་\nཁ་\nག་','translation':'First line.\nSecond line.\nThird line.[^N1]'}
        chapters=[{'chapter':1,'pairs':[pair]}]
        notes=[{'raw':'[^N1]: Preserve the exact note.\n    And its continuation.'}]
        before=copy.deepcopy((chapters,notes))
        shown=a.render(chapters,notes,True).decode()
        self.assertIn('<!-- pair: MTP-DISPLAY-1; format: verse; role: main_text -->\n\n',shown)
        self.assertIn('ཀ་  \nཁ་  \nག་\n\nFirst line.  \nSecond line.  \nThird line.[^N1]',shown)
        self.assertEqual(shown.count('<a id="mtp-display-1"></a>'),1)
        self.assertIn(notes[0]['raw'],shown)
        self.assertEqual((chapters,notes),before)
    def test_bilingual_headings_and_non_main_roles_are_visible(self):
        pairs=[{'id':f'MTP-H{level}','format':f'h{level}','role':'source_heading',
                'source':f'ཀ་{level}','translation':f'Heading {level}'} for level in (1,2,3)]
        roles=('annotation','source_annotation','colophon','work_colophon','chapter_colophon','metadata','source_metadata','blank')
        pairs += [{'id':f'MTP-R{index}','format':'prose','role':role,
                   'source':'ཀ་\nཁ་','translation':f'{role} first line.\nSecond line.'}
                  for index,role in enumerate(roles,1)]
        chapters=[{'chapter':1,'pairs':pairs}];before=copy.deepcopy(chapters)
        bilingual=a.render(chapters,[],True).decode();english=a.render(chapters,[]).decode()
        for level in (1,2,3):
            self.assertIn('\n'+'#'*level+f' ཀ་{level}\n',bilingual)
            self.assertIn('\n'+'#'*level+f' Heading {level}\n',bilingual)
        for role in roles:
            self.assertIn(f'> [{role}] ཀ་\n> ཁ་',bilingual)
            self.assertIn(f'> [{role}] {role} first line.\n> Second line.',bilingual)
            self.assertIn(f'> [{role}] {role} first line.\n> Second line.',english)
        for pair in pairs:
            self.assertEqual(bilingual.count(f'<a id="{pair["id"].lower()}"></a>'),1)
            self.assertIn(f'<!-- pair: {pair["id"]}; format: {pair["format"]}; role: {pair["role"]} -->',bilingual)
        self.assertEqual(chapters,before)
    def test_missing_chapter_refuses_without_writes(self):
        shutil.rmtree(t.directory(self.r,8));p=self.r/'translations/reading.md';before=p.read_bytes()
        with self.assertRaisesRegex(t.Error,'Missing translation chapter 8'):a.build(self.r)
        self.assertEqual(p.read_bytes(),before)
    def test_missing_receipt_rejects(self):
        (self.r/'translations/publication/ch08-v1.json').unlink();self.fails('publication receipt required')
    def test_changed_released_pair_rejects(self):
        self.change('translations/chapters/01/translation.md','Synthetic first line.','Changed first line.');self.fails('Prior released bytes changed')
    def test_changed_canonical_pair_rejects(self):
        self.change('paired/translation.md','Synthetic first line.','Changed first line.');self.fails('Canonical prefix differs')
    def test_changed_canonical_note_rejects(self):
        self.change('paired/translation.md','Preserve this continuation exactly.','Changed endnote.');self.fails('Canonical prefix differs')
    def test_changed_source_rejects(self):
        self.change('paired/source.md','ཀ','ཁ');self.fails('Canonical prefix differs')
    def test_changed_chapter_manifest_rejects(self):
        p=t.directory(self.r,1)/'build-manifest.json';p.write_bytes(p.read_bytes()+b' ');self.fails('Prior manifest changed')
    def test_changed_golden_source_rejects(self):
        p=self.r/'golden/reading.json';p.write_bytes(p.read_bytes()+b' ');self.fails('Prior released input changed')
    def test_changed_glossary_rejects(self):
        (self.r/'glossary.csv').write_bytes(b'Changed glossary');self.fails('Prior released input changed')
    def test_changed_tag_object_rejects(self):
        git(self.r,'tag','-d','translate-ch01-v1');git(self.r,'tag','-a','translate-ch01-v1','-m','Changed tag');self.fails('Prior tag object changed')
    def test_changed_receipt_coverage_rejects(self):
        p=self.r/'translations/publication/ch01-v1.json';obj=t.load(p);obj['coverage_sha256']='0'*64;t.write(p,obj);self.fails('Receipt coverage hash changed')
    def test_changed_qc_review_rejects(self):
        (t.directory(self.r,1)/'QC.md').write_text('Changed review');self.fails('Prior released bytes changed')
    def test_unsigned_chapter_rejects(self):
        (t.directory(self.r,8)/'signoff.json').unlink();self.fails('missing signoff.json')
    def test_changed_output_rejects(self):
        (self.r/'translations/reading.md').write_text('Changed aggregate');self.fails('Aggregate corruption')
    def test_changed_aggregate_manifest_rejects(self):
        p=self.r/'translations/build-manifest.json';p.write_bytes(p.read_bytes()+b' ');self.fails('Aggregate corruption')
    def test_signed_aggregate_cannot_regenerate_changed_bytes(self):
        t.write(self.r/'translations/signoff.json',{'approved':True});(self.r/'translations/reading.md').write_text('Changed aggregate')
        with self.assertRaisesRegex(t.Error,'Refusing to change signed'):a.build(self.r)
    def sequence(self,mutate):
        chapters=copy.deepcopy(self.data[0]);mutate(chapters)
        _,sp,_=t.parse((self.r/'paired/source.md').read_text());_,ep,defs=t.parse((self.r/'paired/translation.md').read_text(),True)
        a.verify_sequence(chapters,t.load(self.r/'golden/reading.json')['objects'],sp,ep,defs)
    def test_duplicate_golden_object_rejects(self):
        with self.assertRaisesRegex(t.Error,'Golden objects changed'):
            self.sequence(lambda cs:cs[1]['pairs'][2]['golden_objects'].append(cs[0]['pairs'][2]['golden_objects'][0]))
    def test_dropped_golden_layer_rejects(self):
        with self.assertRaisesRegex(t.Error,'Golden objects changed'):
            self.sequence(lambda cs:cs[0]['pairs'][2]['golden_objects'][0].update(layers=[]))
    def test_duplicate_note_id_rejects(self):
        with self.assertRaisesRegex(t.Error,'Duplicate aggregate endnote'):
            self.sequence(lambda cs:cs[1]['endnotes'][0].update(id=cs[0]['endnotes'][0]['id']))
    def test_missing_obligation_rejects(self):
        d=t.directory(self.r,1);mapping=t.load(d/'note-map.json');mapping[0]['obligations'].pop();t.write(d/'note-map.json',mapping)
        with self.assertRaisesRegex(t.Error,'obligations missing'):a.chapter(self.r,1)

if __name__=='__main__':unittest.main(verbosity=2)
