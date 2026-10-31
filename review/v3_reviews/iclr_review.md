# Review of "Governing machines that act in the world: a content analysis of embodied-AI governance documents from eight world regions (v3)"

Track: Datasets and Benchmarks / Societal Impact. Reviewer role: adversarial, ICLR/NeurIPS style.

Materials read: `report/paper.md` (the submission), `report/supplement.md`, `report/collection_round2.md`, `report/methods_document_discovery.md`, `report/brief.md` (for consistency only), the tables the paper cites (T07, T09, T10, T17, T20 to T35, T50 to T58), figures F06, F23, F31, F39, F40, F41 and their `figures/data/*.csv`, `data/results.json`, `review/adversarial_review_and_changes.md`, `review/v3_changes_paper.md`, `review/v3_numbers_audit_*.md`, `collection_round2/COLLECTOR_REPORTS.md`, `CANDIDATE_SCHEMA.md`, `ROUND2_RUNBOOK.md`, `codebook/codebook.md`, and the analysis scripts (`scripts/14_analysis_B.py`, `18_analysis_D.py`, `20_figures_v2.py`, `analysis_common.py`). I also ran read-only recomputations on `data/master_table.csv` using the set definitions in `analysis_common.py::load()`. Where a number below is not in the paper, it comes from those recomputations and I say so. No project file was edited.

Paper locations are given as section numbers and, where useful, line numbers of `report/paper.md`.

---

## 1. Summary of claims and contributions

The paper presents a collection of 3,291 documents (3,148 usable) on AI and robotics governance from 116 countries, the EU and the international standards layer, built in two rounds: a round-1 collection by eight regional teams (a "sprint" for robot-specific sources plus a "database" of general-AI instruments) and a round-2 collection by nine collector agents and scripted harvests of seven legal databases that targeted the binding instruments round 1 had missed. Every document is labelled by one proprietary model (Claude Sonnet 5.5) under a 39-field codebook; governance documents and all round-2 documents are labelled from up to 110,000 characters with collector metadata removed. Label consistency is reported five ways on round-1 samples (median kappa 0.83 to 0.91); no human coding exists.

The paper claims that, within this collection: (i) embodied AI is governed by 808 instruments (681 robot-specific), 299 of them binding, and binding law reaches robots through sector law (aviation and drones, road traffic, machinery, medical devices) and general AI law rather than robotics statutes; (ii) research and instruments attend to different robots (social robots +41 points studied-over-governed; drones −32, vehicles −23); (iii) six embodied-specific considerations distinguish embodied from general documents after adjustment for genre, region and year (adjusted OR 3.8 to 170) while most of the ethical core is less present in embodied instruments of the same genre (OR 0.18 to 0.68); (iv) embodied instruments use standards references, licensing, conformity assessment and insurance more than general-AI instruments; (v) regions differ on ethical vocabulary and on licensing and liability more than on physical safety, and Europe and North America are distinguishable but nearest neighbours; (vi) between 2020 to 2024 and 2025 to 2026 legal personhood falls and industrial policy rises at the margin, and v2's cybersecurity rise does not survive. The contributions are the dataset (codebook, annotations, master table, inventory, code), a coverage audit against 38 reference instruments (31 captured), and a documented account of what a second, database-driven collection round changed.

## 2. Strengths

