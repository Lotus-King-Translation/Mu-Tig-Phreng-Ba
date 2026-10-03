# Chapter 5 independent agent QC

**Complete independent agent review: ready with explicit review flags for the requested chapter 5 working candidate. Final content identities are bound below. This is not formal-release clearance.**

Reviewer: `/root/ch05_qc`. Translator: `/root/ch05_translate`; the author's lexical helper is part of the author side, not the independent reviewer. Review date: 2026-10-03. Review mode: full requested chapter, in sequential batches. This report distinguishes representation from resolution and content review from formal publication.

## Scope and authority

The requested scope is MTP-S000636–MTP-S001051: 416 fixed golden objects in 135 pairs, MTP-000186–MTP-000320. Source is `golden-v1`, commit `4d6ba07e1b3379183633127cd387d98d8195eb95`; the chapter source snapshot SHA-256 is `0c574b76b678a3b129dfd584bfd3ad694b87956febaf98726e02106590958b3e`.

The reviewer read all 416 fixed source objects, six recorded golden changes, eleven golden uncertainty statements, the full active combined standard, all 222 glossary rows with all eight columns, AGENTS.md, FORMAT.md, DECISIONS.md, current status/handoff, the source register, and the frozen chapter contract. The glossary SHA-256 is `6b9029f7f02494e947e6a1273da7916b358e4d0738b35f012ce4da662d3fbbaf`; the standard SHA-256 is `934f54616d1c55a6ecb0c594108397cca5b317dafc7c2c945972ffd1351b7760`.

The user explicitly authorized chapter 5 after disclosure that chapter 4's final revision and supporting reports were not saved. Chapter 4 remains its pinned unsigned 396-note draft. This review does not recreate its missing signoff, declare missing prior releases complete, or authorize chapter 6.

Native comparison is conducted by a separate audit team. The QC reviewer has not inspected native images and will not claim independent visual verification of the 27-page audit. Reading source-audit records and their translated notes does not equal repeating that visual inspection.

## Review progress

- Batch 1: pairs 186–230, S636–767, 45 pairs / 132 objects, all English bodies and all 19 translator notes read against the fixed source. No confirmed body mismatch identified in this batch. Three locally unresolved pairs (190/S645, 193/S651, 227/S756) are visibly represented.
- Batch 2: pairs 231–269, S768–898, 39 pairs / 131 objects, all new English bodies and translator notes T05-020–032 read against the fixed source. Combined reviewed draft scope is 84 pairs / 263 objects and 32 translator notes. The five further locally unresolved pairs (239/S793, 252/S838, 263/S878, 267/S888, 269/S897) retain their problematic wording visibly.
- Batch 3: pairs 270–320, S899–1051, 51 pairs / 153 objects, all new English bodies and translator notes T05-033–049 read against the fixed source. All 135 English pairs / 416 source objects and 49 translator notes have now been reviewed; sixteen locally unresolved pairs remain visibly represented.
- Source apparatus: all 14 golden-history endnotes and the semantic content/locators of all 415 native-audit records reviewed. Exact duplicate boilerplate was de-duplicated for reading; all differing explanations, limitations, readable fragments, English consequences and local allocations were examined. A focused check verified every generated native endnote preserves the reviewed record, applicable readings, evidence locator and exact source-anchor/pair reference allocation. Markdown continuation indentation was accounted for. This is documentary/translation review, not new visual inspection.
- Lexical support: all 277 final-review usage records (including merged-prefix changes), all 224 eight-column proposal rows, and all 42 additional lexical notes read. The S998 and S925 extensions to existing notes were read. A focused read-only check confirmed all 466 recorded usage loci have exact fixed-source spans, the correct source-to-pair allocation, translator-note-map source/pair bindings, note definitions, and actual local pair references. The two source hashes in usage.json match their explicitly named files. These are traceability checks, not automated semantic certification.
- Q05-008's final local classification amendment, its existing reader-note addition, and the revised proposal were reviewed. Final lexical totals are 277 records (233 provisional / 44 grammatical), 466 source-linked loci (380 provisional / 86 grammatical), and 224 unique inactive proposals. All comparison/canonical-entry identities exist in the unchanged glossary. Counts measure records or loci, not tokens or accuracy.
- Final generated coverage was read and agrees with the reviewed scope: 135 pairs / 416 objects, 520 notes, all 432 obligations covered, no unrepresented chapter objects or unallocated obligations, 92 translated / 16 unresolved / 27 nontranslatable pairs. Both lexical support files are present. The coordinator's final read-only candidate validation passed.
- The coordinator normalized 53 pair-separator boundaries only, recorded as presentation change C012. The reviewer independently confirmed all 135 final pair bodies match the reviewed original complete draft after removal of note references and boundary spacing. The coordinator additionally checked unstripped body identity and all 104 raw verse-pair line counts, totaling 385 lines. All final 45 manifest input hashes and four chapter-relative output hashes were independently verified, together with final translation, manifest, glossary and standard identities.
- No automated semantic or independent human certification is claimed. The standard's 30 semantic regression fixtures have not been run by this reviewer.

