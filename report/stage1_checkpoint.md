# Stage 1 checkpoint: corpus, taxonomies, dashboard

Generated from 3295 canonical documents (3295 annotated). Annotation spend so far: $97.64.

## 1. Corpus construction

- Files downloaded from Drive: 2557 (plus 26 recovered through the Drive text reader).
- Unique documents after deduplication by content hash, URL, title and prose similarity: 3423.
- Documents listed in more than one regional folder: 78.
- Documents with usable text: 3333; bot-walled or empty captures kept as metadata-only rows: 90.

| Collection region | Sprint | Database |
|---|---|---|
| Africa | 37 | 60 |
| Asia | 200 | 153 |
| Europe | 467 | 241 |
| International | 0 | 0 |
| Latin America & Caribbean | 49 | 125 |
| Middle East | 45 | 75 |
| North America | 0 | 0 |
| North America (Canada, Greenland) | 18 | 24 |
| North America (USA) | 98 | 44 |
| Oceania | 30 | 37 |

### Coverage against the collectors' own manifests

| Region | Set | Rows in sheet | Captured by collectors | Not captured |
|---|---|---|---|---|
| 3. Latin America - Caribbean | sprint | 60 | 52 | 8 |
| 3. Latin America - Caribbean | database | 179 | 158 | 21 |
| 5. Middle East | sprint | 55 | 51 | 4 |
| 5. Middle East | database | 97 | 95 | 2 |
| 7. Oceania | sprint | 52 | 36 | 16 |
| 7. Oceania | database | 87 | 57 | 30 |
| 1. Africa | sprint | 52 | 50 | 2 |
| 1. Africa | database | 79 | 77 | 2 |
| 4. Asia | sprint | 250 | 228 | 22 |
| 4. Asia | database | 200 | 191 | 9 |
| 2a. North America - USA | sprint | 135 | 119 | 16 |
| 2a. North America - USA | database | 70 | 58 | 12 |
| 2b. North America - Canada, Greenland | sprint | 26 | 23 | 3 |
| 2b. North America - Canada, Greenland | database | 38 | 35 | 3 |
| 6. Europe | sprint | 518 | 409 | 109 |
| 6. Europe | database | 262 | 255 | 7 |

The collectors list 180 sprint sources they could not capture (bot walls, dead hosts); these are in `data/not_captured.csv`. A further 34 captured files exceeded the Drive download cap or were permission-denied; 27 were recovered as text, the rest are listed in `data/download_gaps.csv`.

## 2. Annotation results at a glance

| Document class | Documents | Share |
|---|---|---|
| governance_instrument_soft | 796 | 24.2% |
| governance_instrument_binding | 705 | 21.4% |
| research_output | 603 | 18.3% |
| communication_or_news | 592 | 18.0% |
| government_report_or_parliamentary | 261 | 7.9% |
| governance_proposal_or_draft | 220 | 6.7% |
| unusable | 62 | 1.9% |
| grey_literature | 56 | 1.7% |

| AI scope | Documents | Share |
|---|---|---|
| general_ai_only | 1026 | 31.1% |
| embodied_ai_specific_category | 997 | 30.3% |
| not_ai | 576 | 17.5% |
| embodied_ai_robotics_general | 388 | 11.8% |
| general_ai_with_embodied_provisions | 308 | 9.3% |

| Jurisdiction region (from jurisdiction, not folder) | Documents | Share |
|---|---|---|
| Europe | 1347 | 40.9% |
| Asia | 709 | 21.5% |
| International | 387 | 11.7% |
| North America | 369 | 11.2% |
| Latin America & Caribbean | 156 | 4.7% |
| Oceania | 130 | 3.9% |
| Middle East | 110 | 3.3% |
| Africa | 76 | 2.3% |
| Unknown | 11 | 0.3% |

| Language | Documents | Share |
|---|---|---|
| en | 2479 | 75.2% |
| zh | 280 | 8.5% |
| es | 118 | 3.6% |
| ja | 109 | 3.3% |
| pt | 44 | 1.3% |
| fr | 41 | 1.2% |
| ko | 38 | 1.2% |
| de | 26 | 0.8% |
| ru | 18 | 0.5% |
| ar | 17 | 0.5% |
| pl | 16 | 0.5% |
| id | 13 | 0.4% |

| Page quality | Documents | Share |
|---|---|---|
| substantive_document | 2256 | 68.5% |
| partial_or_excerpt | 555 | 16.8% |
| landing_or_index_page | 352 | 10.7% |
| error_or_blocked_page | 124 | 3.8% |
| non_text | 8 | 0.2% |

Year known for 3137 of 3295 annotated documents (annotation 3118, OpenAlex 3, PDF metadata 17). Median year 2024.

Governance instruments by status:

| Status | Documents |
|---|---|
| published_current | 754 |
| in_force | 603 |
| superseded_or_repealed | 118 |
| draft_or_bill_under_consideration | 90 |
| under_development | 51 |
| adopted_not_yet_in_force | 44 |
| consultation_open | 35 |
| proposal_or_concept | 30 |
| unknown | 5 |
| withdrawn_or_lapsed | 5 |

