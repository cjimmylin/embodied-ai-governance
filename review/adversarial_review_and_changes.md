# Adversarial review of v1 and the changes made in v2

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Six independent reviews of the version-1 deliverables were commissioned, each from a fresh reviewer with no stake in the conclusions: a data scientist and statistician, an AI researcher specialising in LLM annotation validity, a conference reviewer (ICLR/NeurIPS style), a technology and policy journalist, an AI-governance and technology-law expert, and a data-visualisation and front-end QA engineer. The six full reviews are in this folder. This document consolidates their findings, states the decision taken on each, and records what changed between v1 and v2. Severity is the reviewers' own; where reviewers disagreed, the stricter reading was kept.

## 1. Summary verdicts

| Reviewer | Verdict on v1 | Scores or headline |
|---|---|---|
| Data scientist | Arithmetic reproduces exactly; several headline inferences do not survive scrutiny; major revision | 4 critical, 10 major, 12 minor findings |
| AI researcher | Major revision: no human validation, label leakage into the prompt, reliability reported on the wrong annotations, excerpt truncation, lexicon bugs | 25 findings |
| ICLR reviewer | Reject in current form (Soundness 2, Presentation 2, Contribution 2, Overall 3/10, confidence 4) | 10 prioritised changes |
| Journalist | Strong story buried under 113 numbers in 33 sentences; headline counts disagree across the package; dashboard first screen destroys trust | 5 critical, 15 major, 7 minor |
| Governance expert | Discourse-level findings defensible; instrument-level headline claims do not survive a coverage audit; major revision before policy use | 27 findings, 41 document corrections, ~75 missing instruments |
| Visualisation QA | Figures numerically honest (8/8 cross-checks); four label collisions; all dark heatmaps mis-encoded; dashboard lacks HTML basics and mobile layout | 34-figure table, 11 dashboard findings |

## 2. Findings and decisions

Status codes: **Fixed** (implemented in v2), **Partly** (implemented with a stated limit), **Reframed** (claim withdrawn or rewritten rather than data changed), **Not done** (with reason).

### 2.1 Data and corpus

