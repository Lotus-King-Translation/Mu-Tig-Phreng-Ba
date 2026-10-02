#!/usr/bin/env python3
"""Read-only integrity validation; does not certify Tibetan readings or completeness."""
import csv,hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
files=list(csv.DictReader((ROOT/'editions/FILE-MANIFEST.csv').open()))
for r in files:
 p=ROOT/r['path'];assert p.exists(),p
 assert p.stat().st_size==int(r['bytes']),p
 assert sha(p.read_bytes())==r['sha256'],p
rows=list(csv.DictReader((ROOT/'editions/REGISTER.csv').open()))
assert len({r['source_id'] for r in rows})==len(rows)
for r in rows:assert sha((ROOT/r['path']).read_bytes())==r['sha256'],r['source_id']
pages=0;editions=0;gaps={}
for p in (ROOT/'editions/scans').glob('*/image-manifest.json'):
 d=json.loads(p.read_text());editions+=1;pages+=d['pages']
 assert sha((p.parent/'mu-tig-phreng-ba.pdf').read_bytes())==d['pdf_sha256'],p
 z=p.parent/'iiif-response-images.zip';assert sha(z.read_bytes())==d['zip_sha256'],p
 with zipfile.ZipFile(z) as archive:
  assert len(archive.namelist())==len(d['images'])==d['pages'],p
  for i in d['images']:assert sha(archive.read(i['file']))==i['sha256'],i
 assert d['all_pdf_pages_pixel_identity_verified'] is True,p
 if d['missing_image_indices']:gaps[d['edition']]=d['missing_image_indices']
print(json.dumps({'verified_files':len(files),'register_rows':len(rows),'facsimiles':editions,'image_pages':pages,'unexposed_manifest_indices':gaps},indent=2))
