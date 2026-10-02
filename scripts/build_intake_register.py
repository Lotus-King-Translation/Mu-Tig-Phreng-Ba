#!/usr/bin/env python3
"""Generate intake register and file receipts from SOURCES.json and acquired originals.

Authored: SOURCES.json, research prose, ACQUISITION-PLAN.json.
Generated: REGISTER.csv, FILE-MANIFEST.csv. Run only after pending acquisitions stop.
"""
import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((ROOT/'editions/SOURCES.json').read_text())
assert len({r['source_id'] for r in rows})==len(rows),'Duplicate source ID'
cols='source_id,siglum,kind,title,path,physical_exemplar,independence_status,role,sha256,provenance,coverage,notes'.split(',')
for r in rows:
 ed=r['source_id']; scan=ROOT/'editions/scans'/ed/'image-manifest.json'
 if scan.exists():
  d=json.loads(scan.read_text());r.update(kind='acquired facsimile manifestation',path=f'editions/scans/{ed}/mu-tig-phreng-ba.pdf')
  r['coverage']+=f"; acquired {d['pages']} image pages; requested indices {d['requested_range']}"
  r['notes']+=f" Original response ZIP and page hashes in same directory. Missing manifest indices: {d['missing_image_indices']}. Rights: {d['rights']}."
  r['provenance']+='; '+str(scan.relative_to(ROOT))
 elif not r.get('path'):
  p=ROOT/'editions/metadata'/ed/'volume-manifest.json'
  r['path']=str(p.relative_to(ROOT)) if p.exists() else 'editions/CATALOGUE.md'
 p=ROOT/r['path'];assert p.exists(),p
 r['sha256']=sha(p)
with (ROOT/'editions/REGISTER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,cols,lineterminator="\n");w.writeheader();w.writerows(rows)
originals=[]
for top in ['editions/metadata','editions/research','editions/scans']:
 for p in sorted((ROOT/top).rglob('*')):
  if p.is_file():originals.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)))
with (ROOT/'editions/FILE-MANIFEST.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,['path','bytes','sha256'],lineterminator="\n");w.writeheader();w.writerows(originals)
print(json.dumps({'register_rows':len(rows),'acquired_facsimiles':sum(r['kind']=='acquired facsimile manifestation' for r in rows),'file_receipts':len(originals)}))
