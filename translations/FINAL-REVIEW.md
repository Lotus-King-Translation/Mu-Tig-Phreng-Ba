<a id="phase-d-review"></a>
# Post-translation review — Phase D

**State: whole-work review, supported repairs, repair self-check and working-view regeneration completed. This is not formal release approval or human certification.** Date: 2026-10-05. Reviewer/session: **GPT-6 Astra Pro / MTP-PhaseD-20261005**. This session is independent of the prior authoring runs listed below. Verification of repairs made by this session is a **self-check**, not a second independent review. Git commits use the repository owner’s configured identity; that is not a claim of human language certification.

## Final current disposition — 2026-10-05

**Review coverage: complete.** All **674 Tibetan–English pairs**, all **2,053 golden objects**, and all **2,597 active note definitions** were reviewed in source order. All **134 repaired English pairs** were rechecked against the Tibetan; the revised English was read continuously through all 674 pairs. **There are no unreviewed pair ranges or unfinished review-pass steps.**

**Text disposition: reviewed and corrected working revision of translation-v1, not an approved formal release.** **140 pairs remain explicitly unresolved**, with the same occurrence-level status inventory and linked alternatives/source questions. Other locally provisional constructions remain visibly qualified. Resolving the local awakened-mind label at MTP-000550 did not close its causal-construction question. Further work is bounded adjudication of those existing source/construction questions and the shared reconciliation queue, not a missing whole-work pass.

Corrections: **134 changed English pairs; 540 unchanged English pair bodies; 189 replacement records / 195 occurrences; 268 existing note definitions updated; 318 existing usage records and 197 existing proposal records given additive current dispositions.** PD-001–PD-027 are English finding groups, PD-028 reconciles current terminology status, and PD-029 repairs portable links in those 268 note additions. The counts are edit/coverage counts, never accuracy percentages. Original note prose, proposal bodies and approval histories are preserved. The shared glossary, fixed Tibetan, stable IDs/order/roles/format metadata, historical releases and tags are unchanged.

The following source-order checkpoints and their interim statements are chronological records, not the current disposition. Their pre-edit findings remain evidence of what was recorded before correction. The final applied ledger, self-check and actual validation results govern the completed review. The original release review retained later in this file applies only to its old fixed inputs.

## Authority and frozen inputs

The owner’s current `POST_TRANSLATION_REVIEW`, `review-and-revise` instruction authorizes the complete existing English and translation-note review in this repository only, minimal supported corrections, dependent-reader regeneration and ordinary commits/pushes. It does not authorize Tibetan changes, segmentation changes, glossary reassignment, a new formal release or tag movement. See the appended local decision.

