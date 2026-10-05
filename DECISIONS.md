# Project-owner decisions

## 2026-10-02 — Create project and find editions

The user selected String of Pearls and instructed: “start by creating the new repository, and then finding every possible edition for string of pearls.” This authorizes repository creation from the Tibetan text template and broad source discovery/acquisition. It does not select a governing witness or start golden-edition or translation work.

Repository slug `Mu-Tig-Phreng-Ba` and work code `MTP` are implementation choices, not claims of separately approved terminology.

## 2026-10-02 — Create the golden edition

The user instructed: “excellent. So next, create the golden edition.” This authorizes editorial preparation, correction against the governing source, validation and publication of the golden Tibetan edition. Translation remains a later phase.

The coordinator explicitly selects Adzom/Sanje Dorje1973–77 (W1KG892, I1KG895, printed417–537) as governing scan and the preserved Tibetan Wikisource rendition as electronic base. The Wylie rendition is a same-family electronic comparator; Adzom2000 is a same-print reference. Selection rationale and limits are recorded in diplomatic/GOVERNING-WITNESS.json. This is an editorial choice within the authorized task, not a representation that the user specified the exemplar.

Eight bounded chapter releases will preserve all original anchors, scan-supported decisions, separate restorations/layers and explicit uncertainty. This does not authorize eclectic smoothing, Sanskrit reconstruction without scan evidence, unrecorded punctuation changes or claims of exhaustive collation.

## 2026-10-02 — Translate the fixed golden edition with Adzom endnotes

The user instructed: “Now translate the golden edition, but mark to endnotes in the translation every time the golden edition is different from adzom and how.” This authorizes the complete English working translation of `golden-v1`, source-linked endnotes, necessary comparison with the governing Adzom scans, terminology-controlled drafting, separate QC, and repository publication.

The fixed Tibetan remains unchanged. The 30 recorded transcript corrections restore the Adzom reading and must not be mislabeled as departures from the print. Actual golden-versus-print differences and omissions, transcript corrections, source-layer/display choices, and unresolved source readings receive distinct note categories. To meet the new completeness requirement, a page-by-page comparison of the governing main text is included; undeciphered or untranscribed source material remains explicit rather than being counted as agreement. Typography and electronic metadata conventions are documented separately from lexical content.

The established glossary remains authoritative. Occurrence-specific uncovered senses and technical gaps may be used provisionally with notes under the translation standard; they do not amend the canonical glossary. The translation is released as an annotated agent-produced working edition for human review, not as independent human certification.

## 2026-10-02 — Stop translation and preserve all work

The user instructed: “Ok, then we stop here. Make sure all the work is fully committed to the repo.” Further translation and source-audit work are stopped. Chapter1 remains the only released English chapter. Its six complete source pages and opening portion of printed423 are represented; English pagination is not set. Chapter2 records were read and a segmentation task was dispatched, then interrupted before any chapter2 artifact or English was created. Resume only on a new explicit user instruction. Commit and verify this stopping state without modifying the fixed chapter release.

## 2026-10-02 — Resume translation through completion

The user instructed: “I want you to continue with the translation from where it is left until completed,” and supplied this repository with GitHub and Remote Desktop Commander selected. This explicitly resumes the stopped translation and source audit under the existing scope, glossary, fixed golden release, Adzom endnote policy, independent agent QC and sequential release gates. Chapters 2–8 and the complete English aggregate are authorized. Existing fixed releases remain unchanged.

Startup recovered remote main `09b0409c1a63eafe19deef1888838d1d3d50d6de` into a clean checkout with all existing annotated releases and scan files. Chapter 1 final read-only validation passed. The selected MacBook was offline when checked; its local-only work, if any, was not inspected or overwritten.

## 2026-10-03 — Proceed to chapter 3 while chapter 2 publication is pending

After being informed that chapter 2 was translated, independently reviewed and signed but its annotated release tag could not be published through the available terminal/connector, the user instructed: “excellent, move to chapter 3 then”. This directly authorizes chapter 3 working translation and review now. The coordinator interprets this as a narrow sequencing exception for chapter 3 drafting, not permission to claim chapter 2 released or to bypass either chapter's final publication checks.

