# Numbers audit of the v4 narratives

Date: 31 October 2026. Auditor: an AI agent (Claude) working from `review/v4_numbers_audit_brief.md`. Scope: every number and quantitative claim in `report/src/brief.md`, `paper.md`, `analysis_report.md`, `supplement.md`, `collection_round2.md`, `methods_document_discovery.md`, `methods_review_and_revision.md`, and the same numbers in `review/adversarial_review_v3_and_changes_v4.md`, `report/v4_summary.md` and `README.md`.

Method. Every count, share, interval, odds ratio, kappa and "x of y" was extracted and checked against, in order: `data/master_table.csv` through `scripts/analysis_common.py::load()` (usable, embodied_set, legal_text, instrument = principal_instrument, binding_text, binding = binding_text & instrument, content_capture, words_ok, round2), `data/results.json`, `report/results_digest.md`, `tables/*.csv`, `figures/data/*.csv`, `data/reliability_fields*.csv`, `data/reliability_variants.csv`, `data/run_manifest.json`, `data/manual_overrides_v4.csv`, `data/overrides_applied.csv`, `data/duplicates_removed.csv`, `data/round2_inventory.csv`, `review/v3_reviews/precision_audit.md` and `precision_audit_sample.csv`, `review/v3_reviews/governance_audit_rows.csv`, the annotation folders, and (for the version-history values) `/home/user/embodied-ai-governance-v3/report/results_digest.md` and `tables/`. Rounding differences were accepted; every other difference was fixed in place, changing only the number or its qualifier. Set definitions, data files and scripts other than one narrative string of `scripts/21_round2_report.py` were not touched. Nothing was invented: where a value could not be recomputed from the package it was left unchanged and is listed under "Claims not verified".

## Summary

| Document | Quantitative claims checked | Discrepancies fixed | Claims not verified |
|---|---:|---:|---:|
| report/src/brief.md | 44 | 0 | 0 |
| report/src/paper.md | 335 | 13 | 3 |
| report/src/analysis_report.md | 530 | 34 | 2 |
| report/src/supplement.md | 310 | 21 | 4 |
| report/src/collection_round2.md (via scripts/21_round2_report.py) | 125 | 1 | 0 |
| report/src/methods_document_discovery.md | 160 | 8 | 5 |
| report/src/methods_review_and_revision.md | 45 | 1 | 2 |
| review/adversarial_review_v3_and_changes_v4.md | 115 | 1 | 6 |
| report/v4_summary.md | 42 | 1 | 0 |
| README.md | 8 | 1 | 0 |
| **Total** | **1,714** | **81** | **22** |

"Discrepancies fixed" counts claims, not edits (one edit sometimes corrected two numbers). The companion report's fix was made in the script's narrative string and the report regenerated (`python3 scripts/21_round2_report.py && python3 scripts/24_precision_vs_rules.py`, both completed; `results.json` precision keys unchanged: n 100, joint 0.54 (0.44 to 0.63), corrected 161 (132 to 190), rule 61%, agreement 0.77, kappa 0.53, 15 / 8).

## 0. Reference values recomputed from the data (used for every document)

