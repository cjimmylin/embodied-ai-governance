---
title: "Supplementary material (v2): codebook, reliability, coverage audit, instrument lists, datasheet"
subtitle: "Companion to the analysis report and paper on the governance of embodied AI and robotics"
author: "Prepared with Claude Code for Jimmy Lin, Centre for Enterprise Innovation (CEI) AI Robotics project"
date: "31 October 2026"
---

## S1. Pipeline, reproducibility and what changed in v2

All steps are scripts in `scripts/` and run in numerical order. Steps 01 to 05 require the converted source texts; steps 07 onward run from the stored annotations, so every number in the report can be regenerated from the package.

| Step | Script | Output |
|---|---|---|
| Registry and first deduplication | `01_build_registry.py` | `data/registry.csv`, `data/files.csv` |
| Text features | `02_text_features.py` | `data/text_features.csv` |
| OpenAlex enrichment (DOI-based) | `03_openalex.py` | `data/openalex.jsonl` |
| Model annotation (v1 excerpt; v2 blind extended excerpt for governance documents) | `04_annotate.py` | `annotations/main`, `main_clean`, `gov_extended`; reliability runs in `reliability_*` |
| Full-text lexicons (repaired in v2) | `05_lexicons.py` | `data/lexicon_features.csv` |
| Master table | `07_assemble.py` | `data/master_table_raw.csv` |
| Documented corrections and second deduplication | `07b_apply_overrides.py` | `data/master_table.csv`, `overrides_applied.csv`, `duplicates_removed.csv` |
| Reliability (five comparisons) | `09_reliability.py` | `data/reliability_fields*.csv`, `reliability_team_crosscheck.csv` |
| Analyses | `13_analysis_A.py`, `14_analysis_B.py`, `15_analysis_C.py`, `18_analysis_D.py`, `19_fulltext_validation.py`, `17_supp_tables.py` | `tables/`, `figures/data/`, `data/results.json` |
| Figures | `20_figures_v2.py` | `figures/` (light and dark PNG and SVG) |
| Dashboard and reports | `10_dashboard.py`, `16_build_reports.py` | `dashboard/`, `report/` |

Annotation used the Claude Code command-line interface in non-interactive mode with the codebook as a fixed system prompt and a JSON schema enforcing all 39 fields; the main model was `claude-sonnet-5-5`, the second annotator `claude-opus-5-5`. The prompt hash of the codebook and schema is `8d4d83e909f0` for every run; v2 runs additionally record an excerpt policy string (`v2|head=100000|mid=6000|tail=4000|blind=True`) and store the exact model input for every document under `annotations/<run>/_inputs/`. The v2 policy strips the collectors' cover block (source URL, issuer, type and tier labels) from the text, passes only the document id, word count and text status as metadata, and keeps short lines containing digits, all-capital headings and sentence-ending lines that the v1 cleaning removed. Temperature and seed are not controllable through the interface used; variability under re-runs is measured directly (test-retest).

Statistics use pandas 3.0, SciPy, statsmodels and scikit-learn: Wilson intervals; chi-square tests with a Monte-Carlo p-value when more than a fifth of expected counts are below five, and Fisher's exact test for 2 by 2 tables with any expected count below five; bias-corrected Cramér's V (Bergsma 2013) with percentile-bootstrap intervals; Holm correction within each family; logistic regression with document class, region and year as covariates; Mantel-Haenszel odds ratios stratified by class; k-means with silhouette and bootstrap adjusted-Rand stability; cosine distance with average linkage, bootstrap intervals and split-half noise floors.

## S2. Codebook

{{CODEBOOK}}

## S3. Taxonomies with corpus counts and examples

{{TAXONOMIES}}

## S4. Reliability

### S4.1 Five comparisons per field

{{T26}}

