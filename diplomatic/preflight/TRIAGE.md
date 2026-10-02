# Preliminary structure and defect triage

**50 candidate checks; 0 scan decisions.** Both archival poem payloads were traversed in full: 2,053 lines each. No text was corrected or normalized. This is the finite preflight inventory for sequential chapter contracts.

Stable IDs are the one-based `splitlines(keepends=True)` index, including initial blank (`MTP-S000001`). Offsets in TRIAGE.json are exact half-open Unicode-character offsets, including LF; all target strings are copied verbatim.

## Chapter structure

| Chapter | Anchor lines | Count | Closing line | Tibetan offsets | Wylie offsets | Page-marker hints | Checks |
|---|---:|---:|---:|---:|---:|---|---:|
| 1 | 1–97 | 97 | 97 | 0–2167 | 0–2651 | 417–423 | 4 |
| 2 | 98–221 | 124 | 221 | 2167–5393 | 2651–6513 | 423–429 | 3 |
| 3 | 222–341 | 120 | 341 | 5393–8483 | 6513–10225 | 429–436 | 3 |
| 4 | 342–635 | 294 | 635 | 8483–16002 | 10225–19225 | 436–454 | 5 |
| 5 | 636–1051 | 416 | 1051 | 16002–26532 | 19225–31932 | 454–480 | 10 |
| 6 | 1052–1427 | 376 | 1427 | 26532–36374 | 31932–43913 | 480–502 | 9 |
| 7 | 1428–1769 | 342 | 1769 | 36374–45098 | 43913–54517 | 502–520 | 8 |
| 8 | 1770–2053 | 284 | 2035 | 45098–52508 | 54517–63399 | 520–537 | 8 |

Chapter8 closes at2035; lines2036–2053 are final prose/colophon/notices/blessings provisionally assigned to its release. This allocation requires the final source-layer check.

## Full-run structural findings

- 120 page-marker lines, eight chapter-marker lines and one blank line leave1,924 text-bearing lines. Both electronic marker sequences agree; page536 is absent from both, not proven missing text.
- Lines6/7 juxtapose `rgya gar skad du` / `bod skad du`; no Sanskrit-title payload is present between them.
- Tibetan payload contains no literal Latin characters or other non-Tibetan/non-whitespace characters. Wylie has one trailing ASCII space, line1489; preserve it in archival anchors.
- LF is the only line separator; both payloads end with LF. No double ASCII spaces in either payload.
- Shared strings do not establish physical-witness agreement: the two renditions are one transcript family.

## Finite candidate scan queue

Printed pages below are locator hints, not accepted evidence. In this Adzom scan, candidate IIIF indices are printed page+10. Verify visible text before accepting allocation. “High/medium/low” describes why to inspect, not certainty of error. No replacement readings are proposed.

### Chapter 1: 4 checks

- **MTP-TRIAGE-001** — pages 417, 418; structure/layer; high. Title, Sanskrit-language heading immediately followed by Tibetan-language heading, invocation. No Sanskrit-title string is supplied between lines 6 and 7; inspect scan before diagnosing omission or restoration.
  4: `mu tig rin po che phreng ba'i rgyud ces bya ba bzhugs`; 6: `rgya gar skad du`; 7: `bod skad du`; 8: `mu tig rin po che phreng ba'i rgyud ces bya ba`; 9: `bcom ldan 'das rig pa'i bdag nyid 'khrul pa mi mnga' ba nyid la phyag 'tshal lo`
- **MTP-TRIAGE-002** — pages 421; unusual_form; medium. rim po che: unexpected lexical form in a list of families. Candidate source check only.
  42: `rim po che'i rigs dang`
- **MTP-TRIAGE-003** — pages 422; unusual_form; high. dan ends an otherwise repeated dang list. Check exact glyph; do not normalize from list grammar.
  78: `lha ma yin dan`
- **MTP-TRIAGE-004** — pages 423; chapter_boundary; high. Classify complete chapter-one closing formula and marker boundary.
  96: `zhes mu tig phreng ba'i rgyud gsang ba las`; 97: `gleng gzhi'i le'u ste dang po'o`

