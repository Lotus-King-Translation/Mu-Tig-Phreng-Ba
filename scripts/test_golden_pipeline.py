#!/usr/bin/env python3
"""Isolated structural corruption tests; fixture editorial assertions are synthetic."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile
import golden_pipeline as g

class GoldenPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='mtp-golden-tests-')
        cls.fixture = Path(cls.temp.name)/'fixture'
        cls.fixture.mkdir()
        for rel in (g.BASE, g.COMPARE, 'editions/scans/adzom-1973/image-manifest.json'):
            p = cls.fixture/rel; p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(g.ROOT/rel,p)
        report = g.prepare(cls.fixture)
        assert report == {'anchors':2053,'chapters':8,'differences':0,'anomalies':28}
        g.plan(cls.fixture,1)
        dest = g.chapter_dir(cls.fixture,1)
        contract = g.load(dest/'contract.json')
        anchors = g.load(cls.fixture/'diplomatic/source-anchors.json')['anchors']
        amap = {a['id']: a for a in anchors}
        with zipfile.ZipFile(g.ROOT/'editions/scans/adzom-1973/iiif-response-images.zip') as archive:
            name = next(n for n in archive.namelist() if Path(n).name == '00427.png')
            image = archive.read(name)
        image_rel = 'diplomatic/evidence/SYNTHETIC-TEST-FIXTURE-427.png'
        p = cls.fixture/image_rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(image)
        target_ids = contract['required_decision_anchors']
        evidence = [{'id':'TEST-E001','path':image_rel,'sha256':g.sha(image),
                     'anchor_ids':target_ids,'status':'accepted',
                     'allocation_reason':'Synthetic validator fixture only; NOT an editorial allocation claim.',
                     'inspection':'native_image_direct','source_id':'adzom-1973','image_index':427}]
        decisions = [{'id':f'TEST-D{i}','anchor_id':aid,'old':amap[aid]['text'],'new':amap[aid]['text'],
                      'role':amap[aid]['mechanical_role'],'treatment':'retain_base',
                      'reason':'Synthetic validator fixture only; not editorial approval.',
                      'evidence_ids':['TEST-E001'],'uncertainty':[]}
                     for i,aid in enumerate(target_ids)]
        checks = [{'id':c['id'],'status':'closed','finding':'Synthetic closure for isolated corruption tests only.',
                   'evidence_ids':['TEST-E001'],'uncertainty':[]} for c in contract['source_checks']]
        for name,obj in [('decisions.json',decisions),('evidence.json',evidence),('source-checks.json',checks)]:
            g.write(dest/name,obj)
        g.build(cls.fixture,1)
        g.validate(cls.fixture,1)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.case = tempfile.TemporaryDirectory(prefix='mtp-golden-case-')
        self.root = Path(self.case.name)/'repo'
        shutil.copytree(self.fixture,self.root)
        self.dest = g.chapter_dir(self.root,1)

    def tearDown(self):
        self.case.cleanup()

    def mutate_json(self,path,fn):
        obj = g.load(path); fn(obj); g.write(path,obj)

    def reject(self,fn=None):
        with self.assertRaises(g.ValidationError):
            (fn or (lambda:g.validate(self.root,1)))()

    def sign(self):
        review = self.dest/'FINAL-REVIEW.md'
        review.write_text('Synthetic test review; not editorial certification.\n')
        manifest = g.load(self.dest/'build-manifest.json')
        g.write(self.dest/'signoff.json',{'chapter':1,'approved':True,'reviewer':'synthetic-test',
                'review':'Isolated fixture signoff','review_path':g.relative(self.root,review),
                'review_sha256':g.file_hash(review),'build_manifest_sha256':g.file_hash(self.dest/'build-manifest.json'),
                'output_sha256':manifest['outputs'],'claims':g.CLAIMS})

    def test_positive_reproducibility_and_exact_extraction(self):
        before = {p:g.file_hash(self.dest/p) for p in (*g.OUTPUTS,'build-manifest.json')}
        g.build(self.root,1)
        self.assertEqual(before,{p:g.file_hash(self.dest/p) for p in before})
        anchors = g.load(self.root/'diplomatic/source-anchors.json')['anchors']
        raw = (self.root/g.BASE).read_text()
        for a in anchors:
            self.assertEqual(a['raw_text'], raw[a['raw_start']:a['raw_end']])
            self.assertEqual(a['raw_text'],a['text']+a['line_ending'])
        self.assertEqual(anchors[0]['raw_text'],'\n')
        self.assertEqual(sum(a['wylie_raw_text'].startswith('@') and a['mechanical_role']=='metadata' for a in anchors),8)
        self.assertTrue(g.validate(self.root,1)['passed'])

    def test_unsigned_final_rejects(self):
        self.reject(lambda:g.validate(self.root,1,final=True))

    def test_signed_final_accepts(self):
        self.sign()
        self.assertTrue(g.validate(self.root,1,final=True)['passed'])

    def test_anchor_corruption_rejects(self):
        self.mutate_json(self.root/'diplomatic/source-anchors.json',lambda x:x['anchors'][2].update(text='corrupt'))
        self.reject()

    def test_archival_source_corruption_rejects(self):
        with (self.root/g.BASE).open('ab') as f:f.write(b'!')
        self.reject()

    def test_false_collation_agreement_rejects(self):
        self.mutate_json(self.root/'diplomatic/electronic-collation.json',lambda x:x['loci'][3].update(derived_tibetan='corrupt'))
        self.reject()

    def test_opcode_corruption_rejects(self):
        self.mutate_json(self.root/'diplomatic/electronic-collation.json',lambda x:x['loci'][3]['opcodes'][0].update(old='corrupt'))
        self.reject()

    def test_old_string_corruption_rejects(self):
        self.mutate_json(self.dest/'decisions.json',lambda x:x[0].update(old='corrupt'))
        self.reject()

    def test_role_corruption_rejects(self):
        self.mutate_json(self.dest/'decisions.json',lambda x:x[0].update(role='certified_main_text'))
        self.reject()

    def test_open_queue_rejects(self):
        self.mutate_json(self.dest/'source-checks.json',lambda x:x[0].update(status='open'))
        self.reject()

    def test_evidence_bytes_corruption_rejects(self):
        rel=g.load(self.dest/'evidence.json')[0]['path']
        (self.root/rel).write_bytes(b'corrupt')
        self.reject()

    def test_evidence_allocation_corruption_rejects(self):
        self.mutate_json(self.dest/'evidence.json',lambda x:x[0].update(anchor_ids=[]))
        self.reject()

    def test_excluded_evidence_rejects(self):
        self.mutate_json(self.dest/'evidence.json',lambda x:x[0].update(status='excluded'))
        self.reject()

    def test_evidence_manifest_mismatch_rejects(self):
        self.mutate_json(self.dest/'evidence.json',lambda x:x[0].update(image_index=428))
        self.reject()

    def test_coverage_claim_corruption_rejects(self):
        self.mutate_json(self.dest/'coverage.json',lambda x:x['claims'].update(full_scan_proofreading=True))
        self.reject()

    def test_contract_mutation_rejects(self):
        self.mutate_json(self.dest/'contract.json',lambda x:x.update(required_decision_anchors=[]))
        self.reject()

    def test_restoration_placement_corruption_rejects(self):
        g.write(self.dest/'restorations.json',[{'id':'MTP-R000001','after_anchor':'MTP-S999999',
                'text':'ཀ','role':'main_text','reason':'Synthetic test','evidence_ids':['TEST-E001'],'uncertainty':[]}])
        self.reject()

    def test_duplicate_restoration_rejects(self):
        anchor=g.load(self.dest/'contract.json')['required_decision_anchors'][0]
        item={'id':'MTP-R000001','after_anchor':anchor,'text':'ཀ','role':'main_text',
              'reason':'Synthetic test','evidence_ids':['TEST-E001'],'uncertainty':[]}
        g.write(self.dest/'restorations.json',[item,item])
        self.reject()

    def test_signoff_hash_corruption_rejects(self):
        self.sign()
        self.mutate_json(self.dest/'signoff.json',lambda x:x.update(build_manifest_sha256='0'*64))
        self.reject(lambda:g.validate(self.root,1,final=True))

    def test_review_corruption_rejects(self):
        self.sign()
        (self.dest/'FINAL-REVIEW.md').write_text('changed')
        self.reject(lambda:g.validate(self.root,1,final=True))

    def test_signed_output_mutation_rejects_rebuild(self):
        self.sign()
        self.mutate_json(self.dest/'decisions.json',lambda x:x[0].update(reason='Changed authored reasoning'))
        self.reject(lambda:g.build(self.root,1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