| Quantity | Recomputed value | Source |
|---|---|---|
| annotated / usable / embodied / general / governance / embodied governance / countries | 3,295 / 3,165 / 1,603 / 1,015 / 1,709 / 822 / 116 | loader; results.json; S08 |
| comparable unit: embodied legal texts / binding embodied texts / binding all sets / binding robot-specific / soft embodied / binding embodied families / binding embodied with autonomy or AI provisions | 810 / 291 / 702 / 254 / 411 / 280 / 194 | loader; T53; T53b |
| principal unit: embodied principal / robot-relevant / binding / binding robot-relevant / binding families / binding with autonomy or AI / binding naming AI / principal with autonomy or AI / principal naming AI | 505 / 408 / 195 / 168 / 194 / 140 / 15 / 395 / 153 | loader; T53b; results.json counting_units |
| 195 principal binding: jurisdiction | US 56, EU 34, JP 22, GB 11, CA 9 (132 of 195); INT 5; MY 4; AU 4; CN 4 | loader, `jurisdiction_country` |
| 195 principal binding: doc_type | 132 regulation_or_decree, 60 statute_or_act, 3 court_decision | loader |
| 195 principal binding: status | **182 in_force, 9 superseded_or_repealed, 4 adopted_not_yet_in_force** (writers had 180 / 11 / 4) | loader |
| 195 principal binding: robot types (any) | drones 107, road vehicles 67, delivery 15, industrial manipulators 13, security 11, mobile logistics 9, agricultural 7, collaborative 6, surgical 6, care 4, weapons 3 | loader, `embodied_categories` |
| 195 principal binding: capture | 175 substantive, 20 partial; 18 dated before 2010; 164 principal + 31 amendments; 190 from round 2 | loader |
| 291 binding embodied texts: doc_type | 207 regulation_or_decree, 71 statute_or_act, 9 technical_standard (mandatory GB), 3 court, 1 treaty | loader; S01 (291 rows) |
| 291 binding embodied texts: unit | 164 principal, 31 amendment, 28 ancillary, 28 catalogue_page, 25 stub, 7 dependent, 6 incorporation, 2 language_copy | loader, `instrument_unit` |
| 810 embodied legal texts: unit | 463 principal, 42 amendment, 222 catalogue_page (191 technical standards), 35 stub, 30 ancillary, 10 dependent, 6 incorporation, 2 language_copy | loader |
| 822 embodied governance-flag documents: status | 384 published_current, **272 in_force**, 47 under_development, **42 superseded**, 23 bills, 21 proposals, 21 adopted_not_yet_in_force, 8 consultation_open, **4 withdrawn_or_lapsed**; binding nature 286 / 241 / 236 / 13 / 46 | loader |
| overrides (manual_overrides_v4.csv) | **157 rows, 91 documents, 156 rows on round-2 documents**; instrument_unit 50 (36 catalogue_page, 14 dependent), relevance 32, embodied_categories 32, instrument_status 17 (**9 superseded, 6 in_force, 2 withdrawn_or_lapsed**), doc_class 14 (**6 binding, 5 soft, 3 report**), year 7, binding_nature **5** (technical_standard_mandated); Machinery Directive 2006/42/EC (R2-80171de4) override = in_force | file |
| expert audit rows | 165 rows; 119 with an error code, 107 material (as computed by 21_round2_report.py) | governance_audit_rows.csv |
| round 2 | 2,075 candidates (1,157 agents, 918 harvests); 1,720 with text (1,704 + 16); 355 without (272 / 46 / 37); 189 of those recorded binding; 1,641 in master table; 1,626 usable; 928 embodied; 988 principal; 444 embodied principal; 378 robot-relevant; 745 embodied legal texts (403 principal + 41 amendments, 218 catalogue, 35 stubs, 48 ancillary/dependent/incorporation/language); **286 binding embodied texts** (writers had 277) resolving to 190 / 164 / 135 / 10; 260 technical standards, 200 landing pages; 379 CJK usable; median 848 words vs 2,646 round 1; 254 landing pages | loader; T50-T53; inventory |
| collector metadata vs annotation | binding 0.93 (kappa 0.855, n 1,608); jurisdiction 0.981 (1,624); year 0.938 (1,542); class **0.767 (kappa 0.661)** | T57 |
| round-2 reliability sample | 160 ids: 116 en, 29 zh, 6 ja, 1 ko, 8 other; **63 binding, 52 soft, 23 drafts**, 14 reports, 8 communications; 109 / 24 / 27 captures; median 848 words; 31 under 150 words; 30 technical standards; 96 embodied | annotations/reliability_round2_opus + master table |
| round-2 kappas | Opus: 0.861 over 37 single/ordinal rows, 0.811 over all 129; multi-label means 0.81 / 0.80 / 0.71 / 0.70; re-run 0.910 / 0.886 (127 rows) | reliability_fields_r2opus/r2rerun.csv |
| round-1 kappas | model 0.854 (min 0.606, 11 below 0.80); retest 0.907 (min 0.657); full text 0.884 (0.714); blind 0.897 (0.649); extended 0.827; every reliability folder holds **160** files (the texts said 161 for the re-run) | T26; run_manifest; annotations/ |
| adjusted models (T20) | transparency 0.47, justice 0.27, non-maleficence 2.61, privacy 0.51, beneficence 0.42, trust 0.55, sustainability 0.65, solidarity 0.42, inclusive growth 0.43, human oversight 1.70; accountability 0.77, freedom 0.68, dignity 0.76, robustness 1.38 n.s.; international cooperation 0.59, funding 0.62 | T20 |
| T09 | binding n 195; **soft-law n 207** (physical safety 73.4 / 32.9); standards 62; drafts 77; research 509 | T09 |
| T28 | industrial policy 1.69 (1.24 to **2.31**), Holm 0.027; personhood 0.39 (0.22 to 0.70), 0.040; ethics 0.67, Holm **0.447** | T28 |
| CJK | 422 re-annotated (376 round 2 + 46 round 1; 380 + 46 annotation files); 57 changed set membership; not-AI 205 to 160 | review log; companion report (computed) |

## 1. report/src/brief.md

All 44 quantitative claims match the data (195 / 15 / 505 / 168 / 140 / 107 / 67; five and 299 for v2 and v3; 190 of 195 from round 2; 0 of 14 and 10 of 14 within round; physical safety 57% vs 7% (T20b 57.4 / 6.5); 43% of 509; 15 of 505; care robots four binding; drones 6% / 42%; 61% / 25% / 62% of 195 (T09); 13 binding instruments reaching industrial manipulators; 3,165; 42% European; 75% English; 160 documents, kappa 0.86; 159 rows, 68%, 62%; 100 texts, 54%; 22 of 39; 898 words, within the 900-word limit stated in the review log). No discrepancy; no v3 state presented as current.

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| para 1 | 195 binding, 15 name AI, 505 principal, 168, 140; drones 107, AVs 67 | same | T53b; loader | verified |
| para 2 | 190 of the 195 from round 2; 0 of 14 and 10 of 14; 57% vs 7% | same | loader; T20b | verified |
| para 3 | 43% of 509; 15 of 505, none binding; care robots four; drones 6% / 42% | same | T07 | verified |
| para 4 | 61%, 25%, 62% of 195 | 61.0 / 24.6 / 61.5 | T09 | verified |
| para 6 | 42% European; 75% English; 0.86; 159 rows 68% / 62%; 54%; 22 of 39 | same | F07; loader; S09b; review log; precision audit; T25 | verified |

