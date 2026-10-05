# String of Pearls — English working edition

## Current post-translation-review working text — 2026-10-05

The canonical authored English is `translations/chapters/NN/translation.md`. The eight chapters, `paired/translation.md`, and chapter/whole-book reading and machine files now form a **working revision of `translation-v1`**, not a new formal release. The original `translation-v1` and chapter tags, signatures, receipts, historical QC and original drafts remain unchanged and apply only to their fixed release bytes.

The independent source-order review covers all **674 pairs / 2,053 golden objects / 2,597 active notes**. Supported repairs affect **134 English pairs**; 140 pairs remain explicitly unresolved. The current report distinguishes review coverage, local provisional constructions, repair self-checks and text readiness. Counts are not accuracy percentages. No final human certification or four-book harmonization is claimed.

Build or verify the working views, from the repository root:

```sh
.venv/bin/python -B scripts/review_working_text.py build
.venv/bin/python -B scripts/review_working_text.py verify
.venv/bin/python -B scripts/test_review_working_text.py
```

The working command reuses the existing parser, source-audit/notes/sequence validators and Markdown renderer. It verifies fixed Tibetan and source metadata against the frozen review input and golden-v1, requires adopted standard 2.1.0 and the full 283-row/eight-column P1/P2/P3 glossary, and labels generated manifests as working/unapproved. It does not alter or bypass the release functions. The original release validators remain available and intentionally reject post-release English changes or policy-pin drift; do not reseal their signatures merely to publish these working files.

Current terminology dispositions are appended to existing notes and to `review_disposition` fields in existing usage/proposal/note-map records. Original authoring fields, eight-column proposal bodies and approval history are retained. The shared glossary is unchanged; proposed shared labels remain proposed. See [the review report](FINAL-REVIEW.md#phase-d-review) and [handoff](HANDOFF.md).

---

The documentation below records the original edition pipeline and retains its historical scope.

The complete eight-chapter translation follows the fixed [golden Tibetan](../golden/reading.md), unchanged [glossary](../glossary/expanded_tibetan_english_glossary.csv), and [translation standard](../guidelines/tibetan_translation_standard_v2.md). This is an agent-produced annotated working edition for human review.

[Read the complete English edition](reading.md) · [Read Tibetan and English](bilingual.md) · [Coverage and limits](coverage.json) · [Final review](FINAL-REVIEW.md)

Published as [`translation-v1`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/translation-v1); see the [verified release receipt](publication/translation-v1.json).

All 2053 fixed objects are represented in 674 pairs with 2597 locally linked notes. No chapters remain to draft. Actual chapter releases: 8/8.

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

- Chapter 1: [English](chapters/01/reading.md) · [Tibetan and English](chapters/01/bilingual.md)
- Chapter 2: [English](chapters/02/reading.md) · [Tibetan and English](chapters/02/bilingual.md)
- Chapter 3: [English](chapters/03/reading.md) · [Tibetan and English](chapters/03/bilingual.md)
- Chapter 4: [English](chapters/04/reading.md) · [Tibetan and English](chapters/04/bilingual.md)
- Chapter 5: [English](chapters/05/reading.md) · [Tibetan and English](chapters/05/bilingual.md)
- Chapter 6: [English](chapters/06/reading.md) · [Tibetan and English](chapters/06/bilingual.md)
- Chapter 7: [English](chapters/07/reading.md) · [Tibetan and English](chapters/07/bilingual.md)
- Chapter 8: [English](chapters/08/reading.md) · [Tibetan and English](chapters/08/bilingual.md)

Endnotes distinguish actual Adzom differences, transcript corrections that agree with Adzom, omitted annotations, presentation, uncertain readings and translation questions. Unresolved language remains visible. No proposed glossary term is activated. The bounded edition does not claim complete commentary decipherment, exhaustive witness collation or human certification.

Canonical content is in `paired/source.md` and `paired/translation.md`; both cover all eight chapters. Generated readings mirror the fixed chapter snapshots. Original author archives are immutable; later reviewed changes are logged separately. See [handoff](HANDOFF.md), [plan](PLAN.json), [endnote policy](ENDNOTE-POLICY.md), and [pipeline schema](PIPELINE-SCHEMA.md).

## Shared policy and review handoff

For the next assigned completed-English review, use [the active standard 2.1.0](../guidelines/tibetan_translation_standard_v2.md#post-translation-review), [the shared glossary](../glossary/expanded_tibetan_english_glossary.csv), [P1/P2/P3 adoption](../DECISIONS.md#policy-adoption-2026-10-05), and [the current handoff](HANDOFF.md#post-translation-review--phase-d). All use template snapshot `882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Earlier release descriptions above refer to their fixed historical policy inputs, not a claim that the unchanged English already conforms to this newly adopted policy. Review is unassigned and not started; adoption on `main` awaits PR merge.
