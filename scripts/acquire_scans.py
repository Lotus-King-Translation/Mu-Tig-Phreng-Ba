#!/usr/bin/env python3
"""Acquire catalogue-bounded, licensed BDRC facsimiles without altering pixels.

Requires Pillow, img2pdf, pikepdf. Inputs: editions/ACQUISITION-PLAN.json and saved
IIIF volume/collection metadata. Downloaded response bytes are archived verbatim.
A completed download does not certify textual completeness or boundary readings.
"""
from pathlib import Path
import argparse, concurrent.futures, hashlib, io, json, re, time, urllib.request, urllib.error, zipfile
from PIL import Image
import img2pdf, pikepdf
ROOT=Path(__file__).resolve().parents[1]

def sha(data): return hashlib.sha256(data).hexdigest()
def get(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MuTigPhrengBa-source-research/1.0'}),timeout=40) as r:return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (401,403,404) or attempt==2:raise
        except (OSError,TimeoutError):
            if attempt==2:raise
        time.sleep(2*(attempt+1))
def write_json(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def canvases(spec):
    md=ROOT/'editions/metadata'/spec['edition']
    rights=json.loads((md/'collection.json').read_text())
    license=rights.get('license','')
    if spec['edition']=='gadkar-manuscript':
        record=json.loads((ROOT/'editions/research/bdrc/batch-03-access-and-provenance/W1BL6.json').read_text())
        notes=record['http://purl.bdrc.io/resource/W1BL6']['http://purl.bdrc.io/ontology/core/scanInfo']
        if not any('CC BY-NC 4.0' in n.get('value','') for n in notes):raise ValueError('Gadkar image licence missing')
        license='https://creativecommons.org/licenses/by-nc/4.0/'
    if license not in ('https://creativecommons.org/licenses/by-nc/4.0/','https://creativecommons.org/publicdomain/mark/1.0/'): raise ValueError('Supported source licence not verified')
    d=json.loads((md/'volume-manifest.json').read_text()); out={}
    for c in d['sequences'][0]['canvases']:
        m=re.search(r'img\. (\d+)',str(c.get('label')))
        if m and c.get('images'):out[int(m[1])]=c
    return out,license

def download(job):
    ed,n,c,folder=job
    resource=c['images'][0]['resource'];url=resource['@id']; ext='.png' if url.endswith('.png') else '.jpg'
    p=folder/f'{n:05d}{ext}'
    b=p.read_bytes() if p.exists() else get(url)
    with Image.open(io.BytesIO(b)) as im:
        im.load(); dims=im.size
    expected=(resource['width'],resource['height'])
    if dims!=expected:raise ValueError(f'{ed}:{n} dimensions {dims} != {expected}')
    if not p.exists():p.write_bytes(b)
    return {'image_index':n,'file':p.name,'url':url,'canvas':c['@id'],'labels':c['label'],'bytes':len(b),'sha256':sha(b),'width':dims[0],'height':dims[1]}

def acquire(spec,samples=False):
    ed=spec['edition'];cs,license=canvases(spec);a,b=spec['start'],spec['end']
    if a is None or b is None:raise ValueError('Unresolved image range')
    out=ROOT/'editions/scans'/ed;out.mkdir(parents=True,exist_ok=True)
    folder=out/'boundary' if samples else ROOT/'.cache/acquisition'/ed
    folder.mkdir(parents=True,exist_ok=True)
    chosen=sorted(n for n in ({a-1,a,a+1,b-1,b,b+1} if samples else range(a,b+1)) if n in cs)
    if not chosen:raise ValueError('No available canvases')
    jobs=[(ed,n,cs[n],folder) for n in chosen];records=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for r in pool.map(download,jobs):
            records.append(r)
            if not samples and len(records)%25==0:print(ed,len(records),'/',len(chosen),flush=True)
    manifest={'edition':ed,'source_group':spec['group'],'source_manifest':f'editions/metadata/{ed}/volume-manifest.json','retrieved_date':'2026-10-02','attribution':('Tibetan Manuscript Project Vienna, photographs 2023; distributed by BDRC; unchanged response images; lossless PDF packaging by Lotus King Translation' if ed=='gadkar-manuscript' else 'Buddhist Digital Resource Center'),'rights':license,'requested_range':[a,b],'boundary_samples':samples,'images':records,'new_ocr':False,'full_scan_proofreading':False,'visual_boundary_verification':'See BOUNDARIES.md; acquisition alone does not verify text extent.'}
    if samples:
        write_json(out/'boundary-manifest.json',manifest);print('SAMPLES',ed,len(records),flush=True);return
    zp=out/'iiif-response-images.zip';pdf=out/'mu-tig-phreng-ba.pdf'
    with zipfile.ZipFile(zp,'w',compression=zipfile.ZIP_STORED) as z:
        for r in records:z.write(folder/r['file'],r['file'])
        if z.testzip() is not None:raise ValueError('ZIP integrity failure')
    pdf.write_bytes(img2pdf.convert([str(folder/r['file']) for r in records]))
    with pikepdf.open(pdf) as doc:
        if len(doc.pages)!=len(records):raise ValueError('PDF page count mismatch')
        for page,r in zip(doc.pages,records):
            imgs=list(page.images.values())
            if len(imgs)!=1:raise ValueError('Unexpected PDF image count')
            decoded=pikepdf.PdfImage(imgs[0]).as_pil_image().convert('RGB')
            with Image.open(folder/r['file']) as original:
                if decoded.size!=original.size or decoded.tobytes()!=original.convert('RGB').tobytes():raise ValueError('PDF pixel mismatch')
    manifest.update(pages=len(records),missing_image_indices=[n for n in range(a,b+1) if n not in cs],pdf_sha256=sha(pdf.read_bytes()),zip_sha256=sha(zp.read_bytes()),all_pdf_pages_pixel_identity_verified=True)
    write_json(out/'image-manifest.json',manifest)
    print('ACQUIRED',ed,len(records),'pages',pdf.stat().st_size,'bytes',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--samples',action='store_true');p.add_argument('--edition',action='append',required=True);args=p.parse_args()
    specs=json.loads((ROOT/'editions/ACQUISITION-PLAN.json').read_text());errors=[]
    for ed in args.edition:
        try:acquire(next(x for x in specs if x['edition']==ed),args.samples)
        except Exception as e:errors.append({'edition':ed,'error':str(e)});print('FAILED',ed,str(e),flush=True)
    if errors:
        write_json(ROOT/'editions'/'ACQUISITION-ERRORS.json',errors)
        raise SystemExit(1)