## 2. report/src/paper.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| Abstract | "multiplied the binding count fifty-six-fold" | 5 to 291 = 58.2-fold | T53 ratio | fixed to fifty-eight-fold |
| 3 Processing | "its 153 documented document-level corrections" | 157 | manual_overrides_v4.csv | fixed |
| 4 Consistency checks | "a Sonnet re-run (161)" | 160 | run_manifest; annotations/reliability_sonnet_rerun; T26 n | fixed |
| 4 Statistics | "sixteen families of 8 to 39 tests" | largest family 38 (T20, T29, T21 strata) | tables | fixed to 8 to 38 |
| 5.1 | "the ladder runs 282, 195 principal" | 291 | T53b | fixed |
| 5.2 | "binding embodied texts from 5 to 282" | 291 | T53 | fixed |
| 5.3 | "180 are in force, 11 superseded or repealed and 4 adopted" | 182 / 9 / 4 | loader | fixed |
| 5.5 | "Soft-law instruments other than standards (208 content captures)" | 207 | T09 | fixed |
| 5.5 | funding and others "(0.51 to 0.61)" | funding 0.62 | T20 | fixed to 0.51 to 0.62 |
| 5.6 | within-genre tables "could not be built ... reported as not separable from genre mix" | T29b exists (regions with at least 20 documents of the genre); values claim retained for the instrument layer | tables/T29b_* | qualifier fixed |
| 5.7 | industrial policy "1.24 to 2.30" | 2.31 | T28 | fixed |
| 5.8 | document class "77% (kappa 0.67)" | kappa 0.661 | T57 | fixed to 0.66 |
| 7 Limitations | T29b "could not be computed", proximity and liability "not tested within round" | T29b computed for regions with at least 20 documents of the genre; T30 has round-1 rows (1.00 each) | T29b; T30 | qualifier fixed |
| Abstract, 3, 5.1 | 3,165; 116; 505; 195; 15; 43% / 3%; 54% | same | results.json; T07; precision audit | verified |
| 3 Round 1, Round 2 | 2,160; 1,894; 2,557 files (files.csv rows 2,557); 266 (109); 27 of 34; 1,656; 2,075 (1,157 / 918); 1,720 (1,704 + 16, four recovered); 272 / 46 / 37 = 355; 1,641; 1,626 | same | results.json coverage; T50-T52; T53 | verified |
| 3 Processing | 3,295 / 3,165; 49 + 79 duplicates; 75% English (792 non-English); 376 + 46 = 422; 57; 205 to 160; 159 rows 68% / 62%; 373 of 581 | same | duplicates_removed.csv; loader; review log; results.json research | verified |
| 3 Analysis sets | 1,603; 1,374; 1,015; 547 (478 legal, 334 binding); 810; 505 = 195 + 240 (85 / 71 / 49) + 70; 408; 97 (27); 372 / 66; 444 of 505; 190 of 195; 127 of 372; 259 reports | same | loader; T32; T33 | verified |
| 4 Annotation | CLI 2.1.314; 351; 1,736 records (380 CJK); costs 126 / 99 / 36 / 70 / 2.5 = about 334 USD | same | run_manifest.json | verified |
| 5.1 | 305 removed = 222 + 35 + 30 + 10 + 6 + 2; 164 acts + 31 amendments; the 15 AI-naming instruments as listed | same (list matches the 15 `ai_explicit` rows) | loader | verified |
| 5.1 audit | 67 (57 to 75), 97, 56 (46 to 65), 67, 14 (9 to 22), 54 (44 to 63), 161 (132 to 190), 61 (51 to 70), 77%, kappa 0.53, 15 / 8 | same | precision audit; T62 | verified |
| 5.2 | 1,656 to 3,295; 806 to 1,015; 65 to 810; 34 to 699; 30 to 60; 61 vs 245; 444 vs 127; 58% vs 83%; 56% vs 76%; 1.31 (1.11 to 1.53); 1.10 (1.03 to 1.18); 1.26 (1.10 to 1.45); 1.05 (1.00 to 1.10) | same | T53; T20b; T30 | verified |
| 5.3 | 32% / 32% / 19%; issuers 516 / 276 / 228 / 217; 380 / 248 / 48; 132 / 60 / 3; drones 107 etc.; US 56, EU 34, JP 22, GB 11, CA 9 = 132; 27; 175 / 20; 81 of 310; F06 4 to 262, 233, 248, 50; 18 before 2010; 22 of 39 and 31; 17 missing | same | loader; T33; F06; T25 | verified |
| 5.3 geography | 1,332 (42%, 48%); 677 (49%); 345 (61%); 374 (64%); 149 (24%); 113 (71%); 98 (46%); 76 (36%); V 0.19; regions 170 / 119 / 102 / 64 / 21 / 11 / 10 / 8; 58 and 40 jurisdictions; US 83, EU 77, INT 65, CN 55, JP 46, GB 39; 68% of 792 vs 49% of 2,373 | same | F07; T54; loader; T04; T19 | verified |
| 5.4 | 432 ... 115; 509 vs 505; all gap indices and intervals; region and period shares | same | results.json category_any; T22; F12; F14 | verified |
| 5.5 | T21 shares; T20 odds ratios; T34 eleven lower; T09 shares; T10/T21 mechanism shares; citation shares; framing shares and n; stance 56 / 31 / 4 of 480 | same | T21; T20; T34; T09; T13; F26; results.json stance | verified |
| 5.6 | n 1,576; V values and intervals; genre shares by region; distances 0.038 (0.026 to 0.060), floors 0.008 / 0.022, 0.010, 0.097, 0.198, 0.070 (0.082), 0.174 | same | T29; T14; T23; T31; T31b | verified |
| 5.7 | 477 vs 746; crude changes; T28 values; T17 and T30 values; 2 of 194, 18 of 218, 33 of 259 | same | T16; T28; T17; T30; F33 | verified |
| 5.8 | 0.85 (0.61; 11 below 0.80), 0.91, 0.88 (0.75 vs 0.84), 0.90, 0.83; 0.86 / 0.91; level-2 0.81 / 0.89; unweighted 0.76 / 0.86; weak fields; multi-label 0.81 / 0.80 / 0.71 / 0.70; 0.84 and 0.91 round-1; 93% of 1,608 (0.85), 98% (1,624), 94% (1,542), 77%; lexicons 0.40 to 0.43, 2,700, 0.88; strict set values | same | T26; T27b; S09b; reliability_fields_r2opus.csv; T57; T18; T32 | verified |
| 6, 7, 8 | 810 / 505 / 408 / 15; 88% and 34%; 62 / 47 / 61 / 25 / 18; 68% on 62; 15 and 4%; 2 of 14 and 12 of 14 with V 0.43 / 0.34 / 0.28; 31% and 26%; 13%; 75%; 22 of 39; 54%; 77%; 112 of 195; 47 / 6; 59 / 27 / 17 / 17 / 17 / 11; 0.75; 547; 110,000; 355; 39-field | same | tables as above; T52 | verified |

