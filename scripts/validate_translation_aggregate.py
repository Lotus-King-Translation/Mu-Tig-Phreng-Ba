#!/usr/bin/env python3
"""Read-only final approval gate; remote verification and publication are separate."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
import build_translation_aggregate as aggregate
import translation_pipeline as t

ROOT=Path(__file__).resolve().parents[1]
SELF='scripts/validate_translation_aggregate.py'


def bound_file(root,relative,expected,label):
    t.need(isinstance(relative,str) and relative.strip() and not Path(relative).is_absolute(),label+' requires a repository-relative path')
    path=t.safe(root,relative)
    t.need(path.is_file(),label+' file missing: '+relative)
    t.need(isinstance(expected,str) and re.fullmatch(r'[0-9a-f]{64}',expected),label+' requires a SHA-256')
    t.need(t.digest(path)==expected,label+' hash mismatch: '+relative)
    return path


def verify(root):
    root=Path(root).resolve()
    result=aggregate.verify(root)  # Retain all eight real release/provenance gates.
    dest=root/'translations';path=dest/'signoff.json'
    t.need(path.is_file(),'Unsigned translation aggregate: final signoff missing')
    signoff=t.load(path);manifest=t.load(dest/'build-manifest.json')
    t.need(isinstance(signoff,dict),'Aggregate signoff must be an object')
    t.need(signoff.get('edition')==manifest.get('edition')=='translation-v1','Aggregate signoff edition mismatch')
    t.need(signoff.get('approved') is True,'Aggregate approval missing')
    reviewer=signoff.get('reviewer')
    t.need(isinstance(reviewer,str) and reviewer.strip(),'Aggregate reviewer missing')
    bound_file(root,'translations/build-manifest.json',signoff.get('build_manifest_sha256'),'Aggregate manifest')
    review=bound_file(root,signoff.get('review_path'),signoff.get('review_sha256'),'Aggregate review')
    t.need(review.stat().st_size>0,'Aggregate review is empty')
    outputs=signoff.get('output_sha256')
    t.need(isinstance(outputs,dict) and set(outputs)==set(aggregate.OUTPUTS) and outputs==manifest['output_sha256'],'Aggregate output hash mapping mismatch')
    for name,expected in outputs.items():
        bound_file(root,'translations/'+name,expected,'Aggregate output')
    claims=signoff.get('claims')
    t.need(isinstance(claims,dict) and claims==manifest['claims']==t.CLAIMS and all(value is False for value in claims.values()),'Unsupported aggregate certification claim')
    supporting=signoff.get('supporting_sha256')
    t.need(isinstance(supporting,dict) and SELF in supporting,'Aggregate signoff must bind its final validator')
    for relative,expected in supporting.items():
        support=bound_file(root,relative,expected,'Aggregate supporting record')
        t.need(support not in {path,dest/'validation.json'},'Cyclic aggregate signoff/validation binding')
    t.need(supporting[SELF]==t.digest(Path(__file__)),'Executing aggregate validator differs from approved validator')
    return {**result,'mode':'final','edition':'translation-v1',
            'signoff_sha256':t.digest(path),'review_sha256':t.digest(review),
            'signoff_hash_binding':True,'remote_refs_verified':False,'claims':claims}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    try:
        print(json.dumps(verify(args.root),indent=2));return 0
    except (t.Error,OSError,KeyError,TypeError,json.JSONDecodeError) as exc:
        print('TRANSLATION AGGREGATE FINAL ERROR: '+str(exc),file=sys.stderr);return 1


if __name__=='__main__':raise SystemExit(main())
