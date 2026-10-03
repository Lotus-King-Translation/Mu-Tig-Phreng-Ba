# Chapter 5 structural checks

Date: 2026-10-03. Reviewer: `/root/ch05_workflow`; coordinator inspected the code and focused test cases. Source freeze: c8f1ad0236c12f7700419977bdb66a69464f1f1f.

All 94 structural tests pass: 36 translation-pipeline tests, 37 scoped-continuation tests (including 16 chapter 5 cases), and 21 aggregate tests. These verify source/coverage integrity and release boundaries; they do not certify Tibetan readings or English meaning. The 30 semantic regression fixtures in the translation standard were not newly executed.

The first combined continuation run encountered a synthetic fixture-setup error after its chapter 5 and chapter 3 cases passed. The isolated chapter 4 suite passed 11/11. A full continuation rerun with an explicit scratch temporary directory then passed 37/37 in 133.990 seconds without a production-code change. The exact cause of the initial fixture interference was not established; it is not reported as a production defect. All test fixture directories were removed after completion.

The real read-only chapter 5 prior gate passed against the committed authorization: chapter 1's genuine annotated release, chapter 2/3 signed candidates and the exact chapter 4 unsigned saved snapshot, bound native inputs and output hashes. Chapter 4's saved 396-note candidate also reproduced unchanged under its own working authorization. Chapter 5 source-only validation passed for all 416 objects in 135 pairs before English drafting.

Normal prior-release checks, final mode and the eight-release aggregate gate remain strict. The chapter 5 exception does not authorize chapter 6 or manufacture chapter 4's missing final records. Signed-content and final candidate validation will be recorded separately after English and audit completion.