Not verified (left unchanged): "483 texts carried collectors' labels in a cover block" and "a 14,000-character excerpt" (v1 annotation policy; no file in the v4 package records them); "28 document types" is supported by the data dictionary and the master table (28 values) although codebook Section C names 27 (the 28th is `unusable`).

## 3. report/src/analysis_report.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| Key numbers | "195 of 282 binding legal texts" | 291 | T53b | fixed |
| Key numbers | "180 of the 195 in force (Table 33b)" | 182 | loader; T33b | fixed |
| Finding 1 | "180 of those in force" | 182 | loader | fixed |
| Finding 1 | "206 of 282 are regulations or decrees and 71 statutes (Table S01)" | 207 of 291; 71 | S01 | fixed |
| Finding 3 | "international cooperation (0.58)" | 0.59 | T20 | fixed |
| Finding 4 | "33% of 208 soft-law instruments" | 207 | T09 | fixed |
| Methodological result | "binding embodied instruments from 5 to 282" | 291 | T53 | fixed |
| Section 2 | "document class 77%, kappa 0.67" | 0.66 | T57 | fixed |
| Section 2 | "153 documented doc-level corrections ... 1 binding-nature corrections" | 157; 5 | manual_overrides_v4.csv | fixed |
| Section 2 | round-2 sample "62 binding, 53 soft-law" | 63 / 52 | master table on the 160 sample ids | fixed |
| Section 3 | "5 to 282 (robot-specific and binding from 4 to 245), soft-law instruments from 50 to 420" | 291; 254; 411 | T53 | fixed |
| Section 4 | "For binding law: 282 texts" | 291 | T53b | fixed |
| Section 4 | "among the 282 binding texts, 28 are ancillary, 25 stubs, 19 catalogue pages" | 291; 28 catalogue pages | loader `instrument_unit` | fixed |
| 5.1 | 822 governance documents: "268 in force, 48 superseded ... 2 lapsed" | 272; 42; 4 | loader | fixed |
| 5.1 | T33b: "180 in force, 11 superseded" | 182; 9 | loader | fixed |
| 5.1 | "(Table S01, 282 rows) ... 206 regulations or decrees, 71 statutes, 3 court decisions, 1 mandatory standard and 1 treaty" | 291 rows; 207; 71; 9 mandatory standards; 3; 1 | S01 | fixed |
| 5.1 | Machinery Directive 2006/42/EC "is coded superseded because the audit's correction codes were applied mechanically" | override now in_force; master table in_force | manual_overrides_v4.csv; loader | qualifier fixed |
| 6 | "binding texts address drones (60%)" | 59.1% | F13 | fixed to 59% |
| 7.1 adjusted | transparency 0.46, beneficence 0.41, trust 0.54, robustness 1.37 | 0.47, 0.42, 0.55, 1.38 | T20 | fixed |
| 7.1 by class | "conformity assessment (39%)" | 37.8% | F22 | fixed to 38% |
| 7.2 | "Soft-law instruments (n = 208) mention physical safety in 74%" | n 207; 73.4% | T09 | fixed |
| 7.2 | standards "never liability or dual use" | liability mentioned in 3.2%, never in depth; dual use 0 | T09 | qualifier fixed |
| 7.3 | "international cooperation (0.58) and funding (0.61)" | 0.59; 0.62 | T20 | fixed |
| 9 | "ethics principles (0.67, Holm p = 0.46)" | 0.447 | T28 | fixed to 0.45 |
| 12 Precision | "the Machinery Directive is coded superseded although it governs machinery until January 2027" | coded in force after the override was corrected | manual_overrides_v4.csv | qualifier fixed |
| 13 Conclusions | "180 of them in force" | 182 | loader | fixed |
| Key numbers, 1, 2 | 2,557 (1,894 of 2,160); 2,075 / 1,720 / 1,641 / 1,626; 3,295 / 3,165 (128); 1,603: 509 and 810 (822); 1,015: 48, 409; 547; 505 / 408 / 395 / 153; 168 / 194 / 140 / 15; 54% (44 to 63), 161 (132 to 190), 299, 61% (51 to 70); 116 / 56 / 38; 60 (58 + 2); 42% (1,332) / 75% (2,373) / 9% (278); seven checks | same | results.json; T53; T53b; T62; S08; loader | verified |
| Findings 1 to 5 | drones 107, AV 67, manipulators 13, delivery 15; 140, 15; Korea cited by 9; 43% (219 of 509), 3% (15 of 505); 214 (107), 201 (67); gap intervals; 170 / 20 / 0; T21 shares; 61 vs 245; 444 vs 127; T20 odds ratios; 62% / 33% / 33%; 95% / 68%; 57 to 66%; 25 / 21 / 23 / 31; 1,576; 34 of 38; 2 of 14; 12 of 14; 1.7 (0.03); 0.39 (0.04); 31% / 26%; 10% / 5%; 1% to 13% | same | T07; T22; T25; T21; T20b; T20; T09; T29; T29b; T28; T30; F33 | verified |
| Section 2 | 2,160 / 1,894 / 2,557; nine agents, seven databases; 2,075; 1,720 (16); 355 (272 / 46 / 37); 1,641; 1,626; 93% of 1,608 (0.85), 98%, 94%; median 24%; 97 Chinese documents; 376 + 46; 57 of 422; 205 to 160; 159 (108, 68%; 98, 62%); 165 / 119 / 107; 79 on 27 round-1 documents; 128; 160 sample (116 / 29 / 6; 27 landing; 848 words); 100 of 299; 2.1.314; 334 USD | same | files.csv; T50-T52; T57; review log; governance_audit_rows via script; overrides_applied.csv; duplicates_removed.csv; sample ids; run_manifest | verified |
| Section 3 | 65 to 810; 34 to 699; 10 to 108; 24 to 97; 30 to 60; 806 to 1,015; region and robot-group before/after; 286 / 236 / 254 vs 79 / 258 / 20, V 0.41; 444 of 505 (88%), 127 of 372 (34%); about 850 vs 2,650; 254 landing pages; 379 CJK | same | T53; T54; T55; results.json binding_nature_test; loader | verified |
| Section 4 | 222 (191), 42, 35, 30, 10, 6, 2; 47 / 6 Australia; 67 / 97 / 56 / 67 / 14 / 54 / 161 / 61 / 77 / 0.53 / 15 / 8; T33 tiers 168 (153 / 15), 176 (112 / 64), 64; 97 (27 / 64 / 6); 0.56 / 0.09 | same | loader; precision audit; T33 | verified |
| 5 to 10 | composition, issuers, regulators 179 / 121 etc.; F06 262 / 143 / 233 / 248 / 50; year shares (10th percentile 2017, median 2024, 38%, 617; 82% (28 of 34), 39% (218 of 558), 42% (259 of 617), OR 0.84 (0.81 to 0.86), 137); T03 years; region counts and shares; 76 / 56 / 38; US 83 (56), CN 55 (4), JP 46 (22), GB 39 (11), CA 19 (9), FR 12 (3), AU 6 (4) vs 47; 305 / 286 / 233; 271 of 305; languages 2,373 / 278 / 107, 62% of 422, 83% of 123; 68% vs 49%; 33% vs 45%; category counts, region shares (F12), class shares (F13), period shares (F14); co-occurrence 123 (0.36), 76 (5.1), 76 (0.68); gap table; sectors 47 / 25 / 18 / 17 / 11 and 72% / 45%; 17 of 20; T21; T20b; T20; F21 ranges; F22 shares; T09; T35; T10/T21 mechanisms; T29; T29b (484; 476; V values; INT 23% / 9%; Asia 75% / 74%); T15 ranges and region n; silhouettes; framing; stance; personhood 174 (19 / 34 / 121), 10% to 5%; citations (T13, F30); distances, stability, research-only; regional unit counts; F33 terms; T16; T28 (1,223); T17; T30 (663); robot-group counts (S12, T55, T07) | same | loader; F06; F05; T03; F07; T04; F10; T19; F12; F13; F14; T06; T07; T22; results.json; T08; T21; T20b; T20; T15; F22; T09; T35; T10; T29; T29b; T24; F26; T12; T13; F30; T23; T23b; T31; T31b; T14; T54; F33; T16; T28; T17; T30; S12 | verified |
| 11 and 12 | T26 medians and minima; 0.1 to 0.4 more labels; 0.75 vs 0.84; 0.60 / 0.55 / 0.49; round-2 0.86 (0.81 over 129), 0.91 (0.89); weak fields; set-defining fields 0.83 / 0.86 / 0.93 (0.76); 19 of 20; taxation 0.16, oversight body 0.35, domestic 0.32, self-regulation 0.43; re-run 0.84 / 0.95 / 0.89 / 0.90 / 0.69 / 0.66; level-2 0.81 / 0.89 vs 0.69 / 0.84; 36 CJK; 27 landing; failure types 14 / 10 / 9 / 8 / 3 / 2; 60 of 100; lexicon 70 to 89%, 72 to 99%, 2,700, 0.40 to 0.43, 0.88; strict set 1,374 / 32% / 708 / 168 / 44% / 16; 936 / 453 / 175; coverage 266 / 109 / 34 / 27; 355; blocked hosts; four recovered; 22 of 39 (11), 31 (12), 17; 251 / 223 / 20 / 15 / 10; 61% vs 54%; 86 pairs; 0.75 / 0.79 / 0.16; 0.99; 21%; 57 of 422; 16%; 2,526 of 2,618; four and five regions; 16 scope texts | same | T26; T27; T27b; reliability_fields_r2*.csv; S09b; precision audit; T18; T32; results.json coverage; T52; T25; T54; results.json excerpt_coverage; loader; T20 | verified |

