---
title: "Supplementary material: codebook, reliability, coverage audit, instrument lists, version history, precision audit, datasheet"
subtitle: "Companion to the analysis report and paper on the governance of embodied AI and robotics"
author: "Prepared with Claude Code for Jimmy Lin, Centre for Enterprise Innovation (CEI) AI Robotics project"
date: "31 October 2026"
---

*Version 5 note (collection round 3, 2 November 2026). The tables and figures in this package were regenerated after round 3, which recovered the text of round-2 instruments that could not be read before, harvested new service-robot, care, exoskeleton and humanoid instruments, re-read the truncated statutes in full and added supplementary fields (whom a rule binds, dates, legal effect of standards, robot-provision year). The narrative below still states the v4 counts of 31 October 2026 and has not been re-audited sentence by sentence against the v5 tables; where a number in the text and a number in a table differ, the table is current. The round-3 companion report (collection_round3) gives the v5 headline counts and what changed, and HUMAN_ASSISTANCE.md lists what still needs a person.*

## S1. Pipeline, reproducibility and what changed in v4

All steps are scripts in `scripts/` and run in numerical order (`run_v4.sh`; `run_v4_post.sh` re-runs from the counting-unit step and `run_v4_analyses.sh` from the analyses). Steps 01 to 05 require the converted source texts; the round-2 merge appends the round-2 registry rows, text features and annotations before assembly; steps 07 onward run from the stored annotations, so every number in the report can be regenerated from the package.

| Step | Script | Output |
|---|---|---|
| Registry and first deduplication (round 1) | `01_build_registry.py` | `data/registry.csv`, `data/files.csv` |
| Text features | `02_text_features.py` | `data/text_features.csv` |
| OpenAlex enrichment (DOI-based) | `03_openalex.py` | `data/openalex.jsonl` |
| Model annotation (v1 excerpt; v2 blind extended excerpt for governance documents; the same blind policy for every round-2 document; v4 character-aware cleaner for Chinese, Japanese and Korean documents) | `04_annotate.py`, `collection_round2/scripts/04_annotate_r2.py` | `annotations/main`, `main_clean`, `gov_extended`, `round2`, `cjk_fix`; reliability runs in `reliability_*` |
| Round-2 merge: registry rows, text features and annotations for every candidate with text; inventory of every candidate | `merge_round2.py` | `data/registry.csv` (rows `R2-*`), `data/round2_inventory.csv` |
| Full-text lexicons (repaired in v2) | `05_lexicons.py` | `data/lexicon_features.csv` |
| Master table | `07_assemble.py` | `data/master_table_raw.csv` |
| Documented corrections and second deduplication (also across rounds) | `07b_apply_overrides.py` | `data/master_table.csv`, `overrides_applied.csv`, `duplicates_removed.csv` |
| v4 counting unit, instrument families, AI-content tiers, status and class rules, text-hash duplicates, audited doc-level corrections | `07c_v4_units_and_tiers.py` | columns `instrument_unit`, `principal_instrument`, `family_key`, `family_size`, `family_rep`, `ai_explicit`, `autonomy_terms`, `words_ok`, `text_hash` in `data/master_table.csv`; `data/ai_content_flags.csv` |
| Reliability (five round-1 comparisons) | `09_reliability.py` | `data/reliability_fields*.csv`, `reliability_team_crosscheck.csv` |
| Round-2 reliability (second model, same-model re-run) and variants (unweighted and level-2 kappa) | `09b_reliability_round2.py`, `09c_reliability_variants.py` | `data/reliability_fields_r2opus.csv`, `_r2rerun.csv`, `data/reliability_variants.csv`, `tables/S09b` |
| Analyses (incl. T20b within-round contrasts, T30 round rows, sparse-cell flags) | `13_analysis_A.py`, `14_analysis_B.py`, `15_analysis_C.py`, `18_analysis_D.py`, `19_fulltext_validation.py`, `17_supp_tables.py` | `tables/`, `figures/data/`, `data/results.json` |
| Figures (wrapped titles, F23, F31, F39, F40 and F41 rebuilt) | `20_figures_v2.py` | `figures/` (light and dark PNG and SVG) |
| Round-2 report: sources, fetch funnel, before/after, counting-unit tiers (T53b), collector-metadata agreement, new instruments | `21_round2_report.py` | `tables/T50` to `T60`, `T53b`, `figures/F50` to `F52`, `report/collection_round2.md` |
| Precision audit versus the rule-based unit | `24_precision_vs_rules.py` | `tables/T62`, `results.json` keys `precision_audit` |
| Run manifest | `23_run_manifest.py` | `data/run_manifest.json` |
| Dashboard and reports | `10_dashboard.py`, `16_build_reports.py` | `dashboard/`, `report/` |

What changed in v4, after the six adversarial reviews of v3 and the two checks commissioned from them (`review/adversarial_review_v3_and_changes_v4.md`): (1) the headline counting unit is the principal instrument, assigned by documented title and capture rules, with instrument families and two text-based AI-content tiers reported beside it (S8; Table 53b); (2) collection round enters the adjusted models as a covariate and the stratified tables as a stratum (Tables 20, 20b, 30); (3) the excerpt cleaner was made character-aware and every Chinese, Japanese and Korean document was re-annotated (S4.7); (4) four status and class rules and 157 audited doc-level corrections were applied (S8); (5) a stratified round-2 reliability sample was re-annotated by a second model and by a same-model re-run, and unweighted and level-2 kappa variants were computed for every comparison (S4.7, Table S09b); (6) an independent precision audit of the v3 binding set was run and compared with the rules (S13, Table 62); (7) the coverage audit uses 39 reference entries and a strict capture criterion (S6); (8) depth statistics use content-analysed captures of at least 150 words and report standards' scope pages separately (Table 9, Figure 23); (9) a recovered-fetch pass added four round-2 texts, so the collection has 3,295 annotated and 3,165 usable documents; (10) the round-2 model inputs and a run manifest are in the package. The version-to-version comparisons are in S10.

