# Electronic repository and translation search boundaries

Checked 2026-10-02. This is a bounded public-discovery pass, not a claim that every existing edition or private translation has been found.

## Repository checks

| Repository | Search performed | Outcome and limit |
|---|---|---|
| Wikisource | Wylie and Tibetan titles; raw fixed revisions; talk pages and complete visible histories | Two renditions acquired in `wikisource/`, sharing Valby f69 provenance. One transcription family. |
| Tsadra | Indexed Tibetan title and Wylie variants across Tsadra domains | Dictionary entries, title references and quotations found; no separate complete root-tantra transcript verified. The French Longchenpa translation noted below is secondary quotation material. |
| Adarshah | Public collection tree and anonymous catalogue for `ngagyurnyingma` (Works of Ngagyur Kama); Tibetan/Wylie title match | No root-title match in the inspected catalogue. Its Nyingma branch lists Ngagyur Kama, Longchenpa and Mipham collections. This is not a full-text search of every collection. Adarshah's unrelated Gampopa String of Pearls is excluded. |
| Esukhia | GitHub code search for quoted Tibetan title, organisation repository inventory | No exact root-tantra repository located. Corpus repositories and canon datasets exist; their contents were not all downloaded or exhaustively searched. |
| OpenPecha / OpenPecha-Data | GitHub Wylie/Tibetan title and collection-title discovery, indexed web search | No distinct root-tantra repository verified. Old `OpenPecha` code-search owner query returned an invalid/unavailable-owner error; no negative conclusion is drawn from that error. Code and hosting have undergone organisational moves. |
| WeBuddhist | Live anonymous `/library/v2/texts` title search for `མུ་ཏིག`, `mu tig`, and `Pearls`, limit 20 | All three responses returned `items: []` and `has_more: false`. Saved verbatim in `search-metadata/`. Only these title queries are ruled out in this response snapshot; not the presence of untitled or differently indexed corpus material. |

Adarshah entry point: https://online.adarshah.org/ . The WeBuddhist public code documents the title endpoint: https://github.com/Webuddhist-tech/WeBuddhist/blob/develop/src/services/library/api.ts . Software licensing is not a license for the text corpus.

## Jim Valby f69

The Wikisource talk pages identify f69 but do not link a publicly downloadable original file. Searches for `"Jim Valby" "f69"`, `"f69" "rgyud"`, `"Valby" "mu tig"`, and `"mu tig rin" "txt"` produced no verified original download. Valby's historical site https://sites.google.com/site/jimvalbythings/ redirects to Google sign-in. No authentication or circumvention attempted. A public original f69 file remains an open acquisition lead.

## Wikisource history exclusion

Earlier Wylie revision 274315 is **not** a second edition of String of Pearls. Direct inspection of its public raw source shows the title `kun tu bzang po klong drug pa'i rgyud`, numbered 111–214, and the matching Six Spaces ending. The editor replaced this mistaken paste with String of Pearls in revision 274319. Do not register the earlier revision as a textual variant. Evidence: https://wikisource.org/w/index.php?title=Mu_tig_rin_po_che_phreng_ba%27i_rgyud&oldid=274315&action=raw . Only inspection performed; the unrelated full text was not added to this repository.

## Language searches and partial-reference leads

The only complete root-tantra translation verified in this pass is Christopher Wilkinson's English 2016 publication, recorded in batch-01. Searches covered English titles, French `Tantra du collier de perles`, Russian `Тантра жемчужного ожерелья` and `Тантра Му тиг`, Chinese simplified/traditional `珍珠鬘续` / `珍珠鬘續`, Italian `Tantra collana di perle`, Spanish `Tantra collar de perlas Dzogchen`, and German `Perlenkette Tantra`. No second complete translation was verified. Non-discovery is not proof of nonexistence; unpublished translations and small-circulation editions remain open.

Useful partial material:

- The University of Virginia Kmaps entry https://terms.kmaps.virginia.edu/features/219191 contains an annotated Wylie passage corresponding to the root tantra's final chapter, with displayed numbers 531–534. Bracketed glosses must remain distinct from root text. Exact manuscript/editorial provenance for the passage is not established here; classify as reference quotation, not an independent witness or complete edition.
- The publisher's account of Malcolm Smith's volumes 1–2 confirms a translated appendix from the String of Pearls commentary: https://wisdomexperience.org/17-tantras/ . Extent and base-text identification need book-level verification.
- Jean-Luc Achard's French *L'Essence de la sagesse primordiale*, volume IV, hosted by Tsadra, contains quotations labelled from the Collier de perles tantra. This is a quotation lead rather than a complete translation of the root tantra; no commercial or copyrighted full text was downloaded: https://rywikitexts.tsadra.org/images/9/94/Essence_Sagesse_Primordiale_vol_IV.pdf . Exact quoted loci have not been inventoried.
- Khenpo Sodargye's public multilingual glossaries identify the French/English/Chinese title equivalences, not full translations: https://khenposodargye.org/content/uploads/2025/04/Glossary-FrenchTibetanChinese.pdf and https://khenposodargye.org/content/uploads/2023/12/Glossary-English-Tibetan-Chinese.pdf .
- The JTL article *The Origins of the Dzogchen Eleven Words and Meanings: Comparing Nyima Bum, Longchenpa, and Rikzin Gödemchen* contains passage translations and compares A-'dzom and Gting skyes readings: https://journaloftibetanliterature.org/index.php/jtl/article/download/69/191/650 . This is secondary textual research, not a full root-tantra edition.

## Further title collisions excluded

- Gampopa, *A String of Pearls: A Collection of Dharma Talks*, Khenpo David Karma Choephel translation (2024): https://dharmaebooks.org/a-string-of-pearls/ . Tibetan `tshogs chos mu tig phreng ba`; unrelated work.
- Jamyang Khyentse Chökyi Lodrö, *The String of Pearls Advice*, Adam Pearcey translation (2020): https://www.lotsawahouse.org/tibetan-masters/jamyang-khyentse-chokyi-lodro/string-of-pearls-advice . Tibetan `zhal gdams mu tig phreng ba`; unrelated work.
- Ratnākaraśānti's *Muktāvalī* on Hevajra, 84000 Toh 1189, and Niguma's similarly titled practice instructions are also excluded; see batch-01.

## Remaining acquisition questions

1. Locate an independently supplied Valby f69 original and establish its date/version.
2. Identify the exact Tibetan manuscript images and editorial basis in Wilkinson 2016 by authorized book access.
3. Verify the full bibliographic description and Tibetan base of Smith's commentary appendix.
4. Revisit OpenPecha/BDRC machine-readable corpora using exact manifestation IDs once the physical-source census supplies them.
5. Follow specialist/library enquiries for unindexed or unpublished translations only if the project authorizes correspondence; no messages sent in this pass.
