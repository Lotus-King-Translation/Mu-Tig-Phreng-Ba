#!/usr/bin/env python3
"""Synthetic final-gate mutations; no real approval, publication or semantic claim."""
from pathlib import Path
import shutil
import tempfile
import unittest
import build_translation_aggregate as aggregate
import translation_pipeline as t
import validate_translation_aggregate as final
from test_translation_aggregate import fixture


class AggregateSignoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-aggregate-signoff-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base);aggregate.build(cls.base)
        t.write(cls.base/final.SELF,Path(final.__file__).read_bytes())
        t.write(cls.base/'translations/FINAL-REVIEW.md',b'Synthetic aggregate review, not a real translation approval.\n')
        t.write(cls.base/'translations/QC.md',b'Synthetic independent assembly review.\n')
        manifest=t.load(cls.base/'translations/build-manifest.json')
        t.write(cls.base/'translations/signoff.json',{
            'edition':'translation-v1','approved':True,'reviewer':'Synthetic coordinator',
            'review_path':'translations/FINAL-REVIEW.md',
            'review_sha256':t.digest(cls.base/'translations/FINAL-REVIEW.md'),
            'build_manifest_sha256':t.digest(cls.base/'translations/build-manifest.json'),
            'output_sha256':manifest['output_sha256'],'claims':t.CLAIMS,
            'supporting_sha256':{p:t.digest(cls.base/p) for p in (final.SELF,'translations/QC.md')}})

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mtp-aggregate-signoff-test-')
        self.root=Path(self.tmp.name)/'repo';shutil.copytree(self.base,self.root)
        self.signoff=self.root/'translations/signoff.json'

    def tearDown(self):self.tmp.cleanup()

    def change(self,mutate):
        value=t.load(self.signoff);mutate(value);t.write(self.signoff,value)

    def fails(self,message):
        with self.assertRaisesRegex(t.Error,message):final.verify(self.root)

    def test_signed_gate_is_readonly(self):
        def snapshot():
            return {p.relative_to(self.root).as_posix():(p.stat().st_mtime_ns,t.digest(p))
                    for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        before=snapshot();result=final.verify(self.root)
        self.assertTrue(result['passed']);self.assertTrue(result['read_only'])
        self.assertEqual(result['mode'],'final');self.assertFalse(result['remote_refs_verified'])
        self.assertEqual(result['signoff_sha256'],t.digest(self.signoff))
        self.assertEqual(snapshot(),before)

    def test_unsigned_rejects(self):
        self.signoff.unlink();self.fails('Unsigned translation aggregate')

    def test_prior_release_gate_still_applies(self):
        (self.root/'translations/publication/ch08-v1.json').unlink()
        self.fails('publication receipt required')

    def test_approval_must_be_boolean_true(self):
        self.change(lambda s:s.update(approved=1));self.fails('Aggregate approval missing')

    def test_wrong_edition_rejects(self):
        self.change(lambda s:s.update(edition='golden-v1'));self.fails('edition mismatch')

    def test_blank_reviewer_rejects(self):
        self.change(lambda s:s.update(reviewer='  '));self.fails('reviewer missing')

    def test_obsolete_manifest_binding_rejects(self):
        self.change(lambda s:s.update(build_manifest_sha256='0'*64));self.fails('manifest hash mismatch')

    def test_changed_review_rejects(self):
        (self.root/'translations/FINAL-REVIEW.md').write_text('Changed review.\n')
        self.fails('review hash mismatch')

    def test_review_outside_repository_rejects(self):
        self.change(lambda s:s.update(review_path='../outside.md'))
        self.fails('Path outside repository')

    def test_output_mapping_cannot_drop_a_file(self):
        self.change(lambda s:s['output_sha256'].pop('bilingual.md'))
        self.fails('output hash mapping mismatch')

    def test_output_corruption_still_rejects(self):
        (self.root/'translations/reading.md').write_text('Corrupt aggregate.\n')
        self.fails('Aggregate corruption')

    def test_certification_claim_rejects(self):
        self.change(lambda s:s['claims'].update(automated_semantic_certification=True))
        self.fails('Unsupported aggregate certification claim')

    def test_claim_false_must_be_boolean(self):
        self.change(lambda s:s['claims'].update(independent_human_certification=0))
        self.fails('Unsupported aggregate certification claim')

    def test_validator_binding_is_required(self):
        self.change(lambda s:s['supporting_sha256'].pop(final.SELF))
        self.fails('must bind its final validator')

    def test_changed_supporting_review_rejects(self):
        (self.root/'translations/QC.md').write_text('Changed supporting review.\n')
        self.fails('supporting record hash mismatch')

    def test_different_executing_validator_rejects(self):
        helper=self.root/final.SELF;helper.write_text('Different validator.\n')
        self.change(lambda s:s['supporting_sha256'].update({final.SELF:t.digest(helper)}))
        self.fails('Executing aggregate validator differs')

    def test_validation_report_cannot_form_a_binding_cycle(self):
        report=self.root/'translations/validation.json';t.write(report,{'synthetic':True})
        self.change(lambda s:s['supporting_sha256'].update({'translations/validation.json':t.digest(report)}))
        self.fails('Cyclic aggregate signoff/validation binding')


if __name__=='__main__':unittest.main(verbosity=2)