Annotation used the Claude Code command-line interface (version 2.1.314 for the v4 runs) in non-interactive mode with the codebook as a fixed system prompt and a JSON schema enforcing all 39 fields; the main model was `claude-sonnet-5-5`, the second annotator `claude-opus-5-5`. The prompt hash of the codebook and schema is `8d4d83e909f0` for every run. The v2, round-2 and v4 runs record an excerpt policy string (`v2|head=100000|mid=6000|tail=4000|blind=True`, with the suffix `|cjk_clean=v4` for the character-aware cleaner) and store the exact model input for every document under `annotations/<run>/_inputs/` (round 2: 1,925 inputs, one per annotation call including the duplicates later removed; also `cjk_fix`, `gov_extended` and `reliability_blind`). The policy strips the collectors' cover block (source URL, issuer, type and tier labels) from the text, passes only the document id, word count and text status as metadata, and keeps short lines containing digits, all-capital headings, sentence-ending lines and, since v4, every line containing Chinese, Japanese or Korean characters. `data/run_manifest.json` lists, per annotation folder, the number of files, the models, prompt hashes and policies, whether inputs are stored, and the cost:

| Folder | Files | Model | Policy | Cost (USD) |
|---|---:|---|---|---:|
| `main` | 1,703 | Sonnet 5.5 | v1 excerpt | 81.92 |
| `main_clean` | 499 | Sonnet 5.5 | v1 excerpt, re-cleaned | 17.28 |
| `gov_extended` | 351 | Sonnet 5.5 | v2 blind extended | 35.85 |
| `round2` | 1,736 | Sonnet 5.5 | v2 blind extended (1,356); with `cjk_clean=v4` (380) | 126.02 |
| `cjk_fix` (round-1 CJK documents) | 46 | Sonnet 5.5 | v2 blind extended, `cjk_clean=v4` | 2.49 |
| `reliability_opus` | 160 | Opus 5.5 | v1 excerpt | 15.72 |
| `reliability_sonnet_rerun` | 160 | Sonnet 5.5 | v1 excerpt | 3.99 |
| `reliability_fulltext` | 160 | Sonnet 5.5 | full text | 10.92 |
| `reliability_blind` | 160 | Sonnet 5.5 | v2 blind, short excerpt | 6.63 |
| `reliability_round2_opus` | 160 | Opus 5.5 | v2 blind extended | 21.46 |
| `reliability_round2_rerun` | 160 | Sonnet 5.5 | v2 blind extended | 11.05 |
| `test` | 7 | Sonnet 5.5 | (earlier prompt hash) | 0.69 |

The folders sum to about 334 USD of model calls. Temperature and seed are not controllable through the interface used; variability under re-runs is measured directly (S4). The round-2 collectors were Claude subagents and harvest scripts; the six reviewers of v3 and the precision auditor were Claude agents with written briefs; no person read or labelled any document, and no human validation exists (S4.5).

Statistics use pandas 3.0, SciPy, statsmodels and scikit-learn: Wilson intervals; chi-square tests with a Monte-Carlo p-value when more than a fifth of expected counts are below five (a parametric bootstrap under independence, not a fixed-margins test), and Fisher's exact test for 2 by 2 tables with any expected count below five; bias-corrected Cramér's V (Bergsma 2013) with percentile-bootstrap intervals; Holm correction within one family per table (Tables 8, 10, 15, 16, 17, 20, 28, 29, 34) and within each stratum for Tables 20b and 21; logistic regression with document class, region, collection round and year as covariates and a sparse-cell flag where one set contributes fewer than five events; Mantel-Haenszel odds ratios stratified by class; k-means with silhouette and bootstrap adjusted-Rand stability; cosine distance with average linkage, bootstrap intervals and split-half noise floors.

## S2. Codebook

{{CODEBOOK}}

## S3. Taxonomies with corpus counts and examples

{{TAXONOMIES}}

## S4. Reliability

### S4.1 Five comparisons per field (round-1 samples)

{{T26}}

Kappa is Cohen's kappa for single-label fields, quadratic-weighted kappa for ordinal fields (relevance 0 to 3; each principle 0 to 2) and the mean of per-label kappas over labels with at least six positives for multi-label fields (where the agreement column reports the mean Jaccard index). All comparisons are against the v1 final annotations (the original run overlaid by the re-cleaned re-annotations), which is the version the v1 analyses used; the last column compares those with the v2 blind extended-excerpt annotations that replace them for governance documents. The five samples (160, 160, 160, 160 and 351 documents) are drawn from the round-1 collection and are unchanged since v2; round-2 documents are not in them (see S4.7). Two cells are degenerate and should not be read as reliability: the governance flag in the extended comparison (kappa −0.005 at a prevalence near 99%) and methodology (1.0, all "not applicable").

### S4.2 Excerpt versus full text

{{T27}}

{{T27b}}

### S4.3 What the v2 extended, blind re-annotation changed for governance documents

{{T35}}

### S4.4 Cross-checks against the collectors' labels (round 1)

{{S10}}

The collectors' labels for issuer type and country were visible to the v1 annotator in the cover block of 483 texts and in the prompt metadata, so these cross-checks overstate independent agreement; the blind re-annotation (S4.1) measures how much the labels change without that information. The round-1 collectors were the regional teams; their labels were not used as a reference for any analysis.

### S4.5 Protocol for a human validation sample (not executed in this study)

A stratified sample of at least 200 documents (all embodied-AI principal instruments; all principal binding instruments; research outputs, government reports and communications in proportion; non-English documents in proportion, with Chinese and Japanese readers; round-1 and round-2 documents in proportion, including standards captured as scope text only and texts the excerpt truncated) would be double-coded by two domain coders using the codebook, with disagreements adjudicated. Human-versus-model kappa per field would be reported, and headline proportions corrected for measurement error with design-based supervised learning (Egami et al. 2023) or prediction-powered inference (Angelopoulos et al. 2023). No human coders were available in this setting, so this was not done in any version; every label in the package is model-produced, and the checks in S4.1, S4.6 and S4.7 measure consistency between model outputs, not correctness.

### S4.6 Round-2 documents: the collectors' metadata versus the blind annotation (a consistency check)

The round-2 collector agents recorded jurisdiction, issuer, year, instrument type, binding nature, status and robot types for every candidate from the catalogue or gazette page, and the harvest scripts wrote one constant instrument type, binding nature and status per source; none of this was shown to the model. On the 1,626 usable round-2 documents the blind annotation agrees with the collector label on whether an instrument is legally binding in 93% of cases (kappa 0.85, n = 1,608), with the jurisdiction code in 98% (n = 1,624), with the year within one year in 94% (n = 1,542) and with the instrument type mapped to document class in 77% (kappa 0.66, n = 1,608); split by origin, binding-nature agreement is 92% (kappa 0.79, n = 754) for collector-agent rows and 94% (kappa 0.88, n = 854) for harvested rows (companion report, Tables 57 and 58). Because the collector agents were AI agents of the same model family as the annotator and the harvested labels are source constants, this is a consistency check between model outputs and script defaults, not a validation; the disagreements on class are mostly guidelines and parliamentary material that the model read as binding or as reports, and regulations the model read as news or catalogue pages. The per-document comparison can be rebuilt from `data/round2_inventory.csv` and `data/master_table.csv`.

