# Other BDRC work clusters and confirmed image groups

Retrieved 2026-10-02. Raw records plus hashes in `retrieval.json`. This batch adds four catalogue root parts, bringing the BDRC identified-root-part count to **10** across three work records. These are manifestations/copies; independence remains unestablished.

**Correction to batch 01:** `W3CN3207` is the **49-volume China Tibetology Research Center Nyingma Gyübum compilation**, not the Sichuan 2016 Seventeen Tantras. The latter is `MW3CN7084` / `W3CN7084`, two volumes. Root volume/range in W3CN7084 remains unresolved.

| Work cluster | Part | Collection | Catalogue volume | Catalogue image range | Confirmed image group |
|---|---|---|---:|---:|---|
| WA0RG0060 | MW1KG11703_0003_004 | Adzom, four-volume edition | 3 | 310–429 | I1KG11712 |
| WA0XL6A6ADDB434FB | MW27491_4BA695 | Tharpaling / Drug Sherig Press | 2 | 271–354 | I4448 |
| WA0XL6A6ADDB434FB | MW3PD988_48295D | Dzongsar manuscript collection | 148 | 263–400 | I3PD1346 |
| WA0XL6A6ADDB434FB | MW21521_6A6ADD | Tsamdrak Nyingma Gyübum | 12 (ancestor path) | Printed extent 304.7–393.7; scan indices unresolved | I0615 (vol 12) |
| WA0XL60123BEBEC01 | MW21518_60123B | Tingkye Nyingma Gyübum | 9 | 531–585 | I1764 |
| WA0RG0060 | MW2PD17382_0038_003 | Zhichen manuscript Nyingma Gyübum | 38 | 218–292 | I1KG81310 |
| WA0RG0060 | MW1BL6_0032_009 | Gadkar manuscript; rearranged reproduction W1ER156 | 32 | 926–1014 | I1ER907 |
| WA0RG0060 | MW1ER119_0006_1 | Seventeen Tantras, NGMPP AT0062/0063 microfilm | 6 | 3–84 | I1ER795 |
| WA0RG0060 | MW3CN3207_O3CN3207_M0YTTN | CTRC 49-volume compilation | 4 | 136–201 | I3CN3237 |
| WA0RG0060 | MW1KG14783_0005_007 | Paltség compilation | 0 anomaly (part ID suggests 5) | 332–424 | unresolved |

Image group numbering is confirmed through `bdo:volumeNumber` and `bdo:volumeOf` records. Ranges still require visual boundary checks. IIIF endpoint format: `https://iiifpres.bdrc.io/il/v:bdr:GROUPID/manifest` (individual access not yet tested in this batch).

## Reproduction and title cautions

- W1ER156's scan metadata explicitly says it uses the same images as W1BL6, reorganized by rKTs to represent a possible original organization. They are **not two independent witnesses**.
- W1KG11703 is four volumes; W1KG892 / Sanje Dorje is three. A bibliography giving Adzom volume 2 pp. 417–537 cannot be transferred to W1KG11703 volume 3 without inspecting both. Repackaging is plausible but unproved.
- `MW21518_60123B` catalogues volume 9; Dra Thal Gyur in the same collection is in volume 10. Do not reuse the latter's group.
- Dzongsar's stated printed extent is 69 folios, pp. 261–398, while catalogue image bounds are 263–400.
- BDRC searches returning HTTP 404 for `mu tig` in MW1ER7, MW1ER128, MW1ER124, MW1KG892 and MW3CN7084 establish only that this outline lookup found no result. They do not establish that the collection lacks the text.

Completed: 10 root parts; 9 image-group mappings (Tsamdrak mapping is volume-only, without image bounds). Remaining: visual boundary/access checks, older Adzom/modern Sichuan/uncatalogued collections, exact Tsamdrak scan range and Paltség anomaly. No proofreading or collation performed.