Chapter 2's signed candidate is pinned to commit `f0f7097621c021b4a03863dc7b7e8925c6975f86` and remains byte-identical. Chapter 1's fixed release and `golden-v1` remain unchanged. Chapter 3 working operations may use a separately recorded, hash-bound draft authorization; strict final validation still requires chapter 2's real annotated tag and verified receipt. No tag or receipt is fabricated. The finite current scope is MTP-S000222–MTP-S000341 (120 objects), native images 439–446 (printed429–436), source pairs, English, source apparatus, independent QC, validation and remote checkpoints. This exception does not authorize starting chapter 4 before the current chapter's release gate.

## 2026-10-03 — Proceed to chapter 4 while formal releases remain pending

After receiving chapter3 as a completed, independently reviewed working translation and being told that chapters2–3 formal tags remain pending, the user instructed: “excellent, next chapter”. In this context the next chapter is chapter4. This explicitly authorizes its working translation, native comparison, complete endnotes, independent review, content signoff and repository preservation now. The coordinator records this as the same narrow sequencing exception used for chapter3; it does not declare any missing release complete, waive final publication checks or authorize chapter5 preparation before the current gate.

Chapter2 remains pinned to f0f7097621c021b4a03863dc7b7e8925c6975f86 and chapter3 to50bef02b5b0088911153ce348f7f45612e147158, with their signed chapter files and manifest inputs unchanged. Chapter1's real annotated release remains mandatory. The committed chapter4 draft authorization binds both reviewed priors; strict final validation still requires real prior tags and receipts. The fixed golden-v1 source and canonical glossary remain unchanged.

Finite current scope: MTP-S000342–MTP-S000635,294 objects,19 native images446–464/printed436–454. Freeze source pairs before English, account for every object and every recorded source obligation, perform separate agent QC, validate reproducible outputs and commit each substantive batch.


## 2026-10-03 — Proceed to chapter 5 from the saved chapter 4 draft

After being told that chapter 4 translation and independent review had completed in the session but the final save failed, the user instructed: “cool, then move on to next chapter”. The disclosure identified the recoverable 396-note draft, the lost final 397-note revision and supporting records/signoff, the five unresolved passages, pending formal release tags, and that chapter 5 had not started. The next chapter is chapter 5. This instruction expressly authorizes chapter 5 working translation, native comparison, endnotes, independent review, content signoff and repository preservation now despite the incomplete chapter 4 final package.

The repository's authoritative chapter 4 state is its complete annotated but unsigned saved draft at `730921898da3e3328bb42d97abea7672bf44afcd`. The final upload stopped after creating some unattached file blobs; it did not create a verified main commit. Workspace maintenance subsequently removed the local checkout and final files. The saved repository was re-cloned unchanged. Historical in-session review and validation are not substituted for missing hash-bound files. The final terminology records, additional note, author/QC reports and signoff are absent from this saved snapshot and remain deferred recovery work. No claim is made that the 397-note candidate was committed or released.

Chapter 5's separately committed schema-3 authorization pins chapter 4's entire saved chapter tree and bound manifest inputs, explicitly labels it `unsigned_saved_draft`, and retains the signed chapter 2/3 pins and actual chapter 1 release. The frozen golden source and canonical glossary remain unchanged. Normal final validation and publication still require real sequential release tags and receipts. This working exception is specific to chapter 5, not permission to start chapter 6 or declare missing review/release files complete.

Finite current scope: MTP-S000636–MTP-S001051, 416 fixed objects, native images 464–490 / printed454–480, including partial spans on the first and last images. Freeze exact source pairs before English drafting, account for all source units and all recorded source obligations, perform separate agent QC, validate reproducible outputs and remotely preserve each substantive batch.

## 2026-10-03 — Preserve GitHub state and proceed to chapter 6

The user instructed: “So make sure that everything is in github up to date, and move on to the next chapter.” Remote main and the clean local checkout were verified at `54d75972da0abf7b9e2de969502abf5414374f7e`; chapter 5's saved signed-content and read-only working validation pass. The next chapter is chapter 6. This instruction explicitly authorizes its bounded working translation, native comparison, endnotes, independent agent review, content signoff and remote preservation.

