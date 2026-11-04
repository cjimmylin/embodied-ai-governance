# Version 4 summary: what the adversarial review of v3 changed

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Date: 31 October 2026. Project: global governance of embodied and physical AI (CEI AI Robotics collection, two collection rounds).

Dashboard (v4): https://claude.ai/artifact/YKsXJRaT7tSfRXseuo5kuZ
Package: embodied-ai-governance-v4.zip (data, tables, figures, scripts, reports, review log, methods documents, round-2 workspace).

## 1. What was done

Six adversarial reviews of version 3 were run in parallel (data scientist, AI-annotation researcher, ICLR-style reviewer, technology journalist, robotics-governance expert, visualisation and dashboard specialist). Their findings were triaged into rules, document-level corrections, definition changes, new measurements and rewritten claims, then every analysis, figure, the dashboard and all narrative documents were regenerated. Two methods documents describe the cycle: an agent runbook (collection_round2/V4_REVIEW_RUNBOOK.md) and a human-readable methods section (report/methods_review_and_revision.pdf). The finding-by-finding log is review/adversarial_review_v3_and_changes_v4.md.

## 2. The four structural problems the reviews converged on

1. Counting unit. v3 counted every legal text as one instrument, so commencement orders, levy acts, exemptions, EEA incorporation decisions, corrigenda, definitions sections, register pages and stubs stood beside the acts they belong to.
2. Collection round as a confound. Embodied-versus-general comparisons pooled web-collected round-1 documents with database-harvested round-2 legal texts without adjusting for the round. The v3 "ethical core deficit" (11 of 14 core principles lower in robot instruments) does not exist within round 1.
3. Excerpt cleaner. A v2 rule for stripping navigation lines deleted most of the text of Chinese, Japanese and Korean documents before annotation.
4. Capture tier. Depth-of-treatment statistics included catalogue pages and stubs.

## 3. What changed in the data and analysis

- Counting unit: each legal text is assigned to principal, amendment, ancillary, incorporation, language copy, catalogue page, stub, duplicate text or dependent act. Headlines use principal instruments (principal plus amendment). Instrument families group renewals and versions.
- AI-content tiers from full text: autonomy or automation provisions; AI named explicitly.
- Status and class rules: standards drafts as unpublished; mandatory Chinese GB standards as binding; treaty-process working papers as position documents; proposals with an adopted act present as superseded.
- 157 audited field-level overrides on 91 documents from the governance expert's 165-row classification audit (the mechanical code-to-value conversion was itself checked against the expert's fix text and corrected in eleven places).
- 422 Chinese, Japanese and Korean documents re-annotated with a character-aware cleaner: 57 changed embodied-set membership; documents rated "not about AI" fell from 205 to 160.
- Round-2 reliability measured for the first time: 160 documents, median kappa 0.86 (second model) and 0.91 (same-model re-run).
- Precision audit: 100 random v3 binding embodied instruments read individually; 54% (44 to 63) are distinct, binding and substantive on an embodied system, implying about 161 (132 to 190) of the v3 count of 299.
- Analyses: collection round as covariate; within-round and within-genre contrasts; sparse-cell flags; one instrument denominator; strict coverage criterion alongside the loose one; rule-versus-audit comparison.
- Figures and dashboard: computed titles, four false titles replaced, regional-similarity figure rebuilt, dashboard tiles and methods panel generated from data, round-2 view, robot-type and instrument-kind filters, not-AI documents hidden by default.

## 4. Before and after

| Quantity | v3 | v4 |
|---|---|---|
| Annotated / usable documents | 3,291 / 3,148 | 3,295 / 3,165 |
| Embodied-AI set / general-AI set | 1,589 / 982 | 1,603 / 1,015 |
| Embodied instruments, all legal texts (comparable unit) | 808 | 810 |
| Embodied instruments, principal unit | not defined | 505 (408 robot-relevant) |
| Binding embodied, all legal texts | 299 | 291 |
| Binding embodied, principal unit | not defined | 195 (168 robot-relevant; 140 with autonomy or AI provisions; 15 naming AI) |
| Audited precision of the v3 binding set | not measured | 54%, about 161 genuine of 299 |
| Core principles lower in robot instruments (Holm) | 11 of 14, pooled | 0 of 14 within round-1 instruments; 10 of 14 within round-2 instruments; reported as a composition effect |
| Regional divergence on values | claimed on all embodied documents | within research outputs 2 of 14 core principles differ; within principal instruments 12 of 14, tracking instrument-type mix |
| Round-2 label reliability | not measured | median kappa 0.86 and 0.91 |
| Documents rated not about AI among CJK texts | 205 | 160 |
| Reference-list coverage (39 instruments) | 31 loose | 22 strict, 31 loose |
| Dashboard methods panel | described v1 | generated from the v4 data |

## 5. What survives every stratification

- The research-versus-governance gap for companion, humanoid and care robots (large research share, few instruments, no or almost no binding ones).
- The dominance of drone, vehicle and machinery law among binding instruments reaching embodied AI, and the near absence of binding instruments that name AI explicitly (15 of 195).
- The physical-safety, proximity, liability and autonomy-level principles as the distinctive content of embodied-AI documents in both rounds.

## 6. Limits that remain

All reviewers, collectors and annotators are language models; no human has labelled a document. The precision audit used one reader. The round-1 instrument stratum is small (61 embodied against 245 general), so the absence of a within-round-1 core-principle difference is partly a power statement. 189 instruments verified by collectors but unreadable from the execution environment (Korea, mainland China NPC, Hong Kong, France, US defence, India, California) remain outside every count. Consolidated statutes carry the year the annotation found.

## 7. Deliverables

- report/brief.pdf, report/paper.pdf, report/analysis_report.pdf, report/supplement.pdf, report/collection_round2.pdf, report/methods_document_discovery.pdf, report/methods_review_and_revision.pdf
- review/adversarial_review_v3_and_changes_v4.md, review/v4_numbers_audit.md and review/v3_reviews/ (six reviews, screenshots, audit tables)
- collection_round2/V4_REVIEW_RUNBOOK.md and collection_round2/ROUND2_RUNBOOK.md
- dashboard/artifact.html (published at the URL above)
- data/, tables/, figures/, scripts/ (run_v4.sh reproduces the pipeline)
