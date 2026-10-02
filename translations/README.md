# String of Pearls — English working edition

The translation follows the fixed [golden-v1 Tibetan edition](../golden/reading.md), under the unchanged [glossary](../glossary/expanded_tibetan_english_glossary.csv) and [translation/QC standard](../guidelines/tibetan_translation_standard_v2.md).

Work proceeds through eight sequential chapter releases. See [current status](HANDOFF.md), [source pins and coverage plan](PLAN.json), and [endnote policy](ENDNOTE-POLICY.md). Until all eight chapters are released, the canonical paired files explicitly declare their chapter-prefix scope.

Endnotes distinguish actual Adzom differences, electronic transcript corrections that agree with Adzom, omitted source annotations, presentation conventions, uncertain readings, and translation or terminology questions. The translation phase compares every chapter's governing main-text span against the native print; untranscribed annotations and unreadable wording remain explicit. This is an agent-produced working translation for human review.

Authoring and validation are documented in [PIPELINE-SCHEMA.md](PIPELINE-SCHEMA.md). Each chapter freezes exact source pairs before English drafting, then binds the complete native audit, endnotes, author self-check, independent agent QC, and release signoff. The Tibetan and canonical glossary are never rewritten by this workflow.

Canonical content is in `paired/source.md` and `paired/translation.md`, mirrored by fixed chapter snapshots. Chapter `reading.md`, `bilingual.md`, `machine.json`, coverage and build manifests are generated from those snapshots. `translation-draft.md` preserves the initial authored English before the coordinator attaches the source apparatus; subsequent reviewed changes have a separate change record.
