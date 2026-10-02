#!/usr/bin/env python3
"""Synthetic structural gates only: no Tibetan semantic certification."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import translation_pipeline as t

class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mtp-translation-tests-');self.r=Path(self.tmp.name);self.d=t.directory(self.r,1)
        self.rows=[{'id':f'MTP-S{i:06}','source_anchor':f'MTP-S{i:06}','text':text,'role':role,'source_text':text,'source_line_ending':'\n','page_hint':418,'uncertainty':unc,'layers':[]} for i,(text,role,unc) in enumerate([('', 'blank',[]),('༤༡༨','metadata',[]),('ཀ','heading',[]),('ཁ','main_text',['Synthetic uncertain source.']),('ག','chapter_colophon',[])],1)]
        self.changes=[{'id':'D4','anchor_id':'MTP-S000004','old':'ང','new':'ཁ'}]
        self.seg=[{'id':'MTP-000001','golden_ids':['MTP-S000001','MTP-S000002'],'role':'source_metadata','format':'prose','rationale':'Synthetic leading blank and metadata.'},{'id':'MTP-000002','golden_ids':['MTP-S000003'],'role':'source_heading','format':'h1','rationale':'Synthetic heading.'},{'id':'MTP-000003','golden_ids':['MTP-S000004'],'role':'main_text','format':'verse','rationale':'Synthetic verse.'},{'id':'MTP-000004','golden_ids':['MTP-S000005'],'role':'chapter_colophon','format':'prose','rationale':'Synthetic closing material.'}]
        for path,data in [('golden/reading.json',{'objects':self.rows,'chapter_boundaries':[{'chapter':1,'first_object':'MTP-S000001','last_object':'MTP-S000005'}]}),('diplomatic/chapters/01/changes.json',{'changes':self.changes})]:t.write(self.r/path,data)
        t.write(self.r/'glossary.csv',b'unchanged glossary\n');t.write(self.r/'standard.md',b'unchanged guidance\n')
        self.git('init','-q');self.git('config','user.name','Synthetic');self.git('config','user.email','synthetic@example.invalid');self.git('add','.');self.git('commit','-qm','Fixture');self.git('tag','-a','golden-v1','-m','Synthetic')
        self.pins={'source_tag':'golden-v1','source_commit':self.git('rev-parse','HEAD').strip(),'source_reading_sha256':t.digest(self.r/'golden/reading.json'),'glossary':'glossary.csv','glossary_sha256':t.digest(self.r/'glossary.csv'),'standard':'standard.md','standard_sha256':t.digest(self.r/'standard.md')}
        t.write(self.r/'translations/PLAN.json',self.pins);t.write(self.d/'segmentation.json',self.seg)
        t.plan(self.r,1);t.source(self.r,1)
        t.write(self.r/'evidence/synthetic.png',b'synthetic bytes, not an inspected image')
        image={'image_index':428,'printed_page':418,'path':'evidence/synthetic.png','sha256':t.digest(self.r/'evidence/synthetic.png'),'anchor_ids':[x['id'] for x in self.rows],'status':'synthetic_fixture','unresolved':[]}
        self.a={'chapter':1,'scope':'Synthetic full fixture','inspector':'Synthetic test','images':[image],'anchor_checks':[{'anchor_id':r['id'],'status':'uncertain' if i==3 else ('blank' if i==0 else 'agrees'),'image_indices':[428],'findings':['A1'] if i==3 else []} for i,r in enumerate(self.rows)],'findings':[{'id':'A1','type':'uncertain_reading','anchor_ids':['MTP-S000004'],'golden_reading':'ཁ','adzom_reading':None,'explanation':'Synthetic source uncertainty.','english_consequence':'Retain an explicit note.','evidence':[{'path':image['path'],'sha256':image['sha256'],'image_index':428,'printed_page':418,'rows_or_crop':'synthetic row','allocation_reason':'Synthetic allocation.'}]}],'limits':['Synthetic fixture, no source certification.']}
        t.write(self.d/'adzom-audit.json',self.a);t.seal_audit(self.r,1)
        self.note_map=[{'id':'N1','pair_ids':['MTP-000003'],'golden_ids':['MTP-S000004'],'category':'uncertain_reading','obligations':['golden-change:D4','golden-uncertainty:MTP-S000004:0','adzom:A1']}]
        t.write(self.d/'note-map.json',self.note_map)
        self.status=[{'id':p['id'],'status':'nontranslatable' if i==0 else ('unresolved' if i==2 else 'translated'),'reason':'Synthetic disposition.','note_ids':['N1'] if i==2 else []} for i,p in enumerate(self.seg)]
        t.write(self.d/'pair-status.json',self.status)
        bodies=['[Electronic metadata preserved.]','Synthetic title','Synthetic unresolved verse.[^N1]','Synthetic colophon.']
        text=t.header(self.pins,1,1,True)+'\n\n'.join(f'<!-- pair: {p["id"]} -->\n\n{b}' for p,b in zip(self.seg,bodies))+'\n\n'+t.END+'\n\n[^N1]: Synthetic source question, correction and retained uncertainty.\n'
        t.write(self.d/'translation.md',text.encode());t.assemble(self.r,1);t.build(self.r,1)
    def tearDown(self):self.tmp.cleanup()
    def git(self,*args):return subprocess.check_output(['git',*args],cwd=self.r,text=True)
    def mutate(self,name,fn):
        p=self.d/name;x=t.load(p);fn(x);t.write(p,x)
    def fails(self,pattern):
        with self.assertRaisesRegex(t.Error,pattern):t.validate(self.r,1)
    def test_valid_candidate_and_leading_blank(self):
        self.assertTrue(t.validate(self.r,1)['passed']);_,pairs,_=t.parse((self.d/'source.md').read_text());self.assertEqual(pairs[0]['text'],'\n༤༡༨')
        m=t.load(self.d/'machine.json');self.assertEqual([x['role'] for x in m['pairs'][0]['golden_objects']],['blank','metadata'])
    def test_source_only_needs_no_english_or_audit(self):
        (self.d/'translation.md').unlink();(self.d/'adzom-audit.json').unlink();self.assertTrue(t.validate(self.r,1,source_only=True)['passed'])
    def test_unsigned_final_rejects(self):
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.validate(self.r,1,final=True)
    def test_source_mutation_rejects(self):
        p=self.d/'source.md';p.write_text(p.read_text().replace('ཁ','ཅ'));self.fails('Source text differs')
    def test_glossary_mutation_rejects(self):
        (self.r/'glossary.csv').write_bytes(b'changed');self.fails('glossary changed')
    def test_golden_mutation_rejects(self):
        p=self.r/'golden/reading.json';p.write_bytes(p.read_bytes()+b' ');self.fails('Golden source bytes changed')
    def test_segmentation_change_rejects(self):
        self.mutate('segmentation.json',lambda x:x[2].update(format='prose'));self.fails('Frozen segmentation')
    def test_duplicate_and_reordered_coverage_rejects(self):
        self.mutate('segmentation.json',lambda x:x[2]['golden_ids'].append('MTP-S000004'));self.fails('omitted, duplicated or reordered')
        reordered=copy.deepcopy(self.seg);reordered[1],reordered[2]=reordered[2],reordered[1];t.write(self.d/'segmentation.json',reordered)
        self.fails('omitted, duplicated or reordered')
    def test_missing_closing_material_rejects(self):
        self.mutate('segmentation.json',lambda x:x.pop());self.fails('omitted, duplicated or reordered')
    def test_cross_role_pair_rejects(self):
        self.mutate('segmentation.json',lambda x:x[2]['golden_ids'].append('MTP-S000005'));self.fails('source-role boundary')
    def test_unset_edition_rejects(self):
        p=self.d/'source.md';p.write_text(p.read_text().replace('edition: golden-v1','edition: unset'));self.fails('Front matter')
    def test_format_on_english_rejects(self):
        p=self.r/'paired/translation.md';p.write_text(p.read_text().replace('pair: MTP-000001 -->','pair: MTP-000001 | format: prose -->'));self.fails('pair metadata')
    def test_canonical_prefix_mutation_rejects(self):
        p=self.r/'paired/translation.md';p.write_text(p.read_text().replace('Synthetic title','Different title'));self.fails('Canonical prefix differs')
    def test_missing_uncertainty_obligation_rejects(self):
        self.mutate('note-map.json',lambda x:x[0]['obligations'].remove('golden-uncertainty:MTP-S000004:0'));self.fails('obligations missing')
    def test_missing_adzom_obligation_rejects(self):
        self.mutate('note-map.json',lambda x:x[0]['obligations'].remove('adzom:A1'));self.fails('obligations missing')
    def test_missing_change_obligation_rejects(self):
        self.mutate('note-map.json',lambda x:x[0]['obligations'].remove('golden-change:D4'));self.fails('obligations missing')
    def test_note_misclassification_rejects(self):
        self.mutate('note-map.json',lambda x:x[0].update(category='transcript_correction'));self.fails('misclassified')
    def test_missing_note_reference_rejects(self):
        p=self.d/'translation.md';p.write_text(p.read_text().replace('verse.[^N1]','verse.'));t.assemble(self.r,1);self.fails('marker missing')
    def test_placeholder_rejects(self):
        p=self.d/'translation.md';p.write_text(p.read_text().replace('Synthetic title','TODO'));t.assemble(self.r,1);self.fails('Placeholder')
    def test_audit_gap_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x['anchor_checks'].pop());self.fails('omits/adds')
    def test_substantive_audit_without_image_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x['anchor_checks'][2].update(image_indices=[]));self.fails('lacks native allocation')
    def test_uncertain_without_finding_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x['anchor_checks'][3].update(findings=[]));self.fails('lacks finding')
    def test_changed_evidence_rejects(self):
        (self.r/'evidence/synthetic.png').write_bytes(b'changed');self.fails('image hash mismatch')
    def test_postseal_finding_mutation_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x['findings'][0].update(explanation='A new observation'));self.fails('changed after seal')
    def test_footnote_definition_midtext_rejects(self):
        p=self.r/'paired/translation.md';p.write_text(p.read_text().replace('Synthetic title','Synthetic title\n[^X]: Hidden note'));self.fails('inside pair body')
    def test_output_corruption_rejects(self):
        (self.d/'reading.md').write_text('corrupt');self.fails('Output corruption')
    def test_read_only_validation(self):
        before={p:p.stat().st_mtime_ns for p in self.d.iterdir()};t.validate(self.r,1);self.assertEqual(before,{p:p.stat().st_mtime_ns for p in self.d.iterdir()})
    def signoff(self):
        t.write(self.d/'QC.md',b'Synthetic independent QC.\n');t.write(self.d/'FINAL.md',b'Synthetic final review.\n')
        q={'chapter':1,'reviewer':'Reviewer','translator':'Translator','independent':True,'source_sha256':t.digest(self.d/'source.md'),'translation_sha256':t.digest(self.d/'translation.md'),'build_manifest_sha256':t.digest(self.d/'build-manifest.json'),'coverage':'complete','disposition':'ready_with_explicit_review_flags','open_blockers':[],'review_path':'translations/chapters/01/QC.md','review_sha256':t.digest(self.d/'QC.md')};t.write(self.d/'qc.json',q)
        s={'chapter':1,'approved':True,'reviewer':'Coordinator','build_manifest_sha256':t.digest(self.d/'build-manifest.json'),'output_sha256':t.load(self.d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(self.d/'qc.json'),'review_path':'translations/chapters/01/FINAL.md','review_sha256':t.digest(self.d/'FINAL.md')};t.write(self.d/'signoff.json',s)
        return q
    def test_final_hash_bound_qc(self):
        q=self.signoff()
        self.assertTrue(t.validate(self.r,1,final=True)['passed']);q['translator']='Reviewer';t.write(self.d/'qc.json',q)
        with self.assertRaisesRegex(t.Error,'Independent QC'):t.validate(self.r,1,final=True)
    def test_previous_release_mutation_rejects(self):
        self.signoff();self.git('add','.');self.git('commit','-qm','Synthetic chapter release');self.git('tag','-a','translate-ch01-v1','-m','Synthetic chapter')
        commit=self.git('rev-parse','HEAD').strip();receipt={'chapter':1,'tag':'translate-ch01-v1','release_commit':commit,'remote_peeled_commit':commit,'remote_main_at_release':commit,'remote_tag_object':self.git('rev-parse','translate-ch01-v1').strip(),'build_manifest_sha256':t.digest(self.d/'build-manifest.json')};t.write(self.r/'translations/publication/ch01-v1.json',receipt)
        t.prior(self.r,2);(self.d/'translation.md').write_text('mutated release')
        with self.assertRaisesRegex(t.Error,'Prior released bytes'):t.prior(self.r,2)
    def test_previous_canonical_mutation_rejects(self):
        p=self.r/'paired/translation.md';p.write_text(p.read_text().replace('Synthetic title','Changed prior title'))
        with self.assertRaisesRegex(t.Error,'Previously released canonical'):t.released_prefix_guard(self.r,2)

    def test_mixed_source_final_modes_reject(self):
        with self.assertRaisesRegex(t.Error,'incompatible'):t.validate(self.r,1,source_only=True,final=True)
    def test_audit_reading_not_in_golden_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x['findings'][0].update(golden_reading='ཆ'))
        self.fails('exact selected span')
    def test_audit_missing_image_page_rejects(self):
        self.mutate('adzom-audit.json',lambda x:x.update(images=[]));self.fails('page/image coverage incomplete')
    def test_stale_qc_after_draft_change_rejects(self):
        self.signoff();(self.d/'signoff.json').unlink()
        p=self.d/'translation.md';p.write_text(p.read_text().replace('Synthetic title','Revised title'));t.assemble(self.r,1);t.build(self.r,1)
        t.write(self.d/'signoff.json',{'chapter':1,'approved':True})
        with self.assertRaisesRegex(t.Error,'QC bound to obsolete'):t.validate(self.r,1,final=True)
    def test_reseal_cannot_drop_obligation(self):
        self.a['anchor_checks'][3].update(status='agrees',findings=[]);self.a['findings']=[];t.write(self.d/'adzom-audit.json',self.a)
        with self.assertRaisesRegex(t.Error,'Cannot remove sealed'):t.seal_audit(self.r,1)

    def test_author_note_map_and_original_draft_hash_bound(self):
        t.write(self.d/'translation-note-map.json',[])
        t.write(self.d/'translation-draft.md',(self.d/'translation.md').read_bytes())
        t.build(self.r,1)
        m=t.load(self.d/'build-manifest.json')['input_sha256']
        self.assertEqual(m['translations/chapters/01/translation-note-map.json'],t.digest(self.d/'translation-note-map.json'))
        self.assertEqual(m['translations/chapters/01/translation-draft.md'],t.digest(self.d/'translation-draft.md'))
        (self.d/'translation-draft.md').write_text('mutated author draft')
        self.fails('Output corruption')

if __name__=='__main__':unittest.main(verbosity=2)
