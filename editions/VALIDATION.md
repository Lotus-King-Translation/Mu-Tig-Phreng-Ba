# Intake validation

Source-intake validation certifies preserved file identity and packaging, not Tibetan textual accuracy or completeness.

- Acquisition checks image dimensions against the provider manifest and retains every response byte in ZIP archives.
- Every PDF image page is decoded and compared pixel-for-pixel with its original source image during acquisition; no new OCR, normalization or image enhancement is applied.
- Source image count, ZIP integrity, PDF page count, PDF SHA-256, archive SHA-256 and per-image SHA-256 are recorded in each `image-manifest.json`.
- Representative PDF pages were separately rendered with Poppler and visually inspected: Adzom2000 page1, Dzongsar page138 and Degé W21939 page60. Rendering preserved the scan orientation, layout, margins and source defects. Dzongsar's final included page is intentionally blank. The renders are disposable QA derivatives; the preserved PDFs and originals are authoritative.
- Boundary allocation is recorded in `BOUNDARIES.md` and BDRC batch05; shared pages retain adjacent material. No full scan proofreading, textual collation or independent human palaeographic review is claimed.

Authored inputs: `SOURCES.json`, `ACQUISITION-PLAN.json`, research prose and boundary decisions. Generated outputs: `REGISTER.csv`, `FILE-MANIFEST.csv`, facsimile PDFs/ZIPs and image manifests. Regenerate the register only after pending acquisitions stop, using `python3 scripts/build_intake_register.py`; validate read-only using `python3 scripts/verify_intake.py`.

Acquisition runtime: Python3 with Pillow12.3.0, img2pdf0.6.3 and pikepdf10.16.0. Large binary assets use Git LFS; use `git lfs pull` after cloning.

Integrity negative test: a clean isolated fixture passed; changing source bytes while preserving the file length was rejected. No project source was modified by the test.

`REGISTER.csv` hashes the named local artifact. For unacquired leads this may be a catalogue or metadata file, never an assertion that the underlying book/manuscript has been acquired. `FILE-MANIFEST.csv` covers preserved research, source metadata and scan assets; generated receipt files are outside that inventory to avoid self-reference.
