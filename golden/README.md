# Golden Tibetan edition — bounded v1

[Read the Tibetan text](reading.md) · [Machine reading](reading.json) · [Coverage and uncertainty](coverage.json) · [Build manifest](build-manifest.json)

This whole-book edition preserves eight individually signed and published chapter readings. Every one of the 2,053 original electronic anchors remains ordered and accounted for; any restorations retain separate IDs. Roles, source layers, exact selected strings and uncertainty notes are copied unchanged from those releases.

## Source and attribution

The governing printing is the Sanje Dorje Adzom reproduction (1973–1977), BDRC W1KG892, image group I1KG895, printed pages 417–537. See the [selection record](../diplomatic/GOVERNING-WITNESS.json) and [source register](../editions/REGISTER.csv).

The electronic base is [Wikisource Tibetan revision 1028862](https://wikisource.org/w/index.php?oldid=1028862); the same-family comparator is [Wylie revision 274319](https://wikisource.org/w/index.php?oldid=274319). Both are attributed by their archived talk pages to Jim Valby, f69. Attribute Wikisource contributors; their [page histories and provenance](../editions/research/etexts-translations/wikisource/README.md) are preserved in the repository. This adapted text is shared under [Creative Commons Attribution–ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The chapter apparatus identifies editorial changes; scan-source rights remain separately recorded.

## Scope and limits

- Maintained reading of the selected Adzom printing; not an eclectic reconstruction or an infallible text.
- Targeted governing-scan checks were performed; full scan proofreading was not performed.
- The Tibetan and Wylie e-texts belong to one transcription family; their mechanical equivalence is not independent witness agreement.
- Exhaustive witness collation and independent human palaeographic certification were not performed.
- Visible source gaps, unresolved annotations and other uncertainties remain explicit. No unattested wording is silently restored.
- Untargeted source punctuation and decorative signs are not silently supplied or normalized.
- No English translation is included in this release.

## Fixed chapter releases

| Chapter | Release | Publication receipt |
| --- | --- | --- |
| 1 | [golden-ch01-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch01-v1) | [Receipt](../diplomatic/publication/ch01-v1.json) |
| 2 | [golden-ch02-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch02-v1) | [Receipt](../diplomatic/publication/ch02-v1.json) |
| 3 | [golden-ch03-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch03-v1) | [Receipt](../diplomatic/publication/ch03-v1.json) |
| 4 | [golden-ch04-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch04-v1) | [Receipt](../diplomatic/publication/ch04-v1.json) |
| 5 | [golden-ch05-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch05-v1) | [Receipt](../diplomatic/publication/ch05-v1.json) |
| 6 | [golden-ch06-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch06-v1) | [Receipt](../diplomatic/publication/ch06-v1.json) |
| 7 | [golden-ch07-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch07-v1) | [Receipt](../diplomatic/publication/ch07-v1.json) |
| 8 | [golden-ch08-v1](https://github.com/Lotus-King-Translation/Mu-Tig-Phreng-Ba/tree/golden-ch08-v1) | [Receipt](../diplomatic/publication/ch08-v1.json) |

## Reproduction

`python scripts/build_golden_aggregate.py build` requires all eight chapter signoffs and receipts, runs each final validator, and compares released file contents with their annotated Git tags. `verify` regenerates the aggregate in memory and compares exact output bytes without writing. The build is deterministic; `golden/` files above are generated, not hand-edited. Aggregate final review, signoff, release tag and publication receipt are authored and published separately.

