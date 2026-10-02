# Wikisource original snapshots

Acquired 2026-10-02 from normal public `index.php` URLs, preserved byte-for-byte. `manifest.json` records the requested URL, revision where fixed, byte count, content type, and SHA-256 of each file. Nine originals acquired; nine hashes verified. These files supersede batch-01's unacquired status for the Wikisource records. No normalization or editorial changes were made.

## Attribution and licensing

Source host: Wikisource. Both text-page HTML snapshots explicitly link https://creativecommons.org/licenses/by-sa/4.0/ as their license. Attribute Wikisource contributors and preserve the source-page and history links in derivative use. Original source-transcriber provenance is the uploader's claim: Jim Valby, f69, A-'dzom blocks of the Seventeen Tantras. The archived talk pages are evidence for that claim, not scan certification.

Wylie text history: all five revisions are by **B9 hummingbird hovering**, 2010-03-27. Current text revision **274319**, 07:33:50 UTC. Tibetan history: **B9 hummingbird hovering** supplied the text in revision **274320**, 2010-03-27 07:34:48 UTC; **Great Brightstar** added eight bytes in revision **411925**, 2015-03-30; **Sowhat666** added 124 bytes in revision **1028862**, 2024-03-01. Both talk-page provenance statements are by B9 hummingbird hovering. History HTML files preserve all visible revisions and contributor links.

## Shared transcription family and transformations

Both talk pages explicitly identify the same Valby f69/A-'dzom source. Wylie and Tibetan `<poem>` payloads each have 2,053 lines as counted by Python `splitlines()` (including initial empty line). Their order, numeric page markers, chapter divisions, and terminal colophon correspond. Treat the Tibetan page as a script-conversion-family rendition, not an independent witness. The conversion software and original conversion procedure are not stated in the saved history; do not invent them. Full equivalence between the two script forms has not been checked.

The Tibetan `<poem>` payload from revision 274320 (2010) is exactly identical to revision 1028862 (2024); comparison used direct string equality after extracting the content between `<poem>` and `</poem>`. Later changes affect the wrapper/categories, not that payload. This proves preservation across those revisions, not accuracy against the physical print.

The page markers include 535 followed by 537 at the end. Verify against physical images before describing missing text. No complete scan proofreading or witness collation was performed.

## File roles

- `*-raw.wiki`: unmodified wikitext text-page originals.
- `*-talk-raw.wiki`: unmodified provenance statements.
- `*-history.html`: attribution history snapshots, acquired-date state (not immutable endpoint).
- `*-page.html`: fixed-revision HTML, preserving title, displayed text, metadata, and license.
- `manifest.json`: authored acquisition metadata.
- This README: authored account of the acquisition and bounded checks.
