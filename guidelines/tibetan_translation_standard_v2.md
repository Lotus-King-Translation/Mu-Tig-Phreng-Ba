# Tibetan–English LLM translation standard

**Guidance, independent QC and post-translation review · Version 2.1.0 · 5 October 2026**

This document combines translation, independent QC and review of completed English works. Use it with the current eight-column glossary and the Tibetan source. It does not replace or alter the glossary.

## How to use this document

**Translation run:** provide this standard, the current glossary, the Tibetan source, and any explicit decisions. Set the task to **TRANSLATE**. Part I governs the working translation and contains a copy-ready instruction.

**QC run:** provide the same materials plus the English draft and its notes. Set the task to **QC**. Part II governs the independent review; Part I remains its terminology and translation policy. Do not call the translator's own self-check independent QC.

**Completed-work review:** set the task to **POST_TRANSLATION_REVIEW**. Part III defines Phase D for a reviewer receiving another agent's completed English. It uses Parts I–II and the shared controls in §8.1. Declare review-only or explicitly authorized review-and-revise.

Drafting and independent review remain separate. A review must not silently rewrite the source, glossary, or original draft.

**Active terminology:** the original assignments remain established. The owner-approved P2 additions are active within their recorded scope; retention-only policies do not resolve uncertain meanings or syntax. Other pending supplemental uses remain pending. New operational rules are not blanket approval of alternatives. [P2]

**Superseded document:** do not load `revised_translation_guidance.md` as active guidance alongside this version. Its incompatible rules and tests have been replaced, especially the rejected objection to **ordinary mind**.

The documents define a working LLM draft and review process, not a final human edition. The 63 regression fixtures in Part II are tests to run, not a claim of measured model performance.

---

# Part I — Translation guidance

**Version 2.1.0 · 5 October 2026**

**Purpose:** a source-aligned, terminology-controlled, annotated working translation for subsequent human editing  
**Companion:** Part II of this document
**Replaces:** `revised_translation_guidance.md` and incompatible recommendations in the initial translation assessment

> Preserve the established Tibetan–English vocabulary. Make its grammatical use accurate, its contextual exceptions controlled, and unresolved matters visible. Do not use translation or review as an occasion to renegotiate established terminology.

## 1. Mandate and boundaries

This project requires English that keeps its relationship to the Tibetan systematically recognizable. Familiar Buddhist-English wording, majority usage, elegance, and conventionality are not independent reasons to replace a glossary assignment. An established multiword English term is a lexical equivalent, not necessarily a collection of separately added modifiers.

Produce grammatical and intelligible English, but preserve meaningful lexical distinctions, components, pairings, repetition, and relationships ahead of stylistic smoothing. Final human editing is a later stage; its existence does not excuse inaccurate grammar now. Conversely, neither the LLM nor its QC reviewer may sacrifice terminology to make the draft read like a conventional published translation.

The supplied source governs what the passage says; the glossary governs the established English vocabulary used to express it. These are concurrent requirements. Grammar must not become a loophole for replacing vocabulary, and vocabulary must not become a justification for changing the source's meaning.

This guidance does not authenticate the Tibetan edition, settle outstanding glossary proposals, or supply missing doctrinal explanations. It implements the project decisions supplied in the glossary and discussion. The procedural details below are the working specification, not evidence that a proposed lexical addition has been approved.

## 2. Authority and the eight-column glossary

### 2.1 What is authoritative

Use the current project owner's explicit decisions, the current original Tibetan–English assignments, and individually approved usage decisions. Apply a later explicit project decision where it changes an earlier one; record the change and its scope. Do not assume that a later assistant suggestion is such a decision.

The original 222 Tibetan–English pairs are established and remain unchanged. P2 appends 61 approved records (including separately recorded attested forms), bringing the active table to 283 rows; their authority and limits are recorded in the same eight columns. [P2] Their continued authority does not depend on having a complete explanation in the supplementary columns. A blank field means **not documented here**, not **free choice** and not **no grammatical variation permitted**.

The expanded glossary's row label “Established” applies to the original pair. It does not approve every explanatory sentence, grammatical proposal, or contextual suggestion attached to that row. Distinguish:

| Information | How it may be used |
| --- | --- |
| Original pair or explicitly approved replacement | Active canonical assignment |
| Existing whole-expression assignment | Active for that expression when the source occurrence matches it |
| Explicit user decision or separately approved usage | Active within its recorded scope |
| Observation directly recoverable from the original table | Evidence about the table; not a new doctrinal definition |
| Assistant-added explanation without independent approval | Supporting documentation to assess; no independent permission to change a term |
| Proposed wording, pending trigger, or open question | Not an approved alternative |

For example, the expanded table marks “thoughts,” “integrate with,” “by its intrinsic nature,” and “gesture of equipoise” as proposals or matters requiring review. Do not activate them merely because the parent row is established. A necessary working construction may still be proposed locally under section 6; it must not be represented as previously approved. [E]

### 2.2 How to use each column

| Column | Function |
| --- | --- |
| Tibetan | Exact headword or expression; retain the original form |
| English | Canonical lexical assignment; not an immutable grammatical string |
| Meaning and scope | Approved explanations and relevant documentation; inspect their provenance |
| Allowed grammatical forms | Recorded realizations; distinguish approved examples from proposals |
| Contextual exceptions | Scoped alternatives, or references to established whole expressions; inspect the basis and conditions |
| Related entries | Links for family, component, contrast, pairing, or form checks; do not infer undocumented semantic identity |
| Rationale and sources | Evidence and decision history; missing rationale does not invalidate an established pair |
| Status and open questions | Keep original-pair status separate from the status of any attached proposal |

Do not change this schema or the original two columns during translation. Keep one Tibetan form per primary row. Multiple contextual uses belong in linked or clearly separated usage records, not slash-separated alternative defaults.

## 3. Protected lexical commitments

### 3.1 Full expressions remain identifiable

The following are established assignments, shown here in prose case:

| Tibetan | English | Boundary to preserve |
| --- | --- | --- |
| སེམས་ | ordinary mind | Do not reduce to generic “mind” because “ordinary” lacks a separate Tibetan word |
| ཐ་མལ་གྱི་ཤེས་པ་ | ordinary knowing | Do not merge with ordinary mind |
| བློ་ | conceptual mind | Preserve the whole expression, including within its established phrases |
| ཡིད་ | mental faculty | Do not make it interchangeable with the other mind/knowing entries |
| ཤེས་པ་ | knowing | Distinguish its assignment from the more specific knowing expressions |
| རིག་པ་ | awareness | Retain its identifiable assignment |
| རྣམ་ཤེས་ | consciousness | Retain its identifiable assignment |
| རང་བཞིན་ | intrinsic nature | Preserve the complete term even when its construction is not a standalone noun phrase |
| རྣམ་རྟོག་ | differentiating conceptualization | Do not reopen this canonical choice; handle differing uses through controlled usage records |
| ཡེ་ཤེས་ | primordial knowing | Do not replace with generic “wisdom” |
| ཤེས་རབ་ | discerning knowing | Preserve its distinction from primordial knowing |
| དགོངས་པ་ | enlightened intent | Do not weaken it simply to avoid repetition |

Basis: G, lines 40, 62–63, 79, 99, 104, 115, 132, 137, 169–170, 218; U2.

“Ordinary” in **ordinary mind**, “intrinsic” in **intrinsic nature**, and “differentiating” in **differentiating conceptualization** are parts of established equivalents. Their presence alone is not an addition error. Additional qualifications outside the established equivalent still require support.

The user's explanation connects ordinary mind/ordinary knowing with a threefold account. Preserve the supplied commitments, but do not invent the full threefold taxonomy, its names, or its distribution across texts. That explanation is not fully documented in the present materials. [E, entries སེམས་ and ཐ་མལ་གྱི་ཤེས་པ་; U2]

Distinct English labels preserve which Tibetan terms occur; they do not require the translator to assert that the terms always name different realities. If the source identifies, relates, or equates them, preserve that relationship in the sentence without collapsing their labels.

### 3.2 Families, compounds, and pairings

Preserve lexical-family visibility and glossary-defined components unless a relevant established whole expression or approved contextual use governs otherwise. Do not shorten an expression merely because it repeats. Keep meaningful source order in pairs: **denying and affirming**, **abiding and movement**, **apprehended object and apprehending subject**. Preserve inversions when the source actually reverses a pair; do not force every occurrence into the glossary's order without checking it.

Retain the visible **doing / free from doing** and **cultivation / non-cultivation** relationships. Preserve the established **contrivance** family rather than casually reassigning that vocabulary to unrelated technical expressions. [G:76, 81, 91, 125, 147, 182, 187, 205]

Keep རྟོགས་པ་, **realization**, distinct from the རྟོག་ / རྟོག་པ་ family. Keep **experience**, **experiential acquaintance**, and **realization** linked to their respective entries rather than rotating them for style. Preserve the different actions in **naked seeing** and **naked resting**. [G:26–27, 45–46, 164–165, 204]

### 3.3 Established whole expressions govern their own occurrences

Before building a translation from components, check for a complete entry. Examples already established in G include:

| Complete Tibetan expression | Established English |
| --- | --- |
| སྣང་བ་བཞི་ | four visions |
| རླུང་སེམས་ | wind-mind |
| ཡིད་ཀྱི་རྣམ་ཤེས་ | mental consciousness |
| ཞི་ལྷག་ཟུང་འབྲེལ་ | union of calm abiding and insight |
| སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ | discriminating primordial knowing |

Do not “correct” these to mechanically expanded component renderings. Their assignments do not authorize shortening the corresponding standalone terms. A longer text match is a candidate for analysis, not proof that the phrase has been correctly identified. Confirm boundaries, construction, and context. [G:65, 101, 120, 139, 163]

When an explicit Tibetan modifier overlaps with a component already present in an established English equivalent, determine its function in the complete construction. Do not duplicate the English component merely to give each source element a separate word, and do not absorb a modifier that contributes additional meaning. Record a materially uncertain relationship in the existing note or usage record. This is not automatic approval of either treatment at a disputed locus. [P1]