### Chapter 2: 3 checks

- **MTP-TRIAGE-005** — pages 424; possible_interleaving/lineation; high. Long strings containing 'das shes su bdal and bar dor plus two short adjacent lines merit main-text/annotation and line-allocation checks. These are only candidates; short or long lines alone do not prove annotation.
  117: `ma rig 'khor ba 'das shes su bdal`; 124: `ye shes snang ba bar dor bu la snang`; 128: `rig pa'i mthong phye`; 129: `stong snang bar gyur`
- **MTP-TRIAGE-006** — pages 427, 428; possible_abbreviation/layer; high. Literal zhes pa nas may signal an abbreviated quotation, cross-reference or source note. Inspect surrounding long lines and ma la zha; do not expand from a parallel passage without source evidence.
  178: `stong pa nyid kyi dngos po las 'das pa'i ye shes la`; 183: `da ltar snang zhing 'od lnga ltar 'byung`; 184: `rig pa'i snang ba 'od gsal ba`; 185: `zhes pa nas`; 186: `sna tshogs zhen pa rang grol te`; 188: `dran byed bsam pa'i chos las 'das ste`; 193: `'khrul pa'i ye shes ma la zha`
- **MTP-TRIAGE-007** — pages 429; chapter_boundary; high. Classify chapter-two closing formula.
  220: `zhes mu tig phreng ba'i rgyud gsang ba las`; 221: `'khrul pa gzhi las ldog pa'i le'u ste gnyis pa'o`

### Chapter 3: 3 checks

- **MTP-TRIAGE-008** — pages 429; ritual_formula; medium. sar ba 'dus ha is a ritual-formula candidate; preserve source spelling and establish allocation rather than repair Sanskrit.
  228: `ma bzhugs pa yi stan las langs`; 229: `sar ba 'dus ha sgra brjod nas`; 230: `'dus pa'i tshogs la bka' stsal pa`
- **MTP-TRIAGE-009** — pages 434; unusual_form/structural_number; medium. lug rgyud, snyin po and gsum in adjacent short verses warrant a finite source check. Contraction or source variant remains possible.
  309: `ngo bo rmad byung lug rgyud rgya`; 315: `snyin po nyid la snying po brtan`; 316: `nges pa'i gsum man ngag 'di`
- **MTP-TRIAGE-010** — pages 436; chapter_boundary; high. Classify chapter-three closing formula.
  340: `zhes mu tig phreng ba rin po che'i rgyud gsang ba las`; 341: `'khrul pa la bzla bar bstan pa'i le'u ste gsum pa'o`

### Chapter 4: 5 checks

- **MTP-TRIAGE-011** — pages 436; possible_lineation; low. dur followed by them across transcript lines: verify printed line allocation and word division; unusual wording is not proof of corruption.
  355: `sangs rgyas sems can kun gyi dur`; 356: `them zhing yang dag don la spyod`
- **MTP-TRIAGE-012** — pages 442; possibly_broken_string; medium. yid bzhin dgongs par ye nas pas is syntactically unusual. No replacement is proposed.
  456: `yid bzhin dgongs par ye nas pas`
- **MTP-TRIAGE-013** — pages 443; unusual_form; high. Repeated dir in dir ma and dir med may be transcript transposition or printed spelling; verify scan.
  469: `dir ma rnams ni rang dag pas`; 470: `dir med zang thal chen por gnas`
- **MTP-TRIAGE-014** — pages 453; structural_number; medium. bdun tshan bdun and zla bcu form adjacent numerical statements. Check exact numbers without arithmetic correction or biological harmonization.
  618: `bdun tshan bdun gyi rtogs tshad do`; 619: `zla bcu sa rnams bgrod pa nyid`
- **MTP-TRIAGE-015** — pages 454; chapter_boundary; high. Classify chapter-four closing formula.
  634: `zhes mu tig phreng ba rin po che'i rgyud las`; 635: `'bad med rang grol gyi le'u ste bzhi pa'o`

### Chapter 5: 10 checks