1. The collection effort is real and the funnel is fully documented: candidates, texts obtained, blocked hosts, inventory of 359 unfetchable candidates, collector reports listing what could not be found (`COLLECTOR_REPORTS.md`), and a datasheet. Few governance-document corpora report recall failures this honestly.
2. The coverage audit (Table 25, Figure 41) is a good idea and is now a recurring instrument; the seven still-missing items are named, and instrument counts are consistently called lower bounds.
3. The statistical apparatus added in v2 (genre stratification, covariate adjustment, Mantel-Haenszel, bias-corrected V with bootstrap intervals on a common population, split-half noise floors, trend sensitivities) held through v3, and the paper reports reversals of its own earlier findings rather than hiding them.
4. Most v2 fixes held under re-check: the AI Act appears once; Executive Order 14110 is coded as revoked; the gap index has bootstrap intervals; chi-square uses Monte-Carlo p-values on sparse tables; the metadata-blind, extended-excerpt annotation is used for every governance document; k-means is out of the narrative; `results.json` `round2_coverage` now reads 12/31 (the numbers audit's residual was fixed).
5. The numbers audit (`review/v3_numbers_audit_*.md`) is unusually rigorous and its 24 corrections to the paper were applied; I found no residual arithmetic error in the quoted numbers themselves. The problems below are about design, construct, reliability coverage and presentation, not arithmetic.
6. Code, master table, per-document annotations with prompt hash and cost, and the round-2 scripts are released; the pipeline from stored annotations onward reruns.

## 3. Weaknesses, ordered by importance

### W1. The embodied-vs-general comparison is confounded with collection round, and the headline "ethical core deficit" is a round-2 phenomenon that the adjustment does not address

Location: abstract (line 9: "unlike in the first collection, most of the ethical core is less present in embodied documents of the same genre (odds ratios 0.18 to 0.68)"), Section 5.3 (line 226), Table 20, Table 34, Discussion paragraph 2 (line 481), Limitations (line 493).

Verifiable facts (recomputed from `master_table.csv`; round = doc_id prefix `R2-`):

- Embodied instruments: 808, of which 743 (92%) are round 2 and 65 round 1. General-AI instruments: 372, of which 262 (70%) are round 1 and 110 round 2. The comparison is therefore almost a comparison of round-2 harvested legal texts with round-1 team-collected strategies and guidelines.
- Within round 1 (65 embodied vs 262 general instruments) the core principles do not differ in the direction the paper reports: transparency 78.5% vs 81.7%, justice 64.6% vs 73.3%, beneficence 86.2% vs 81.7%, trust 75.4% vs 67.9%, inclusive growth 84.6% vs 72.5%, privacy 72.3% vs 76.3%.
- Within round 2 (743 vs 110) they differ sharply: transparency 29.3% vs 57.3%, justice 9.6% vs 50.9%, beneficence 24.9% vs 67.3%, trust 12.2% vs 50.9%, inclusive growth 31.4% vs 68.2%.
- Round-2 general-AI instruments themselves differ from round-1 general-AI instruments on the same labels (transparency 57% vs 82%, justice 51% vs 73%, beneficence 67% vs 82%). The collection mechanism moves the labels as much as set membership does.
- The adjusted models (`18_analysis_D.py`, line 22: `pd.get_dummies(M[["doc_class","study_region"]])` plus year) do not include round, source (team / agent / harvest) or `doc_type`. `doc_class` separates binding from soft from draft but not "regulation or decree" from "national strategy" within a class, and the general-AI instrument set is dominated by strategies (83), guidelines (75) and consultations (38) while the embodied binding set is 223 regulations and 72 statutes.
- The general-AI binding comparison group (n = 53) is heterogeneous to the point of not being a comparison group: it contains CFSP Council Decisions, a 1989 Council Decision instituting a research programme, Commission Implementing Decisions on harmonised standards, two NDAA public laws, two Clearview AI judgments, MLIT organisational rules and State Council replies (list from my recompute).

Consequence: the sentence "Robots are governed in the language of product safety more than in the language of AI ethics" (line 481) is, on the present evidence, indistinguishable from "regulations harvested from legal databases mention ethical principles less than strategies and guidelines found by web search". The direction may well be true, and the round-2-only binding contrast (294 vs 30: justice 4% vs 37%, trust 3% vs 37%) supports it, but with n = 30 on one side and no adjustment for round or source, the claim is not established at the strength the abstract gives it. The Limitations paragraph says the design "confounds the two sets with genre twice over" but then treats the within-genre and adjusted analyses as addressing it; they address genre, not round.

The same design artefact produces two other items presented as findings: "among instruments with a settled nature the binding share is now far higher in the embodied set than in the general set (304 of 764 vs 55 of 323; p < 0.001, V = 0.44), where v2 had found the two shares similar" (line 96) is a direct consequence of harvesting legal databases for drone and vehicle terms and not for general-AI terms, and should not be reported as a result; and the regional reversal in 5.4 (Oceania's 52 binding instruments are 48 Australian Federal Register items, of which 28 are CASA instruments) is, as the authors half-admit at line 487, a map of which databases were harvestable.

### W2. Construct validity: "embodied-AI governance" is operationalised as regulation of drones, vehicles and machines regardless of AI content, and the paper's framing does not say so

Location: title; Introduction (line 15 to 17, "how embodied AI is governed"); abstract; Section 3 "Analysis sets" (line 35); Section 5.1 (line 96); Discussion paragraph 1.

Verifiable facts (recompute):

- Of the 299 binding embodied instruments, 162 have primary category `drones_uas` and 93 `autonomous_road_vehicles`; 228 carry `ai_scope = embodied_ai_specific_category`.
- Only 28 of the 299 have a model summary or key-provisions field that mentions "artificial intelligence", "AI", "machine learning" or "algorithm"; 120 mention autonomy or automation in any form. The remaining 179 are, by the annotator's own description, rules about unmanned aircraft registration, levies, aircraft marking, road traffic, export-control lists and the like.
- Examples in the binding set: Japan's Road Vehicles Act (1951), Civil Aeronautics Act (1952), Road Traffic Act Enforcement Order (1960); the 1968 Vienna Convention on Road Traffic; 14 CFR Part 47 (aircraft registration); 15 CFR Part 772 (definitions of terms); Radiocommunications exemption determinations for anti-drone jamming at the Commonwealth Games.
- The codebook's relevance scale (codebook line 61) is "governance of robots or physical AI", so the annotator is instructed to count any drone or vehicle rule as relevant whether or not the rule concerns autonomy.

The paper's own key finding that "the binding layer reaches robots sideways" is partly a restatement of this operational definition. A reader of the abstract will take "embodied AI is governed by 808 instruments, 299 legally binding" to mean 299 instruments governing AI in machines; the data support "299 instruments governing the machine classes in which embodied AI is deployed, a minority of which address autonomy or AI at all". Both are legitimate objects of study, but the paper must choose and say which, and should report headline counts under both (e.g. an "AI-content" tier from the stored texts or a lexicon). Without this, the comparison with the AI-ethics guideline literature (Jobin et al.; Corrêa et al.) in Section 6 is a comparison between AI documents and non-AI documents.

### W3. Precision of the instrument count is not audited; the unit "instrument" is not applied consistently to harvested rows

Location: Section 3 (line 31, 35), Section 5.1 (line 96), Table 53, abstract.

Verifiable facts:

- Among the 299 binding embodied instruments, 15 are commencement orders, levy acts and regulations, radiocommunications exemption determinations, or export-control "definitions" and "control list" parts (e.g. "The Automated Vehicles Act 2024 (Commencement No. 1) Regulations 2025" and "(Commencement No. 3) Regulations 2026" are two instruments; "Civil Aviation (Unmanned Aircraft Levy) Act 2020", "Civil Aviation Amendment (Unmanned Aircraft Levy Collection and Payment) Act 2020" and "Civil Aviation (Unmanned Aircraft Levy) Regulations 2021" are three). 53 titles contain "amend".
- Commission Implementing Regulation (EU) 2019/947 is counted twice, once from EUR-Lex (jurisdiction EU) and once as UK retained law from legislation.gov.uk (jurisdiction GB); the texts are identical.
- `CANDIDATE_SCHEMA.md` states the rule "a law amended several times is one row; a regulation and its implementing ordinance are two rows", but scripted harvests return every matching CFR part, legislative instrument or EUR-Lex expression and the annotation accepts each as a binding instrument at relevance 2 or 3.
- The coverage audit (Table 25) measures recall against 38 reference items only. Nothing in the paper measures precision: the share of the 299 that are distinct, substantive instruments with provisions on embodied systems.
- The gap index's instrument denominator (Table 22, Figure 40) inherits the harvest keyword lists: the EUR-Lex title search used 25 terms of which one is "robots" and the rest are drones, automated driving, machinery, toy safety, product liability, medical devices, lifts, cyber resilience, U-space, type-approval (methods document, Section 2.1); the collector briefs, by contrast, enumerated robot types including companion robots. The social-robot gap (+41) and the drone gap (−32) are therefore partly what the search terms made them, and the gap should be reported by source (collector agents vs scripted harvests) to show how much of it survives.

Instrument counts are "lower bounds" (abstract) only on the recall side; on the precision side they are upper bounds, and the paper does not say so.

### W4. The reliability evidence does not cover the population that produces the v3 findings, and the one round-2 check is neither independent nor about any outcome variable

Location: abstract ("Label consistency was measured five ways"), Section 4 "Consistency checks" (line 43), Section 5.6 (line 475), Limitations (line 495), supplement S4.6.

Verifiable facts:

- `data/reliability_ids.txt` lists 155 documents, all round 1: 56 research outputs, 51 communications, 23 soft instruments, 9 drafts, 7 reports, 5 grey literature and 4 binding instruments; 119 in English. It contains no round-2 document, no technical-standard scope page, and four binding instruments against the 299 that drive Sections 5.1 to 5.4.
- 743 of 808 embodied instruments and 294 of 299 binding ones are round 2. Among embodied instruments 91 are Chinese-language and 48 Japanese; among binding ones 26 Japanese, 14 Spanish, 9 Chinese. The reliability sample has 3 Japanese and 0 Chinese documents.
- The round-2 check (Table 57) compares the annotation with "the collectors' catalogue metadata, which the annotator did not see" and calls it "the only independent reference" (line 43, 475, 495). `ROUND2_RUNBOOK.md` line 20 states that "everything ran inside one Claude Code session ... with nine collector agents ... as subagents". The collectors were LLM agents of the same model family; the paper never says so. The check is a same-vendor model-vs-model agreement on four bibliographic fields (binding nature, jurisdiction, year, class). It says nothing about principles, mechanisms, robot types, relevance or the 0/1/2 depth scale, which are the variables every finding in 5.2 to 5.5 rests on.
- Section 4 (line 43) says "unweighted and level-2 variants in the supplement". They are not in the release: `data/reliability_fields*.csv` has columns `field,type,n,percent_agreement,kappa,note` only, and no file under `tables/`, `report/supplement.md` or `report/analysis_report.md` contains "unweighted" or "level-2". The v1 review item A9 was logged as fixed in `adversarial_review_and_changes.md`; the fix did not survive into v3. This matters because the specification claims ("specified in depth in 47% and 46%") are level-2 claims with no reported reliability of their own.
- A 160-document round-2 reliability sample (re-run plus second model) would cost on the order of 12 to 25 USD at the paper's own per-document cost. Its absence is a choice, not a constraint.

### W5. Table 9 and the abstract's specification claims include 177 landing pages; the v2 rule that landing pages stay out of operationalisation statistics did not hold

Location: abstract ("Technical standards and binding instruments specify physical safety in depth in 47% and 46% of cases; autonomy-level control ... specified in depth by 13 to 37%"), Section 5.3 (line 267: "Figure 23 (content-analysed captures only) and Table 9 show ... Technical standards (238, annotated on scope text) mention physical safety in 80% of cases and specify it in depth in 47%"), Table 9, Discussion paragraph 3.

Verifiable facts:

- `14_analysis_B.py` line 50 builds Table 9 from every embodied document in each group with no `page_quality` filter; `20_figures_v2.py` line 285 builds Figure 23 from `page_quality in {substantive_document, partial_or_excerpt}` only.
- Of the 238 technical standards in the embodied set, 177 are `landing_or_index_page` (median 356 words), 58 `partial_or_excerpt` and 3 `substantive_document`. 71 of the 177 landing pages carry `pr_physical_safety = 2` ("substantively treated, operationalised or required", codebook line 48).
- Figure 23's own data (`figures/data/F23_embodied_principles_by_type.csv`) gives technical standards n = 61, physical safety mentioned 95.1%, in depth 67.2%; Table 9 gives n = 238, 80.3% and 47.1%. The paper cites the figure and quotes the table in the same sentence, and the abstract quotes the table.
- `adversarial_review_and_changes.md` item D4 (v2): "landing pages count in the instrument inventory but not in operationalisation statistics". Table 33's own caption distinguishes the tiers; Table 9 ignores them.

Beyond the inconsistency, scoring "specified in depth" from a 350-word scope statement is not the same measurement as scoring it from a statute, and Table 9 presents them in one column. The Discussion's sentence "standards specify physical safety in depth in 47% of cases" is a statement about catalogue abstracts.

### W6. Dating of consolidated statutes assigns the enactment year to provisions that were added decades later

Location: Section 5.1 (line 106: "a further 16 binding instruments predate 2010 (Japanese road, vehicle and aviation statutes of the 1950s and 1960s, EU machinery and medical-device directives)"), Figure 6, Table 30 and T17 (year as regressor), Section 5.6 (collector-year agreement), codebook line 11.

Verifiable facts: the 16 pre-2010 binding embodied instruments include Japan's Road Vehicles Act (1951), its Enforcement Regulations (1951), the Civil Aeronautics Act (1952), the Road Act (1952), the Road Traffic Act Enforcement Order and Regulations (1960), three 1990 freight-transport ordinances and the 1968 Vienna Convention on Road Traffic; all have `date_basis = stated_in_document`. The e-Gov API returns the consolidated text (methods document 2.1), whose automated-driving provisions date from 2019 to 2023 amendments; the Vienna Convention's automated-driving amendment is from 2016. The codebook instructs "for a law, the enactment date". The paper treats the 1950s dates as a finding rather than a dating artefact. Figure 6's cumulative curve, the year covariate in Tables 20, 28 and 30, the 7% per year decline of proximity and liability (line 416), and the "year within one" agreement with collector metadata (93%) all inherit this. For consolidated texts the relevant date is the version or amending-act date and should be recorded as such (a `version_date` field, or `date_basis = consolidated_text`).

### W7. The v2-to-v3 before/after framing belongs in a response to reviewers and a supplement, not in the paper; but the underlying contrast is a finding in its own right and is under-sold

Location: title "(v3)"; author line ("Version 3, revised after six independent adversarial reviews and extended by a second collection round"); Introduction line 17 ("It is a third version: the first was reviewed adversarially ..."); the Section 5 opening paragraph and Table 53 (lines 51 to 71); roughly twenty sentences of the form "unlike in v2", "v2 had found", "the v2 finding ... does not survive", "far below the 30% per year of v2" (lines 96, 152, 226, 296, 353, 416, 475, 479 to 489); Section 8; Appendix.

Two problems. First, a venue submission is read without access to v2; sentences that compare against numbers the reader has never seen ("the vehicle gap shrank from −54 to −23") carry no information for them, and the version history ("six independent adversarial reviews", "the six reviews ... are provided in the release") reads as an appeal to process. Second, and more important, the paper has buried a result: the same codebook, model and analysis applied to two collection strategies (team web search vs database harvest and agent search) changed the embodied instrument count twelve-fold, the binding count sixty-fold, and reversed three substantive conclusions (ethical-core convergence, regional agreement on values, the cybersecurity trend). That is a methodological finding about governance-document corpora in general (it bears directly on OECD.AI, AlgorithmWatch and the Jobin/Corrêa guideline reviews, all of which are web- or submission-collected) and it is the most novel thing in the paper. It should be stated as a contribution and analysed as one (findings by source, Section 3's T19 "sprint vs database" sensitivity extended to "round 1 vs round 2 vs harvest vs agent"), with Table 53 recast as "collection strategy and what it finds" rather than "v2 vs v3".

Concretely: remove version language from the title, abstract, introduction and author line; move every "v2 found X" sentence to a supplement section "Changes from the previous version"; keep one paragraph in the Discussion on what a database-driven round changes and why.

### W8. Reproducibility and availability claims do not match the release

Location: Section 4 (line 41, "with the exact inputs stored"), supplement S1 ("v2 and round-2 runs additionally ... store the exact model input for every document under `annotations/<run>/_inputs/`"), README ("the exact model inputs in `annotations/*/_inputs/`"), Section 4 cost sentence.

Verifiable facts: `annotations/gov_extended/_inputs/` holds 351 files; `annotations/round2/_inputs/` does not exist (0 files); the 1,732 `annotations/round2/*.json` files contain `doc_id, model, prompt_hash, policy, annotated_at, usage, annotation` and no input text; `collection_round2/data/` holds id lists only (876 KB). Because source texts are not redistributed (a reasonable copyright decision), the round-2 annotations, which are 92% of the instrument layer, cannot be re-derived or inspected from the release at all, and the claim that inputs are stored is false for the part of the collection that matters most. The annotation cost is given as 122 USD (paper line 41), "about 125" (methods document, runbook) and "annotation spend so far: $97.64" (supplement S9). Temperature and seed are uncontrollable through the interface used (S1), which is acknowledged. Finally, the paper should say in Section 3 that the round-2 collectors were LLM agents and that the entire round ran in one 4.5-hour session (runbook line 20); readers of a datasets track need to know that no human curated the round-2 candidates.

### W9. Denominators, cross-document consistency and figure defects (presentation)

Location: throughout Section 5; brief; Figures 6, 31, 39, 41.

- Three denominators are used for the same concept: 808 embodied instruments (Section 3, Table 53), 804 (Table 22, Table 33, Table 21, "content-analysed captures"), 812 (Table 10, Table 7, "governance documents"), and the brief uses 812 where the paper uses 804 (drones 312 vs 309 instruments; AVs 293 vs 288; social robots "13 of 812, 2%" vs "1.6%" of 804; care robots 49 vs 48; industrial manipulators 105 vs 104). Binding instruments are 299 (doc_class), 302 (binding_nature) and 304 (line 96, "304 of 764"). The brief's "research papers barely moved (508 to 509)" and the paper's "581 to 582 research outputs" are different populations with no label. This is the v1 reviewers' item C1 ("one set of definitions") regressing.
- Figure 31's title states "Africa and Latin America have the closest regional profiles (distance 0.03)". The text (line 353) never mentions it, the bootstrap tables (T23, T31b) cover six regions and exclude Africa (n = 26) and Latin America (n = 36), and 0.03 is below the Middle East's own noise floor (0.078). The figure's dendrogram leaf labels overlap the heatmap row labels ("North America Oceania", "International North America" in the rendered PNG). Figure 39's legend overlaps the transparency row. Figure 6's axis starts at 2014 while the text says "from 4 (2012)". Figure 41's title says "the rest are cited in the corpus but not captured" while the text says one is neither. Label collisions were v1 item C3, logged as fixed.
- The abstract is about 730 words with more than 60 numbers; the Section 5.3 and 5.4 paragraphs are lists of percentages. The reader needs the five findings with one number each (the brief does this better than the paper).
- Table 33's `median_fraction_seen` is defined as "the share of the text inside the v1 excerpt" (14,500 characters, `18_analysis_D.py` line 321), a quantity that no longer corresponds to any annotation input in v3; its value of 1.0 for robot-specific instruments reflects short texts, not full reading. 97 of 743 round-2 embodied instruments (67 binding) exceed the 110,000-character extended excerpt; the paper says only that "the extended annotation still truncates the longest governance documents".

### W10. Statistical presentation

- The adjusted odds ratios for the six embodied-specific considerations (OR 3.8 to 170, abstract and Table 20) are near-tautological: the considerations are defined as embodied-specific and the general set is defined by the absence of embodiment, so "survives adjustment" is uninformative; proximity is present in 1 of 372 general instruments, the model is near separation and the CI (54 to 535) says so. These should not lead the abstract; the core-principle result (if it survives W1) is the informative one.
- Holm correction is applied "within families" but the number and definition of families is not stated anywhere; across Tables 20, 21 (four strata), 28, 29, 30 and 34 there are well over 200 tests.
- The trend claims (line 416: proximity and liability declining about 7% per year) adjust for class and region but, like everything else, not for source; the within-instrument composition shifts toward drone and vehicle regulation over time and these instruments rarely mention proximity. A trend model with source as covariate, or restricted to research outputs, would separate the two.
- The binding-share test (line 96) and the "jurisdictions with an embodied instrument 30 to 60" (Table 53) are design artefacts reported with p-values and effect sizes.

### W11. Novelty relative to prior corpora and LLM-annotation studies

The related-work paragraphs are adequate and the related-datasets table (S7) is useful but sits in the supplement. The genuinely new elements are (a) a corpus that separates embodied from general AI and codes six embodied-specific considerations, (b) the coverage audit as a reusable instrument, and (c) the demonstration that collection strategy, not coding, determines what such a corpus says about binding law. Element (c) is not claimed as a contribution (see W7). The LLM-annotation methodology adds no new validation method beyond Gilardi et al., Törnberg, Pangakis et al.: the "five ways" are all same-vendor consistency checks on round-1 samples, and the v1 review's gating request (a human-coded sample; `adversarial_review_and_changes.md` A1, "Not done") remains undone two versions later while the supplement's S4.5 protocol shows that a 200-document double-coded sample is specified and feasible. For a datasets-and-benchmarks track, labels without any human validation are a known-unknown that limits the contribution regardless of scale.

### W12. Ethics and limitations

The Limitations section is candid about genre confounding, the single model family, truncation and the sandbox's reach. It should add: that round-2 collectors were LLM agents (W4, W8); that the instrument counts are upper bounds on precision as well as lower bounds on recall (W3); that the collection over-represents jurisdictions with open legal APIs (Australia supplies 48 of 299 binding instruments; Japan 26; the EU 56 through CELLAR), which the Discussion mentions for regions but the abstract's "116 countries" does not; and that technical standards' scope texts were fetched from a committee mirror and annotated (copyright status of that use should be stated). The datasheet's "not a census of instruments" should appear in the paper, since the abstract leads with the census-like numbers.

### W13. Check of v2 fixes

Held: D1, D2, D3, D5, D6, D7, D9, D10 (data corrections); A3, A4, A5, A6, A7, A8, A11 (annotation); S1 to S9 (statistics); C2 (brief), C4, C5, C6, C7, C9, C10.

Did not hold or regressed in v3: D4 (landing pages in operationalisation statistics: Table 9, abstract; W5); A9 (unweighted and level-2 kappas: absent from the release; W4); C1 (one set of definitions across documents: 804/808/812, brief vs paper; W9); C3 (label collisions: Figures 31 and 39; W9); C8 (stored model inputs: absent for round 2; W8).

Not done and still gating: A1 (human validation).

## 4. Questions for the authors

1. Within round 1 (65 embodied vs 262 general instruments) the core principles do not differ; within round 2 they differ sharply, and round-2 general instruments differ from round-1 general instruments by 20 to 25 points on the same labels. Does the core-principle deficit survive a model with round (or source) and `doc_type` as covariates, and a round-2-only contrast? If it does not, how should the Discussion's second paragraph read?
2. What fraction of the 299 binding instruments contain any AI or autonomy provision in their text (not their title)? The stored texts exist on your side; a lexicon count over the full texts would answer this in minutes.
3. Please estimate precision: draw 50 to 100 of the 299 at random and classify each as (a) a distinct instrument under the candidate schema's own rule, (b) carrying substantive provisions on an embodied system, (c) carrying any AI or autonomy provision. What are the three shares with intervals?
4. Why does the reliability sample contain no round-2 document and only four binding instruments, when round 2 supplies 92% of the instrument layer? What would a 160-document round-2 re-run and second-model check cost?
5. Were the round-2 collector agents Claude models? If so, in what sense is the collector-metadata agreement an "independent reference" (lines 43, 475, 495)?
6. Table 9 uses n = 238 standards and Figure 23 n = 61. Which do you intend the abstract's "47%" to describe, and does a scope statement's "substantively treated" mean the same thing as a statute's?
7. Where are the "unweighted and level-2 variants" promised at line 43?
8. Why is `annotations/round2/_inputs/` absent when S1 and the README say inputs are stored for round-2 runs?
9. Japan's Road Vehicles Act is dated 1951 and the Vienna Convention 1968. Do you intend year to mean enactment of the consolidated text? If so, what does the 7% per year decline in proximity and liability mean?
10. The EUR-Lex title harvest used 25 terms, one of which is "robots". How much of the social-robot gap (+41) and the drone gap (−32) comes from the scripted harvests versus the collector agents, which were briefed with robot-type lists?
11. Is 2019/947 (EU) and its UK retained copy two instruments by your rule? Are commencement orders and levy regulations instruments?
12. Which v2 sentences should a reader of this paper, who has no access to v2, be expected to understand?

## 5. Requested changes

### Must (for the paper to be sound)

1. Add round (or source: team / collector agent / scripted harvest) and `doc_type` as covariates to Tables 20, 28 and 30 and the Mantel-Haenszel analysis; report round-1-only and round-2-only versions of Table 21; rewrite the abstract and Discussion paragraph 2 to whatever survives. Drop the binding-share test (line 96) and the "jurisdictions 30 to 60" line as findings; present them as consequences of the design. (W1, W10)
2. State the construct. Either retitle the object as instruments governing the machine classes in which embodied AI is deployed, or add an AI-content tier (text-based) and report the headline counts (808 / 681 / 299) under both definitions in the abstract and Section 5.1. (W2)
3. Run and report a precision audit of the binding set (random sample, three criteria, intervals), apply a documented rule to commencement orders, levy and fee instruments, amendment-only instruments and cross-jurisdiction copies of one text, and recompute Table 53, Table 22 and Section 5.1 under it. Report the gap index by source. (W3)
4. Add a round-2 reliability sample (re-run and second model, at minimum; full-text and blind are already the policy) stratified over binding instruments, standards scope pages and non-English texts, and report per-field kappa including the level-2 (depth) labels. Either supply the unweighted and level-2 kappa tables or delete the sentence that promises them. (W4)
5. Recompute Table 9 on content-analysed captures (or show both tiers side by side with a clear statement that scope-page scores are a different measurement) and correct the abstract's "47% and 46%" and "13 to 37%" accordingly. (W5)
6. Record a version or amendment date for consolidated texts and use it, or exclude consolidated texts dated before the technology existed from Figure 6 and the year-based models, and say so. (W6)
7. Remove version history from the title, abstract, author line and introduction; move the v2 comparisons to a supplement section; add the collection-strategy contrast as an explicit contribution with its own analysis. (W7)
8. Correct the availability claims: state that round-2 inputs are not stored, or store them; reconcile the three cost figures; disclose that round-2 collectors were LLM agents in a single session. (W8)

### Should

9. Use one denominator for embodied instruments throughout the paper and the brief (my recommendation: 804 content-analysed, with 808 stated once in Section 3), one for binding (299), and label every population when quoting a count. (W9)
10. Fix Figure 31 (six regions to match T23 and T31b, or eight regions with Africa and Latin America noise floors added; remove the label collision; make the title consistent with the text), Figure 39's legend, Figure 6's axis start and Figure 41's title. (W9)
11. State the number and definition of Holm families. Move the embodied-specific odds ratios out of the abstract's first sentence of results and lead with the core-principle result once W1 is settled. (W10)
12. Cut the abstract to about 300 words with one number per finding; move the percentage lists in 5.3 and 5.4 to tables. (W9)
13. Add to Limitations: precision as an upper-bound issue; API-availability bias by jurisdiction with the Australia / Japan / EU shares; the LLM identity of round-2 collectors; copyright status of mirrored scope texts. (W12)
14. Bring the related-datasets comparison (S7) into Section 2 and state the novelty claim in one sentence. (W11)

### Could

15. Execute the S4.5 human-validation protocol on 200 documents and report model-vs-human kappa and corrected headline proportions (Egami et al.; Angelopoulos et al.). This is the change that would move the contribution score. (W11)
16. Replace `median_fraction_seen` in Table 33 with the share of documents fully inside the 110,000-character extended excerpt, by tier. (W9)
17. Report the research-only trend models alongside Table 30 so that the proximity and liability declines can be attributed. (W10)
18. Add a short "how to read the counts" box (what an instrument is, what binding means, what relevance 2 means for a drone rule) at the top of Section 5.

## 6. Scores

- Soundness: 2 / 4. The arithmetic reproduces and the genre adjustments are competent, but the headline comparative finding is confounded with collection round and the adjustment does not touch that; the construct is not what the framing says; the instrument count is unaudited for precision; the reliability evidence covers 4 of 299 binding instruments and no round-2 document.
- Presentation: 2 / 4. Organised and candid, but written as a revision log rather than a paper, with three denominators for one concept, an abstract of 60 numbers, figure/table disagreement on the specification claim, and label collisions that a previous round logged as fixed.
- Contribution: 3 / 4. A large, documented, releasable corpus with a coverage audit and a demonstration that collection strategy dominates coding in governance-document studies; held back from 4 by the absence of any human-validated labels and by the construct problem.
- Overall: 4 / 10. Reject in current form; a clear revision path exists (changes 1 to 8), and the collection-strategy result could make a strong datasets-track paper once the comparison is sound and the counts are audited.
- Confidence: 4 / 5. I read the full paper, supplement and companion report, re-ran the set definitions on the master table, checked the scripts that build the contested tables and figures, and verified every numeric claim I make above; I did not re-run the annotation or the bootstrap code.
