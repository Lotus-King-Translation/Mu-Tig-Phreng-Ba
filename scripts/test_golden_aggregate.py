#!/usr/bin/env python3
"""Isolated aggregate gates; synthetic fixtures do not certify Tibetan readings."""
import copy
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import build_golden_aggregate as ag
import golden_pipeline as gp


def fixture_chapters():
    boundaries=[97,221,341,635,1051,1427,1769,2053]
    first=1; chapters=[]
    for n,last in enumerate(boundaries,1):
        rows=[{'id':f'MTP-S{i:06}','source_anchor':f'MTP-S{i:06}','text':'ཀ',
               'role':'main_text','layers':[],'uncertainty':[]} for i in range(first,last+1)]
        chapters.append({'chapter':n,'objects':rows,'apparatus':f'diplomatic/chapters/{n:02}/apparatus.json',
                         'coverage':{'anchor_count':len(rows),'accounted_original_anchors':len(rows),'restoration_count':0}})
        first=last+1
    return chapters


class AggregateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='mtp-aggregate-test-')
        self.root=Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self,*args):
        return ag.git(self.root,*args)

    def git_fixture(self):
        self.git('init','-q')
        self.git('config','user.name','Synthetic aggregate test')
        self.git('config','user.email','synthetic@example.invalid')
        (self.root/'released.txt').write_bytes(b'fixed chapter bytes\n')
        self.git('add','released.txt'); self.git('commit','-qm','Synthetic fixture')
        self.git('tag','-a','golden-ch01-v1','-m','Synthetic fixture tag')

    def test_missing_chapter_rejects_without_output(self):
        with self.assertRaisesRegex(gp.ValidationError,'Missing chapter'):
            ag.build(self.root)
        self.assertFalse((self.root/'golden').exists())

    def test_missing_receipt_rejects_without_output(self):
        for n in range(1,9):
            d=gp.chapter_dir(self.root,n); d.mkdir(parents=True)
            gp.write(d/'signoff.json',{'synthetic':True})
        with self.assertRaisesRegex(gp.ValidationError,'receipt required'):
            ag.build(self.root)
        self.assertFalse((self.root/'golden').exists())

    def test_missing_signoff_rejects(self):
        for n in range(1,9):
            d=gp.chapter_dir(self.root,n); d.mkdir(parents=True)
            gp.write(self.root/'diplomatic/publication'/f'ch{n:02}-v1.json',{'synthetic':True})
        with self.assertRaisesRegex(gp.ValidationError,'Missing chapter signoff'):
            ag.build(self.root)

    def test_all_originals_accounted(self):
        self.assertEqual(ag.verify_sequence(fixture_chapters()),{'original_anchors':2053,'restorations':0,'reading_objects':2053})

    def test_duplicate_anchor_rejects(self):
        chapters=fixture_chapters(); chapters[1]['objects'][0]=copy.deepcopy(chapters[0]['objects'][-1])
        with self.assertRaisesRegex(gp.ValidationError,'Duplicate'):
            ag.verify_sequence(chapters)

    def test_anchor_gap_rejects(self):
        chapters=fixture_chapters(); chapters[-1]['objects'].pop()
        chapters[-1]['coverage']['anchor_count']-=1;chapters[-1]['coverage']['accounted_original_anchors']-=1
        with self.assertRaisesRegex(gp.ValidationError,'exactly'):
            ag.verify_sequence(chapters)

    def test_reordered_anchors_rejects(self):
        chapters=fixture_chapters(); rows=chapters[0]['objects'];rows[0],rows[1]=rows[1],rows[0]
        with self.assertRaisesRegex(gp.ValidationError,'exactly'):
            ag.verify_sequence(chapters)

    def test_duplicate_restoration_rejects(self):
        chapters=fixture_chapters()
        for c in chapters[:2]:
            row={'id':'MTP-R000001','source_anchor':None,'after_anchor':c['objects'][0]['id'],
                 'text':'ཀ','role':'main_text','layers':[],'uncertainty':['Synthetic unresolved sign.']}
            c['objects'].insert(1,row);c['coverage']['restoration_count']=1
        with self.assertRaisesRegex(gp.ValidationError,'Duplicate'):
            ag.verify_sequence(chapters)

    def test_valid_restoration_preserves_order(self):
        chapters=fixture_chapters()
        row={'id':'MTP-R000001','source_anchor':None,'after_anchor':'MTP-S000001',
             'text':'ཀ','role':'main_text','layers':[],'uncertainty':[]}
        chapters[0]['objects'].insert(1,row);chapters[0]['coverage']['restoration_count']=1
        self.assertEqual(ag.verify_sequence(chapters)['restorations'],1)

    def test_unchanged_released_file_accepts(self):
        self.git_fixture()
        self.assertEqual(ag.verify_tagged_file(self.root,'golden-ch01-v1','released.txt'),gp.file_hash(self.root/'released.txt'))

    def test_changed_released_bytes_rejects(self):
        self.git_fixture();(self.root/'released.txt').write_bytes(b'changed')
        with self.assertRaisesRegex(gp.ValidationError,'Released bytes changed'):
            ag.verify_tagged_file(self.root,'golden-ch01-v1','released.txt')

    def test_lfs_content_identity_and_corruption(self):
        self.git_fixture()
        body=b'Synthetic native image bytes'
        (self.root/'image.png').write_text('version https://git-lfs.github.com/spec/v1\noid sha256:'+gp.sha(body)+'\nsize '+str(len(body))+'\n')
        self.git('add','image.png');self.git('commit','-qm','Synthetic LFS fixture');self.git('tag','-a','lfs-v1','-m','Synthetic')
        (self.root/'image.png').write_bytes(body)
        self.assertEqual(ag.verify_tagged_file(self.root,'lfs-v1','image.png'),gp.sha(body))
        (self.root/'image.png').write_bytes(body+b'!')
        with self.assertRaisesRegex(gp.ValidationError,'Released LFS content changed'):
            ag.verify_tagged_file(self.root,'lfs-v1','image.png')

    def test_receipt_binds_annotated_tag(self):
        self.git_fixture();d=gp.chapter_dir(self.root,1);d.mkdir(parents=True)
        gp.write(d/'build-manifest.json',{'synthetic':True});gp.write(d/'coverage.json',{'synthetic':True})
        commit=self.git('rev-parse','refs/tags/golden-ch01-v1^{}').decode().strip()
        receipt={'chapter':1,'tag':'golden-ch01-v1',
                 'remote_tag_object':self.git('rev-parse','refs/tags/golden-ch01-v1').decode().strip(),
                 'remote_peeled_commit':commit,'release_commit':commit,'remote_main_at_release':commit,
                 'build_manifest_sha256':gp.file_hash(d/'build-manifest.json'),'coverage':gp.load(d/'coverage.json')}
        path=self.root/'diplomatic/publication/ch01-v1.json';gp.write(path,receipt)
        self.assertEqual(ag.receipt_identity(self.root,1)['tag'],receipt['tag'])
        receipt['remote_peeled_commit']='0'*40;gp.write(path,receipt)
        with self.assertRaisesRegex(gp.ValidationError,'commit mismatch'):
            ag.receipt_identity(self.root,1)

    def test_readable_roles_and_uncertainty_preserved(self):
        chapters=fixture_chapters();rows=chapters[0]['objects']
        rows[0]['role']='metadata';rows[0]['text']='༄༡'
        rows[1]['uncertainty']=['Synthetic source gap remains unresolved.']
        rows[1]['layers']=[{'role':'annotation','text':'ཁ'}]
        releases=[{'url':'https://example.invalid/fixed'} for _ in chapters]
        md=ag.reading_markdown(chapters,releases).decode()
        self.assertIn('[Electronic metadata] ༄༡',md)
        self.assertIn('[Source annotation] ཁ',md)
        self.assertIn('[^MTP-S000002]',md)
        self.assertIn('Synthetic source gap remains unresolved.',md)
        self.assertIn('<a id="mtp-s002053"></a>',md)

    def test_verify_does_not_write(self):
        expected={'reading.md':b'fixed\n','build-manifest.json':b'{}\n'}
        dest=self.root/'golden';dest.mkdir()
        for name,data in expected.items():(dest/name).write_bytes(data)
        before={p.name:(p.read_bytes(),p.stat().st_mtime_ns) for p in dest.iterdir()}
        with patch.object(ag,'generate',return_value=expected):
            self.assertTrue(ag.verify(self.root)['passed'])
        self.assertEqual(before,{p.name:(p.read_bytes(),p.stat().st_mtime_ns) for p in dest.iterdir()})
        (dest/'reading.md').write_bytes(b'changed')
        with patch.object(ag,'generate',return_value=expected):
            with self.assertRaisesRegex(gp.ValidationError,'Aggregate corruption'):
                ag.verify(self.root)

if __name__=='__main__':
    unittest.main(verbosity=2)
