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
        with self.assertRaises(FileNotFoundError):t.prior(self.r,5,self.latest)

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


class ChapterFiveDraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3,4,5}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-ch05-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        ChapterFourDraftContinuationTests.setUp(self)
        ChapterFourDraftContinuationTests.prepare(self)
        # Give chapter 4 its own real manifest-bound evidence, so mutation tests
        # exercise its unsigned gate rather than fail on a signed predecessor.
        evidence='evidence/ch04-synthetic.png'
        t.write(self.r/evidence,(self.r/'evidence/synthetic.png').read_bytes())
        audit=t.load(self.d/'adzom-audit.json')
        for image in audit['images']:image['path']=evidence
        for finding in audit['findings']:
            for item in finding['evidence']:item['path']=evidence
        t.write(self.d/'adzom-audit.json',audit)
        t.seal_audit(self.r,4,self.latest);t.build(self.r,4,self.latest)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic saved unsigned chapter 4')
        self.saved=git(self.r,'rev-parse','HEAD')
        reviewed=t.load(self.path)['reviewed_priors']
        self.path=self.r/'translations/draft-authorizations/ch05.json';self.d=t.directory(self.r,5)
        t.write(self.path,{'schema_version':3,'chapter':5,'prior_chapter':4,'prior_commit':self.saved,
            'reviewed_priors':reviewed,'unsigned_prior':{'chapter':4,'commit':self.saved,
                'build_manifest_sha256':t.digest(t.directory(self.r,4)/'build-manifest.json'),
                'snapshot_tree_sha':git(self.r,'rev-parse',self.saved+':translations/chapters/04'),
                'review_state':'unsigned_saved_draft'},
            'authorized_scope':'working_draft_only','user_instruction':'cool, then move on to next chapter',
            'date':'2026-10-03','reason':'Synthetic explicit continuation after disclosure of lost final refinements.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic chapter 5 authorization')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,5,self.saved);t.source(self.r,5,self.saved)
        t.assemble(self.r,5,draft_prior_commit=self.saved);t.build(self.r,5,self.saved)

    def change_authorization(self,change):ChapterFourDraftContinuationTests.change_authorization(self,change)

    def repin_saved(self):
        self.saved=git(self.r,'rev-parse','HEAD')
        self.change_authorization(lambda a:(a.update(prior_commit=self.saved),a['unsigned_prior'].update(
            commit=self.saved,snapshot_tree_sha=git(self.r,'rev-parse',self.saved+':translations/chapters/04'),
            build_manifest_sha256=t.digest(t.directory(self.r,4)/'build-manifest.json'))))

    def test_chapter_five_candidate_preserves_priors_and_unsigned_state(self):
        before={p:p.read_bytes() for n in (1,2,3,4) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        old_auth={n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in (3,4)}
        self.prepare()
        self.assertEqual(t.validate(self.r,5,source_only=True,draft_prior_commit=self.saved)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,5,draft_prior_commit=self.saved)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        self.assertEqual(old_auth,{n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in old_auth})
        self.assertEqual(t.load(self.d/'build-manifest.json')['input_sha256']['translations/draft-authorizations/ch05.json'],t.digest(self.path))
        self.assertFalse((t.directory(self.r,4)/'qc.json').exists())
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.final_gate(self.r,4)

    def test_default_final_and_aggregate_still_require_real_releases(self):
        import build_translation_aggregate as aggregate
        with self.assertRaises(FileNotFoundError):t.prior(self.r,5)
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,5,final=True,draft_prior_commit=self.saved)
        with self.assertRaisesRegex(t.Error,'publication receipt required'):aggregate.build(self.r)

    def test_chapter_six_is_not_authorized(self):
        with self.assertRaises(FileNotFoundError):t.prior(self.r,6,self.saved)

    def test_chapter_one_actual_receipt_is_required(self):
        (self.r/'translations/publication/ch01-v1.json').unlink()
        with self.assertRaises(FileNotFoundError):t.prior(self.r,5,self.saved)

    def test_unsigned_snapshot_bytes_are_frozen(self):
        for name in ('translation.md','source.md','note-map.json','adzom-audit.json','reading.md','build-manifest.json'):
            with self.subTest(file=name):
                p=t.directory(self.r,4)/name;before=p.read_bytes();p.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'Unsigned saved draft bytes changed'):t.prior(self.r,5,self.saved)
                finally:p.write_bytes(before)

    def test_unsigned_snapshot_cannot_gain_final_or_lexical_records(self):
        for name in ('qc.json','signoff.json','usage.json','glossary-proposals.json'):
            with self.subTest(file=name):
                p=t.directory(self.r,4)/name;p.write_bytes(b'{}\n')
                try:
                    with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,5,self.saved)
                finally:p.unlink()

    def test_unsigned_snapshot_cannot_lose_a_file(self):
        (t.directory(self.r,4)/'note-map.json').unlink()
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,5,self.saved)

    def test_unsigned_native_input_is_frozen(self):
        (self.r/'evidence/ch04-synthetic.png').write_bytes(b'Changed chapter 4 evidence')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft input changed'):t.prior(self.r,5,self.saved)

    def test_unsigned_committed_input_must_match_manifest(self):
        p=self.r/'evidence/ch04-synthetic.png';before=p.read_bytes();p.write_bytes(b'Changed committed evidence')
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic inconsistent saved evidence')
        self.repin_saved();p.write_bytes(before)
        with self.assertRaisesRegex(t.Error,'committed input differs'):t.prior(self.r,5,self.saved)

    def test_repinning_cannot_label_signed_snapshot_unsigned(self):
        t.write(t.directory(self.r,4)/'signoff.json',{'approved':True})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic false saved signoff')
        self.repin_saved()
        with self.assertRaisesRegex(t.Error,'unexpectedly has final review records'):t.prior(self.r,5,self.saved)

    def test_unsigned_output_hashes_are_checked_after_repinning(self):
        path=t.directory(self.r,4)/'build-manifest.json';manifest=t.load(path)
        manifest['output_sha256']['reading.md']='0'*64;t.write(path,manifest)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic inconsistent output hash')
        self.repin_saved()
        with self.assertRaisesRegex(t.Error,'output hash mismatch'):t.prior(self.r,5,self.saved)

    def test_prior_reviewed_candidates_are_still_signed_and_frozen(self):
        for n in (2,3):
            with self.subTest(chapter=n):
                path=t.directory(self.r,n)/'qc.json';before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,5,self.saved)
                finally:path.write_bytes(before)

    def test_reviewed_pins_must_match_existing_chapter_four_authorization(self):
        self.change_authorization(lambda a:a['reviewed_priors'][1].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'reviewed priors differ'):t.prior(self.r,5,self.saved)

    def test_unsigned_tree_and_manifest_pins_are_required(self):
        for field,value,error in [('snapshot_tree_sha','0'*40,'tree pin mismatch'),('build_manifest_sha256','0'*64,'manifest pin mismatch')]:
            with self.subTest(field=field):
                original=t.load(self.path)['unsigned_prior'][field]
                self.change_authorization(lambda a:a['unsigned_prior'].update({field:value}))
                with self.assertRaisesRegex(t.Error,error):t.prior(self.r,5,self.saved)
                self.change_authorization(lambda a:a['unsigned_prior'].update({field:original}))

    def test_unsigned_state_and_exact_instruction_are_required(self):
        self.change_authorization(lambda a:a['unsigned_prior'].update(review_state='signed_candidate'))
        with self.assertRaisesRegex(t.Error,'acknowledged unsigned'):t.prior(self.r,5,self.saved)
        self.change_authorization(lambda a:(a['unsigned_prior'].update(review_state='unsigned_saved_draft'),a.update(user_instruction='excellent, next chapter')))
        with self.assertRaisesRegex(t.Error,'Incomplete working-draft authorization'):t.prior(self.r,5,self.saved)

    def test_chapter_five_authorization_is_committed_and_contract_frozen(self):
        self.prepare();before=self.path.read_bytes();self.path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,5,self.saved)
        self.path.write_bytes(before)
        self.change_authorization(lambda a:a.update(reason='Synthetic altered decision record'))
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,5,draft_prior_commit=self.saved)


class ChapterSixDraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3,4,5,6}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-ch06-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        ChapterFiveDraftContinuationTests.setUp(self)
        ChapterFiveDraftContinuationTests.prepare(self)
        # Separate evidence ensures chapter 5 input failures reach its own gate.
        evidence='evidence/ch05-synthetic.png'
        t.write(self.r/evidence,(self.r/'evidence/synthetic.png').read_bytes())
        audit=t.load(self.d/'adzom-audit.json')
        for image in audit['images']:image['path']=evidence
        for finding in audit['findings']:
            for item in finding['evidence']:item['path']=evidence
        t.write(self.d/'adzom-audit.json',audit)
        t.seal_audit(self.r,5,self.saved);t.build(self.r,5,self.saved)
        d=self.d
        t.write(d/'qc.json',{'chapter':5,'reviewer':'Independent reviewer','translator':'Translator','independent':True,
            'source_sha256':t.digest(d/'source.md'),'translation_sha256':t.digest(d/'translation.md'),
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage':'complete',
            'disposition':'ready_with_explicit_review_flags','open_blockers':[],
            'review_path':'translations/chapters/05/QC.md','review_sha256':t.digest(d/'QC.md')})
        t.write(d/'signoff.json',{'chapter':5,'approved':True,'reviewer':'Coordinator',
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),
            'output_sha256':t.load(d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(d/'qc.json'),
            'review_path':'translations/chapters/05/FINAL.md','review_sha256':t.digest(d/'FINAL.md')})
        t.final_gate(self.r,5)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic signed chapter 5 draft')
        self.fifth=git(self.r,'rev-parse','HEAD');previous=t.load(self.path)
        self.path=self.r/'translations/draft-authorizations/ch06.json';self.d=t.directory(self.r,6)
        t.write(self.path,{'schema_version':4,'chapter':6,'prior_chapter':5,'prior_commit':self.fifth,
            'reviewed_priors':previous['reviewed_priors']+[{'chapter':5,'commit':self.fifth,
                'build_manifest_sha256':t.digest(t.directory(self.r,5)/'build-manifest.json')}],
            'unsigned_prior':previous['unsigned_prior'],'authorized_scope':'working_draft_only',
            'user_instruction':'So make sure that everything is in github up to date, and move on to the next chapter.',
            'date':'2026-10-03','reason':'Synthetic explicit continuation after chapter 5 review and saved-state verification.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic chapter 6 authorization')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,6,self.fifth);t.source(self.r,6,self.fifth)
        t.assemble(self.r,6,draft_prior_commit=self.fifth);t.build(self.r,6,self.fifth)

    def change_authorization(self,change):ChapterFourDraftContinuationTests.change_authorization(self,change)

    def repin_fifth(self):
        self.fifth=git(self.r,'rev-parse','HEAD')
        self.change_authorization(lambda a:(a.update(prior_commit=self.fifth),a['reviewed_priors'][-1].update(
            commit=self.fifth,build_manifest_sha256=t.digest(t.directory(self.r,5)/'build-manifest.json'))))

    def test_chapter_six_preserves_all_prior_bytes_and_authorizations(self):
        before={p:p.read_bytes() for n in range(1,6) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        old_auth={n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in (3,4,5)}
        self.prepare()
        self.assertEqual(t.validate(self.r,6,source_only=True,draft_prior_commit=self.fifth)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,6,draft_prior_commit=self.fifth)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        self.assertEqual(old_auth,{n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in old_auth})
        self.assertEqual(t.load(self.d/'build-manifest.json')['input_sha256']['translations/draft-authorizations/ch06.json'],t.digest(self.path))
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.final_gate(self.r,4)

    def test_chapter_six_default_final_and_aggregate_gates_remain_strict(self):
        import build_translation_aggregate as aggregate
        with self.assertRaises(FileNotFoundError):t.prior(self.r,6)
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,6,final=True,draft_prior_commit=self.fifth)
        with self.assertRaisesRegex(t.Error,'publication receipt required'):aggregate.build(self.r)
        with self.assertRaises(FileNotFoundError):t.prior(self.r,7,self.fifth)

    def test_chapter_one_real_release_remains_required(self):
        (self.r/'translations/publication/ch01-v1.json').unlink()
        with self.assertRaises(FileNotFoundError):t.prior(self.r,6,self.fifth)

    def test_signed_chapter_five_snapshot_is_immutable(self):
        for name in ('translation.md','source.md','note-map.json','adzom-audit.json','reading.md','qc.json','signoff.json'):
            with self.subTest(file=name):
                path=t.directory(self.r,5)/name;before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,6,self.fifth)
                finally:path.write_bytes(before)

    def test_missing_chapter_five_review_cannot_be_repinned(self):
        (t.directory(self.r,5)/'qc.json').unlink()
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic missing prior review')
        self.repin_fifth()
        with self.assertRaisesRegex(t.Error,'Prior release files missing'):t.prior(self.r,6,self.fifth)

    def test_invalid_chapter_five_review_cannot_be_repinned(self):
        path=t.directory(self.r,5)/'qc.json';q=t.load(path);q['reviewer']=q['translator'];t.write(path,q)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic invalid chapter 5 review')
        self.repin_fifth()
        with self.assertRaisesRegex(t.Error,'Independent QC'):t.prior(self.r,6,self.fifth)

    def test_chapter_five_current_and_committed_inputs_are_frozen(self):
        path=self.r/'evidence/ch05-synthetic.png';before=path.read_bytes();path.write_bytes(b'Changed chapter 5 evidence')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,6,self.fifth)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed committed chapter 5 input')
        self.repin_fifth();path.write_bytes(before)
        with self.assertRaisesRegex(t.Error,'Prior tagged input differs'):t.prior(self.r,6,self.fifth)

    def test_unsigned_chapter_four_bytes_inventory_and_evidence_remain_frozen(self):
        path=t.directory(self.r,4)/'translation.md';before=path.read_bytes();path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft bytes changed'):t.prior(self.r,6,self.fifth)
        path.write_bytes(before)
        extra=t.directory(self.r,4)/'qc.json';t.write(extra,{'approved':True})
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,6,self.fifth)
        extra.unlink();path.unlink()
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,6,self.fifth)
        path.write_bytes(before)
        (self.r/'evidence/ch04-synthetic.png').write_bytes(b'Changed unsigned chapter 4 evidence')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft input changed'):t.prior(self.r,6,self.fifth)

    def test_reviewed_records_and_inherited_unsigned_record_are_exact(self):
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        with self.assertRaisesRegex(t.Error,'exactly chapters 2, 3 and 5'):t.prior(self.r,6,self.fifth)
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'reviewed priors differ'):t.prior(self.r,6,self.fifth)
        previous=t.load(self.r/'translations/draft-authorizations/ch05.json')
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(previous['reviewed_priors'][0]))
        self.change_authorization(lambda a:a['unsigned_prior'].update(snapshot_tree_sha='0'*40))
        with self.assertRaisesRegex(t.Error,'unsigned prior differs'):t.prior(self.r,6,self.fifth)

    def test_signed_chapter_five_manifest_and_latest_commit_pins_are_required(self):
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'manifest pin mismatch'):t.prior(self.r,6,self.fifth)
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(commit=self.saved))
        with self.assertRaisesRegex(t.Error,'latest prior commit mismatch'):t.prior(self.r,6,self.fifth)

    def test_all_legacy_authorizations_must_remain_committed(self):
        for n in (3,4,5):
            with self.subTest(chapter=n):
                path=self.r/f'translations/draft-authorizations/ch{n:02}.json';before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,6,self.fifth)
                finally:path.write_bytes(before)

    def test_changed_committed_chapter_five_authorization_cannot_be_inherited(self):
        path=self.r/'translations/draft-authorizations/ch05.json';a=t.load(path);a['reason']='Altered legacy explanation';t.write(path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed legacy authorization')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,6,self.fifth)

    def test_unrelated_prior_commit_is_not_accepted(self):
        unrelated=git(self.r,'commit-tree',git(self.r,'rev-parse','HEAD^{tree}'),'-m','Synthetic unrelated history')
        self.change_authorization(lambda a:(a.update(prior_commit=unrelated),a['reviewed_priors'][-1].update(commit=unrelated)))
        with self.assertRaisesRegex(t.Error,'Git check failed'):t.prior(self.r,6,unrelated)

    def test_chapter_six_scope_and_exact_instruction_are_required(self):
        before=t.load(self.path)
        for field,value,error in [('schema_version',3,'scope/commit mismatch'),('authorized_scope','release','Incomplete working-draft'),
                ('user_instruction','cool, then move on to next chapter','Incomplete working-draft')]:
            with self.subTest(field=field):
                self.change_authorization(lambda a:a.update({field:value}))
                with self.assertRaisesRegex(t.Error,error):t.prior(self.r,6,self.fifth)
                self.change_authorization(lambda a:a.update({field:before[field]}))

    def test_chapter_six_authorization_must_be_committed_and_frozen(self):
        self.prepare();before=self.path.read_bytes();self.path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,6,self.fifth)
        self.path.write_bytes(before)
        self.change_authorization(lambda a:a.update(reason='Synthetic changed chapter 6 explanation'))
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,6,draft_prior_commit=self.fifth)


class ChapterSevenDraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3,4,5,6,7}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-ch07-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        ChapterSixDraftContinuationTests.setUp(self)
        ChapterSixDraftContinuationTests.prepare(self)
        # Separate evidence ensures chapter 6 input failures reach its own gate.
        evidence='evidence/ch06-synthetic.png'
        t.write(self.r/evidence,(self.r/'evidence/synthetic.png').read_bytes())
        audit=t.load(self.d/'adzom-audit.json')
        for image in audit['images']:image['path']=evidence
        for finding in audit['findings']:
            for item in finding['evidence']:item['path']=evidence
        t.write(self.d/'adzom-audit.json',audit)
        t.seal_audit(self.r,6,self.fifth);t.build(self.r,6,self.fifth)
        d=self.d
        t.write(d/'qc.json',{'chapter':6,'reviewer':'Independent reviewer','translator':'Translator','independent':True,
            'source_sha256':t.digest(d/'source.md'),'translation_sha256':t.digest(d/'translation.md'),
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage':'complete',
            'disposition':'ready_with_explicit_review_flags','open_blockers':[],
            'review_path':'translations/chapters/06/QC.md','review_sha256':t.digest(d/'QC.md')})
        t.write(d/'signoff.json',{'chapter':6,'approved':True,'reviewer':'Coordinator',
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),
            'output_sha256':t.load(d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(d/'qc.json'),
            'review_path':'translations/chapters/06/FINAL.md','review_sha256':t.digest(d/'FINAL.md')})
        t.final_gate(self.r,6)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic signed chapter 6 draft')
        self.sixth=git(self.r,'rev-parse','HEAD');previous=t.load(self.path)
        self.path=self.r/'translations/draft-authorizations/ch07.json';self.d=t.directory(self.r,7)
        t.write(self.path,{'schema_version':5,'chapter':7,'prior_chapter':6,'prior_commit':self.sixth,
            'reviewed_priors':previous['reviewed_priors']+[{'chapter':6,'commit':self.sixth,
                'build_manifest_sha256':t.digest(t.directory(self.r,6)/'build-manifest.json')}],
            'unsigned_prior':previous['unsigned_prior'],'authorized_scope':'working_draft_only',
            'user_instruction':'go on',
            'date':'2026-10-04','reason':'Synthetic explicit continuation after chapter 6 review and saved-state verification.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic chapter 7 authorization')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,7,self.sixth);t.source(self.r,7,self.sixth)
        t.assemble(self.r,7,draft_prior_commit=self.sixth);t.build(self.r,7,self.sixth)

    def change_authorization(self,change):ChapterFourDraftContinuationTests.change_authorization(self,change)

    def repin_sixth(self):
        self.sixth=git(self.r,'rev-parse','HEAD')
        self.change_authorization(lambda a:(a.update(prior_commit=self.sixth),a['reviewed_priors'][-1].update(
            commit=self.sixth,build_manifest_sha256=t.digest(t.directory(self.r,6)/'build-manifest.json'))))

    def test_chapter_seven_preserves_all_prior_bytes_and_authorizations(self):
        before={p:p.read_bytes() for n in range(1,7) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        old_auth={n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in (3,4,5,6)}
        self.prepare()
        self.assertEqual(t.validate(self.r,7,source_only=True,draft_prior_commit=self.sixth)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,7,draft_prior_commit=self.sixth)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        self.assertEqual(old_auth,{n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in old_auth})
        self.assertEqual(t.load(self.d/'build-manifest.json')['input_sha256']['translations/draft-authorizations/ch07.json'],t.digest(self.path))
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.final_gate(self.r,4)

    def test_chapter_seven_default_final_and_aggregate_gates_remain_strict(self):
        import build_translation_aggregate as aggregate
        with self.assertRaises(FileNotFoundError):t.prior(self.r,7)
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,7,final=True,draft_prior_commit=self.sixth)
        with self.assertRaisesRegex(t.Error,'publication receipt required'):aggregate.build(self.r)
        with self.assertRaises(FileNotFoundError):t.prior(self.r,8,self.sixth)

    def test_chapter_one_real_release_remains_required(self):
        (self.r/'translations/publication/ch01-v1.json').unlink()
        with self.assertRaises(FileNotFoundError):t.prior(self.r,7,self.sixth)

    def test_signed_chapter_six_snapshot_is_immutable(self):
        for name in ('translation.md','source.md','note-map.json','adzom-audit.json','reading.md','qc.json','signoff.json'):
            with self.subTest(file=name):
                path=t.directory(self.r,6)/name;before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,7,self.sixth)
                finally:path.write_bytes(before)

    def test_missing_chapter_six_review_cannot_be_repinned(self):
        (t.directory(self.r,6)/'qc.json').unlink()
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic missing prior review')
        self.repin_sixth()
        with self.assertRaisesRegex(t.Error,'Prior release files missing'):t.prior(self.r,7,self.sixth)

    def test_invalid_chapter_six_review_cannot_be_repinned(self):
        path=t.directory(self.r,6)/'qc.json';q=t.load(path);q['reviewer']=q['translator'];t.write(path,q)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic invalid chapter 6 review')
        self.repin_sixth()
        with self.assertRaisesRegex(t.Error,'Independent QC'):t.prior(self.r,7,self.sixth)

    def test_chapter_six_current_and_committed_inputs_are_frozen(self):
        path=self.r/'evidence/ch06-synthetic.png';before=path.read_bytes();path.write_bytes(b'Changed chapter 6 evidence')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,7,self.sixth)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed committed chapter 6 input')
        self.repin_sixth();path.write_bytes(before)
        with self.assertRaisesRegex(t.Error,'Prior tagged input differs'):t.prior(self.r,7,self.sixth)

    def test_unsigned_chapter_four_bytes_inventory_and_evidence_remain_frozen(self):
        path=t.directory(self.r,4)/'translation.md';before=path.read_bytes();path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft bytes changed'):t.prior(self.r,7,self.sixth)
        path.write_bytes(before)
        extra=t.directory(self.r,4)/'qc.json';t.write(extra,{'approved':True})
        self.assertTrue(extra.is_file(),'Synthetic added-file mutation must exist before validating')
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,7,self.sixth)
        extra.unlink();path.unlink()
        self.assertFalse(extra.exists(),'Synthetic review-file deletion must complete before validating')
        self.assertFalse(path.exists(),'Synthetic translation-file deletion must complete before validating')
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,7,self.sixth)
        path.write_bytes(before)
        (self.r/'evidence/ch04-synthetic.png').write_bytes(b'Changed unsigned chapter 4 evidence')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft input changed'):t.prior(self.r,7,self.sixth)

    def test_reviewed_records_and_inherited_unsigned_record_are_exact(self):
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        with self.assertRaisesRegex(t.Error,'exactly chapters 2, 3, 5 and 6'):t.prior(self.r,7,self.sixth)
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'reviewed priors differ'):t.prior(self.r,7,self.sixth)
        previous=t.load(self.r/'translations/draft-authorizations/ch06.json')
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(previous['reviewed_priors'][0]))
        self.change_authorization(lambda a:a['unsigned_prior'].update(snapshot_tree_sha='0'*40))
        with self.assertRaisesRegex(t.Error,'unsigned prior differs'):t.prior(self.r,7,self.sixth)

    def test_signed_chapter_six_manifest_and_latest_commit_pins_are_required(self):
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'manifest pin mismatch'):t.prior(self.r,7,self.sixth)
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(commit=self.saved))
        with self.assertRaisesRegex(t.Error,'latest prior commit mismatch'):t.prior(self.r,7,self.sixth)

    def test_all_legacy_authorizations_must_remain_committed(self):
        for n in (3,4,5,6):
            with self.subTest(chapter=n):
                path=self.r/f'translations/draft-authorizations/ch{n:02}.json';before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,7,self.sixth)
                finally:path.write_bytes(before)

    def test_changed_committed_chapter_six_authorization_cannot_be_inherited(self):
        path=self.r/'translations/draft-authorizations/ch06.json';a=t.load(path);a['reason']='Altered legacy explanation';t.write(path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed legacy authorization')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,7,self.sixth)

    def test_unrelated_prior_commit_is_not_accepted(self):
        unrelated=git(self.r,'commit-tree',git(self.r,'rev-parse','HEAD^{tree}'),'-m','Synthetic unrelated history')
        self.change_authorization(lambda a:(a.update(prior_commit=unrelated),a['reviewed_priors'][-1].update(commit=unrelated)))
        with self.assertRaisesRegex(t.Error,'Git check failed'):t.prior(self.r,7,unrelated)

    def test_chapter_seven_scope_and_exact_instruction_are_required(self):
        before=t.load(self.path)
        for field,value,error in [('schema_version',4,'scope/commit mismatch'),('authorized_scope','release','Incomplete working-draft'),
                ('user_instruction','cool, then move on to next chapter','Incomplete working-draft')]:
            with self.subTest(field=field):
                self.change_authorization(lambda a:a.update({field:value}))
                with self.assertRaisesRegex(t.Error,error):t.prior(self.r,7,self.sixth)
                self.change_authorization(lambda a:a.update({field:before[field]}))

    def test_chapter_seven_authorization_must_be_committed_and_frozen(self):
        self.prepare();before=self.path.read_bytes();self.path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,7,self.sixth)
        self.path.write_bytes(before)
        self.change_authorization(lambda a:a.update(reason='Synthetic changed chapter 7 explanation'))
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,7,draft_prior_commit=self.sixth)


