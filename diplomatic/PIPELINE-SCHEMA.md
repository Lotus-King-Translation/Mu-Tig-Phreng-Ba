# Golden pipeline schema, version 1

Run with `.venv/bin/python scripts/golden_pipeline.py COMMAND`. Dependency: `pyewts==0.2.0` (installed with `uv pip install --python .venv/bin/python --no-build-isolation pyewts==0.2.0`; older package build requires `setuptools<81`). Conversion runs with `fix_spacing=False`; converted strings and warnings are preserved as derived data, not a witness.

## Generated global extraction

`prepare` freezes `source-anchors.json`, `electronic-collation.json`, `chapter-map.json` and `anomalies.json`. Existing files must be byte-identical before this command writes anything. Tibetan and Wylie archival raw-file hashes are pinned in the script. Each poem payload is split with `splitlines(keepends=True)`, including its leading blank line. IDs `MTP-S000001` through `MTP-S002053` never change. `text` excludes only the line ending; `line_ending` and `raw_text` preserve it. `raw_start`/`raw_end` are absolute Unicode-code-point offsets into the exact decoded raw file, not UTF-8 byte offsets. Wylie offsets and exact strings remain separate.

The 8 mechanically located chapter closures are anchors 97, 221, 341, 635, 1051, 1427, 1769 and 2035. Chapter 8 includes the final post-chapter material through anchor 2053. Chapter allocation is an electronic locator until the authored native-image review supports it. Numeric page markers and all eight `@1`–`@8` electronic chapter markers are classified as metadata, distinct from main text; their exact Unicode conversion strings remain preserved.

## Frozen chapter contract

`plan --chapter N [--checks path/to/additional-checks.json]` creates `diplomatic/chapters/NN/contract.json`, its `contract.sha256`, and four empty authored arrays. Global extraction hashes, exact anchor boundaries, difference/anomaly IDs, required decision anchors and source checks are fixed in the contract. Additional checks are an array of `{ "id": "…", "anchor_ids": ["MTP-S…"], "question": "…" }`. Freeze these before editorial review. No command automatically changes a contract.

## Authored chapter arrays

`decisions.json`: one object per reviewed anchor; required fields are:

```json
{
  "id": "MTP-C01-D001",
  "anchor_id": "MTP-S000026",
  "old": "exact original text, without line ending",
  "new": "selected text, without line ending",
  "role": "main_text",
  "treatment": "retain_with_uncertainty",
  "reason": "Specific editorial rationale",
  "evidence_ids": ["MTP-C01-E001"],
  "uncertainty": ["Specific retained uncertainty"]
}
```

Roles: `main_text`, `heading`, `chapter_colophon`, `colophon`, `annotation`, `graphic`, `metadata`, `blank`, `unresolved`. Treatments: `retain_base`, `retain_with_uncertainty`, `scan_supported_correction`, `separate_source_layer`, `classify_layer`, `display_only`, `defer_outside_scope`. A text change requires governing-image evidence. Retention/classification must retain exact text. Layer separation additionally requires `layers: [{"role":"annotation","text":"…"}]`. Additional authored `source_notes` or `gaps` fields remain verbatim in the apparatus. Put any limitation that must appear in readable text into `uncertainty`; never fabricate a restoration for an undeciphered omission.

`evidence.json`: each object requires `id`, repository-relative `path`, `sha256`, `anchor_ids`, `status` (`accepted`, `excluded`, `mislocated`) and `allocation_reason`. Accepted evidence also requires `inspection: "native_image_direct"`, `source_id: "adzom-1973"` and numeric `image_index`. Full-image hash must match the governing image manifest. A crop additionally requires `crop: [left,top,right,bottom]` and `original_sha256`, with dimensions and original hash validated. Allocation is an authored assertion; a hash does not prove the locus association.

`source-checks.json`: exactly one result per frozen check, with `id`, `status: "closed"`, `finding`, `evidence_ids` and `uncertainty: []`. Accepted evidence must cover every target anchor. Unreadability can close a check when explicitly recorded as uncertainty; closure does not assert successful decipherment.

`restorations.json`: normally `[]`. Each attested restoration requires unique `id: "MTP-R000001"`, `after_anchor`, exact `text`, `role`, `reason`, `evidence_ids` and `uncertainty`. IDs are separate from stable source anchors. Restorations require accepted governing-image evidence allocated to the placement anchor.

## Generated chapter build and review

`build --chapter N` writes `reading.md`, `reading.json`, `apparatus.json`, `changes.json`, `coverage.json` and `build-manifest.json`. Reading objects account for every original anchor, including metadata and blanks; these two roles are omitted only from the human display. Unreviewed lines explicitly retain `review_status: "retained_unreviewed_transcript"`. Original strings, source line endings and page hints remain in the machine reading. The apparatus carries all exact comparisons, decisions, evidence and checks. Build inputs and outputs are hashed. Signed outputs cannot be overwritten with changed content.

`validate --chapter N` regenerates in memory and checks exact byte identity, source preservation, full-locus and opcode reconstruction, evidence hashes/allocation fields, closed frozen queues and explicit false coverage flags. `validate --chapter N --final` additionally requires authored `signoff.json`:

```json
{
  "chapter": 1,
  "approved": true,
  "reviewer": "named agent or reviewer",
  "review": "Specific final review statement",
  "review_path": "diplomatic/chapters/01/FINAL-REVIEW.md",
  "review_sha256": "SHA256 of the authored review",
  "build_manifest_sha256": "SHA256 of generated build-manifest.json",
  "output_sha256": {"reading.md":"…","reading.json":"…","apparatus.json":"…","changes.json":"…","coverage.json":"…"},
  "claims": {"full_scan_proofreading":false,"exhaustive_witness_collation":false,"independent_witness_electronic_collation":false,"independent_human_certification":false}
}
```

`test` runs isolated fixtures and negative corruption checks; it does not mutate the edition. Validation proves structure and provenance consistency; direct image interpretation remains an explicit editorial judgement. Publication, prior-release immutability, sequential chapter progression and tag/receipt verification are coordinated by the root agent under the repository release method.