### 3.4 Reserved English and reversibility

Reserve complete technical expressions and their identifiable families; avoid casual reassignment to unrelated Tibetan terms. Check both directions: repeated Tibetan should not drift between unrelated English terms, and a technical English expression should not silently acquire unrelated Tibetan sources.

Do not mistake an English substring for a collision: **knowing** inside **primordial knowing** is intentional component preservation. Likewise, do not make every ordinary English use of a broad word an automatic violation. In an aligned technical passage, ambiguous reuse still requires review.

Retain original shared mappings, such as the two **gaze** entries, without inventing a distinction or inventing a rationale for their equivalence. Reversibility is strongest where the glossary assigns distinct expressions; documented shared mappings require source alignment. Metadata supplements reader-visible terminology; it is not permission to erase it. [G:47–48; E]

Apply owner-approved complete additions such as **karmic being** without reconstructing their components. **Matter** is not an inverse label meaning non-karmic being and does not replace every body, entity or material substance. When a source contrast is obscured by concise wording, preserve it through the approved contextual treatment or a source-linked note, not unapproved synonyms. [P2]

## 4. Analysis and grammatical realization

Read the glossary and the source together. Identify the source unit, complete expression, grammatical function, participants, modifier attachments, negation, reference, and instructional context before committing to an English sentence. Do not parse entirely in isolation from the project's terminology, then import generic equivalents afterward.

Use these categories for actual occurrences:

| Category | Meaning | Treatment |
| --- | --- | --- |
| Canonical | Direct use of the applicable entry, including an established whole expression | Normal output |
| Grammatical | Same lexical commitment, adjusted to the source construction | Normal output when covered by the general rule below or approved usage |
| Approved exception | Different wording under an explicitly supported, scoped exception | Record entry, condition, and source occurrence |
| Provisional | Unresolved application, uncovered technical term, or proposed alternative | Visible note and review record; not approved terminology |

### General permission for grammar

Articles, agreement, supported number, ordinary inflection, and sentence syntax may change without a new lexical decision. Transparent changes such as **cultivation → cultivate**, **recognition → recognize**, **clear and distinct → clearly and distinctly**, or **free from doing → freedom from doing** are permitted when the source requires that function and the lexical meaning remains intact. Check for separately assigned neighboring entries before deriving a form. [U2, discussion of grammatical flexibility; E]

This permission does not authorize removing a substantive component, selecting a new synonym, changing semantic scope, adding agency, or inventing a relationship. A possessive, preposition, nominalization, or change of number can be interpretive in a particular sentence; treat it accordingly when it affects the meaning.

For རང་བཞིན་གྱིས་, preserve **intrinsic nature** while establishing its grammatical relationship. Do not duplicate it as both an extra modifier and an additional entity. “By its intrinsic nature” remains a proposed construction in this dossier, not a blanket formula. [E; T:41, p. 295]

Do not force a source expression into a technical noun merely because the English glossary headword is a noun. Equally, do not claim that an adverbial construction requires dropping the established vocabulary.

## 5. Fidelity beyond individual terms

Verify actions and relationships, not just nouns. Preserve who speaks, acts, knows, possesses, instructs, or is described. Check long modifier chains before splitting sentences. Retain negation, modality, conditions, quantities, comparisons, temporal scope, and meaningful repetition.

Distinguish statements such as **is**, **appears as**, **is called**, **is the basis of**, and **is endowed with**. Do not replace one with another solely to fit a doctrinal expectation. Preserve a relationship identified in the project discussion without turning it into a universal lexical equation.

Track instructional function: temporary exercise, diagnostic test, objection, quotation, description, and concluding instruction. In the discussed suppression/proliferation sequence, an early direction must not be flattened into the text's unrestricted final instruction. [T:17–19, pp. 283–284]

Retain both the established terms and the source relationships in the colophon. Do not fix possible attachment errors by replacing **enlightened intent** with generic **mind** simply to avoid repetition. P2 now supplies the standalone ཐུགས་ cognitive/honorific assignment **awakened mind**. That entry does not settle an unclear colophon relationship or a heart/location construction; those remain source-specific. [G:170; E; T:49, p. 299; U2; P2]

Account for content in both directions: every substantive source unit must have an English counterpart or a visible unresolved marker; every substantive English addition must be supported by the source, an established lexical equivalent, an approved usage, or a disclosed interpretive supply. Do not require separate source words for each component of an established English term.

## 6. Contextual exceptions and unresolved applications

A different contextual sense may require different English. It does not permit free synonym selection. An approved exception needs an identifiable source use, allowed wording, triggering conditions, exclusions, evidence, and approval scope. A broad label such as “Dzogchen context” is not an adequate trigger where the same text uses the term in several ways.

Before changing wording, determine whether the problem is already covered by a whole-expression entry or by grammar. These are not contextual exceptions.

Once adopted into a project's active glossary version, an approved shared usage governs occurrences meeting its stated conditions. A different chapter or book is not, by itself, grounds for different terminology. Reuse the existing decision and record only genuinely new sense or construction questions; retain occurrence traceability and the visible first-use note required below. [P1]

When a canonical application appears materially wrong and no approved exception covers it:

1. Recheck the exact source, full construction, whole-expression entries, and contextual evidence.
2. Distinguish positive evidence of a mismatch from unfamiliar English, stylistic discomfort, or conventional translation preference.
3. Preserve the canonical entry in the glossary. Explain the occurrence-specific problem.
4. Use the narrowest defensible provisional wording with a note, or retain the unresolved Tibetan where a responsible rendering cannot be chosen. Do not knowingly conceal a misleading application as settled.
5. Record the canonical term, proposed realization, source location, evidence, and open decision. Do not let the provisional usage become a default in later passages or later runs.

An unannotated substitution is a deviation. A disclosed provisional treatment is a review item; it is neither an approved equivalent nor automatically a mistranslation. The reviewer must evaluate its evidence.

For རྣམ་རྟོག་, retain **differentiating conceptualization** as canonical. The discussion identifies a need to distinguish the epistemological process/scheme use from references to occurring thoughts. It does not approve a blanket **thoughts** replacement or a complete trigger rule. Annotate unresolved applications without importing the technical account into every occurrence. [E; U2]

For ལུ་གུ་རྒྱུད་, apply the user's documented non-visionary chain distinction in the discussed delusion passage; do not import **vajra** there merely from the canonical visionary assignment. The working example **chain of delusion** is recorded in E. This does not replace **vajra chains** universally, nor authorize **continuum** indiscriminately. [G:122, 188; E; T:25, p. 287; U1]

When a noncanonical rendering hides the Tibetan identity, make that identity available in a visible note at its first use in each independently readable section and link further occurrences in the usage record. Keep provisional occurrences visibly linked to their unresolved status.

## 7. Mandatory annotations

Annotate suspected source defects, ambiguous syntax or scope, omitted or unreadable material, proposed reconstruction, materially supplied subjects or relationships, technical glossary gaps, and unresolved contextual applications. Ordinary English articles do not require notes unless they resolve a substantive ambiguity.

Use a stable note ID, such as `[N-001]`, attached to the affected translation segment. Each note must include:

| Field | Required content |
| --- | --- |
| Location | Source file/version, printed page if available, and segment or exact anchor |
| Exact Tibetan | The smallest sufficient passage, unchanged from the source |
| Category | Source reading; syntax/reference; scope; terminology gap; contextual use; interpretive supply |
| Problem and evidence | Concise, checkable explanation; do not substitute speculation for evidence |
| Working treatment | What the draft does, including any retained Tibetan or provisional English |
| Uncertainty | Plausible alternatives where useful, and confidence in the working interpretation |
| Review action | The specific decision or source check needed |

A suspected defect is not an authenticated corruption. Preserve the supplied reading separately from a proposed emendation. Do not silently omit a difficult location, repair a disrupted verse, or resolve an unclear numerical grouping. The crown/heart phrase, the disrupted song on p. 289, and the grouping on p. 291 remain annotation examples, not settled editorial corrections. [T:35, 29, 33]

Annotations should expose the problem rather than overwhelm the draft: one explanatory record may cover repeated occurrences, but every affected span must remain traceable. Never replace the actual problematic passage with a generic “translation uncertain” note that prevents review.

## 8. Adding words systematically

Translation may expose a glossary gap. It does not authorize silently extending the canonical table. The existing glossary represents accumulated decisions; a new entry must join that system rather than solve only one sentence.

For every proposed technical addition or new usage:

1. Capture the exact attested form, construction, source location, and working meaning. Distinguish the source form from a proposed headword.
2. Search the entire current glossary for the form, longer expressions, related forms, components, paired expressions, and the proposed English output.
3. Identify which existing choices the addition must preserve. Do not infer a complete paradigm or a lexical-family relationship solely from similar spelling.
4. Decide whether the gap concerns a new primary entry, a linked grammatical realization, a contextual exception, or missing documentation of an existing entry.
5. Check English collisions, reversibility, whole-expression precedence, and any consequences for neighboring entries.
6. Propose the minimum supported addition using the existing eight columns. Leave unknown definitions or sources blank or explicitly unresolved; do not invent them.
7. Mark the new mapping or usage **Proposed**, list affected source occurrences, and explain the family-level impact. Keep alternative candidates in open questions, not as competing canonical glosses.
8. Activate only after explicit project-owner approval; record the exact decision, update the version, and recheck affected passages. Neither repeated LLM use nor a QC recommendation constitutes approval.

For the discussed mixing gap, start with the existing **mix/mixed/mixing** vocabulary in སྒྲ་དོན་འདྲེས་རུང་ and མིང་དོན་འདྲེས་པ་. Investigate the encountered འདྲེ་ and འདྲེས་ forms and the daytime-appearance construction. Do not promote **integrate with** as an unrelated new default merely because it works in one English sentence. [G:23, 86; E; T:31, 49]

Likewise, the established **denying and affirming** compound does not by itself supply the missing standalone དགག་ entry for the suppression exercise. Determine that verb's contextual use separately from the contextual treatment of རྣམ་རྟོག་. [G:19; E; T:17]

