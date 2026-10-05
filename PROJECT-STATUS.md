# Published English working edition

## Current Phase D disposition — 2026-10-05

**The whole-work post-translation review is complete.** Reviewer/session: **GPT-6 Astra Pro / MTP-PhaseD-20261005**, independent of the original authoring runs. Input commit: `46110acd02a6caa14a00f91605c1a478eda72bcd`; adopted policy: template `882454cb2576d0b2529296bd7a3a7c87371ab4cf`, standard 2.1.0 Parts I–III and the complete 283-row/eight-column P1/P2/P3 glossary. No new shared assignment or book-specific default was approved.

All **674 pairs (MTP-000001–MTP-000674), eight chapters, 2,053 golden objects and 2,597 active notes** were reviewed. **134 English pairs** were corrected and self-checked against Tibetan, and the revised English was read continuously. **540 English bodies remain unchanged**. Current dispositions were appended to **268 notes, 318 usage records and 197 proposal records**, preserving original evidence and approval history. **No unreviewed range remains.**

**Text readiness is separate:** this is a reviewed, corrected **working revision of translation-v1**, not a new formal release or final human certification. **140 pairs remain explicitly unresolved**, with exact locations and alternatives in their existing notes/status records. Bounded remaining work is owner/source/human adjudication of those questions and the shared reconciliation queue, not completion of a missing review pass. No four-book harmonization is claimed.

Canonical authored English remains `translations/chapters/NN/translation.md`. All **46 dependent chapter/whole-work reading and machine files**, including `paired/translation.md`, were regenerated from it. Fixed Tibetan/source metadata, pair and note IDs/order/allocation, historical drafts, signatures, releases and all **18 remote release tags** are unchanged. Do not edit generated English separately or reseal old release approvals for this working text.

Working commands from the repository root:

```sh
.venv/bin/python -B scripts/review_working_text.py build
.venv/bin/python -B scripts/review_working_text.py verify
.venv/bin/python -B scripts/test_review_working_text.py
```

Actual results: working build/read-only verification and deterministic reproduction passed; **17 working-view, 36 pipeline and 24 aggregate tests passed**; golden-v1 validation passed. **95 protected files** and all remote tags were checked unchanged. The legacy signoff and draft-continuation test runs reached their explicit 180-second limits and are **not claimed passed**. The pre-existing generic paired-parser failure and adopted-glossary/release-pin rejection remain documented; release gates were not loosened. The standard's documented semantic examples were not separately executed as semantic tests. No hosted CI is configured. The final working-text, 17-test working-view, 36-test pipeline and golden-source checks passed again during the main-integration continuation; the review report corrects the earlier unconditional whitespace-check PASS.