The schema-4 working authorization pins chapter 5's signed reviewed candidate at `c0b7945a56e8c670363d50a6c67448bdda83003a`, preserves the prior signed chapter 2/3 candidates and actual chapter 1 release, and inherits chapter 4's exact unsigned saved snapshot at `730921898da3e3328bb42d97abea7672bf44afcd`. Chapter 4's missing final package remains missing; this continuation neither recreates it nor substitutes historical in-session review for saved evidence. Fixed golden source and canonical glossary remain unchanged. Genuine sequential publication tags and receipts remain mandatory in strict final and aggregate modes.

Finite scope: chapter 6, MTP-S001052–MTP-S001427, 376 objects, 23 native images490–512 / printed480–502 with partial boundary spans. Freeze exact source pairings before English, preserve substantive batches on GitHub, account for every required source obligation and obtain separate agent QC. The exception does not authorize chapter 7 preparation.

## 2026-10-04 — Continue to chapter 7

After receiving chapter 6 as a completed independently reviewed working translation, with formal release tags explicitly pending, the user selected GitHub and Remote Desktop Commander and instructed: “go on”. In this context the next chapter is chapter 7. This expressly authorizes its bounded source preparation, native comparison, English translation, endnotes, terminology records, independent agent review, content signoff and GitHub preservation. It is the same narrow working-continuation exception used for chapter 6, not permission to invent prior releases or waive strict final publication.

Startup verified remote main `ddc3ff3e9b42de9279a550d9c5e3a30109565601`, the chapter 6 signed candidate at `a02f8c79a31c561c1888495b4178bfa7c25eda45`, its exact manifest `8b00c111bc44a0aabb04e82a6def3cb9039ea0174b2b6548756b786f0d9cd767`, and passing read-only working validation and content checks. The new schema-5 authorization will retain the actual chapter 1 release, signed chapter 2/3/5/6 candidates and exact unsigned saved chapter 4 snapshot. Chapter 4's missing final package remains missing. Frozen golden source and canonical glossary remain unchanged. Genuine sequential tags and receipts remain mandatory for formal final and aggregate publication.

Finite scope: chapter 7, MTP-S001428–MTP-S001769, 342 objects, 19 native images 512–530 / printed pages 502–520, with partial boundary spans. Freeze exact source pairs beginning MTP-000453 before English. Compare every allocated main-text span, preserve all required source obligations, review the complete English and support records independently, and save each substantive batch remotely. This exception does not authorize chapter 8 preparation.

The startup local scan ZIP was truncated to 5,703,168 bytes and failed ZIP integrity checking. That copy was preserved separately with SHA-256 `268e5b762aedf6953eef9e327b2a654b846a54a568698f617235557af9d7ef00` before restoration; a local recovery branch preserves the starting commit. The exact original cached LFS object, 7,759,123 bytes with SHA-256 `82ec9ea1255dc217ade08562b4400c29f2eb8c7d96f07b9c46814998ccbbfdac`, passed integrity checking for all 121 members and restored the original tracked bytes. All 19 allocated native images independently match exact archive bytes and manifest hashes, dimensions, sizes, URLs and canvases. This repair changes no archival identity and is not a visual reading claim.


## 2026-10-04 — Continue to the final chapter

The user instructed: “great, next chapter then...how many do we have left?” The next and final chapter is chapter 8, containing 284 fixed source objects. This explicitly authorizes its bounded working source preparation, native comparison, English translation, endnotes, terminology records, independent agent review, content signoff and GitHub preservation. The schema-6 continuation retains the actual chapter 1 release, signed chapter 2/3/5/6/7 candidates and exact unsigned saved chapter 4 snapshot. It is not a waiver of genuine formal final or aggregate publication gates.