- **MTP-TRIAGE-016** — pages 454; possibly_broken_string; medium. ji ltar ngas and short bdag cag rnams ni gyur na warrant checking against the scan; no absent word is inferred as fact.
  640: `sems can rnams la ji ltar ngas`; 645: `bdag cag rnams ni gyur na`
- **MTP-TRIAGE-017** — pages 455; possible_interleaving; high. gnyis ni gzhi ngo bo gcig khyad par las is unusually expanded against adjacent verse units. Check for smaller interlinear words; no automatic deletion.
  651: `gnyis ni gzhi ngo bo gcig khyad par las`
- **MTP-TRIAGE-018** — pages 459; unusual_form; high. ya ma brla: unusual consonant sequence in both renditions.
  721: `gsog dang ya ma brla dang ni`
- **MTP-TRIAGE-019** — pages 461; unusual_form; medium. dum grags in this repeated negative sequence merits checking; retain if source-supported.
  756: `chos zhes ming du dum grags pas`
- **MTP-TRIAGE-020** — pages 463; unusual_form; high. bcung du dril: check unusual initial cluster.
  793: `bcung du dril bas rig pa gsal`
- **MTP-TRIAGE-021** — pages 466; unusual_form; high. gnyis lang mi ltos contrasts nearby recurring list structure; inspect exact source and word division.
  838: `'khor 'das gnyis lang mi ltos`
- **MTP-TRIAGE-022** — pages 470; unusual_form; high. pe nas occurs amid recurring ye nas phrases; evidence must decide.
  902: `grub mthas pe nas bskyangs dang bral`
- **MTP-TRIAGE-023** — pages 472; unusual_form/word_division; medium. dril sogs: verify consonant and word division, without introducing an expected term.
  944: `sgra med dril sogs pa med`
- **MTP-TRIAGE-024** — pages 478; unusual_form; high. kun rdzog occurs twice on the same page; check repeated spelling against scan.
  1027: `don dam kun rdzog gzugs can no`; 1032: `'jig rten kun rdzog tsam du ste`
- **MTP-TRIAGE-025** — pages 479, 480; chapter_boundary/unusual_form; high. mu ting in work title plus closure split over page markers479/480; classify both title formula and chapter-five closure.
  1049: `zhes mu ting phreng ba rin po che gsang ba'i rgyud las`; 1051: `gnas lugs 'khrul pa rang rdzogs su bstan pa'i le'u ste lnga pa'o`

### Chapter 6: 9 checks

- **MTP-TRIAGE-026** — pages 480; unusual_form; medium. gongs pa spelling in question: check exact printed form.
  1056: `de nyid gongs pa ji ltar lags`
- **MTP-TRIAGE-027** — pages 481, 482; unusual_form; high. sags and skom in formulaic enumerations; check against governing scan, not merely parallel wording.
  1085: `sangs rgyas sags dkon mchog nga`; 1089: `lta dang skom dang spyod pa nga`
- **MTP-TRIAGE-028** — pages 486; unusual_form; high. sungs in recurring request formula; verify printed initial cluster.
  1150: `bcom ldan 'das kyis bdag la sungs`
- **MTP-TRIAGE-029** — pages 489; possibly_broken_string; high. dmyal ba par and rnams lan bun ltar: check allocation/word division and unusual spellings.
  1199: `dmyal ba par ni me chur snang`; 1201: `byol song rnams lan bun ltar`
- **MTP-TRIAGE-030** — pages 490; unusual_form; high. shes krab: unusual cluster requires scan evidence.
  1216: `thabs dang shes krab nyid du grol`
- **MTP-TRIAGE-031** — pages 492; unusual_form; high. mya ngang 'das: verify nasal ending in recurring phrase.
  1256: `'byung ba lnga nyid mya ngang 'das`
- **MTP-TRIAGE-032** — pages 495; possible_interleaving/unusual_form; high. g.yas pa ro ma is an expanded phrase; yan lag ca is truncated-looking. Inspect source layers and exact ending without silently rewriting either.
  1306: `g.yas pa ro ma kun rdzob thig le ste`; 1307: `bde ba chen po'i yan lag ca`; 1311: `don dam chos sku'i rang bzhin can`; 1312: `stong gsal thig le gcig tu gnas`
