# Pipeline aggregate output review

**Result: no blocker found.** Finite audit complete: 5/5 generated outputs, 8/8 chapter identities, 2,053/2,053 reading objects, 96/96 uncertainty objects.
Reviewer: golden_pipeline agent. I authored the generator; its code examination is self-review. The actual-output audit below used separate JSON, Git and Markdown checks without importing or regenerating through that generator.

| Reviewed artifact | SHA-256 |
| --- | --- |
| `build-manifest.json` | `66a085a74cf3420c832bcc338cbdf43696cb950d8113ee388992c51c4e361d20` |
| `reading.md` | `75fc6f052921f547e30fabb19e4fb4cc2db232c67c5e04a3449855ea844f7c36` |
| `reading.json` | `dc371e71f4eb0fa842963eebf3ebb0bb7c60e9623a038cf1cdcd3339855be2c1` |
| `coverage.json` | `6b2867ee4d62762787c6c12cda5509820f5fa4669fd2f1bf4e933c840f4bfd35` |
| `README.md` | `9c6214951ff148636122190713d6e06db10a1cb57333c41ef3cc1c7b9cf3a705` |

- Every aggregate object equals the exact ordered concatenation of reading JSON from eight fixed chapter tags, including all fields, roles, original strings, line endings, empty layer arrays and uncertainty. All original IDs occur once; restorations: 0.
- Coverage independently sums to 183 editorial decisions, 102 source checks, 30 changed-text anchors, 50 layer/text changes, 1,870 unreviewed retained anchors, 161 accepted and 10 excluded evidence records; both remaining queues are 0. All four unperformed-work claims remain false; the frozen aggregate contract agrees.
- Markdown source audit: all 2,053 anchors and exact selected text represented; 96 footnotes preserve all 101 uncertainty statements and return links. Role labels preserve 128 metadata, 4 heading, 16 chapter-colophon, 3 annotation and 6 colophon objects; 1 blank and 1,895 main-text objects remain accounted. No nested source layers exist in these releases.
- All 121 local-link occurrences resolve to 23 existing targets; uncertainty links and source/rights attribution remain explicit. Wikisource revision links match the archived provenance, and the archived page HTML contains the stated CC BY-SA 4.0 URL. Separate scan rights are disclosed. External license/source HTTP availability was not rechecked.
- Fresh origin lookup matched all 8 annotated chapter-tag objects and all 8 peeled commits to the aggregate manifest. Reviewed main/remote HEAD: `8e90d9afa1f0889c064871b81822783050d62b30`. Publisher self-review confirms both requested guards: fresh chapter refs and publication-path/index checks; repository-relative root is present.
- Code bindings: generator `9f5dc66d3289bb8bbec45982fc0f56b147e17bce573d854bfd70d145535ec491`; publisher `27445f887a0a972d89993b7363d787010f54bac5351870c7c24b420b3a64d50e`; aggregate contract `12a0374edc767f769f54d938ae8760cedd6936ef7fa4a2feb258d971d05333d1`.
- Limits: this is an object/coverage/Markdown-source audit, not a rendered-browser inspection, new scan proofreading, independent human palaeographic certification, fresh license adjudication or whole-book publication. Final signoff and publication remain coordinator gates.