Not verified (left unchanged): "46 of its 48 v3 binding rows were register entries for individual CASA instruments" (Section 8; the v3 S01 holds 48 Australian and 52 Oceanian rows, but the 46 cannot be recomputed from the v4 package); "ISO 10218 and the Machinery Regulation are the instruments most cited for industrial manipulators" (Section 10; S13 lists GDPR 26, ISO 10218 24, Machinery Regulation 20, so the claim holds for robot instruments only).

## 4. report/src/supplement.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| S1 (4) | "153 audited doc-level corrections" | 157 | manual_overrides_v4.csv | fixed |
| S4.1 | "The five samples (160, 161, 160, 160 and 351 documents)" | 160, 160, 160, 160, 351 | run_manifest; annotation folders; T26 | fixed |
| S4.6 | "document class in 77% (kappa 0.67, n = 1,608)" | kappa 0.66 | T57 | fixed |
| S4.7 | "62 binding instruments, 53 soft-law instruments or standards" | 63 / 52 | master table on sample ids | fixed |
| S5 | "S01 lists the 282 legally binding texts (206 regulations or decrees, 71 statutes, 3 court decisions, 1 mandatory standard and 1 treaty ...)" | 291 (207, 71, 9 mandatory standards, 3, 1) | S01; loader | fixed |
| S5 | Table 33b "(180 in force, 11 superseded, 4 adopted ...)" | 182 / 9 / 4 | loader | fixed |
| S5 | "S02 lists the 420 soft-law texts" | 411 | S02 (411 rows) | fixed |
| S8 rules | "among the 282 binding texts ... 28 ancillary, 25 stubs, 19 catalogue pages" | 291; 28 catalogue pages | loader | fixed |
| S8 corrections | "153 field-level corrections on 91 documents (152 rows concern round-2 documents)" | 157; 156 | manual_overrides_v4.csv | fixed |
| S8 corrections | "17 status corrections (15 to superseded, 2 to in force), 14 class corrections (10 to soft law, 3 to report, 1 to binding) ... 1 binding-nature correction" | status 9 superseded, 6 in force, 2 withdrawn or lapsed; class 6 binding, 5 soft, 3 report; binding nature 5 | manual_overrides_v4.csv `new_value` | fixed |
| S8 corrections | Machinery Directive "was set to superseded by its D code" (as a standing consequence) | override now in_force | manual_overrides_v4.csv | qualifier fixed |
| S10 table | binding embodied every legal text, v4 "282" | 291 | T53 | fixed |
| S10 table | "195 (180 in force; ...)" | 182 | loader | fixed |
| S10 table | proximity and liability "not checked within round (Table 30 lacks them)" | T30 round-1 rows: 1.00 (0.95 to 1.07) and 1.00 (0.94 to 1.06) | T30 | qualifier fixed |
| S10 table | reliability samples "(160, 161, 160, 160, 351)" | 160 each | run_manifest | fixed |
| S10 prose | "153 audited corrections" | 157 | manual_overrides_v4.csv | fixed |
| S10 prose | "binding embodied texts from 5 to 282" | 291 | T53 | fixed |
| S1 | CLI 2.1.314; prompt hash 8d4d83e909f0; 1,925 round-2 inputs; manifest table (1,703 / 81.92; 499 / 17.28; 351 / 35.85; 1,736 (1,356 + 380) / 126.02; 46 / 2.49; six reliability folders 160 each with their costs; 7 / 0.69); about 334 USD; 3,295 / 3,165 | same | run_manifest.json; annotations/round2/_inputs (1,925 files) | verified |
| S4.6, S4.7 | 93% (0.85, 1,608); 98% (1,624); 94% (1,542); 92% (0.79, 754); 94% (0.88, 854); 129 and 127 rows; 116 / 29 / 6 / 1 (36; 8); 14 reports, 8 communications; 109 / 24 / 27; 848; 31; 96; 37 rows (16 + 1 + 20); 0.86 (0.81); weak fields; set-defining fields; jurisdiction 0.96; 19 of 20 (0.72); multi-label weakest 0.16 / 0.35 / 0.32 / 0.43 / 0.49 / 0.50; mechanisms 0.72 / 0.79 / 0.84 / 0.93 / 0.96; re-run 0.91 (0.89) and listed fields; 0.58; S09b twelve pairs; 0.05 to 0.18; 24% (270), 97, 83, 50%; 380 and 46 files; 57 of 422; 205 to 160 | same | T57; companion report (computed); reliability_fields_r2*.csv; S09b; review log; annotations/ | verified |
| S5, S6 | 254 standards, 62 and 192; 47 under development, 42 of them in S03; 105 and 108; 97; 205; 190 and 378; 39 entries; 22 (11), 31 (12); 17 missing with citing counts; 189 unread binding | same | loader; S03-S05; T25; inventory | verified |
| S8 | 79 on 27 documents; 128 = 49 + 79; 463 + 42 = 505; 222, 35, 30, 10, 6, 2; 164 + 31 = 195; 194 of 195; 47 draft standards; 165 rows (108 / 68%; 98 / 62%; 119; 107); 36 catalogue_page and 14 dependent; 32 and 32; 7 years | same | overrides_applied.csv; duplicates_removed.csv; loader; governance_audit_rows via script; manual_overrides_v4.csv | verified |
| S10 | v3 values 3,291 / 3,148; 1,589 / 982; 808; 681; 299 (268 in force); 238; 60; 31 of 38 loose; 11 of 14 (804 vs 367); 13 of 14; 1.09 (Holm 0.10) / 1.05; 0.93 / 0.93; 33 of 38 (V to 0.34); v4 values 3,295 / 3,165; 1,603 / 1,015; 810; 505 (408; 395; 153); 699; 195 (168; 194; 140; 15); 161 (132 to 190); 254 / 62; 60; 22 of 39 and 31; 10 of 14 (505 vs 372), 0 of 14, 10 of 14; 10 of 14 adjusted; 1.31 / 1.26 and 1.10 / 1.05; pooled 0.94 / 0.94; 34 of 38 (0.09 to 0.35); 2 of 14; 12 of 14; 0.01; 160 (57); 0.86 / 0.91; 1,716 with text (v3) | same | v3 results_digest and tables; v4 tables | verified |
| S12, S13 | 3,423 registry rows; 197 fields; 42% / 75% / 9%; 810 / 505; 2,075 / 355; 2,557; 266; 16; audit method and table (299 = 294 + 5; seed 2026; 6,000 characters; 67 / 97 / 56 / 67 / 14 / 64 / 54 / 53 with intervals; 53 and 8; 161 and 158; regional and category shares; failure types; 60 of 100); rule comparison 74% / 67% (0.79, 0.50), 61% / 54% (0.77, 0.53; 15 / 8), 46% / 53% (0.71, 0.42); 194 of 195; 20 of 195; 168; 27 | same | registry.csv; master_table.csv; precision_audit.md and sample; T62 | verified |

