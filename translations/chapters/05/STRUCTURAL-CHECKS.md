# Chapter 5 structural checks

Date: 2026-10-03. Reviewer: `/root/ch05_workflow`; coordinator inspected the code and focused test cases. Source freeze: c8f1ad0236c12f7700419977bdb66a69464f1f1f.

All 94 structural tests pass: 36 translation-pipeline tests, 37 scoped-continuation tests (including 16 chapter 5 cases), and 21 aggregate tests. These verify source/coverage integrity and release boundaries; they do not certify Tibetan readings or English meaning. The 30 semantic regression fixtures in the translation standard were not newly executed.

The first combined continuation run encountered a synthetic fixture-setup error after its chapter 5 and chapter 3 cases passed. The isolated chapter 4 suite passed 11/11. A full continuation rerun with an explicit scratch temporary directory then passed 37/37 in 133.990 seconds without a production-code change. The exact cause of the initial fixture interference was not established; it is not reported as a production defect. All test fixture directories were removed after completion.

The real read-only chapter 5 prior gate passed against the committed authorization: chapter 1's genuine annotated release, chapter 2/3 signed candidates and the exact chapter 4 unsigned saved snapshot, bound native inputs and output hashes. Chapter 4's saved 396-note candidate also reproduced unchanged under its own working authorization. Chapter 5 source-only validation passed for all 416 objects in 135 pairs before English drafting.

Normal prior-release checks, final mode and the eight-release aggregate gate remain strict. The chapter 5 exception does not authorize chapter 6 or manufacture chapter 4's missing final records. Signed-content and final candidate validation will be recorded separately after English and audit completion.

## Complete first draft verification

The full 135-pair / 416-object draft, with 478 notes and all 432 required source obligations, was built and passed read-only draft-candidate validation before final lexical and note refinements. This preliminary build manifest was `3cbb5e7c8800ac6edb5b82ca91af3383a180c4ef60cb963cb5899ad70a7a62bd`; the complete generated checkpoint is `741e5d17c52640e634932662b1a3102f3686acc0`. It is not the final reviewed binding.

Before any signoff, the chapter 5 content gate rejected with “Unsigned translation: final signoff missing.” Strict final validation rejected the missing genuine `translations/publication/ch02-v1.json` receipt. Combining final validation with the draft-continuation flag rejected with “Draft continuation cannot be used for final validation or release.” These are expected boundary rejections, not formal final-mode passes.

## Final reviewed working candidate

Final English SHA-256: `67505fa2bf43bee10a240fcbea61772e44a02b2404ef6cb8afe312aef58849e7`. Final manifest: `0afe04a17427ac29e9aff38de4e8c469e9aafbd7a011a9a8acb4a6a49e1abd02`. The rebuilt candidate and read-only validation pass; independent QC and coordinator signoff are bound to those exact files. The signed content gate passes. Formal final mode remains blocked as described above.

The independent structural reviewer checked all 277 usage records/466 exact source loci and 224 inactive eight-column proposals: every locus has valid source, pair, local definition and actual reference bindings. The 520 notes cover 432/432 source obligations. The final source, audit, evidence and immutable prior snapshots remain unchanged.

The coordinator removed extra boundary spacing from 53 pairs after lexical-note attachment. All 135 final English bodies then match the first full draft byte-for-byte after removing only note-reference tokens, without stripping body whitespace. All 104 verse pairs retain their exact 385 source line counts. The independent structural reviewer verified these final identities and counts and extended its earlier lexical/note approval to the final English hash without repeating unrelated tests. No semantic or human certification is inferred from these checks.