- **MTP-TRIAGE-033** — pages 499; unusual_form; high. rgyad occurs in an explanation of lamp terminology; verify exact glyph.
  1364: `rgyad ni sgo lnga'i rta pho la`
- **MTP-TRIAGE-034** — pages 502; chapter_boundary; high. Classify chapter-six closing formula.
  1426: `zhes mu tig phreng ba rin po che gsang ba'i rgyud las`; 1427: `sems can gyi snang ba thabs la mkhas pa bstan pa'i le'u ste drug pa'o`

### Chapter 7: 8 checks

- **MTP-TRIAGE-035** — pages 503; unusual_form; low. rol in a sensory list; may be source wording, so do not harmonize to an expected list.
  1451: `dri dang rol dang sgra dang reg`
- **MTP-TRIAGE-036** — pages 506; unusual_form; medium. dngos bo and brgags: verify unusual forms and any source-layer distinction.
  1506: `de phyir bla dang dngos bo yi`; 1507: `chos ni brgags pa nyid du'o`
- **MTP-TRIAGE-037** — pages 507; unusual_form; high. smin lam in a list of perfections; exact source evidence controls treatment.
  1522: `stobs dang smin lam ye shes dang`
- **MTP-TRIAGE-038** — pages 508; unusual_form; high. brag pa bcas in a paired phrase with zag med; verify printed glyphs.
  1549: `brag pa bcas dang zag med dang`
- **MTP-TRIAGE-039** — pages 514; unusual_form; high. rtos: unusual contracted-looking ending; do not add a letter without source support.
  1661: `mdo sde chos nyid zab mo rtos la`
- **MTP-TRIAGE-040** — pages 516; unusual_form; high. lgas: unexpected consonant order in recurring ma ... na formula.
  1700: `de nyid rigs pa ma lgas na`
- **MTP-TRIAGE-041** — pages 519; unusual_form; medium. dum gzugs: check exact wording without doctrinal harmonization.
  1751: `dum gzugs snang lus med pa'o`
- **MTP-TRIAGE-042** — pages 520; chapter_boundary; high. Classify chapter-seven closing formula.
  1768: `zhes mu tig phreng ba rin po che'i rgyud las`; 1769: `'khor 'das kyi chos thams cad rang la rdzogs par bstan pa'i le'u ste bdun pa'o`

### Chapter 8: 8 checks

- **MTP-TRIAGE-043** — pages 523; possibly_missing_text/structural_number; high. gnad gsum followed by lus dang dang yul: duplicated dang with no intervening noun. Inspect source; any restoration requires separate ID.
  1823: `gnad ni rnam pa gsum dag gis`; 1824: `de yi don nyid nyams su blangs`; 1825: `lus dang dang yul nyid do`; 1826: `lus kyi gnad ni rnam gsum ste`
- **MTP-TRIAGE-044** — pages 526; unusual_form; high. lta se and rgyad: verify exact printed endings.
  1861: `rang bzhin rgyud ni 'di lta se`; 1873: `snying po rdzogs pa'i rang bzhin rgyad`
- **MTP-TRIAGE-045** — pages 528; possible_interleaving; high. lam drang po within expanded ground/path/result verse may contain interlinear material. This is a layer check, not authority to remove words.
  1903: `gzhi dang lam drang po dang 'bras bu yis`
- **MTP-TRIAGE-046** — pages 530, 531; structural_number/list; medium. Inspect tantra-name enumeration as printed. The received list contains18 names; do not force it to the conventional corpus label Seventeen Tantras.
  1939: `rgya mtsho dang ni nyi ma dang`; 1940: `seng ge dang ni ri rgyal dang`; 1941: `531`; 1942: `'khor lo dang ni lde mig dang`; 1943: `ral gri dang ni gsal shing dang`; 1944: `gser zhun dang ni ma bu 'brel`; 1945: `me long dang ni mu tig brgyus`; 1946: `sbrul mdud dang ni khyung chen dang`; 1947: `chu rgyun dang ni spu gri dang`; 1948: `rgyal pos dang ni bang mdzod dang`; 1949: `de ltar rnam par phye bas ni`
