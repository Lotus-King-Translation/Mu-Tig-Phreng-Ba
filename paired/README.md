# Paired publication

Canonical content: [Tibetan source](source.md) and [English translation](translation.md), sharing stable pair IDs and order. Read [FORMAT.md](../FORMAT.md) and the [strict pipeline schema](../translations/PIPELINE-SCHEMA.md).

The source is derived exactly from `golden-v1`; its front matter records the fixed commit and SHA-256. Every golden object belongs to one coherent pair. The source alone specifies `format: prose|verse|h1|h2|h3`; English inherits it. Electronic metadata remains separately identified.

During translation these files represent an explicitly declared contiguous chapter prefix. Normal sequencing closes the preceding chapter release gate before starting the next chapter. The owner explicitly authorized chapters 3, 4 and 5 as working continuations while prior publication is pending. Chapter 5 proceeds from the preserved unsigned chapter 4 snapshot after disclosure of its final upload failure. These narrow exceptions are recorded in [DECISIONS.md](../DECISIONS.md) and the chapter [3](../translations/draft-authorizations/ch03.json), [4](../translations/draft-authorizations/ch04.json) and [5](../translations/draft-authorizations/ch05.json) authorizations. Final release checks remain strict. The complete edition will cover all 2,053 golden objects.

English endnotes explain every recorded Adzom difference and retained source uncertainty. Chapter artifacts are retained in `translations/chapters/NN/`, with their actual completeness and review state recorded in the [handoff](../translations/HANDOFF.md). Chapter 4’s saved unsigned draft does not contain its lost final lexical and review records.

Use the strict gate for the active chapter:

```sh
python3 scripts/translation_pipeline.py validate --chapter N --final
```

The generic `scripts/validate_paired.py` checks paired-format syntax only; it does not replace the source, audit, endnote, QC or release gates.