Kappa is Cohen's kappa for single-label fields, quadratic-weighted kappa for ordinal fields (relevance 0 to 3; each principle 0 to 2) and the mean of per-label kappas over labels with at least six positives for multi-label fields (where the agreement column reports the mean Jaccard index). All comparisons are against the v1 final annotations (the original run overlaid by the re-cleaned re-annotations), which is the version the v1 analyses used; the last column compares those with the v2 blind extended-excerpt annotations that replace them for governance documents.

### S4.2 Excerpt versus full text

{{T27}}

{{T27b}}

### S4.3 What the v2 extended, blind re-annotation changed for governance documents

{{T35}}

### S4.4 Cross-checks against the collectors' labels

{{S10}}

The collectors' labels for issuer type and country were visible to the v1 annotator in the cover block of 483 texts and in the prompt metadata, so these cross-checks overstate independent agreement; the blind re-annotation (S4.1) measures how much the labels change without that information.

### S4.5 Protocol for a human validation sample (not executed in this study)

A stratified sample of at least 200 documents (all embodied-AI governance instruments; all binding instruments; research outputs, government reports and communications in proportion; non-English documents in proportion) would be double-coded by two domain coders using the codebook, with disagreements adjudicated. Human-versus-model kappa per field would be reported, and headline proportions corrected for measurement error with design-based supervised learning (Egami et al. 2023) or prediction-powered inference (Angelopoulos et al. 2023). Until then, the labels should be read as consistent across models and re-runs, not as certified.

## S5. Instruments in the embodied-AI set (after corrections)

{{T33}}

{{T33b}}

{{S01}}

{{S02}}

{{S03}}

{{S04}}

{{S05}}

## S6. Coverage audit against a reference list of instruments

{{T25}}

The reference list (`data/reference_instruments.csv`) was compiled from the governance expert's review and covers binding law, quasi-binding instruments and the principal safety standards relevant to embodied AI. "Captured" means a document in the collection matches the instrument by title; "citing" counts usable documents whose full text matches the instrument's pattern. Instruments that are cited but not captured are the first targets for a further collection round.

## S7. Related datasets and how this collection differs

| Resource | Scope | Relation to this collection |
|---|---|---|
| OECD.AI Policy Observatory | National AI policies and instruments (1,000+) | Broader on general AI; does not separate embodied systems or code content at the principle and mechanism level. |
| AlgorithmWatch AI Ethics Guidelines Global Inventory | Ethics guidelines (160+) | Guideline-only; several of its entries are in this collection's general-AI set. |
| Stanford AI Index legislation tracker; IAPP Global AI Law and Policy Tracker; Digital Policy Alert | Legislation and policy events | Event trackers rather than coded corpora; useful for extending the coverage audit. |
| RoboLaw guidelines (Palmerini et al. 2014); Nevejans (2016); Bertolini (2020) | Expert legal mapping of robotics regulation in Europe | Hand-coded analyses of the regimes this collection codes automatically; natural baselines for a validation study. |
| Reviews of AV regulation (Taeihagh and Lim 2019) and drone regulation (Stöcker et al. 2017) | Sector regulation | Document the sectoral binding layer that this collection captures only partly. |

## S8. Quality-assurance flags, corrections and duplicates

{{S06}}

Corrections applied after review are listed with their reasons and sources in `data/overrides_applied.csv`; duplicates removed by the documented merges and the second deduplication pass are in `data/duplicates_removed.csv`.

## S9. Coverage accounting (collection stage)

{{STAGE1}}

## S10. Extended tables

{{S08}}

{{S11}}

OpenAlex citation counts are reported as retrieved; several values are implausible for the stated venue and year and almost certainly reflect record merges on OpenAlex's side. They were not used in any analysis beyond the median citation statistic.

{{S12}}

{{S13}}

{{T24}}

{{T11}}

## S11. Datasheet