Startup verified clean local and remote main at `40f2fb91acd2e8cc8879a779ac70a4db476700f0`, the actual golden and chapter 1 tag objects and peeled commits, and passing chapter 7 signed-content and read-only working validation. The chapter 7 candidate remains pinned to `e40041ace3efe51bf2aa205a092c7d117011514a`, manifest `288560e60dfbb38e73991311599f47fd55a7d9046bf747299311dec1ed84b8f9`. Chapter 4 recovery remains separate; its absent final package is not presumed. Fixed golden source and canonical glossary remain unchanged.

Finite scope: MTP-S001770–MTP-S002053, 284 objects, 18 native images 530–547 / printed pages 520–537 with partial opening span. The frozen segmentation contains 107 pairs MTP-000568–MTP-000674: 83 verse pairs / 248 lines and 24 prose pairs preserving metadata, closing narrative, chapter and work colophons, source annotations and three blessings. The 55 inherited obligations comprise 14 change records and 41 uncertainty statements. Compare every allocated main-text span, record newly observed differences without altering the fixed golden release, preserve each substantive batch remotely, and review the complete English and supporting records independently before content signoff. Completion will represent all 2,053 fixed source objects; it does not itself establish formal whole-book publication.


## 2026-10-04 — Complete chapter 4 review and formal English publication

After being told that all eight working translations were complete and chapter 4's final package and formal releases remained pending, the user instructed: “go on”. This authorizes completing that finite remaining work: fresh chapter 4 terminology, independent review and signoff; genuine sequential chapter releases 2–8; and the complete English aggregate. It does not approve proposed glossary entries or resolve uncertain readings.

Startup verified clean main at `3972b751e37538779cbbfcc01c9bdc7e5c6beb24`. The complete eight-chapter state is preserved on `archive/working-edition-3972b751`, and fresh chapter 4 work is isolated on `review/ch04-final-20261004`. The local Git inventory found no genuine copy of the lost final package; fresh review is not represented as recovery of that lost revision. The authoritative 396-note saved draft and immutable original author archive remain preserved.

Chapter 4 review covers 294 fixed source objects S342–635, 86 pairs MTP-000100–000185, 272 verse lines, 60 translator notes, 336 source notes and all 337 source obligations. The finite task is to complete an occurrence-bound lexical ledger and inactive proposals, author review, independent QC, reproducible outputs and new explicit signoff. Only newly established corrections will be logged; no historical 397-note target is imposed. Fixed golden source, evidence, glossary and signed chapter 1/2/3/5/6/7/8 packages remain unchanged.

The connected Mac is now online; authenticated GitHub access to the exact repository confirms push/admin permissions. This resolves the prior annotated-tag transport blocker. Publication will use genuine annotated tags at freshly verified actual main commits, followed by committed receipts. Existing strict gates remain unchanged. Sequential canonical projections through chapters 2, 3, 4, 5, 6, 7 and 8 are necessary to satisfy the existing bounded release surface; all eight chapter directories and the archived complete working edition remain preserved. Historical working-authorizations retain their exact pins and remain reproducible at their original commits. The complete canonical surface will be restored through chapter 8 before the aggregate release.

## Shared template decisions — preserved scope and provenance