## Findings

### Q05-001 — scope of “not two”

- Source: S762 `བྱ་དང་བྱེད་པ་གཉིས་མེད་པས`; S764 `ཡུལ་དང་དབང་པོ་གཉིས་མེད་པས`.
- Draft: pair 228, “Because doing and the doer are not two”; pair 229, “Because objects and faculties are not two.”
- Label/category: open question; meaning/scope and annotation.
- Severity: Medium. Confidence: Moderate that the choice needs explicit disclosure; the preferred interpretation remains unsettled.
- Evidence: the English can assert nondifference, whereas S758–760 negate establishment/existence; S760's `གཉིས་མེད` is itself rendered “there are no two stains.” Both absence of the two members and a nondual reading require consideration.
- Minimal action: extend T05-019 to disclose the tentative nondual reading and the alternative “the two ... are absent”; do not silently replace the fixed source or impose a settled doctrinal conclusion.
- Authority: local annotation proposal, not an approved glossary decision.
- Rules: Part I §§5–7; QC Q2–Q4, Q7, Q9.
- Disposition: author accepted and expanded T05-019 explicitly; reviewer read the amendment and accepts it as a responsible open question. Neither reading is thereby settled.

### Q05-002 — predication versus existential absence

- Source: S892 `འགྱུ་བ་མ་ཡིན་དྲན་པ་གནས`.
- Draft: pair 268, “There is no movement; mindfulness abides.”
- Label/category: confirmed error; meaning/scope.
- Severity: Medium. Confidence: High regarding the predicate distinction; the implicit subject remains open.
- Evidence: `མ་ཡིན` negates predication, “is not movement,” whereas the draft asserts existential absence. Nearby S887 `སེམས་མེད` supplies an actual absence construction and should not flatten this distinction.
- Minimal action: “[It] is not movement; mindfulness abides.” Bracket the unexpressed subject and retain the note's unresolved continuity rather than inventing an agent.
- Authority: local source-supported semantic/syntactic correction; no glossary update.
- Rules: Part I §5; QC Q3, Q9.
- Disposition: author applied the minimal correction; reviewer verified the corrected English.

### Q05-003 — local commitment wording and annotation cleanup

- Source: S678 `དམ་ཚིག`.
- Draft: pair 200 “commitments”; T05-007 calls the bare mapping a local proposal.
- Label/category: documentation gap; provisional terminology. Severity: Low. Confidence: High that prior usage differs, without evidence that either local proposal is a body mistranslation.
- Evidence: the saved chapter 4 draft uses provisional “samaya.” Neither choice is an approved bare glossary entry.
- Minimal action: explicitly compare and scope chapter 5's provisional “commitment” in its note and lexical records; do not change either chapter merely for stylistic uniformity. The coordinator also requested removal of T05-007's unrelated harmful-act disclaimer from the ritual-negation note.
- Disposition: author added the explicit commitment/samaya comparison and removed the unrelated framing; reviewer verified both note changes, analogous cleanup of T05-027, and the final usage/proposal comparison. No body change requested.

### Q05-004 — shared negation at S940 remains possible