- **MTP-TRIAGE-047** — pages 533; unusual_form; high. go zhub: check exact source syllable.
  1977: `go zhub ldan pa'i sgo bsrung 'dra`
- **MTP-TRIAGE-048** — pages 533, 534; structural_number/list; medium. Enumerated groups total18 if counted 2+2+2+2+4+3+2+1. Check printed numerals as a finite list; never repair arithmetic to17.
  1981: `de yang rgyud kyi rim pa ni`; 1982: `rtsa ba'i rgyud ni gnyis kyis ni`; 1983: `chos kun gcig pa nyid du bshad`; 1984: `bshad rgyud ma bu gnyis kyis ni`; 1985: `lo 'dab rgyas pa'i tshul du bshad`; 1986: `yan lag rgyud ni gnyis dag gis`; 1987: `rgya mtshor gza' skar shar bzhin bshad`; 1988: `lung rig gsal ba'i rgyud gnyis kyis`; 1989: `me tog kha bye'i tshul du bshad`; 1990: `man ngag rgyud sde bzhi yis ni`; 1991: `534`; 1992: `'bras bu smin pa'i tshul du bshad`; 1993: `dgongs pa rang gnas rgyud gsum gyis`; 1994: `mthong byed mig gi tshul du bshad`; 1995: `'jug pa rang grol rgyud gnyis kyis`; 1996: `dran gzhi snying gi tshul du bshad`; 1997: `mkhas pa cho ga'i rgyud kyis ni`; 1998: `me la tshe byed pa'i khye ltar bshad`
- **MTP-TRIAGE-049** — pages 535; unusual_form; high. brab mo and thus in final summary: check source letters and possible smaller notes.
  2020: `mdo ni brab mo'i don du bsdu`; 2026: `gnas pa thus te cit ta'i dkyil`
- **MTP-TRIAGE-050** — pages 535, 536, 537; chapter_boundary/page_gap/colophon_layers; high. Last chapter closing, final prose, work ending and commentary notice span the535→537 marker jump. Inspect printed535–537, classify final notices/blessings, and distinguish absent page marker from missing textual span.
  2034: `zhes mu tig phreng ba rin po che'i rgyud las`; 2035: `rgyud thams cad bsdoms te bstan pa'i le'u ste brgyad pa'o`; 2036: `de skad ces sems med pa'i rig pas bka' stsal pa dang`; 2037: `rig pa rdo rje rnon po la sogs pa`; 2038: `rigs lnga'i de bzhin gshegs pa dang`; 2039: `537`; 2040: `rigs gsum gyi khro bo dang`; 2041: `sangs rgyas chos dang dge 'dun dang`; 2042: `lha dang lha ma yin dang`; 2043: `mkha' 'gro ma dpag tu med pa dang`; 2044: `dri zar bcas pa'i 'jig rten yi rang ste`; 2045: `bcom ldan 'das kyis gsungs pa la mngon par bstod do`; 2046: `mu tig phreng ba rin po che gsang ba'i rgyud ces bya ba`; 2047: `rang bzhin rdzogs pa chen po'i rgyud 'bum phrag drug cu rtsa bzhi'i khyad par du phyung ba'o`; 2048: `rdzogs so`; 2049: `mu tig phreng ba'i rgyud kyi 'grel pa gsal byed ces bya ba yod`; 2050: `mu tig phreng ba'i rgyud la ma bu gsum`; 2051: `dge'o`; 2052: `dge'o`; 2053: `dge'o`

## Limits

No native images were examined for this triage; no dictionary spellcheck, full scan proofreading or exhaustive witness collation was performed. The scan queue remains50 unchecked candidates. The coordinator may freeze these into chapter contracts, recording every later disposition; this report itself authorizes no spelling repair, missing-span expansion, numerical harmonization or source-layer deletion.
