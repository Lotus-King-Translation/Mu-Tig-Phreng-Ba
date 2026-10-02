# BDRC access, provenance and exclusions

Retrieved 2026-10-02. Raw metadata, selected manifests and query results have retrieval URLs and SHA-256 in `retrieval.json`. `access-observations.json` distinguishes successful manifests, previews and HTTP 401 failures.

## Findings that change classification

1. **The two Adzom publications share a print source.** MW1KG892's Tibetan bibliography explicitly states that it and MW1KG11703 differ only as reprints and have the same printing base: `འདི་དང་དཔེ་རྒྱུན་ཨང་MW1KG11703་གཉིས་བསྐྱར་པར་མི་འདྲ་བ་ཙམ་ལས་པར་གཞི་གཅིག་པ་ཡིན།` Treat them as separate manifestations/copies, not independent textual witnesses. The older three-volume publication's volume 2 is I1KG895 (547 exposed canvases); the four-volume publication uses volume 3, I1KG11712. Exact root boundaries still require visual verification.
2. **Gadkar photographs have a separate image licence.** W1BL6 scan metadata attributes the 2023 photographs to the Tibetan Manuscript Project Vienna under CC BY-NC 4.0. MW1BL6 marks the historical work Public Domain. W1BL6 (in-situ ordering) and W1ER156 (rKTs reordering) reproduce the same manuscript and images. Preserve this image licence even where a general catalogue field says Public Domain. The openly returned I1ER907 manifest does not itself contain a `license` field. No restricted image endpoint was circumvented.
3. **Spiti 1977 excludes String of Pearls.** MW21520's Tibetan bibliography explicitly lists `མུ་ཏིག་ཕྲེང་བའི་རྒྱུད་` among seven missing tantras. This is stronger than mere absence from a short table of contents. The note suggests that omitted texts might remain at the source monastery; that is a research lead, not an acquired/confirmed Pearls witness.
4. **Sangyeling's volume 12 is absent.** MW1KG16449's note reports whole volumes 11, 12 and 41 missing. A Tsamdrak-like ordering would place Pearls in volume 12, but that match has not been established. Keep this as an unresolved collection lead, not a confirmed Pearls manifestation.
5. **Rigzin Tshewang Norbu has a digitized reproduction, but tested manifests are restricted.** MW2PD19896 identifies W2PD19896, with 31 digital volume groups. I2PD20024 is digital volume 10; adjacent groups I2PD20022/23 are volumes 8/9. All three manifests returned HTTP 401. rKTs Gtn010.006 gives ff. 122a4–145b6; its numbered volume has not been equated with the reorganized digital-volume sequence. No image access was attempted after the 401 findings. The catalogue's English description and Tibetan note disagree on surviving volume counts; retain the original notes.

## Catalogue/image locations resolved

- **Tsamdrak W21521:** child chapter records corroborate I0615, volume 12, images 306–395. First chapter is catalogue image 306 line 2; eighth chapter ends image 395 line 3. Root extent statement is printed 304.7–393.7. These are not fully consistent at line level; inspect adjacent pages 305/306 and 395/396. Do not silently infer the root heading from the chapter boundary.
- **Paltség W1KG14783:** rKTs links I1KG21610, verified by the image-group record as volume 5. This resolves the digital group even though the BDRC root part's volume field says 0. Its manifest exposes only 41 preview canvases; root images 332–424 are not available in that preview.
- **CTRC W3CN3207:** root part remains volume 4, images 136–201, group I3CN3237. Manifest exposes only 41 preview canvases, not the requested full range.
- **Sichuan 2016 W3CN7084:** bibliography explicitly includes Pearls as item 12 of 17. Both I3CN8461 and I3CN8462 expose 41 preview canvases. Root volume/page boundaries are not yet established by this batch.
- Standard public manifests tested here returned 200 for Adzom2000, Tharpaling, Dzongsar, Tingkye, Tsamdrak, Zhichen, W1ER119 and Gadkar. A successful manifest alone does not certify all images downloadable or text complete; acquisition is coordinated separately in `editions/metadata` and `editions/scans`.

## Search scope and disambiguation

The preserved BDRC title searches returned 7 records for `"mu tig rin po che"` and 72 for `"mu tig" AND "rgyud"`; many are unrelated. These searches corroborated the three root-work clusters recorded in batches 01–02. Records titled `mu tig phreng rgyud gsal byed` are commentary/reference works, not additional root witnesses. Likewise the short Pema Lingpa text MW21727_F2C035 and Lingrepa's MW23778_EAB04E were not admitted as root witnesses from title similarity alone.

Completed: 10 previously identified root parts retained; 1 same-print relationship documented; 1 explicit publication exclusion; 1 image-licence distinction; 1 digital group anomaly resolved; Tsamdrak chapter range corroborated. Remaining: coordinator's visual boundary and acquisition work; inaccessible/unmapped collections; independent witness relationships. No collation or full proofreading performed.