The following P1, P2 and P3 records are copied verbatim from [`Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`](https://github.com/Lotus-King-Translation/tibetan-text-project-template/blob/882454cb2576d0b2529296bd7a3a7c87371ab4cf/DECISIONS.md). Their template-only scope, historical version/hash statements, validation claims and issue dispositions describe those original template changes, not tests or translation corrections in this book. The local adoption record below makes the pinned resulting policy operative here. P3's explicit issue-disposition supersession is retained; older assistant proposals and unapproved book usages are not new authority.

<a id="post-translation-review-2026-10-05"></a>

### 2026-10-05 — Capture issues #1/#2 and add completed-English review (P3)

**Authorization:** the owner directed that the lessons in issues #1 and #2 be incorporated into the template rather than left pending in tickets, and that the guideline and AGENTS.md cover review of completed English by another agent. The owner will propagate the files and assign one reviewer to each of the four works. This task does not perform those reviews.

**Implemented scope:** baseline `43b24b2781d9f278b413b5c833012e42758232d4`; standard **2.1.0**, Phase D in `AGENTS.md`, shared controls in Part I §8.1 and the executable review contract in Part III. Reuse Part II Q1–Q9, the existing finding/usage formats, status and handoff. No new workflow file, schema, validator, lexicon redesign or translation is introduced. The entire **283-row glossary is byte-for-byte unchanged**, including all original assignments and P1/P2 controls.

**What replaces the pending-ticket dependency:** approved vocabulary stays in the CSV. The remaining U01–U14 questions are captured as explicit, reusable construction/family review controls, including the owner's preferences and exclusions; they are no longer dependent on issue comments or chat. Reviewers must examine them when encountered, record evidence and a local disposition or visible unresolved treatment, and return genuinely new shared-label proposals without activating competing book glossaries. This instruction authorizes the review process, not unspecified new English defaults. Uncertainty is an explicit review outcome, not a silent omission or reason to leave the entire task unprocessed.

**Capture map (all 44 U groups and 21 G groups):**

| Groups | Operative home |
| --- | --- |
| U01–U03 | Approved honorific/name CSV rows; Part I §8.1 full/short forms, unresolved honorific/title and recurring-name controls |
| U04 / U09 / U11 / U14 / U15–U44 | P2 CSV assignments, conditions and source references; Part I §8.1 links and Part III §3 checks |
| U05–U08 / U10 / U12–U13 | Part I §8.1's family/meditation/compound/means/two-truth/phrase/luster controls, with actual alternatives and comparator IDs |
| G01–G10 | Existing protected terms plus Part III §3's lexical, component, whole-expression and omitted-relationship checks, with loci |
| G11 / G13 / G14 / G17 / G20 | P1 CSV rules; Part I §9 and Part III §3 scope/capitalization/adoption checks |
| G12 / G15 / G16 / G18 / G19 / G21 | Part III §3's source-dependent exception, qualifier, ordinary-sense and short-form checks under Part I §6 |

**Phase D boundary:** freeze source/English/policy inputs and reviewer identity; distinguish review-only from authorized revision; inspect every pair including closing material; recheck corrections and derived outputs; preserve historical records. Reuse one report with exact coverage, before/after evidence, no-change cases, unresolved questions and actual tests. A completed review is not clean text approval, a new release, or human certification. Four agents may finish independently under one pinned policy; the coordinator handles cross-work reconciliation. No additional review stage is required merely to check the reviewer's own edits.

**Issue disposition:** issues #1 and #2 may close as completed **template learning-capture** tasks once this commit is published and linked. Their audit bodies and comments remain historical evidence. This supersedes P1/P2's instruction to keep those template tickets open; it does not claim their example passages were corrected or their unresolved lexical interpretations approved. Work-specific findings now belong to the Phase D review package, not a new holding ticket.

**Propagation:** adopt `AGENTS.md`, `guidelines/tibetan_translation_standard_v2.md`, and `glossary/expanded_tibetan_english_glossary.csv` from the same template snapshot. Merge P1/P2/P3 into each book's `DECISIONS.md` and add Phase D fields from `translations/HANDOFF.md`; preserve local decisions, populated status and history. The three updated READMEs are optional navigation changes. Update local `PROJECT-STATUS.md` for adoption without copying its template placeholders. No source/English placeholder, script, tag or source register needs propagation.

**Validation:** all 44 U groups and 21 G groups are accounted for in the capture map and operative files. The full 283-row/eight-column glossary and 24 unrelated tracked files are unchanged; exactly eight existing documents changed, with no new tracked files. Relative links, section anchors, active version references and 72 distinct cited pair IDs were checked. Ten in-memory document-integrity corruption controls were rejected. The existing paired-template validator passed with zero placeholder pairs, and `git diff --check` passed. R58–R63 extend the existing section to 63 fixture specifications; R48 corrects a copied unresolved-source spelling, not a Tibetan edition; the other 56 prior fixture rows are unchanged. The new contract and controls were self-reviewed, not independently certified. No translation-model benchmark or new full-book semantic review was performed. No book/source/tag is changed by this patch.

**Content identities:** glossary SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`; standard SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`.

<a id="terminology-expansion-2026-10-05"></a>

### 2026-10-05 — Approved issue #1 additions and matter/karmic-being clarification (P2)

**Authorization:** the owner accepted the proposed U15–U44 treatments in chat and instructed implementation in the template, except that U35 should not use the proposed insentient-matter label. The owner explicitly confirmed **karmic being** for སེམས་ཅན and suggested **matter** for བེམ་པོ/བེམས་པོ, subject to comprehension. P2 implements matter with a source-sensitive scope note, rather than reintroducing sentience vocabulary. Earlier firm decisions in [the owner's issue comment](https://github.com/Lotus-King-Translation/tibetan-text-project-template/issues/1#issuecomment-5978887526) remain authoritative. Approval concerns these proposed defaults and their stated conditions, not unconditional application to disputed clauses.

**Finite scope:** template only; baseline `cd9d1c26ee70dc7d486b50c2d9df1244613215f5`. Append **61 records**, including separate attested forms, for **283 total glossary rows**. This covers all **30 groups U15–U44**, six earlier groups with specifically settled implementation (U01/U03/U04/U09/U11/U14), and the newly reconfirmed karmic-being convention. The original **222 Tibetan–English assignments remain unchanged and in order**. Correct only status/provenance fields in two existing rows that still called standalone ཐུགས absent. Update the existing combined standard to **2.0.2**, retaining its filename; update the decision/status/handoff records and issue #1. No translation or source publication is part of this patch.

**Approved defaults and controls:** exact forms, grammar, triggers, exclusions, related entries and pinned source evidence are in the existing CSV, not a competing synonym list. U15–U44 follow the accepted proposals. The linked cluster is **essence / core / pure extract / quintessence**; core never becomes essence, and no general core-to-quintessence exception is activated. Existing whole-expression assignments, including Mahamudra, retain precedence. Earlier firm entries added here are the full/short **Blessed One**, the proper name **Vajradhara**, **sacred pledge**, **transmission**, **key point**, and **core**.

**U35:** use **matter** as the mass noun and **material thing(s)** where the source requires count grammar. The relevant knowing/non-knowing distinction must remain intelligible, with a source-linked explanatory note where the concise label obscures it. Matter does not mean immobile, dead, lifeless or non-karmic being, and does not imply that karmic beings lack material bodies. It does not replace every occurrence of body, entity or substance. Selected checks: DTG-000111/000869, SMB-000047/000050 and MTP-000540/000550. The default is implemented; disputed comprehension or clause interpretation remains locally reviewable.

**U36/U40:** citta is an approved **retention policy**, not certification of a heart/anatomical identity. Awakened mind is approved for standalone ཐུགས in the cognitive/honorific scope. Heart/location passages and the unresolved Pearls clauses remain open to construction-level review. Lexical approval alone must not remove their uncertainty markers.

**Not silently approved:** U02's specific Joy-Maker/Delight-Maker/Maker-of-Joy choice; U05's affliction/mental-state defaults; U06's bsam gtan label; U07's every-occurrence itself treatment; U08's thabs rule; U10's superficial/superfactual pair; U12's phrase/word rule; U13's luster/lustre decision. The English equivalent for Tathāgata and the distinct rdo rje dzin title also still need explicit selection. Neither this patch nor a settled proper-name entry turns those open questions into approved defaults. The owner-approved U15–U44 label choices do not decide every disputed historical passage.

**Guidance and examples:** recognize scoped Approved P2 entries alongside the preserved original assignments; preserve complete karmic-being wording and avoid an invented inverse relation to matter; distinguish English honorifics from retained proper names and compositional epithets. Remove obsolete standalone-thugs absence claims in Parts I/II and R24. Add **R35–R57**, yielding **57 fixture specifications**, covering both conforming treatments and prohibited overextensions. These extend the existing section only.

**Adoption and remaining work:** template encoding is complete (**61/61 rows; 30/30 approved new groups**). Eight earlier groups still need specific choices, with the partial honorific/title questions noted above. All four books still require explicit glossary/standard adoption and source-sensitive English/note revisions. Do not overwrite historical release inputs, rewrite Tibetan, or treat issue #1 as closed. Issue #2's existing translation departures are not corrected by adding entries here.

**Validation:** Structural/source-reference checks passed: all 222 original assignments and their order preserved; the eight-column schema unchanged; 220 original raw records untouched, with only status/provenance fields changed in the two obsolete standalone-thugs documentation records. All 61 additions have explicit approval, scoped usage and verified pinned Tibetan occurrence references; no new duplicate headwords. 14 in-memory corruption controls were rejected. All 33 unchanged original fixtures and P1 expected results are preserved; R24 is updated and R35–R57 added. The existing paired-template validator passed with zero placeholder pairs, and git diff --check passed. New fixture specifications and selected matter/citta/related-term examples were self-reviewed, not independently certified; no translation-model benchmark, full book retranslation, scan proofreading or exhaustive new semantic audit was performed. 27 unrelated tracked files are unchanged; no new tracked file, tool, schema or review stage is introduced.

**Content identities:** glossary SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`; standard SHA-256 `c1b8e91dcfc858fa3b87bb0adba63f98b28ff273f350e34cf9d45e82951cfbbb`. This is a template maintenance commit, not a new fixed Tibetan or English release; no tag is created or moved.

<a id="terminology-clarification-2026-10-04"></a>

### 2026-10-04 — Bounded issue #2 terminology clarification (P1)

**Authorization:** after reviewing [issue #2](https://github.com/Lotus-King-Translation/tibetan-text-project-template/issues/2) and the proposed bounded patch, the owner instructed: “Do the changes/updates now in the template repo.” The approval concerns the specific five-row/three-amendment proposal, not every alternative interpretation listed in the issue.

**Scope and version:** template only; translation standard **2.0.1** and glossary clarification revision **2026-10-04 (P1)**. Retain the standard's existing filename. Baseline template commit: `f6431c25c7c9fa852c404b8cd3e0e3cdeae1178f`. All 222 Tibetan–English assignments, row order, eight columns and unrelated supplementary cells remain unchanged. No new headwords, files, tools, schemas or review stages are introduced.

**Approved glossary clarifications:** the operative conditions and exclusions are recorded in the five existing rows, with P1 provenance:

| Existing assignment, unchanged | Approved clarification | Issue group |
| --- | --- | --- |
| རྒྱུད་ → Continuum | Literary **tantra** only for unambiguous tantric scripture/text-genre uses; retain other senses and whole-expression precedence | G11 |
| སྒྲ་ → Word | Auditory **sound** where the sense is supported; retain linguistic whole expressions and review ambiguous extensions | G14 |
| འབྲས་བུ་ → Result | Botanical **fruit** and explicitly sustained tree/fruit metaphors, not blanket stylistic alternatives | G17 |
| གཞི་ → The Ground | Technical **Ground**, with ordinary article grammar; no adjudication of disputed support/other senses | G13 |
| གཞི་སྣང་ → Ground-appearance | Consistent technical capital G and existing hyphenation | G13 |

**Guidance:** Part I §3.3 now addresses overlapping source modifiers and established English components without automatic duplication or loss; §6 requires reuse of adopted shared approved usages rather than competing chapter/book defaults; §9 defers to approved glossary presentation rules. Part II extends R04/R11/R18 and adds R31–R34, retaining all existing IDs and the other expected distinctions. Normal grammatical variation still needs no new lexical approval.

**Not approved or performed:** no general logical-property, physical-movement, separating/secret-preliminary or nominal-apprehension exceptions (G12/G15/G16/G18); no final adjudication of the individual G19 vajra passages. Other pending proposals remain pending. G01–G10 remain translation-remediation tasks, not reasons to add synonyms. No sibling repository, Tibetan source, English translation or release tag is changed, and issue #2 remains open.

**Adoption:** consuming projects must explicitly adopt the new glossary/standard versions and recheck affected occurrences. Do not overwrite inputs bound to historical releases. This template update is not a claim that existing translations have been corrected or brought into compliance.

**Validation:** Structural checks passed: all 222 base assignments, their order and the eight columns are unchanged; exactly five glossary records changed, with the other 217 raw records unchanged. All 29 other tracked files are unchanged. The fixture table has 34 unique IDs, with 27 original fixture rows unchanged. Seven in-memory corruption controls covering assignment/headword changes, row order/count, schema, unrelated supplementary edits and duplicate/replaced rows were rejected. `git diff --check` and the existing paired-template validator passed (zero placeholder pairs). The seven affected fixture specifications were manually reviewed; no translation/QC model benchmark or independent philological certification was performed.

**Content identities:** glossary SHA-256 `07e1b3a567aa6abb72fac931b23830deba68de14477a9c3b147296d960995ce4`; standard SHA-256 `710abf09ac7b98f6cb092dec11493787425280cc52031b2c1b41d8fe477e89c2`.

<a id="policy-adoption-2026-10-05"></a>

## 2026-10-05 — Adopt the common pinned policy; do not review English

**Authority and scope:** the owner's current propagation instruction explicitly names this repository, the template commit `882454cb2576d0b2529296bd7a3a7c87371ab4cf`, the three operative files, and the required decision/status/handoff merges. It authorizes policy adoption, validation and publication only; it expressly prohibits English review, retranslation or correction, source/pair changes, archived-input changes, new terminology decisions, and template-repository edits.

**Operative baseline:** standard **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; glossary **283 data rows / eight columns**, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`. Both files are byte-identical to the pinned template. P1/P2/P3 are adopted with their original anchors and scoped approvals. No later explicit owner-approved local terminology exception was found in the inspected decision history; no exception is inferred from assistant proposals or local usage notes.

**Local history retained:** The Adzom endnote requirement and all continuation/publication decisions remain in force within their recorded scope. The later explicit completion authorizations supersede the 2026-10-02 stop. Fresh chapter 4 review of the saved 396-note draft remains distinct from recovery of the missing 397-note package; no lost package is claimed recovered. Earlier 'glossary unchanged' statements and phase deferrals retain their original release/task scope; they do not override this newer explicit active-policy adoption. They are not rewritten to claim that earlier releases used the new baseline.

**Preservation and validation boundary:** existing source/English releases and tags remain fixed. Historical policy inputs remain available at their exact unchanged commits/tags, and archived copies are not overwritten. Legacy validators that bind active policy paths to earlier release hashes may reject this adoption checkout; those failures are reported, not hidden by editing old contracts, signatures, validators, or derived outputs. See [actual before/after checks](translations/HANDOFF.md#policy-adoption-validation). Publication is via `policy/adopt-template-882454cb` and a pull request to `main`; adoption on `main` is not claimed before merge.

**Review state:** reviewer/session unassigned; reviewed pairs **0/674**; review completion **not started**; text disposition **not assessed**. One bounded policy adoption is recorded for this repository, with **0** English changes and **0** reviews performed.

## Post-translation review authorization — 2026-10-05

The owner assigned `POST_TRANSLATION_REVIEW`, mode `review-and-revise`, for this repository’s complete existing English translation. Authorized scope: read every fixed Tibetan–English pair, apply the smallest supported English and translation-note corrections under adopted standard 2.1.0/P1/P2/P3, reconcile active usage records, regenerate dependent reading outputs, preserve historical records, and commit/push through the normal workflow. The fixed Tibetan, segmentation, shared glossary assignments and release tags are not editable under this instruction. This is a reviewed working text, not a new formal release or human certification. Reviewer/session and frozen inputs are recorded in [FINAL-REVIEW.md](translations/FINAL-REVIEW.md#phase-d-review). No new book-local terminology default is approved by this authorization.

## 2026-10-05 — Land the complete reviewed working package in main

The owner instructed: “But of course you must ensure everything lands in main.” This explicitly requires integration of the complete existing Phase D review package, including the saved English/note corrections, generated readers, build support, review evidence and status/handoff records, into `main` using the normal non-force workflow. Preserve interrupted work before synchronization, verify the actual remote merge and final main state, and leave no valuable unpublished changes. This is repository integration authority only: no new English default, shared glossary assignment, source change, release tag or human certification is approved.