| # | Finding (reviewers) | Decision | v2 change |
|---|---|---|---|
| D1 | The EU AI Act was counted twice (three times with the catalogue record) and the 2021 proposal twice; the Civil Law Rules twice; an Israeli draft twice; 29 further exact-title duplicate groups among usable documents (DS, ICLR, GOV, JOUR) | Fixed | Documented merges in `data/manual_overrides.csv` (duplicate_of rows, fuller capture kept) plus a second deduplication pass on normalised title + jurisdiction (years within one). 46 documents removed, listed in `data/duplicates_removed.csv`. |
| D2 | Executive Order 14110 coded as current although revoked on 20 January 2025 and its successor is in the corpus (ICLR, GOV, AI) | Fixed | Status set to superseded_or_repealed; EO 13859 corrected to in force; AI Act negotiating texts and 2021 proposal marked superseded (enacted). |
| D3 | Taiwan "Industrial Robot Hazard Prevention Standards (2025)" is a 204-word login stub at confidence 0.40, dated from PDF metadata; the instrument dates from 1987 (last amended 2018) (ICLR, GOV, DS) | Fixed | Excluded from content analyses as a failed capture; year corrected to 2018; listed in the coverage audit as an instrument that exists but could not be read. Same treatment for the Taiwan AI Basic Act stub. |
| D4 | Seven of twelve "technical standards" are ISO catalogue, committee or store pages; three further AI Act article pages and a catalogue record counted as instruments (ICLR, AI, GOV, DS) | Fixed | Catalogue, committee and store pages reclassified as web pages (not instruments). Remaining standard captures are labelled by capture tier; content-level claims use substantive or partial captures only; landing pages count in the instrument inventory but not in operationalisation statistics. |
| D5 | A Shakespeare poem (1594), a 1947 Japanese antitrust act and a document dated 2027 were in the usable set and drove the dashboard's "Year span 1594 to 2027" (JOUR, VIZ, DS) | Fixed | Off-topic captures excluded; the 2027 forthcoming date capped at 2026; the dashboard shows the usable range. |
| D6 | Bills coded "legally binding"; soft law coded "in force"; drafts enacted since capture still coded as drafts (GOV, DS) | Fixed | Rule: bills, proposals and consultations cannot be binding instruments (prospective binding nature recorded separately); 41 further field corrections from the governance expert's table applied with sources. |
| D7 | "Primary category" not always among the categories (F11 impossibility) (VIZ) | Fixed | Enforced in the override step. |
| D8 | Project deliverable (MARIO D1.2), a CPSC staff report and a funding-call appendix coded as governance instruments; a standards-body white paper not (GOV) | Fixed | Reclassified as specified. |
| D9 | The African Commission resolution assigned to "International" while EU bodies are "Europe" (GOV) | Fixed | Assigned to Africa. |
| D10 | Two North America regions | Fixed (user request) | Merged into one "North America" region throughout. |
| D11 | Known binding instruments absent from the collection (UK Automated Vehicles Act, German autonomous-driving law, Japan Level-4 regime, Korea's Intelligent Robots Act, EU Machinery Regulation, Product Liability Directive, drone rules, UN R157, ISO 10218:2025 and others) (GOV, ICLR, JOUR) | Partly | The collection cannot be extended within this study. A reference list of 38 instruments and standards was compiled and a coverage audit added (T25, F41): each is marked captured or not and the number of corpus documents citing it is reported. Every instrument-level claim is now stated as "within this collection" and the absences are listed in the limitations. |

### 2.2 Annotation validity

| # | Finding | Decision | v2 change |
|---|---|---|---|
| A1 | No human-coded ground truth; the second annotator is a same-vendor model (all reviewers) | Not done, reframed | Human double-coding is outside what this study can deliver; v2 says so in the first paragraph of every document and calls the labels "consistent, not certified". The protocol for a human validation sample is specified in the supplement for a follow-up. |
| A2 | Reliability was computed on pre-cleaning annotations, not the ones analysed; 54 of 160 reliability documents were later re-annotated (ICLR, AI) | Fixed | Reliability recomputed against the final v1 annotations (main overlaid by main_clean). The main-vs-cleaned perturbation on 499 documents is reported as an input-perturbation reliability. |
| A3 | Label leakage: the prompt passed the collectors' folder, title, language and text status, and 483 texts carry a cover block with the collectors' issuer, country, type and tier labels (AI) | Fixed | A metadata-blind, cover-stripped annotation mode was added. All governance documents were re-annotated in this mode (A4) and the 160-document sample was re-annotated blind; the per-field effect is reported (F44, T26). |
| A4 | Instruments annotated from a 14,000-character excerpt (median 38% of governance texts seen; AI Act 2.3%), which cannot support operationalisation or mechanism claims (ICLR, AI, DS) | Fixed | All governance documents re-annotated from up to 110,000 characters (first 100,000, a 6,000 middle slice and 4,000 tail), blind and cover-stripped; these annotations replace the v1 ones for governance documents in every analysis. The effect on labels is reported (T35) and the remaining truncation stated. |
| A5 | Excerpt-vs-full-text sensitivity never measured (ICLR, AI) | Fixed | The 160-document sample was re-annotated from the full text; kappa per field and label-count inflation reported (F43, T27). |
| A6 | Cleaning rule deleted dates, titles and headings (AI) | Fixed | v2 cleaning keeps short lines with digits, all-caps headings and sentence-ending lines; excerpt policy is recorded in every annotation and in the prompt hash scope. |
| A7 | Lexicon bugs: case-insensitive `\bLAWS\b` matched "laws"; `\bharm` matched "harmonised"; unbounded `arma`, `militar`, `defen[cs]e`; NIST pattern; the EU AI Act pattern absorbed the Colorado AI Act (ICLR, AI, DS) | Fixed | Patterns repaired; lexicon features and validation recomputed; the report's earlier interpretation of the military-lexicon disagreement withdrawn. |
| A8 | The Spearman 0.93 in the abstract is the correlation of embodied-minus-general differences, not of principle rankings (ICLR, AI, DS) | Fixed | Text states exactly what is computed; the rank correlation of shares (0.84) is reported alongside. |
| A9 | Kappa mixes quadratic-weighted and per-label statistics; level-2 reliability is lower; "none"/"other" labels in the multi-label mean; confidence is uncalibrated (AI, DS) | Partly | Unweighted and level-2 kappas added to the reliability table; the headline reliability sentence now gives both; the confidence field is described as a page-quality proxy and the confidence subset dropped from the sensitivity table. |
| A10 | Conformity assessment and dual use are not "principles"; relevance scale conflates embodiment and governance (AI) | Reframed | The six embodied-specific items are called "embodied-specific considerations" throughout; the relevance field is described as what it is. |
| A11 | Set definition misdescribed (120, not 6, documents enter by category label alone); circularity of model-defined sets (DS, AI) | Fixed, reframed | Correct description; a strict-definition sensitivity (relevance 2-3 only) added (T32). |

### 2.3 Statistics and inference

| # | Finding | Decision | v2 change |
|---|---|---|---|
| S1 | The embodied-vs-general comparison is confounded by genre and mirrors the sprint/database collection design; several core-principle differences reverse within genre (accountability is a Simpson's paradox) (all) | Fixed, reframed | Genre-stratified comparisons (T21, F39), covariate-adjusted odds ratios (T20, F38) and Mantel-Haenszel tests (T34) added; the narrative leads with instrument-only and within-genre results and names the design confound in the summary. |
| S2 | Cramér's V compared across tables of different dimension and population; chi-square on sparse tables; "core principles do not differ" selective (ICLR, DS) | Fixed | Bias-corrected V with bootstrap CIs on a common population (T29); Monte-Carlo chi-square for sparse tables; Fisher rule now uses expected counts as described. |
| S3 | Topic change 2025-26 unadjusted for the genre and region shift; adjusted models disagree (ICLR, DS, AI) | Fixed | Adjusted topic-change models (T28); F34 marks crude and adjusted significance separately; the "turn" is described as what survives adjustment (human oversight). |
| S4 | Trend models with low events per variable and sensitivity to the partial year 2026 (DS, ICLR) | Fixed | Sensitivity specifications: collapsed covariates, excluding 2026, stated-date documents only (T30). |
| S5 | Regional cosine distances have no uncertainty and sit below the sampling-noise floor; genre drives the "International" outlier (DS, ICLR) | Fixed | Bootstrap CIs and nearest-neighbour stability (T23), split-half noise floor (T31b), research-only distances (T31); the claim is restricted to what exceeds the floor. |
| S6 | Gap index without intervals; tiny instrument denominators shown as precise percentages (all) | Fixed | Bootstrap CIs (T22, F40); counts shown wherever n < 30 in figures and text. |
| S7 | k-means bundles: silhouette 0.18, k=2 beats k=3, selection rule misdescribed (ICLR, DS) | Reframed | Stability by k reported (T24); bundles demoted to an exploratory supplement table and removed from the narrative. |
| S8 | Mechanism "embodied-specific" claims (liability, insurance) rest on research papers; on instruments only, three mechanisms survive (DS) | Fixed | Mechanism comparison reported on instruments only; the all-document panel is labelled genre-confounded. |
| S9 | Personhood "opposition faded" not significant (DS) | Fixed | Wording changed to describe the distribution without a trend claim. |

### 2.4 Communication

| # | Finding | Decision | v2 change |
|---|---|---|---|
| C1 | Headline numbers disagree across dashboard, report and figures (JOUR) | Fixed | One set of definitions (usable set, embodied set, governance documents, binding) shared by the dashboard script and the analysis code; a key-numbers box at the top of every document. |
| C2 | Executive summary too dense (3.4 numbers per sentence), ten indistinguishable findings, jargon without explanation (JOUR) | Fixed | Five findings with one bold number each; statistics moved to tables; glossary added; plain-language one-page brief added. |
| C3 | Figure titles are labels, not findings; four label collisions; dark heatmaps non-monotone; small n at full weight; slug labels; inconsistent region names and hue assignment (VIZ, JOUR) | Fixed | Every figure redrawn (`scripts/20_figures_v2.py`): title states the finding, subtitle says what is plotted and the n, small-n columns hatched and threshold stated, collisions removed, monotone ramps in both themes, label dictionaries, embodied = blue and general = orange throughout. |
| C4 | "First quantitative map", "110 jurisdictions", "the only general robotics statute in force", "specified nowhere" overclaim (JOUR, ICLR, GOV) | Fixed | Rewritten: first at this scale separating embodied from general AI; documents from 110 countries, 65 of which contribute an instrument; "the only one captured in this collection" with the Korean 2008 Act named; "specified by almost none". |
| C5 | No named robots, laws or people; no "what it means for me" (JOUR) | Fixed | The brief opens with El Salvador's law and names Brazil's humanoid bill, Dubai's vehicle law and Taiwan's factory rules; a four-scenario box added. |
| C6 | Chinese-language sources essentially absent while the humanoid claim leans on Asia (JOUR, GOV) | Fixed | Stated explicitly with counts; Asian conclusions attributed to the countries actually present. |
| C7 | Related work ignores existing governance-document datasets, robot-law mapping and the LLM-annotation validation literature; title promises bibliometrics (ICLR, AI) | Fixed | Related-work paragraphs added; title changed; a related-datasets comparison in the supplement. |
| C8 | No datasheet, licence, ethics statement, README or environment file; converted texts not in the release (ICLR, AI) | Partly | README, LICENSE, requirements and a datasheet added; model inputs for the v2 runs stored; source texts are not redistributed (copyright) and this is stated. |
| C9 | Dashboard: no doctype/charset/viewport, mojibake, 980 px phone layout, clipped bar labels, trust-destroying first screen, codebook strings as labels, no findings strip, no instrument view, keyboard gaps (VIZ, JOUR) | Fixed | Standalone HTML document; usable-only default with an "include excluded captures" switch; "start here" findings buttons; plain-language labels with counts; rules/research column views; CSV export; responsive charts with fixed text size and 24 px bars; sortable headers as buttons with aria-sort; Space opens rows; dialog semantics and focus management; empty state; glossary and methods panels. |
| C10 | Asimov's Laws listed among governance instruments (JOUR) | Fixed | Omitted from the instrument chart and footnoted in the table. |

### 2.5 Not addressed, and why

- **Human validation** (A1): requires domain coders and time beyond this study; the protocol is specified.
- **Acquiring the missing instruments and the standards' texts** (D11, D4): the collection is the study's input; the coverage audit documents what is missing so that a follow-up collection round can target it.
- **Chunked annotation of the longest instruments**: the extended excerpt covers most governance documents in full but still truncates the longest (the AI Act full text, several national strategies); the remaining truncation is reported per class.
- **A second annotator from a different model family**: not available in this environment.

## 3. Changelog v1 to v2 (numbers)

Filled from `data/results.json` after the v2 run; see section 4 of the analysis report for the full set.

| Quantity | v1 | v2 | Why it changed |
|---|---|---|---|
| Unique documents | 1,703 | 1,656 | 46 duplicate captures merged; 3 off-topic or failed captures excluded |
| Usable documents | 1,589 | 1,538 | as above, plus stub captures excluded |
| Embodied-AI set / general-AI set | 674 / 859 | 675 / 806 | duplicates and off-topic captures removed; extended re-annotation added robot types to some instruments |
| Governance instruments (usable) | 381 | 326 instruments + 112 government reports counted separately | catalogue pages, article pages, project deliverables and reports reclassified; duplicates merged |
| Embodied governance instruments | 63 | 65 (34 robot-specific, 31 general with provisions) | reclassifications and re-annotation; now tiered by relevance |
| Binding instruments reaching robots | 7 (claimed) | 5 captured, 4 in force (one revoked) | AI Act duplicate removed, Taiwan stub excluded, EO 14110 marked revoked |
| Technical standards in the embodied set | 12 | 8 (4 content-captured) | catalogue, committee and store pages reclassified |
| Social-robot gap (research share minus instrument share) | +39.9 (no interval) | +37.0 (95% CI 29.4 to 43.5) | bootstrap added; instrument denominator corrected |
| Autonomous-vehicle gap | −33.7 | −53.8 (−65.7 to −41.7) | extended re-annotation found vehicle provisions in more instruments |
| Core-principle differences embodied vs general | 13 of 14 significant (pooled) | 2 of 14 after adjustment (transparency, justice); accountability lower within genre | genre-adjusted and stratified models replace pooled comparison |
| Mechanisms "embodied-specific" | liability regimes, insurance (all documents) | standards references, testing, conformity assessment (instruments only) | comparison restricted to instruments |
| "Regions differ in mechanism more than principle" | claimed (V across different populations) | withdrawn; regions differ on liability and control (V 0.19 to 0.33 on a common population), not on the ethical core | bias-corrected V on one population with bootstrap intervals |
| Europe vs United States distance | 0.012 "nearly identical" | 0.008, below the split-half noise floor (0.033): indistinguishable | noise floor and bootstrap added; North America merged |
| 2025-26 topic shift | industrial policy, oversight, cybersecurity (crude) | cybersecurity (adjusted OR 2.7) and personhood decline (0.38); oversight marginal; industrial policy not significant | adjusted for document class and region |
| Trend in risk-based tiering | OR 1.47 per year | 1.32 (1.09 to 1.60), robust to excluding 2026 and to stated dates | sensitivity specifications |
| Inter-model kappa (median) | 0.89 (computed on pre-cleaning annotations) | 0.85 (computed on the final annotations); re-run 0.91; full text 0.88; blind 0.90; extended 0.83 | recomputed on the right annotations; three new comparisons |
| Lexicon validation | kappa 0.41 to 0.47; rho 0.93 "for principle rankings" | kappa 0.42 to 0.46 after bug fixes; rho 0.92 for embodied-minus-general differences; 0.82 for shares | lexicon repaired; statistic described correctly |
| Share of governance text seen by the annotator (median) | 0.36 | 1.0 (74% of governance documents seen in full) | blind extended re-annotation |
| Reference instruments captured (coverage audit) | not measured | 10 of 38 captured; most of the rest cited but not captured | new audit |
| Regions | 9 (two North America regions) | 8 (North America merged, user request) | |
| Figures / tables | 34 / 19 | 44 / 35 (+13 supplementary) | adjusted models, stratified comparisons, bootstraps, audit, validation |
| Dashboard | fragment only; 1594 to 2027 year span; mixed definitions | standalone document, usable-only default, findings strip, plain labels, rules and research views, export, accessibility pass | |

