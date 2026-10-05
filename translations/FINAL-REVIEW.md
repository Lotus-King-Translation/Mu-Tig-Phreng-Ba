<a id="phase-d-review"></a>
# Post-translation review — Phase D

**State: in progress; not text-ready or a release approval.** Date: 2026-10-05. Reviewer/session: **GPT-6 Astra Pro / MTP-PhaseD-20261005**. This session is independent of the prior authoring runs listed below. Verification of repairs made by this session is a **self-check**, not a second independent review. Git commits use the repository owner’s configured identity; that is not a claim of human language certification.

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
| 1 | `MTP-000001`–`MTP-000030` | 30 | 97 | 112 | 1 | `translation author /root/golden_triage` / `coordinating agent /root` | 000001–000030, all pairs and 112 active notes read; repairs pending |
| 2 | `MTP-000031`–`MTP-000065` | 35 | 124 | 175 | 4 | `/root/ch02_translate` / `/root/ch02_qc` | 000031–000065, all pairs and 175 active notes read; repairs pending |
| 3 | `MTP-000066`–`MTP-000099` | 34 | 120 | 165 | 2 | `/root/ch02_translate` / `/root/ch02_qc` | 000066–000099, all pairs and 165 active notes read; repairs pending |
| 4 | `MTP-000100`–`MTP-000185` | 86 | 294 | 396 | 5 | `/root/ch04_author` / `/root/ch04_qc` | 000100–000185, all pairs and 396 active notes read; repairs pending |
| 5 | `MTP-000186`–`MTP-000320` | 135 | 416 | 520 | 16 | `/root/ch05_translate` / `/root/ch05_qc` | 000186–000320, all pairs and 520 active notes read; repairs pending |
| 6 | `MTP-000321`–`MTP-000452` | 132 | 376 | 435 | 21 | `/root/ch06_translate` / `/root/ch06_qc` | Not yet reviewed |
| 7 | `MTP-000453`–`MTP-000567` | 115 | 342 | 373 | 45 | `/root/ch07_translate` / `/root/ch07_qc` | Not yet reviewed |
| 8 | `MTP-000568`–`MTP-000674` | 107 | 284 | 421 | 46 | `/root/ch08_translate` / `/root/ch08_qc` | Not yet reviewed |

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
