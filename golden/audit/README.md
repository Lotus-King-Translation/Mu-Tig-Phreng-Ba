# Release audit records

- `test-results.json` and `tests.txt`: 36 chapter and aggregate structural/negative tests passed during whole-book assembly. Exact script/suite hashes are recorded. These tests do not certify Tibetan interpretation.
- `unsigned-final-check.txt`: the aggregate publisher rejected the candidate without signoff before any commit or index mutation; HEAD and the empty index were checked unchanged.
- `intake-integrity.json`: the read-only intake integrity check performed earlier in this edition session verified 367 files, 43 register rows, 12 facsimile manifestations and 1,122 images. Before reusing this result, `git diff --exit-code golden-ch04-v1 -- editions` confirmed the entire intake tree unchanged. This is historical evidence reused for unchanged source files, not a claim that the acquisition was repeated.
- Individual native evidence, pixel identity, final reviews, signoffs and validation records remain with each fixed chapter. Aggregate verification checks their tagged bytes and preserves the distinction between reviewed and unreviewed anchors.