### S4.7 Round-2 reliability sample, reliability variants and the CJK re-annotation

{{S09b}}

A stratified sample of 160 round-2 documents (the ids are the files in `annotations/reliability_round2_opus/`) was re-annotated by a second model (Claude Opus 5.5) and by a same-model re-run (Claude Sonnet 5.5), both under the v2 blind extended-excerpt policy, and compared field by field with the final round-2 annotations (`data/reliability_fields_r2opus.csv`, `_r2rerun.csv`; 129 and 127 rows). By the master-table fields of the sampled ids, the sample holds 116 English, 29 Chinese, 6 Japanese and 1 Korean document (36 Chinese, Japanese or Korean in all, with 8 others); 63 binding instruments, 52 soft-law instruments or standards (30 technical standards), 23 drafts, 14 government reports and 8 communications; 109 substantive captures, 24 partial and 27 landing pages; a median of 848 words, with 31 documents under 150 words; 96 in the embodied set.

Against the second model the median kappa over the 37 single-label and ordinal rows (16 single-label fields, relevance and the 20 principle levels) is 0.86 (0.81 over all 129 rows including the multi-label items); the weakest fields are page quality (0.53), stance toward regulation (0.65), publication stage (0.66), date basis (0.70), instrument status (0.75) and document type (0.79); the set-defining fields are AI scope 0.83, document class 0.86, binding nature 0.86, embodiment status 0.86, primary robot type 0.89 and relevance 0.93 (quadratic-weighted; 0.76 unweighted); jurisdiction 0.96; 19 of 20 principle levels are at or above 0.79 (solidarity 0.72); among multi-label items the weakest are the taxation topic (0.16), the creation of an oversight body (0.35), domestic robots (0.32), self-regulation codes (0.43), the education sector (0.49) and the "other" topic (0.50), and the mechanisms that carry the findings are at 0.72 (licensing and registration), 0.79 (references to standards), 0.84 (conformity assessment), 0.93 (risk-based tiering) and 0.96 (insurance). Against the same-model re-run the median is 0.91 (0.89 over all rows); AI scope 0.84, relevance 0.95, instrument status 0.89, binding nature 0.90, document class 0.93, stance 0.84, date basis 0.85, page quality 0.69 and publication stage 0.66; every principle level at or above 0.83; the weakest multi-label item is the creation of an oversight body (0.58). The round-1 values for the same statistics are 0.85 and 0.91 (S4.1), so the codebook transfers to the round-2 genres with the same overall consistency and the same weak fields (page quality, stance, date basis), plus instrument status and publication stage, which matter more in a legal-text collection.

Table S09b gives, for all six comparisons, the quadratic-weighted and unweighted kappa for relevance and for the median principle, and the agreement and kappa on the level-2 ("treated in depth") threshold: round-1 second model 0.90 / 0.73 (relevance), 0.85 / 0.75 (principles), level-2 kappa 0.69; round-1 re-run 0.96 / 0.87, 0.89 / 0.83, 0.84; round-1 full text 0.94 / 0.82, 0.88 / 0.80, 0.83; round-1 blind 0.94 / 0.84, 0.91 / 0.84, 0.85; round-2 second model 0.93 / 0.76, 0.86 / 0.79, 0.81; round-2 re-run 0.95 / 0.86, 0.91 / 0.87, 0.89. The unweighted kappas are 0.05 to 0.18 lower than the weighted ones, which is the price of the ordinal scales; the level-2 kappas are the reliability of the depth statistics in Table 9.

Limits of this check. The second-model and re-run annotations were produced before the character-aware cleaner (policy without `cjk_clean=v4`), so for the 36 Chinese, Japanese and Korean documents in the sample the comparison with the final annotation also measures the effect of the cleaner change; 27 of the 160 are landing pages, on which agreement is easy; the sample was drawn to cover languages, classes and lengths, not to estimate a population kappa; and agreement between two models says nothing about whether either is right.

The CJK re-annotation. The v2 cleaning rule drops short lines near the top of a text that carry no digit, capital letter or sentence punctuation, to remove navigation menus; Chinese, Japanese and Korean have no whitespace words and no ASCII full stops, so the rule deleted most CJK paragraphs. The AI researcher's review measured a median of 24% of each Chinese document reaching the model (n = 270), 97 Chinese documents whose raw text named robots, AI, drones or automated driving but whose model input contained none of those terms (83 of them labelled "not about AI"), and a median of 50% for Japanese. The v4 cleaner never drops a line that contains CJK characters or CJK punctuation (policy tag `cjk_clean=v4`); all 376 round-2 and 46 round-1 Chinese, Japanese and Korean documents were re-annotated (`annotations/round2`, `annotations/cjk_fix`; 380 and 46 annotation files). Of the 422 documents, 57 changed embodied-set membership and the number rated not about AI fell from 205 to 160 (review log, A1). The master table carries the policy string per document (`_policy`), so the two cleaner versions can be separated.

## S5. Instruments in the embodied-AI set (after corrections)

{{T33}}

{{T33b}}

