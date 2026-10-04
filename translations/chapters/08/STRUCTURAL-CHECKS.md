# Structural checks — chapter 8

Date: 2026-10-04. Structural reviewer: `/root/ch08_workflow`. The committed schema-6 continuation at `d85e4ec70f07a528c1cd898ca5ae75c3c3d807c5` authorizes chapter 8 as a working candidate. It preserves chapter 1's actual release, signed chapters 2, 3, 5, 6 and 7, and the entire unsigned saved chapter 4 snapshot. Formal final validation and the eight-release aggregate still require genuine annotated tags and publication receipts. No aggregate gate was bypassed.

## Executed regression tests

All 140 distinct affected structural tests passed on their first uninterrupted suite runs: 36 pipeline, 83 continuation and 21 aggregate cases. The continuation suite comprises 10 original, 11 chapter-4, 16 chapter-5, 15 chapter-6, 15 chapter-7 and 16 chapter-8 cases. No test failure or suite rerun occurred. The new cases check exact authorization and inherited pins; unchanged prior content and inputs; rejected current and committed input mutations; invalid or missing independent review; added and deleted prior files; unrelated history; the genuine chapter-1 release requirement; incompatible final/working modes; and strict aggregate publication requirements.

`fixed_prior` now requires the exact current file inventory in addition to checking every saved file and manifest-bound input. This closes an added-file preservation gap and tightens the signed-prior check to match the existing unsigned-snapshot rule. Negative cases cover added and deleted files across every signed predecessor; the unsigned chapter-4 snapshot remains exact. No production or test correction was needed during the runs.

| Suite | Passed | Runtime (seconds) | Log SHA-256 |
| --- | ---: | ---: | --- |
| pipeline | 36 | 8.186 | `378fe047a15df90e38716411ba83247b0bf53caf41972ef555ce34f0c8f056c2` |
| aggregate | 21 | 27.695 | `8e28fa922fc1d3fa73a6a8ecbee3a2bc92936bab74991e8d02558674d7fa9ac0` |
| continuation | 83 | 1707.610 | `29201f93af6fba3dd42a21c12587d8262f0a1caef4401bd632ddd0e19fa9b076` |

Logs and run accounting are in the execution workspace under `ch08-workflow-tests/`. Fixtures used an external temporary directory. A separate post-run hygiene assertion found three owned synthetic fixture directories still present despite successful suite completion. Those eighteen-, 170- and 173-file synthetic remnants were identified, recorded in `cleanup.json`, removed and their absence verified. Their original cleanup cause is not established. No fixture directory remained inside the repository. This was a post-run cleanup finding, not a failing validator test.

The standard's thirty semantic regression fixtures were not newly executed. These synthetic tests protect structure and provenance; they do not certify translation meaning.

## Actual frozen source and native audit

The actual committed chapter-8 authorization, exact prior-state gate and read-only source validation pass. Source checkpoint `d3302aca0a00cfaecae3d116169ee47d1c95784a` contains 284 fixed objects MTP-S001770–MTP-S002053 in 107 pairs MTP-000568–MTP-000674. All 83 verse pairs retain 248 source lines. Pair roles remain separate: 85 main-text, seventeen metadata, one chapter-colophon, two work-colophon and two source-annotation pairs. Every closing object retains its original order and role. Canonical `paired/source.md` represents all 2,053 fixed golden objects exactly once in 674 pairs. This is source coverage; full English coverage is a separate later check.

The independently checked native audit has 284 anchor checks: 259 agreements, seventeen metadata, seven uncertain objects and one difference. Its 306 findings comprise 239 source omissions, 36 presentation, 23 source-layer, seven uncertain-reading and one Adzom-difference records. All image-to-anchor and finding-to-anchor relationships were checked in both directions, including allocated evidence identities. The seal covers exactly 361 obligations: 55 inherited golden obligations and 306 native findings. It matches the frozen audit, required obligations and evidence hashes.

All eighteen native PNGs, images 530–547 / printed pages 520–537, match exact archive members and registered manifest identities: SHA-256, byte count, dimensions, source URL and canvas. This verifies evidence identity separately from visual inspection attributed in the native audit. The structural reviewer did not repeat that visual reading or decipher untranscribed commentary.

| Frozen input | SHA-256 |
| --- | --- |
| source.md | `1a81db08209fd0813fe9b1cfc017e89454286f72f10c792b2eda5be9ad059b95` |
| segmentation.json | `5644b5b062721cf79f0e26e36fe4560728e790b8e3142c06b274b50d9b22ac04` |
| contract.json | `bf15411ae0be5c4364481f21928386f6ab1874c88b372cef144585297dfdd772` |
| adzom-audit.json | `e07e0a26fb42f045813bc2bc7ca6a5adc1903ebdc30988ad05a2a06207529c3d` |
| audit-contract.json | `c09a548dc9178941507be622c74882c8968769e29d69a0b8ae1d71f2b7cf5df9` |
| Native provenance | `7b1394569075c403fd0a5f5d59fd50c2697f500746a1219dab701e4a6d8defdf` |

All eight checked source, contract, audit, seal and provenance paths retained identical hashes and nanosecond modification times throughout the source/audit check. The execution-workspace report is `ch08-structural-report.json`.

## Immutable prior state

Independent read-only verification compares all 178 chapter 1–7 files against their exact pinned inventories and committed bytes, plus 217 distinct manifest-bound inputs against both current hashes and committed blobs or LFS identities and lengths. All saved output hashes agree. The six signed chapter content gates pass, and chapter 1's genuine annotated release and publication receipt remain required and valid. All 299 distinct checked prior paths retain identical hashes and nanosecond modification times.

| Chapter | Exact ref | Chapter files | Bound inputs | Saved review state |
| --- | --- | ---: | ---: | --- |
| 1 | `refs/tags/translate-ch01-v1` | 27 | 27 | Actual fixed release |
| 2 | `f0f7097621c021b4a03863dc7b7e8925c6975f86` | 28 | 24 | Signed content |
| 3 | `50bef02b5b0088911153ce348f7f45612e147158` | 28 | 26 | Signed content |
| 4 | `730921898da3e3328bb42d97abea7672bf44afcd` | 17 | 35 | Unsigned saved draft |
| 5 | `c0b7945a56e8c670363d50a6c67448bdda83003a` | 26 | 45 | Signed content |
| 6 | `a02f8c79a31c561c1888495b4178bfa7c25eda45` | 26 | 41 | Signed content |
| 7 | `e40041ace3efe51bf2aa205a092c7d117011514a` | 26 | 37 | Signed content |

Per-chapter bound-input counts overlap; 217 is their distinct union. Chapter 4 remains the exact seventeen-file unsigned snapshot at `730921898da3e3328bb42d97abea7672bf44afcd`, tree `3a788e26750edf3682407c1643c22483dd199842`. Its missing final revision, lexical records, QC and signoff have not been recreated or inferred. Chapter 7 remains pinned to signed candidate `e40041ace3efe51bf2aa205a092c7d117011514a`, manifest `288560e60dfbb38e73991311599f47fd55a7d9046bf747299311dec1ed84b8f9`.

## Remaining candidate checks

Complete English, source apparatus, lexical bindings, archive identity and reproducible final candidate validation remain to be checked when chapter inputs are frozen and the coordinator provides the exact build-manifest hash. Independent translation QC and coordinator signoff are separate records. This report does not assert full chapter-8 English clearance, whole-book semantic certification, independent human certification or formal publication clearance.