Not verified (left unchanged): the v1 column of the S10 table (1,703; 1,589; 674 / 859; 63; 12; 7 claimed) and the v2 column values that are not in the v4 package (8 standards, 4 content-captured; "10 of 38" from the v2 audit; "65 vs 258 instruments"; "about 1.3 / 1.3"; V 0.19 to 0.33); the v3 "177 catalogue pages" among 238 standards; "n = 270" and "a median of 50% for Japanese" (the AI researcher's measurements, quoted from the review).

## 5. report/src/collection_round2.md (generated by scripts/21_round2_report.py)

Every number in the companion report is computed from the data and matched a recomputation with the loader (1,656 / 65 / 34; 2,075 (1,157 / 918; nine agents, eight runs); 1,720 (1,704 + 16; four recovered); 1,641 after 79 removed; 1,626 / 1,351 / 988 / 745 / 444 / 378; 301 = 218 + 35 + 48; 286 to 190 / 164 / 135 / 10; 65 to 810 (x12.5); 34 to 699; 5 to 291; 505 (408; 395; 153); 195 (168; 194; 140; 15); 11 to 22 and 12 to 31 with the 17 missing; 46 / 272 / 37; 189 of 355; 376 + 46; 57 of 422; 205 to 160; 157 on 91 (156); 119 of 165, 107; 93.0% (0.85, 1,608); 98.1% (1,624); 93.8% (1,542); 76.7% (0.66, 1,608); 91.9% (0.79, 754); 93.9% (0.88, 854); 160; 0.86 / 0.91 with the five weakest fields; 190 and 378; audit 67 / 97 / 56 / 67 / 14 / 54 (44 to 63) / 161 (132 to 190) / 61 (51 to 70) / 77 (0.53); 200 of 260 standards; 110,000; 2014 to 2026; 54%).

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| Summary (script line 246 f-string) | "1,641 entered the master table after 79 cross-round duplicates were removed" | 77 of the 79 removed round-2 rows duplicate other round-2 rows; 2 duplicate round-1 documents | duplicates_removed.csv `duplicate_of` | qualifier fixed in the script ("duplicates were removed (identical normalised title and jurisdiction, mostly against other round-2 rows)"); report regenerated |

No stale qualifier presents v3 state as current.

## 6. report/src/methods_document_discovery.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| 6.2 | "binding ... (277 round-2 texts in the embodied set)" | 286 | loader | fixed |
| 6.2 | "153 documented document-level corrections (on 91 documents, 152 of the rows ...)" | 157; 156 | manual_overrides_v4.csv | fixed |
| 6.2 | "binding nature 1" | 5 | manual_overrides_v4.csv | fixed |
| 6.3 | "the 277 binding embodied-set texts resolve into 190" | 286 | loader | fixed |
| 6.3 | "for binding instruments, 282 texts" | 291 | T53b | fixed |
| 7.1 | "77.1% on document class (kappa 0.67, n = 1,608)" | 76.7% (0.66) | T57 | fixed |
| 1, 2, 3, 4, 5 | 39; 11 (12); 65; 5; seven databases, eight runs; nine agents and a tenth; 17 fields; 13 types; eight statuses; 23 categories; 977 / 1,008 / 90; 2,075 = 1,157 + 918; 119 rows (78 round 2) + 1; 79 of 1,720; 1,641; 1,720 (1,704; 16); 355 (272 / 46 / 37); 4 recovered; hosts 59 / 27 / 17 / 17 / 17 / 11; 189 | same | T25; T53; T50; inventory (confidence counts); duplicates_removed.csv; T51; T52 | verified |
| 6, 7, 8 | 39 fields; 110,000 = 100,000 + 6,000 + 4,000; 1,736 calls, about 126 USD; 24%; 376 + 46 = 422; 57; 205 to 160; sixteen standards inputs; 1,626 of 1,641; 928; 1,351; 745; 159 rows (108, 68%; 98, 62%); 165 / 119; 403 + 41 = 444; 218 / 35 / 30 / 10 / 6 / 2; 190 / 164 / 135 / 10; 810 / 505 / 408 / 395 / 153; 195 / 168 / 194 / 140 / 15; 200 of 260; 92.9% (0.85, 1,608; T57 stores 0.93); 98.1%; 93.8%; 160; 0.86 / 0.91; 0.85 / 0.91; weak fields; 39; 22 (11); 31 (12); 17; audit values; yield table (all 17 rows against T50); 38 / 32 / none | same | run_manifest; review log; loader; T50; T57; T25; precision audit | verified |

Not verified (left unchanged): the harvester term counts for gov.cn (twelve), the Australian register (nine) and eCFR (twenty) could not be located by pattern in `collection_round2/scripts/harvest_apis.py` (the EUR-Lex 25, legislation.gov.uk 15 and Japanese nine lists were found); "across 88 jurisdiction codes" (the inventory has 87 distinct codes plus one blank); "would have removed 69 distinct documents" (the abandoned rule is not reproducible from the package); "at least 80 words or 400 CJK characters" (fetch-script threshold not checked); "92.9%" (T57 stores 0.93, a rounding-level difference).

## 7. report/src/methods_review_and_revision.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| 7 Limits | "190 instruments that collectors verified but ... remain outside every count" | 189 (candidates without text recorded as legally binding) | round2_inventory.csv; T51; companion report | fixed |
| 2, 4, 5, 6 | six reviews; 14 to 25 minutes; 159 instruments (165 rows), 68%, 62%; 39 screenshots; 83 Chinese documents; 100 of 299; 67 / 97 / 56 / 67 / 14; 54 (44 to 63); 161 (132 to 190); 160; 0.86 / 0.91 vs 0.85 / 0.91; 165 rows; eleven inverted values; 157 on 91; 0.77, 0.53, 15, 8; 422; 57; 205 to 160; four false titles; six documents; 810 and 291 vs 65 and 5; 505 / 408 / 195 / 168 / 140 / 15; 161; 22 of 39; 31 of 39 | same | brief (reviews, screenshots, durations); review log; precision audit; S09b; manual_overrides_v4.csv; T62; T53; T25 | verified |

Not verified: findings-table sizes "about a dozen" and "about sixty" (approximate descriptions of the review files, not recounted); the review durations and screenshot count are taken from the brief.

## 8. review/adversarial_review_v3_and_changes_v4.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| Section 3 table | "CJK documents (424): rated not about AI" | 422 re-annotated CJK documents (376 + 44 + 2 = 380 and 46 annotation files; 422 usable CJK documents in the master table) | companion report (computed); loader | fixed |
| Sections 1, 2, 3 | precision audit values; round-2 reliability values and weak fields; 376 + 46, 57 of 422; 157 (153 first conversion; six status and five class values = eleven); 22 of 39 / 31 / 11 and 12; 4 texts recovered; 2 of 14 and 12 of 14; headline table (1,656 / 1,538; 3,291 / 3,148; 3,295 / 3,165; 675 / 1,589 / 1,603; 65 / 808 / 810 / 505 / 408; 395 / 153; 5 / 299 / 291 / 195 / 168; 194 / 140 / 15; 54% and 161, 61%, 0.77, 0.53; 30 / 60 / 60; coverage; 0 of 14 and 10 of 14; trends 1.31 / 1.26 and 1.10 / 1.05; 205 / 160 (57); 0.86 / 0.91); closing paragraph | same | precision audit; reliability files; manual_overrides_v4.csv; T25; T29b; T53; v3 digest; T20b; T30 | verified |

Not verified (the reviewers' own tallies, recorded as historical findings and not recomputed): severity counts per reviewer; "29-document spot check: 12 with an error"; "36 of 44 figures"; "55 of 299 binding instruments enter the embodied set with relevance 0 or 1"; "three denominators (804 / 808 / 812)"; "177 landing pages" in the v3 Table 9; "86 near-duplicate title pairs"; the governance expert's "190 verified binding candidates" (correct for the review date; 189 after the retry pass).

## 9. report/v4_summary.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| 6 Limits | "190 instruments verified by collectors but unreadable" | 189 | round2_inventory.csv; companion report | fixed |
| 2 to 5 | 11 of 14 (v3, qualified); 157 on 91; 165-row audit; eleven; 422; 57; 205 to 160; 160; 0.86 / 0.91; 100; 54% (44 to 63); 161 (132 to 190); 299; table (3,291 / 3,148; 3,295 / 3,165; 1,589 / 982; 1,603 / 1,015; 808 / 810; 505 (408); 299 / 291; 195 (168; 140; 15); 0 of 14, 10 of 14; 205 / 160; 31; 22 / 31); 15 of 195; 61 vs 245 | same | review log; v3 digest; T53; T53b; T20b | verified |

## 10. README.md

| Location | Claim as written | Correct value | Source | Action |
|---|---|---|---|---|
| para 1 | "status and class rules plus 153 audited corrections" | 157 | manual_overrides_v4.csv | fixed |
| Deliverables | 160 round-2 documents; n = 100; F50 to F52; T50 to T60 | same | files present | verified |

## 11. Cross-document consistency after the fixes

Every quantity now carries one value in every document: 3,295 / 3,165 / 1,603 / 1,015 / 1,709 / 822 / 116; 810 / 291 / 702 / 254 / 411 / 280 / 194 on the comparable unit; 505 / 408 / 195 / 168 / 194 / 140 / 15 / 395 / 153 on the principal unit; 182 / 9 / 4 for the status of the 195; 157 overrides on 91 documents (156 round-2 rows); 0.66 for the collector-class kappa; 207 soft-law content captures; 63 / 52 / 23 in the round-2 reliability sample; 160 for every round-1 reliability sample; 189 unread binding candidates; 422 CJK documents. Comparable-unit and principal-unit values are never given for the same quantity without the unit being named.

## 12. Placeholders

All placeholders resolve under `scripts/16_build_reports.py` (figure key to the first `figures/<key>_*.png`; table key to the first `tables/<key>_*.md`, with a suffix key such as `T29b_research` selecting `tables/T29b_*_research.md`): brief 0; paper 31 (F01, F06, F07, F11, F23, F24, F29, F31, F34, F38, F39, F40, F41, F43, F50, T09, T10, T20, T20b, T22, T26, T28, T29, T30, T33, T34, T53, T53b, T62 and the special AUDIT key); analysis report 90 (all F01 to F44 present except the merged 9, 15 and 32, F50 to F52, T01 to T35 with T20b, T23b, T27b, T29b_research, T29b_principal, T31b, T33b, T50 to T62 with T53b, S09b, S12, S13, AUDIT); supplement 26 (incl. CODEBOOK, TAXONOMIES, STAGE1, S01 to S06, S08 to S13); companion report 14. `codebook/codebook.md`, `codebook/taxonomies.md`, `report/stage1_checkpoint.md` and `tables/T25_coverage_audit.csv` exist for the special keys.

## 13. v3 state presented as current

Checked in every document: "299 binding" appears only as the v3 value under audit; 808 and 810 appear only with the comparable-unit qualifier; "11 of 14 core principles lower" appears only as the v3 pooled result next to the within-round values; the Machinery Directive 2006/42/EC is no longer described as coded superseded (analysis report 5.1 and 12, supplement S8); the override count is 157 everywhere; Table 29b is nowhere described as not produced (paper 5.6 and 7 corrected); Table 30 is nowhere described as lacking proximity and liability rows (supplement S10 corrected). The remaining mentions of "v3" name the version explicitly as the earlier one.

## 14. Notes on the brief's own reference values

All headline values in the brief were confirmed against the data, with two notes: the override breakdown is doc_class 14 (the brief gives 15 in one place and 14 in another; the file and all texts say 14), and the instrument_status totals in_force 604 / superseded 118 / withdrawn 5 hold on all annotated rows (on usable rows: 601 / 118 / 5); no narrative cites them. The 195 principal binding instruments split 182 in force, 9 superseded or repealed and 4 adopted but not yet in force (the writers' 180 / 11 / 4 predated the override corrections).