- Source: S940 `གཟུང་བར་བྱ་ཞིང་འཛིན་པ་མེད`.
- Draft: pair 282, “there is what is to be apprehended, and no apprehending subject.” T05-036 initially says the source “does not negate its first clause.”
- Label/category: open question with overconfident documentation; syntax/negation scope and annotation.
- Severity: Medium. Confidence: High that the categorical annotation exceeds the evidence; the preferable reading remains unsettled.
- Evidence: final `མེད` can plausibly scope both members coordinated by `ཞིང`, despite no earlier negative. The selected positive existential paraphrase is not compelled merely by absence of an earlier `མེད`.
- Minimal action: keep the selected positive treatment explicitly tentative and record the alternative “neither what is to be apprehended nor an apprehending subject”; no forced body repair or source change. The coordinator independently raised the same scope concern.
- Authority: annotation of an unresolved construction, not a settled glossary or doctrinal decision.
- Rules: Part I §§5–7; QC Q3–Q4, Q7, Q9.
- Disposition: author applied the requested note-only amendment; reviewer verified it. The open source interpretation remains explicit.

### Q05-005 — unsupported “belief” in a note

- Source: S1028 `སྤྲུལ་མཐོང་དེ་ཉིད་མཐོང་བས་བདེན`.
- Draft: T05-046 describes a “seeing/belief criterion of truth.” The English body speaks only of seeing.
- Label/category: confirmed annotation overstatement; meaning/scope. Severity: Low. Confidence: High.
- Evidence: the cited Tibetan and translated body express seeing, without a separate belief expression.
- Minimal action: delete “/belief” from T05-046. No English-body, source, or glossary change.
- Rules: Part I §5; QC Q3, Q7, Q9.
- Disposition: author removed “/belief”; reviewer verified the corrected note. No body change.

### Q05-006 — proposed headwords must not inherit omitted modifiers or negatives

- Source and draft proposal evidence: S706 `འབྱུང་བ་ཆེ`, with bare proposed headword `འབྱུང་བ་` mapped to “great element”; S752 `ཀུན་ཏུ་མ་བརྟགས`, with bare `བརྟགས་` mapped to “not imputed”; S825 `འགག་པ་མེད་པ`, with bare `འགག་པ་` mapped to “without cessation.”
- Label/category: confirmed documentation error; provisional glossary proposal scope. Severity: Medium. Confidence: High.
- Evidence: the English modifier/negation is supported by the complete occurrence but absent from the proposed Tibetan headword. The prospective mapping could otherwise carry that modifier or negative to a different occurrence. The English body is correctly source-supported at these loci.
- Minimal action: give the bare proposed headwords “element,” “imputed,” and “cessation,” respectively, and explicitly retain the complete occurrence-specific realizations in usage/scope; alternatively use a complete construction as the proposed headword.
- Authority: proposal documentation only; no source, body or canonical-glossary change.
- Rules: Part I §§5–7; QC Q2–Q4, Q7, Q9.
- Disposition: author adopted the bare primary proposals and explicit occurrence-scope explanations. Reviewer verified all three corrected rows and usage explanations; the locally supported modifier and negatives remain in the English body.

### Q05-007 — stale S940 certainty in usage metadata

- Source: S940 `གཟུང་བར་བྱ་ཞིང་འཛིན་པ་མེད`.
- Draft evidence: usage T05-U260 still stated “positive first clause not negated by later subject absence” after T05-036 had been corrected under Q05-004.
- Label/category: confirmed documentation inconsistency; unresolved negation scope. Severity: Medium. Confidence: High about the inconsistency; the preferred source reading remains unsettled.
- Minimal action: align usage condition_evidence with T05-036's tentative positive reading and possible coordination-wide final negation.
- Disposition: author applied the metadata correction; reviewer verified that neither reading is claimed settled. English body unchanged.

### Q05-008 — inconsistent authority classification of the same verbal form