Prioritize gaps affecting meaning, technical consistency, or recurrent usage. Do not require every ordinary function word to become a technical glossary entry.

<a id="shared-review-controls"></a>

### 8.1 Shared review controls carried forward from the four-work audit

These are operative instructions for translation and review, not a second glossary. First consult the adopted CSV: an approved assignment governs within its scope. For a genuinely unapproved choice, use the source-linked provisional procedure in §6; do not silently select a new series default or stop the rest of the work waiting on an issue. Record the actual construction, alternatives tested, and the narrow conclusion in the existing usage/review record. A supported local interpretation and approval of a shared lexical assignment are different decisions.

| Audit group and expression | Required treatment when encountered |
| --- | --- |
| U01 / U03 — honorifics and names | Use the approved full/short **Blessed One** and proper name **Vajradhara**. English honorifics are required; do not turn that policy into translation of all proper names. For དེ་བཞིན་གཤེགས་པ (Tathāgata) supply a source-linked English proposal if no approved entry governs. Keep རྡོ་རྗེ་འཛིན་(པ), currently vajra-holder/holder of the vajra, distinct from རྡོ་རྗེ་འཆང་; a similar English title does not prove identity. |
| U02 — ལྷ་དབང་དགའ་བྱེད་ / དགའ་བྱེད་ | Collect recurring names in the existing usage record, including full/short forms and referents. For Joy-Maker/Delight-Maker/Maker of Joy, compare DTG-001028/001736/002090/002539 and recommend one source-supported form with all affected loci. Do not silently equate different figures or create a glossary row for every descriptive epithet. |
| U05 — mental/affliction family | Review གཏི་མུག (dull confusion/bewilderment/deluded dullness), རྨོངས་པ (bewilderment), and རྨུགས་(པ) (stupefaction/torpid) together. Preserve established མ་རིག་པ **ignorance**, འཁྲུལ་པ **delusion**, and technical བྱིང་བ **dullness**. Include the encountered འདོད་ཆགས desire, ཞེ་སྡང hatred, ང་རྒྱལ pride, ཕྲག་དོག jealousy, and ཁོང་ཁྲོ anger in the collision check, without presenting those unlisted labels as newly approved. Compare actual lists and oppositions (DTG-002423; MTP-000212/000343/000367; SMB-000044; BMD-000063/000064); do not invent a graded taxonomy or collapse the family into ignorance. |
| U06 — བསམ་གཏན་ | Preserve its distinction from established ཏིང་ངེ་འཛིན་ **deep absorption**, especially when both occur (MTP-000338). Test the recorded **meditative stability** proposal against process/state grammar and the existing absorption/stabilization/concentration variants. Do not normalize both Tibetan expressions to absorption or invent a meditation hierarchy. |
| U07 — སེམས་ཉིད་ | Retain **ordinary mind** and determine whether ཉིད is intensive or belongs to a lexicalized construction. The owner's preference is **ordinary mind itself**, not permission to replace every nature-construction blindly. Compare DTG-000332/001115 with MTP-000088/000244; justify any retained nature-of rendering and do not reduce either to generic mind. |
| U08 — ཐབས་ | Test **means** in the technical pairing with **discerning knowing** and **method** for an actual procedure; book or chapter preference is not a trigger. Record the construction rather than rotating synonyms. Exclude the idiom ཐབས་ཅིག (together). Comparators: SMB-000012/000058/000096; BMD-000032. |
| U10 — ཀུན་རྫོབ་ / དོན་དམ་ | Evaluate the owner's preferred **superficial / superfactual** pair together at exact source occurrences, including the sphere and two-truth constructions. Do not automatically change every English relative/conventional/ultimate. མཐར་ཐུག (culmination/ultimate in BMD-000070–000076) is a different expression. Preserve the pair and document its contextual scope before recommending a shared addition. |
| U12 — ཚིག་ | Test **phrase** for a formulated verbal unit and where སྒྲ / ཚིག / མིང are explicitly contrasted (DTG-001188). Test generic **word(s)** only where that does not erase the source distinction. Preserve established **word**, **word and meaning**, and **name** entries; do not let the auditory sound exception settle this separate term. Comparators: SMB-000012/000059; MTP-000539; BMD-000073. |
| U13 — མདངས་ | Compare luminous **luster/lustre** with broader **splendor** against DTG-000151/001442 and MTP-000302/000422; retain the rationale for the narrower luster proposal. Check གཟི་མདངས and བཀྲག separately. Never normalize the spelling into established གདངས་ **radiance**. Treat English spelling separately from source meaning. |

The other missing-term audit groups are implemented in the P2 glossary, including **sacred pledge**, **transmission**, **key point**, **core**, and U15–U44. Apply their stated conditions, not the superseded alternatives in historical notes. In particular keep **essence / core / pure extract / quintessence**, **self-knowing / self-awareness / self-recognition**, **matter / karmic being**, and technical versus ordinary senses identifiable. A source assertion that relates these terms is not grounds to merge their labels. [P2; P3]

## 9. Source preservation and presentation

Keep an unchanged copy of the Tibetan and the current glossary. Use separate lookup keys for any agreed whitespace, punctuation, or character normalization; do not overwrite the source. Record normalization operations. They do not authorize spelling correction, lemmatization, or conflation of distinct lexical items.

For glossary headwords, retain one Tibetan form per row and the final-tsheg convention. Do not impose that headword convention on source quotations, where punctuation and attached forms must remain as supplied. Preserve original order and original assignments unless a separate glossary update is authorized.

Use normal sentence capitalization in running prose. An initial capital in the supplied glossary is not a command to capitalize a term mid-sentence. Retain proper names and explicitly approved glossary presentation rules; apply those rules consistently across independently readable sections, without a competing chapter-local convention. Do not infer an exception merely from an initial capital. For potentially intentional internal capitals not yet covered by an approved rule, such as **Cutting Through** or **Guru Yoga**, record an unresolved presentation choice once and use it consistently; do not silently rewrite the original entry. Term-specific decisions remain in the glossary rows. [G:13, 144, 175; U2; P1]

Translate recurring honorifics into English using approved entries; retain approved proper names such as Vajradhara. Translate compositional epithets without inventing new identities or building an exhaustive epithet catalogue. An untranslated honorific without an approved English record remains a specific glossary question, not a license to invent one. [P2]

For future glossary additions, common headwords normally use lowercase; proper names and explicit exceptions retain their capitals. Use no terminal period on an English gloss, maintain the established hyphenation conventions, and keep number consistent where the source meaning permits. Do not force singular or plural across different senses or constructions. Do not migrate the existing 222 entries as part of this translation or QC task.

Preserve meaningful verse lineation, quotation boundaries, headings, enumeration, and source-page traceability. Page markers must not produce artificial English word breaks or sentence fragments. A translation unit may span pages; record that span. Do not silently rearrange Tibetan lines to produce smoother verse.

Keep four change classes separate: **source/textual**, **terminological**, **semantic/syntactic**, and **presentation**. A formatting pass may not choose a new meaning, repair a source reading, alter a technical assignment, or resolve a doubtful compound. Spelling changes that could change the Tibetan lexical item are textual edits, not mechanical cleanup.

## 10. Translation run and required deliverables

### Run sequence

Establish the supplied source, glossary, applicable decisions, and requested coverage. Read the relevant context, identify units, draft with the glossary, attach necessary notes, check coverage in both directions, and perform a terminology-and-grammar self-check. This self-check is not independent QC.

For a long text, maintain a continuation record containing the last completed source anchor, next unprocessed anchor, active versions, and open decisions. Chunking must not lose sentence continuations, change terminology, or imply that unread material has been reviewed.

### Default output package

| Output | Contents |
| --- | --- |
| Run header | Source, glossary and guidance versions; reviewed range; supplied or missing context |
| Annotated English draft | Stable segment IDs, source locators, and note markers; no unnecessary rewriting of the Tibetan |
| Review notes | Section 7 records, including unresolved source and usage questions |
| Coverage record | Each source unit linked to its translated segment or explicit unresolved marker; distinguish represented, resolved, and not processed |
| Usage record | All approved exceptions and provisional technical uses, plus non-obvious grammatical choices that need review |
| Proposed glossary additions | Separate eight-column candidate records; none silently activated |
| Handoff statement | Work completed, checks actually performed, unresolved items, and material not reviewed |

A standard usage record is:

`Source unit | Exact Tibetan span | Canonical entry | English realization | Category | Condition/evidence | Approval or note ID`

Repeated canonical occurrences need not each produce a verbose note. Alignment must nevertheless allow a reviewer to recover their source, and every noncanonical/provisional occurrence must be accounted for.

Do not call an output complete when a passage has merely disappeared. An untranslated phrase retained with a note is accounted for but remains unresolved. Do not claim full semantic review when only a sample or a mechanical scan was checked.

## 11. Copy-ready translation instruction

Use this instruction with this guidance, the current glossary, the Tibetan source, and any explicit decision records:

```text
Task: TRANSLATE under Tibetan–English LLM translation guidance v2.1.0.

Produce an annotated working translation of the supplied Tibetan, not a final
stylistic rewrite. Treat the original glossary assignments as established.
Use existing whole-expression entries and approved usage conditions. Preserve
full technical expressions, their families, and meaningful source distinctions.
Allow faithful grammatical realization without unapproved synonym substitution.
Do not treat row-level “Established” as approval of proposed supplementary uses.

Preserve the source's syntax, participants, scope, actions, and instructional
sequence. Do not silently repair, omit, or harmonize difficult material. Where
an application is materially doubtful, give a source-linked note and narrowly
provisional treatment; do not create an unmarked new glossary default.

Return the run header, annotated draft, review notes, coverage and usage records,
separate proposed glossary additions, and an honest handoff statement. Leave the
supplied source and glossary unchanged. Follow the requested coverage; identify
anything not processed. Use the companion QC procedure for a separate review,
not as a substitute for producing the translation requested in this run.
```

## Source and decision register

**G — Original glossary:** `Pasted markdown(20260920-073604).md`, 222 entries, physical lines 3–224. Citations such as G:137 identify a physical file line, not a doctrinal source. Original assignments were compared with E for this revision.