The full evidence, exact Tibetan/before/after ledger, no-change decisions, shared questions, self-check and validation results are in [the existing review report](translations/FINAL-REVIEW.md#phase-d-review). The complete review package **landed in `main` through [PR #2](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/pull/2)**, merged at [`44ac091`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/commit/44ac091e588c2321c3d8f4addf88af37ed4b6d33) on 2026-10-05. The merged tree exactly matches verified delivery `2b18a90f242810a3d2cec60c6e6424db05543cd5`; all 46 working outputs and the 17-test working-view suite pass on merged main. The review branch is retained for stable note links. No review-package delivery work remains; the unresolved text and shared decisions retain their separate status. Own-repair verification is a self-check, not another independent review.

---

## Historical status and earlier handoff checkpoints

The earlier release and interim review statements below retain their historical scope. Earlier “not started,” “partial,” “pending” or continuation-point statements do not describe the completed current pass above.

## Shared policy adoption — 2026-10-05

The active standard **2.1.0**, the **283-row/eight-column** glossary, and the shared Phase D operating contract are adopted from exactly `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Standard and glossary are byte-identical to that snapshot; there is no local terminology exception. See [P1/P2/P3 and adoption provenance](DECISIONS.md#policy-adoption-2026-10-05) and the [review handoff](translations/HANDOFF.md#post-translation-review--phase-d).

Scope completed on this branch: **1/1 repository policy adoption; 0 English reviews; 0 translation corrections**. The four-repository propagation task does not assign reviewers. Publication route: `policy/adopt-template-882454cb` → pull request to `main`; merge into `main` is not yet verified. Legacy release checks bind earlier active policy bytes, so their current-tree incompatibilities are disclosed rather than changing signed manifests or validators.

Ready for an owner-assigned **review-only** pass using this branch's common policy and the fixed English below; adoption on `main` awaits PR merge. Reviewer/session: **unassigned**. Reviewed coverage: **0/674 pairs**. Review completion: **not started**. Text disposition: **not assessed**. No revision authority, new release, or independent/human certification is inferred from policy adoption.

Preserved starting `main`: `21fb131912bf7ed161c08a70614702764464030d`. Fixed Tibetan: `golden-v1` (`4d6ba07e1b3379183633127cd387d98d8195eb95`). Fixed English: `translation-v1` (`f9839a3caa0d1920f596c12bc796adae4c58b39b`). Canonical content remains `paired/source.md` and `paired/translation.md`; **674** matching pairs represent 2,053 fixed source objects. 2,597 notes and 2,199 represented source obligations remain preserved; 140 unresolved pairs remain flagged. Prior independent agent chapter/assembly reviews retain their original scope and do not count as this new Phase D review.

The Adzom endnote requirement and all continuation/publication decisions remain in force within their recorded scope. The later explicit completion authorizations supersede the 2026-10-02 stop. Fresh chapter 4 review of the saved 396-note draft remains distinct from recovery of the missing 397-note package; no lost package is claimed recovered.

Actual before/after policy validation, exact input hashes, complete chapter inventory, and pre-existing versus introduced failures are recorded in [the existing handoff](translations/HANDOFF.md#policy-adoption-validation). Historical policy copies, release tags, English, notes, Tibetan, source registers and pair identities are unchanged. The active policy update does not retroactively certify the English against the new standard.

Next finite task: await the owner's reviewer assignment and PR integration; then review all **674** pairs, including closing material, under Part III and Q1–Q9. No review has begun here.

## Preserved publication state — before policy adoption

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

## Active post-translation review — 2026-10-05

Phase D is assigned by the current owner instruction and in progress on `review/phase-d-20261005`, input `46110acd02a6caa14a00f91605c1a478eda72bcd`. Policy adoption is merged (PR #1), not pending. Reviewer: GPT-6 Astra Pro / MTP-PhaseD-20261005. Finite scope: all 674 pairs / eight chapters; source-order chapter 1 body read, note reconciliation and the remaining chapters pending. No English correction applied yet. Coverage is partial; readiness is not claimed. Current evidence and continuation: [Phase D review](translations/FINAL-REVIEW.md#phase-d-review). Historical release statements below/above retain their original scope.

### Phase D checkpoint — chapters 1–4 read

Reviewer MTP-PhaseD-20261005 has now read all 185 pairs through MTP-000185 and their 848 active notes. Supported findings are recorded before correction in [the existing review report](translations/FINAL-REVIEW.md#phase-d-review); no English repair has yet been applied. Continue at MTP-000186 (chapter 5), then through MTP-000674. Review coverage is partial; note/usage reconciliation, repairs, dependent-reader regeneration and verification remain.

### Phase D checkpoint — chapters 1–6 read

Reviewer MTP-PhaseD-20261005 has read all 452 pairs through MTP-000452 and their 1,803 active note definitions. Supported findings are recorded before correction in [the existing review report](translations/FINAL-REVIEW.md#phase-d-review); no English repair has yet been applied. Continue at MTP-000453 (chapter 7), then through MTP-000674. Coverage is partial; terminology consolidation, note/usage reconciliation, repairs, dependent-reader regeneration and verification remain.