- Source: S958 and S1023 both have `བཟུང་བས`, rendered “by apprehending.”
- Draft evidence: T05-U202 treats the S958 use as provisional without a canonical entry, while T05-U268 treats S1023 as grammatical under canonical `གཟུང་བ་` (apprehended object), without explaining a context-dependent authority distinction.
- Label/category: confirmed documentation inconsistency; provisional terminology authority. Severity: Low. Confidence: High regarding the inconsistent classification; no body mistranslation asserted.
- Minimal action: use a consistent provisional verbal-form relation for both occurrences, with local note and proposal coverage; keep the instrumental realization at actual source loci and the bare proposed primary “apprehending.”
- Disposition: author made U268 provisional with no asserted canonical assignment, added the explicit local comparison to existing T05-046, and included both source loci in the existing proposal with bare primary “apprehending.” Reviewer verified the complete amendment. The actual instrumental English remains unchanged.

## Important conforming choices

The protected ordinary mind, mental faculty, intrinsic nature, enlightened intent, primordial knowing and discerning knowing remain identifiable. Whole-expression compounds are distinguished from standalone terms. The sensory “sound” for canonical `སྒྲ་` “word” is locally proposed and annotated, not silently activated. Textual `རྒྱུད` “tantra” is separately provisional against canonical “continuum.” The opaque S756 wording and missing S645 complement remain visible rather than normalized. These are conforming treatments within the stated review scope; they do not certify every provisional interpretation.

## Explicit review flags and limits

All requested English pairs and notes are represented and reviewed. Sixteen pairs remain locally unresolved, with source wording or uncertain relationships explicitly retained: 190/S645, 193/S651, 227/S756, 239/S793, 252/S838, 263/S878, 267/S888, 269/S897, 273/S910, 285/S952, 286/S956, 297/S986–988, 298/S989–991, 309/S1021, 311/S1027, and 312/S1028. The responsibility to retain these flags is independent of numerical coverage. Other tentative readings, including S762/S764 and S940 negation scope, remain disclosed in their local notes even where the pair has no retained opaque form.

The final reader apparatus has 520 notes: 91 translator notes (49 original plus 42 lexical), 14 golden-history notes, and 415 native-audit notes. The native findings comprise 340 source-omission, 45 presentation, and 30 source-layer records. The documentary audit records 416 anchor checks over 27 native images; two layer boundaries remain uncertain, at S729 and S1033. The omission records preserve limitations and any readable fragments without claiming that all smaller explanatory writing has been transcribed or translated. Numeric coverage of all 432 required obligations does not settle those source omissions or boundaries.

All 224 glossary proposals remain inactive. The review distinguishes local provisional decisions from approved glossary authority, preserves whole-expression precedence, and does not certify provisional interpretations merely because their source links are valid. The native audit is a separate team's work; this reviewer assessed its documentary/translation apparatus and did not view the images. No automated semantic or independent human certification is claimed, and the 30 standard semantic-regression fixtures were not run by this reviewer.

## Final identities and outcome

| Artifact | SHA-256 |
| --- | --- |
| Chapter source.md | `0c574b76b678a3b129dfd584bfd3ad694b87956febaf98726e02106590958b3e` |
| Final translation.md | `67505fa2bf43bee10a240fcbea61772e44a02b2404ef6cb8afe312aef58849e7` |
| Final build-manifest.json | `0afe04a17427ac29e9aff38de4e8c469e9aafbd7a011a9a8acb4a6a49e1abd02` |
| usage.json | `ce7053e925101d6f7f6fdafbcf23752581e79b135f52f398f24b8a55a9463ec1` |
| glossary-proposals.json | `2ef77bb1e447f345476796da34e144a41f702d6d96055dde8fb444aed77c33e8` |

Coverage: **complete** for the requested chapter. Disposition: **ready_with_explicit_review_flags**. Open blocking correction requests: **none**. Q05-001–008 have all received verified local corrections or explicit open-question treatment. The paired qc.json binds this report, the final source, translation and manifest.

The candidate represents all requested source units while preserving the sixteen unresolved pair flags, the source-apparatus limitations and inactive lexical proposals. This outcome is not clearance for a formal English release, approval of the proposed glossary entries, a claim that chapter 4's missing final support exists, or authorization to begin chapter 6. Changes to the bound translation, source, manifest inputs/outputs or this review require revalidation and appropriately scoped renewed review.