**E — Expanded glossary:** `expanded_tibetan_english_glossary.md`, with the eight agreed columns. Locate an entry by its exact Tibetan headword. Its introductory status/provenance qualifications remain operative.

**T — Tibetan source:** `Pasted markdown(20260907-085600).md`, printed pages 276–300. References such as T:41 identify physical file lines; the long Tibetan lines may contain several sentences. This is the supplied text, not a newly verified edition.

**D — Earlier English draft:** `Pasted markdown (2)(4).md`. It provides examples of drafting and review problems; it is not an authority over G or T.

**U1 — User's initial principles:** the eighteen rules and A–G terminology QA model in this conversation.

**U2 — User's subsequent corrections:** retain established terminology; do not default to conventional translations; distinguish grammatical realization from contextual semantic exceptions; add glossary entries systematically; retain sentence relationships and lexical transparency; annotate source and scope problems; use normal prose capitalization; target LLM drafting before human editing.

**U3 — Agreed data structure:** keep Tibetan and English as the authoritative pair, with the six supplementary columns. Preserve original data and separate established assignments from proposed uses.

**P1 — Bounded template clarification, 4 October 2026:** the owner approved implementation of five existing glossary-row clarifications, the three short guidance amendments and focused regression updates. See [the exact decision and limits](../DECISIONS.md#terminology-clarification-2026-10-04) and [issue #2](https://github.com/Lotus-King-Translation/tibetan-text-project-template/issues/2) for the source-linked G findings. The operative contextual/presentation rules are in the current CSV glossary's supplementary columns; all 222 base assignments remain unchanged. The cited sibling passages are evidence, not translations revised by this patch.

**P2 — Approved issue #1 additions, 5 October 2026:** the owner approved the U15–U44 proposals, replacing the proposed insentient-matter label with **matter** and confirming **karmic being**. Earlier firm decisions are encoded where a specific label was settled; unrelated open questions are not promoted. See [the exact scope and outstanding decisions](../DECISIONS.md#terminology-expansion-2026-10-05). The glossary records source-linked conditions, grammatical forms, distinctions and retention-only citta policy. No sibling translation is revised by this template patch.

**P3 — Captured audit lessons and Phase D, 5 October 2026:** the owner directed incorporation of both audit issues into the template and a bounded post-translation review phase. Part I §8.1 supplies the shared controls; Part III makes the completed-work review executable without issue threads. See [scope, capture map and propagation](../DECISIONS.md#post-translation-review-2026-10-05). This is review authority, not blanket approval of undecided English labels.

No external doctrinal research was added to this guidance. General procedures and templates are the present implementation of these project decisions. Earlier assistant assessments that conflict with this version, including the rejected “unqualified སེམས་ must not become ordinary mind” test, must not be reused as active rules.


---

# Part II — Independent QC

**Version 2.1.0 · 5 October 2026**

**Purpose:** independent, source-based quality control of a terminology-controlled LLM working draft  
**Governing companion:** Part I of this document
**Default mode:** review and propose minimal corrections; do not rewrite the source or glossary

> Check whether the draft preserves the source through this project's established terminology. Then check that the proposed corrections preserve the same standard.

## 1. Review mandate

QC is not a second opportunity to replace the glossary with familiar Buddhist-English vocabulary. It must detect mistranslation, unsupported additions, omissions, defective relationships, terminology drift, unapproved exceptions, and inadequate annotations. It must also reject false positives caused by the reviewer's own translation preferences.

Apply the current guidance and explicit project decisions. Re-examine the source independently of the translator's explanation and earlier assistant criticisms. A previous “high-confidence error” label is not evidence. The initial assessment's objections to **ordinary mind** as an addition and to **intrinsic nature** merely because of its English wording have been superseded.

Treat **ordinary mind**, **intrinsic nature**, **differentiating conceptualization**, and the other original assignments as established. Do not demand separate Tibetan modifiers for the words within an established English equivalent. Do not call unfamiliarity, length, or repetition an error. Check sentence structure without diluting its vocabulary.

Independence means an independent check of source, decisions, and evidence. Do not describe a translator's self-check as independent QC, even if it uses this checklist.

## 2. Required inputs and scope declaration

Record the exact source version, draft version, glossary version, guidance version, explicit usage decisions, and requested range. Read the expanded glossary's introductory status qualifications and inspect relevant rows in full, not only their English cells.

The reviewer needs the Tibetan, not merely the English and a term list. When source context, a page, or a decision is unavailable, identify the resulting limitation. Review the available material without claiming inaccessible material was checked. Do not ask again for information already supplied.

Before substantive review:

| Check | Required action |
| --- | --- |
| Source baseline | Retain an unchanged source copy and establish source locators |
| Glossary baseline | Confirm which original assignments are active; compare any later edits with authorized decisions |
| Supplementary status | Separate original-pair authority from proposed or assistant-added usage notes |
| Scope | Declare the pages/segments actually reviewed and any sampling |
| Draft artifacts | Obtain annotations, usage records, coverage records, and proposals when supplied; report missing records |
| Conflicts | Use the latest explicit project decision, not the latest unsupported suggestion |

Missing documentation does not automatically invalidate an established mapping. Missing source evidence may prevent a semantic verdict. Keep those issues separate.

## 3. Review outcomes and finding labels

### 3.1 Classify each finding before proposing a change

| Finding label | Meaning |
| --- | --- |
| Confirmed error | The supplied evidence establishes a mismatch within the reviewed scope |
| Probable error | Evidence favors a mismatch, but a reading or attachment remains open |
| Open question | The available materials do not settle the reading, usage, or editorial choice |
| Documentation gap | A decision or occurrence is insufficiently recorded; do not presume its wording is wrong |
| Conforming / no change | The flagged wording follows the project standard and should remain |

Assign a category separately: **source integrity**, **syntax/reference**, **meaning/scope**, **coverage**, **terminology**, **grammar**, **exception/provisional use**, **glossary gap**, **presentation**, or **reviewer-introduced error**. Multiple categories may apply to one issue; avoid double-counting the same underlying error.

### 3.2 Severity and confidence are different

Use **High**, **Medium**, or **Low** severity for the consequence of the issue. A reassigned speaker, reversed instruction, suppressed passage, or systematic loss of a protected term may be high severity. An isolated traceability weakness may be medium; an isolated presentation inconsistency may be low. Judge the actual consequence, not only the category.

Use **High**, **Moderate**, or **Low** confidence for the strength of evidence behind the finding. When uncertain, state what remains uncertain. A probable high-impact attachment error need not be called certain. A certain capitalization defect need not be called high impact. For an unresolved source question, severity describes the potential consequence, not proof that an error exists.

Do not average these into an overall “accuracy percentage” or let good formatting compensate for a material translation error.

## 4. The QC passes

### Q1 — Authority and preservation

Verify the original Tibetan–English pair and any governing whole-expression entry before flagging a term. Check whether an apparent alternative is already an original assignment, an approved usage, an ordinary grammatical realization, or a pending proposal.

An “Established” row does not approve a pending alternative inside it. Assistant-written explanatory notes do not acquire project-owner authority by being copied into a table. Blanks do not authorize synonyms.

Check that the source and glossary have not been silently changed. A copied working draft may contain disclosed proposals; it must not masquerade as the unchanged baseline.

### Q2 — Source integrity and completeness

Map each substantive source unit to its English counterpart or an explicit unresolved marker. Check titles, quotations, line continuations, enumerations, instructions, and colophons, not only the most technical paragraphs. Verify both source-to-English coverage and English-to-source support.

Distinguish **represented** from **resolved**. Retained Tibetan with an uncertainty note is represented but not fully translated. A missing paragraph is neither. Page breaks must not cause omissions or duplicate sentence continuations.

Check suspected source defects without automatically declaring the source corrupt. A smooth English sentence may hide an unacknowledged reconstruction. Demand an unchanged reading, a marked proposal where applicable, and an actionable source query.

### Q3 — Syntax, reference, and meaning

Independently verify the main action, grammatical relationships, participants, possession, modifier attachments, conjunctions, negation, modality, time, number, and scope. Determine whether the draft changes **what happens**, **to whom**, or **under what condition**.

Check long modifier chains before accepting an English sentence split. In the colophon, test which clauses qualify the lamas and which concern the author; do not convert a probable reading into a settled claim merely because an earlier review did so. Preserve **enlightened intent** while examining the relationship. Do not make repetition alone a collision finding. [T:49, p. 299; G:170; U2]

Apply the addition test to semantic content, not word counts. A component of a canonical English term has glossary support. A genuinely additional doctrinal adjective or causal relationship still needs textual or approved contextual support.

### Q4 — Context and instructional function

Check the local use, audience, practice stage, rhetorical role, and surrounding sequence. Distinguish a temporary exercise from the final instruction, a quotation from the author's claim, and an objection from an endorsement.

Do not force specialized senses into every occurrence. Do not treat “context” as an unrestricted license to change wording. Test the conditions of an approved exception; where those conditions are unresolved, evaluate the provisional annotation instead of silently approving a new default.

The suppression/proliferation exercise requires separate decisions about the contextual action of དགག་ and the use of རྣམ་རྟོག་. A correct finding about the verb does not approve **thoughts** as a new universal rendering of the noun. [T:17–19; E]

### Q5 — Terminology, components, and pairings

For each technical source span, perform these checks:

| Check | Question |
| --- | --- |
| Identity | Which exact entry or established expression governs this occurrence? |
| Form | Is this an attested/recognized source form or an unsupported fuzzy match? |
| Family | Are related entries and meaningful lexical relationships preserved? |
| Compound | Does a complete entry govern before component substitution? |
| Collision | Is a technical English output being assigned to an unrelated Tibetan expression without authority? |
| Pairing | Are both members, their roles, and meaningful source order preserved? |
| Reversibility | Can the reader identify the intended Tibetan entry as well as this glossary permits? |
| Coverage | Has a protected component disappeared, appeared twice, or migrated to the wrong clause? |

In particular, do not normalize རྟོག་ and རྟོགས་པ་ into one item. Do not confuse component preservation with crude substring replacement. Attached source forms require grammatical analysis, not unrestricted stripping of letters or syllables.

Do not reject **four visions**, **wind-mind**, **mental consciousness**, **union of calm abiding and insight**, or **discriminating primordial knowing** for failing to reproduce every standalone component gloss; these are original whole-expression assignments. Conversely, those phrases do not license unrestricted shortening elsewhere. [G:65, 101, 120, 139, 163]

Original shared outputs are not new unauthorized collisions. Keep them and record any missing explanation as documentation work. Avoid false collision flags for **knowing** within **primordial knowing**, or similar expected nesting. A new many-to-one technical assignment still requires review.

### Q6 — Grammar, exceptions, and provisional uses

Allow grammatical realization that preserves the lexical commitment and source function. Do not require the exact display string in every sentence. Do not reclassify a semantic substitution as grammar simply because it improves readability.

For every noncanonical or non-obvious occurrence, check the entry, English realization, usage category, condition, evidence, and approval or note. A note referring to an approved exception must identify the actual approval, not merely label the alternative “approved.”

Pending **thoughts**, **integrate with**, **by its intrinsic nature**, and **gesture of equipoise** remain pending as stored usage proposals. They may be evaluated as transparently provisional local treatments under the guidance; they must not be reported as previously authorized defaults. [E]

Where no approved realization fits without a material distortion, require a defensible provisional treatment or retained Tibetan with a note. Do not demand that a known misreading remain unmarked merely to satisfy literal glossary matching. Do not silently turn the proposed correction into a new glossary row.

### Q7 — Annotations and systematic glossary extension

Check all known textual, syntactic, scope, and terminology uncertainties. Each material unresolved point needs its exact Tibetan, location, issue, working treatment, uncertainty, and review action. A note must describe the actual problem; “uncertain” alone is not enough.

Check whether proposed additions investigate the full existing family, compounds, English assignments, and related passages. Require a source-attested form and the same eight-column structure. Separate form, construction, contextual use, and canonical-entry decisions. New candidates remain **Proposed** until the owner explicitly approves them.

For the mixing gap, verify that the proposal engages the existing **mix/mixed/mixing** vocabulary rather than introducing an isolated unrelated default. For standalone དགག་, do not pretend the original compound already establishes every verbal sense. Use the separately approved P2 standalone ཐུགས་ entry within its scope; do not infer it from ཐུགས་རྗེ་ or use it to resolve unclear syntax. [P2] [G:19, 23, 86, 178; E]

### Q8 — Presentation and mechanical checks

Review prose capitalization separately from terminology identity. Sentence-case **ordinary mind** conforms to the glossary's **Ordinary mind** display form. Proper names and explicit capitalization exceptions require separate handling; uncertain internal capitalization remains a presentation query, not a semantic rewrite.

Check hyphenation, quotation and verse presentation, note links, source locators, and sentence continuity across pages. A glossary final-tsheg check applies to headword records, not raw source quotations. Do not let a formatting correction change Tibetan spelling, English meaning, or a mapping's status.

### Q9 — Audit the proposed corrections

Before recommending a change, ask:

1. Is there a source-supported or project-rule-supported defect, rather than a preference?
2. Does the correction retain the established complete terms and relevant whole-expression decisions?
3. Does it repair the actual relationship without introducing a new agent, meaning, or omission?
4. Does it accidentally activate a pending use, erase a distinction, or create a collision?
5. Is the change local, or is a separate glossary decision required?
6. Would this correction pass the same QC as the original draft?

Prefer the smallest sufficient correction. When no settled correction is available, specify the required decision and a marked candidate rather than writing a confident replacement. Do not perform global find-and-replace on semantic variants.

A proposal to replace **ordinary mind** with **mind** solely because “ordinary” has no separate Tibetan modifier fails this audit. A proposal to rewrite the lamas' entire sentence while preserving its technical expressions may pass, but its syntax must still be supported and its unresolved wording marked.

## 5. Report format

### 5.1 Run header

```text
QC version:
Source file/version and reviewed range:
Draft file/version:
Glossary file/version:
Guidance version and explicit decision records:
Review mode: full requested scope / sample / limited
Missing inputs or context:
Checks actually performed:
```

### 5.2 Finding record

```text
Issue ID:
Source locator and exact Tibetan:
Draft locator and exact English:
Finding label:
Category:
Severity:
Confidence and remaining uncertainty:
Evidence: source construction, glossary entry, or explicit project decision
Explanation: concise, checkable reason for the finding
Recommended action: no change / local correction / annotation / glossary proposal
Proposed wording, when justified:
Authority status of proposed wording:
Affected rule(s):
Related occurrences and note/proposal IDs:
Disposition: open / corrected / referred / rejected finding
```

Do not invent approval history, citations, exact locations, or confidence. If an issue has multiple occurrences, identify all detected locations and distinguish exhaustive coverage from examples.

### 5.3 Required report sections

Return the scope and outcome, confirmed errors, probable errors and open questions, any important rejected findings, proposed glossary decisions, presentation issues, and coverage/usage limitations. Empty sections may say “None identified within the stated scope.” Do not equate that statement with proof that none exist.

Keep proposed glossary changes separate from local translation corrections. Corrected drafts are an additional output only when revision is requested; preserve the original draft and supply a change record.

### 5.4 Final status has two dimensions

| Dimension | Allowed description |
| --- | --- |
| Coverage | Complete for the requested range; partial with listed omissions; or not assessable |
| Disposition | Ready for human editing; ready with explicit review flags; revision required; or undetermined |

**Ready for human editing** means the requested QC was performed and no unresolved material defects or questions were identified. It does not certify a final human edition.

**Ready with explicit review flags** means the material is accounted for and suitable to hand to a human with identified unresolved readings or provisional uses. These points are not thereby approved, and the draft is not publication-cleared.

**Revision required** applies to identified material defects that remain misleading or unmarked, including omitted content, incorrect relationships, or silent terminology changes. A glossary that needs an addition is not itself an error in the draft when the gap is responsibly represented and annotated.

**Undetermined** applies where missing evidence prevents the relevant judgment. A partially reviewed text must not receive an unqualified whole-text clearance.

## 6. Worked review records

### Example A — An invalid correction of a protected term

**Source:** T:3, p. 276, རང་སེམས་གདོད་ནས་དག་པའི་སངས་རྒྱས་དེ།  
**Draft wording under review:** “our own ordinary mind, pure from the very beginning.”  
**Proposed criticism:** “Ordinary is added; replace ordinary mind with mind.”

**QC finding:** Conforming / no change for the protected term; the proposed criticism is a reviewer-introduced terminology error. **Evidence:** G:137 establishes **ordinary mind**; U2 expressly preserves it in this context. **Action:** reject that correction. This does not certify every other element of the whole sentence.

### Example B — A real verb problem without premature glossary approval

**Source:** T:31, p. 290, ཟླ་བ་གཅིག་ཙམ་ནས་ཉིན་སྣང་འདྲེ་ཐུབ།  
**Draft:** D:198, “After about a month, daytime Appearance can be overcome.”

**QC finding:** Confirmed meaning problem on the basis accepted in the project discussion; high severity because the action of the instruction changes. **Evidence:** the discussed mixing use and the existing mix-family compounds, G:23 and G:86. **Action:** remove the unsupported overcoming interpretation, establish the subject and relation, and use a source-linked provisional construction pending the missing entry. **Status:** neither **integrate with** nor a newly formulated mix construction becomes an approved glossary default through this finding. Confidence in identifying the wrong action is distinct from confidence in the exact replacement sentence.

### Example C — A source query, not an invisible omission

**Source:** T:35, p. 292, སྤྱི་བོའི་སྙིང་གར་བླ་མ་བསྒོམས་ནས་གསོལ་བ་བཏབ།  
**Draft:** D:225, “Cultivate the lama and make supplication.”

**QC finding:** The locative material is unrepresented; its precise reading remains open. **Action:** preserve the location problem with a visible note, exact Tibetan, and a source-check request. Do not confidently select crown, heart, or a reconstructed combination without evidence. **Separation of judgments:** omission can be established while the intended source reading remains unresolved.

## 7. Regression tests

These are acceptance fixtures for future translation and review runs, not a report that a model has passed them. Many fixtures are deliberately constructed examples. Run them against both the translator and the reviewer: the system must catch genuine deviations and leave conforming terminology alone.

For each fixture record the tested output, observed result, evidence, and pass/fail/not-tested status. A pass requires the expected distinction, not merely a keyword. An unresolved source fixture passes by being correctly flagged, not by inventing a final translation.

| ID | Fixture | Expected behavior |
| --- | --- | --- |
| R01 | སེམས་ rendered **ordinary mind**; reviewer says “ordinary” is an addition. [G:137; U2] | Preserve the term and reject that reason for correction |
| R02 | Source describes སེམས་ as primordially buddha. [T:23] | Do not infer that **ordinary mind** must become generic **mind** |
| R03 | ཐ་མལ་གྱི་ཤེས་པ་ and སེམས་ both become **ordinary mind**. [G:137, 169] | Restore the separate **ordinary knowing** assignment where applicable |
| R04 | རང་བཞིན་གྱིས་ is awkwardly constructed; proposed fix deletes **intrinsic**. Also DTG-001760/U03653: རང་བཞིན་ becomes **intrinsically**. [G:40; T:41; P1, issue #2/G02] | Repair or flag the construction while retaining **intrinsic nature**; neither component may disappear. Do not claim a pending construction is already approved |
| R05 | རྣམ་རྟོག་ uses **differentiating conceptualization**. [G:62] | Do not reopen the canonical term because another rendering is conventional |
| R06 | **Thoughts** silently replaces རྣམ་རྟོག་ on the authority of an open-question note. [E] | Flag unauthorized activation; require a scoped provisional record or explicit approval |
| R07 | རྟོག་ and རྟོགས་པ་ are merged by fuzzy matching. [G:45, 204] | Reject the conflation and preserve the separate lexical items |
| R08 | ཤེས་རབ་ and ཡེ་ཤེས་ both become **wisdom**. [G:104, 218] | Preserve **discerning knowing** and **primordial knowing** |
| R09 | ཉམས་མྱོང་ becomes **experience** or **realization** without authority. [G:164–165, 204] | Flag loss of the **experiential acquaintance** assignment |
| R10 | ཅེར་མཐོང་ and ཅེར་གཞག་ both become **naked seeing**. [G:26–27] | Preserve the seeing/resting distinction |
| R11 | Reviewer changes **four visions** to **four appearances** for component consistency. Also DTG-002278/U04690: དབང་པོའི་སྒོ་ becomes **gates of the faculties** rather than **sense gates**. [G:64–65, 80; P1, issue #2/G04] | Reject component reconstruction where the established complete entry governs. Check the source boundaries; do not force every differently worded gate expression into that entry |
| R12 | Reviewer inserts **special** into the established **union of calm abiding and insight**. [G:162–163] | Reject the claimed mandatory correction; preserve the original complete mapping |
| R13 | **Wind-mind** and **mental consciousness** are mechanically expanded. [G:99–101, 120, 137] | Preserve the established whole expressions without generalizing their shortening |
| R14 | **Discriminating primordial knowing** is rebuilt from individual conceptual-thought components. [G:139] | Preserve the lexicalized complete expression |
| R15 | Both original gaze entries use **gaze**. [G:47–48] | Do not invent a new English distinction; a missing rationale is documentation work |
| R16 | A checker flags **knowing** inside **primordial knowing** as a collision. [G:104, 132] | Reject the substring-only false positive |
| R17 | A sentence requires **clearly and distinctly** or **freedom from doing**. [G:76, 135–136; U2] | Permit faithful grammatical realization; do not require the display string |
| R18 | **Ordinary mind** becomes **ordinary mind** mid-sentence. Technical གཞི་ / གཞི་སྣང་ use **Ground / Ground-appearance** under P1; contrast a physical/support ground construction. [G:137; U2; P1, issue #2/G13] | Allow normal prose case and article grammar, retain the approved technical capital G and hyphenation, and reject competing chapter-local casing. Do not use capitalization to decide an ambiguous sense or capitalize every physical ground |
| R19 | དགག་སྒྲུབ་ becomes **affirming and denying** without source reversal. [G:19] | Preserve the source pair's order |
| R20 | Suppression exercise is translated as **deny**, inferred from the compound entry. [T:17; E] | Flag the contextual verb problem; treat the standalone entry and the thought-use decision separately |
| R21 | Daytime-appearance passage uses **overcome**; proposed replacement is automatically added as an established entry. [T:31; E] | Correct/flag the action, but reject silent glossary promotion and require systematic family review |
| R22 | Non-visionary delusion chain is forced into **vajra chains**. [T:25; U1; E] | Apply the documented chain distinction, with occurrence traceability; do not change the visionary default globally |
| R23 | Colophon qualities are assigned to the author without checking the modifier chain. [T:49; D:343] | Review attachment and flag uncertainty; do not settle it merely by preserving all the nouns |
| R24 | Repeated **enlightened intent** is changed to generic **mind** simply to avoid repetition. [G:170; U2] | Reject that rationale; examine the sentence and the separately approved P2 standalone ཐུགས་ scope without replacing enlightened intent or claiming the attachment is resolved |
| R25 | Crown/heart locative material disappears because its reading is difficult. [T:35; D:225] | Require a visible source-linked query; do not invent a repaired location |
| R26 | The disrupted p. 289 song is smoothly reconstructed without a note. [T:29] | Preserve the supplied reading and disclose any proposed reconstruction |
| R27 | རབ་འབྲིང་གསུམ་གའི་ is confidently narrowed to “all three middling types.” [T:33] | Flag scope and source reading; do not replace with a different unsupported grouping |
| R28 | Blank supplementary fields or parent-row **Established** are treated as approval of an alternative. [E introduction] | Preserve original-pair authority and reject the inferred usage approval |
| R29 | A formatting pass changes source spellings/final punctuation, or a review of one section claims whole-text coverage. | Reject the unauthorized source edit or overclaimed coverage; distinguish mechanical checks from semantic review |
| R30 | A QC fix makes prose more conventional but erases a protected component or turns a provisional use into a later default. | Fail the correction under Q9; retain or restore the lexical commitment and scoped status |
| R31 | Clear scripture/title རྒྱུད་, e.g. MTP-000005, versus a nonliterary continuum construction, e.g. SMB-000013, and the established ལུ་གུ་རྒྱུད་ compound. [P1, issue #2/G11] | Use **tantra** only for the supported literary sense; retain **continuum** in other applicable senses and **vajra chains** for its whole expression. Do not infer the literary sense from proximity to a title; flag ambiguous applications |
| R32 | Auditory སྒྲ་ in a sensory/instrument list, e.g. MTP-000462 or DTG-002074, versus the established སྒྲ་དོན་ expression; MTP-000505 tests an appearance-related extension. [P1, issue #2/G14] | Use **sound** for supported auditory phenomena, retain **word and meaning**, and reject a blanket sound-for-word substitution. Review the appearance-related occurrence's actual sense; its setting alone does not activate the exception |
| R33 | Botanical འབྲས་བུ་ and sustained tree/body correspondences, MTP-000461/000468/000474, versus the Ground–path–result enumeration at MTP-000483. [P1, issue #2/G17] | Use **fruit** within the supported botanical/metaphorical scope; retain **result** in the technical enumeration. Reject stylistic rotation among result, fruit and fruition or extension beyond the sustained metaphor |
| R34 | Explicit རྡོ་རྗེ preceding ལུ་གུ་རྒྱུད་ at MTP-000016/000404 and SMB-000087; contrast overlapping English content with a genuinely additional qualification. [P1, issue #2/G19] | Apply Part I §3.3: reject automatic duplication and automatic absorption. Represent the component once only where construction-level analysis supports it without loss; preserve genuine additional meaning or flag the relationship unresolved. These cited loci are not settled by this fixture alone |
| R35 | སེམས་ཅན is reconstructed from ordinary mind, or matter is called a non-karmic being. [P2, P2-KB; U35; BMD-000055; DTG-000111] | Retain karmic being as the complete owner-approved equivalent, without a separate karma-word requirement. Preserve the knowing/non-knowing contrast; matter does not imply that karmic beings lack material bodies. |
| R36 | Historical notes call Bhagavān, samaya or vital point provisional after P2 is adopted. [P2, U01; U03; U04; U09; U11; MTP-000006; MTP-000569; BMD-000075; BMD-000099; MTP-000589] | Apply English honorific, sacred pledge, transmission and key-point decisions within scope; retain the approved proper name Vajradhara. Do not confuse the distinct vajra-holder expression or treat older notes as new approval. |
| R37 | Core, pure extract and quintessence are reduced to essence, or contents becomes quintessence. [P2, U14; U29; U37; MTP-000602; MTP-000608; MTP-000612; MTP-000339] | Keep essence/core/pure extract/quintessence distinct. Never use essence for སྙིང་པོ; retain contents/inhabitants in the supported receptacle construction rather than extending the extract sense. |
| R38 | Every ཆོས་ཅན becomes either logical subject or bearer of properties. [P2, U15; DTG-000304; MTP-000353] | Use bearer of phenomena for its technical scope and subject specifically in a logical proposition. This does not establish an independently existing bearer or approve property for ཆོས་ཉིད. |
| R39 | Mindfulness and thinking is made a noun string in a verbal clause, or remembers replaces mindfulness freely. [P2, U16; SMB-000022; MTP-000541] | Preserve both members with appropriate grammar. Permit recollection wording only for an actual recollection use, not as a general synonym. |
| R40 | An action/agent pair becomes actions, or an agent is imposed on two actions. [P2, U17; MTP-000057; SMB-000069; BMD-000080] | Use doing and the doer only where roles support it; doing and making requires a two-action construction. Preserve number, negation and both members. |
| R41 | Projecting/gathering is conflated with established འཕྲོ་འདུ. [P2, U18; MTP-000060; MTP-000247; SMB-000075] | Keep the approved pair and distinct attested forms; retain actual coordination/temporal force. Physical extension/retraction requires its own supported construction. |
| R42 | Every seal is called a gesture, or every mandala is called a disc. [P2, U19; U26; DTG-002548; BMD-000099; BMD-000050] | Use seal and mandala in their technical scopes, gesture for an actual bodily gesture, and disc for literal geometry. Preserve Mahamudra and source word explanations; apply consistent mandala spelling. |
| R43 | Collection categories alternate Sanskrit/English or lose the explicit great modifier. [P2, U20; MTP-000026; MTP-000338; MTP-000487] | Use discourse collection, discipline and higher doctrine; preserve modifiers/order. Do not force a collection title onto an ordinary training verb. |
| R44 | Mark and characteristic merge, or defining is added to every characteristic. [P2, U21; MTP-000123; MTP-000449; BMD-000073] | Preserve the separate labels; defining requires an actual definition. Analyze the longer signifying-word construction instead of mechanically inserting mark. |
| R45 | Every passing-beyond phrase or chapter title is changed to decisive resolution. [P2, U22; DTG-001042; DTG-001438; MTP-000099] | Use decisive resolution for settling a view/question and passing beyond only for its supported different sense; check the title construction and do not equate བཟློག. |
| R46 | Tenets always becomes tenet systems, or buddha/pure is inserted into every realm. [P2, U23; U24; DTG-000891; DTG-002202; BMD-000082] | Distinguish systems from constituent assertions; use unqualified realm unless the qualification is supported. These are scope decisions, not global English substitutions. |
| R47 | Vocatives become Listen or Alas regardless of rhetoric; kye ma plus awareness is mistaken for ignorance. [P2, U25; MTP-000570; MTP-000398; BMD-000010; BMD-000070] | Use the approved vocative/exclamation function, preserve repetition and separate listen verbs, and check boundaries. Lament must be supported; do not manufacture མ་རིག from a boundary-crossing substring. |
| R48 | Object/domain, entity and matter become interchangeable or negative entity wording is restricted to material presence. [P2, U27; U28; MTP-000386; MTP-000486; MTP-000577; BMD-000022] | Apply each approved scope. Preserve object of focus, distinguish geographical/domain uses, and do not impose materiality on every entity or repair unresolved དངོས་མ. |
| R49 | Familiarity is rejected as a synonym or open sky/midair is merged with space. [P2, U30; U31; MTP-000155; SMB-000060; SMB-000075] | Allow process/state/verb realization of familiarization; do not confuse cultivation. Use midair positionally and retain space/basic-space distinctions; reject accidental substring matches. |
| R50 | All conviction becomes confidence, or a relational trust is forced into a technical numbered set. [P2, U32; DTG-001030; MTP-000115; SMB-000060] | Preserve conviction and source-supported number; trust requires a genuine relational use. Do not merge faith or confident devotion. |
| R51 | Self-knowing/self-awareness/one’s own knowing are made identical to self-recognition. [P2, U33; U44; MTP-000261; SMB-000024; SMB-000035; DTG-002404] | Keep the knowing, awareness and recognition expressions distinct. Choose technical self-form versus ordinary possession from the actual construction; hyphenation alone does not decide it. |
| R52 | Matter is replaced with inert/insentient matter, pluralized as matters, or a body-as-matter simile loses its cognitive contrast. [P2, U35; SMB-000047; SMB-000050; MTP-000540; MTP-000550] | Use matter or material thing(s) as grammar requires. Preserve the contrast and source predicate; explain non-knowing in a note when necessary. Movement does not disqualify matter; do not add dead/lifeless. |
| R53 | Approved citta/awakened mind entries are treated as resolution of an uncertain heart/location clause. [P2, U36; U40; MTP-000015; MTP-000550; MTP-000664] | Retain citta under the approved retention policy; heart needs a locally established referent. Use awakened mind in its cognitive/honorific scope while keeping unresolved syntax visible and enlightened intent distinct. |
| R54 | Every isolated beyond/transcendence or འདས is globally replaced by transcendence of sorrow. [P2, U38; BMD-000053; DTG-000451; SMB-000050] | Apply the noun pair only to the identified full/short expressions; allow pass beyond sorrow verbally. Do not infer a death event or alter unrelated transcending constructions. |
| R55 | Identity is imposed on first-person reference or sovereign is freely substituted in a descriptive clause. [P2, U39; MTP-000582; BMD-000011; BMD-000056] | Use identity for the descriptive scope and self-reference forms when grammatical. A title/lordship reading remains separately justified; labels do not settle attachment. |
| R56 | Spiritual/oral is dropped because no separate source word is identified, or spiritual accomplishment is limited to final awakening. [P2, U41; U43; DTG-002608; BMD-000110; MTP-000261] | Retain the approved complete equivalents and source modifiers. Preserve generic accomplishment/attainment distinctions; oral instruction can be written, and its label does not prove disjointness from pith instruction. |
| R57 | House of light becomes lighthouse or an asserted anatomical structure. [P2, U42; BMD-000096; SMB-000097] | Keep house of light and the exact compact/expanded source forms. Neither a nautical building nor an anatomical identity follows automatically from the metaphor. |

| R58 | A 283-entry scan or source-reconciliation build is called a complete independent English review. [P3; Part III §2] | Require actual pair-by-pair Tibetan–English review, including main/closing material, and a distinct reviewer; distinguish mechanical coverage, semantic coverage and readiness. |
| R59 | After adopting P1/P2, an old proposal note overrides the new rule, or an already repaired finding is filed again. [P3; BMD-000081; Part III §3] | Inspect current English, source and approval version; update active note disposition without rewriting historical records or treating a previous defect as current. |
| R60 | Four agents silently choose different defaults for an unapproved related-term family. [P3; Part I §8.1] | Apply the shared constraints, compare exact source distinctions and report evidenced proposals without activating separate book glossaries; finish the bounded work with explicit unresolved dispositions. |
| R61 | A revision fixes a glossary word but changes its genitive/negation or leaves a reading edition on old English. [P3; Part III §2] | Recheck the whole changed clause and neighbors; derive dependent views from the declared canonical input and verify note/status consistency. A term-string pass does not clear the fix. |
| R62 | A review-only task modifies canonical English or overwrites a book's decisions with template placeholders. [P3; Part III §1] | Save findings/proposals only; require revision authority for English changes and merge policy records without losing local decisions, fixed inputs or history. |
| R63 | Closing a template audit or finishing a flagged review is treated as clean publication approval. [P3; Part III §4] | Separate template capture, reviewed coverage and text readiness. Unread pairs mean partial coverage; unresolved findings remain visible; no release tag or final-human claim follows from the review task. |

These tests do not exhaust Tibetan grammar or establish model-wide accuracy. Add a source-linked regression fixture whenever an approved glossary decision or recurring error exposes a new failure mode. Do not rewrite existing expected results solely because a model repeatedly disagrees with them.

## 8. Mechanical support versus semantic judgment

A script can compare original mappings, identify altered rows, check headword punctuation, find broken links, gather candidate term occurrences, and flag apparent output variation. These are support checks, not a substitute for source interpretation.

Whole expressions, attached forms, grammatical realizations, shared mappings, and contextual exceptions must be considered before treating string mismatches as translation errors. Preserve an allowlist of original shared assignments and approved uses tied to the actual glossary version, rather than suppressing every collision globally.

If a report gives counts or rates, define the denominator and coverage. “No exact-string mismatches found” is not “the translation is correct.” Do not claim automated tests were run when only the procedure was written or examples were manually inspected.

## 9. Copy-ready QC instruction

Use this instruction with this QC procedure, the translation guidance, current glossary, Tibetan source, draft, and supplied notes/decisions:

```text
Task: QC under Tibetan–English LLM translation QC v2.1.0.

Review the draft independently against the supplied Tibetan, current glossary,
and project decisions. Declare the exact scope and missing evidence. Preserve
established terminology; do not substitute conventional English or treat words
inside canonical multiword terms as unsupported additions.

Check source coverage, syntax and attribution, actions, negation and scope,
instructional context, lexical identity and families, whole-expression entries,
pairings, grammatical realization, exception authority, annotations, proposed
additions, and presentation. Distinguish confirmed errors, probable errors, open
questions, documentation gaps, and conforming usages. Keep severity separate
from confidence. Pending glossary suggestions are not active terminology.

Audit every proposed correction under the same standard. Prefer the smallest
supported correction; where unsettled, record a source-linked question and a
clearly provisional candidate rather than silently standardizing it. Do not
change the source or glossary. Return the report specified in section 5, with
separate coverage and disposition statements. Do not claim tests or full-text
review that were not performed. A rewritten draft is not required unless the
user explicitly requests revision as well as QC.
```

## Source register and revision note

Version 2.1.0 adds P3: shared audit controls, a bounded Phase D using the existing QC method, and R58–R63. P1/P2 terminology is unchanged. R48 corrects the copied unresolved-source example to དངོས་མ; the other 56 earlier fixture rows are unchanged. The 63 fixtures are specifications, not measured translation-model results.

G, E, T, D, and U1–U3 refer to the source/decision register in Part I of this document. G is the original 222-entry glossary; E is the expanded eight-column Markdown glossary; T is the supplied Tibetan source; D is the earlier English draft. File-line references identify locations in those supplied files, not independently verified editions.

This procedure supersedes the earlier QC assumptions that challenged **ordinary mind** merely as an addition, treated **intrinsic nature** as dispensable in grammatical constructions, or required the established **union of calm abiding and insight** to be rebuilt from its components. It preserves the real checks for wrong verbs, defective sentence relationships, omitted material, and unmarked uncertainty without promoting unresolved replacements.

---

<a id="post-translation-review"></a>

# Part III — Post-translation review of a completed English work

**Phase D · Version 2.1.0 · 5 October 2026**

Use this phase when another agent receives an existing English translation for review. Parts I and II remain the terminology policy and Q1–Q9 review method; this part supplies the handoff, whole-work coverage, and completion contract. It is not a new translation, a new Tibetan edition, or an invitation to improve prose for taste. No issue thread or earlier chat is required to execute this contract.

## 1. Fix the inputs and the authority to edit

Record the reviewer/session, the English input commit or release, the governing golden Tibetan and pair-ID range, and the adopted glossary/standard commit and hashes in `translations/HANDOFF.md`. The reviewer must be distinct from the authoring run; changing a role label in the same drafting run is not independent review. Existing translator notes are evidence to assess, not findings to accept without checking.

Use one common template snapshot across the four works. Adopt the glossary and standard explicitly before applying changed policy; inspect any newer owner-approved project decisions and record conflicts rather than overwriting them. Preserve the input English in Git history and the fixed Tibetan byte-for-byte. Do not replace a book's `DECISIONS.md`, status, or handoff with blank template records.

Declare **review-only** or **review-and-revise**. A request only to review defaults to review-only: save the report and proposed changes without altering canonical English. When revision is authorized, record each finding before applying the smallest supported English/note correction. Neither mode authorizes source emendation, new shared terminology, unrelated rewriting, changing historical releases, or publishing a release tag.

The expected input is a complete working translation, including titles, headings, closing material, and explicit unresolved/non-translatable markers. Missing material is a coverage finding, not a reason to claim completion from file names or release labels. Declare the finite chapter/pair inventory and existing queries at the outset; do not add an open-ended scan or witness-research project.

## 2. Review the whole work, then check the changes

1. **Read every pair in source order.** Apply Q1–Q9 to Tibetan and English together, including sentence continuations across pairs and chapters. Check speaker, subject, action, genitives, modifier attachment, negation, number, conditions, temporal scope, and rhetorical/instructional function. A concordance or a review of selected passages is not this full pass.
2. **Check the terminology across the work.** Search all applicable glossary entries, attested forms, whole expressions, recurrent names and the shared controls in Part I §8.1. Search the reverse direction for collisions as well as Tibetan-to-English variation. Review source boundaries before classifying a hit; extend a confirmed pattern to all matching occurrences, not just the old example IDs.
3. **Reconcile notes and reading continuity.** Check the current fixed source and current English before reusing an old finding. Keep source annotations, variants, editorial metadata and translator notes out of main text unless they actually belong there. Update active usage/notes when a policy is adopted, linking rather than rewriting historical records. An old proposal may now be approved; a documented proposal may still be wrong; a corrected historical finding must not be filed again. Read the English continuously for broken references, name drift, quotation boundaries and accidental fragments, while retaining source repetition and prose/verse differences.
4. **Audit the proposed or applied corrections.** Recheck changed clauses and their neighbors against the Tibetan and full glossary rows. Verify that the fix has not lost a protected component, created an agent or causal relation, removed real repetition, resolved an uncertainty without evidence, or spread a local sense globally. When revising, regenerate dependent views from their declared canonical input rather than maintaining separately edited English versions.

The reviewer may resolve a construction using evidence and the existing rules. When evidence remains insufficient, preserve a source-linked provisional treatment or exact unresolved span, state the alternatives and what would settle them, and continue. Do not halt the whole book on one term; do not quietly convert a local proposal into a shared default. Such questions belong in the completed review report and usage record, not solely in chat or an issue.

## 3. Carry forward the audit lessons

The following are mandatory checks where applicable. IDs are historical locator examples, not a claim that the current text is still defective. Inspect the current occurrence first. P1/P2 conditions in the glossary govern; the table does not introduce alternative defaults.

| Audit groups | Check and representative evidence |
| --- | --- |
| G01 / G03 / G05 — lexical substitution | Keep **magical display**, **delusory appearance**, and **confident devotion** rather than miraculous display, delusive appearance, or aspiration and devotion at the governing source expressions. DTG-001188; DTG-001120/001459/001659/001727; DTG-001539. Distinguish exact compounds from expanded genitive forms; do not blacklist those English words globally. |
| G02 / G08 — lost components | **Intrinsically / intrinsic abiding** can lose **intrinsic nature** (DTG-001760/002236); **virtuous minds** can lose **ordinary mind** (DTG-000426). Repair the complete construction, not by blindly appending the missing word. Longer compounds and names require their own boundary check. |
| G04 / G06 — whole expressions | Preserve **sense gates** (DTG-002278/002393/002519), not freshly decomposed gates of faculties; preserve **self-recognition** (DTG-000906), not an unapproved explanatory synonym. An established whole expression governs before components. |
| G07 / G09 / G10 — actual relationship and coverage | **Clinging** must not drift to attachment at the same governing expression (DTG-001117/001131). Check unrepresented **nature of phenomena** in the question at DTG-002109. Preserve **object of focus** and its syntactic role (DTG-001477/002071/002074); the separate words object and focus somewhere in a paragraph do not prove fidelity (DTG-000199/001227). |
| G11 / G13 / G14 / G17 / G20 — approved sense and presentation rules | Apply literary **tantra**, auditory **sound**, botanical/sustained-metaphorical **fruit**, and technical **Ground / Ground-appearance** only under P1's conditions. Check titles and colophons as well as main text. Use **dharma embodiment** mid-sentence unless part of an actual title/name, not because the glossary display starts with a capital. Neither a nearby title nor a chapter-local convention decides the sense. |
| G12 / G15 / G16 / G18 — source-dependent exceptions | Review logical **property** versus **nature of phenomena** (DTG-000304); physical move versus **vibration** (DTG-000852/002188; SMB-000047); separating versus the named **secret preliminary**, retaining any separately written distinguishing predicate (DTG-000127; SMB-000091); nominal apprehension versus **apprehending subject** and finite verbs (SMB-000063; BMD-000040). Preserve canonical labels; justify any provisional local exception under Part I §6. Different grammar is not automatically an error or an approved new synonym. |
| G19 — overlapping qualifier | At MTP-000016/000404 and SMB-000087, an explicit རྡོ་རྗེ overlaps with English **vajra** inside **vajra chains**. Check the complete construction and the prior opposing notes. Neither mechanically duplicate vajra nor absorb meaningful additional qualification; record the supported relation or preserve its uncertainty. |
| G21 — ordinary senses and short forms | Distinguish **doing** from activity in an actual action construction (DTG-000590/000770/001752), **abiding** from a temporal/locative remain (DTG-001513/001640), **knowing** from an interpretive understand (DTG-000780), and technical **adornment** from a physical ornament (DTG-001083). Do not force **dullness** on physical sinking (DTG-001186), accept examining for རྟོག་པ without checking it (DTG-001904), or expand a short primordial-knowing name by fuzzy matching (DTG-001751/001975). Record the local grammatical/sense disposition, not a pool of new canonical synonyms. |
| U01–U44 — approved additions and shared controls | Read all relevant P2 rows, including conditions and provenance; apply Part I §8.1 to the remaining construction/lexical questions. Preserve the distinction between an approved label, a retention policy such as **citta**, and a resolved sentence. **Matter** may require explanation of a knowing/non-knowing contrast; **karmic being** is not assembled from the standalone ordinary-mind entry. Names and honorifics must not acquire new synonyms by chapter. |

**False-positive controls:** whole compounds and homographic sequences are not standalone glossary hits. Examples include གླེང་གཞི (setting), དངོས་གཞི (main practice), ཡིད་ཆེས (conviction), ཉམས་སུ་བླང (a practice construction), and ཀྱེ་མ / རིག་པ rather than a boundary-crossing ignorance match. Keep faithful **clings**, **vibrate**, supported plurals, self-forms and normal articles. Do not equate རྟོག with རྟོགས or rewrite variant Tibetan spellings. Source-word explanations may deliberately unpack an otherwise fixed expression. An unlisted ordinary word or a stable unlisted technical rendering is not a new defect merely because a row is absent.

**Historical controls:** BMD-000081 was already corrected to **self-purified**; Pearls chapter 4 received a fresh review of the preserved snapshot, not recovery of its lost later notes. Check commits and actual files rather than repeating obsolete findings. Coverage hashes, golden-source alignment, release labels and translator self-checks do not establish independent semantic review. A source-reconciliation pass may leave earlier English untouched. Unresolved citta/thugs and other source constructions remain visible until evidence supports their resolution.

The examples come from the four-work audit snapshots: [DTG `3ae74a2`](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/tree/3ae74a2adaa734b6332e64bd2f905f25aec1044a/paired), [MTP `21fb131`](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/21fb131912bf7ed161c08a70614702764464030d/paired), [SMB `dc48f4b`](https://github.com/Lotus-King-Translation/Sgron-Ma-Bar-Ba/tree/dc48f4b20ec9b6f3ec5f7e8769cd86f5c344af34/paired), and [BMD `8965e8b`](https://github.com/Lotus-King-Translation/Bkra-Shis-Mdzes-Ldan/tree/8965e8b8b89c396c58789ed83984540699c07be9/paired). Match the stable ID in `source.md` and `translation.md`, and follow its linked notes. The local current files govern the new review; inaccessible comparators are a reported limit, not authority to invent evidence. [P3]

## 4. Deliver one review package and stop at the declared boundary

Use the existing QC report and usage records; where no report exists, use `translations/REVIEW.md`. Reuse Part II §5's finding format. Do not create parallel ledgers for the same facts or verbose notes for every conforming occurrence.

The package must record:

- **Inputs and coverage:** reviewer, modes and pinned versions; expected and actually reviewed pair IDs/ranges by chapter, including closing material; unreviewed/missing ranges explicitly listed. Reviewed, changed and unresolved counts are different. Compact ranges or the existing coverage record are sufficient if gaps remain detectable.
- **Findings and dispositions:** exact Tibetan, before/proposed-or-after English, rule/evidence and severity/confidence; corrected, justified no-change/rejected finding, or source-linked unresolved treatment. A repeated finding may use one explanation with every affected locus. Put genuinely new shared-label proposals together; do not edit the shared glossary independently in each book.
- **Verification and handoff:** source hash and pair-ID/order preservation, active note links, dependent-view consistency, available validation/build results, targeted regression results with not-tested stated, and coverage/disposition under Part II §5.4. In revision mode recheck every changed clause; the reviewer's check of their own repair is not an additional independent review. Update `PROJECT-STATUS.md` and `translations/HANDOFF.md` with the remaining bounded work and commit the authorized outputs.

**Review completion is not publication clearance.** A full pass is complete when every expected pair has actually been inspected and every finding has a recorded disposition. Unresolved but visibly represented material may yield **ready with explicit review flags**; uncorrected misleading errors yield **revision required**. Neither is a clean approval. Missing/unread pairs mean partial coverage. A human-final or release claim requires its separate evidence and existing release gate. Do not create or move tags merely to finish this review task.

When four agents work in parallel, each owns one work and uses the same pinned policy. Their reports must expose new cross-work choices for shared disposition; no agent may silently publish a competing glossary. Each finishes its bounded report rather than waiting indefinitely for the other three. Cross-work reconciliation belongs to the coordinator before claiming the set is harmonized; it is not four additional translation projects.

## 5. Copy-ready post-translation review instruction

```text
Task: POST_TRANSLATION_REVIEW under standard 2.1.0, Part III.

Read AGENTS.md, the project status and translation handoff, the active glossary,
this standard (Parts I–III), DECISIONS.md and FORMAT.md. Record the existing
English input, fixed Tibetan, common policy snapshot and reviewer identity.
Review every pair of the completed work in order, including titles, headings,
closing material, annotations and unresolved spans. Apply Q1–Q9 and the shared
controls in Part I §8.1; do not substitute a terminology scan for semantic review.

Use review-only unless revision is explicitly authorized. In revision mode,
record findings before the smallest supported English/note changes and recheck
them against the Tibetan. Preserve fixed source, pair IDs, original input and
historical releases. Keep generated views consistent with canonical English.
Do not change shared glossary assignments or claim a local proposal is approved.

Save one review package using Part II §5 and Part III §4, with exact coverage,
findings, changes or proposed changes, justified no-change cases, unresolved
questions and actual validation results. Update the existing status/handoff.
Complete the available bounded pass without inventing resolutions, waiting on
issue discussions, or expanding into new source research or a stylistic rewrite.
Return the review commit/report and separate coverage from readiness. Do not
publish a release tag or claim final human certification through this task.
```