## 3. Reliability (main model vs independent second model, 10% sample)

Overlap documents: 160. Cohen's kappa (quadratic-weighted for ordinal fields; mean per-label kappa for multi-label fields).

| Field | Agreement | Kappa |
|---|---|---|
| issuer_type | 0.94 | 0.93 |
| date_basis | 0.87 | 0.64 |
| jurisdiction_country | 0.96 | 0.95 |
| jurisdiction_scope | 0.96 | 0.94 |
| doc_type | 0.84 | 0.82 |
| doc_class | 0.93 | 0.91 |
| is_governance_document | 0.97 | 0.91 |
| instrument_status | 0.94 | 0.84 |
| binding_nature | 0.95 | 0.85 |
| publication_stage | 0.93 | 0.88 |
| ai_scope | 0.91 | 0.86 |
| embodiment_status | 0.91 | 0.85 |
| primary_embodied_category | 0.91 | 0.84 |
| primary_topic | 0.83 | 0.81 |
| robot_legal_personhood_position | 0.99 | 0.93 |
| risk_framing | 0.81 | 0.77 |
| stance_toward_regulation | 0.73 | 0.61 |
| methodology | 0.93 | 0.87 |
| faith_or_religious_perspective | 1.00 | 1.00 |
| page_quality | 0.82 | 0.61 |
| language | 0.97 | 0.94 |
| pub_year (exact, both known) | 0.95 |  |
| pub_year (within 1 year) | 1.00 |  |
| pub_year (known in both) | 0.95 |  |
| relevance_to_embodied_ai_governance | 0.79 | 0.90 |
| embodied_categories | 0.88 | 0.79 |
| application_sectors | 0.85 | 0.79 |
| governance_topics | 0.71 | 0.76 |
| governance_mechanisms | 0.63 | 0.75 |
| principle:transparency | 0.84 | 0.87 |
| principle:justice_fairness | 0.86 | 0.87 |
| principle:non_maleficence | 0.79 | 0.71 |
| principle:responsibility_accountability | 0.84 | 0.86 |
| principle:privacy | 0.88 | 0.89 |
| principle:beneficence | 0.86 | 0.79 |
| principle:freedom_autonomy | 0.86 | 0.77 |
| principle:trust | 0.89 | 0.85 |
| principle:sustainability | 0.93 | 0.90 |
| principle:dignity | 0.89 | 0.81 |
| principle:solidarity | 0.92 | 0.84 |
| principle:human_oversight | 0.86 | 0.81 |
| principle:robustness_security | 0.87 | 0.84 |
| principle:inclusive_growth | 0.82 | 0.84 |
| principle:physical_safety | 0.92 | 0.89 |
| principle:human_robot_proximity | 0.91 | 0.90 |
| principle:liability_for_physical_damage | 0.97 | 0.97 |
| principle:autonomy_level_control | 0.93 | 0.85 |
| principle:conformity_assessment_certification | 0.96 | 0.87 |
| principle:dual_use_military | 0.97 | 0.86 |

### Cross-check against the collectors' labels

| Check | n | Agreement | Kappa |
|---|---|---|---|
| Europe collector 'Robot focus' (Robotics/Humanoid/Embodied vs General AI) vs annotated ai_scope (embodied incl. provisions vs general) | 684 | 0.82 | 0.61 |
| Europe collector 'Robot focus' vs annotated embodiment_status (physical/mixed vs none/software) | 684 | 0.82 | 0.63 |
| Europe collector 'Type' vs annotated issuer_type (4 collapsed classes) | 646 | 0.97 | 0.95 |
| Collector 2-letter country vs annotated jurisdiction_country (research papers, first-author country) | 1594 | 0.98 |  |
| Collector set (sprint=robotics vs database=general AI) vs annotated relevance>=2 | 3295 | 0.63 | 0.22 |
| Collector tier Core vs annotated is_governance_document | 1250 | 0.78 | 0.32 |

## 4. Quality flags for review

398 documents carry at least one flag (`data/qa_flags.csv`). Counts by flag:

- sprint_doc_rated_irrelevant: 124
- language_disagreement: 123
- annotation_year_vs_openalex>1: 86
- low_confidence_with_text: 54
- year<1990: 36
- jurisdiction_unknown: 11
- governance_doc_in_news_or_research_class: 2

## 5. Deliverables in this stage

- `data/master_table.csv` and `data/master_table.xlsx` (sheet `documents` plus `data_dictionary`): one row per document, 160+ columns.
- `dashboard/index.html`: interactive dashboard (filters, four charts with table views, document table with detail drawer).
- `codebook/codebook.md`, `codebook/schema.json`, `codebook/lexicons.json`: the annotation scheme.
- `codebook/taxonomies.md`: the three taxonomies with definitions, counts and example documents.
- `data/registry.csv`, `data/files.csv`: document registry and file-to-document mapping.
- `data/reliability_fields.csv`, `data/reliability_team_crosscheck.csv`: reliability results.
- `data/collector_coverage.csv`, `data/not_captured.csv`, `data/download_gaps.csv`: coverage accounting.
- `annotations/main/*.json`: raw per-document annotations with model, prompt hash and cost.