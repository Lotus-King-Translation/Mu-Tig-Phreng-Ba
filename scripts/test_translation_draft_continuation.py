#!/usr/bin/env python3
"""Scoped draft continuation gates; synthetic fixtures, no semantic claims."""
from pathlib import Path
import shutil
import tempfile
import unittest
import translation_pipeline as t
from test_translation_aggregate import fixture, git


class DraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='mtp-translation-draft-test-')
        self.r=Path(self.tmp.name)/'repo'
        # Construct unsigned target chapters directly; never copy obsolete signoffs
        # into the mutable fixture and then rely on deleting them before a build.
        omitted={f'translations/chapters/{n:02}' for n in self.unsigned_chapters}
        def ignore(path,names):
            return {'contract.json','contract.sha256','qc.json','signoff.json'} if Path(path).relative_to(self.base).as_posix() in omitted else set()
        shutil.copytree(self.base,self.r,ignore=ignore)
        self.commit=git(self.r,'rev-parse','translate-ch02-v1^{commit}')
        # Remove only synthetic publication state, retaining the reviewed candidate.
        for n in range(2,9):
            git(self.r,'tag','-d',f'translate-ch{n:02}-v1')
            (self.r/f'translations/publication/ch{n:02}-v1.json').unlink()
        self.d=t.directory(self.r,3)
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

    def test_chapter_three_authorization_does_not_authorize_chapter_four(self):
        with self.assertRaises(FileNotFoundError):t.prior(self.r,4,self.commit)

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


class ChapterFourDraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3,4}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-ch04-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        DraftContinuationTests.setUp(self)
        DraftContinuationTests.prepare(self)
        # Sign a synthetic chapter 3 with the real legacy draft contract shape.
        d=self.d
        t.write(d/'qc.json',{'chapter':3,'reviewer':'Independent reviewer','translator':'Translator','independent':True,
            'source_sha256':t.digest(d/'source.md'),'translation_sha256':t.digest(d/'translation.md'),
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage':'complete',
            'disposition':'ready_with_explicit_review_flags','open_blockers':[],
            'review_path':'translations/chapters/03/QC.md','review_sha256':t.digest(d/'QC.md')})
        t.write(d/'signoff.json',{'chapter':3,'approved':True,'reviewer':'Coordinator',
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),
            'output_sha256':t.load(d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(d/'qc.json'),
            'review_path':'translations/chapters/03/FINAL.md','review_sha256':t.digest(d/'FINAL.md')})
        t.final_gate(self.r,3)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic signed chapter 3 draft')
        self.latest=git(self.r,'rev-parse','HEAD');self.d=t.directory(self.r,4)
        self.path=self.r/'translations/draft-authorizations/ch04.json'
        t.write(self.path,{'schema_version':2,'chapter':4,'prior_chapter':3,'prior_commit':self.latest,
            'reviewed_priors':[{'chapter':n,'commit':ref,'build_manifest_sha256':t.digest(t.directory(self.r,n)/'build-manifest.json')}
                for n,ref in ((2,self.commit),(3,self.latest))],
            'authorized_scope':'working_draft_only','user_instruction':'excellent, next chapter',
            'date':'2026-10-03','reason':'Synthetic continuation after chapter 3 content review.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic chapter 4 authorization')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,4,self.latest);t.source(self.r,4,self.latest)
        t.assemble(self.r,4,draft_prior_commit=self.latest);t.build(self.r,4,self.latest)

    def change_authorization(self,change):
        a=t.load(self.path);change(a);t.write(self.path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic authorization alteration')

    def test_chapter_four_candidate_preserves_all_prior_chapter_bytes(self):
        before={p:p.read_bytes() for n in (1,2,3) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        legacy=(self.r/'translations/draft-authorizations/ch03.json').read_bytes()
        self.prepare()
        self.assertEqual(t.validate(self.r,4,source_only=True,draft_prior_commit=self.latest)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,4,draft_prior_commit=self.latest)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        self.assertEqual(legacy,(self.r/'translations/draft-authorizations/ch03.json').read_bytes())
        self.assertEqual(t.load(self.d/'build-manifest.json')['input_sha256']['translations/draft-authorizations/ch04.json'],t.digest(self.path))

    def test_chapter_four_default_and_final_gates_remain_strict(self):
        with self.assertRaises(FileNotFoundError):t.prior(self.r,4)
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,4,final=True,draft_prior_commit=self.latest)

    def test_chapter_five_is_not_authorized(self):
        with self.assertRaisesRegex(t.Error,'only for chapters 3 and 4'):t.prior(self.r,5,self.latest)

    def test_chapter_one_actual_receipt_is_required(self):
        (self.r/'translations/publication/ch01-v1.json').unlink()
        with self.assertRaises(FileNotFoundError):t.prior(self.r,4,self.latest)

    def test_both_reviewed_priors_are_required_in_order(self):
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        with self.assertRaisesRegex(t.Error,'exactly chapters 2 and 3'):t.prior(self.r,4,self.latest)
        self.change_authorization(lambda a:a['reviewed_priors'].pop())
        with self.assertRaisesRegex(t.Error,'exactly chapters 2 and 3'):t.prior(self.r,4,self.latest)

    def test_chapter_two_pin_must_match_legacy_authorization(self):
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(commit=self.latest))
        with self.assertRaisesRegex(t.Error,'scope/commit mismatch'):t.prior(self.r,4,self.latest)

    def test_chapter_three_manifest_pin_rejects_corruption(self):
        self.change_authorization(lambda a:a['reviewed_priors'][1].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'manifest pin mismatch'):t.prior(self.r,4,self.latest)

    def test_each_prior_snapshot_is_immutable(self):
        for n in (2,3):
            with self.subTest(chapter=n):
                p=t.directory(self.r,n)/'translation.md';original=p.read_bytes();p.write_bytes(b'Changed prior English')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,4,self.latest)
                finally:p.write_bytes(original)

    def test_invalid_signed_content_cannot_be_blessed_by_repinning(self):
        p=t.directory(self.r,3)/'qc.json';q=t.load(p);q['reviewer']=q['translator'];t.write(p,q)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic invalid prior QC')
        self.latest=git(self.r,'rev-parse','HEAD')
        self.change_authorization(lambda a:(a.update(prior_commit=self.latest),a['reviewed_priors'][1].update(commit=self.latest)))
        with self.assertRaisesRegex(t.Error,'Independent QC'):t.prior(self.r,4,self.latest)

    def test_chapter_four_authorization_must_be_committed_and_frozen(self):
        self.prepare();original=self.path.read_bytes();self.path.write_bytes(original+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,4,self.latest)
        self.path.write_bytes(original)
        self.change_authorization(lambda a:a.update(reason='Different synthetic explanation'))
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,4,draft_prior_commit=self.latest)

    def test_actual_releases_allow_unchanged_chapter_four_outputs(self):
        self.prepare();before={name:(self.d/name).read_bytes() for name in (*t.OUTPUTS,'build-manifest.json')}
        for n,ref in ((2,self.commit),(3,self.latest)):
            tag=f'translate-ch{n:02}-v1';git(self.r,'tag','-a',tag,ref,'-m','Synthetic actual prior release')
            t.write(self.r/f'translations/publication/ch{n:02}-v1.json',{'chapter':n,'tag':tag,'release_commit':ref,
                'remote_peeled_commit':ref,'remote_main_at_release':ref,'remote_tag_object':git(self.r,'rev-parse',tag),
                'build_manifest_sha256':t.digest(t.directory(self.r,n)/'build-manifest.json')})
        self.assertTrue(t.validate(self.r,4)['passed']);self.assertEqual(before,t.candidate(self.r,4))
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.validate(self.r,4,final=True)


if __name__=='__main__':unittest.main(verbosity=2)