class ChapterEightDraftContinuationTests(unittest.TestCase):
    unsigned_chapters={3,4,5,6,7,8}
    @classmethod
    def setUpClass(cls):
        cls.shared=tempfile.TemporaryDirectory(prefix='mtp-translation-ch08-draft-fixture-')
        cls.base=Path(cls.shared.name);fixture(cls.base)

    @classmethod
    def tearDownClass(cls):cls.shared.cleanup()

    def setUp(self):
        ChapterSevenDraftContinuationTests.setUp(self)
        ChapterSevenDraftContinuationTests.prepare(self)
        # Separate evidence ensures chapter 7 input failures reach its own gate.
        evidence='evidence/ch07-synthetic.png'
        t.write(self.r/evidence,(self.r/'evidence/synthetic.png').read_bytes())
        audit=t.load(self.d/'adzom-audit.json')
        for image in audit['images']:image['path']=evidence
        for finding in audit['findings']:
            for item in finding['evidence']:item['path']=evidence
        t.write(self.d/'adzom-audit.json',audit)
        t.seal_audit(self.r,7,self.sixth);t.build(self.r,7,self.sixth)
        d=self.d
        t.write(d/'qc.json',{'chapter':7,'reviewer':'Independent reviewer','translator':'Translator','independent':True,
            'source_sha256':t.digest(d/'source.md'),'translation_sha256':t.digest(d/'translation.md'),
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),'coverage':'complete',
            'disposition':'ready_with_explicit_review_flags','open_blockers':[],
            'review_path':'translations/chapters/07/QC.md','review_sha256':t.digest(d/'QC.md')})
        t.write(d/'signoff.json',{'chapter':7,'approved':True,'reviewer':'Coordinator',
            'build_manifest_sha256':t.digest(d/'build-manifest.json'),
            'output_sha256':t.load(d/'build-manifest.json')['output_sha256'],'qc_sha256':t.digest(d/'qc.json'),
            'review_path':'translations/chapters/07/FINAL.md','review_sha256':t.digest(d/'FINAL.md')})
        t.final_gate(self.r,7)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic signed chapter 7 draft')
        self.seventh=git(self.r,'rev-parse','HEAD');previous=t.load(self.path)
        self.path=self.r/'translations/draft-authorizations/ch08.json';self.d=t.directory(self.r,8)
        t.write(self.path,{'schema_version':6,'chapter':8,'prior_chapter':7,'prior_commit':self.seventh,
            'reviewed_priors':previous['reviewed_priors']+[{'chapter':7,'commit':self.seventh,
                'build_manifest_sha256':t.digest(t.directory(self.r,7)/'build-manifest.json')}],
            'unsigned_prior':previous['unsigned_prior'],'authorized_scope':'working_draft_only',
            'user_instruction':'great, next chapter then...how many do we have left?',
            'date':'2026-10-04','reason':'Synthetic explicit continuation after chapter 7 review and saved-state verification.'})
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic chapter 8 authorization')

    def tearDown(self):self.tmp.cleanup()

    def prepare(self):
        t.plan(self.r,8,self.seventh);t.source(self.r,8,self.seventh)
        t.assemble(self.r,8,draft_prior_commit=self.seventh);t.build(self.r,8,self.seventh)

    def change_authorization(self,change):ChapterFourDraftContinuationTests.change_authorization(self,change)

    def repin_seventh(self):
        self.seventh=git(self.r,'rev-parse','HEAD')
        self.change_authorization(lambda a:(a.update(prior_commit=self.seventh),a['reviewed_priors'][-1].update(
            commit=self.seventh,build_manifest_sha256=t.digest(t.directory(self.r,7)/'build-manifest.json'))))

    def test_chapter_eight_preserves_all_prior_bytes_and_authorizations(self):
        before={p:p.read_bytes() for n in range(1,8) for p in t.directory(self.r,n).iterdir() if p.is_file()}
        old_auth={n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in (3,4,5,6,7)}
        self.prepare()
        self.assertEqual(t.validate(self.r,8,source_only=True,draft_prior_commit=self.seventh)['mode'],'draft-source')
        self.assertEqual(t.validate(self.r,8,draft_prior_commit=self.seventh)['mode'],'draft-candidate')
        self.assertEqual(before,{p:p.read_bytes() for p in before})
        self.assertEqual(old_auth,{n:(self.r/f'translations/draft-authorizations/ch{n:02}.json').read_bytes() for n in old_auth})
        self.assertEqual(t.load(self.d/'build-manifest.json')['input_sha256']['translations/draft-authorizations/ch08.json'],t.digest(self.path))
        with self.assertRaisesRegex(t.Error,'Unsigned'):t.final_gate(self.r,4)

    def test_chapter_eight_default_final_and_aggregate_gates_remain_strict(self):
        import build_translation_aggregate as aggregate
        with self.assertRaises(FileNotFoundError):t.prior(self.r,8)
        with self.assertRaisesRegex(t.Error,'cannot be used for final'):t.validate(self.r,8,final=True,draft_prior_commit=self.seventh)
        with self.assertRaisesRegex(t.Error,'publication receipt required'):aggregate.build(self.r)
        with self.assertRaisesRegex(t.Error,'only for chapters 3, 4, 5, 6, 7 and 8'):t.prior(self.r,9,self.seventh)

    def test_chapter_one_real_release_remains_required(self):
        (self.r/'translations/publication/ch01-v1.json').unlink()
        with self.assertRaises(FileNotFoundError):t.prior(self.r,8,self.seventh)

    def test_signed_chapter_seven_snapshot_is_immutable(self):
        for name in ('translation.md','source.md','note-map.json','adzom-audit.json','reading.md','qc.json','signoff.json'):
            with self.subTest(file=name):
                path=t.directory(self.r,7)/name;before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released bytes changed'):t.prior(self.r,8,self.seventh)
                finally:path.write_bytes(before)

    def test_signed_prior_added_and_deleted_files_are_rejected(self):
        for n in (1,2,3,5,6,7):
            with self.subTest(chapter=n):
                extra=t.directory(self.r,n)/'unexpected-review.md';extra.write_bytes(b'Unexpected file.\n')
                self.assertTrue(extra.is_file(),'Synthetic added file must exist before validating')
                with self.assertRaisesRegex(t.Error,'Prior released file inventory changed'):t.prior(self.r,8,self.seventh)
                extra.unlink()
                path=t.directory(self.r,n)/'QC.md';before=path.read_bytes();path.unlink()
                self.assertFalse(path.exists(),'Synthetic file deletion must complete before validating')
                try:
                    with self.assertRaisesRegex(t.Error,'Prior released file inventory changed'):t.prior(self.r,8,self.seventh)
                finally:path.write_bytes(before)

    def test_missing_chapter_seven_review_cannot_be_repinned(self):
        (t.directory(self.r,7)/'qc.json').unlink()
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic missing prior review')
        self.repin_seventh()
        with self.assertRaisesRegex(t.Error,'Prior release files missing'):t.prior(self.r,8,self.seventh)

    def test_invalid_chapter_seven_review_cannot_be_repinned(self):
        path=t.directory(self.r,7)/'qc.json';q=t.load(path);q['reviewer']=q['translator'];t.write(path,q)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic invalid chapter 7 review')
        self.repin_seventh()
        with self.assertRaisesRegex(t.Error,'Independent QC'):t.prior(self.r,8,self.seventh)

    def test_chapter_seven_current_and_committed_inputs_are_frozen(self):
        path=self.r/'evidence/ch07-synthetic.png';before=path.read_bytes();path.write_bytes(b'Changed chapter 7 evidence')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,8,self.seventh)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed committed chapter 7 input')
        self.repin_seventh();path.write_bytes(before)
        with self.assertRaisesRegex(t.Error,'Prior tagged input differs'):t.prior(self.r,8,self.seventh)

    def test_unsigned_chapter_four_bytes_inventory_and_evidence_remain_frozen(self):
        path=t.directory(self.r,4)/'translation.md';before=path.read_bytes();path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft bytes changed'):t.prior(self.r,8,self.seventh)
        path.write_bytes(before)
        extra=t.directory(self.r,4)/'qc.json';t.write(extra,{'approved':True})
        self.assertTrue(extra.is_file(),'Synthetic added-file mutation must exist before validating')
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,8,self.seventh)
        extra.unlink();path.unlink()
        self.assertFalse(extra.exists(),'Synthetic review-file deletion must complete before validating')
        self.assertFalse(path.exists(),'Synthetic translation-file deletion must complete before validating')
        with self.assertRaisesRegex(t.Error,'file inventory changed'):t.prior(self.r,8,self.seventh)
        path.write_bytes(before)
        (self.r/'evidence/ch04-synthetic.png').write_bytes(b'Changed unsigned chapter 4 evidence')
        with self.assertRaisesRegex(t.Error,'Unsigned saved draft input changed'):t.prior(self.r,8,self.seventh)

    def test_reviewed_records_and_inherited_unsigned_record_are_exact(self):
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        with self.assertRaisesRegex(t.Error,'exactly chapters 2, 3, 5, 6 and 7'):t.prior(self.r,8,self.seventh)
        self.change_authorization(lambda a:a['reviewed_priors'].reverse())
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'reviewed priors differ'):t.prior(self.r,8,self.seventh)
        previous=t.load(self.r/'translations/draft-authorizations/ch07.json')
        self.change_authorization(lambda a:a['reviewed_priors'][0].update(previous['reviewed_priors'][0]))
        self.change_authorization(lambda a:a['unsigned_prior'].update(snapshot_tree_sha='0'*40))
        with self.assertRaisesRegex(t.Error,'unsigned prior differs'):t.prior(self.r,8,self.seventh)

    def test_signed_chapter_seven_manifest_and_latest_commit_pins_are_required(self):
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(build_manifest_sha256='0'*64))
        with self.assertRaisesRegex(t.Error,'manifest pin mismatch'):t.prior(self.r,8,self.seventh)
        self.change_authorization(lambda a:a['reviewed_priors'][-1].update(commit=self.saved))
        with self.assertRaisesRegex(t.Error,'latest prior commit mismatch'):t.prior(self.r,8,self.seventh)

    def test_all_legacy_authorizations_must_remain_committed(self):
        for n in (3,4,5,6,7):
            with self.subTest(chapter=n):
                path=self.r/f'translations/draft-authorizations/ch{n:02}.json';before=path.read_bytes();path.write_bytes(before+b' ')
                try:
                    with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,8,self.seventh)
                finally:path.write_bytes(before)

    def test_changed_committed_chapter_seven_authorization_cannot_be_inherited(self):
        path=self.r/'translations/draft-authorizations/ch07.json';a=t.load(path);a['reason']='Altered legacy explanation';t.write(path,a)
        git(self.r,'add','.');git(self.r,'commit','-qm','Synthetic changed legacy authorization')
        with self.assertRaisesRegex(t.Error,'Prior released input changed'):t.prior(self.r,8,self.seventh)

    def test_unrelated_prior_commit_is_not_accepted(self):
        unrelated=git(self.r,'commit-tree',git(self.r,'rev-parse','HEAD^{tree}'),'-m','Synthetic unrelated history')
        self.change_authorization(lambda a:(a.update(prior_commit=unrelated),a['reviewed_priors'][-1].update(commit=unrelated)))
        with self.assertRaisesRegex(t.Error,'Git check failed'):t.prior(self.r,8,unrelated)

    def test_chapter_eight_scope_and_exact_instruction_are_required(self):
        before=t.load(self.path)
        for field,value,error in [('schema_version',5,'scope/commit mismatch'),('authorized_scope','release','Incomplete working-draft'),
                ('user_instruction','cool, then move on to next chapter','Incomplete working-draft')]:
            with self.subTest(field=field):
                self.change_authorization(lambda a:a.update({field:value}))
                with self.assertRaisesRegex(t.Error,error):t.prior(self.r,8,self.seventh)
                self.change_authorization(lambda a:a.update({field:before[field]}))

    def test_chapter_eight_authorization_must_be_committed_and_frozen(self):
        self.prepare();before=self.path.read_bytes();self.path.write_bytes(before+b' ')
        with self.assertRaisesRegex(t.Error,'committed unchanged'):t.prior(self.r,8,self.seventh)
        self.path.write_bytes(before)
        self.change_authorization(lambda a:a.update(reason='Synthetic changed chapter 8 explanation'))
        with self.assertRaisesRegex(t.Error,'Frozen draft authorization changed'):t.validate(self.r,8,draft_prior_commit=self.seventh)


if __name__=='__main__':unittest.main(verbosity=2)