- **Motivation.** To describe quantitatively how embodied AI (robots, vehicles, drones, medical and industrial machines) is governed worldwide compared with AI in general, from a purposive multilingual document collection built by eight regional teams.
- **Composition.** 1,703 captured documents reduced to the canonical set reported in the analysis report after deduplication and exclusion of failed and off-topic captures; one row per document in `data/master_table.csv` with 180+ fields (collection metadata, text features, OpenAlex enrichment, 39 model-annotated fields, derived regions and years, lexicon features). The corpus over-represents Europe and English; Chinese-language documents are essentially absent; the robot-specific sprint drew mainly on academic literature and the general-AI database on official sources.
- **Collection process.** Regional teams listed sources in manifests and saved them as files (2,557 files); 266 listed sources could not be captured. Files were converted to text; oversized files were recovered through a document reader where possible.
- **Labelling.** All fields were assigned by a language model under a fixed codebook; governance documents were re-annotated in v2 from extended excerpts without collector metadata. No human coding beyond the collectors' own labels and the corrections documented after review.
- **Uses.** Comparative description of governance discourse and instruments; not a census of instruments and not a source of legal advice on any instrument's status.
- **Distribution and licence.** Code MIT; derived data CC BY 4.0; source texts not redistributed (publishers' copyright); source URLs and content hashes in `data/registry.csv`.
- **Maintenance.** Corrections are made through `data/manual_overrides.csv` with a reason and source per row; the pipeline regenerates every output.
- **Ethical considerations.** Documents are public policy, legal and research texts; no personal data were collected beyond author names as published. Texts were sent to a commercial model API for annotation; paywalled and permission-restricted captures were used only to derive labels and short summaries.

## S12. Figure index

| Figure | File | Content |
|---|---|---|
| 1 | F01_composition_by_set | Document classes by set |
| 2 | F02_timeline | Documents per year by set |
| 3 | F03_issuer_types | Issuer types by set |
| 4 | F04_lifecycle_binding | Lifecycle status and binding nature |
| 5 | F05_embodied_share_by_year | Embodied share per year (collection effect) |
| 6 | F06_cumulative_instruments | Cumulative embodied governance documents |
| 7 | F07_region_counts | Documents by region |
| 8 | F08_top_countries | Top 20 national jurisdictions |
| 10 | F10_language_by_region | Language by region |
| 11 | F11_categories | Robot types addressed |
| 12 to 14 | F12, F13, F14 | Robot types by region, class, period |
| 16, 17 | F16, F17 | Co-occurrence of robot types and of topics |
| 18 | F18_governance_gap | Research vs governance attention |
| 19 | F19_sectors | Sectors by set |
| 20 | F20_principles_by_set | Principles by set (pooled) |
| 21, 22 | F21, F22 | Principles by region and by class |
| 23 | F23_embodied_principles_by_type | Embodied-specific considerations by document type |
| 24 | F24_mechanisms_by_set | Mechanisms, instruments only and all documents |
| 25 | F25_mechanisms_by_region | Mechanisms by region |
| 26, 27 | F26, F27 | Framing by region; stance by class |
| 28 | F28_personhood_over_time | Personhood positions |
| 29, 30 | F29, F30 | Instruments cited by set and by region |
| 31 | F31_region_similarity | Regional distances |
| 33 | F33_term_trends | Term usage within the embodied set |
| 34 | F34_topic_change | Topic change with adjusted significance |
| 35 | F35_reliability | Inter-model and test-retest reliability |
| 36 | F36_lexicon_validation | Lexicon validation (repaired) |
| 37 | F37_coverage | Collection coverage |
| 38 | F38_adjusted_odds | Adjusted odds ratios, embodied vs general |
| 39 | F39_stratified_principles | Within-genre principle comparison |
| 40 | F40_gap_bootstrap | Gap index with bootstrap intervals |
| 41 | F41_coverage_audit | Coverage audit against reference instruments |
| 42 | F42_category_trends_within_embodied | Robot-type trends within the embodied set |
| 43 | F43_reliability_three_way | Full-text vs excerpt vs second model |
| 44 | F44_blind_reannotation | Metadata-blind re-annotation |

Each figure exists as `<name>.png` and `<name>.svg` (light) and `<name>_dark.png` and `<name>_dark.svg` (dark), with the plotted values in `figures/data/<name>.csv`.
