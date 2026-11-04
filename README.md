# Global governance of embodied AI and robotics: corpus, annotations and analysis (v5)

**Start here: the project hub** at [`docs/index.html`](https://cjimmylin.github.io/embodied-ai-governance/docs/index.html) (served by GitHub Pages; the same page as [docs/index.html](docs/index.html) in this repository) links every deliverable: the document explorer, the talks and videos, the papers and reports, the reviews and audits, the data and what still needs a person.

This folder is the fourth version of a quantitative study of how robots, autonomous vehicles, drones and other embodied AI are governed worldwide. Version 1 was built from the CEI *AI Robotics (Filtered Sources)* collection; version 2 corrected it after six adversarial reviews; version 3 added a second collection round that searched official legal databases, treaty-body archives, standards catalogues and regulator sites for the governance instruments the first collection had missed; version 4 answers a second set of six adversarial reviews of v3 (`review/v3_reviews/`, mapped to decisions in `review/adversarial_review_v3_and_changes_v4.md`): a documented counting unit (principal instruments) with text-based AI-content tiers, collection round as a covariate with within-round results, a character-aware excerpt cleaner and re-annotation of every Chinese, Japanese and Korean document, status and class rules plus 157 audited corrections, a round-2 reliability sample, an independent precision audit, and a rebuilt dashboard. `report/collection_round2.md` describes that round (sources, fetch outcomes, before/after counts, agreement between collector metadata and blind annotation, the new instruments), and `collection_round2/` holds its candidate lists, scripts and inventory.

Version 5 (2 November 2026) adds collection round 3, executed by agents alone: the round-2 candidates whose text could not be read were re-fetched by official alternative routes with an honestly identified research crawler (no browser impersonation, no bot-check circumvention; hosts that refuse the crawler are listed for manual download); legal databases were harvested with service-robot, care, exoskeleton, humanoid and collaborative-robot terms and EuroVoc concepts; the 104 principal instruments whose text exceeded the excerpt were re-read in full and their labels replaced; a supplementary schema (whom the rule binds, entry-into-force, application and repeal dates, legal effect of standards, the year the robot provision arrived) was run on all 505 principal embodied instruments; a second independent precision audit re-read 100 of the 195 principal binding instruments; the governance-gap index is reported by collection source; a 200-document human-validation kit was prepared; and the dashboard shows the new fields. `report/collection_round3.md` is the companion report and `HUMAN_ASSISTANCE.md` lists what still needs a person. The narrative documents (brief, analysis report, paper, supplement) carry a v5 note: their tables and figures were regenerated, their sentences still state the v4 counts.

## Deliverables

| What | Where |
|---|---|
| Two non-technical talks with narrated videos: a conference keynote (21 min) and a main-stage talk in the TED format (11 min), with scripts and editable decks | `report/talks/` (decks: https://claude.ai/artifact/FaM6krx6snfSm69VKW4d98 and https://claude.ai/artifact/MMcpN4zupd3k9EifNgSksq) |
| Collection round 3 report (recovered instruments, harvest, full-text re-reads, supplementary fields, second audit, source split) | `report/collection_round3.md`, `.pdf`, `.html` |
| What needs a person (blocked hosts, missing instruments, paid standards, validation kit, legal checks, boundary decisions) | `HUMAN_ASSISTANCE.md` |
| Second precision audit (random n=100 of the v4 binding set, seed 2027) | `review/v5_audit/precision_audit_v5.md`, `precision_audit_v5_results.csv` |
| Human-validation kit (200 stratified documents, coding sheet, instructions, sealed answer key) | `data/human_validation/` |
| Round-3 inventory and collector reports | `data/round3_inventory.csv`, `collection_round3/` |
| Supplementary fields and full-text comparison | columns `bound_parties`, `entry_into_force_date`, `applicability_date`, `repeal_or_expiry_date`, `legal_effect_of_standard`, `robot_provision_year`, `robot_provision_basis` in `data/master_table.csv`; `tables/T70` to `T75`, `T80`, `T81`, `T07b` |
| Review log and changelog v3 to v4 (six reviews, precision audit, decisions) | `review/adversarial_review_v3_and_changes_v4.md`, `review/v3_reviews/` |
| Methods: the review-and-revision cycle (paper-style) | `report/methods_review_and_revision.md`, `.pdf`, `.html` |
| Runbook for agents: how the v3 review and v4 revision were run | `collection_round2/V4_REVIEW_RUNBOOK.md` |
| Collection round 2 report (what was added and how) | `report/collection_round2.md`, `.pdf`, `.html` |
| Methods: document discovery and inclusion in v3 (paper-style) | `report/methods_document_discovery.md`, `.pdf`, `.html` |
| Round-2 runbook for agents (sources, endpoints, scripts, failure modes, how to run a round 3) | `collection_round2/ROUND2_RUNBOOK.md` |
| Plain-language brief (1 page) | `report/brief.md`, `report/brief.pdf` |
| Analysis report (all figures and tables) | `report/analysis_report.md`, `.pdf`, `.html` |
| Paper (venue-agnostic) | `report/paper.md`, `.pdf` |
| Supplement (codebook, taxonomies, reliability, instrument lists, data dictionary, datasheet) | `report/supplement.md`, `.pdf` |
| Review log and changelog v1 to v2 | `review/adversarial_review_and_changes.md` |
| Change logs v2 to v3 and v3 to v4 for each narrative document, and numbers audits | `review/v3_changes_*.md`, `review/v4_changes_*.md`, `review/v*_numbers_audit*.md` |
| Interactive dashboard | `dashboard/index.html` (standalone), `dashboard/artifact.html` (fragment for claude.ai); public copy at https://claude.ai/artifact/YKsXJRaT7tSfRXseuo5kuZ |
| Master table (one row per document) | `data/master_table.csv`, `data/master_table.xlsx`, `data/data_dictionary.csv` |
| Round-2 inventory (every candidate, fetch outcome, whether content-analysed) | `data/round2_inventory.csv` |
| Figures (light and dark, PNG and SVG) and their data | `figures/`, `figures/data/` (F50 to F52 are the round-2 figures) |
| Tables | `tables/` (CSV and Markdown; T50 to T60 are the round-2 tables) |
| Per-document model annotations with model, prompt hash, policy and cost | `annotations/` (`main`, `main_clean`, `gov_extended`, `round2`, `round3`, `fulltext_v5`, `supplement_v5`, `reliability_*`) and, in the package archive only (not in the public GitHub repository, because they are excerpts of the source documents), the exact model inputs in `annotations/*/_inputs/` |
| Manual corrections and de-duplication | `data/manual_overrides.csv`, `data/manual_overrides_v4.csv`, `data/overrides_applied.csv`, `data/duplicates_removed.csv` |
| Counting-unit, family and AI-content flags per document; run manifest | columns `instrument_unit`, `principal_instrument`, `family_key`, `family_size`, `ai_explicit`, `autonomy_terms` in `data/master_table.csv`; `data/run_manifest.json` |
| Round-2 reliability (second model and re-run on 160 round-2 documents) and reliability variants | `data/reliability_fields_r2opus.csv`, `data/reliability_fields_r2rerun.csv`, `data/reliability_variants.csv`, `tables/S09b_reliability_variants.md` |
| Precision audit of the v3 binding set (random n=100) | `review/v3_reviews/precision_audit.md`, `precision_audit_sample.csv`, `tables/T62_precision_audit_vs_rules.md` |
| Reference list for the coverage audit | `data/reference_instruments.csv` |
| Round-2 candidate schema, candidate lists, harvest/fetch/registry scripts and collector reports | `collection_round2/` |

## Reproducing

Scripts run in numerical order from `scripts/` (Python 3.13; `requirements.txt`). Steps 01 to 05 need the converted source texts (not redistributed; see Licensing); steps 07 onward run from the stored annotations. `scripts/run_v4.sh` runs the whole v4 chain (assembly, overrides, `07c_v4_units_and_tiers.py`, reliability incl. round 2 and variants, analyses, figures, round-2 report, precision comparison, manifest, dashboard); `scripts/run_v4_post.sh` re-runs from the unit step and `scripts/run_v4_analyses.sh` from the analyses.

```bash
python3 scripts/merge_round2.py          # append round-2 registry rows, text features and annotations; write data/round2_inventory.csv
python3 scripts/05_lexicons.py           # full-text lexicon features (cached for unchanged documents)
python3 scripts/07_assemble.py           # master_table_raw.csv from annotations + enrichment
python3 scripts/07b_apply_overrides.py   # documented corrections, second (identical-title) and third (cross-round) de-duplication passes
python3 scripts/07c_v4_units_and_tiers.py   # v4: counting unit, instrument families, AI-content tiers, status/class rules, text-hash duplicates, audited overrides
python3 scripts/09_reliability.py annotations/reliability_opus   # and the other reliability folders
python3 scripts/09b_reliability_round2.py annotations/reliability_round2_opus _r2opus; python3 scripts/09c_reliability_variants.py
python3 scripts/13_analysis_A.py; python3 scripts/14_analysis_B.py; python3 scripts/15_analysis_C.py
python3 scripts/18_analysis_D.py; python3 scripts/19_fulltext_validation.py; python3 scripts/17_supp_tables.py
python3 scripts/20_figures_v2.py; python3 scripts/21_round2_report.py; python3 scripts/24_precision_vs_rules.py; python3 scripts/23_run_manifest.py; python3 scripts/10_dashboard.py; python3 scripts/16_build_reports.py
```

The v5 chain is `scripts/run_v5.sh`: `collection_round3/scripts/merge_round3.py` (append the round-3 registry rows, text features and annotations; write `data/round3_inventory.csv`), assembly and overrides as above, then `run_v5_post.sh` (unit step, `07d_supplement_v5.py` merging the supplementary fields and writing T70 to T73, `27_fulltext_compare.py` writing T74 and T75, reliability, analyses, figures, round-2 report, precision comparison, `25_round3_report.py` writing the round-3 companion, `28_human_assistance.py` writing `HUMAN_ASSISTANCE.md`, manifest, dashboard) and `16_build_reports.py`. The round-3 annotation passes were `26_supplement_v5.py` (supplementary schema, `codebook/supplement_v5_schema.json` and `supplement_v5_prompt.md`, `--head 40000 --mid 2000 --tail 6000 --blind`), `04_annotate.py --head 400000` for the full-text re-reads (`annotations/fulltext_v5`), and `collection_round3/scripts/04_annotate_r3.py` with the round-2 settings for the round-3 documents (`annotations/round3`).

Round-2 discovery and acquisition live in `collection_round2/scripts/`: `harvest_apis.py` (EUR-Lex CELLAR SPARQL by title and by EuroVoc concept, legislation.gov.uk, Japan e-Gov, gov.cn policy library, Federal Register of Legislation, eCFR, Brazil Camara), `merge_candidates.py` (schema validation, relevance filter for title-searched sources, de-duplication within the round and against round 1, stable ids), `fetch_texts.py` (primary/secondary URLs, CELLAR and UN document API routing, ISO committee mirror, PDF/HTML/XML conversion), `build_registry.py`, `04_annotate_r2.py` and `incremental.sh`. Collector-agent briefs produced `collection_round2/candidates/*.csv`; their condensed reports, including what they looked for and could not find, are in `collection_round2/COLLECTOR_REPORTS.md`.

Annotation (`04_annotate.py`, `04_annotate_r2.py`) used the Claude Code command-line interface in non-interactive mode with a fixed system prompt and JSON schema. All governance-document annotations in v2 and every round-2 annotation were produced with `--blind --policy v2 --head 100000 --mid 6000 --tail 4000` (collector cover block stripped, minimal metadata, up to 110,000 characters of text); every Chinese, Japanese and Korean document was re-annotated in v4 with a character-aware cleaner (policy tag `cjk_clean=v4`, folders `annotations/round2` and `annotations/cjk_fix`). Model identifiers, prompt hash, excerpt policy and cost are stored in every annotation file.

## Licensing and provenance

- Code: MIT (see `LICENSE`).
- Derived data (annotations, master table, figures, tables, inventory): CC BY 4.0. Annotations were produced by a language model and have not been verified by human coders except through the checks described in the supplement and the collector-metadata agreement check in the round-2 report.
- Source documents: not redistributed. Round-1 documents are public documents collected by the CEI regional teams from the URLs recorded in `data/registry.csv` (`source_url`); round-2 documents were fetched from the official URLs recorded in `data/round2_inventory.csv` (`url_primary`, `fetch_url`). Copyright remains with their publishers. Technical standards were annotated on their public scope or abstract pages only.
- Model summaries (`summary_en`, `key_provisions_or_claims`) are short derived descriptions, not reproductions of the texts.
