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