The lists that follow are generated from the v4 master table on the comparable unit, every usable text of instrument class, with the counting-unit flag available in the master table (`instrument_unit`) for each row. S01 lists the 291 legally binding texts in the embodied-AI set (207 regulations or decrees, 71 statutes, 9 mandatory standards, 3 court decisions and 1 treaty captured as a status page); 195 of them are principal instruments and are listed with their relevance tier and capture quality in Table 33b (182 in force, 9 superseded, 4 adopted but not yet in force; 175 substantive and 20 partial captures; 168 rated robot-relevant). S02 lists the 411 soft-law texts and technical standards (the embodied set holds 254 technical standards by document type across S02 and S03, of which 62 have a content-analysed scope page and 192 are catalogue entries; the 47 standards under development are classed as drafts by rule, 42 of them, and are not published instruments). S03 lists the 105 proposals, bills and consultations that carry the governance flag (108 draft-class texts in all; CCW working papers and chair's texts are no longer in it). S04 lists the 97 government and parliamentary reports. S05 lists the 205 usable governance documents whose scope label is general-AI with embodied provisions; it is not the 97-instrument "with embodied provisions" tier of Table 33, which is defined by relevance 0 or 1 plus a robot-type label on the principal unit, so the two overlap but are not nested. Round-2 documents carry identifiers beginning `R2-`; the principal instruments round 2 added are listed in Tables 59 (190 binding) and 60 (378 robot-relevant) of the companion report. Technical standards appear with the text status of their public scope page.

{{S01}}

{{S02}}

{{S03}}

{{S04}}

{{S05}}

## S6. Coverage audit against a reference list of instruments

{{T25}}

The reference list (`data/reference_instruments.csv`) was compiled from the governance expert's reviews and covers binding law, quasi-binding instruments and the principal safety standards relevant to embodied AI, together with the main general-AI instruments as controls. It has 39 entries after the v4 repairs: UN Regulation No. 157 and No. 171 are separate rows (R171 is not captured); Taiwan's industrial-robot hazard prevention standards are dated 2018 (promulgated 1987, amended 2018), not 2025; and the "US state AV statutes" entry uses a stricter pattern (named codes, acts and regulations rather than any page mentioning autonomous vehicles). "Captured" now means that a principal instrument with a content-analysed capture matches the instrument's title pattern; the looser v3 criterion (any document of a matching title family, including enforcement orders, web pages and national adoptions) is kept for comparison. "Citing" counts usable documents whose full text matches the pattern.

On the strict criterion 22 of 39 are captured (11 in v2); on the loose criterion 31 (12 in v2). The 17 not captured are the German Autonomous Driving Act (StVG amendment, 2021; 9 documents cite it), Korea's Intelligent Robots Development and Distribution Promotion Act (2008; 9) and AI Basic Act (5), the revised Product Liability Directive (EU) 2024/2853 (48), the Shenzhen intelligent-connected-vehicle regulation (2022; 34), Beijing's humanoid and embodied-intelligence measures (25), ISO/TS 15066 (27), IEC 61508 (14), ISO 26262 (26), ISO 21448 (18), ISO/IEC 42001 (37), IEEE 7001 (7), ANSI/RIA R15.06 (5), ANSI/A3 R15.08 (1), the OECD AI Principles (56), Taiwan's industrial-robot hazard prevention standards (0) and UN Regulation No. 171 (1). The two US executive orders of 2023 and 2025 are captured (D0915, D0918). Beyond the list, the round-2 collectors located and verified instruments the environment could not read; section 7.1 of the governance review names them and they are listed in the analysis report (Section 11.5) as the first targets of a round 3: the Hangzhou embodied-robot regulations (2026), the Shenzhen regulations on intelligent connected vehicles, the AI industry and the low-altitude economy, Hong Kong's Road Traffic (Autonomous Vehicles) Regulation, Korea's Intelligent Robots Act and decree and its Autonomous Vehicles Act decrees, DoD Directive 3000.09, California SB 243, India's Drone Rules 2021, the Product Liability Directive 2024/2853, the Toy Safety Regulation 2025/2509 and Directive 2009/48/EC, France's ordonnance 2021-443 and décret 2021-873, Switzerland's DETEC ordinance on aircraft of special categories, ANSI/A3 R15.06-2025 and GB/T 48317.1-2026. The companion report counts 189 verified candidates recorded as legally binding that remain unread.

## S7. Related datasets and how this collection differs

| Resource | Scope | Relation to this collection |
|---|---|---|
| OECD.AI Policy Observatory | National AI policies and instruments (1,000+) | Broader on general AI; does not separate embodied systems or code content at the principle and mechanism level. |
| AlgorithmWatch AI Ethics Guidelines Global Inventory | Ethics guidelines (160+) | Guideline-only; several of its entries are in this collection's general-AI set. |
| Stanford AI Index legislation tracker; IAPP Global AI Law and Policy Tracker; Digital Policy Alert | Legislation and policy events | Event trackers rather than coded corpora; useful for extending the coverage audit. |
| RoboLaw guidelines (Palmerini et al. 2014); Nevejans (2016); Bertolini (2020) | Expert legal mapping of robotics regulation in Europe | Hand-coded analyses of the regimes this collection codes automatically; natural baselines for a validation study. |
| Reviews of AV regulation (Taeihagh and Lim 2019) and drone regulation (Stöcker et al. 2017) | Sector regulation | Document the sectoral binding layer that round 2 brought into the collection (Tables 59 and 60); useful for auditing its jurisdiction coverage. |

The collection differs from these in coding research, policy and law in one scheme, across eight regions and ten languages, with a stated counting unit and construct tiers; it is a coded corpus with model-produced labels, not a hand-verified register.

## S8. Quality-assurance flags, corrections, counting-unit rules and duplicates

{{S06}}

**Corrections from earlier versions.** Corrections applied after the v1 review are listed with their reasons and sources in `data/overrides_applied.csv` (79 field corrections on 27 round-1 documents); duplicates removed by the documented merges and the second deduplication pass are in `data/duplicates_removed.csv` (128 rows: 49 round-1 captures and 79 round-2 candidates removed as duplicates on normalised title and jurisdiction).

**v4 counting-unit rules** (`scripts/07c_v4_units_and_tiers.py`, applied after the overrides above, to every round). Each legal text receives an `instrument_unit`:

- `language_copy`: title contains "corrigendum", "language version" or "rectification".
- `incorporation`: title names an EEA Joint Committee decision.
- `ancillary`: title names a commencement or bringing-into-force instrument, a levy, fee or charges instrument, an exemption, direction, area approval, approval for operation, permit or authorisation for operation or flights, a definitions-only part or a table of contents or chapter index.
- `amendment`: title contains amend, modify, supplement, repeal or vary (kept in the headline unit).
- `catalogue_page`: the capture is a landing or index page.
- `stub`: a principal or amendment text under 150 words whose capture is not a substantive document (the v2 Taiwan-stub rule, now applied to every round).
- `duplicate_text`: a byte-identical text already counted under another id (MD5 of the text file; the longer-worded capture is kept).
- `dependent`: assigned by the audited corrections below to parts, copies and successive versions of an instrument already present.
- `principal`: everything else. The headline unit, `principal_instrument`, is `principal` or `amendment` on a text of instrument class.

Among the 810 embodied legal texts the rules leave 463 principal texts and 42 amendments (505 principal instruments), 222 catalogue pages, 35 stubs, 30 ancillary instruments, 10 dependent parts, 6 incorporation decisions and 2 language copies; among the 291 binding texts, 164 principal and 31 amendments (195), 28 ancillary, 25 stubs, 28 catalogue pages, 7 dependent, 6 incorporation and 2 language copies (master table).

**Instrument families** (`family_key`): the normalised title with years, act numbers (2019/947, 64/23), version and instrument numbers and amending words removed, plus the jurisdiction; `family_size` is the number of texts of instrument class sharing a key and `family_rep` marks the longest usable capture, which carries the family-level count (194 of the 195 principal binding instruments are family representatives; Table 53b).

**AI-content tiers** (`ai_explicit`, `autonomy_terms`), from the full text and cached in `data/ai_content_flags.csv`: `ai_explicit` is true when the text contains at least two matches of artificial intelligence, machine learning, AI system, AI, algorithm, neural network, deep learning or intelligent system, or their Chinese, Japanese, Korean, French, German, Spanish, Portuguese or Italian equivalents; `autonomy_terms` is true when it contains at least two matches of autonomous or automated operation, driving, vehicle, flight, system, lane or function, self-driving, driverless, remotely piloted, unmanned, automated driving system, ADS or automation, or their Japanese, Chinese, Korean, French, German, Spanish or Portuguese equivalents, or when `ai_explicit` is true. `words_ok` marks captures of at least 150 words, the floor for depth (level-2) statistics.

**Status and class rules** (same script): technical standards whose title carries a development-stage designation (AWI, PWI, WD, CD, DIS, FDIS, DTS, DTR, PRF) are set to status under development and class proposal or draft (47 standards in the embodied set); Chinese national standards numbered GB without /T or /Z are binding (class binding instrument, binding nature mandated standard); CCW working papers, chair's summaries, rolling texts and the draft articles on autonomous weapons issued from the international or unknown jurisdiction are classed as government or parliamentary reports (position and process documents), not instruments; proposals and draft texts whose adopted act is in the collection under a matching title are set to superseded.

**Audited doc-level corrections** (`data/manual_overrides_v4.csv`, applied last; the file keeps the reason and source per row). The governance expert's audit of v3 (`review/governance_expert_review.md`, with the row table `review/v3_reviews/governance_audit_rows.csv`) judged 159 instruments in the review text (108 with at least one error, 68%; 98 with a material one, 62%; the released row table holds 165 rows, 119 with an error code and 107 material) with error codes A (dependent act counted separately), B (not an instrument: stub, catalogue, register or status page), C (wrong binding class or document class), D (wrong lifecycle status), E (wrong year), F (wrong jurisdiction) and G (not genuinely about embodied-AI governance). The codes were converted into 157 field-level corrections on 91 documents (156 rows concern round-2 documents): 50 counting-unit corrections (36 to `catalogue_page`, 14 to `dependent`), 32 relevance corrections and 32 robot-type corrections (code G: relevance set to 1 and the robot-type labels removed, so that the text leaves the robot-relevant tier), 17 status corrections (9 to superseded, 6 to in force, 2 to withdrawn or lapsed), 14 class corrections (6 to binding, 5 to soft law, 3 to report), 7 enactment-year corrections and 5 binding-nature corrections (to mandated standard). The audit sample was risk-stratified, so its error rates are upper bounds for the tables as a whole; the random-sample precision audit in S13 gives the population estimate. Two consequences of the mechanical mapping are known: the Machinery Directive 2006/42/EC was at first set to superseded by its D code although the reviewer's point was that it remains in force until January 2027 (the override now reads in force), and the Beijing E-Town embodied-robot measure is both a catalogue-page unit and a soft-law class (it leaves every instrument count either way).

## S9. Coverage accounting (collection stage)

{{STAGE1}}

### S9.1 Collection round 2: inventory and collector reports

The stage-1 accounting above covers the round-1 manifests. Round 2 is accounted for in `data/round2_inventory.csv`, which has one row for each of the 2,075 de-duplicated candidates with the collectors' metadata (jurisdiction, subnational unit, issuer, year, instrument type, binding nature, status, robot types, language, primary and secondary URL, source database, confidence and a one-line note), the de-duplication keys, the fetch outcome and URL, the text status and whether the candidate was content-analysed (1,720 were, including four texts recovered in a retry pass after the v3 review; 355 have no text and appear in no count). Tables 50 to 52 in the companion report summarise the inventory by discovery source, fetch outcome and blocked host. The condensed collector reports (`collection_round2/COLLECTOR_REPORTS.md`, with the candidate CSVs and the candidate schema) record for each of the nine briefs what was found and verified, which hosts blocked the sandbox, where the shared search budget ran out and which instruments were looked for but not found; the collectors were Claude subagents, and 189 verified candidates recorded as legally binding remain unread. These reports bound what round 2 can claim and are the starting point for any further round.

## S10. Version history: v1 to v4

The study has had four versions, each revised after independent adversarial reviews (six per cycle; the reviewers of v1 and v3 were AI agents with written briefs, as were the round-2 collectors and the v3 precision auditor). The narratives no longer carry the version history; it is kept here so that readers of earlier versions can trace each number. The before-and-after comparisons between the two collection rounds are on the comparable unit, every usable text of instrument class, because the principal unit did not exist before v4; they describe where each collection searched and are not findings about the world.

| Quantity | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| Documents annotated | 1,703 | 1,656 | 3,291 | 3,295 |
| Usable documents | 1,589 | 1,538 | 3,148 | 3,165 |
| Embodied-AI set / general-AI set | 674 / 859 | 675 / 806 | 1,589 / 982 | 1,603 / 1,015 |
| Embodied instruments, every legal text | 63 | 65 | 808 | 810 |
| Embodied principal instruments | | | | 505 (408 robot-relevant; 395 with autonomy or AI provisions; 153 naming AI) |
| Robot-specific instruments (relevance 2 or 3), every legal text | | 34 | 681 | 699 |
| Binding embodied instruments, every legal text | 7 (claimed) | 5 (4 in force) | 299 (268 in force) | 291 |
| Binding embodied principal instruments | | | | 195 (182 in force; 168 robot-relevant; 194 per family; 140 with autonomy or AI provisions; 15 naming AI) |
| Independent precision estimate for the binding set | | | | 54% (44 to 63) of the 299 v3 texts distinct, binding and substantive: about 161 (132 to 190) |
| Technical standards in the embodied set | 12 | 8 (4 content-captured) | 238 (177 catalogue pages) | 254 by document type; 62 with a content-analysed scope page |
| Jurisdictions with an embodied legal text | | 30 | 60 | 60 |
| Reference instruments captured | | 11 of 39 strict; 12 loose (recomputed; the v2 audit reported 10 of 38) | 31 of 38 loose | 22 of 39 strict; 31 loose |
| Core principles lower in embodied than general instruments after Holm | | none of 14 (65 vs 258 instruments) | 11 of 14 pooled (804 vs 367) | 10 of 14 pooled (505 vs 372); 0 of 14 within round-1 instruments; 10 of 14 within round-2 instruments (Table 20b) |
| Adjusted core principles differing (embodied vs general) | | | 13 of 14 (class, region, year) | 10 of 14 (class, region, round, year) |
| Trend in risk-based tiering / conformity-assessment mechanism, odds ratio per year | | about 1.3 / 1.3 | 1.09 (Holm p = 0.10) / 1.05 | 1.31 / 1.26 within round 1; 1.10 / 1.05 with round as covariate (Table 30) |
| Proximity and liability trend | | | 0.93 / 0.93 per year (decline) | pooled 0.94 / 0.94; flat within round-1 documents (1.00 / 1.00; Table 30); not reported as trends |
| Regional divergence | | core does not differ; tools do (V 0.19 to 0.33) | 33 of 38 items (V 0.08 to 0.34), "values too" | 34 of 38 (V 0.09 to 0.35); values claim qualified: within research outputs 2 of 14 core principles differ by region, within principal instruments 12 of 14 (T29b); Europe and North America 0.01 apart on research outputs (T31) |
| Chinese, Japanese and Korean documents rated not about AI | | | 205 of 422 (cleaner defect) | 160 (57 changed set membership) |
| Reliability samples | round-1 inter-model and re-run | five round-1 comparisons (160, 160, 160, 160, 351) | unchanged | plus 160 round-2 documents, second model (median 0.86) and re-run (0.91); unweighted and level-2 variants (S09b) |
| Human validation | none | none | none | none |

What changed between versions and why. v1 to v2 (`review/adversarial_review_and_changes.md`): 46 duplicate captures merged and 3 off-topic or failed captures excluded; catalogue, committee and article pages reclassified; the AI Act duplicate removed, the Taiwan login stub excluded, EO 14110 marked revoked; every governance document re-annotated from a longer, metadata-blind excerpt; lexicons repaired; comparisons restricted to within-genre or adjusted estimates. v2 to v3 (`review/v3_changes_*.md`): a second collection round of 2,075 candidates from legal databases, treaty archives, standards catalogues and regulator sites, 1,716 with text, annotated under the v2 blind policy; the collection doubled and the embodied instrument layer grew twelvefold on the comparable unit. v3 to v4 (`review/adversarial_review_v3_and_changes_v4.md`): the counting unit, families and AI-content tiers (Table 53b); collection round as covariate and stratum (Tables 20, 20b, 30); the character-aware cleaner and CJK re-annotation; status and class rules and 157 audited corrections; the round-2 reliability sample and variants; the precision audit; the strict coverage criterion; the capture-tier rule for depth statistics; a recovered-fetch pass (four texts); stored inputs and a run manifest; five figures rebuilt; the dashboard regenerated from data.

{{T53}}

Table 53 gives the before-and-after on the comparable unit. The twelvefold rise of embodied legal texts (65 to 810) and the rise of binding embodied texts from 5 to 291 are what a search of legal databases returns that a topical web search does not; on the headline unit the same collection holds 505 principal embodied instruments and 195 binding ones. Tables 54 and 55 in the companion report give the additions by region and robot group with the v4 column on the principal unit. Within the round-1 documents the v2 results hold (no core-principle difference within instruments; compliance machinery growing about 30% a year); within round 2 they do not (Tables 20b and 30). The analysis report presents this contrast as its methodological result.

## S11. Extended tables

{{S08}}

{{S11}}

OpenAlex citation counts are reported as retrieved; several values are implausible for the stated venue and year and almost certainly reflect record merges on OpenAlex's side. They were not used in any analysis beyond the median citation statistic.

{{S12}}

{{S13}}

Tables S12 and S13 count governance-flagged documents on the comparable unit (any mention of a robot type, every legal text); the principal-unit counts per group and category are in Tables 55 and 7.

{{T24}}

{{T11}}

## S12. Datasheet

- **Motivation.** To describe quantitatively how the machine classes in which embodied AI is deployed (robots, vehicles, drones, medical and industrial machines, autonomous weapons) are governed worldwide compared with AI in general, from a purposive multilingual document collection built by eight regional teams and extended by a targeted second collection round for instruments, with a stated counting unit and AI-content tiers.
- **Composition.** 3,423 registry rows (the round-1 captures, the recovered files and 1,720 round-2 candidates with text) reduced to 3,295 annotated and 3,165 usable documents after deduplication and exclusion of failed and off-topic captures; one row per document in `data/master_table.csv` with 197 fields (collection metadata, text features, OpenAlex enrichment, 39 model-annotated fields, derived regions and years, lexicon features, and the v4 fields `instrument_unit`, `principal_instrument`, `family_key`, `family_size`, `family_rep`, `ai_explicit`, `autonomy_terms`, `words_ok`, `text_hash` and the annotation policy per document). The corpus over-represents Europe (42% of usable documents) and English (75%); Chinese-language documents (9%) come almost entirely from one round-2 harvest of the State Council policy library; the robot-specific sprint drew mainly on academic literature, the general-AI database on official sources, and round 2 on legal databases, standards catalogues and regulator sites, so the instrument layer is dominated by vehicle, drone, workplace and product law and by jurisdictions with open legal databases that the environment could reach. Of the 810 embodied legal texts, 505 are principal instruments; the rest are catalogue pages, stubs, amendments and ancillary, dependent, incorporation or language-copy acts, flagged per row. A further 2,075-row inventory (`data/round2_inventory.csv`) lists every round-2 candidate, including the 355 without text.
- **Collection process.** Round 1: regional teams of people listed sources in manifests and saved them as files (2,557 files); 266 listed sources could not be captured. Files were converted to text; oversized files were recovered through a document reader where possible. Round 2: nine collector agents (Claude subagents) with regional, thematic and standards briefs and scripted harvests of seven legal databases (eight runs) produced candidate lists that were de-duplicated within the round and against round 1; texts were fetched from the issuing source with documented fallbacks and a retry pass; technical standards were captured as public scope text only, 16 of them through a committee mirror or as collector-written abstracts.
- **Labelling.** All fields were assigned by a language model under a fixed codebook; governance documents were re-annotated in v2, every round-2 document annotated, and every Chinese, Japanese and Korean document re-annotated in v4, from extended excerpts without collector metadata. No person read or labelled any document. Corrections are rule-based (S8) or documented per document (`data/overrides_applied.csv`, `data/manual_overrides_v4.csv`, the latter converted from an audit written by an AI agent acting as governance expert). The reliability checks (S4) compare model outputs with each other; the precision audit (S13) is an independent model-assisted reading of 100 documents.
- **Uses.** Comparative description of governance discourse and instruments within this collection; not a census of instruments, not a register of what is in force, and not a source of legal advice on any instrument's status or applicability.
- **Distribution and licence.** Code MIT; derived data CC BY 4.0; source texts not redistributed (publishers' copyright); source URLs and content hashes in `data/registry.csv`, and for round-2 candidates the primary and secondary URLs in `data/round2_inventory.csv`; the exact model inputs for the round-2, CJK, governance and blind-reliability runs in `annotations/*/_inputs/`; models, prompt hashes, policies, counts and costs per run in `data/run_manifest.json`. The copyright status of the mirrored standards' scope pages was not checked.
- **Maintenance.** Corrections are made through `data/manual_overrides.csv` and `data/manual_overrides_v4.csv` with a reason and source per row, and through the documented rules in `scripts/07c_v4_units_and_tiers.py`; the pipeline regenerates every output.
- **Ethical considerations.** Documents are public policy, legal and research texts; no personal data were collected beyond author names as published. Texts were sent to a commercial model API for annotation; paywalled and permission-restricted captures were used only to derive labels and short summaries.

## S13. Precision audit of the v3 binding embodied instruments

{{T62}}

**Method.** The population is the 299 documents in the v3 table S01 (binding instruments in the embodied-AI set; 294 round-2 and 5 round-1 ids). A simple random sample of 100 without replacement was drawn from the alphabetically sorted ids with `numpy.random.default_rng(2026)`; the draw is reproducible and the ids are in `review/v3_reviews/precision_audit_sample.csv`. The auditor was an independent AI agent (Claude) with a written brief and no part in the earlier annotation; it read each document's own text (at least the first 6,000 characters plus the tail), keyword hit counts and context snippets for robot, autonomy, drone, AI and ancillary-paperwork markers in English, Japanese and Chinese, and the master-table row as a guide only, and judged five yes-or-no criteria: (a) distinct instrument (a principal legal instrument or substantive amendment; not a commencement order, individual exemption or approval, definitions-only section, table-of-contents, index, catalogue, register or tracking page, EEA incorporation decision, language corrigendum, date-only amendment, harmonised-standards publication decision or duplicate); (b) legally binding as captured; (c) substantive embodied provisions (obligations, prohibitions, requirements or authorisations specific to robots, automated vehicles, drones, delivery, surgical or medical robots, exoskeletons, humanoids or autonomous weapons, not a mention, list entry, eligible-business category or scope clause); (d) autonomy or AI content (any provision about automation, autonomy, remote piloting, algorithms, machine learning or AI); (e) explicit AI (artificial intelligence, machine learning, AI systems or algorithms named in an AI sense); plus (f) a counting-unit note on whether the text belongs to a family with another member in the population. The full report is `review/v3_reviews/precision_audit.md`.

**Shares with 95% Wilson intervals (n = 100).**

| Criterion | Yes | Share | 95% interval |
|---|---:|---:|---|
| (a) distinct instrument | 67 | 0.67 | 0.57 to 0.75 |
| (b) binding | 97 | 0.97 | 0.92 to 0.99 |
| (c) substantive embodied provisions | 56 | 0.56 | 0.46 to 0.65 |
| (d) autonomy or AI content | 67 | 0.67 | 0.57 to 0.75 |
| (e) explicit AI | 14 | 0.14 | 0.09 to 0.22 |
| (a) and (b) | 64 | 0.64 | 0.54 to 0.73 |
| (a), (b) and (c) | 54 | 0.54 | 0.44 to 0.63 |
| (a), (b), (c) and (d) | 53 | 0.53 | 0.43 to 0.62 |

Among the 54 documents passing (a), (b) and (c), 53 also pass (d) and 8 pass (e). Multiplying the population of 299 by the joint share gives about 161 binding instruments with substantive embodied provisions (132 to 190); requiring autonomy or AI content as well gives about 158 (129 to 187). This is a precision correction only: it does not consolidate families and it does not add instruments the collection missed, so precision and recall corrections are reported separately and never netted. By region the joint share is 0.54 in Europe (15 of 28), 0.62 in North America (16 of 26), 0.78 in Asia (14 of 18) and 0.11 in Oceania (2 of 18): every Australian document in the sample was captured from legislation.gov.au as a register page or table of contents, and 12 of the 15 are individual CASA or ACMA approvals, directions, exemptions or naming instruments. By primary robot type the joint share is 0.59 for drones (30 of 51) and 0.63 for automated road vehicles (19 of 30); the smaller categories are indicative only. Primary failure types among the 46 failing documents: individual exemption, approval or direction instruments captured as register pages (14); binding regimes with no embodied-specific provision (10); register, catalogue, index or table-of-contents captures (9); ancillary EU and UK acts (standards-list decisions, a corrigendum, date postponements, an EEA incorporation decision, commencement orders; 8); non-binding Chinese policy or industrial-support documents coded as regulations (3); definitions-only sections (2). Sixty of the 100 belonged to a family with at least one other member in the population (Japan's Road Traffic Act with its enforcement order and regulations; the EU drone regulations 2019/945 and 2019/947 with their amendments, retained UK copies and EEA decisions; the UK Automated Vehicles Act with its commencement and marketing regulations; the yearly CASA directions, exemptions and approvals; the US small-UAS parts and export-control parts; successive Argentine, Icelandic and EU versions of one regime).

**Comparison with the v4 rules on the same documents (Table 62).** The rule-based unit (principal instrument, binding class, embodied set) keeps 74% of the sample where the auditor keeps 67% as distinct (agreement 79%, kappa 0.50); adding the embodied-set and binding conditions, the rules keep 61% (51 to 70) where the auditor keeps 54% (agreement 77%, kappa 0.53; 15 documents the rules keep and the auditor rejects, 8 the reverse); requiring the robot-relevant tier as a proxy for an autonomy or AI provision, the rules keep 46% where the auditor keeps 53% (agreement 71%, kappa 0.42). The rules therefore remove most of the inflation the auditor found but keep about one document in seven that a reader would not count, mostly partial captures of instruments whose operative text is elsewhere and binding regimes whose robot content is a mention; the v4 counts are upper bounds and the audit's 161 (132 to 190) is the independent estimate for the v3 population.

**The eight counting-unit rules the auditor proposed, and their status in v4.**

1. Count regimes, not documents (a principal instrument with its implementing, amending, correcting, commencing and incorporating acts), reporting regimes and documents per regime separately. Partly: the principal unit excludes the dependent acts and instrument families group renewals, versions and parts (194 of 195 principal binding instruments are family representatives); documents per regime are not reported.
2. Exclude ancillary paperwork by rule, not by model judgement (commencement orders, levy and fee acts, EEA decisions, corrigenda, date-only amendments, harmonised-standards publication decisions, definitions-only and table-of-contents sections, tracking and catalogue pages), keeping them as metadata of the parent. Partly: all of these are excluded except date-only amendments and harmonised-standards publication decisions, which the amendment rule keeps unless the audit overrode them.
3. Exclude individual administrative acts (exemptions, approvals, directions, permits, named-person instruments, device-specific orders, company authorisations) unless they are the only way a jurisdiction regulates the activity, counting a renewed series once. Fixed by the ancillary rule for the titled forms; company authorisations and device-specific orders were handled by the audited corrections.
4. Require operative text: no register header, landing page, index or table of contents, and no text under about 2,000 characters without article text, enters the count until the full text is fetched. Partly: landing pages and captures under 150 words are excluded; partial captures above that floor remain in the unit (20 of the 195 principal binding instruments), and the auditor's higher floor was not adopted.
5. Require an embodied-specific operative provision (relevance 2 or more and at least one obligation naming the embodied system), placing generic product-safety, cybersecurity, medical-device and export-control regimes in the "with embodied provisions" tier only when such a provision exists. Partly: the robot-relevant tier (168 binding) is the model's relevance rating, not a test for an operative provision; the 27 binding instruments with embodied provisions are reported separately.
6. Separate binding from policy for Chinese administrative documents (decrees and regulations binding; subsidy measures, plans, replies and notices issuing plans as policy). Partly: mandatory GB standards are binding by rule, and the audited corrections reclassified the Beijing and State Council measures the audit named; no general rule for Chinese document forms was written.
7. De-duplicate across ids where one rule appears as a de novo order and its codified section, as an EU regulation and its retained UK copy, or as successive versions, keeping the current version. Partly: byte-identical texts are one unit and successive versions fall into one family; retained UK copies are kept as distinct instruments of a distinct jurisdiction.
8. Report precision-corrected counts with the sampling interval and keep the recall audit separate. Fixed: Table 62, the key-numbers table and Section 11.2 of the analysis report give both, and the coverage audit (S6) is reported apart.

## S14. Figure index

| Figure | File | Content |
|---|---|---|
| 1 | F01_composition_by_set | Document classes by set |
| 2 | F02_timeline | Documents per year by set (2014 to 2026) |
| 3 | F03_issuer_types | Issuer types by set |
| 4 | F04_lifecycle_binding | Lifecycle status and binding nature (governance-flagged documents) |
| 5 | F05_embodied_share_by_year | Embodied share per year (collection effect) |
| 6 | F06_cumulative_instruments | Cumulative embodied legal texts by binding nature (comparable unit) |
| 7 | F07_region_counts | Documents by region |
| 8 | F08_top_countries | Top 20 national jurisdictions (principal embodied instruments) |
| 10 | F10_language_by_region | Language by region |
| 11 | F11_categories | Robot types addressed |
| 12 to 14 | F12, F13, F14 | Robot types by region, class, period |
| 16, 17 | F16, F17 | Co-occurrence of robot types and of topics |
| 18 | F18_governance_gap | Research vs governance attention (principal instruments) |
| 19 | F19_sectors | Sectors by set |
| 20 | F20_principles_by_set | Principles by set (pooled) |
| 21, 22 | F21, F22 | Principles by region and by class |
| 23 | F23_embodied_principles_by_type | Embodied-specific considerations by document type, content-analysed captures of at least 150 words (rebuilt in v4) |
| 24 | F24_mechanisms_by_set | Mechanisms, principal instruments only and all documents |
| 25 | F25_mechanisms_by_region | Mechanisms by region |
| 26, 27 | F26, F27 | Framing by region; stance by class |
| 28 | F28_personhood_over_time | Personhood positions |
| 29, 30 | F29, F30 | Instruments cited by set and by region |
| 31 | F31_region_similarity | Regional distances, dendrogram order and aligned region set with n (rebuilt in v4) |
| 33 | F33_term_trends | Term usage within the embodied set |
| 34 | F34_topic_change | Topic change with adjusted significance |
| 35 | F35_reliability | Inter-model and test-retest reliability (round 1) |
| 36 | F36_lexicon_validation | Lexicon validation (repaired) |
| 37 | F37_coverage | Collection coverage (round-1 lists only) |
| 38 | F38_adjusted_odds | Adjusted odds ratios, embodied vs general (with collection round) |
| 39 | F39_stratified_principles | Within-genre principle comparison (single shared axis, rebuilt in v4) |
| 40 | F40_gap_bootstrap | Gap index with bootstrap intervals; title computed from Table 22 (rebuilt in v4) |
| 41 | F41_coverage_audit | Coverage audit on the strict capture criterion (rebuilt in v4) |
| 42 | F42_category_trends_within_embodied | Robot-type trends within the embodied set |
| 43 | F43_reliability_three_way | Full-text vs excerpt vs second model |
| 44 | F44_blind_reannotation | Metadata-blind re-annotation |
| 50 | F50_round2_funnel | Round 2: candidates to texts, usable captures and principal instruments |
| 51 | F51_before_after_region | Embodied instruments by region, before and after round 2 |
| 52 | F52_round2_classes | Round-2 additions by annotated document class |

Each figure exists as `<name>.png` and `<name>.svg` (light) and `<name>_dark.png` and `<name>_dark.svg` (dark), with the plotted values in `figures/data/<name>.csv`; Figure 31 has two data files (distance matrix and similarity matrix) and Figure 42 has no data file in this build.