The input is `46110acd02a6caa14a00f91605c1a478eda72bcd` (remote `main`, merge of policy-adoption PR [#1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/pull/1), merged 2026-10-05T06:35:03Z). Existing English edition: `translation-v1`; its fixed release peels to `f9839a3caa0d1920f596c12bc796adae4c58b39b`. Golden edition: `golden-v1`, commit `4d6ba07e1b3379183633127cd387d98d8195eb95`; governing payload is **golden/reading.json**, not reading.md.

Active common policy: template commit `882454cb2576d0b2529296bd7a3a7c87371ab4cf`, standard **2.1.0, Parts I–III**, complete **283 data rows / eight columns** and adopted P1/P2/P3. Current glossary and standard bytes were compared with that exact upstream commit via GitHub and match. Part I §8.1 and Part III were read. All startup files were read. No later owner-approved local terminology exception was found; prior drafting/publication exceptions retain only their recorded historical scope. Initial template provenance and old proposals are not substituted for this adoption.

| Frozen input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `2532b82a0464e31e50c624b7a6d0c102992c91fd48bb331f983b0140b58ac16e` |
| `FORMAT.md` | `c4c6d00ff8cb09dea5743368087da735c7adb86fde0692c3a10594a5ccba7b98` |
| `DECISIONS.md` | `3731bdbf79fcc645539600bea9cf025a8ed750a561b4d4f0aed4a5a84a571cd1` |
| `guidelines/tibetan_translation_standard_v2.md` | `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f` |
| `glossary/expanded_tibetan_english_glossary.csv` | `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7` |
| `golden/reading.json` | `dc371e71f4eb0fa842963eebf3ebb0bb7c60e9623a038cf1cdcd3339855be2c1` |
| `golden/reading.md` | `75fc6f052921f547e30fabb19e4fb4cc2db232c67c5e04a3449855ea844f7c36` |
| `paired/source.md` | `1cd1a2c2f4528980314f5ce1a831f7a8d725615c699b2fb6e0e1caf4ed97fb31` |
| `paired/translation.md` | `0dda06f238a218a635eaed9576a596bcfe6bd84ddd4411104b0545734c002614` |

Initial checkout was clean on `policy/adopt-template-882454cb` at `c622e6a`; no unpublished commits or unstaged/untracked work were present. Its content equals the merged remote main. Local main was fast-forwarded without rewriting history, then `review/phase-d-20261005` was created at the frozen input. The existing archive/review branches and sole worktree were preserved. Remote main is unprotected and has no rulesets; the recent workflow uses a pull request. No GitHub Releases were returned by `gh release list`; the existing annotated tags/receipts are the relevant formal editions.

## Finite whole-work inventory and coverage

Every pair, including metadata, opening headings, all source annotations and closing material, is in scope. Pair counts are representation/coverage counts, never accuracy percentages. The eight current chapter inventories were parsed from authored files, not an old audit.

| Chapter | Expected pair range | Pairs | Golden objects | Notes | Input unresolved | Prior author / reviewer | Actually reviewed |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| 1 | `MTP-000001`–`MTP-000030` | 30 | 97 | 112 | 1 | `translation author /root/golden_triage` / `coordinating agent /root` | 000001–000030, all pairs and 112 active notes read; repairs applied and self-checked |
| 2 | `MTP-000031`–`MTP-000065` | 35 | 124 | 175 | 4 | `/root/ch02_translate` / `/root/ch02_qc` | 000031–000065, all pairs and 175 active notes read; repairs applied and self-checked |
| 3 | `MTP-000066`–`MTP-000099` | 34 | 120 | 165 | 2 | `/root/ch02_translate` / `/root/ch02_qc` | 000066–000099, all pairs and 165 active notes read; repairs applied and self-checked |
| 4 | `MTP-000100`–`MTP-000185` | 86 | 294 | 396 | 5 | `/root/ch04_author` / `/root/ch04_qc` | 000100–000185, all pairs and 396 active notes read; repairs applied and self-checked |
| 5 | `MTP-000186`–`MTP-000320` | 135 | 416 | 520 | 16 | `/root/ch05_translate` / `/root/ch05_qc` | 000186–000320, all pairs and 520 active notes read; repairs applied and self-checked |
| 6 | `MTP-000321`–`MTP-000452` | 132 | 376 | 435 | 21 | `/root/ch06_translate` / `/root/ch06_qc` | 000321–000452, all pairs and 435 active notes read; repairs applied and self-checked |
| 7 | `MTP-000453`–`MTP-000567` | 115 | 342 | 373 | 45 | `/root/ch07_translate` / `/root/ch07_qc` | 000453–000567, all pairs and 373 active notes read; repairs applied and self-checked |
| 8 | `MTP-000568`–`MTP-000674` | 107 | 284 | 421 | 46 | `/root/ch08_translate` / `/root/ch08_qc` | 000568–000674, all pairs and 421 active notes read; repairs applied and self-checked |

Total: **674 pairs; 2,053 source objects; 2,597 locally linked notes; 140 input unresolved pairs; 127 nontranslatable metadata pairs.** Pair-status files remain the occurrence-level unresolved inventory. Source roles: 530 main-text, 127 metadata, three headings, nine chapter-colophon, three source-annotation and two work-colophon pairs. The chapter-5 interrupted colophon and chapter-8 narrative, colophons, notices and triple blessing are included.

Existing records used: this report’s preserved historical section, `AGGREGATE-QC.md`, `AGGREGATE-CHECKS.json`, the eight chapter `QC.md`, `FINAL-REVIEW.md`, `qc.json`, `signoff.json`, `usage.json`, `glossary-proposals.json`, source audits and current note maps. Historical aggregate manual sampling is not counted as this review. The 30 golden transcript corrections and separate native-audit findings must be checked as current source history, not automatically reissued as English defects. No fixed-golden payload update was found; later paired-source commits assemble the chapter prefix. The historical author drafts remain archival inputs, not editorial targets.

Authored English is `translations/chapters/NN/translation.md`, assembled into `paired/translation.md` under the local pipeline schema. Chapter/whole-book readers and machine projections are generated. The original final gates intentionally bind fixed release bytes and old policy pins. Their rejection of current policy adoption is retained, not bypassed as release approval. A working-text rebuild must preserve that distinction.

## Initial findings recorded before correction

These findings are **recorded, not yet applied**. They will be extended only to occurrences confirmed by reading the current source.

| Finding | Location and exact Tibetan | Before English | Smallest supported after | Rationale / severity / confidence |
| --- | --- | --- | --- | --- |
| PD-001 | MTP-000006: `བཅོམ་ལྡན་འདས` | `Bhagavān` | `Blessed One` | Full P2 honorific row; retain the rest of the awareness/identity construction. Terminology, medium; high. |
| PD-002 | MTP-000015: `དཀྱིལ་འཁོར` | `maṇḍala` | `mandala` | P2 spelling policy only; does not settle thugs/citta or its locative relation. Terminology, low; high. |
| PD-003 | MTP-000026: `འདུལ་བ་དང / མདོ་སྡེ་དང / མངོན་པ་ལ་སོགས་པ་དང` (slashes show existing object boundaries) | `Vinaya, Sūtra, Abhidharma, and so forth;` | `discipline, discourse collection, higher doctrine, and so forth;` | P2 category rows govern this explicit collection list; keep source order and continuation. Terminology, medium; high. |

Chapter-1 no-change controls already checked: MTP-000007 says “taught,” not the later “heard” at 000015; 000008 retains negation and its documented unresolved temporal relation; 000012 technical Ground already has approved capitalization; 000024 is a sensory sound use, not a linguistic word use; 000029 `ཐབས་ཅིག` means the assembly’s “together,” not a new technical means occurrence; 000030 `གླེང་གཞི` is the whole setting expression, not standalone Ground. Title/colophon tantra, sensory sound, Ground, identity, realm, citta-retention and object notes need policy-status reconciliation without erasing their independent syntax uncertainties. The Tathāgata title, full vajra-chain overlap, and thugs/citta construction retain exact linked provisional treatment pending construction evidence.


## Source-order findings through chapter 3 (recorded before English edits)

Chapters 1–3: **99/674 pairs read**, including every metadata and colophon pair, and all **452 active note definitions**. Source-audit prose was checked against the current English and fixed Tibetan; this is not a claim of newly inspecting the facsimile images. Identical apparatus sentences may be read once and applied at their individually read source-linked occurrences. The full current glossary rows, including conditions and exclusions, govern the findings below. The manuscript-level and syntactic uncertainties in those notes remain explicit.

| Finding | Exact Tibetan / source-supported scope | Before → after English | Affected current pairs | Rationale; severity; confidence |
| --- | --- | --- | --- | --- |
| PD-001 extension | `བཅོམ་ལྡན་འདས`, shortened `བཅོམ་ལྡན` as honorific | `Bhagavān` → `Blessed One` | 000032, 000033, 000034, 000068, 000069 (also 000006 above) | Both P2 honorific rows apply. Preserve Vajrasattva/Vajradhara and every descriptive epithet. Medium; high. |
| PD-002 extension | `དཀྱིལ་འཁོར` | `maṇḍala` → `mandala` | 000044 (also 000015 above) | P2 retained technical spelling; no inference about the object/mandala construction. Low; high. |
| PD-004 | `སེམས་ཅན` | `sentient beings` → `karmic beings` (retain possessive ending where present) | 000033, 000035, 000083 | P2 owner-approved complete equivalent. Bare `སེམས`, ordinary being expressions and body references are not included. Medium; high. |
| PD-005 | `འཁོར་བ`, genitive `འཁོར་བའི`; nominal `མྱ་ངན་འདས` | `saṃsāra` → `cyclic existence`; `nirvāṇa` → `transcendence of sorrow` | Cyclic existence: 000033, 000037, 000041, 000043, 000064, 000080. Transcendence of sorrow: 000080. | P2 technical noun/contrast; preserve the negative naming claim in 000080 and the continuation of its condition at 000082. Medium; high. |
| PD-006 | 000037 `གཞི་ལ་སྙིང་པོ་མི་རྟོག་ཅན` | `an essence endowed with non-conceptuality` → `a core endowed with non-conceptuality` | 000037 | P2 `སྙིང་པོ` core, distinct from `ངོ་བོ` essence. Keep the existing bracketed copular supply and its unresolved attachment. Medium; high. |
| PD-007 | 000043 `དངོས་མེད` | `without substance` → `without entities` | 000043 | P2 negative-entity row expressly allows this grammatical realization; no uniquely material restriction is supported here. Medium; high. |
| PD-008 | 000043 `བེམ་རིག་གཉིས་མེད་འཁོར་བ་སངས`; 000062 `བེམས་པོའི་སྣང་བས་ང་མི་བསྒྲིབ` | `Insentience and awareness are nondual` → `Matter and awareness are nondual`; `insentient matter` → `matter` | 000043, 000062 | Full `བེམས་པོ` P2 row plus the locally supported abbreviated matter/awareness contrast already linked in T02-011. The abbreviation is a construction finding, not a new shared headword. Explain the material/non-knowing contrast in a linked note; never infer that karmic beings lack bodies. Medium; high for full form, medium for abbreviated construction. |
| PD-009 | `མཚན་མར་སྣང`, `མཚན་མར་འཛིན་པ`, `མཚན་མ་དངོས་དག` | `a characteristic` → `a mark`; `characteristics` → `marks`; `Characteristics` → `Marks` | 000061, 000062, 000088 respectively | P2 mark, distinct from characteristic. Preserve the supported singular/plural realization, apprehending action and provisional actuality qualification. Medium; high. |
| PD-010 | `ཨེ་མ་ཧོ` | `Emaho!` → `How wondrous!` | 000062, 000087, 000091 | P2 full wonder-exclamation, not an inserted listening instruction. Low; high. |
| PD-011 | 000068 `རང་རིག་ཡེ་ཤེས་ཆེན་པོའི་ལུང` | `authoritative teaching` → `transmission` | 000068 | P2 teaching/transmission sense of `ལུང`. No added named scripture; preserve the great modifier, possessive structure and following bestowal request. Medium; high. |
| PD-012 | 000091 `སྙིང་པོ་བཅུད་ཀྱི་གདམས་ངག་འདི` | `This instruction of the core’s vital extract` → `This oral instruction of the core’s quintessence` | 000091 | P2 `གདམས་ངག` oral instruction and `བཅུད` quintessence; preserve both the already-correct core label and the existing provisional genitive relation. No new whole-expression default. Medium; high for labels; the recorded syntax remains provisional. |

### Important no-change and open-construction controls, chapters 2–3

The current English already distinguishes the fixed Tibetan’s `བཅས` (000038, disclosed print-supported bracketed interpretation) from printed `བཅད`, and `བར` (000049, exact flagged wording) from printed `འབར`. Those are not silent source corrections to make during this pass. At 000053 the emptiness/primordial-knowing span remains a separate source annotation. The explicit source abbreviation at 000055–000056 is not a missing translation to reconstruct. The isolated `ཞ` at 000059 stays unresolved. At 000060 the unusual negative “not held by the apprehended object” follows `གཟུང་བས་མ་ཟིན`; do not normalize it to a subject. At 000065, “from the Ground” preserves `གཞི་ལས`, unlike earlier locative constructions.

At 000069 preserve “where he did not abide” and exact retained formula `སར་བ་འདུས་ཧ`; neither negation nor ritual encoding is silently repaired. At 000072, means is paired with discerning knowing, but the ablative/subject relation remains explicitly provisional. At 000073 retain like (`ལྟར`), unceasing/proliferating and doing/doer distinctions. At 000079, lower-case “ground” represents `ས`, not technical `གཞི`. At 000080 `རྡོ་རྗེ་འཛིན` stays the descriptive “holder of the vajra,” not the differently written proper name Vajradhara. At 000082–000086 preserve each condition, the different seeking/accomplishing verbs and cross-page consequent; do not supply names for “the five great [ones].”

At 000088 “varied ordinary mind itself” already preserves `སྣ་ཚོགས་སེམས་ཉིད` and the protected ordinary-mind component. Its whole-expression status is explicitly provisional, in line with §8.1, not a new default. At 000090, `ལུག་རྒྱུད` is the exact fixed contracted-looking form, already linked provisionally to vajra chains; no source respelling. At 000091, the corrected initial `སྙིང` is already in golden-v1 and is not a new finding; preserve the core repetition. At 000092 the grouping “three of certainty” is not silently regularized. Literary “tantras” there is only a source-linked provisional reading in T03-020; continuum remains the alternative, not settled merely by the P1 title/genre exception. The full chapter-title construction `འཁྲུལ་པ་ལ་བཟླ་བར་བསྟན་པ` at 000099 remains linked to pass-beyond / decisive-resolution alternatives; preference for a glossary label alone does not decide it. Keep the different long/short title modifier arrangements.

§8.1 family disposition still needs to be appended to current notes for `དོན་དམ` / `ཀུན་རྫོབ` (000043, 000077, 000092, 000096): owner-preferred **superfactual / superficial** are shared proposals, not silently activated defaults. Retain the clearly linked provisional ultimate/conventional treatment and exact construction uncertainties; distinguish `མཐར་ཐུག` at 000092 from `དོན་དམ`. Current P2 approval of selected labels must not be misrepresented as approval of other unlisted names, retinue/affliction labels or every term grouped in an old note.

**No English or note repair has yet been applied.** Continue at chapter 4, MTP-000100–000185, then chapters 5–8; whole-work bidirectional terminology consolidation, active-note/usage dispositions, working-reader regeneration and repair self-check remain.

## Source-order findings through chapter 4 (recorded before English edits)

Coverage is now **185/674 pairs and 848/2,597 active note definitions**, including every current source annotation and disclosed print/golden discrepancy through chapter 4. The note evidence was checked as existing source history, not presented as new facsimile inspection. Repeated source-apparatus prose was read through a losslessly folded view; exact Tibetan, note IDs, pair allocations and unique qualifications were preserved.

| Finding | Exact Tibetan and location | Before → supported after | Evidence / severity / confidence |
| --- | --- | --- | --- |
| PD-001 extension | `བཅོམ་ལྡན` / `བཅོམ་ལྡན་འདས`: 000102, 000103, 000110, 000172, 000175 | `Bhagavān` → `Blessed One` | Both approved honorific forms; preserve proper Vajradhara and the different descriptive “vajra hero” at 000103. Medium; high. |
| PD-004 extension | `སེམས་ཅན`: 000105, 000172 (twice), 000174, 000182 | `sentient beings` → `karmic beings` | Approved whole expression; this does not resolve retained `དུར / ཐེམ་ཞིང` at 000105 or deny material bodies at 000182. Medium; high. |
| PD-005 extension | `འཁོར་བ`: 000126, 000139 | `saṃsāra` → `cyclic existence` | Preserve turning-back and cessation predicates respectively; 000126’s `རུ་ནས` stays unresolved. Medium; high. |
| PD-007 extension | 000161: `དངོས་མེད་མཐའ་ཡས་སྟོང་པར་གྲོལ` | `insubstantial, limitless emptiness` → `limitless emptiness without entities` | P2 negative-entity construction; surrounding elemental sequence repeatedly uses `དངོས་པོ` as entity and does not establish an exclusively material sense. Preserve liberation **as**, not **from**. Medium; high. |
| PD-008 extension | 000174: `འབད་པས་གྲོལ་ན་བེམ་པོ་ནི / གྲོལ་བར་རིགས་པ་མ་ལགས་ན` | `and the inert / are not reasonably to be liberated` → `and matter / is not reasonably to be liberated` | Approved mass noun plus required verb agreement only. Preserve both conditions and the negative; explain material/non-knowing contrast in T04-126 without asserting immobility or a bodiless karmic being. Medium; high. |
| PD-010 extension | `ཨེ་མ་ཧོ`: 000111, 000122, 000126 | `Emaho!` → `How wondrous!` | Exact approved full exclamation. Do not silently treat every other interjection as this full form. Low; high. |
| PD-012 extension | 000155: `ཤེས་རིག་གསལ་བ་གདམས་ངག་ལ` | `is instruction` → `is oral instruction` | Approved complete label; retain knowing-awareness and the following application question. Medium; high. |
| PD-013 | 000115: `ཡིད་ཆེས་གསུམ` | `the three assurances` → `the three convictions` | Full P2 row expressly covers the numbered expression. Preserve instrumental relation and do not name the three members. Medium; high. |
| PD-014 | 000121: `གནད་དུ་བརྡེག`; 000155: `གོམས་པའི་གནད` | `vital point` → `key point` | P2 contemplative key point; keep striking action, genitive familiarization and whole phrases. Medium; high. |
| PD-015 | Technical `གཞི` at 000128 (twice), 000130, 000136, 000180, 000181; whole `གཞི་སྣང` at 000181 | `ground` → `Ground`; `ground-appearance` → `Ground-appearance` | Current contexts concern appearance/self-awareness/origin and explicit technical equations; T04-019/024/135 disclose the old lowercase convention, not an approved exception. P1 supersedes that convention, without deciding other syntax. Ordinary physical `ས` at 000142 and levels at 000139/180 are excluded. Presentation; low; high (lexical relation at 000136 remains provisional). |
| PD-016 | 000152: `འདའ་བར་འདོད་པ་དམ་ཚིག་ལ` | `samaya` → `sacred pledge` | Full P2 label; keep the counterintuitive desire-to-transgress assertion and the separate guarding/bondage statement. Medium; high. |
| PD-017 | 000161: `བསྐྱོད་ཅིང་དངས་སྙིགས་འབྱེད་པར་གྲོལ` | `the refined portion and dregs` → `the pure extract and residue` | Exact attested P2 pair, both components/order preserved; no Tibetan respelling and no change to the moving/separating action. Medium; high. |

### Chapter-4 no-change decisions and bounded construction questions

Keep the exact nominal and causal relationships disclosed in T04-003, 006–009 and 011–025. In particular, `ལྷུན་འབྱམས` at 000111 is not `ལྷུན་གྲུབ`; `དངས` at 000122 is a clearing verb, not a pure-extract noun; `ཉིད` is not silently substituted for fixed `གཉིད` at 000130. The 000135 `དྲི` corrections are already golden-v1 corrections, not new English findings. The 000168 prefix discrepancy is already disclosed in T04-123/C04-237; current “arising” follows fixed `བྱུང་བ`, not printed `འབྱུང་བ`. The extra printed `རྟག་ཆད` around 000145 remains separate layer uncertainty (C04-223), not words to insert into fixed-root English.

Read 000140–000144 continuously: the astonished figure faints; the next speaker intends to raise him. Keep the separate narrative and speech boundaries. At 000144/182, short `ཨེ་མ` is not an exact canonical headword. Test its local wonder function separately from full `ཨེ་མ་ཧོ` and vocatives before proposing an English realization; no automatic replacement yet. At 000145–000147, the apprehending subject continues across metadata and its predicate is retained. The wrong-view/authentic-desire attachment remains explicitly open, not corrected merely to a more conventional meaning.

At 000148, “gesture” is justified by the explicit bodily-limb movement (`ཡན་ལག་བསྐྱོད་པ་ཕྱག་རྒྱའོ`), satisfying the P2 contextual exception; do not replace it mechanically by seal. At 000153, “signs of the gesture” still needs a scoped reference decision against that nearby physical context; generic seal remains the canonical alternative. At 000149/165, audible loudness/music and melody support P1 sound. `ཚིག` in 000149’s mantra unit is a separate §8.1 formulated-unit question: test **phrase**, keeping auditory `སྒྲ` distinct, before deciding this local wording. At 000151, `དོན་སྙིང` is the anatomical organs/heart construction, not Meaning/core reconstructed from components. At 000152, `ཉམས་པ` deterioration is not experiential acquaintance or the canonical experience noun. At 000155, `གོམས་པ` familiarization is already distinct from cultivation. Bare `སྒྲུབ་པ` at 000153 is not the full `དངོས་གྲུབ` spiritual-accomplishment term.

At 000159–000170, preserve each of the twenty-five elemental descriptions, unexpected actions, explicit instruments and number. Do not change water’s burning/ripening into fire’s action, `གིས`/`ཡིས` into genitives to make a symmetrical matrix, “by entities” into “from entities,” or physical holding into apprehending-subject terminology. At 000163, `འཕེན་སྡུད་ཕྱེད` remains explicitly open between dividing and half; it is not silently respelled or equated with the different approved `སྤྲོ་བསྡུ` expression. At 000170, ordinary mind itself already preserves the §8.1 component; no generic mind substitute. At 000171, keep Glorious Supreme Horse’s different epithet rather than harmonizing it to Hayagrīva.

At 000172, `བཅུད` means **contents** in the explicit container-world/inhabitants opposition, not quintessence. The question continues through the page marker into 000174: question-connector `ལམ` is not a liberation-path noun. The subsequent negation of effort at 000176 is preserved, not back-projected to reverse the question’s premise. At 000177–000178 the means/discerning-knowing pairing supports **means**; do not invent biological substances or reduce separate `སྙོམས་འཇུག` absorption to canonical deep absorption. At 000180 keep seven groups of seven and ten months without inserting “weeks” or reconciling the numbers. At 000181 confidence (`གདིང`) is distinct from conviction. At 000182 do not insert the missing-looking negation in the first line to match later negative parallels. At 000185 keep the different colophon, including the absence of a “secret” modifier.

The §8.1 **meditative stability** proposal for `བསམ་གཏན` at 000135 remains linked to T04-023; its state grammar and distinction from deep absorption will be compared with the actual chapter-6 paired occurrence, not promoted to a book default now. Current terminology-note status changes must be narrower than their old bundled lists: approved labels do not approve every name, affliction, state, realm (`ཁམས` vs `ཞིང་ཁམས`) or technical compound in T04-002.

**Repairs remain unapplied.** Continue source order at chapter 5, MTP-000186–000320, followed by chapters 6–8. Working-text regeneration, note/usage reconciliation, bidirectional terminology consolidation and all repair self-checks remain pending.

## Source-order findings through chapter 5 (recorded before English edits)

Coverage: **320/674 pairs and 1,368/2,597 active note definitions** read in source order, including the interrupted chapter-five colophon at 000318–000320. No English repairs have yet been applied. The following occurrence extensions were confirmed by the full current pairs and notes, not by English substring matching.

| Finding | Exact Tibetan / scope | Before → supported after | New chapter-five locations | Rationale / severity / confidence |
| --- | --- | --- | --- | --- |
| PD-001 | `བཅོམ་ལྡན་འདས` | Bhagavān → Blessed One | 000188 | P2 honorific; preserve the invocation and its question. Medium; high. |
| PD-004 | `སེམས་ཅན` | sentient beings → karmic beings | 000188, 000220, 000278, 000301; active fragment gloss C05-388 linked to 000314 | P2 complete expression. The fragment remains commentary, not added root text. Medium; high. |
| PD-005 | `འཁོར་བ` / `མྱ་ངན་འདས`, compressed `འཁོར་འདས` and the separately unresolved `འཁོར་བ་འདས་འདུ་འབྲལ` | saṃsāra → cyclic existence; nirvāṇa → transcendence of sorrow | Both members: 000203, 000252, 000259, 000271, 000277; cyclic existence only: 000307. Fragment C05-162 linked to 000241 also requires current-policy disposition. | P2 domain contrast, preserving both components/order. Retain opaque `ལང` in 000252 and the joining/separating uncertainty in 000271; label approval does not settle them. Medium; high for labels. |
| PD-008 | 000264 `བེམ་རིག་གཉིས་མེད་ཚོགས་གཉིས་རྫོགས` | inert matter → matter | 000264 | Same locally attested abbreviated matter/awareness contrast as 000043, disclosed in T05-030; do not add immobility or bodiless beings. Medium; medium for abbreviated construction. |
| PD-012 | 000261 `རང་ཤེས་ཡིན་ཕྱིར་གདམས་ངག་རྫོགས` | instructions → oral instructions | 000261 | P2 complete oral-instruction label; preserve causal relation and self-knowing, which is distinct from self-awareness. Medium; high. |
| PD-016 | 000200 `དབང་དང་དམ་ཚིག་ག་ལ་ཡོད` | commitments → sacred pledges | 000200 | P2 label, preserving the rhetorical question and the other member, empowerment. Medium; high. |
| PD-018 | 000247 `སྤྲོ་བསྡུ་མེད་པས་ཁྱུང་ཆེན་འདྲ` | no elaboration or withdrawal → no projection or gathering | 000247 | Exact P2 pair; nominal realization under negation. Preserve both members, negative coordination and the garuḍa simile. Do not extend this to bare `སྤྲོ་བ` at 000202 or the different `འཕེན་སྡུད` construction in chapter 4. Medium; high. |

### Chapter-five no-change decisions and construction/family review

The current text already preserves **ordinary mind itself** at 000244/000253 and elsewhere; **words / phrases** for `སྒྲ / ཚིག` at 000234; technical **Ground** and **Ground-appearance**; **core** versus **essence**; and **luster** for `མདངས` at 000302, distinct from `གདངས` radiance. These are not defects merely because older notes called them provisional. P1/P2 dispositions must be appended narrowly to those notes, without approving every member of their bundled terminology lists. C05-258’s limited `གཞི` gloss needs current capitalized Ground status, but remains a source-annotation fragment.

Read all causal, comparative and enumerative sequences continuously across the page-control pairs. Preserve the missing complement at 000190; all occurrences of “from that,” “through itself,” and deliberate reversal or negation; the distinction between `རང་ཤར` and `རང་བྱུང`; and the different descriptive holder-of-the-vajra (`རྡོ་རྗེ་འཛིན`) and proper Vajradhara (`རྡོ་རྗེ་འཆང`). The first-person teaching at 000203 is not an impersonalized metaphysical assertion. The source’s giving/life-taking and same-kind similes at 000204/000251–000256 are represented as statements of the text, not rewritten to avoid their paradoxes.

**Rejected substring false positives:** 000215 “insubstantiality” represents `ཡ་མ་བརླ`, not P2 `དངོས་མེད`; 000241/000263 “material encumbrance” represents `རྡོས་བཅས`, not `བེམས་པོ`; 000247 `ས་གཞི` is earth in a physical simile, not technical Ground; 000259 `རང་ས` is own place; 000308 `རྒྱུད་ཆགས` is a whole continuity/succession construction, not a standalone continuum error; 000276/000308 turning/circling is not automatically technical cyclic existence. The bodily beings (`ལུས་ཅན`) at 000298 and creatures (`སྐྱེད་གུ`) at 000302 must not be replaced by karmic beings. Anatomical `དོན་སྙིང` at 000307 is not reconstructed from Meaning/core entries.

**Contextual P1/P2 exceptions:** sound at 000214/000283 is auditory/sensory, not linguistic word. The tantra genre at 000197 is supported by the textual discourse/pith-instruction context, whereas continuum at 000243 is the deliberate naming explanation from primordial abiding. `བཅུད` is contents in the container-world opposition at 000311 and inhabitants at 000314; C05-388’s separate `སེམས་ཅན` fragment reinforces the inhabitants context but must not be inserted into the fixed root as a different noun. The “quintessence” default would erase that contrast. `ཐབས` beside discerning knowing at 000281 is means, not an arbitrary methods synonym. Bare physical faculties/organs, `ཁམས` elements versus realms, and `ཡུལ` object versus domain remain subject to their actual constructions, not to words found within longer canonical expressions.

**Bounded questions retained:** the exact `དུམ་གྲགས་པས` at 000227, `བཅུང` at 000239, `ལང` at 000252, `འོད་རེགས` at 000269, `སྤྱིས་གཞི` at 000285, praise/mantra-like `སྔགས` at 000286, and the six mental faculties at 000287 remain locally linked and unresolved; no source respelling. At 000282, the scope of the final negative in `གཟུང་བར་བྱ་ཞིང་འཛིན་པ་མེད` is already explicitly provisional (T05-034); do not pretend that the alternative affirmative gerundive first clause is settled. The eleven/twelve hundred-thousand/million cosmological numbers at 000290–000291, eighty-thousand lifetime at 000302, four births and all fivefold lists remain exactly numbered without inserting unstated units or named taxonomies. The unusual absence-of-consciousness statement at 000297 is not normalized to a familiar formless-attainment scheme. The rope’s `སྤྲུལ` apparition at 000309–000312 is not silently changed to `སྦྲུལ`, snake.

**Current source history, not fresh defects:** C05-094 already marks uncertain smaller extra particles in the print’s expanded mental-factor line at 000217. C05-397 already marks the print’s extra `ལ` at 000313 as uncertain source layer. C05-298 already allocates the marginal addition adjacent to 000268. Existing small-note omissions, including the eight-consciousness and year-unit fragments, remain apparatus rather than root additions. Golden corrections already adopted are not reissued as current errors. The 000318–000320 colophon is one continued formula across a page marker, not an accidental fragment to resegment.

**Further family/construction tests required:** compare `གཏི་མུག` bewilderment in the five-affliction list at 000212 with the later chapter-six mental taxonomy; compare `མདངས` luster at 000302 with chapter-six praise; compare the local lymph/serum proposals for `ཆུ་སེར` across physiology contexts without inventing medical precision. Test phrase for `ཐ་སྙད་ཚིག` (000252) and `བཅོས་པའི་ཚིག` (000266) against the already-distinct words/phrases at 000234 and the later chapter-seven usage. For `དོན་དམ / ཀུན་རྫོབ` at 000311/000313 and source fragments C05-380/384, retain linked provisional ultimate/conventional pending the paired **superfactual / superficial** construction test; this is not an approved local default. The compact `གྲུབ་མཐའ` at 000238/000271 now has the P2 tenet-system row, but the expanded `གྲུབ་པའི་མཐའ` at 000268 requires its own construction/wordplay decision (T05-L040), not an assumed substring replacement. The “scriptural transmission(s)” realizations of `ལུང` at 000197/000243/000259 require separate citation-versus-naming-context checks against the full P2 row before altering their modifiers.

Continue at **MTP-000321**, chapter 6, then chapters 7–8. Whole-work bidirectional terminology consolidation, repairs, note/usage reconciliation, working-reader regeneration and self-verification remain. Coverage remains partial; readiness is not claimed.

## Source-order findings through chapter 6 (recorded before English edits)

Coverage: **452/674 pairs and 1,803/2,597 active note definitions** read. Chapter 6 includes its dialogue, first-person declarations, imprisonment imagery, repeated sorrow-transcendence predicates, channel/lamp exposition, syllable explanations and colophon. The existing source-audit qualifications were read, not newly certified by facsimile inspection. **Repairs remain unapplied.**

| Finding | Exact Tibetan / current scope | Before → supported after | Chapter-six locations | Evidence / severity / confidence |
| --- | --- | --- | --- | --- |
| PD-001 extension | `བཅོམ་ལྡན་འདས` / short `བཅོམ་ལྡན` as honorific | Bhagavān → Blessed One | 000322, 000324, 000325, 000354, 000357, 000397, 000398, 000399 | Both approved P2 forms. Other names, number and speaker relations remain unchanged. Medium; high. |
| PD-003 extension | 000338 `མདོ་སྡེ་འདུལ་བ་མངོན་པ་ང` | sūtra discourses → discourse collection | 000338 | P2 collection row; discipline and higher doctrine already conform. Preserve this chapter’s different collection order and its first-person predicate. Medium; high. |
| PD-004 extension | `སེམས་ཅན` | sentient beings → karmic beings, retaining possessives | 000324, 000355, 000358, 000361, 000362, 000378, 000398, 000452 | Approved P2 whole expression. In particular, keep the explicit instrumental **by** karmic beings and missing-subject marker at 000355; do not reverse it into “what binds beings?” Medium; high. |
| PD-005 extension | `འཁོར་བ`, compressed `འཁོར་འདས`, and `མྱང་འདས` | saṃsāra → cyclic existence; nirvāṇa → transcendence of sorrow | Both members: 000334, 000350, 000351 (twice), 000355. Cyclic existence only: 000366, 000367, 000378, 000380, 000384, 000419, 000433, 000434. | P2 nouns and domain contrasts; preserve repeated members, case and negation. 000419 rescues cyclic existence as its object; do not insert beings or “from.” Medium; high. |
| PD-008 extension | 000347 `ང་ནི་བེམ་རིག་གཉིས་མེད་ཀུན་ལ་ཁྱབ་པ་ཡིན` | For me, insentient and aware are not two → For me, matter and awareness are not two | 000347 | Same attested abbreviated matter/awareness contrast as 000043/000264, supported by T06-013; keep the existing predication and its disclosed nonduality-versus-absence question. P2 matter does not imply immobility or bodiless karmic beings. Medium; medium for abbreviated construction. |
| PD-010 extension | `ཨེ་མ་ཧོ` | Emaho! → How wondrous! | 000395 | Approved full exclamation; not an added instruction to listen. Low; high. |
| PD-016 extension | 000337 `དབང་དང་དམ་ཚིག་སྡོམ་པ་ང` | commitments → sacred pledges | 000337 | P2 now supersedes the historically provisional chapter-five/chapter-six preference; empowerment and vows remain separate. Medium; high. |
| PD-017 extension | 000432 `ཆུ་ནི་དངས་སྙིགས་འབྱེད་པར་བྱེད` and `མདོར་ན་དབང་པོའི་དངས་མ་ཡིན` | the clear from the sediment → the pure extract from the residue; refined essence → pure extract | 000432 | Full P2 pair and separate pure-extract row. Preserve water’s distinguishing action, source order, faculties’ genitive and the unknown identity of “the two” in the intervening line. Medium; high. |
| PD-018 extension | 000414 `སྤྲོ་བསྡུ་སྨྲ་བསམ་ཡུལ་ལས་འདས` | proliferating and gathering → projecting and gathering | 000414 | Exact P2 action pair, distinct from established `འཕྲོ་འདུ`. Keep the separate speaking/thinking pair and beyond-the-objects relation. Medium; high. |

### Chapter-six no-change controls and bounded open constructions

Preserve the source’s different names: descriptive holder of the vajra, Vajradhara, Lord of Secret Mantra, Lord of Secrets and those possessing vajras. At 000397–000398 the plural petitioners use singular “me”; do not regularize number. Lowercase ground at 000347/000350/000398 represents `ས`, not technical `གཞི`. At 000326–000327 keep the instrumental differentiation by essence, the unresolved antecedent of “that,” and the explicitly five unnamed embodiments. At 000328–000331 preserve continuation across metadata, union without adding named participants, and simultaneous/gradual predication without substituting named practitioner types. At 000337 retain the repeated gathering forms. At 000339 do not name the two truths that the source leaves unnamed. At 000340/000353 retain receptacle/contents under the P2 container/inhabitants exception, and distinguish going/non-going from absent “beings.”

The linguistic words at 000342 (names/letters context) and sensory sound at 000343/000390 are justified P1 distinctions. Bewilderment at 000343 is `རྨོངས་པ`; deluded dullness at 000367/000438 is `གཏི་མུག`, distinct from canonical dullness and ignorance. This supplies evidence for the whole-work family test with chapter-five 000212, not authority to silently approve a new shared entry. Meditative stability at 000338 and 000451 is nominal/state-oriented and remains explicitly distinct from deep absorption; compare the earlier meditative-concentration treatment at 000135 under §8.1. Contrived utterance at 000344 and utterances at 000440 require the same formulated-unit **phrase** test as chapters 4–5, not automatic replacement of every English “word.”

At 000344 the current notes already disclose fixed `ཕགས` versus printed `འཕགས` and fixed `ཉིས་མེད` versus printed `གཉིས་མེད`; the latter does not settle exclusion-of-both versus nonduality. At 000347 keep **I depend on all**, not the reverse. At 000348 retain exact `རྒྱ་ཐེག`, `ཧུབ་ཀྱིས་སྟོབ` and `ལྒོབ` uncertainty instead of reconstructing expected marvels. At 000350 keep majesty (`གཟི་བརྗིད`) distinct from splendor (`བརྗིད`); an English substring does not prove a luster/radiance error. At 000353 retain exact `ཡེ་ང`, and distinguish fear-related apprehension from the technical apprehending-subject family. At 000355 retain the fixed instrumental `གིས` and absent interrogative; at 000356 retain exact unresolved `སུངས`. The possession/juxtaposition at 000358 and negative conditional argument through 000364 remain locally qualified. Becoming clear at 000363 is a verb, not the nominal pure-extract entry.

Read the imprisonment sequence continuously through metadata and retain its actual agents, instruments, body parts and imagery. The affliction phrase `ལན་ཚའི་རོལ` at 000367, verb `འབོགས` at 000373 and animal comparison `ལན་བུན` at 000374 stay exact and unresolved. Mindfulness itself at 000369 surprisingly binds; do not substitute an expected guard. At 000371 the current source audit already notes that the print shows one repeated-looking construction where the fixed text has two `ལས་ཀྱིས་མ་བུ` phrases: preserve both fixed lines and the linked layer uncertainty. At 000375 both `ཁམས` and explicitly five `འབྱུང་བ` legitimately appear as elements in different catalogue roles; do not insert the annotation’s five/eighteen/twelve into the root or collapse the lists. At 000378 the cause/referent of lacking intrinsic nature remains provisional. The means/discerning-knowing pair at 000379 is supported; its repaired golden `ཤེས་རབ` is not a fresh finding.

At 000383–000385 preserve binding by compassionate responsiveness, binding in cyclic existence by conceptual thought, and the positive genitive self-awareness **of attachment**; doctrinal discomfort does not justify invented negation or liberation. Experiential acquaintance retains its complete protected term. At 000386 retain emptiness-then-clarity source order, the provisional excellence/continuous-deep-absorption relation and the actual escape-from predicate. At **000389–000394**, the repeated **have/has passed beyond sorrow** is a supported P2 **verbal** realization: preserve its subjects and repetition instead of replacing it by a noun. Entities/nonentities there and at 000448 already fit the approved paired-negative context. The three-thousandfold [world] is not converted into an asserted arithmetic cosmology. At 000396 preserve all three leaving/resting expressions, not only the first canonical-family phrase.

At 000403, mandala of awakened mind is supported by the respectful cognitive context of buddhas and the P2 `ཐུགས` row; this does not decide the different chapter-one citta/heart construction. At 000404 the explicit vajra plus the canonical vajra-chain phrase remains exactly linked as an unresolved overlap, not silently collapsed or retranslated component by component. At 000406–000408 the apparent fragment continues through the page marker. At 000411 retain the unresolved layer/segmentation of `གཡས་པ་རོ་མ`, and the already-corrected single `ཆ` without adding `ཅན`. The conventional/ultimate family here (000380, 000411–000412, 000415) ranges from doctrinal predication to channel/sphere descriptions; owner-preferred superficial/superfactual must be tested in those whole constructions rather than activated as a local default. At 000414 preserve the affirmative assertion that both extremes are completely clear. At 000415 preserve entity, not an invented nonentity. At 000416 keep the negative and unknown participants of the bliss/union construction; do not add anatomy.

The explicit counts at 000420 are not harmonized with the differently formulated lamp list at 000421. Its shortened pure-basic-space description lacks the canonical perfectly-pure modifier, and its naturally arising discerning-knowing member lacks an overt lamp noun; do not add either. At 000422 peacock luster (`མདངས`) remains distinct from primordial radiance (`ཡེ་གདངས`) at 000419. Preserve the deliberate **Thig / le** division at 000423–000425 and **Rab / Rang / Byung ba** component explanations at 000428; these are not accidental fragments or new whole-expression defaults. At 000430 fixed `རྒྱུད`, already corrected in golden-v1, is continuum, not the expected-looking `རྒྱང` of the lamp name. Keep the unresolved continuum/stallion/mental-consciousness join and the subject/object attachment at 000431. At 000432 the identity of “the two” is not supplied from an unincorporated small annotation. At 000433 **gold chain** is justified by the expressly physical craftsman simile, while the later technical **vajra chains** in the same stanza remains protected; knowing and being aware stay separate verbs. At 000434 retain exact unresolved `རྣལ་བ`; the following four births and six classes are not normalized into a single count. At 000439 preserve the ordinary-mind component despite awkward genitive syntax. At 000444 the bare middling group is not given an absent faculty noun; at 000445 retain every distributive “each.” At 000446 do not insert named visions. The result referents at 000447–000448 remain explicitly open, while defining characteristic at 000449 is supported by the actual definition. The chapter-six colophon stays separate from the next dialogue.

Continue at **MTP-000453**, chapter 7, then chapter 8. Whole-work terminology consolidation, note/usage reconciliation, corrections, dependent-reader generation and repair self-checks remain. Coverage remains partial; text readiness is not claimed.

## Complete source-order pass and final pre-edit disposition

**All 674/674 pairs, eight chapters, and 2,597/2,597 active note definitions have now been read. There are no unreviewed pair ranges.** This includes all opening material, 127 metadata pairs, the interrupted chapter-five colophon, chapter-eight narrative, work colophon, both final source notices and all three blessing statements. Tibetan-to-English coverage and English-to-Tibetan support were checked under Q1–Q9, with particular attention to the continuations, speakers, agents, cases, negation, conditions, number, modifiers and rhetorical function documented below and in the source-order checkpoints. Apparatus text and previous source audits were read; no claim is made of a new facsimile-image inspection.

The remaining chapters extend the same approved policy only where the actual source supports it. Chapter 7 retains its bodily correspondences, literal flower/fruit similes, separate collection order, school-name variations, speaker changes and source-form uncertainties. Chapter 8 preserves the Ground/core/quintessence and extract distinctions, different kinds of continuum, actual numerical lists, interrupted constructions, unnamed referents, source notices and final repetitions. Their lexical repairs and exact Tibetan/before/after evidence are included in the authoritative occurrence ledger below, not inferred from the old template examples.

### Whole-work construction decisions and important no-change cases

The bidirectional comparison covered the full 283-row/eight-column glossary, its longer expressions, both attested matter spellings, compact and inflected expressions, names/honorifics and the §8.1 families. The complete paired reading preceded concordance searches. Current usage records were inspected structurally and compared by Tibetan key, English realization and source context: **1,601 records / 3,096 source-unit allocations**. Seven initial literal-source mismatches are explicitly marked **print-only insertion; layer unresolved** in chapter 1, not defective root quotations; all other allocations match their linked fixed source spans. Those seven remain in the source-commentary layer. Exact headword searches are evidence only: the case form `གྲུབ་མཐས` at 000271 required a separate grammatical check and is not absent merely because a literal headword search missed it.

The repairs preserve **Blessed One** versus proper **Vajradhara** versus descriptive **holder of the vajra**, and retain other distinct epithets. “Thus-Gone One” and “Thus-Come One” are source-linked English proposals for Tathāgata, not newly approved equivalents. The latter remains visibly provisional at 000019, 000599 and 000668 pending shared honorific reconciliation. The sharp-vajra epithet at 000668 is already present in current English, so an old omission criticism is rejected.

**Matter / karmic being:** all seven actual matter/abbreviated-matter body occurrences are covered, not only the old examples. The source can simultaneously say that karmic beings have bodies and contrast non-knowing matter with awareness. At 000540 matter is the grammatical agent that cannot generate; no missing object or extra being is invented. At 000550 the cognitive verbs support **awakened mind** for standalone `ཐུགས`, while the causal relation remains provisional. The different citta/heart/location construction at 000664 stays exactly unresolved; the new canonical row explicitly does not settle it. The source’s freedom-from-stirring statement is not turned into the definition of matter.

**Mental and state families:** 000212’s five-affliction list matches 000438 and the noose at 000367, supporting local **deluded dullness**, distinct from 000343’s **bewilderment** (`རྨོངས་པ`), ignorance, delusion and established dullness. This includes the print-only affliction-list annotation linked to 000021, without inserting it into the root. **Meditative stability** is supported by the actual state/list constructions at 000135, 000261, 000338, 000451, 000475 and 000482; 000338 expressly distinguishes it from **deep absorption**. These are documented local provisional interpretations, not newly approved shared assignments or an invented meditation hierarchy. All ordinary-mind-itself expressions retain the protected ordinary-mind component. Technical means/discerning-knowing pairings preserve their source order; `ཐབས་ཅིག` together remains excluded.

**Verbal units:** the explicit words/phrases distinction at 000234 and already conforming contrived phrases at 000266 support **phrase** in the twelve repaired mantra/formulation/meaning-versus-phrase constructions, including 000539 and 000625–000630. Generic “put into words” and “in these words” at 000656–000657 remain grammatical speech formulae, not a new competing technical label. Sacred pledge, oral instruction, letter, name, linguistic word and sensory sound remain distinct. Sound at 000505 is retained as a linked contextual question because its varied-appearance and cognitive-object setting does not by itself resolve sound versus linguistic word. The approved sound exception does not decide the separate phrase family.

**Context, not mechanical matching:** keep gesture at 000148/000153 in the bodily enactment sequence; use gestures for explicit limb-turning at 000500 but seals in the generic ritual list at 000480. Keep the separate whole Mahamudra expression. Keep **contents/inhabitants** in the container-world contrasts, not quintessence; keep botanical **fruit** in the actual plant similes, not result. Preserve the split center/surrounding-circle word explanation at 000495 and bare center at 000664 rather than inserting mandala. Preserve actuality at 000062 and material presence in the explicit body/element construction at 000464; the negative-entity contexts at 000577/000578/000581 have no equivalent material restriction. Their separate exact `དངོས་ཏེ` spans, and `དངོས་མ` at 000566, remain unresolved and are not respelled into approved headwords.

P1 **Ground** capitalization applies to the confirmed technical uses in chapter 4. Current compounds such as Ground for expression (000522), Ground of habitual tendencies (000547), Ground of mindfulness (000554) and the heart/Ground relation (000654) retain their linked provisional technical-versus-support interpretation; the row does not make every `གཞི` technical. Physical ground/levels and `ས་གཞི`, all-basis, own place, chapter-setting and source metadata are not altered by a substring match. **Continuum / tantra** remains contextual: titles and explicit textual-genre uses receive the approved tantra exception, while naming/continuity explanations keep continuum. The literary reading at 000259 remains source-linked and provisional rather than silently treated as settled from the neighboring transmission noun. `རྒྱུད་ཆགས` succession, `བརྒྱུད་པ` transmission at 000262, and `རྒྱུན` continuity are different expressions. **Scriptural transmission** is retained in the explicit citation/reasoning/text context at 000197; its unsupported modifier is removed in the state/naming contexts at 000243/000259.

The owner-preferred **superficial / superfactual** pair was tested together across the actual doctrinal, worldly-convention, two-truth, form and sphere/channel uses. Noun/adjective fit alone does not settle the sphere/element/physical-surface implications or open entity/form relations at 000411–000415 and 000311–000313. The existing linked provisional conventional/ultimate treatments remain, with the proposed pair and the required shared scope decision recorded; distinct `མཐར་ཐུག` is excluded. Luminous **luster** is justified narrowly at 000302/000422 and remains a shared proposal, not a spelling change into radiance. Serum/lymph remain an unresolved bodily-fluid family at 000151/000216; the text does not establish modern medical precision.

At 000238/000271, the compact/case-inflected tenet-system noun receives P2. The expanded `གྲུབ་པའི་མཐའ` at 000268 remains a separate establishment/limits/tenets construction and possible wordplay. The chapter-three `ལ་བཟླ` title remains linked to the decisive-resolution versus passing-beyond alternatives: the full row explicitly forbids deciding that title by label preference. Ordinary grasping in compounds/verbs is not mechanically replaced by a nominal apprehending subject; the current locally qualified I-grasping and object-appearance constructions remain separate from the explicit apprehended-object/apprehending-subject pair.

### Closing-material controls and bounded unresolved work

Chapter 7 preserves the expressly written `བྱང་ཆུབ་སེམས` without adding an absent dpa’, the different school-name spellings, the affirmative with-outflows line at 000533, the corpse/space question at 000541, the exact retained `སྔགས་པས`, `དུམ་གཟུགས་ནང་ལུས` and `བག་རྡུལ` spans, and the unspecified mother in 000565. That pair’s “five domains—objects of focus” is retained with its linked construction question: the canonical `དམིགས་པ` row does not alone determine the relation to its additional `ཡུལ` noun. Appearance, object, domain and faculty are not freely interchanged.

Chapter 8 preserves the repeated all-to-all relation, the collective/member repetition in the three cores, the three clarities versus knowing, the first path wording already corrected in golden-v1, and the different sixteen/eighteen-style enumerations without retrofitting an external catalogue. The eighteen listed title-items and the later root/mother-child/limb/transmission-awareness/pith-instruction classifications retain their exact names, source order and unresolved `གསལ་ཤིང`, `རྒྱལ་པོས`, `ཡེ་ཤེས་གསུམ་ཟློག`, `བ་གམ` and ritual spans; no known-work identification is invented. Actual retained spellings and numerical groupings, including sixty-four groups of one hundred thousand, are not emended to a familiar catalogue. Narrative speaker, plural petitioners/singular me, the sixth Vajradhara ordinal, praising versus rejoicing, the final commentary notices and triple blessing remain separate. The two notices are source annotations, not translated root claims or translator commentary.

**Input hard-unresolved pair statuses: 140; planned final hard-unresolved statuses: 140.** Resolving the thugs label at 000550 does not settle its causal construction, so that pair remains unresolved with a more precise reason. Other provisional constructions are not concealed merely because their pair’s status is translated. Exact remaining spans, alternatives and required evidence remain attached through existing notes and pair-status IDs. No whole-work coverage is withheld because one expression is open, and no uncertainty is invented away to claim readiness.

### Candidate reconciliation before editing

The exact occurrence ledger below supersedes earlier checkpoint candidate locations where the current English already conforms. In particular, **000261 already reads oral instructions** and is a no-change case; not every honorific locus mentioned in the early checkpoints contains Bhagavān in the current body. Actual additional matches include Bhagavān at **000356** and the full Emaho at **000262**. Candidate counts are not change counts. All final before/after strings below were extracted and asserted against the frozen current authored English and actual fixed Tibetan before any repair.

### Current note and usage dispositions (PD-028)

Before editing, the planned reconciliation is **268 existing note definitions, 318 existing usage records, and 197 existing local proposal records**. No note IDs or source allocations are added or removed. Original note prose and proposal/approval history remain verbatim; a dated **Phase D current disposition** is appended, and structured `review_disposition` fields identify the current policy and source-specific limits. Existing canonical labels now approved by P1/P2 are not left falsely unapproved. Unlisted names/compounds and open syntactic relations bundled in the same old note are not approved wholesale. The three explicitly updated source-fragment glosses remain in the annotation layer. The eight-column bodies of old proposals and the shared CSV remain unchanged; new shared questions stay grouped in this review rather than a parallel ledger.

The complete active eight-column row is carried in the applicable usage/proposal disposition, not reconstructed from a short English label. Repeated note updates share the preceding rationale. Their exact additions are visible in the authored chapter diff; the location inventory below identifies every affected existing note. Severity: medium for misleading active status or fragment gloss, low for presentation-only status. Confidence: high for adopted assignment/status; explicitly provisional for the §8.1 constructions and listed contextual questions. No original author’s approval is rewritten as approval of these repairs.

### Shared reconciliation queue (not activated glossary entries)

These are local recommendations/open questions for later comparison across the four works, not a claim to have reviewed the other repositories. The primary shared assignment for each remains **Proposed** until explicit owner approval. The owner-preferred superficial/superfactual pair is considered together, not independently replaced word by word.

| Tibetan | English proposal / current local treatment | Meaning and scope | Grammatical forms | Contextual exceptions / open question | Related entries | Evidence / sources | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `གཏི་མུག་` | deluded dullness | The recorded five-affliction/noose uses | Mass noun in the reviewed lists | Not a graded taxonomy or every dull state | bewilderment; ignorance; delusion; dullness | 000212/000367/000438 and print-only list at 000021; §8.1 U05 | Proposed; local provisional treatment |
| `བསམ་གཏན་` | meditative stability | Nominal/state use in this work | Abiding in; list/state noun | Do not merge deep absorption or imply a hierarchy | `ཏིང་ངེ་འཛིན་` | Six current occurrences; especially 000135/000338; §8.1 U06 | Proposed; local provisional treatment |
| `ཚིག་` | phrase | Formulated verbal unit | phrase; phrases | Generic speech formula may use words without assigning a rival technical label | word; name; letter; sacred pledge (excluded compound) | 000234/000266 controls and PD-025 loci; §8.1 U12 | Proposed; scoped local treatment |
| `མདངས་` | luster | Luminous/visible sheen | luster | Broader splendor needs shared scope; never respell as `གདངས` | radiance; brilliance; splendor | 000302/000422; §8.1 U13 | Proposed; retain narrower rationale |
| `ཀུན་རྫོབ་` | superficial proposed; conventional/convention retained provisionally | Paired doctrinal/worldly/sphere uses | Noun/adjective treatment unresolved | Do not assert surface anatomy from the English proposal | `དོན་དམ་` | 000043/000077/000313/000411 and linked fragments; §8.1 U10 | Proposed; paired scope decision required |
| `དོན་དམ་` | superfactual proposed; ultimate retained provisionally | Paired doctrinal/form/sphere uses | Noun/adjective treatment unresolved | Not `མཐར་ཐུག`; preserve open form/entity relations | `ཀུན་རྫོབ་` | 000043/000077/000092/000096/000311/000380/000411–000415; §8.1 U10 | Proposed; paired scope decision required |
| `དེ་བཞིན་གཤེགས་པ་` | Thus-Gone One; Thus-Come One alternative | English honorific proposal | Singular/plural as source requires | Directional lexical choice not decided by retinue/title syntax | Blessed One (distinct); proper names | 000019/000599/000668; §8.1 U01/U03 | Proposed; Tathāgata visibly provisional |
| `ཆུ་སེར་` | serum / lymph remain alternatives | Recorded bodily-fluid contexts only | Mass noun | Historical sense evidence needed; avoid invented medical precision | blood; flesh; organs | 000151/000216 and their linked notes | Unresolved shared-label question |

The abbreviated matter/awareness contrast, the thugs/citta construction, the title’s la-bzla verb and support-versus-technical Ground compounds are **construction/documentation questions**, not automatically new shared headwords. Joy-Maker comparisons in other books are outside this repository’s review; no four-work identity or harmony is asserted.

### Exact planned correction ledger (recorded before applying repairs)

Each entry below is one actually changed pair. Tibetan is copied exactly from its source pair; `<br>` represents an existing line break, not resegmentation. The displayed English before/after omits footnote markers only for readability; those markers and all note allocations remain in the authored files. Per-finding severity/confidence and short substitution evidence follow each pair. Unchanged surrounding clauses are included so that scope, agents, negation, number and connectors can be rechecked. This ledger records the proposed repair; subsequent self-check/build results are reported separately and are not a second independent review.

#### MTP-000006 — chapter 1

Location: [`chapters/01/translation.md`](chapters/01/translation.md); fixed source: [`chapters/01/source.md`](chapters/01/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཅོམ་ལྡན་འདས་རིག་པའི་བདག་ཉིད་འཁྲུལ་པ་མི་མངའ་བ་ཉིད་ལ་ཕྱག་འཚལ་ལོ |
| Before | I bow to the Bhagavān, whose very identity is awareness, who has no delusion. |
| After | I bow to the Blessed One, whose very identity is awareness, who has no delusion. |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000015 — chapter 1

Location: [`chapters/01/translation.md`](chapters/01/translation.md); fixed source: [`chapters/01/source.md`](chapters/01/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འདི་སྐད་བདག་གིས་ཐོས་པའི་དུས་གཅིག་ན<br>ཆ་ཡིས་མ་བགོས་པའི་གཞལ་ཡས་ཁང་དམ་པ<br>ཐུགས་ཙིཏྟའི་དཀྱིལ་འཁོར་ན |
| Before | “Thus did I hear at one time. In the sublime palace undivided into parts, in the maṇḍala of the heart (citta), |
| After | “Thus did I hear at one time. In the sublime palace undivided into parts, in the mandala of the heart (citta), |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.

#### MTP-000026 — chapter 1

Location: [`chapters/01/translation.md`](chapters/01/translation.md); fixed source: [`chapters/01/source.md`](chapters/01/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འདུལ་བ་དང<br>མདོ་སྡེ་དང<br>མངོན་པ་ལ་སོགས་པ་དང |
| Before | Vinaya, Sūtra, Abhidharma, and so forth; |
| After | discipline, discourse collection, higher doctrine, and so forth; |

- **PD-003**: `འདུལ་བ`; “Vinaya” → “discipline” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `མདོ་སྡེ`; “Sūtra” → “discourse collection” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `མངོན་པ`; “Abhidharma” → “higher doctrine” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.

#### MTP-000032 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ནས་བཅོམ་ལྡན་འདས་འཁྲུལ་པ་ཐམས་ཅད་དག་པའི་མངའ་བདག་ལ<br>གསང་བའི་བདག་པོ་ལ་སོགས་པའི་རིགས་གསུམ་གྱི་ཁྲོ་བོ་རྣམས་ཀྱིས་འདི་སྐད་ཅེས་གསོལ་ཏེ |
| Before | Then the wrathful ones of the three families, the Lord of Secrets and the others, addressed the Bhagavān, the sovereign in whom all delusion is pure, in these words: |
| After | Then the wrathful ones of the three families, the Lord of Secrets and the others, addressed the Blessed One, the sovereign in whom all delusion is pure, in these words: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000033 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་བཅོམ་ལྡན་འཁྲུལ་མེད་སྐུ<br>ཁམས་གསུམ་འཁོར་བའི་སེམས་ཅན་རྣམས<br>འཁྲུལ་པ་ལྡོག་ན་ཇི་ལྟར་ལྡོག<br>བདག་ཅག་རྣམས་ལ་བཀའ་སྩལ་ཅིག |
| Before | “O, O Bhagavān, embodiment without delusion!<br>For the sentient beings of saṃsāra in the three realms,<br>if delusion is reversed, how is it reversed?<br>Please tell us!” |
| After | “O, O Blessed One, embodiment without delusion!<br>For the karmic beings of cyclic existence in the three realms,<br>if delusion is reversed, how is it reversed?<br>Please tell us!” |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000034 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ནས་བཅོམ་ལྡན་རྡོ་རྗེ་སེམས་དཔའ་དེས<br>ཉེ་བའི་འཁོར་ལ་བཀའ་སྩལ་པ |
| Before | Then that Bhagavān Vajrasattva<br>spoke to the close retinue: |
| After | Then that Blessed One Vajrasattva<br>spoke to the close retinue: |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000035 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་མ་ཉོན་ཅིག་གསང་བའི་བདག<br>དང་པོ་གཞི་ལ་འཁྲུལ་མེད་ཀྱང<br>སེམས་ཅན་བློ་ལ་འཁྲུལ་པ་སྟེ<br>དེ་ཡང་རིག་པའི་ཡེ་ཤེས་ཀྱི<br>རྩི་ཡི་དོན་ལ་ཐེབས་གྱུར་ན |
| Before | “Ah! Listen, Lord of Secrets.<br>Although there is no delusion in the Ground at the beginning,<br>there is delusion in sentient beings’ conceptual minds.<br>If, then, one reaches the meaning of the sap<br>of awareness’s primordial knowing, |
| After | “Ah! Listen, Lord of Secrets.<br>Although there is no delusion in the Ground at the beginning,<br>there is delusion in karmic beings’ conceptual minds.<br>If, then, one reaches the meaning of the sap<br>of awareness’s primordial knowing, |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000037 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁྲུལ་པ་དང་པོའི་གཞི་ལ་ལྡོག<br>རང་རིག་ཡེ་ཤེས་རྟོགས་དཀའ་བ<br>གཞི་ལ་སྙིང་པོ་མི་རྟོག་ཅན<br>འཁྲུལ་པ་གདར་ཤ་བཅད་པའི་ཐབས<br>མ་རིག་འཁོར་བ་འདས་ཤེས་སུ་བདལ |
| Before | delusion is reversed in the initial Ground.<br>Self-awareness’s primordial knowing is difficult to realize.<br>In the Ground, [there is] an essence endowed with non-conceptuality.<br>The means of conclusively determining delusion:<br>spread ignorance and saṃsāra into [unresolved: འདས་ཤེས]. |
| After | delusion is reversed in the initial Ground.<br>Self-awareness’s primordial knowing is difficult to realize.<br>In the Ground, [there is] a core endowed with non-conceptuality.<br>The means of conclusively determining delusion:<br>spread ignorance and cyclic existence into [unresolved: འདས་ཤེས]. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-006**: `སྙིང་པོ་མི་རྟོག་ཅན`; “an essence endowed” → “a core endowed” (1 occurrence(s)); severity **medium**, confidence **high**. P2 core for སྙིང་པོ, distinct from essence. Preserve the bracketed copula and non-conceptuality attachment.

#### MTP-000041 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁྲུལ་སྣང་ཡུལ་ཕྱུང་རིག་པ་རང<br>དྲན་པ་རྒྱུན་བཅད་ཆོས་སྐུའི་ངང<br>འཁོར་བ་སྤྱི་ཕྱུད་སྐུ་གསུམ་གསལ |
| Before | Bring forth the object of delusory appearance—awareness itself.<br>Cut the flow of mindfulness—the state of the dharma embodiment.<br>Extract saṃsāra’s quintessence—the three embodiments are clear. |
| After | Bring forth the object of delusory appearance—awareness itself.<br>Cut the flow of mindfulness—the state of the dharma embodiment.<br>Extract cyclic existence’s quintessence—the three embodiments are clear. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000043 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྟོང་པ་དངོས་མེད་གསལ་བས་མཛེས<br>དུག་ལྔ་མདོར་ཕྱུང་སྨན་གྱི་ངང<br>མུན་པའི་རྒྱུ་ཟད་སྒྲོན་མ་ཉིད<br>འཁྲུལ་པའི་རྒྱུ་ཟད་ཡེ་ཤེས་གྲོགས<br>གསལ་བའི་སྐུ་འབར་གཉིས་མེད་ངང<br>བེམ་རིག་གཉིས་མེད་འཁོར་བ་སངས<br>དོན་གྱི་ཡེ་ཤེས་གཞི་ལ་ལྡོག<br>དོན་དམ་ཀུན་རྫོབ་གཉིས་མེད་པའི |
| Before | Empty and without substance, beautiful with clarity;<br>sum up the five poisons—the state of medicine.<br>The cause of darkness exhausted—the lamp itself.<br>The cause of delusion exhausted—primordial knowing as companion.<br>The embodiment of clarity blazes—the nondual state.<br>Insentience and awareness are nondual; saṃsāra is cleared away.<br>The primordial knowing of meaning returns to the Ground,<br>of the nonduality of the ultimate and the conventional—[attachment unresolved]. |
| After | Empty and without entities, beautiful with clarity;<br>sum up the five poisons—the state of medicine.<br>The cause of darkness exhausted—the lamp itself.<br>The cause of delusion exhausted—primordial knowing as companion.<br>The embodiment of clarity blazes—the nondual state.<br>Matter and awareness are nondual; cyclic existence is cleared away.<br>The primordial knowing of meaning returns to the Ground,<br>of the nonduality of the ultimate and the conventional—[attachment unresolved]. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-007**: `དངོས་མེད`; “without substance” → “without entities” (1 occurrence(s)); severity **medium**, confidence **high**. P2 negative entity family; these empty/clear/entity contrasts do not establish an exclusively material sense. Retain separate exact དངོས་ཏེ uncertainties and all predicates.
- **PD-008**: `བེམ་རིག`; “Insentience and awareness” → “Matter and awareness” (1 occurrence(s)); severity **medium**, confidence **medium**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.

#### MTP-000044 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་རྟ་མགྲིན་རྒྱལ་པོ་ཉོན<br>སེམས་ཀྱི་གནས་ཕྱུང་ཡེ་ཤེས་ཉིད<br>རྐྱེན་སྣང་ཡུལ་མེད་ཅིག་ཆར་བ<br>འཁྲུལ་པ་ལྡོག་པའི་ལྡོག་ས་ནི<br>ལུ་གུ་རྒྱུད་དུ་ཐམས་ཅད་སངས<br>དྲན་མེད་ཡུལ་གྱི་དཀྱིལ་འཁོར་དུ<br>རྣམ་རྟོག་ལས་གྲོལ་རྒྱུད་ཆེན་གསལ |
| Before | Ah! Listen, King Hayagrīva.<br>Bring forth the abiding of ordinary mind—primordial knowing itself.<br>Conditioned appearance is without an object, all at once.<br>As for the place of reversal where delusion is reversed:<br>everything is cleared away in the vajra chains.<br>In the maṇḍala of the object without mindfulness,<br>free from differentiating conceptualization, the great continuum is clear. |
| After | Ah! Listen, King Hayagrīva.<br>Bring forth the abiding of ordinary mind—primordial knowing itself.<br>Conditioned appearance is without an object, all at once.<br>As for the place of reversal where delusion is reversed:<br>everything is cleared away in the vajra chains.<br>In the mandala of the object without mindfulness,<br>free from differentiating conceptualization, the great continuum is clear. |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.

#### MTP-000061 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རིག་པ་ཉིད་ཀྱི་ངོ་བོ་ནི<br>སྤྲོ་མེད་བསྡུ་མེད་ངང་དུ་གྲོལ<br>ཆོས་ཀྱི་སྐུ་ཡི་རང་སྣང་ནི<br>ཐད་ཀ་ཙམ་དུ་སྣང་བ་ལས<br>དངོས་པོ་དྲན་བྱེད་ཡིད་ལས་འདས<br>མཚན་མར་སྣང་བ་ཐམས་ཅད་ཀུན<br>སྐྱེ་མེད་ཆོས་སྐུ་ཐོབ་པའོ |
| Before | The essence of awareness itself<br>is liberated in a state without projection or gathering.<br>The self-appearance of the dharma embodiment<br>merely appears directly;<br>it is beyond the mental faculty that recalls entities.<br>Every appearance as a characteristic, without exception,<br>attains the non-arising dharma embodiment. |
| After | The essence of awareness itself<br>is liberated in a state without projection or gathering.<br>The self-appearance of the dharma embodiment<br>merely appears directly;<br>it is beyond the mental faculty that recalls entities.<br>Every appearance as a mark, without exception,<br>attains the non-arising dharma embodiment. |

- **PD-009**: `མཚན་མ`; “a characteristic” → “a mark” (1 occurrence(s)); severity **medium**, confidence **high**. P2 mark, not characteristic, for the complete མཚན་མ expression in these appearances/apprehending constructions.

#### MTP-000062 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>རིག་པའི་ཡེ་ཤེས་སྣང་མེད་པས<br>བེམས་པོའི་སྣང་བས་ང་མི་བསྒྲིབ<br>སྟོང་པའི་ཆོས་ཉིད་ཡུལ་མེད་པས<br>སྟོང་པ་ཉིད་ལ་ང་མི་གནས<br>མཚན་མར་འཛིན་པ་དངོས་དག་པས<br>འཛིན་པའི་ཆོས་ལ་ང་མི་གནས |
| Before | Emaho!<br>Since awareness’s primordial knowing has no appearance,<br>the appearance of insentient matter does not obscure me.<br>Since the empty nature of phenomena has no object,<br>I do not abide in emptiness.<br>Since apprehending as characteristics is pure in actuality,<br>I do not abide in the phenomena of the apprehending subject. |
| After | How wondrous!<br>Since awareness’s primordial knowing has no appearance,<br>the appearance of matter does not obscure me.<br>Since the empty nature of phenomena has no object,<br>I do not abide in emptiness.<br>Since apprehending as marks is pure in actuality,<br>I do not abide in the phenomena of the apprehending subject. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.
- **PD-008**: `བེམས་པོ`; “insentient matter” → “matter” (1 occurrence(s)); severity **medium**, confidence **high**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.
- **PD-009**: `མཚན་མ`; “characteristics” → “marks” (1 occurrence(s)); severity **medium**, confidence **high**. P2 mark, not characteristic, for the complete མཚན་མ expression in these appearances/apprehending constructions.

#### MTP-000064 — chapter 2

Location: [`chapters/02/translation.md`](chapters/02/translation.md); fixed source: [`chapters/02/source.md`](chapters/02/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཤེས་རབ་ཆེན་པོས་རང་བྱུང་བས<br>སྡེ་སྣོད་ཆོས་ལ་ང་མི་གནས<br>ང་ལ་དགེ་དང་སྡིག་མེད་པས<br>འཁོར་བའི་ཆོས་ལ་ང་མི་གནས |
| Before | Since [I] arise naturally through great discerning knowing,<br>I do not abide in the teachings of the scriptural collections.<br>Since for me there is neither virtue nor wrongdoing,<br>I do not abide in the phenomena of saṃsāra.” |
| After | Since [I] arise naturally through great discerning knowing,<br>I do not abide in the teachings of the scriptural collections.<br>Since for me there is neither virtue nor wrongdoing,<br>I do not abide in the phenomena of cyclic existence.” |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000068 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་བཅོམ་ལྡན་རྡོ་རྗེ་འཆང<br>རང་རིག་ཡེ་ཤེས་ཆེན་པོའི་ལུང<br>ངེས་པའི་རྒྱལ་པོས་བཀའ་སྩོལ་ཅིག |
| Before | “O, O Bhagavān Vajradhara!<br>The authoritative teaching of self-awareness’s great primordial knowing—<br>please bestow [it], king of certainty!” |
| After | “O, O Blessed One Vajradhara!<br>The transmission of self-awareness’s great primordial knowing—<br>please bestow [it], king of certainty!” |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-011**: `ལུང`; “authoritative teaching” → “transmission” (1 occurrence(s)); severity **medium**, confidence **high**. P2 transmission in teaching/naming contexts. Keep source-supported scriptural at 000197, not as an automatic modifier elsewhere; retain continuum/tantra distinctions and open apposition.

#### MTP-000069 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ནས་བཅོམ་ལྡན་རྡོ་རྗེ་འཆང<br>མ་བཞུགས་པ་ཡི་སྟན་ལས་ལངས<br>སར་བ་འདུས་ཧ་སྒྲ་བརྗོད་ནས<br>འདུས་པའི་ཚོགས་ལ་བཀའ་སྩལ་པ |
| Before | Then Bhagavān Vajradhara<br>arose from the seat where he did not abide.<br>Having uttered the word-formula [retained: སར་བ་འདུས་ཧ],<br>he spoke to the assembled gathering: |
| After | Then Blessed One Vajradhara<br>arose from the seat where he did not abide.<br>Having uttered the word-formula [retained: སར་བ་འདུས་ཧ],<br>he spoke to the assembled gathering: |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000080 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་གསང་བདག་རྡོ་རྗེ་འཛིན<br>འཁོར་བ་ཉིད་ཀྱི་དོན་རྟོགས་ན<br>མྱ་ངན་འདས་ཞེས་ཡོད་མ་ཡིན<br>ཉོན་མོངས་ལྔ་ཡི་དོན་རྟོགས་ན |
| Before | O, O, Lord of Secrets, holder of the vajra!<br>If one realizes the meaning of saṃsāra itself,<br>there is no such thing called ‘nirvāṇa.’<br>If one realizes the meaning of the five afflictions, |
| After | O, O, Lord of Secrets, holder of the vajra!<br>If one realizes the meaning of cyclic existence itself,<br>there is no such thing called ‘transcendence of sorrow.’<br>If one realizes the meaning of the five afflictions, |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `མྱ་ངན་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000083 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབྱུང་ལྔ་ཉིད་ཀྱི་དོན་རྟོགས་ན<br>ཆེན་པོ་ལྔ་ཉིད་བབས་ཀྱིས་འགྲུབ<br>མ་རིག་ཉིད་ཀྱི་རྩད་ཆོད་ན<br>རིག་པའི་སྐུ་ཉིད་མ་བསྒྲུབས་འགྲུབ<br>སེམས་ཅན་ཉིད་ཀྱི་དོན་ཤེས་ན<br>སངས་རྒྱས་ཉིད་ཀྱང་མ་བཙལ་རྙེད<br>སྣ་ཚོགས་སྣང་བའི་དོན་རྟོགས་ན<br>རང་རིག་འོད་སྣང་མ་བཙལ་རྙེད |
| Before | If one realizes the meaning of the five elements themselves,<br>the five great [ones] are accomplished naturally.<br>If the root of ignorance itself is ascertained,<br>the embodiment of awareness itself is accomplished without being accomplished.<br>If one knows the meaning of sentient beings themselves,<br>buddhas themselves are found without being sought.<br>If one realizes the meaning of varied appearances,<br>the light-appearance of self-awareness is found without being sought. |
| After | If one realizes the meaning of the five elements themselves,<br>the five great [ones] are accomplished naturally.<br>If the root of ignorance itself is ascertained,<br>the embodiment of awareness itself is accomplished without being accomplished.<br>If one knows the meaning of karmic beings themselves,<br>buddhas themselves are found without being sought.<br>If one realizes the meaning of varied appearances,<br>the light-appearance of self-awareness is found without being sought. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000087 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>རང་སྣང་སྟོང་པ་ཉིད་ཀྱི་རྒྱ<br>ཤེས་ཀྱི་རྒྱས་བཏབ་པ་བསྟན |
| Before | Emaho!<br>Self-appearance—the seal of emptiness itself—<br>is taught as stamped with the seal of knowing. |
| After | How wondrous!<br>Self-appearance—the seal of emptiness itself—<br>is taught as stamped with the seal of knowing. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000088 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྟོང་འབྱམས་ཡེ་ཤེས་སྐུ་ཡི་རྒྱ<br>སྣ་ཚོགས་སེམས་ཉིད་རིག་པའི་རྒྱ<br>རྣམ་དག་ཀློང་ཡངས་ཡེ་ཤེས་རྒྱ<br>མཚན་མ་དངོས་དག་རང་རིག་རྒྱ<br>སྣང་བ་རང་རྫོགས་དབྱིངས་ཀྱི་རྒྱ<br>སྤྱོད་པ་རྨད་བྱུང་སྣང་བའི་རྒྱ<br>བསྒོམ་པ་རྨད་བྱུང་སེམས་ཀྱི་རྒྱ |
| Before | Boundless emptiness—the seal of the embodiment of primordial knowing.<br>Varied ordinary mind itself—the seal of awareness.<br>The perfectly pure, spacious expanse—the seal of primordial knowing.<br>Characteristics pure in actuality—the seal of self-awareness.<br>Appearance complete in itself—the seal of basic space.<br>Wondrous activity—the seal of appearance.<br>Wondrous cultivation—the seal of ordinary mind. |
| After | Boundless emptiness—the seal of the embodiment of primordial knowing.<br>Varied ordinary mind itself—the seal of awareness.<br>The perfectly pure, spacious expanse—the seal of primordial knowing.<br>Marks pure in actuality—the seal of self-awareness.<br>Appearance complete in itself—the seal of basic space.<br>Wondrous activity—the seal of appearance.<br>Wondrous cultivation—the seal of ordinary mind. |

- **PD-009**: `མཚན་མ`; “Characteristics” → “Marks” (1 occurrence(s)); severity **medium**, confidence **high**. P2 mark, not characteristic, for the complete མཚན་མ expression in these appearances/apprehending constructions.

#### MTP-000091 — chapter 3

Location: [`chapters/03/translation.md`](chapters/03/translation.md); fixed source: [`chapters/03/source.md`](chapters/03/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>གསང་བའི་བདག་པོ་ཆེན་པོ་ཉོན<br>གསང་བའི་དབང་ཉིད་རབ་རྫོགས་པ<br>སྙིང་པོ་བཅུད་ཀྱི་གདམས་ངག་འདི<br>སྙིང་པོ་ཉིད་ལ་སྙིང་པོ་བརྟན |
| Before | Emaho!<br>Listen, great Lord of Secrets.<br>The secret empowerment itself is utterly complete.<br>This instruction of the core’s vital extract—<br>in the core itself, the core is stable. |
| After | How wondrous!<br>Listen, great Lord of Secrets.<br>The secret empowerment itself is utterly complete.<br>This oral instruction of the core’s quintessence—<br>in the core itself, the core is stable. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.
- **PD-012**: `སྙིང་པོ་བཅུད་ཀྱི་གདམས་ངག་འདི`; “This instruction of the core’s vital extract” → “This oral instruction of the core’s quintessence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 oral instruction and quintessence; preserve the core genitive and repetition. Current 000261 already says oral instructions and needs no repair.

#### MTP-000102 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་བཅོམ་ལྡན་ཐུགས་རྗེ་ཅན<br>བདག་ཅག་རང་རིག་རྗེས་མཐུན་ལ<br>ཆོས་ཉིད་དབྱིངས་ཀྱི་བསྟན་པ་གསུངས |
| Before | “O, O Bhagavān, endowed with compassionate responsiveness!<br>In accord with our self-awareness,<br>speak the teaching of the basic space of the nature of phenomena.” |
| After | “O, O Blessed One, endowed with compassionate responsiveness!<br>In accord with our self-awareness,<br>speak the teaching of the basic space of the nature of phenomena.” |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000103 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་སྐད་རབ་ཏུ་ཞུས་པ་དང<br>བཅོམ་ལྡན་རྡོ་རྗེ་དཔའ་བོ་དེས<br>ཏིང་ངེ་འཛིན་ལས་བཞེངས་ནས་ནི<br>ཉེ་བའི་འཁོར་ལ་བཀའ་སྩལ་པ |
| Before | When [he] had thoroughly petitioned in these words,<br>that Bhagavān, the vajra hero,<br>arose from deep absorption<br>and spoke to the nearby retinue: |
| After | When [he] had thoroughly petitioned in these words,<br>that Blessed One, the vajra hero,<br>arose from deep absorption<br>and spoke to the nearby retinue: |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000105 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཆོས་དབྱིངས་རྒྱན་དང་ལྡན་པའི་ཕྱིར<br>སངས་རྒྱས་ཀུན་གྱི་ཡེ་ཤེས་སྐུ<br>སངས་རྒྱས་སེམས་ཅན་ཀུན་གྱི་དུར<br>ཐེམ་ཞིང་ཡང་དག་དོན་ལ་སྤྱོད |
| Before | Because the basic space of phenomena is endowed with adornment,<br>the embodiment of the primordial knowing of all buddhas—<br>of all buddhas and sentient beings, [retained: དུར]<br>[retained: ཐེམ་ཞིང]; [it] acts in the authentic meaning. |
| After | Because the basic space of phenomena is endowed with adornment,<br>the embodiment of the primordial knowing of all buddhas—<br>of all buddhas and karmic beings, [retained: དུར]<br>[retained: ཐེམ་ཞིང]; [it] acts in the authentic meaning. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000110 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཆོས་ཉིད་ཡངས་པའི་དཀྱིལ་འཁོར་དུ<br>གསང་སྔགས་ཐབས་ཀྱི་སྤྱོད་པ་ནི<br>བཅོམ་ལྡན་རྡོ་རྗེ་སེམས་དཔས་བསྟན |
| Before | In the vast mandala of the nature of phenomena,<br>the activity of the means of secret mantra<br>was taught by Bhagavān Vajrasattva: |
| After | In the vast mandala of the nature of phenomena,<br>the activity of the means of secret mantra<br>was taught by Blessed One Vajrasattva: |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000111 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>སྣང་བ་ཆེན་པོ་གསལ་བ་ཆེ<br>དག་པའི་ཡེ་ཤེས་འོད་དུ་གསལ<br>ཆོས་ཉིད་སྤྲོས་པ་མེད་པའི་ཀློང<br>འགྱུར་མེད་ཕོ་བྲང་ལྷུན་འབྱམས་འདི<br>སོ་སོར་སྣང་ཞིང་དོན་བྱེད་པས |
| Before | “Emaho!<br>Great appearance has great clarity.<br>Pure primordial knowing is clear as light.<br>The expanse of the nature of phenomena, without conceptual elaborations—<br>this spontaneously vast, unchanging palace—<br>since [it] appears individually and serves purposes, |
| After | “How wondrous!<br>Great appearance has great clarity.<br>Pure primordial knowing is clear as light.<br>The expanse of the nature of phenomena, without conceptual elaborations—<br>this spontaneously vast, unchanging palace—<br>since [it] appears individually and serves purposes, |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000115 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ལྟ་བའི་ཡེ་ཤེས་ཐབས་མཁས་པས<br>མ་བསྐྱོད་རྡོ་རྗེ་སེམས་དཔའི་ངང<br>སྣ་ཚོགས་རོལ་པའི་སྐུ་བསྟན་པས<br>རྒྱུན་ཏུ་སྣང་ཞིང་རྣམ་པར་རོལ<br>གསང་སྔགས་ཐབས་ཀྱི་སྒོ་མང་བས<br>ཡིད་ཆེས་གསུམ་གྱིས་རབ་ཏུ་བསྟན |
| Before | Since the primordial knowing of the view is skilled in means,<br>in the state of unmoved Vajrasattva,<br>since the embodiment of varied play is shown,<br>[it] appears continuously and fully plays.<br>Since the means of secret mantra have many gates,<br>[it] is thoroughly taught through the three assurances. |
| After | Since the primordial knowing of the view is skilled in means,<br>in the state of unmoved Vajrasattva,<br>since the embodiment of varied play is shown,<br>[it] appears continuously and fully plays.<br>Since the means of secret mantra have many gates,<br>[it] is thoroughly taught through the three convictions. |

- **PD-013**: `ཡིད་ཆེས་གསུམ`; “three assurances” → “three convictions” (1 occurrence(s)); severity **medium**, confidence **high**. P2 three convictions for numbered ཡིད་ཆེས་གསུམ; distinguish confidence, faith and devotion and do not name the three members.

#### MTP-000121 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཆོས་སྐུ་དངོས་པོའི་ལམ་དུ་སྣང<br>དྲི་མ་མེད་པའི་ཡེ་ཤེས་ནི<br>སྟོང་པའི་ཡུལ་གྱི་གནད་དུ་བརྡེག<br>མན་ངག་རྒྱལ་པོ་སྤྱི་བཅིངས་དང<br>ཐམས་ཅད་རང་སྣང་ལྷུན་རྫོགས་པའོ |
| Before | The dharma embodiment appears on the path of entities.<br>Primordial knowing without stains<br>strikes the vital point of the object of emptiness.<br>The king of pith instruction binds all together, and<br>everything—self-appearance—is spontaneously complete. |
| After | The dharma embodiment appears on the path of entities.<br>Primordial knowing without stains<br>strikes the key point of the object of emptiness.<br>The king of pith instruction binds all together, and<br>everything—self-appearance—is spontaneously complete. |

- **PD-014**: `གནད`; “vital point” → “key point” (1 occurrence(s)); severity **medium**, confidence **high**. P2 key point; preserve striking/application and the familiarization genitive.

#### MTP-000122 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>རྣལ་འབྱོར་ཀུན་གྱི་ལྟ་བ་ནི<br>སེམས་ཀྱི་སྒོ་བཅད་རྣམ་རྟོག་དངས<br>ཁྱིམ་ཡངས་ཕུགས་རྡིབ་མན་ངག་ནི<br>འདོད་པའི་སྒོ་བཅད་ཡེ་ཤེས་ནང་དུ་གསལ |
| Before | Emaho!<br>As for the view of all yogas:<br>the gate of ordinary mind is closed; differentiating conceptualization clears.<br>The pith instruction: a spacious house, a collapsed interior;<br>with desire’s gate closed, primordial knowing is clear within. |
| After | How wondrous!<br>As for the view of all yogas:<br>the gate of ordinary mind is closed; differentiating conceptualization clears.<br>The pith instruction: a spacious house, a collapsed interior;<br>with desire’s gate closed, primordial knowing is clear within. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000126 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>རང་རིག་ཡེ་ཤེས་མ་གཡོས་ངང་དུ་ཞོག<br>མ་རིག་པ་ཉིད་ཀློང་དུ་སྐྱོལ<br>འཁོར་བ་ཉིད་ཀྱང་རུ་ནས་བཟློག<br>སྤྱད་པས་མ་ཕྱེད་ཡུལ་དུ་མེད |
| Before | Emaho!<br>Rest self-awareness’s primordial knowing in an unmoved state.<br>Carry ignorance itself into the expanse.<br>Turn back even saṃsāra [རུ་ནས: locus unresolved].<br>[It] is not distinguished by activity and does not exist as an object. |
| After | How wondrous!<br>Rest self-awareness’s primordial knowing in an unmoved state.<br>Carry ignorance itself into the expanse.<br>Turn back even cyclic existence [རུ་ནས: locus unresolved].<br>[It] is not distinguished by activity and does not exist as an object. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000128 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀུན་གཞི་ལུས་ཀྱི་མེ་ལོང་ལ<br>སྟོང་རིག་གསལ་བའི་གཞི་བསྟན་པས<br>གཞན་བྱུང་འཁྲུལ་པ་གཞི་ལ་བསྐྱལ<br>ཕུང་པོ་ལྔ་ཉིད་རྒྱུ་མེད་པས<br>འཁྲུལ་པའི་ལུས་ནི་མངོན་སངས་རྒྱས |
| Before | In the mirror of the all-basis body,<br>since the ground of empty, clear awareness is shown,<br>delusion arising from another is brought to the ground.<br>Since the five aggregates themselves are without cause,<br>the body of delusion is manifestly buddha. |
| After | In the mirror of the all-basis body,<br>since the Ground of empty, clear awareness is shown,<br>delusion arising from another is brought to the Ground.<br>Since the five aggregates themselves are without cause,<br>the body of delusion is manifestly buddha. |

- **PD-015**: `གཞི`; “ground” → “Ground” (2 occurrence(s)); severity **low**, confidence **high**. P1 capital Ground / Ground-appearance for these explicitly technical uses; no change to ordinary physical ground, levels or disputed support compounds.

#### MTP-000130 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབྱུང་བ་ལྔ་ཉིད་ཡེ་དངས་པས<br>སྣང་བ་འོད་གསལ་གཉིད་དུ་གྲོལ<br>དབང་པོ་ལྔ་ཉིད་ཅེར་བཞག་པས<br>འཛིན་པའི་ཡུལ་ལྔ་རང་སར་གྲོལ<br>ཉོན་མོངས་ལྔ་ཉིད་རང་ཡིན་པས<br>ཁམས་གསུམ་ཉིད་ནི་གཞི་ལ་བསྐྱལ |
| Before | Since the five elements themselves are primordially clarified,<br>appearance is liberated into clear-light sleep.<br>Since the five faculties themselves are left in naked resting,<br>the five objects of the apprehending subject are liberated in their own place.<br>Since the five afflictions themselves are [one’s] own,<br>the three realms themselves are brought to the ground. |
| After | Since the five elements themselves are primordially clarified,<br>appearance is liberated into clear-light sleep.<br>Since the five faculties themselves are left in naked resting,<br>the five objects of the apprehending subject are liberated in their own place.<br>Since the five afflictions themselves are [one’s] own,<br>the three realms themselves are brought to the Ground. |

- **PD-015**: `གཞི`; “ground” → “Ground” (1 occurrence(s)); severity **low**, confidence **high**. P1 capital Ground / Ground-appearance for these explicitly technical uses; no change to ordinary physical ground, levels or disputed support compounds.

#### MTP-000135 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མེད་པའི་འཕྲོ་འདུ་ཡེ་སྟོང་པས<br>ཡེ་ནས་བསམ་གཏན་ཆེན་པོར་གནས<br>དྲི་མ་རྣམས་ནི་རང་དག་པས<br>དྲི་མེད་ཟང་ཐལ་ཆེན་པོར་གནས<br>བྱས་པ་བྱུང་བ་མེད་པའི་ཕྱིར<br>ཐོག་མ་ཉིད་ནས་བྱ་བྱེད་བྲལ |
| Before | Since the proliferating and gathering of nonexistence are primordially empty,<br>[one] abides in great meditative concentration from the beginning.<br>Since the stains are self-purified,<br>[one] abides in great stainless unimpeded penetration.<br>Because what is done has not arisen,<br>[one is] free from doing and the doer from the outset. |
| After | Since the proliferating and gathering of nonexistence are primordially empty,<br>[one] abides in great meditative stability from the beginning.<br>Since the stains are self-purified,<br>[one] abides in great stainless unimpeded penetration.<br>Because what is done has not arisen,<br>[one is] free from doing and the doer from the outset. |

- **PD-023**: `བསམ་གཏན་ཆེན་པོར་གནས`; “meditative concentration” → “meditative stability” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 local meditative-stability proposal tested against state grammar (abides in) and the six actual occurrences, especially the separate deep absorption at 000338. Local provisional construction decision, not a newly approved shared entry.

#### MTP-000136 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | གཞི་ནས་གཞན་འབྱུང་ཆོས་མེད་པས |
| Before | Since, from the ground, no phenomena arise from another, |
| After | Since, from the Ground, no phenomena arise from another, |

- **PD-015**: `གཞི`; “ground” → “Ground” (1 occurrence(s)); severity **low**, confidence **high**. P1 capital Ground / Ground-appearance for these explicitly technical uses; no change to ordinary physical ground, levels or disputed support compounds.

#### MTP-000139 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་བ་རྒྱུ་མེད་འགགས་ཟིན་པས<br>ཡེ་ནས་སངས་རྒྱས་ཉིད་ཀྱི་ས<br>མཚན་མའི་དངོས་པོ་སྟོང་སངས་པས<br>བདག་འཛིན་བློ་ནི་ཡེ་ནས་ཟད<br>རྐྱེན་རྣམས་རྐྱེན་གྱིས་རང་གྲོལ་བས<br>ལྟོས་ཆོས་རྣམས་ནི་ཅོག་བཞག་པའོ |
| Before | Since saṃsāra, without cause, has already ceased,<br>[there is] the level of buddha itself from the beginning.<br>Since entities of marks are emptied and cleared away,<br>the self-grasping conceptual mind is exhausted from the beginning.<br>Since conditions are self-liberated by conditions,<br>dependent phenomena are left as they are.” |
| After | Since cyclic existence, without cause, has already ceased,<br>[there is] the level of buddha itself from the beginning.<br>Since entities of marks are emptied and cleared away,<br>the self-grasping conceptual mind is exhausted from the beginning.<br>Since conditions are self-liberated by conditions,<br>dependent phenomena are left as they are.” |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000144 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་དེ་ལྟར་སྣང་བ་རྣམས<br>འཁྲུལ་པ་ཉིད་ཀྱང་རང་གྲོལ་ན<br>འཁྲུལ་མེད་སྣང་བ་ཅིས་མི་གྲོལ<br>ཇི་ལྟར་སྨྲ་དང་བྱ་བྱེད་རྣམས<br>སྟོང་རིག་གསལ་བའི་སྤྱོད་པ་ཡིན |
| Before | “Ema! If appearances such as those,<br>even delusion itself, are self-liberated,<br>why are appearances free from delusion not liberated?<br>Whatever the speaking, and all doing and doers,<br>are the activity of clear empty awareness. |
| After | “Ah! If appearances such as those,<br>even delusion itself, are self-liberated,<br>why are appearances free from delusion not liberated?<br>Whatever the speaking, and all doing and doers,<br>are the activity of clear empty awareness. |

- **PD-027**: `ཨེ་མ`; “Ema!” → “Ah!” (1 occurrence(s)); severity **low**, confidence **medium**. Local rendering of short ཨེ་མ as Ah!, tested with 000044/000625/000645. Retain the short/full source distinction; do not treat this as a new canonical entry or silently equate it with the full wonder formula.

#### MTP-000149 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཇི་ལྟར་སྨྲས་པ་སྔགས་ཀྱི་ཚིག<br>བསམ་པ་རྣམས་ནི་བསྐྱེད་རིམ་ཡིན<br>ཡིད་ལ་འགྱུ་བ་མཆོད་པ་ཉིད<br>གཟུགས་སུ་སྣང་བ་ལྷ་ཡི་སྐུ<br>སྒྲ་ཆེན་བརྗོད་པ་རོལ་མོ་ཉིད |
| Before | Whatever is spoken is a word of mantra.<br>Acts of thinking are the generation stage.<br>Movement in the mental faculty is offering itself.<br>Appearance as form is the deity’s embodiment.<br>The utterance of loud sound is music itself. |
| After | Whatever is spoken is a phrase of mantra.<br>Acts of thinking are the generation stage.<br>Movement in the mental faculty is offering itself.<br>Appearance as form is the deity’s embodiment.<br>The utterance of loud sound is music itself. |

- **PD-025**: `ཚིག`; “a word of mantra” → “a phrase of mantra” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000152 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འདའ་བར་འདོད་པ་དམ་ཚིག་ལ<br>བསྲུང་བར་འདོད་པ་བཅིངས་པ་ཉིད<br>དགྲོལ་བར་འདོད་པ་ཉམས་པ་སྟེ<br>མེད་པར་འདོད་པ་ཐུབ་མཆོག་ཡིན |
| Before | The desire to transgress is samaya;<br>the desire to guard is bondage itself.<br>The desire to liberate is deterioration;<br>the desire for absence is the supreme sage. |
| After | The desire to transgress is sacred pledge;<br>the desire to guard is bondage itself.<br>The desire to liberate is deterioration;<br>the desire for absence is the supreme sage. |

- **PD-016**: `དམ་ཚིག`; “samaya” → “sacred pledge” (1 occurrence(s)); severity **medium**, confidence **high**. P2 sacred pledge; preserve contrast with empowerment and vows, transgression/guarding and negative/rhetorical function.

#### MTP-000155 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཤེས་རིག་གསལ་བ་གདམས་ངག་ལ<br>ཡུལ་སེམས་གཉིས་འདུས་གདབ་པའི་ཡུལ<br>སྐྱེ་རྒས་ན་འཆི་གོམས་པའི་གནད<br>ཚོགས་དྲུག་མ་འགགས་རྟོགས་པའོ |
| Before | Clear knowing-awareness is instruction;<br>object and ordinary mind gathered together are the object of application.<br>Birth, aging, sickness, and death are the vital point of familiarization.<br>The unceasing six collections are realization.” |
| After | Clear knowing-awareness is oral instruction;<br>object and ordinary mind gathered together are the object of application.<br>Birth, aging, sickness, and death are the key point of familiarization.<br>The unceasing six collections are realization.” |

- **PD-012**: `གདམས་ངག`; “is instruction” → “is oral instruction” (1 occurrence(s)); severity **medium**, confidence **high**. P2 oral instruction and quintessence; preserve the core genitive and repetition. Current 000261 already says oral instructions and needs no repair.
- **PD-014**: `གནད`; “vital point” → “key point” (1 occurrence(s)); severity **medium**, confidence **high**. P2 key point; preserve striking/application and the familiarization genitive.

#### MTP-000161 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བསྐྱོད་ཅིང་དངས་སྙིགས་འབྱེད་པར་གྲོལ<br>ས་ནི་སྐྱེད་བྱེད་བདེགས་པས་ན<br>དངོས་མེད་མཐའ་ཡས་སྟོང་པར་གྲོལ<br>ཆུ་ནི་སྡུད་བྱེད་རླན་པས་ན<br>སྲེག་བྱེད་སྨིན་པའི་ལས་སུ་གྲོལ |
| Before | [it] is liberated as moving and separating the refined portion and dregs.<br>Since earth generates and supports,<br>[it] is liberated as insubstantial, limitless emptiness.<br>Since water gathers and moistens,<br>[it] is liberated as the work of burning and ripening. |
| After | [it] is liberated as moving and separating the pure extract and residue.<br>Since earth generates and supports,<br>[it] is liberated as limitless emptiness without entities.<br>Since water gathers and moistens,<br>[it] is liberated as the work of burning and ripening. |

- **PD-007**: `དངོས་མེད`; “insubstantial, limitless emptiness” → “limitless emptiness without entities” (1 occurrence(s)); severity **medium**, confidence **high**. P2 negative entity family; these empty/clear/entity contrasts do not establish an exclusively material sense. Retain separate exact དངོས་ཏེ uncertainties and all predicates.
- **PD-017**: `དངས་སྙིགས`; “refined portion and dregs” → “pure extract and residue” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000172 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་མ་བཅོམ་ལྡན་རྡོ་རྗེ་འཆང<br>སྣོད་འཇིག་རྟེན་ཀྱང་གྲོལ་གྱུར་བས<br>བཅུད་ཀྱི་སེམས་ཅན་ཅིས་མི་གྲོལ<br>སེམས་ཅན་གྲོལ་བ་རྣམས་ལ་དོན་མེད་འགྱུར<br>ཡང་ན་གྲོལ་བ་དེ་དག་ཀུན |
| Before | “O Bhagavān Vajradhara!<br>Since even the container-world has become liberated,<br>why are its contents, sentient beings, not liberated?<br>For liberated sentient beings, [this] would become meaningless.<br>Or are all those liberated ones |
| After | “O Blessed One Vajradhara!<br>Since even the container-world has become liberated,<br>why are its contents, karmic beings, not liberated?<br>For liberated karmic beings, [this] would become meaningless.<br>Or are all those liberated ones |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (2 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000174 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབད་པ་མེད་པར་གྲོལ་ལམ་ཅི<br>འབད་པས་གྲོལ་ན་བེམ་པོ་ནི<br>གྲོལ་བར་རིགས་པ་མ་ལགས་ན<br>སེམས་ཅན་གྲོལ་བ་ཇི་ལྟར་གྲོལ |
| Before | liberated without effort—or what?<br>If liberation is through effort, and the inert<br>are not reasonably to be liberated,<br>as for the liberation of sentient beings, how are they liberated?” |
| After | liberated without effort—or what?<br>If liberation is through effort, and matter<br>is not reasonably to be liberated,<br>as for the liberation of karmic beings, how are they liberated?” |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-008**: `བེམ་པོ་ནི<br>གྲོལ་བར་རིགས་པ་མ་ལགས་ན`; “and the inert<br>are not reasonably” → “and matter<br>is not reasonably” (1 occurrence(s)); severity **medium**, confidence **high**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.

#### MTP-000175 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ |
| Before | The Bhagavān spoke: |
| After | The Blessed One spoke: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000180 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མངལ་གྱི་ལྷུམས་སུ་ཚུད་པ་ནི<br>རང་རིག་གཞི་ནས་སྣང་བར་ཤར<br>བདུན་ཚན་བདུན་གྱི་རྟོགས་ཚད་དོ<br>ཟླ་བཅུ་ས་རྣམས་བགྲོད་པ་ཉིད |
| Before | Entry into the enclosure of the womb<br>is self-awareness arising as appearance from the ground.<br>[It is] the measure of realization of seven groups of seven.<br>Ten months—traversing the levels themselves. |
| After | Entry into the enclosure of the womb<br>is self-awareness arising as appearance from the Ground.<br>[It is] the measure of realization of seven groups of seven.<br>Ten months—traversing the levels themselves. |

- **PD-015**: `གཞི`; “ground” → “Ground” (1 occurrence(s)); severity **low**, confidence **high**. P1 capital Ground / Ground-appearance for these explicitly technical uses; no change to ordinary physical ground, levels or disputed support compounds.

#### MTP-000181 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཙས་པ་ཉིད་ནི་སྐུར་བཞེངས་ཏེ<br>ལུས་བསྐྱེད་པ་ནི་གཞི་སྣང་ཡུལ<br>ལུས་སུ་གནས་པ་གཞི་ཡིན་ཏེ<br>རྒས་པ་དག་ནི་འཁྲུལ་པ་སངས<br>ན་བ་ཉིད་ནི་རྟོགས་པའི་གདིང<br>ཤི་བས་ཆོས་ཉིད་སྟོང་པར་གྲོལ |
| Before | Birth itself is arising as embodiment.<br>The body’s growth is the object of ground-appearance.<br>Abiding in the body is the ground.<br>Aging is delusion clearing away.<br>Sickness itself is the confidence of realization.<br>Through death, [one] is liberated into the empty nature of phenomena. |
| After | Birth itself is arising as embodiment.<br>The body’s growth is the object of Ground-appearance.<br>Abiding in the body is the Ground.<br>Aging is delusion clearing away.<br>Sickness itself is the confidence of realization.<br>Through death, [one] is liberated into the empty nature of phenomena. |

- **PD-015**: `གཞི`; “ground” → “Ground” (2 occurrence(s)); severity **low**, confidence **high**. P1 capital Ground / Ground-appearance for these explicitly technical uses; no change to ordinary physical ground, levels or disputed support compounds.

#### MTP-000182 — chapter 4

Location: [`chapters/04/translation.md`](chapters/04/translation.md); fixed source: [`chapters/04/source.md`](chapters/04/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ལྟར་གཟུགས་སུ་སེམས་ཅན་ཏེ<br>འབད་པ་མེད་པར་ཡེ་ནས་གྲོལ<br>ཨེ་མ་སྤྱོད་བསམ་བསྒྱུར་སྣང་བ་གྲོལ<br>བསྒོམས་པས་མ་བཅོས་ཆོས་ཅན་གྲོལ |
| Before | Thus, sentient beings in form<br>are primordially liberated without effort.<br>Ema! Activity, thinking, transformation—appearance is liberated.<br>Uncontrived by cultivation, the bearer of phenomena is liberated. |
| After | Thus, karmic beings in form<br>are primordially liberated without effort.<br>Ah! Activity, thinking, transformation—appearance is liberated.<br>Uncontrived by cultivation, the bearer of phenomena is liberated. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-027**: `ཨེ་མ`; “Ema!” → “Ah!” (1 occurrence(s)); severity **low**, confidence **medium**. Local rendering of short ཨེ་མ as Ah!, tested with 000044/000625/000645. Retain the short/full source distinction; do not treat this as a new canonical entry or silently equate it with the full wonder formula.

#### MTP-000188 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་བཅོམ་ལྡན་རྡོ་རྗེ་འཆང<br>སངས་རྒྱས་ཀུན་གྱི་རང་བཞིན་གང<br>སེམས་ཅན་རྣམས་ལ་ཇི་ལྟར་གནས |
| Before | “O, O Bhagavān Vajradhara!<br>What is the intrinsic nature of all buddhas?<br>How does it abide in sentient beings? |
| After | “O, O Blessed One Vajradhara!<br>What is the intrinsic nature of all buddhas?<br>How does it abide in karmic beings? |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000200 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ལ་དཀྱིལ་འཁོར་ཡོད་པ་མིན<br>ལྷ་མེད་སྐྱེད་པའི་ས་བོན་མེད<br>སྔགས་དང་ཕྱག་རྒྱས་ཅི་ཞིག་བྱ<br>མཆོད་པ་ལ་སོགས་སྤྲོ་མི་དགོས<br>དབང་དང་དམ་ཚིག་ག་ལ་ཡོད |
| Before | There is no mandala in that;<br>there is no deity, no seed of generation.<br>What would one do with mantra and seals?<br>There is no need to elaborate offerings and the like.<br>Where are empowerment and commitments? |
| After | There is no mandala in that;<br>there is no deity, no seed of generation.<br>What would one do with mantra and seals?<br>There is no need to elaborate offerings and the like.<br>Where are empowerment and sacred pledges? |

- **PD-016**: `དམ་ཚིག`; “commitments” → “sacred pledges” (1 occurrence(s)); severity **medium**, confidence **high**. P2 sacred pledge; preserve contrast with empowerment and vows, transgression/guarding and negative/rhetorical function.

#### MTP-000203 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ནི་ཡིན་འགྲོ་བའང་ཡིན<br>སེམས་ཡིན་སེམས་ལས་བྱུང་བ་སྟེ<br>དུ་མ་ཡིན་ལ་ཉག་གཅིག་ཡིན<br>འཁོར་དང་མྱང་འདས་ང་རང་ཡིན |
| Before | It is that, and is also beings;<br>it is ordinary mind and what arises from ordinary mind.<br>It is many, and it is unique;<br>I myself am saṃsāra and nirvāṇa. |
| After | It is that, and is also beings;<br>it is ordinary mind and what arises from ordinary mind.<br>It is many, and it is unique;<br>I myself am cyclic existence and transcendence of sorrow. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `མྱང་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000212 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་དང<br>ང་རྒྱལ་ཕྲག་དོག་ལ་སོགས་ནི<br>དེ་ཉིད་ལས་ནི་ཆོ་འཕྲུལ་འབྱུང |
| Before | Desire, hatred, bewilderment,<br>pride, jealousy, and the like—<br>magical display arises from that itself. |
| After | Desire, hatred, deluded dullness,<br>pride, jealousy, and the like—<br>magical display arises from that itself. |

- **PD-024**: `གཏི་མུག`; “bewilderment” → “deluded dullness” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 local deluded-dullness proposal: 000212 and 000438 share the five-affliction list; 000367 confirms the same term. Keep རྨོངས་པ bewilderment, ignorance, delusion and established dullness distinct. Not approval of other unlisted affliction labels.

#### MTP-000220 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཁྲོ་བདག་དེ་ལྟར་གནས་པའི་ཆོས་ཉིད་ལ<br>འཁྲུལ་པ་གདོད་ནས་མེད་པ་སྟེ<br>ཆོས་སྐུ་ནམ་མཁའ་ལྟ་བུ་ལ<br>གློ་བུར་སེམས་ཅན་སྤྲིན་གྱིས་བསྒྲིབས |
| Before | O lord of wrathful ones, in the nature of phenomena abiding in this way,<br>there is no delusion from the beginning.<br>The dharma embodiment, like space,<br>is obscured by adventitious clouds of sentient beings. |
| After | O lord of wrathful ones, in the nature of phenomena abiding in this way,<br>there is no delusion from the beginning.<br>The dharma embodiment, like space,<br>is obscured by adventitious clouds of karmic beings. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000238 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མ་བུ་འཕྲད་པས་སྤྲུལ་སྐུར་བྱུང<br>རྟགས་སུ་ཡོད་པས་ཐབས་སུ་བྱུང<br>བསམ་འདས་ཡིན་པས་དྲན་པ་སངས<br>རྟག་ཆད་མེད་པས་གྲུབ་མཐའ་རྫོགས |
| Before | Because mother and child meet, [it] arises as emanation embodiment;<br>because [it] exists as a sign, [it] arises as means.<br>Because [it] is beyond thinking, mindfulness clears;<br>because there is no permanence or annihilation, philosophical tenets are complete. |
| After | Because mother and child meet, [it] arises as emanation embodiment;<br>because [it] exists as a sign, [it] arises as means.<br>Because [it] is beyond thinking, mindfulness clears;<br>because there is no permanence or annihilation, tenet systems are complete. |

- **PD-019**: `གྲུབ་མཐའ`; “philosophical tenets” → “tenet systems” (1 occurrence(s)); severity **medium**, confidence **high**. P2 tenet systems: actual organized positions and their sustaining function at 000238/000271; remove unsupported philosophical. The expanded 000268 construction stays provisional.

#### MTP-000243 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མ་ལུས་རྫོགས་པས་འབྲས་བུ་ཉིད<br>དམིགས་པ་དག་པས་ལམ་ཞེས་བྱ<br>འཁྲུལ་པ་ཟད་པས་ལུང་ཡང་ཡིན<br>ཡེ་ནས་གནས་པས་རྒྱུད་ཅེས་བྱ<br>མཚོན་དུ་ཡོད་པས་མན་ངག་ཡིན<br>གྲངས་ལས་འདས་པས་རྩིས་ཞེས་བྱ |
| Before | Because [it] is complete without remainder, [it] is the result itself;<br>because objects of focus are pure, [it] is called “path.”<br>Because delusion is exhausted, [it] is also scriptural transmission;<br>because [it] abides primordially, [it] is called “continuum.”<br>Because [it] can be indicated, [it] is pith instruction;<br>because [it] is beyond number, [it] is called “reckoning.” |
| After | Because [it] is complete without remainder, [it] is the result itself;<br>because objects of focus are pure, [it] is called “path.”<br>Because delusion is exhausted, [it] is also transmission;<br>because [it] abides primordially, [it] is called “continuum.”<br>Because [it] can be indicated, [it] is pith instruction;<br>because [it] is beyond number, [it] is called “reckoning.” |

- **PD-011**: `ལུང`; “scriptural transmission” → “transmission” (1 occurrence(s)); severity **medium**, confidence **high**. P2 transmission in teaching/naming contexts. Keep source-supported scriptural at 000197, not as an automatic modifier elsewhere; retain continuum/tantra distinctions and open apposition.

#### MTP-000247 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྤྲོ་བསྡུ་མེད་པས་ཁྱུང་ཆེན་འདྲ<br>ལྟ་བའི་རྩལ་རྫོགས་སེང་གེ་བཞིན<br>གཏིང་རྫོགས་ཁྱབ་པས་རྒྱ་མཚོ་འདྲ<br>རང་བྱུང་གྲོལ་བས་ནམ་མཁའ་བཞིན<br>ཐམས་ཅད་བརྟེན་པས་ས་གཞི་འདྲ<br>ཡུལ་རྣམས་ཀུན་ལས་ཁྱད་པར་འཕགས |
| Before | Because there is no elaboration or withdrawal, [it] is like a great garuḍa;<br>complete in the expressiveness of view, [it] is like a lion.<br>Because [it] pervades with complete depth, [it] is like the ocean;<br>naturally arising and liberated, [it] is like space.<br>Because everything rests upon [it], [it] is like the earth;<br>[it] is exceptionally exalted above all objects. |
| After | Because there is no projection or gathering, [it] is like a great garuḍa;<br>complete in the expressiveness of view, [it] is like a lion.<br>Because [it] pervades with complete depth, [it] is like the ocean;<br>naturally arising and liberated, [it] is like space.<br>Because everything rests upon [it], [it] is like the earth;<br>[it] is exceptionally exalted above all objects. |

- **PD-018**: `སྤྲོ་བསྡུ`; “no elaboration or withdrawal” → “no projection or gathering” (1 occurrence(s)); severity **medium**, confidence **high**. P2 projecting/gathering pair; preserve both source actions and negative scope. Do not replace distinct proliferating-and-gathering or bare elaboration expressions.

#### MTP-000252 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རྒྱུ་ཉིད་རྒྱུ་ཡིས་གྲོལ་བ་ལ<br>འཁོར་འདས་གཉིས་ལང་མི་ལྟོས<br>ཆོས་ནི་ཆོས་ཀྱིས་གྲོལ་བ་ལ<br>ཐ་སྙད་ཚིག་ལ་ང་མི་ལྟོས |
| Before | When the cause itself is liberated through the cause,<br>[there is] no dependence on saṃsāra and nirvāṇa, the two—[retained: ལང].<br>When phenomena are liberated through phenomena,<br>I do not depend on words of designation. |
| After | When the cause itself is liberated through the cause,<br>[there is] no dependence on cyclic existence and transcendence of sorrow, the two—[retained: ལང].<br>When phenomena are liberated through phenomena,<br>I do not depend on phrases of designation. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-025**: `ཚིག`; “words of designation” → “phrases of designation” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000259 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་ས་ཡིན་ཕྱིར་རྒྱུ་རྐྱེན་རྫོགས<br>རང་གིས་རྟོགས་ཕྱིར་ཆོས་ཉིད་རྫོགས<br>རང་ལོག་ཡིན་ཕྱིར་འཁོར་འདས་རྫོགས<br>རང་གནས་ཡིན་ཕྱིར་རྒྱུད་ལུང་རྫོགས<br>རང་རྫོགས་ཡིན་ཕྱིར་དུས་གཅིག་རྫོགས |
| Before | Because [it] is its own place, causes and conditions are complete;<br>because [it] is realized by itself, the nature of phenomena is complete.<br>Because there is self-reversal, saṃsāra and nirvāṇa are complete;<br>because there is self-abiding, tantras and scriptural transmissions are complete.<br>Because there is self-completeness, [it] is complete at one time. |
| After | Because [it] is its own place, causes and conditions are complete;<br>because [it] is realized by itself, the nature of phenomena is complete.<br>Because there is self-reversal, cyclic existence and transcendence of sorrow are complete;<br>because there is self-abiding, tantras and transmissions are complete.<br>Because there is self-completeness, [it] is complete at one time. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-011**: `ལུང`; “scriptural transmissions” → “transmissions” (1 occurrence(s)); severity **medium**, confidence **high**. P2 transmission in teaching/naming contexts. Keep source-supported scriptural at 000197, not as an automatic modifier elsewhere; retain continuum/tantra distinctions and open apposition.

#### MTP-000262 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>རང་རྫོགས་པ་ཆེན་པོའི་ཆོས་སྐུ་ནི<br>ཀ་ནས་དག་པས་དྲི་མ་ཟད<br>ཐོག་མར་བྱུང་བས་བརྒྱུད་པ་ཟད<br>ཟླ་དང་བྲལ་བས་རྩིས་ལས་འདས |
| Before | Emaho!<br>The dharma embodiment of great self-completeness:<br>because [it] is pure from the beginning, stains are exhausted;<br>because [it] arose at the beginning, transmission is exhausted;<br>because [it] is without a counterpart, [it] is beyond reckoning. |
| After | How wondrous!<br>The dharma embodiment of great self-completeness:<br>because [it] is pure from the beginning, stains are exhausted;<br>because [it] arose at the beginning, transmission is exhausted;<br>because [it] is without a counterpart, [it] is beyond reckoning. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000264 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | གཉིས་ཀྱིས་འཕེལ་མེད་ངོ་བོ་ཉིད<br>ཆོས་དང་བྲལ་བས་མཐའ་ལས་འདས<br>རྟོག་མེད་གསལ་བས་འགྱུ་བ་སངས<br>བེམ་རིག་གཉིས་མེད་ཚོགས་གཉིས་རྫོགས |
| Before | The essence itself, not increased by the two,<br>is beyond extremes because [it] is free from phenomena.<br>Clear and free from conceptualization, movement clears;<br>without the two, inert matter and awareness, the two accumulations are complete. |
| After | The essence itself, not increased by the two,<br>is beyond extremes because [it] is free from phenomena.<br>Clear and free from conceptualization, movement clears;<br>without the two, matter and awareness, the two accumulations are complete. |

- **PD-008**: `བེམ་རིག`; “inert matter” → “matter” (1 occurrence(s)); severity **medium**, confidence **medium**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.

#### MTP-000271 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབྲས་བུ་ཡེ་ནས་རང་གནས་པ<br>ཆོས་ཀྱིས་ཡེ་ནས་བཅོས་སུ་མེད<br>གྲུབ་མཐས་ཡེ་ནས་བསྐྱངས་དང་བྲལ<br>དུག་ལྔས་ཡེ་ནས་གོས་པ་མེད<br>འཁོར་བ་འདས་འདུ་འབྲལ་ག་ལ་ཡོད |
| Before | The result abides of itself primordially;<br>primordially, it cannot be contrived through phenomena.<br>Primordially, it is free from being sustained by philosophical tenets;<br>primordially, it is unstained by the five poisons.<br>Where could there be gathering or separation of saṃsāra and nirvāṇa? |
| After | The result abides of itself primordially;<br>primordially, it cannot be contrived through phenomena.<br>Primordially, it is free from being sustained by tenet systems;<br>primordially, it is unstained by the five poisons.<br>Where could there be gathering or separation of cyclic existence and transcendence of sorrow? |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་བ་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-019**: `གྲུབ་མཐས`; “philosophical tenets” → “tenet systems” (1 occurrence(s)); severity **medium**, confidence **high**. P2 tenet systems: actual organized positions and their sustaining function at 000238/000271; remove unsupported philosophical. The expanded 000268 construction stays provisional.

#### MTP-000277 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་བྱུང་འོད་གསལ་བཀོད་རེ་ལེགས<br>གཞི་སྣང་ཆེན་པོ་ཤོངས་རེ་ཆེ<br>འཁོར་འདས་གཉིས་པོ་འབྲེལ་རེ་མཁས<br>སྐུ་ལྔ་ཡེ་ཤེས་བརྩེགས་རེ་ལེགས |
| Before | Naturally arising clear light—how well arranged!<br>Great Ground-appearance—how vast its capacity!<br>The two, saṃsāra and nirvāṇa—how skillfully connected!<br>Five embodiments and primordial knowing—how well arrayed in layers! |
| After | Naturally arising clear light—how well arranged!<br>Great Ground-appearance—how vast its capacity!<br>The two, cyclic existence and transcendence of sorrow—how skillfully connected!<br>Five embodiments and primordial knowing—how well arrayed in layers! |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000278 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་བཞིན་གནས་པའི་ངོ་བོ་ལ<br>སངས་རྒྱས་མེད་ཅིང་སེམས་ཅན་མེད<br>མ་རིག་མེད་ཅིང་འཁྲུལ་པ་མེད |
| Before | In the essence abiding as intrinsic nature,<br>there are no buddhas and no sentient beings;<br>there is no ignorance and no delusion. |
| After | In the essence abiding as intrinsic nature,<br>there are no buddhas and no karmic beings;<br>there is no ignorance and no delusion. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000301 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་ཅན་དེ་དག་སྐྱེ་བ་བཞི |
| Before | those sentient beings [have] four births. |
| After | those karmic beings [have] four births. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000307 — chapter 5

Location: [`chapters/05/translation.md`](chapters/05/translation.md); fixed source: [`chapters/05/source.md`](chapters/05/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ལྟར་འཇིག་རྟེན་གསུམ་པ་ཉིད<br>ཕུང་པོ་ལྔ་དང་དབང་པོ་ལྔ<br>ཡན་ལག་ལྔ་དང་དོན་སྙིང་ལྔ<br>ཡུལ་ལྔ་དང་ནི་ཉོན་མོངས་ལྔ<br>སེམས་ལྔ་ཡིད་ལྔ་རྟོག་པ་ལྔ<br>གཟུང་འཛིན་འཁོར་བ་ཉིད་དུ་གྲུབ |
| Before | Thus, the three worlds themselves—<br>five aggregates and five faculties,<br>five limbs and five vital organs,<br>five objects and five afflictions,<br>five ordinary minds, five mental faculties, five conceptual thoughts—<br>are established as saṃsāra of apprehended object and apprehending subject. |
| After | Thus, the three worlds themselves—<br>five aggregates and five faculties,<br>five limbs and five vital organs,<br>five objects and five afflictions,<br>five ordinary minds, five mental faculties, five conceptual thoughts—<br>are established as cyclic existence of apprehended object and apprehending subject. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000324 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཉོན་མོངས་ལྔ་ཡི་དྲི་མ་ཡིས<br>སེམས་ཅན་ཇི་ལྟར་བཅིངས་པར་འགྱུར<br>བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ལ་གསུངས |
| Before | Through the stains of the five afflictions,<br>how do sentient beings become bound?<br>Bhagavān, speak to me.” |
| After | Through the stains of the five afflictions,<br>how do karmic beings become bound?<br>Blessed One, speak to me.” |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000325 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ |
| Before | The Bhagavān spoke: |
| After | The Blessed One spoke: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000334 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ང་ཉིད་སངས་རྒྱས་དགོངས་པ་ལས<br>འཁོར་བ་ང་ཡིན་མྱང་འདས་ང<br>ཆོས་ཀྱང་ང་ཡིན་ཆོས་མིན་ང |
| Before | I myself, from the enlightened intent of buddhas,<br>am saṃsāra; I am nirvāṇa.<br>I am phenomena; I am non-phenomena. |
| After | I myself, from the enlightened intent of buddhas,<br>am cyclic existence; I am transcendence of sorrow.<br>I am phenomena; I am non-phenomena. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `མྱང་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000337 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྟོན་པ་འཁོར་དང་བསྟན་པ་ང<br>རང་གི་འཁོར་སྡུད་སྡུད་པ་ང<br>ལྟ་དང་སྒོམ་དང་སྤྱོད་པ་ང<br>དབང་དང་དམ་ཚིག་སྡོམ་པ་ང |
| Before | I am the teacher, retinue, and teaching.<br>I am gathering—gathering my own retinue.<br>I am view, cultivation, and activity.<br>I am empowerment, commitments, and vows. |
| After | I am the teacher, retinue, and teaching.<br>I am gathering—gathering my own retinue.<br>I am view, cultivation, and activity.<br>I am empowerment, sacred pledges, and vows. |

- **PD-016**: `དམ་ཚིག`; “commitments” → “sacred pledges” (1 occurrence(s)); severity **medium**, confidence **high**. P2 sacred pledge; preserve contrast with empowerment and vows, transgression/guarding and negative/rhetorical function.

#### MTP-000338 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མཆོད་པ་དང་བསམ་གཏན་ཏིང་འཛིན་ང<br>ཁྲུས་དང་གཙང་སྦྲ་དྲི་མེད་ང<br>དགེ་དང་མི་དགེ་སྤྱོད་པ་ང<br>མདོ་སྡེ་འདུལ་བ་མངོན་པ་ང |
| Before | I am offerings, meditative stability, and deep absorption.<br>I am washing, cleanliness, and stainlessness.<br>I am virtuous and nonvirtuous activity.<br>I am sūtra discourses, discipline, and higher doctrine. |
| After | I am offerings, meditative stability, and deep absorption.<br>I am washing, cleanliness, and stainlessness.<br>I am virtuous and nonvirtuous activity.<br>I am discourse collection, discipline, and higher doctrine. |

- **PD-003**: `མདོ་སྡེ`; “sūtra discourses” → “discourse collection” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.

#### MTP-000344 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མདོར་ན་ཇི་ལྟར་སྣང་བ་ང<br>ང་ནི་མི་འཕམ་ཀུན་ལས་རྒྱལ་བའོ<br>ང་ནི་བཅོས་པའི་ཚིག་མེད་ཀུན་ལས་ཕགས་པ་ཡིན<br>ང་ནི་རྟག་ཆད་ཉིས་མེད་ཀུན་ལྟར་འཇུག་པ་ཡིན |
| Before | In brief, I am however [things] appear.<br>I am undefeated, victorious over all.<br>I have no contrived utterance; I am exalted beyond all.<br>I have neither permanence nor annihilation; I enter in every manner. |
| After | In brief, I am however [things] appear.<br>I am undefeated, victorious over all.<br>I have no contrived phrase; I am exalted beyond all.<br>I have neither permanence nor annihilation; I enter in every manner. |

- **PD-025**: `ཚིག`; “contrived utterance” → “contrived phrase” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000347 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ང་ནི་གནས་པའི་ས་མེད་ཀུན་ལ་བརྟེན་པ་ཡིན<br>ང་ནི་འགྲན་པའི་ཟླ་མེད་ཀུན་ལ་ཉག་གཅིག་གོ<br>ང་ནི་བེམ་རིག་གཉིས་མེད་ཀུན་ལ་ཁྱབ་པ་ཡིན<br>ང་ནི་མུན་པའི་གོས་གྱོན་ཀུན་ལ་སྣང་བ་སྟོན |
| Before | I have no ground on which to abide; I depend on all.<br>I have no rival to compete with; I am unique among all.<br>For me, insentient and aware are not two; I pervade all.<br>I wear the clothing of darkness; I show appearance to all. |
| After | I have no ground on which to abide; I depend on all.<br>I have no rival to compete with; I am unique among all.<br>For me, matter and awareness are not two; I pervade all.<br>I wear the clothing of darkness; I show appearance to all. |

- **PD-008**: `བེམ་རིག`; “insentient and aware” → “matter and awareness” (1 occurrence(s)); severity **medium**, confidence **medium**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.

#### MTP-000350 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ང་ཡིས་མུན་པ་གོས་སུ་གྱོན་པས་དཔའ་བོ་ཆེ<br>ང་ཡིས་འཁོར་འདས་གོམ་གཅིག་བགྲོད་པས་མཆོངས་པ་ཆེ<br>ང་ཡིས་ས་རྣམས་དུས་གཅིག་ནོན་པས་གཟི་བརྗིད་ཆེ<br>ང་ཡིས་ཉི་ཟླ་གདན་དུ་བཏིང་བས་བརྗིད་པོ་ཆེ |
| Before | Having worn darkness as clothing, I am a great hero.<br>Having traversed saṃsāra and nirvāṇa in one stride, my leap is great.<br>Having pressed down the grounds at one time, my majesty is great.<br>Having spread out the sun and moon as a seat, my splendor is great. |
| After | Having worn darkness as clothing, I am a great hero.<br>Having traversed cyclic existence and transcendence of sorrow in one stride, my leap is great.<br>Having pressed down the grounds at one time, my majesty is great.<br>Having spread out the sun and moon as a seat, my splendor is great. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000351 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ང་ལ་འཁོར་འདས་དུས་གཅིག་རྫོགས་པས་བྱ་དང་བྲལ<br>ང་ལ་སྣང་བ་ཐོགས་མེད་ཤར་བས་རང་ཤར་ཉིད<br>ང་ལ་རྟོགས་དང་མ་རྟོགས་མེད་པས་ཡེ་སངས་རྒྱས<br>ང་ལ་རེ་དང་དོགས་པ་མེད་པས་འཁོར་འདས་དུས་གཅིག་རྫོགས |
| Before | Because saṃsāra and nirvāṇa are complete in me at one time, I am free from doing.<br>Because appearance arises unobstructedly in me, [it is] self-arising itself.<br>Because realization and non-realization are absent in me, [I am] primordially buddha.<br>Because hope and fear are absent in me, saṃsāra and nirvāṇa are complete at one time. |
| After | Because cyclic existence and transcendence of sorrow are complete in me at one time, I am free from doing.<br>Because appearance arises unobstructedly in me, [it is] self-arising itself.<br>Because realization and non-realization are absent in me, [I am] primordially buddha.<br>Because hope and fear are absent in me, cyclic existence and transcendence of sorrow are complete at one time. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (2 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (2 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000355 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ལྟར་འཇིག་རྟེན་འཁོར་འདས་ཆོས<br>ཐམས་ཅད་ངོ་བོ་གཅིག་ཉིད་ན<br>སེམས་ཅན་གིས་བཅིངས་པ་ལགས |
| Before | “If, in this way, all worldly phenomena of saṃsāra and nirvāṇa<br>are one in essence,<br>[—] is bound by sentient beings? |
| After | “If, in this way, all worldly phenomena of cyclic existence and transcendence of sorrow<br>are one in essence,<br>[—] is bound by karmic beings? |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000356 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་དག་འཆིང་བར་མི་རིགས་ན<br>ཡང་ན་མ་བཅིངས་དེ་ཉིད་དམ<br>འོན་ཏེ་གཞན་དག་གིས་བཅིངས་སམ<br>བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ལ་སུངས |
| Before | If it is unfitting that those are bound,<br>or is that itself unbound?<br>Or is [it] bound by others?<br>Bhagavān, སུངས to me.” |
| After | If it is unfitting that those are bound,<br>or is that itself unbound?<br>Or is [it] bound by others?<br>Blessed One, སུངས to me.” |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000357 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ |
| Before | The Bhagavān spoke: |
| After | The Blessed One spoke: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000358 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་ཅན་ཉོན་མོངས་ལྔ་ཉིད་ནི |
| Before | “As for sentient beings’ five afflictions, |
| After | “As for karmic beings’ five afflictions, |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000361 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་བཞིན་ཉོན་མོངས་དྲི་མ་མེད<br>རང་བྱུང་རང་བཞིན་ཉིད་ཤེས་ན<br>སེམས་ཅན་འཆིང་བར་ག་ལ་འགྱུར |
| Before | Likewise, [there is] no stain of affliction.<br>If naturally arising intrinsic nature itself is known,<br>how could sentient beings be bound? |
| After | Likewise, [there is] no stain of affliction.<br>If naturally arising intrinsic nature itself is known,<br>how could karmic beings be bound? |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000362 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ཉིད་ལ་ནི་བདེན་བཟུང་ན<br>སངས་རྒྱས་ཉིད་ཀྱང་འཆིང་བར་འགྱུར<br>སེམས་ཅན་རྣམས་ནི་ཅིས་མི་འཆིང |
| Before | If that itself is held as true,<br>even buddhas themselves become bound;<br>why would sentient beings not be bound? |
| After | If that itself is held as true,<br>even buddhas themselves become bound;<br>why would karmic beings not be bound? |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000366 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་བ་ཉིད་ལ་ཡུན་རིང་གནས<br>ཁམས་གསུམ་པ་ཡི་ཁང་པ་རུ<br>མིང་དང་གཟུགས་ཀྱི་བཙོན་པར་ཚུད<br>མ་རིག་ལས་ཀྱི་ལྕགས་ཀྱིས་བསྡམས |
| Before | [one] abides for a long time in saṃsāra itself.<br>In the house of the three realms,<br>[one] enters the prison of name and form,<br>bound with the iron of ignorance and action, |
| After | [one] abides for a long time in cyclic existence itself.<br>In the house of the three realms,<br>[one] enters the prison of name and form,<br>bound with the iron of ignorance and action, |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000367 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་བྱུང་སྒྲོན་མ་ཉིད་དང་བྲལ<br>འཁོར་བའི་མུན་ནག་སྟུག་པོས་གཡོགས<br>འདོད་ཆགས་ལན་ཚའི་རོལ་ཆགས<br>གཏི་མུག་ཞགས་པས་དམ་དུ་བཅིངས |
| Before | separated from the naturally arising lamp itself,<br>covered by the thick darkness of saṃsāra,<br>attached to the ལན་ཚའི་རོལ of desire,<br>bound tightly by the noose of deluded dullness, |
| After | separated from the naturally arising lamp itself,<br>covered by the thick darkness of cyclic existence,<br>attached to the ལན་ཚའི་རོལ of desire,<br>bound tightly by the noose of deluded dullness, |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000378 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | གསང་བའི་བདག་པོ་རྡོ་རྗེ་འཛིན<br>སེམས་ཅན་འཁོར་བ་དེ་དག་ནི<br>རང་གི་རྣམ་རྟོག་གིས་བཅིངས་ཀྱང<br>རང་བཞིན་མེད་པས་གྲོལ་བར་ངེས<br>ཆོས་ཀྱི་དབྱིངས་སུ་མཉམ་པའི་ཕྱིར |
| Before | Lord of Secrets, holder of the vajra!<br>Those sentient beings in saṃsāra,<br>although bound by their own differentiating conceptualization,<br>are certain to be liberated because [it] lacks intrinsic nature,<br>for, in the basic space of phenomena, [they] are even. |
| After | Lord of Secrets, holder of the vajra!<br>Those karmic beings in cyclic existence,<br>although bound by their own differentiating conceptualization,<br>are certain to be liberated because [it] lacks intrinsic nature,<br>for, in the basic space of phenomena, [they] are even. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000380 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་བ་ཆོས་ཀྱི་དབྱིངས་སུ་གྲོལ<br>ཆོས་ཉིད་གཞལ་ཡས་ཟང་ཐལ་ཉིད<br>དོན་དམ་ངེས་མེད་ཡངས་པ་ཆེ<br>ཡེ་ཤེས་འཕྲུལ་གྱི་ལྡེ་མིག་མངའ |
| Before | Saṃsāra is liberated into the basic space of phenomena.<br>The nature of phenomena is immeasurable, unimpeded penetration itself.<br>The ultimate is unfixed, greatly open.<br>[One] possesses the magical key of primordial knowing. |
| After | Cyclic existence is liberated into the basic space of phenomena.<br>The nature of phenomena is immeasurable, unimpeded penetration itself.<br>The ultimate is unfixed, greatly open.<br>[One] possesses the magical key of primordial knowing. |

- **PD-005**: `འཁོར་བ`; “Saṃsāra” → “Cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000384 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་རིག་མཚོན་ཐོགས་དམག་གི་དཔུང<br>ལྟ་སྤྱོད་གཉིས་ལ་ལུས་བརྟེན་ཏེ<br>རྟོག་པའི་ཞགས་པས་འཁོར་བར་བཅིངས |
| Before | an army’s force bears the weapon of self-awareness;<br>the body rests on the two, view and activity;<br>with the noose of conceptual thought, [one] is bound in saṃsāra. |
| After | an army’s force bears the weapon of self-awareness;<br>the body rests on the two, view and activity;<br>with the noose of conceptual thought, [one] is bound in cyclic existence. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000395 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>འདི་ནི་རྫོགས་པའི་སངས་རྒྱས་ཀྱི<br>ངོ་བོ་ཉིད་ལས་མ་གཡོས་པའི<br>མི་འགྱུར་ཆོས་ཉིད་རབ་ཏུ་བརྟན |
| Before | Emaho!<br>This, from the perfectly [awakened] buddhas’<br>very essence, has not moved:<br>the unchanging nature of phenomena, utterly stable. |
| After | How wondrous!<br>This, from the perfectly [awakened] buddhas’<br>very essence, has not moved:<br>the unchanging nature of phenomena, utterly stable. |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000397 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ནས་རྡོ་རྗེ་ཅན་རྣམས་ཀྱིས<br>བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་གསོལ |
| Before | Then those possessing vajras<br>petitioned the Bhagavān in these words: |
| After | Then those possessing vajras<br>petitioned the Blessed One in these words: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000398 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་མ་བཅོམ་ལྡན་རྡོ་རྗེ་འཆང<br>འཇིག་རྟེན་སེམས་ཅན་འདི་ཀུན་གྱི<br>གནས་པའི་ས་ནི་ཇི་ལྟ་བུ<br>འགྲོ་བའི་ལམ་ནི་གང་ལྟར་ལགས<br>འབྲས་བུ་ཇི་ལྟ་བུ་ཞིག་ཐོབ<br>རྡོ་རྗེ་འཆང་གིས་བདག་ལ་གསུངས |
| Before | “Alas, Bhagavān Vajradhara!<br>For all these worldly sentient beings,<br>what is the ground on which they abide like?<br>What is the path along which they go like?<br>What sort of result do they attain?<br>Vajradhara, speak to me.” |
| After | “O Blessed One Vajradhara!<br>For all these worldly karmic beings,<br>what is the ground on which they abide like?<br>What is the path along which they go like?<br>What sort of result do they attain?<br>Vajradhara, speak to me.” |

- **PD-001**: `བཅོམ་ལྡན`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-026**: `ཀྱེ་མ`; “Alas,” → “O” (1 occurrence(s)); severity **low**, confidence **high**. P2 ཀྱེ་མ is direct address here, not lament: the following petition asks about abiding, path and result. O preserves the address without adding grief.

#### MTP-000399 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ |
| Before | The Bhagavān spoke: |
| After | The Blessed One spoke: |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000414 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དབུས་ནང་གནས་ཤིང་རང་བཞིན་གསལ<br>སྤྲོ་བསྡུ་སྨྲ་བསམ་ཡུལ་ལས་འདས<br>བགས་ཀྱིས་རྣམ་པར་རྟོག་པ་བྲལ<br>ཡོད་མེད་མཐའ་གཉིས་རྣམ་པར་གསལ |
| Before | [It] abides within the center, and intrinsic nature is clear;<br>[it] is beyond the objects of proliferating and gathering, speaking and thinking.<br>Gently, [it is] free from differentiating conceptualization.<br>The two extremes of existence and nonexistence are completely clear. |
| After | [It] abides within the center, and intrinsic nature is clear;<br>[it] is beyond the objects of projecting and gathering, speaking and thinking.<br>Gently, [it is] free from differentiating conceptualization.<br>The two extremes of existence and nonexistence are completely clear. |

- **PD-018**: `སྤྲོ་བསྡུ`; “proliferating and gathering” → “projecting and gathering” (1 occurrence(s)); severity **medium**, confidence **high**. P2 projecting/gathering pair; preserve both source actions and negative scope. Do not replace distinct proliferating-and-gathering or bare elaboration expressions.

#### MTP-000419 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་བ་བསྐྱབ་པའི་ཐབས་ཆེན་པོ<br>གསང་བའི་ཡེ་གདངས་འབར་བའི་འོད<br>དེ་ནི་བདེ་ཆེན་ངོ་བོའོ |
| Before | [It is] the great means that rescues saṃsāra,<br>the light blazing with the primordial radiance of secrecy.<br>That is the essence of great bliss. |
| After | [It is] the great means that rescues cyclic existence,<br>the light blazing with the primordial radiance of secrecy.<br>That is the essence of great bliss. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000432 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཆུ་ནི་དངས་སྙིགས་འབྱེད་པར་བྱེད<br>དེ་ཡང་གཉིས་ན་ཆ་མཉམ་སྟེ<br>མདོར་ན་དབང་པོའི་དངས་མ་ཡིན |
| Before | “Water” distinguishes the clear from the sediment.<br>Moreover, in the two the portions are equal.<br>In brief, [it] is the refined essence of the faculties. |
| After | “Water” distinguishes the pure extract from the residue.<br>Moreover, in the two the portions are equal.<br>In brief, [it] is the pure extract of the faculties. |

- **PD-017**: `དངས་སྙིགས`; “the clear from the sediment” → “the pure extract from the residue” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.
- **PD-017**: `དངས་མ`; “refined essence” → “pure extract” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000433 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དཔེར་ན་གསེར་གྱི་ལུ་གུ་རྒྱུད<br>བཟོ་མཁས་ལེགས་པར་བརྒྱུས་པ་ལྟར<br>རིག་པས་ཐམས་ཅད་ཤེས་ཤིང་རིག<br>རྟོག་མེད་འཁོར་བས་གོས་པ་མེད<br>ལུ་གུ་རྒྱུད་ནི་འབྲེལ་ཆགས་སོ<br>བདེ་ཆེན་བུ་ག་རྟོག་མེད་ལམ |
| Before | For example, like a gold chain<br>well strung by a skilled craftsman,<br>awareness knows and is aware of everything.<br>Free from conceptualization, [it] is unstained by saṃsāra.<br>Vajra chains are connected in succession.<br>The opening of great bliss is the path free from conceptualization. |
| After | For example, like a gold chain<br>well strung by a skilled craftsman,<br>awareness knows and is aware of everything.<br>Free from conceptualization, [it] is unstained by cyclic existence.<br>Vajra chains are connected in succession.<br>The opening of great bliss is the path free from conceptualization. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000434 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབྲས་བུ་རྣལ་བ་གཉིས་ཞེས་ཏེ<br>མ་སྨིན་འཁོར་བ་ཉིད་དང་ནི<br>གྲོལ་བྱེད་སྐུ་དང་ཡེ་ཤེས་སོ |
| Before | The result is said to be two རྣལ་བ:<br>unripened saṃsāra itself,<br>and the liberating embodiments and primordial knowing. |
| After | The result is said to be two རྣལ་བ:<br>unripened cyclic existence itself,<br>and the liberating embodiments and primordial knowing. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000440 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མངོན་སྣང་ཡུལ་ནི་འདི་ལྟར་རོ<br>སྐུ་གསུམ་དང་ནི་ཡེ་ཤེས་ལྔ<br>སྟོང་པ་ཉིད་དང་གསལ་བས་ཁྱབ<br>ཐིག་ལེ་འདུ་འབྲལ་མེད་པའི་ཕྱིར<br>ཚིག་མེད་ཉིད་དང་རྗོད་བྱེད་བྲལ |
| Before | The object of manifest appearance is like this:<br>three embodiments and five primordial knowings<br>are pervaded by emptiness and clarity.<br>Because the sphere has no coming together or separation,<br>[there are] no utterances, and [it is] free from what expresses. |
| After | The object of manifest appearance is like this:<br>three embodiments and five primordial knowings<br>are pervaded by emptiness and clarity.<br>Because the sphere has no coming together or separation,<br>[there are] no phrases, and [it is] free from what expresses. |

- **PD-025**: `ཚིག`; “no utterances” → “no phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000452 — chapter 6

Location: [`chapters/06/translation.md`](chapters/06/translation.md); fixed source: [`chapters/06/source.md`](chapters/06/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཞེས་མུ་ཏིག་ཕྲེང་བ་རིན་པོ་ཆེ་གསང་བའི་རྒྱུད་ལས<br>སེམས་ཅན་གྱི་སྣང་བ་ཐབས་ལ་མཁས་པ་བསྟན་པའི་ལེའུ་སྟེ་དྲུག་པའོ |
| Before | Thus, from the precious secret tantra String of Pearls, the sixth chapter, teaching skill in means concerning the appearances of sentient beings. |
| After | Thus, from the precious secret tantra String of Pearls, the sixth chapter, teaching skill in means concerning the appearances of karmic beings. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000455 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་ཅན་རྣམས་དང་འཁོར་འདས་ཆོས<br>གཅིག་གམ་འོན་ཏེ་ཐ་དད་ལགས<br>དེ་ལ་བདག་ནི་ཐེ་ཚོམ་མཆིས<br>བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ལ་གསུང |
| Before | “Are sentient beings and the phenomena of saṃsāra and nirvāṇa<br>one, or are they different?<br>I have doubts about that.<br>Bhagavān, speak to me.” |
| After | “Are karmic beings and the phenomena of cyclic existence and transcendence of sorrow<br>one, or are they different?<br>I have doubts about that.<br>Blessed One, speak to me.” |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000457 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་བའི་ཆོས་ནི་འདི་ལྟ་བུ<br>ཐོག་མ་ཉིད་ནི་འདི་མེད་པས<br>ཡུལ་ལ་འཁྲུལ་པས་བརྟགས་པ་ལྟར<br>སེམས་ཅན་ཡུལ་ལ་སྣང་བའོ |
| Before | “The phenomena of saṃsāra are like this:<br>since this is absent [at] the very beginning,<br>just as imputed through delusion about objects,<br>[they] appear within the domain of sentient beings. |
| After | “The phenomena of cyclic existence are like this:<br>since this is absent [at] the very beginning,<br>just as imputed through delusion about objects,<br>[they] appear within the domain of karmic beings. |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.
- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000476 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རོལ་མོ་འོད་ལྔའི་དཀྱིལ་འཁོར་རྫོགས<br>འཕན་ནི་ཁ་དོག་གསལ་བས་དངས<br>གདུགས་ནི་སྐྱོབ་པ་ཤེས་རབ་གདངས<br>བླ་རེ་མན་ངག་ཆེ་བའི་གནད<br>རྒྱལ་མཚན་རྟོགས་པ་མངོན་སངས་རྒྱས |
| Before | Music is the complete maṇḍala of the five lights.<br>Pennants are colors, limpid through clarity.<br>Parasols are protection, the radiance of discerning knowing.<br>Canopies are the key point of the greatness of pith instructions.<br>Victory banners are realization, manifestly buddha. |
| After | Music is the complete mandala of the five lights.<br>Pennants are colors, limpid through clarity.<br>Parasols are protection, the radiance of discerning knowing.<br>Canopies are the key point of the greatness of pith instructions.<br>Victory banners are realization, manifestly buddha. |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.

#### MTP-000479 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་རྡོ་རྗེ་འཛིན་པ་ལེགས་ཉོན་ཅིག<br>འདས་པ་དཀར་པོའི་ཆོས་རྣམས་ནི<br>ལུས་དང་སེམས་ལ་ཐམས་ཅད་རྫོགས<br>འཁོར་བའི་ཆོས་ནི་འདས་སྟོང་ཕྱིར |
| Before | O holder of the vajra, listen well!<br>The white phenomena of transcendence<br>are all complete in body and ordinary mind.<br>For the phenomena of saṃsāra are [འདས་སྟོང: relation unresolved]: |
| After | O holder of the vajra, listen well!<br>The white phenomena of transcendence<br>are all complete in body and ordinary mind.<br>For the phenomena of cyclic existence are [འདས་སྟོང: relation unresolved]: |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000480 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དཀྱིལ་འཁོར་ལྷ་དང་མཆོད་པ་དང<br>སྔགས་དང་ཕྱག་རྒྱ་ཏིང་འཛིན་དང<br>དབང་བསྐུར་བ་དང་དམ་ཚིག་དང<br>མན་ངག་འབོགས་དང་ཉམས་མྱོང་དང<br>དེ་བཞིན་བསྐྱེད་པའི་རིམ་པ་དང<br>ཐོས་དང་བསམ་དང་སྒོམ་པ་དང |
| Before | maṇḍalas, deities and offerings;<br>mantras, mudrās and deep absorption;<br>empowerment and commitments;<br>bestowal of pith instructions and experiential acquaintance;<br>likewise the generation stage;<br>hearing, reflection and cultivation; |
| After | mandalas, deities and offerings;<br>mantras, seals and deep absorption;<br>empowerment and sacred pledges;<br>bestowal of pith instructions and experiential acquaintance;<br>likewise the generation stage;<br>hearing, reflection and cultivation; |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.
- **PD-016**: `དམ་ཚིག`; “commitments” → “sacred pledges” (1 occurrence(s)); severity **medium**, confidence **high**. P2 sacred pledge; preserve contrast with empowerment and vows, transgression/guarding and negative/rhetorical function.
- **PD-021**: `ཕྱག་རྒྱ`; “mudrās” → “seals” (1 occurrence(s)); severity **medium**, confidence **high**. P2 seal in the generic ritual list, gesture in the explicit limb-turning construction; do not change the whole Mahamudra expression or the bodily gesture at 000148.

#### MTP-000486 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་ཧོ<br>འདི་ཀུན་ཤེས་བྱའི་ཡུལ་དུ་སྣང |
| Before | Emaho!<br>All this appears as the domain of what is to be known: |
| After | How wondrous!<br>All this appears as the domain of what is to be known: |

- **PD-010**: `ཨེ་མ་ཧོ`; “Emaho!” → “How wondrous!” (1 occurrence(s)); severity **low**, confidence **high**. P2 How wondrous! for the full ཨེ་མ་ཧོ exclamation; no added listening imperative.

#### MTP-000487 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སངས་རྒྱས་ཆོས་དང་དགེ་འདུན་དང<br>བསྟན་པ་གནས་དང་འཁོར་དང་དུས<br>ཆོས་སྐུ་ལོངས་སྐུ་སྤྲུལ་སྐུ་དང<br>མདོ་སྡེ་འདུལ་བ་མངོན་པ་ཆེ<br>ཉན་ཐོས་རང་རྒྱལ་བྱང་ཆུབ་སེམས |
| Before | buddha, Dharma and Saṅgha;<br>the teaching, place, retinue and time;<br>dharma embodiment, complete enjoyment embodiment and emanation embodiment;<br>the sūtra collection, Vinaya and great Abhidharma;<br>hearers, solitary victors and [བྱང་ཆུབ་སེམས: identification unresolved]; |
| After | buddha, Dharma and Saṅgha;<br>the teaching, place, retinue and time;<br>dharma embodiment, complete enjoyment embodiment and emanation embodiment;<br>the discourse collection, discipline and great higher doctrine;<br>hearers, solitary victors and [བྱང་ཆུབ་སེམས: identification unresolved]; |

- **PD-003**: `མདོ་སྡེ`; “sūtra collection” → “discourse collection” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `འདུལ་བ`; “Vinaya” → “discipline” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `མངོན་པ`; “Abhidharma” → “higher doctrine” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.

#### MTP-000492 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མཁའ་དང་མཉམ་པའི་ཆོས་དབྱིངས་ལ<br>རིག་པའི་ཡེ་ཤེས་རྣམ་སྣང་བ<br>མྱང་འདས་མཚོན་པའི་ཆོས་དེ་རྣམས<br>ལུས་དང་སེམས་ལ་ཇི་ལྟར་གནས<br>དོན་ཉིད་ངོ་ལ་ཇི་ལྟར་འཆར<br>བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ལ་གསུང |
| Before | “Within the basic space of phenomena, equal to space,<br>primordial knowing of awareness appears in its aspects.<br>Those phenomena that indicate nirvāṇa—<br>how do they abide in body and ordinary mind?<br>How do they arise in the presence of meaning itself?<br>Bhagavān, speak to me.” |
| After | “Within the basic space of phenomena, equal to space,<br>primordial knowing of awareness appears in its aspects.<br>Those phenomena that indicate transcendence of sorrow—<br>how do they abide in body and ordinary mind?<br>How do they arise in the presence of meaning itself?<br>Blessed One, speak to me.” |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.
- **PD-005**: `མྱང་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000496 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རང་རིག་མཆོད་པའི་གནས་འགྱུར་ཕྱིར<br>རང་གི་ལྷར་ནི་རང་ཉིད་ཆེ<br>བསྟི་གནས་ཆེན་པོར་རང་གནས་པས<br>རང་གི་དཀྱིལ་འཁོར་རང་ཉིད་མཆོད |
| Before | Since self-awareness becomes the place of offering,<br>as one’s own deity, one is oneself great.<br>Since one abides oneself in the great abode,<br>one oneself offers to one’s own maṇḍala. |
| After | Since self-awareness becomes the place of offering,<br>as one’s own deity, one is oneself great.<br>Since one abides oneself in the great abode,<br>one oneself offers to one’s own mandala. |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.

#### MTP-000499 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཐམས་ཅད་རང་གི་སྔགས་ཀྱི་ཚིག |
| Before | all are the words of one’s own mantra. |
| After | all are the phrases of one’s own mantra. |

- **PD-025**: `ཚིག`; “words of one’s own mantra” → “phrases of one’s own mantra” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000500 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | བསྐྱོད་ཅིང་བསྒྱུར་བ་རང་ཡིན་པས<br>ཡན་ལག་མ་བསྒྱུར་ཕྱག་རྒྱ་རྫོགས<br>བསམ་པས་ཆོས་ཉིད་སྟོང་ཉིད་རང་སངས་པས<br>རྫོགས་པས་ཏིང་འཛིན་བསྒོམ་དུ་མེད |
| Before | Since moving and turning are oneself,<br>the mudrās are complete without turning the limbs.<br>Since, through thinking, the nature of phenomena—emptiness—is self-purified,<br>through completeness, there is no deep absorption to cultivate. |
| After | Since moving and turning are oneself,<br>the gestures are complete without turning the limbs.<br>Since, through thinking, the nature of phenomena—emptiness—is self-purified,<br>through completeness, there is no deep absorption to cultivate. |

- **PD-021**: `ཡན་ལག་མ་བསྒྱུར་ཕྱག་རྒྱ`; “mudrās” → “gestures” (1 occurrence(s)); severity **medium**, confidence **high**. P2 seal in the generic ritual list, gesture in the explicit limb-turning construction; do not change the whole Mahamudra expression or the bodily gesture at 000148.

#### MTP-000501 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རིག་པའི་རྩལ་དབང་གཞིར་གནས་པས<br>རྫས་ནི་མི་དགོས་དབང་བསྐུར་ཐོབ<br>བསྲུང་བའི་མཚམས་མེད་འདའ་ཉམས་བྲལ<br>ཚིག་བརྗོད་དམ་ཚིག་བསྲུང་ལས་འདས |
| Before | Since empowerment of awareness’s expressiveness abides in the Ground,<br>no material substances are needed: empowerment is attained.<br>There is no boundary to guard, [and there is] freedom from transgression and deterioration;<br>[it is] beyond guarding commitments expressed in words. |
| After | Since empowerment of awareness’s expressiveness abides in the Ground,<br>no material substances are needed: empowerment is attained.<br>There is no boundary to guard, [and there is] freedom from transgression and deterioration;<br>[it is] beyond guarding sacred pledges expressed in phrases. |

- **PD-016**: `དམ་ཚིག`; “commitments” → “sacred pledges” (1 occurrence(s)); severity **medium**, confidence **high**. P2 sacred pledge; preserve contrast with empowerment and vows, transgression/guarding and negative/rhetorical function.
- **PD-025**: `ཚིག`; “expressed in words” → “expressed in phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000502 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྣང་བ་ཉིད་ནི་རང་གྲོལ་པས<br>ཚིག་མཚོན་མན་ངག་རང་རིག་ཀློང<br>རང་ལས་བྱུང་བས་རང་གྲོལ་བས<br>ཉམས་སུ་མྱོང་བའི་ཡེ་ནས་གདིངས |
| Before | Since appearance itself is self-liberated,<br>pith instructions indicated by words are the expanse of self-awareness.<br>Since [it] arises from itself, since [it] is self-liberated,<br>[there is] primordial confidence in experiential acquaintance. |
| After | Since appearance itself is self-liberated,<br>pith instructions indicated by phrases are the expanse of self-awareness.<br>Since [it] arises from itself, since [it] is self-liberated,<br>[there is] primordial confidence in experiential acquaintance. |

- **PD-025**: `ཚིག`; “indicated by words” → “indicated by phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000507 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རིག་པའི་ཡེ་ཤེས་ཡེ་གདངས་པས<br>བསྒོམ་ཞིང་བཅོས་པའི་ཚིག་ལས་གྲོལ<br>འཁོར་འདས་གཉིས་ནི་རང་རྫོགས་པས<br>རིག་སྟོང་རང་གྲོལ་ལྟ་བ་ཆེ |
| Before | Since primordial knowing of awareness is primordially radiant,<br>[it is] liberated from words of cultivating and contriving.<br>Since saṃsāra and nirvāṇa, the two, are complete in themselves,<br>awareness-emptiness, self-liberated, is the great view. |
| After | Since primordial knowing of awareness is primordially radiant,<br>[it is] liberated from phrases of cultivating and contriving.<br>Since cyclic existence and transcendence of sorrow, the two, are complete in themselves,<br>awareness-emptiness, self-liberated, is the great view. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-025**: `ཚིག`; “words of cultivating and contriving” → “phrases of cultivating and contriving” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000528 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | མདོ་སྡེ་ཆོས་ཉིད་ཟབ་མོ་རྟོགས་ལ<br>འདུལ་བ་རང་གི་འཁྲུལ་སྣང་འདུལ<br>མངོན་པ་སེམས་ཉིད་རྟོགས་པར་མངོན |
| Before | The sūtra collection is realization of the profound nature of phenomena;<br>Vinaya subdues one’s own delusory appearance;<br>Abhidharma manifests ordinary mind itself in realization. |
| After | The discourse collection is realization of the profound nature of phenomena;<br>Discipline subdues one’s own delusory appearance;<br>Higher doctrine manifests ordinary mind itself in realization. |

- **PD-003**: `མདོ་སྡེ`; “sūtra collection” → “discourse collection” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `འདུལ་བ`; “Vinaya” → “Discipline” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.
- **PD-003**: `མངོན་པ`; “Abhidharma” → “Higher doctrine” (1 occurrence(s)); severity **medium**, confidence **high**. P2 discipline / discourse collection / higher doctrine in explicit collection contexts; preserve order, great modifier and explanatory verbs.

#### MTP-000539 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཚིག་དང་ཡི་གེ་བརྡར་བཀོད་པའི<br>ཆོས་ལ་དགོས་པ་ཡོད་མ་ཡིན<br>དེ་ཕྱིར་ཆོས་མེད་ལུས་འདི་ལ<br>སེམས་དེ་ཇི་ལྟར་དགོས་པ་འགྱུར |
| Before | for phenomena set out as signs in words and letters,<br>there is no need.<br>Therefore, for this body without phenomena,<br>how could that ordinary mind be needed? |
| After | for phenomena set out as signs in phrases and letters,<br>there is no need.<br>Therefore, for this body without phenomena,<br>how could that ordinary mind be needed? |

- **PD-025**: `ཚིག`; “in words and letters” → “in phrases and letters” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000540 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་དེ་མེད་ན་བེམ་པོས་ནི<br>བསྐྱེད་པར་ནུས་པ་མ་ཡིན་ཏེ<br>མ་བསྐྱེད་དོན་རྣམས་ཇི་ལྟར་འབྱུང |
| Before | If that ordinary mind is absent, insentient matter<br>cannot generate.<br>How can ungenerated meanings arise? |
| After | If that ordinary mind is absent, matter<br>cannot generate.<br>How can ungenerated meanings arise? |

- **PD-008**: `བེམ་པོས`; “insentient matter” → “matter” (1 occurrence(s)); severity **medium**, confidence **high**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.

#### MTP-000541 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ཉིད་དྲན་བསམ་སེམས་མེད་ན<br>དུར་ཁྲོད་རོ་དང་ཁྱད་ཅི་ཡོད<br>ཡང་ན་ནམ་མཁའ་ཇི་བཞིན་ནོ |
| Before | If that itself has no ordinary mind that remembers and thinks,<br>what difference is there from a corpse in a charnel ground?<br>Or [it is] just like space. |
| After | If that itself has no ordinary mind that is mindful and thinks,<br>what difference is there from a corpse in a charnel ground?<br>Or [it is] just like space. |

- **PD-020**: `དྲན་བསམ`; “remembers and thinks” → “is mindful and thinks” (1 occurrence(s)); severity **medium**, confidence **high**. P2 mindfulness and thinking; neither occurrence concerns recollection. Preserve the relative clause/conditional at 000541 and retinue address at 000544; current 000286 already conforms.

#### MTP-000542 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ཉིད་ཡིན་ན་སྟོང་པས་ནི<br>སེམས་ཅན་དོན་ནི་ཇི་ལྟར་འབྱུང<br>དེ་ཉིད་རིགས་པ་མ་ལགས་ན<br>བདག་ལ་གཙོ་བོས་བཀའ་སྩོལ་ཅིག |
| Before | If that is so, how, through emptiness,<br>could benefit for sentient beings arise?<br>If that is not reasonable,<br>chief, grant me your word.” |
| After | If that is so, how, through emptiness,<br>could benefit for karmic beings arise?<br>If that is not reasonable,<br>chief, grant me your word.” |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (1 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000544 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་མེད་དྲན་བསམ་འཁོར་གྱིས་ཉོན<br>སེམས་ནི་འདུས་ཚོགས་འབྱུང་བའི་ཕྱིར<br>དྲི་མ་ཉིད་དང་ཡང་སྔགས་པས<br>ཀུན་གཞི་སྡུད་པའི་སེམས་ལ་སོགས |
| Before | “Retinue of remembering and thinking without ordinary mind, listen!<br>Since ordinary mind arises [from] a gathered collection,<br>a stain itself, and also [སྔགས་པས: construction unresolved];<br>the all-basis—the ordinary mind that gathers—and so forth, |
| After | “Retinue of mindfulness and thinking without ordinary mind, listen!<br>Since ordinary mind arises [from] a gathered collection,<br>a stain itself, and also [སྔགས་པས: construction unresolved];<br>the all-basis—the ordinary mind that gathers—and so forth, |

- **PD-020**: `དྲན་བསམ`; “remembering and thinking” → “mindfulness and thinking” (1 occurrence(s)); severity **medium**, confidence **high**. P2 mindfulness and thinking; neither occurrence concerns recollection. Preserve the relative clause/conditional at 000541 and retinue address at 000544; current 000286 already conforms.

#### MTP-000547 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སེམས་ནི་བག་ཆགས་ཀུན་གྱི་གཞི<br>ལུས་ཅན་རྣམས་ཀྱི་དྲི་མ་ཡིན<br>གཟུང་བ་ཡིན་ལ་འཛིན་པ་ཡིན<br>དེ་ཕྱིར་འཁོར་བའི་ཆོས་ཉིད་དོ |
| Before | Ordinary mind is the Ground of all habitual tendencies,<br>the stain of bodied beings.<br>[It] is apprehended object and apprehending subject.<br>Therefore, [it is] the nature of phenomena of saṃsāra. |
| After | Ordinary mind is the Ground of all habitual tendencies,<br>the stain of bodied beings.<br>[It] is apprehended object and apprehending subject.<br>Therefore, [it is] the nature of phenomena of cyclic existence. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000550 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཐུགས་ནི་བསྐྱོད་པ་ཀུན་བྲལ་བས<br>བེམ་པོ་ལྟ་བུ་མ་ཡིན་ཏེ<br>ཤེས་ཞིང་རིག་ལ་གསལ་བྱེད་སྣང<br>རྣམ་པར་རྟོག་པ་ཀུན་བསྲེགས་ཏེ<br>ཡེ་ཤེས་ཉིད་ནི་མེ་བཞིན་ཟ |
| Before | Since [ཐུགས: unresolved] is free from all stirring,<br>[it] is not like insentient matter.<br>[It] knows and is aware; [it] makes clear and appears.<br>Burning all differentiating conceptualization,<br>primordial knowing itself consumes like fire. |
| After | Since awakened mind is free from all stirring,<br>[it] is not like matter.<br>[It] knows and is aware; [it] makes clear and appears.<br>Burning all differentiating conceptualization,<br>primordial knowing itself consumes like fire. |

- **PD-008**: `བེམ་པོ`; “insentient matter” → “matter” (1 occurrence(s)); severity **medium**, confidence **high**. P2 matter, a mass noun; the abbreviated བེམ་རིག contrast is a source-supported local construction, not a new glossary headword. Preserve non-knowing/knowing contrast in linked notes, not extra adjectives. No assertion of immobility or bodiless karmic beings.
- **PD-022**: `ཐུགས་ནི་བསྐྱོད་པ་ཀུན་བྲལ་བས`; “[ཐུགས: unresolved]” → “awakened mind” (1 occurrence(s)); severity **medium**, confidence **medium**. P2 awakened mind: standalone cognitive/honorific ཐུགས is supported here by knowing, awareness and making clear, contrasted with matter and earlier ordinary mind. This resolves the local lexical gap only; causal and clause attachment remain flagged, unlike the heart/citta location at 000664.

#### MTP-000561 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འབྱུང་ཆེན་ལྔ་བོ་ལུས་སྣང་བས<br>དངས་མའི་འོད་ལྔ་དྲི་མས་བསྒྲིབས<br>ཕྲ་རགས་ལྔ་ནི་ཡུལ་སྣང་བས<br>ཁ་དོག་ལྔ་ཡང་རྡུལ་དང་བཅས |
| Before | Since the five great elements appear as body,<br>the five lights of the refined essence are obscured by stains.<br>Since the subtle and coarse five appear as objects,<br>the five colors, too, are accompanied by dust. |
| After | Since the five great elements appear as body,<br>the five lights of the pure extract are obscured by stains.<br>Since the subtle and coarse five appear as objects,<br>the five colors, too, are accompanied by dust. |

- **PD-017**: `དངས་མ`; “refined essence” → “pure extract” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000566 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཡུལ་དང་ཤེས་པ་རང་ཡལ་བས<br>འབྱུང་བའི་དངོས་མ་འོད་དུ་ཐིམ<br>དེ་ཕྱིར་འབྱུང་བ་དངས་སྙིགས་དབྱེ |
| Before | Since objects and knowing vanish of themselves,<br>the [དངོས་མ: unresolved] of the elements dissolves into light.<br>Therefore, distinguish the refined part and dregs of the elements.” |
| After | Since objects and knowing vanish of themselves,<br>the [དངོས་མ: unresolved] of the elements dissolves into light.<br>Therefore, distinguish the pure extract and residue of the elements.” |

- **PD-017**: `དངས་སྙིགས`; “refined part and dregs” → “pure extract and residue” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000567 — chapter 7

Location: [`chapters/07/translation.md`](chapters/07/translation.md); fixed source: [`chapters/07/source.md`](chapters/07/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཞེས་མུ་ཏིག་ཕྲེང་བ་རིན་པོ་ཆེའི་རྒྱུད་ལས<br>འཁོར་འདས་ཀྱི་ཆོས་ཐམས་ཅད་རང་ལ་རྫོགས་པར་བསྟན་པའི་ལེའུ་སྟེ་བདུན་པའོ |
| Before | Thus, from the precious tantra String of Pearls, the seventh chapter, teaching that all the phenomena of saṃsāra and nirvāṇa are complete in oneself. |
| After | Thus, from the precious tantra String of Pearls, the seventh chapter, teaching that all the phenomena of cyclic existence and transcendence of sorrow are complete in oneself. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་འདས`; “nirvāṇa” → “transcendence of sorrow” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000570 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་ཀྱེ་སྟོན་པ་རྡོ་རྗེ་སེམས<br>གསང་བའི་རྒྱུད་ཀྱི་ཐབས་དང་ནི<br>རང་བཞིན་ཇི་ལྟ་བུ་ཞིག་ལགས<br>བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ལ་གསུང |
| Before | “O, O, teacher, Vajrasattva,<br>what are the means<br>and intrinsic nature of the secret continuum?<br>Bhagavān, speak to me.” |
| After | “O, O, teacher, Vajrasattva,<br>what are the means<br>and intrinsic nature of the secret continuum?<br>Blessed One, speak to me.” |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

#### MTP-000577 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྟོང་པ་རྒྱུ་གཅིག་དངོས་མེད་ཕྱིར<br>དངོས་པོ་ཀུན་གྱི་ཆོས་ལས་འདས<br>དངོས་ཏེ་སྣང་མེད་ཁྱབ་གཅིག་པས<br>ཀུན་གྱི་གཞིར་གྱུར་ངོ་བོ་གཅིག<br>ཁྱབ་བདག་ཉིད་དང་བྱང་ཆུབ་པོ |
| Before | Emptiness is one cause; because [it] lacks material presence,<br>[it] transcends the phenomena of all entities.<br>[དངོས་ཏེ: construction unresolved], without appearance, with a single pervasion,<br>[it] becomes the Ground of all, one essence—<br>the all-pervading lord itself and awakening. |
| After | Emptiness is one cause; because [it] lacks entities,<br>[it] transcends the phenomena of all entities.<br>[དངོས་ཏེ: construction unresolved], without appearance, with a single pervasion,<br>[it] becomes the Ground of all, one essence—<br>the all-pervading lord itself and awakening. |

- **PD-007**: `དངོས་མེད`; “lacks material presence” → “lacks entities” (1 occurrence(s)); severity **medium**, confidence **high**. P2 negative entity family; these empty/clear/entity contrasts do not establish an exclusively material sense. Retain separate exact དངོས་ཏེ uncertainties and all predicates.

#### MTP-000578 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྐྱེ་མེད་དྲན་པ་ཟད་པ་ཡིས<br>ཀ་དག་ཉིད་ཁྱད་པར་ལས<br>སྟོང་ཞིང་སྣང་ལ་སྣང་ཞིང་སྟོང<br>དངོས་ཏེ་དངོས་མེད་ཉིད་ཀྱང་ཡིན |
| Before | [With] non-arising, through the exhaustion of mindfulness,<br>primordial purity itself: from [its] distinction,<br>empty yet appearing, appearing yet empty,<br>[དངོས་ཏེ: construction unresolved], [it] is also absence of material presence itself. |
| After | [With] non-arising, through the exhaustion of mindfulness,<br>primordial purity itself: from [its] distinction,<br>empty yet appearing, appearing yet empty,<br>[དངོས་ཏེ: construction unresolved], [it] is also absence of entities itself. |

- **PD-007**: `དངོས་མེད`; “absence of material presence” → “absence of entities” (1 occurrence(s)); severity **medium**, confidence **high**. P2 negative entity family; these empty/clear/entity contrasts do not establish an exclusively material sense. Retain separate exact དངོས་ཏེ uncertainties and all predicates.

#### MTP-000581 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཁྱབ་བརྡལ་དངོས་མེད་ངོ་བོས་སྟོང<br>དྲི་མ་མེད་ཅིང་མ་འདྲེས་རྫོགས<br>རྟོག་མེད་སྟོང་པའི་རང་བཞིན་ཏེ<br>སྟོང་པས་ཁྱབ་ཕྱིར་རྒྱུད་ཅེས་སོ |
| Before | Pervasively spread, without material presence, empty in essence,<br>stainless, unmixed and complete—<br>free from conceptualization, the intrinsic nature of emptiness;<br>because [it] pervades through emptiness, [it] is called “continuum.” |
| After | Pervasively spread, without entities, empty in essence,<br>stainless, unmixed and complete—<br>free from conceptualization, the intrinsic nature of emptiness;<br>because [it] pervades through emptiness, [it] is called “continuum.” |

- **PD-007**: `དངོས་མེད`; “without material presence” → “without entities” (1 occurrence(s)); severity **medium**, confidence **high**. P2 negative entity family; these empty/clear/entity contrasts do not establish an exclusively material sense. Retain separate exact དངོས་ཏེ uncertainties and all predicates.

#### MTP-000600 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | འཁོར་དང་འདས་པ་གང་གིས་ཀྱང<br>འདི་ཉིད་ཤེས་པ་མ་ཡིན་ཏེ<br>མི་ཕྱེད་རྡོ་རྗེའི་རང་བཞིན་ཅན<br>རང་གི་མཚོན་པའི་གཞི་གཅིག་པའི<br>རང་བཞིན་སྟོང་པ་ཉིད་དུ་གཅིག<br>རྫོགས་པའི་སངས་རྒྱས་བསྐྱེད་པའི་ཡུལ |
| Before | By anything of saṃsāra and transcendence,<br>this itself is not known:<br>endowed with the indivisible intrinsic nature of vajra,<br>of the single Ground of its own indication,<br>[its] intrinsic nature is one in emptiness itself;<br>[it is] the domain that generates complete buddhahood. |
| After | By anything of cyclic existence and transcendence of sorrow,<br>this itself is not known:<br>endowed with the indivisible intrinsic nature of vajra,<br>of the single Ground of its own indication,<br>[its] intrinsic nature is one in emptiness itself;<br>[it is] the domain that generates complete buddhahood. |

- **PD-005**: `འཁོར`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-005**: `འཁོར་དང་འདས་པ`; “and transcendence,” → “and transcendence of sorrow,” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.

#### MTP-000606 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | སྣང་བ་ཐམས་ཅད་རྒྱུད་ཡིན་ཏེ<br>ཐམས་ཅད་ཐམས་ཅད་འབྲེལ་ཞིང་ཆགས<br>རང་བཞིན་ཅིཏྟའི་དཀྱིལ་འཁོར་དུ<br>མ་བསྐྱེད་རྫོགས་པའི་སྙིང་པོ་ཆེ |
| Before | All appearances are continuum;<br>everything connects and attaches to everything.<br>Intrinsic nature: within citta’s maṇḍala,<br>the great core, complete without being generated. |
| After | All appearances are continuum;<br>everything connects and attaches to everything.<br>Intrinsic nature: within citta’s mandala,<br>the great core, complete without being generated. |

- **PD-002**: `དཀྱིལ་འཁོར`; “maṇḍala” → “mandala” (1 occurrence(s)); severity **low**, confidence **high**. P2 mandala spelling, including ordinary plural inflection; no change to the citta/locative construction.

#### MTP-000611 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | གསང་བའི་རྒྱུད་ནི་རྣམ་བཤད་པ<br>ངེས་པས་གཟུང་དུ་ཡོད་པའི་ལུང<br>རང་བཞིན་སྟོང་པ་ཀུན་ཁྱབ་པོ |
| Before | An explanation of the secret continuum:<br>a transmitted teaching that can be held with certainty,<br>intrinsic nature, empty and all-pervading. |
| After | An explanation of the secret continuum:<br>a transmission that can be held with certainty,<br>intrinsic nature, empty and all-pervading. |

- **PD-011**: `ལུང`; “transmitted teaching” → “transmission” (1 occurrence(s)); severity **medium**, confidence **high**. P2 transmission in teaching/naming contexts. Keep source-supported scriptural at 000197, not as an automatic modifier elsewhere; retain continuum/tantra distinctions and open apposition.

#### MTP-000612 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ཡང་བཅུད་ཀྱི་རང་བཞིན་ནི<br>སྙིང་པོ་བསྡུས་པས་དངས་མ་གསུམ<br>གསལ་བ་གསུམ་དང་ཤེས་པས་ཁྱབ |
| Before | Further, the intrinsic nature of quintessence:<br>through gathering the core, [there are] three refined essences,<br>pervaded by three clarities and knowing. |
| After | Further, the intrinsic nature of quintessence:<br>through gathering the core, [there are] three pure extracts,<br>pervaded by three clarities and knowing. |

- **PD-017**: `དངས་མ`; “refined essences” → “pure extracts” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000625 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཨེ་མ་རྡོ་རྗེ་འཛིན་པ་ཉོན<br>དེ་ཉིད་རྣམ་པར་བཤད་པར་བྱ<br>དོན་རྒྱུད་དང་ནི་ཚིག་གི་རྒྱུད<br>དོན་ནི་སྔར་བསྟན་རིམ་པའོ |
| Before | “Ah! Holder of the vajra, listen.<br>That itself is to be explained:<br>the continuum of meaning and the continuum of words.<br>The meaning is the sequence taught before. |
| After | “Ah! Holder of the vajra, listen.<br>That itself is to be explained:<br>the continuum of meaning and the continuum of phrases.<br>The meaning is the sequence taught before. |

- **PD-025**: `ཚིག`; “continuum of words” → “continuum of phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000626 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཚིག་རྒྱུད་རིམ་པ་གསལ་བར་དབྱེ<br>སྤྲོས་པ་གཅོད་བྱེད་འཁོར་བ་ཡི<br>དོན་རྣམས་རྒྱུད་ཀྱིས་འགྲོལ་བར་འགྱུར |
| Before | Clearly distinguish the sequence of the continuum of words:<br>conceptual elaborations are cut off; the meanings of saṃsāra<br>will be unravelled through the continuum. |
| After | Clearly distinguish the sequence of the continuum of phrases:<br>conceptual elaborations are cut off; the meanings of cyclic existence<br>will be unravelled through the continuum. |

- **PD-005**: `འཁོར་བ`; “saṃsāra” → “cyclic existence” (1 occurrence(s)); severity **medium**, confidence **high**. P2 cyclic existence / transcendence of sorrow, including supported compressed domain contrast. Preserve both members, negation, possessives and open syntax. Verbal passed-beyond-sorrow passages stay verbal.
- **PD-025**: `ཚིག`; “continuum of words” → “continuum of phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000630 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | དེ་ལྟར་རྣམ་པར་ཕྱེ་བས་ནི<br>ཚིག་རྒྱུད་གསལ་བར་བྱེད་པའོ<br>དེ་ཡི་དོན་རྣམས་རྣམ་ཕྱེ་བས<br>ངོ་བོ་ཉིད་ཀྱང་མཐོང་བར་འགྱུར<br>རྡོ་རྗེ་འཛིན་པ་ངེས་ཟུངས་ཤིག |
| Before | By distinguishing [them] in that way,<br>the continuum of words is made clear.<br>By distinguishing its meanings,<br>the essence itself will also be seen.<br>Holder of the vajra, hold [this] with certainty. |
| After | By distinguishing [them] in that way,<br>the continuum of phrases is made clear.<br>By distinguishing its meanings,<br>the essence itself will also be seen.<br>Holder of the vajra, hold [this] with certainty. |

- **PD-025**: `ཚིག`; “continuum of words” → “continuum of phrases” (1 occurrence(s)); severity **medium**, confidence **medium**. Part I §8.1 phrase for a formulated verbal unit, tested against the explicit words/phrases distinction at 000234 and the existing contrived phrases at 000266. Scope is these mantra/formulation/meaning-versus-phrase constructions, not every generic speech word or a new shared default.

#### MTP-000633 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རྒྱུད་ཀྱི་དངས་མ་གསུམ་ཤེས་ན<br>རི་གསུམ་རྩེ་མོར་ཕྱིན་པ་འདྲ |
| Before | If [you] know the three refined essences of the continuum,<br>it is like reaching the peaks of three mountains. |
| After | If [you] know the three pure extracts of the continuum,<br>it is like reaching the peaks of three mountains. |

- **PD-017**: `དངས་མ`; “refined essences” → “pure extracts” (1 occurrence(s)); severity **medium**, confidence **high**. P2 pure extract / pure extract and residue; both members and source-supported number preserved, distinct from essence/core/quintessence and unresolved དངོས་མ.

#### MTP-000649 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ལུང་རིག་གསལ་བའི་རྒྱུད་གཉིས་ཀྱིས<br>མེ་ཏོག་ཁ་བྱེའི་ཚུལ་དུ་བཤད |
| Before | The two continua that make transmitted teaching and awareness clear<br>explain in the manner of flowers opening. |
| After | The two continua that make transmission and awareness clear<br>explain in the manner of flowers opening. |

- **PD-011**: `ལུང`; “transmitted teaching” → “transmission” (1 occurrence(s)); severity **medium**, confidence **high**. P2 transmission in teaching/naming contexts. Keep source-supported scriptural at 000197, not as an automatic modifier elsewhere; retain continuum/tantra distinctions and open apposition.

#### MTP-000659 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | ཀྱེ་མ་དྲུག་པ་རྡོ་རྗེ་འཆང<br>རྒྱུད་ཀུན་རིམ་པ་དེ་ལྟར་ན<br>མ་འོངས་སེམས་ཅན་རྣམས་ལ་ཡང<br>རྒྱུད་ཀུན་བསྡོམས་པས་གཅིག་གྱུར་པའི<br>སྙིང་པོ་ཐམས་ཅད་དྲིལ་ནས་ནི<br>སེམས་ཅན་རྣམས་ལ་ཇི་ལྟར་བསྟན<br>རྡོ་རྗེ་འཆང་གིས་བདག་ལ་གསུངས |
| Before | “O, sixth Vajradhara,<br>if the sequence of all continua is like that,<br>also for sentient beings to come,<br>of [what] becomes one through summing all continua,<br>having drawn together the entire core,<br>how should [this] be taught to sentient beings?<br>Vajradhara, speak to me.” |
| After | “O, sixth Vajradhara,<br>if the sequence of all continua is like that,<br>also for karmic beings to come,<br>of [what] becomes one through summing all continua,<br>having drawn together the entire core,<br>how should [this] be taught to karmic beings?<br>Vajradhara, speak to me.” |

- **PD-004**: `སེམས་ཅན`; “sentient beings” → “karmic beings” (2 occurrence(s)); severity **medium**, confidence **high**. P2 karmic being for the complete སེམས་ཅན expression; preserve number and possessives; do not change bodily beings, creatures or ordinary mind.

#### MTP-000670 — chapter 8

Location: [`chapters/08/translation.md`](chapters/08/translation.md); fixed source: [`chapters/08/source.md`](chapters/08/source.md).

| Evidence | Exact content |
| --- | --- |
| Tibetan | རིགས་གསུམ་གྱི་ཁྲོ་བོ་དང<br>སངས་རྒྱས་ཆོས་དང་དགེ་འདུན་དང<br>ལྷ་དང་ལྷ་མ་ཡིན་དང<br>མཁའ་འགྲོ་མ་དཔག་ཏུ་མེད་པ་དང<br>དྲི་ཟར་བཅས་པའི་འཇིག་རྟེན་ཡི་རང་སྟེ<br>བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་ལ་མངོན་པར་བསྟོད་དོ |
| Before | the wrathful ones of the three families; buddhas, Dharma and Saṅgha; deities and asuras; immeasurable ḍākinīs; and the world together with gandharvas rejoiced and openly praised what the Bhagavān had said. |
| After | the wrathful ones of the three families; buddhas, Dharma and Saṅgha; deities and asuras; immeasurable ḍākinīs; and the world together with gandharvas rejoiced and openly praised what the Blessed One had said. |

- **PD-001**: `བཅོམ་ལྡན་འདས`; “Bhagavān” → “Blessed One” (1 occurrence(s)); severity **medium**, confidence **high**. P2 approved full/short Blessed One honorific; retain proper names, descriptive epithets, speakers and case.

### PD-028 affected existing note IDs

Chapter 1 (9 notes; definitions in `chapters/01/translation.md`): `T01-007`, `T01-001`, `T01-015`, `T01-002`, `T01-009`, `T01-012`, `T01-016`, `T01-017`, `MTP-AUDIT-C01-078`.

Chapter 2 (16 notes; definitions in `chapters/02/translation.md`): `T02-001`, `T02-004`, `T02-011`, `T02-012`, `T02-025`, `T02-017`, `T02-018`, `T02-013`, `T02-022`, `T02-020`, `T02-023`, `T02-002`, `T02-005`, `T02-009`, `T02-024`, `T02-014`.

Chapter 3 (17 notes; definitions in `chapters/03/translation.md`): `T03-001`, `T03-012`, `T03-002`, `T03-004`, `T03-021`, `T03-005`, `T03-024`, `T03-006`, `T03-009`, `T03-020`, `T03-010`, `T03-016`, `T03-019`, `T03-023`, `T03-014`, `T03-003`, `T03-015`.

Chapter 4 (38 notes; definitions in `chapters/04/translation.md`): `T04-003`, `T04-001`, `T04-101`, `T04-128`, `T04-130`, `T04-002`, `T04-114`, `T04-131`, `T04-017`, `T04-016`, `T04-129`, `T04-011`, `T04-010`, `T04-008`, `T04-012`, `T04-132`, `T04-115`, `T04-126`, `T04-118`, `T04-124`, `T04-116`, `T04-013`, `T04-108`, `T04-025`, `T04-023`, `T04-103`, `T04-109`, `T04-110`, `T04-111`, `T04-117`, `T04-134`, `T04-006`, `T04-021`, `T04-024`, `T04-135`, `T04-004`, `T04-005`, `T04-019`.

Chapter 5 (46 notes; definitions in `chapters/05/translation.md`): `T05-001`, `T05-L025`, `T05-L001`, `T05-003`, `T05-007`, `T05-023`, `T05-005`, `T05-L018`, `T05-049`, `T05-028`, `T05-008`, `T05-010`, `T05-012`, `T05-037`, `T05-013`, `T05-021`, `T05-L036`, `T05-014`, `T05-L014`, `T05-L029`, `T05-L013`, `T05-L003`, `T05-009`, `T05-L010`, `T05-L012`, `T05-L028`, `T05-033`, `T05-024`, `T05-L016`, `T05-035`, `T05-029`, `T05-032`, `T05-L038`, `T05-038`, `T05-044`, `T05-045`, `T05-046`, `T05-047`, `T05-048`, `T05-L039`, `T05-016`, `T05-026`, `T05-030`, `MTP-AUDIT-C05-388`, `MTP-AUDIT-C05-162`, `MTP-AUDIT-C05-258`.

Chapter 6 (41 notes; definitions in `chapters/06/translation.md`): `T06-001`, `T06-L006`, `T06-049`, `T06-L001`, `T06-005`, `T06-048`, `T06-036`, `T06-037`, `T06-L013`, `T06-006`, `T06-L004`, `T06-L008`, `T06-032`, `T06-007`, `T06-008`, `T06-040`, `T06-L012`, `T06-L014`, `T06-042`, `T06-009`, `T06-011`, `T06-029`, `T06-012`, `T06-046`, `T06-015`, `T06-016`, `T06-025`, `T06-020`, `T06-021`, `T06-L011`, `T06-028`, `T06-026`, `T06-027`, `T06-L009`, `T06-030`, `T06-038`, `T06-017`, `T06-018`, `T06-044`, `T06-013`, `T06-031`.

Chapter 7 (47 notes; definitions in `chapters/07/translation.md`): `T07-001`, `T07-024`, `T07-055`, `T07-070`, `T07-034`, `T07-015`, `T07-057`, `T07-002`, `T07-020`, `T07-069`, `T07-062`, `T07-042`, `T07-051`, `T07-066`, `T07-028`, `T07-018`, `T07-033`, `T07-068`, `T07-012`, `T07-041`, `T07-004`, `T07-005`, `T07-025`, `T07-007`, `T07-043`, `T07-040`, `T07-017`, `T07-010`, `T07-011`, `T07-013`, `T07-016`, `T07-027`, `T07-029`, `T07-030`, `T07-044`, `T07-019`, `T07-021`, `T07-046`, `T07-036`, `T07-045`, `T07-031`, `T07-052`, `T07-049`, `T07-059`, `T07-053`, `T07-061`, `T07-054`.

Chapter 8 (54 notes; definitions in `chapters/08/translation.md`): `T08-001`, `T08-019`, `T08-002`, `T08-011`, `T08-006`, `T08-003`, `T08-004`, `T08-021`, `T08-005`, `T08-012`, `T08-015`, `T08-018`, `T08-007`, `T08-023`, `T08-013`, `T08-020`, `T08-022`, `T08-024`, `T08-010`, `T08-025`, `T08-042`, `T08-026`, `T08-027`, `T08-028`, `T08-030`, `T08-031`, `T08-032`, `T08-029`, `T08-035`, `T08-038`, `T08-037`, `T08-039`, `T08-041`, `T08-033`, `T08-040`, `T08-045`, `T08-046`, `T08-050`, `T08-051`, `T08-057`, `T08-056`, `T08-060`, `T08-061`, `T08-063`, `T08-068`, `T08-067`, `T08-066`, `T08-064`, `T08-065`, `T08-047`, `T08-049`, `T08-052`, `T08-054`, `T08-059`.

**Pre-edit state:** all review inputs and original English still unchanged. Recorded plan: **134 changed pairs, 189 replacement records / 195 occurrences, 27 English finding groups plus PD-028 note/usage status reconciliation**. These counts describe edits and coverage, not accuracy. Next: apply only this recorded plan, regenerate dependent working views, self-check the repaired clauses and run the actual validators/builds.

## Actual validation observations

Baseline commands run by this session, before English or note edits:

| Command | Actual result |
| --- | --- |
| `python3 -B scripts/validate_paired.py` | FAIL: `PAIRED VALIDATION FAILED: invalid pair metadata for M` (0.048 s). Pre-existing generic-parser failure. |
| `python3 -B scripts/validate_translation_aggregate.py` | FAIL: `Prior released input changed: glossary/expanded_tibetan_english_glossary.csv` (1.705 s). Pre-existing policy/release-pin incompatibility. |
| `python3 -B scripts/build_golden_aggregate.py verify` | FAIL: `ModuleNotFoundError: No module named pyewts` (0.191 s); system Python environment, not evidence of changed Tibetan. |

No semantic regression fixture is claimed run from reading the standard. Further tests, changed-clause self-checks, generated-output reproduction and remote verification are pending.

## Release identities frozen at review start

The following remote tag objects and peeled commits were observed with `git ls-remote --tags origin`; no tag is created or moved by this task.

```text
d56fe35ef78cc31c52696c9c8c29e77790ac04d9	refs/tags/golden-ch01-v1
405bd61c6afac6cded17f70a9b661eae028f8fa9	refs/tags/golden-ch01-v1^{}
b72c8dffc1edc477a4daf371306a26a0d3242ba0	refs/tags/golden-ch02-v1
4bd85fee1d157380051acf97a7614fc3c4d16519	refs/tags/golden-ch02-v1^{}
1fb0a8c8146710f6e943bb736d1c193171641f63	refs/tags/golden-ch03-v1
2ede3f022d1af504d3c75942d2280896f590aad9	refs/tags/golden-ch03-v1^{}
c693ad02281629367569405d6ba9037e8121168c	refs/tags/golden-ch04-v1
7c1da84cc1d0de731a517957d7a6b62a176a5a3f	refs/tags/golden-ch04-v1^{}
ea9cc55c97e89f2133889799fdba2ca6c2ed89cc	refs/tags/golden-ch05-v1
916131f5a1eed2ce3dcc4eeb56af098f173fc8bd	refs/tags/golden-ch05-v1^{}
9a70b49dd2282111d14021b3efd525f61f3ac6e0	refs/tags/golden-ch06-v1
3ba32292c566d225bcd57394a6d454f81aafc033	refs/tags/golden-ch06-v1^{}
a0a8d3dfe2d497f0cfd2b5a7cc5107dca68eff70	refs/tags/golden-ch07-v1
0129fc7224d0af8379051716abd7b05265c5ddf9	refs/tags/golden-ch07-v1^{}
3391bb302e11092f0d3e400113a8707ca25c5d95	refs/tags/golden-ch08-v1
360c900eeb8eb5b5c4b451901403d7a4f6c2920f	refs/tags/golden-ch08-v1^{}
2dda46d0a11ee533a30dec1e196f506307a4957f	refs/tags/golden-v1
4d6ba07e1b3379183633127cd387d98d8195eb95	refs/tags/golden-v1^{}
601ee9f11790e19fa52ff2269595b2d1a829032f	refs/tags/translate-ch01-v1
2a25fd13805628a76aadea614bfc7fd7248cd392	refs/tags/translate-ch01-v1^{}
ac905d8e9e2c085a9172cf560d13bdaf0d5c5d80	refs/tags/translate-ch02-v1
3cbe657cea281992123ccb85e0008e306e9d3108	refs/tags/translate-ch02-v1^{}
238c498de680dc12a8bf3465925b6ab82e9a1448	refs/tags/translate-ch03-v1
bd235b87322eb84718930c56e92d4bbe7c198a11	refs/tags/translate-ch03-v1^{}
3920988c3829b5f313c2c6ebc09dcc3a0edf78cc	refs/tags/translate-ch04-v1
7c5f10610915ee029837c866c9b33835962d924d	refs/tags/translate-ch04-v1^{}
f2338c31f8f60e612a3a3ff48499ca29f0cbd6ff	refs/tags/translate-ch05-v1
23cb6d38ba494dd8f53f22c6618168cd50761782	refs/tags/translate-ch05-v1^{}
896ac288c08b29c80458621c22a49a123e2b6227	refs/tags/translate-ch06-v1
713aa49a269ce42ac505bd8dff0299c6946bbdfa	refs/tags/translate-ch06-v1^{}
b88926a22f750ac23475d42475681e0b0b53ae99	refs/tags/translate-ch07-v1
3fae729775f57b100c785cb7ed5c23340524d3ae	refs/tags/translate-ch07-v1^{}
cb4ab7f12468fe3e3ec2294e4b24a4b5b242187e	refs/tags/translate-ch08-v1
71480071296de443e80f82216c464c558001e7c1	refs/tags/translate-ch08-v1^{}
ad131e1d06c582c1032808a61168548821c2790c	refs/tags/translation-v1
f9839a3caa0d1920f596c12bc796adae4c58b39b	refs/tags/translation-v1^{}
```

## Continuation and disposition

Continue chapter 1 active-note reconciliation, then source-order pair 000031 through 000674. Whole-work terminology concordance, continuous English check, supported repairs, note/usage dispositions, reader regeneration and final verification remain. **Review coverage is partial; text readiness is not yet assessed.** This is not human certification or a harmonization claim for the other three works.

---

The following historical release review is preserved verbatim; its approval applies only to its recorded fixed inputs, not to subsequent Phase D edits.

# Coordinator final review — translation-v1

Date: 2026-10-04. Reviewer and release coordinator: `/root`.

Approved for the bounded annotated working-edition release at build-manifest SHA-256 `7a4693c3eaffa12d94af78a147a7289d9701c4061ad41fbb0532ebbc9a604a07`. All eight chapter translations and their actual fixed releases are present. This approval covers faithful assembly and publication of the separately reviewed chapters, with inherited uncertainties retained.

## Exact scope and evidence

The edition represents all 2,053 fixed golden objects in 674 pairs, with 2,597 endnotes and all 2,199 required source obligations. Nothing remains to draft within the eight-chapter scope. Pair dispositions remain 407 translated, 140 unresolved and 127 nontranslatable; representation does not imply that uncertain wording has been resolved.

I read the complete independent assembly review and its machine check record. Reviewer `/root/ch04_structure` verified the complete source/pair/note/obligation identity, all eight fixed chapter inventories and release identities, the 369 bound inputs, and all English and bilingual display projections. Its declared reader sample comprises 63 pair treatments, including 31 bilingual treatments and 15 note definitions. This independent assembly review is distinct from the chapter translators' own checks and from my coordinating signoff.

I inspected the aggregate opening, the corrected bilingual title MTP-000005, the final narrative MTP-000668–670, the work colophon, both post-work annotations and the triple blessing MTP-000671–674. I also read the actual aggregate definitions T02-005, CH02-G000117, T04-008, T04-010, T08-066 and T08-068. The exact source qualifications, provisional syntax, received colophon number and unresolved mother/child grouping remain explicit. Chapter 4's fresh reviewed corrections are included through its fixed release; its original author archive remains preserved.

Two aggregate-only presentation findings were corrected before approval: visible bilingual verse/headings/source roles, and the two-line Tibetan h2 title displayed as one heading. For the final correction I checked the code diff, the actual heading and manifest delta. Only the builder input and that one bilingual display changed; the other 368 inputs and complete English, machine and coverage outputs remain exact. Canonical and signed chapter strings were not rewritten.

## Validation and publication boundary

The actual aggregate passes read-only reproduction. The same final validator used for approval first rejected the real unsigned candidate with “Unsigned translation aggregate: final signoff missing”; that record binds this manifest. The new approval/hash-binding gate has 17 recorded passing synthetic tests and an independent code review. The affected aggregate suite passes all 24 tests on its single retry. Its initial setup-only failure, unreproduced diagnostic and successful retry are recorded transparently; no source pin or gate was relaxed. These structural tests do not certify translation semantics.

Fresh remote observations independently match all eight annotated chapter tag objects and peeled commits, the fixed golden tag and the observed main commit. The publication gate will repeat this remote check against the clean committed signoff state before creating `translation-v1`. A verified receipt will follow the fixed tag; the tag will not move. This review does not claim that those subsequent publication actions have already occurred.

## Remaining qualifications

The active glossary, translation standard and governing golden text remain fixed. Proposed terminology remains inactive. This is an agent-produced working edition for human review, with 140 unresolved pairs and 101 preserved source uncertainty statements. The aggregate review adds no fresh whole-book semantic certification, native-image proofreading, commentary decipherment, exhaustive witness collation or independent human certification. The separate chapter reviews and explicit local notes define the scope of the language and source work already performed.

No assembly correction blocker remains. The signoff binds this review, the exact manifest and outputs, the independent review records, the actual unsigned rejection, remote observations, test records and the executing final validator.

## Repair application checkpoint — chapters 1–4

The pre-recorded plan was applied to 46 pairs and 80 existing note definitions in chapters 1–4, with corresponding existing usage/proposal/current-note dispositions. The source, pair IDs, note IDs/order/allocation and historical approvals are unchanged. Current authored-English policy pins now identify the adopted policy. Chapters 5–8 and dependent working views are pending; no release or final self-verification is claimed at this checkpoint.

## Repair application checkpoint — chapters 5–8

The remaining recorded repairs were applied. Whole-work totals are now **134 English pairs, 268 existing note definitions, 318 existing usage records and 197 existing proposal dispositions**. Source text, IDs/order, note links and historical approvals remain unchanged. MTP-000550 remains unresolved with a more precise reason after its lexical repair. Dependent working-reader generation and changed-clause self-verification are next; coverage is complete but readiness is not being inferred from that count.

## PD-029 — portable review links (recorded before repair)

The 268 newly appended note dispositions currently link to `../../FINAL-REVIEW.md#phase-d-review`, which resolves from a chapter directory but not from the assembled `paired/translation.md` or whole-book readers. Replace only those new links with the absolute repository review-branch report URL so the same canonical note works in every projection. Before: `(../../FINAL-REVIEW.md#phase-d-review)`. After: `(https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/blob/review/phase-d-20261005/translations/FINAL-REVIEW.md#phase-d-review)`. Locations: the 268 existing note IDs already inventoried under PD-028. Classification: presentation/link correctness; severity low; confidence high. No root English, Tibetan, note ID or source allocation changes.

## Working-view build scope

Existing release builders reject changed chapter English and adopted policy pins by design. Preserve those gates and signatures. A separate explicit working-review command will reuse their parser, segmentation, source-audit, note/status, sequence-validation and Markdown-rendering functions, with fixed golden/source/segmentation checks and current English policy pins. It must regenerate chapter and aggregate projections from authored chapter English, never certify or republish a release, and label old release links as historical. Existing `translation-v1` and chapter tags remain the immutable release history; the current files are a working revision of that edition.

## Changed-clause self-check and continuous-English verification — completed

This reviewer re-read **all 134 repaired pairs against their exact Tibetan** after application, including the necessary clauses preserved in the before/after ledger. The self-check covered the honorific/possessive and speaker repairs, mass-noun agreement at 000174, abbreviated matter/awareness relations, core versus essence, negative-entity scope, complete quintessence/pure-extract components, nominal versus verbal sorrow-transcendence, the projected/gathered pair, contextual gesture/seal distinctions, mindfulness/thinking relative-clause grammar, the locally supported awakened-mind label at 000550, and all provisional §8.1 family repairs. No additional omission, agent, causal connector, changed negation/number, lost approved component or unsupported certainty was found in those repairs. Open relationships explicitly identified in the report remain open; this does not certify every provisional interpretation.

The current English was then read continuously, in order, through **MTP-000001–MTP-000674**, including the opening quoted discourse, cross-page syntax, intentional component explanations, school/epithet differences, the interrupted chapter-five colophon, chapter-eight petition/response/narrative transitions, two source notices and triple blessing. No further demonstrable repair was found without deciding the already flagged constructions or imposing a new literary style. Fragments and repetitions that represent the fixed source or an explicit unresolved span were retained.

**This is the reviewer’s self-check of their own corrections, not a second independent review.** The original-text review was independent of all listed authoring runs. Neither stage is final human certification. The exact-edit check also confirmed that the other **540 English pair bodies are unchanged**, every original note’s prose is retained before the dated addition, and the new review links resolve consistently from all generated projections.

## Working-build and initial regression results

The working build regenerated **46 existing dependent files** from authored chapter English, representing all **674 pairs, 2,053 golden objects, 2,597 notes and 2,199 covered source obligations**, with **140 explicitly unresolved pairs**. The existing native-audit evidence is structurally verified and preserved, not claimed newly inspected. `scripts/test_review_working_text.py`: **17 tests passed** against the actual current corpus, including changed Tibetan/English/role/format/object, missing/reordered/duplicate pair and note mutations, protected-byte/policy drift, all-output reproduction, portable note links, local Markdown file links and non-release labeling. Mutation tests use in-memory copies or mocked expected bytes; they do not alter repository sources or tags. These are not the standard’s 63 documented semantic examples.

` .venv/bin/python -B scripts/build_golden_aggregate.py verify` passed (`Verified golden-v1: 8 chapters, 2053 objects`). The initial system-Python failure was the missing pyewts dependency, not changed source. The original pipeline regression suite passed **36 tests**. The first legacy aggregate-suite attempt exceeded the explicit 180-second execution limit; the complete 24-test retry passed in four isolated groups of six tests each. Further final results and remote closure will be appended below. No timed-out run is counted as a pass.

## Final actual validation and preservation results

| Check executed | Actual result |
| --- | --- |
| `scripts/review_working_text.py build` and read-only `verify` under the repository virtual environment | PASS. All 46 existing dependent files regenerated and reproduced: 674 pairs, 2,053 objects, 2,597 notes, 2,199 covered source obligations, 140 unresolved pairs. No formal-release approval is asserted. |
| `scripts/test_review_working_text.py` | PASS: 17 tests on the actual reviewed corpus, including mutation rejection, output reproduction, note identity/portable links, local file links and unapproved-working labels. |
| `scripts/test_translation_pipeline.py` | PASS: 36 tests. |
| `scripts/test_translation_aggregate.py` | PASS: all 24 distinct tests on retry in four isolated groups of six. The first serial run hit its explicit 180-second execution limit and is not counted as a pass. |
| `scripts/test_translation_aggregate_signoff.py` | INCOMPLETE TEST RUN: reached the explicit 180-second execution limit. Partial progress was printed, but the suite has no passing completion result and is not claimed passed. |
| `scripts/test_translation_draft_continuation.py` | INCOMPLETE TEST RUN: reached the explicit 180-second execution limit. Partial progress was printed, but the suite has no passing completion result and is not claimed passed. |
| `.venv/bin/python -B scripts/build_golden_aggregate.py verify` | PASS: golden-v1, eight chapters, 2,053 objects. The earlier system-Python attempt failed because pyewts was absent; the repository virtual environment supplies it. |
| `scripts/validate_paired.py` | Pre-existing FAIL: `invalid pair metadata for M`. Reproduced after review; the existing generic parser was not changed. Current chapter/aggregate structure and pair coverage pass the working validator using the established translation parser. |
| `scripts/validate_translation_aggregate.py` | Pre-existing release-pin rejection: `Prior released input changed: glossary/expanded_tibetan_english_glossary.csv`. Adoption already caused this at review start. The release gate and old approvals remain intact; the explicitly unapproved working builder is not represented as release approval. |
| Frozen-input and history checks | PASS: 95 protected files byte-identical to the frozen input, all 18 remote annotated release tag identities unchanged, source/pair/note allocations unchanged, historical note/proposal/approval fields preserved. |
| Exact edit and status checks | PASS: 134 bodies match the pre-recorded repair plan, 540 bodies unchanged, 268 expected note additions, 318 usage and 197 proposal dispositions; all 140 unresolved pair IDs/statuses retained. |
| Deterministic working rebuild and verification | PASS: the same 46 generated file hashes before and after another build, followed by read-only verification. |
| `git diff --check` | NOT a default pass: the interrupted commit attempt returned exit 2 for renderer-generated Markdown trailing whitespace. At landing verification, 2,943 changed lines were flagged. The command-local Markdown-aware check `git -c core.whitespace=-blank-at-eol diff --check` passes; meaningful verse hard breaks and fixed source bytes are preserved. No repository/global Git configuration or release gate was changed. |

The semantic regression examples documented in the standard were **not executed as a separate semantic fixture suite**. Reading them and testing structural invariants is not counted as testing those examples. The two timed-out ancillary legacy suites remain a bounded validation limitation, not unreviewed translation ranges. No CI workflow is configured in this repository, so no hosted-CI success is claimed.

## Final handoff and remaining bounded decisions

The complete review and corrected working text are ready for owner inspection through the review branch/pull request, not for an automatic new release. The next decisions are the existing exact unresolved spans/source-layer questions, the local provisional constructions, and the grouped shared terminology proposals in this report. Shared reconciliation is still required for deluded dullness, meditative stability, phrase, luster, the paired superficial/superfactual proposal, an English Tathāgata honorific, and the serum/lymph bodily-fluid question. The different thugs/citta constructions, title verb, abbreviated matter/awareness contrast and technical-versus-support Ground uses remain construction questions, not silently promoted shared headwords.

No source emendation, segmentation change, release tag creation/movement, approval-history rewrite, force-push, human certification or four-work harmonization claim is part of this task. Verification of this reviewer's own repairs is a self-check only. The independent review of the original authoring runs and that repair self-check remain separately identified.

## Main-integration continuation — 2026-10-05

The owner explicitly required the complete package to land in `main`. This continuation completes delivery of the already reviewed text; it is not a second semantic review or a new translation. The current remote review head was verified as `377d848848be6bf95f682965d0db226c4188195c`, with the chapters 5–8 repair commit `2b30952e5ee7a9576a0741cc76262721c436522b`. These actual Git identities supersede the incorrect hashes in the earlier chat summary. Remote main remained `46110acd02a6caa14a00f91605c1a478eda72bcd`, an ancestor of the review branch; no conflicting remote work or active rulesets were found.

Before synchronization or further changes, all 62 pending files were captured without changing the normal index or working files on recovery branch `recovery/phase-d-working-20261005-main-landing`, commit `393d7dc36e1e73e88e0d8f4b6d03604a869ee380`. The final saved package is staged explicitly. Publication uses an ordinary non-force review-branch checkpoint and pull request to `main`; no release tag or historical approval is created or modified. The existing review branch is retained so its portable note URLs continue to resolve.

Fresh landing checks: read-only working verification **PASS** for all 46 dependent files; working-view regression suite **17/17 PASS**; existing pipeline suite **36/36 PASS**; fixed-golden read-only validation **PASS**, eight chapters and 2,053 anchors. An independent mechanical comparison with the pre-edit evidence ledger confirms all **134** repaired bodies exactly match their recorded after-text, the other **540** bodies are unchanged, all **2,597** original note bodies and their reference sequences are preserved, and only the expected **268** notes have appended dispositions. This is a reproducibility/integrity check, not independent semantic certification. All historical usage/proposal fields are unchanged apart from the recorded 318/197 added dispositions; all 140 unresolved IDs/statuses remain. Fixed source, golden, diplomatic, edition, evidence, glossary and guideline trees, AGENTS.md and FORMAT.md have no changes from the frozen review input. All 36 remote tag/peeled-ref entries (18 annotated releases) match the frozen inventory.

The previous unconditional whitespace-check PASS was incorrect and is corrected in the table above. The actual earlier terminal output shows a `git diff --check` failure before commit; it must not be represented as a successful final checkpoint or solely a missing terminal session. The supported Markdown rendering is retained, using a command-local whitespace setting for the checkpoint. Other prior test results and explicitly incomplete legacy suites retain their recorded scope. No additional English/source-body change was made during this integration continuation.
