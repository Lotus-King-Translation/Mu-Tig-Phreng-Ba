# Published English working edition

## Template policy baseline — P3

Adopted common snapshot: `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Active standard **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; P2 glossary **283 data rows in the existing eight-column format**, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`. Both active files match the pinned template byte-for-byte, with no local terminology exception. [P3](../DECISIONS.md#post-translation-review-2026-10-05) defines Phase D; [P1](../DECISIONS.md#terminology-clarification-2026-10-04) and [P2](../DECISIONS.md#terminology-expansion-2026-10-05) retain their exact scopes and provenance. The 63 regression fixtures are specifications, not measured model results.

Adoption is recorded on `policy/adopt-template-882454cb` for a pull request to `main`; merge into `main` is not yet verified. This is policy adoption only, not a translation review or new release. Prior release-time statements that the glossary/standard were unchanged describe those fixed historical inputs. Do not update old manifests, signatures, release receipts or archived policy copies to make them claim the new policy was used then.

## Fixed inputs for the assigned review

- Golden release / commit: `golden-v1` / `4d6ba07e1b3379183633127cd387d98d8195eb95`.
- English release / commit: `translation-v1` / `f9839a3caa0d1920f596c12bc796adae4c58b39b`.
- Canonical English/source input checkpoint: starting `main` `21fb131912bf7ed161c08a70614702764464030d`; `paired/source.md` and `paired/translation.md` remain byte-identical to that checkpoint.
- Active glossary: P2, 283 rows, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`.
- Active translation guideline: **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; read Parts I–III, including Part I §8.1 and Q1–Q9.
- Explicit project decisions: [root decision history and adoption](../DECISIONS.md#policy-adoption-2026-10-05). The Adzom endnote requirement and all continuation/publication decisions remain in force within their recorded scope. The later explicit completion authorizations supersede the 2026-10-02 stop. Fresh chapter 4 review of the saved 396-note draft remains distinct from recovery of the missing 397-note package; no lost package is claimed recovered.

## Current translated coverage — not review coverage

All **674/674** canonical source pairs have matching English; **0** remain to draft. They represent 2,053 fixed source objects. These are representation counts, not accuracy or decipherment scores. 2,597 notes and 2,199 represented source obligations remain preserved; 140 unresolved pairs remain flagged. Prior independent agent chapter/assembly reviews retain their original scope and do not count as this new Phase D review.

[Existing final review](FINAL-REVIEW.md), [assembly QC](AGGREGATE-QC.md), [chapter review/usage records](chapters/), and [publication receipt](publication/translation-v1.json) remain preserved. Their earlier authoring, source-reconciliation or independent-agent review claims retain only their recorded scope; they do not count as completion of the newly adopted Phase D contract.

## Post-translation review — Phase D

- Review mode: **unassigned / not started**; the next assignment must explicitly choose review-only or authorize revision. This adoption task authorizes neither review nor revision.
- Reviewer/session and authoring run: **reviewer and session unassigned**; no new authoring run. Historical author/reviewer identities remain in the existing release reports above.
- English input commit/release: `translation-v1` at `f9839a3caa0d1920f596c12bc796adae4c58b39b`; unchanged canonical checkpoint `21fb131912bf7ed161c08a70614702764464030d`.
- Adopted common policy commit: `882454cb2576d0b2529296bd7a3a7c87371ab4cf`.
- Expected pair inventory: **674 pairs**, by chapter and terminal material as tabulated below.
- Actually reviewed pair ranges / count: **none / 0**.
- Unreviewed or missing ranges: **all 674 pairs are unreviewed under Phase D**. Mechanical inventory comparison found no missing or mismatched source/English pair IDs; this is not semantic review.
- Findings — corrected / justified no-change / unresolved: **not assessed**; no Phase D findings or dispositions created. Existing uncertainties remain visible in their original notes and usage records.
- Changed pairs rechecked and dependent views verified: **not applicable; 0 changed pairs**. No reading edition was regenerated. Byte-preservation checks do not count as semantic rechecking.
- Report path/commit and actual validation results: **no Phase D report or review commit yet**. Reuse the appropriate existing review/usage records when assigned, preserving historical reports; do not create parallel ledgers. Adoption-only validation is recorded below.
- Coverage disposition: **not started, 0/674**. Text disposition, separately: **not assessed**. Neither is clean publication approval or human certification.
- Remaining bounded work / shared proposals: owner assignment, PR integration, then all **674** pairs under Part III and Q1–Q9, including titles, colophons, closing material and unresolved spans. Unapproved local usage proposals are not activated by local history or by this propagation.

### Expected ordered inventory

| Chapter / part | Expected pairs | First → last in source order |
| --- | ---: | --- |
| 1 | 30 | `MTP-000001` → `MTP-000030` |
| 2 | 35 | `MTP-000031` → `MTP-000065` |
| 3 | 34 | `MTP-000066` → `MTP-000099` |
| 4 | 86 | `MTP-000100` → `MTP-000185` |
| 5 | 135 | `MTP-000186` → `MTP-000320` |
| 6 | 132 | `MTP-000321` → `MTP-000452` |
| 7 | 115 | `MTP-000453` → `MTP-000567` |
| 8 | 107 | `MTP-000568` → `MTP-000674` |

Chapter 8 includes its closing narrative, chapter/work colophons, annotations and blessings through MTP-000674. The existing chapter source files define the exact ordered inventory.

## Policy adoption validation

Executed on the connected Mac against starting `main` `21fb131912bf7ed161c08a70614702764464030d` before edits, then against this policy-adoption working tree. These are structural/integrity tests, not English review or semantic certification. `main` was verified unchanged before publication. All 36 remote tag/peeled-ref entries and the local tag inventory remain unchanged.

| Existing command | Before adoption | After adoption | Classification |
| --- | --- | --- | --- |
| `python3 -B scripts/validate_paired.py` | FAIL: PAIRED VALIDATION FAILED: invalid pair metadata for M | FAIL: PAIRED VALIDATION FAILED: invalid pair metadata for M | Pre-existing failure or execution limit |
| `python3 -B scripts/validate_translation_aggregate.py` | PASS | FAIL: TRANSLATION AGGREGATE FINAL ERROR: Prior released input changed: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B scripts/build_golden_aggregate.py verify` | FAIL: ModuleNotFoundError: No module named 'pyewts' | FAIL: ModuleNotFoundError: No module named 'pyewts' | Pre-existing failure or execution limit |
| `python3 -B scripts/test_translation_pipeline.py` | PASS: 36 tests | PASS: 36 tests | Pass retained |
| `python3 -B scripts/test_translation_aggregate.py` | PASS: 24 tests | PASS: 24 tests | Pass retained |
| `python3 -B scripts/test_translation_aggregate_signoff.py` | TIMEOUT after 180 seconds; incomplete run, not a pass | TIMEOUT after 180 seconds; incomplete run, not a pass | Pre-existing failure or execution limit |
| `git diff --check` | PASS | PASS | Pass retained |

Adoption-specific checks **PASS**: exact pinned standard/glossary bytes and hashes; standard 2.1.0; CSV 283 data rows and eight columns; exact, singly anchored P1/P2/P3 records; full shared Phase D instructions retained; populated project histories preserved; matching ordered inventory of **674** unchanged source/English pairs; relative links/anchors in the bounded documents checked with **no introduced broken links**; `git diff --check` clean. **1184 tracked files outside the eight-file adoption set are byte-identical** to the starting checkpoint. This includes fixed Tibetan, source editions/registers, canonical English, active notes, pair IDs, historical release inputs and policy copies, generated readers, scripts, schemas and unrelated files.

The newly failing English release checks bind active policy paths to the old release-time hashes; they do not distinguish later active-policy adoption from alteration of a release input in the current checkout. Historical contracts, manifests, signoffs and archived bytes were left untouched rather than re-signed or regenerated. The adopted current tree must not be represented as passing those historical release gates.

**Integration blocker:** the adoption branch is complete as a policy-only candidate, but `main` adoption awaits PR merge with the legacy active-path/release-pin incompatibility explicitly visible. Branch protection was not reported on `main`; the PR route is used to avoid silently publishing a failing release-validation state on `main`. Any validator/manifest architecture change is outside this task and requires a separately scoped owner decision. This blocker does not authorize English correction, a new release, or commencement of Phase D.

## Next finite task

Await PR integration and an explicit reviewer assignment. That reviewer must freeze the actual English/source/policy inputs and mode, review the complete inventory above, and record coverage separately from text disposition. **No review or English revision has started.** Do not reopen source collation or create a new release for this policy-only task.

## Preserved release handoff — before policy adoption

Updated 2026-10-04. All eight working chapters are complete: 2053 fixed source objects / 674 pairs / 2597 notes. Zero chapters remain to draft. Representation includes explicitly unresolved passages and metadata; these counts do not measure accuracy or complete decipherment.

Governing Tibetan: `golden-v1` at `4d6ba07e1b3379183633127cd387d98d8195eb95`. Fixed source, canonical glossary, source audits and signed chapter 1/2/3/5/6/7/8 packages remain unchanged. Chapter 4 has completed fresh review of its saved 396-note draft, with three separately logged corrections; the absent historical final package is not presumed recovered. Its original draft and the full starting working edition remain preserved in Git history and `archive/working-edition-3972b751`.

| Chapter | Objects | Pairs | Notes | Publication |
| --- | ---: | ---: | ---: | --- |
| 1 | 97 | 30 | 112 | [`translate-ch01-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch01-v1) |
| 2 | 124 | 35 | 175 | [`translate-ch02-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch02-v1) |
| 3 | 120 | 34 | 165 | [`translate-ch03-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch03-v1) |
| 4 | 294 | 86 | 396 | [`translate-ch04-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch04-v1) |
| 5 | 416 | 135 | 520 | [`translate-ch05-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch05-v1) |
| 6 | 376 | 132 | 435 | [`translate-ch06-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch06-v1) |
| 7 | 342 | 115 | 373 | [`translate-ch07-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch07-v1) |
| 8 | 284 | 107 | 421 | [`translate-ch08-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translate-ch08-v1) |

Actual chapter releases: 8/8. The complete annotated `translation-v1` release and its post-tag receipt are verified. Canonical paired files cover chapters 1–8; all eight fixed chapter directories remain available.

All 2199 source obligations are represented in the chapter apparatus. Native main-text comparisons preserve their recorded uncertainties, untranscribed annotations, actual print differences and electronic correction history. Fresh chapter 4 review does not claim a second nineteen-page visual audit. Full commentary translation, complete multi-layer proofreading, exhaustive witness collation, automated semantic certification and independent human certification are not claimed. Provisional terminology remains inactive.

The connected Mac provides authenticated publication access. Tags are created only at freshly verified actual main commits after strict final validation; receipts follow the fixed tags. Historical working authorizations and pinned candidates are unchanged. Source editorial queues remain closed; research leads remain outside this bounded translation.

Next finite task: Bounded translation publication complete; retain explicit human-review questions and inactive terminology proposals.

## Active Phase D session — 2026-10-05

Current owner authorization starts review-and-revise, superseding the earlier unassigned/not-started handoff. Policy PR #1 is merged at `46110acd02a6caa14a00f91605c1a478eda72bcd`; reviewer/session GPT-6 Astra Pro / MTP-PhaseD-20261005 is distinct from all original authoring runs. All 674 current pairs are frozen for review. Chapter 1 body has been read; continue its active notes, then MTP-000031–000674. Three supported terminology findings are recorded before editing, with no corrections yet applied. Existing release gates fail on the already-adopted glossary; do not alter signatures or loosen release checks. Preserve fixed Tibetan, source metadata, original drafts and all tags. See [the current review package](FINAL-REVIEW.md#phase-d-review); coverage remains partial and readiness unassessed.

### Phase D checkpoint — chapters 1–4 read

Reviewer MTP-PhaseD-20261005 has now read all 185 pairs through MTP-000185 and their 848 active notes. Supported findings are recorded before correction in [the existing review report](FINAL-REVIEW.md#phase-d-review); no English repair has yet been applied. Continue at MTP-000186 (chapter 5), then through MTP-000674. Review coverage is partial; note/usage reconciliation, repairs, dependent-reader regeneration and verification remain.

### Phase D checkpoint — chapters 1–6 read

Reviewer MTP-PhaseD-20261005 has read all 452 pairs through MTP-000452 and their 1,803 active note definitions. Supported findings are recorded before correction in [the existing review report](FINAL-REVIEW.md#phase-d-review); no English repair has yet been applied. Continue at MTP-000453 (chapter 7), then through MTP-000674. Coverage is partial; terminology consolidation, note/usage reconciliation, repairs, dependent-reader regeneration and verification remain.
