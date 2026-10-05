#!/usr/bin/env python3
"""Read-only working-view regressions on the actual reviewed corpus.

Mutations below are in-memory copies or mocked expected hashes, never repository
source/tag edits. These are structural tests, not the standard's semantic examples.
"""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch
import review_working_text as w
import translation_pipeline as t
import build_translation_aggregate as a


class WorkingReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.products, cls.summary = w.generate(cls.root)
        cls.machine = t.load(cls.root / 'translations/machine.json')
        cls.golden = t.load(cls.root / 'golden/reading.json')['objects']
        _, cls.sp, _ = t.parse((cls.root / 'paired/source.md').read_text())
        _, cls.ep, cls.defs = t.parse((cls.root / 'paired/translation.md').read_text(), True)
        cls.chapters = []
        for n in range(1, 9):
            m = t.load(t.directory(cls.root, n) / 'machine.json')
            cls.chapters.append({'chapter': n, 'pairs': m['pairs'], 'endnotes': m['endnotes']})

    def sequence(self, mutate):
        chapters = copy.deepcopy(self.chapters)
        mutate(chapters)
        return a.verify_sequence(chapters, self.golden, self.sp, self.ep, self.defs)

    def test_actual_complete_sequence(self):
        pairs, notes = self.sequence(lambda _: None)
        self.assertEqual((len(pairs), len(notes)), (674, 2597))
        self.assertEqual(self.summary['unresolved_pairs'], 140)
        self.assertEqual(self.summary['obligations_covered'], 2199)

    def test_all_46_outputs_reproduce_read_only(self):
        self.assertEqual(len(self.products), 46)
        for rel, body in self.products.items():
            self.assertEqual((self.root / rel).read_bytes(), body, rel)

    def test_dropped_pair_rejects(self):
        with self.assertRaisesRegex(t.Error, 'pair order'):
            self.sequence(lambda c: c[0]['pairs'].pop())

    def test_reordered_pairs_rejects(self):
        with self.assertRaisesRegex(t.Error, 'pair order'):
            self.sequence(lambda c: c[0]['pairs'].reverse())

    def test_duplicate_id_rejects(self):
        with self.assertRaisesRegex(t.Error, 'Duplicate aggregate pair'):
            self.sequence(lambda c: c[0]['pairs'][1].update(id=c[0]['pairs'][0]['id']))

    def test_changed_tibetan_rejects(self):
        with self.assertRaisesRegex(t.Error, 'canonical pair text'):
            self.sequence(lambda c: c[0]['pairs'][5].update(source='ཀ'))

    def test_changed_english_rejects(self):
        with self.assertRaisesRegex(t.Error, 'canonical pair text'):
            self.sequence(lambda c: c[0]['pairs'][5].update(translation='Unsupported extra agent.'))

    def test_changed_role_rejects(self):
        with self.assertRaisesRegex(t.Error, 'pair metadata'):
            self.sequence(lambda c: c[0]['pairs'][5].update(role='source_annotation'))

    def test_changed_format_rejects(self):
        with self.assertRaisesRegex(t.Error, 'pair metadata'):
            self.sequence(lambda c: c[0]['pairs'][5].update(format='h3'))

    def test_changed_golden_object_rejects(self):
        with self.assertRaisesRegex(t.Error, 'Golden objects changed'):
            self.sequence(lambda c: c[0]['pairs'][5]['golden_objects'][0].update(text='ཁ'))

    def test_duplicate_note_rejects(self):
        with self.assertRaisesRegex(t.Error, 'Duplicate aggregate endnote'):
            self.sequence(lambda c: c[1]['endnotes'][0].update(id=c[0]['endnotes'][0]['id']))

    def test_changed_note_rejects(self):
        with self.assertRaisesRegex(t.Error, 'endnote definition'):
            self.sequence(lambda c: c[0]['endnotes'][0].update(text='Changed source-layer claim.'))

    def test_frozen_byte_difference_rejects(self):
        with patch.object(t, 'git', return_value=b'not the frozen source'):
            with self.assertRaisesRegex(t.Error, 'Protected input changed'):
                w.frozen(self.root, 'paired/source.md')

    def test_policy_hash_drift_rejects(self):
        with patch.dict(w.POLICY, {'guidelines/tibetan_translation_standard_v2.md': '0' * 64}):
            with self.assertRaisesRegex(t.Error, 'Active policy version changed'):
                w.authority(self.root)

    def test_working_views_do_not_claim_release_approval(self):
        for rel, body in self.products.items():
            if rel.endswith('build-manifest.json'):
                import json
                m = json.loads(body)
                self.assertFalse(m['formal_release_approved'])
                self.assertEqual(m['claims'], t.CLAIMS)
                self.assertEqual(m['policy_commit'], w.POLICY_COMMIT)
            if rel.endswith(('reading.md', 'bilingual.md')):
                text = body.decode()
                self.assertNotIn('Eight fixed chapter releases, translated', text)
                self.assertIn('not a new formal release', text)
                self.assertIn('Historical chapter release', text)

    def test_review_links_are_portable_and_notes_exact(self):
        affected = 0
        for note in self.machine['endnotes']:
            if 'Phase D current disposition' in note['raw']:
                affected += 1
                self.assertIn('(' + w.REVIEW_URL + ')', note['raw'])
                self.assertNotIn('(../../FINAL-REVIEW.md', note['raw'])
            for rel in ('translations/reading.md', 'translations/bilingual.md', 'paired/translation.md'):
                self.assertIn(note['raw'], self.products[rel].decode(), (rel, note['id']))
        self.assertEqual(affected, 268)

    def test_local_markdown_file_links_exist(self):
        import re
        from urllib.parse import unquote, urlsplit
        for rel, body in self.products.items():
            if not rel.endswith('.md'): continue
            for link in re.findall(r'\]\(([^\s)]+)\)', body.decode()):
                url = urlsplit(link)
                if url.scheme or url.netloc or not url.path: continue
                target = (self.root / rel).parent / unquote(url.path)
                self.assertTrue(target.resolve().is_file(), (rel, link))


if __name__ == '__main__':
    unittest.main(verbosity=2)
