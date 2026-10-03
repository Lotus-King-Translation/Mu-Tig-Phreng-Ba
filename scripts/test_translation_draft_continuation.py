#!/usr/bin/env python3
"""Scoped draft continuation gates; synthetic fixtures, no semantic claims."""
from pathlib import Path
import shutil
import tempfile
import unittest
import translation_pipeline as t
from test_translation_aggregate import fixture, git


class DraftContinuationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mtp-translation-draft-test-')
        self.r=Path(self.tmp.name)/'repo';shutil.copytree(self.base,self.r)
        self.commit=git(self.r,'rev-parse','translate-ch02-v1^{commit}')
        # Remove only synthetic publication state, retaining the reviewed candidate.
        for n in range(2,9):
            git(self.r,'tag','-d',f'translate-ch{n:02}-v1')
            (self.r/f'translations/publication/ch{n:02}-v1.json').unlink()
        self.d=t.directory(self.r,3)
        for name in ('contract.json','contract.sha256','qc.json','signoff.json'):(self.d/name).unlink()
        self.path=self.r/'translations/draft-authorizations/ch03.json'
        t.write(self.path,{'schema_version':1,'chapter':3,'prior_chapter':2,'prior_commit':self.commit,
            'prior_build_manifest_sha256':t.digest(t.directory(self.r,2)/'build-manifest.json'),
            'authorized_scope':'working_draft_only','user_instruction':'excellent, move to chapter 3 then',
            'date':'2026-10-03','reason':'Synthetic terminal publication blocker.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic authorized continuation')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,3,self.commit);t.source(self.r,3,self.commit)
        t.assemble(self.r,3,draft_prior_commit=self.commit)
        t.build(self.r,3,self.commit)

    def test_draft_source_and_candidate_with_fixed_prior_bytes(self):
        before={p:p.read_bytes() for n in (1,2) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        self.prepare()
        self.assertEqual(t.validate(self.r,3,source_only=True,draft_prior_commit=self.commit)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,3,draft_prior_commit=self.commit)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        manifest=t.load(self.d/'build-manifest.json')
        self.assertEqual(manifest['input_sha256']['translations/draft-authorizations/ch03.json'],t.digest(self.path))

    def test_default_path_still_requires_actual_prior_receipt(self):
        with self.assertRaises(FileNotFoundError):t.prior(self.r,3)

    def test_final_rejects_draft_flag_even_before_artifact_checks(self):
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,3,final=True,draft_prior_commit=self.commit)

    def test_exception_cannot_extend_to_chapter_four(self):
        with self.assertRaisesRegex(t.Error,'only for chapter 3'):t.prior(self.r,4,self.commit)

    def test_uncommitted_authorization_rejects(self):
        self.path.write_bytes(self.path.read_bytes()+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,3,self.commit)

    def test_wrong_commit_or_manifest_pin_rejects(self):
        with self.assertRaisesRegex(t.Error,'scope/commit mismatch'):t.prior(self.r,3,git(self.r,'rev-parse','HEAD'))
        a=t.load(self.path);a['prior_build_manifest_sha256']='0'*64;t.write(self.path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic invalid manifest pin')
        with self.assertRaisesRegex(t.Error,'manifest pin mismatch'):t.prior(self.r,3,self.commit)

    def test_prior_candidate_mutation_rejects(self):
        (t.directory(self.r,2)/'translation.md').write_text('Changed prior candidate')
        with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,3,self.commit)

    def test_prior_input_mutation_rejects(self):
        (self.r/'evidence/synthetic.png').write_bytes(b'Changed evidence')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,3,self.commit)

    def test_changed_committed_authorization_invalidates_frozen_contract(self):
        self.prepare();a=t.load(self.path);a['reason']='Changed synthetic authorization';t.write(self.path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed authorization')
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,3,draft_prior_commit=self.commit)

    def test_real_prior_release_allows_same_outputs_under_strict_checks(self):
        self.prepare();before={name:(self.d/name).read_bytes() for name in (*t.OUTPUTS,'build-manifest.json')}
        tag='translate-ch02-v1';git(self.r,'tag','-a',tag,self.commit,'-m','Synthetic actual prior release')
        t.write(self.r/'translations/publication/ch02-v1.json',{'chapter':2,'tag':tag,'release_commit':self.commit,
            'remote_peeled_commit':self.commit,'remote_main_at_release':self.commit,
            'remote_tag_object':git(self.r,'rev-parse',tag),'build_manifest_sha256':t.digest(t.directory(self.r,2)/'build-manifest.json')})
        self.assertTrue(t.validate(self.r,3)['passed'])
        self.assertEqual(before,t.candidate(self.r,3))
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.validate(self.r,3,final=True)


if __name__=='__main__':unittest.main(verbosity=2)
