# Stage 2 analysis plan (for review at the Stage 1 checkpoint)

Unit of analysis: the canonical document (deduplicated). Primary corpus: documents with `relevance_to_embodied_ai_governance >= 2` or any `embodied_categories` label ("embodied set"); comparison corpus: the general-AI documents. Analyses are run over all annotated documents unless stated, and each figure carries its n. Where percentages are compared across groups, 95% Wilson intervals and chi-square or Fisher tests are reported; where trends over time are claimed, a Cochran-Armitage trend test or logistic regression on year is reported; where counts per group are modelled, negative-binomial regression. Multiple comparisons within a family are Holm-corrected. All code is in `scripts/12_analysis.py`; every figure has a CSV twin in `figures/data/`.

## A. The document landscape (what exists)
1. Corpus composition by document class, type and issuer type; embodied vs general-AI comparison (stacked bars, mosaic).
2. Instrument lifecycle: for governance documents, status by binding nature and by region (proposal, draft, adopted, in force). Share of embodied-AI governance that is binding vs soft vs standards, compared with general AI.
3. Timeline: documents per year by class, 2010 onward; embodied share per year; cumulative count of binding embodied instruments; first-appearance years per embodied category (when each category entered governance texts).
4. Geography: documents per jurisdiction and per study region; per-capita and per-document normalisation; map-style ranking; the "International" layer (ISO, IEEE, UNESCO, OECD, ILO) and its citation into national documents.
5. Language and venue: language mix by region; research outputs by venue type and OpenAlex citation counts; share of peer-reviewed vs grey.

## B. What is governed (the taxonomy in use)
6. Embodied-category prevalence overall and by region, by document class, by year (heatmaps; category x region normalised within region).
7. Co-occurrence network of embodied categories and of governance topics (edge weight = documents mentioning both; community detection).
8. Which categories receive binding instruments vs only research attention: a "governance gap" index per category = (share of research documents) minus (share of governance instruments). Categories with high research attention and few instruments are flagged.
9. Sector coverage and the medical/industrial/consumer split; the special status of autonomous vehicles and drones (often governed outside "AI" law).

## C. How it is governed (principles and mechanisms)
10. Principle salience profiles: share of documents with each principle at level 1 and 2; embodied vs general; by region (radar/heat); by document class (do laws, standards and papers emphasise different principles?). Statistical tests per principle with Holm correction.
11. Embodied-specific principles (physical safety, proximity, liability for physical damage, autonomy level, certification, dual use): which regions and instrument types operationalise them (level 2) rather than mention them.
12. Governance mechanisms by region and by class: risk-based tiering, conformity assessment, liability regimes, human-oversight requirements, bans. Mechanism bundles via clustering of documents on their mechanism vectors.
13. Risk framing and regulatory stance: distribution by region and class; association between stance and document type (papers calling for new regulation vs instruments).
14. Legal-personhood debate: positions over time and by region.
15. Reference network: which named instruments are cited where (EU AI Act, ISO 13482/10218, UNESCO Recommendation, OECD Principles, Asimov's Laws); regional dependence on EU and ISO instruments; standards citation as a proxy for harmonisation.

## D. Regional comparison
16. Region profiles: for each study region, a one-page profile (counts, class mix, top categories, top principles, top mechanisms, binding share, median year) and a cross-region distance matrix (cosine on principle/topic vectors) with hierarchical clustering: which regions govern embodied AI alike.
17. Divergence tests: principle and mechanism shares by region with effect sizes (Cramer's V) and pairwise comparisons.

## E. Trends and recency
18. Newest documents (2024 to 2026): what themes rise (humanoids, embodied foundation models, agentic systems, physical AI terminology); term-frequency trends from the lexicon features (per 1,000 words by year).
19. Trend models: logistic regression of embodied-specific principle presence on year, region and class.

## F. Robustness and validation
20. Reliability: inter-model kappa per field (Sonnet vs Opus) and same-model test-retest; results re-run on the reliability subsample to show conclusions hold under the alternate annotator.
21. Lexicon validation: agreement between lexicon-based presence (full text) and annotated presence (excerpt) per principle and category; sensitivity of headline results to using lexicon features instead.
22. Collector-bias checks: results split by sprint vs database set, by collector tier, by text availability; sensitivity to excluding bot-walled captures and documents with confidence < 0.5.
23. Coverage limits: documents not captured, oversized, duplicated across regions; English-language and Europe over-representation; implications stated in the limitations section.

## Deliverables
- `report/analysis_report.md` (+ PDF): full narrative with every figure and table, numbered.
- `figures/*.png|svg` (light and dark) and `figures/data/*.csv`.
- `report/paper.md` (+ PDF): paper-style write-up (abstract, introduction, related work, data, methods, results, discussion, limitations, appendix) with no venue formatting constraints.
- `report/supplement.md`: supplementary tables and figures, codebook, reliability detail, coverage.
