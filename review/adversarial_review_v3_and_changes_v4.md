# Adversarial review of v3 and the changes made in v4

Six independent reviews of the version-3 deliverables were commissioned from fresh reviewers (AI agents in this session, each with a written brief and no stake in the conclusions): a data scientist and applied statistician, an AI researcher specialising in LLM annotation validity, a conference reviewer (ICLR/NeurIPS style), a technology and policy journalist, an AI and robotics governance expert, and a data-visualisation and dashboard QA specialist. Each wrote a full review to `review/v3_reviews/`. Two further checks were commissioned from the findings: an independent precision audit of 100 randomly sampled "binding embodied instruments" (`review/v3_reviews/precision_audit.md`) and a round-2 reliability sample (second model and same-model re-run on 160 stratified round-2 documents). This log maps every material finding to a decision and to what changed in v4. Status codes: **Fixed**, **Partly** (implemented with a stated limit), **Reframed** (claim withdrawn or rewritten rather than data changed), **Not done** (with reason).

## 1. Summary verdicts on v3

| Reviewer | Verdict | Headline |
|---|---|---|
| Data scientist | Arithmetic reproduces and v2 fixes hold on round-1 rows; the round-2 design enters every "v2 finding reversed" claim as a confound; the counting unit inflates instrument counts | 4 critical, 10 major, 12 minor |
| AI researcher | Major revision: the excerpt cleaner deleted most of the text of Chinese and Japanese documents; no reliability evidence for round 2; stubs re-enter the counts; the core-principle reversal is a round/length artefact | 5 critical, 9 major, 7 minor; 29-document spot check: 12 with an error in a set-defining field |
| ICLR reviewer | Reject in current form (Soundness 2, Presentation 2, Contribution 3, Overall 4/10, Confidence 4); clear revision path; the collection-strategy contrast is the most novel result and should be a contribution | 8 must, 6 should, 4 could |
| Journalist | The lead counts paperwork, not regimes; trust claims do not cover the data the headline rests on; the dashboard's methods panel is v1 text; brief density worse than v1 | 5 critical, 12 major, 9 minor |
| Governance expert | Headline instrument count is a document count inflated roughly two-fold; 68% of a risk-stratified sample of 159 rows had an error (62% material); status and class rules recurred at scale in round 2; 190 verified binding candidates were never read | 4 critical, 12 major, 7 minor |
| Visualisation QA | Computed titles overflow 36 of 44 figures; four titles contradict their data; F31 unreadable; dashboard methods panel stale, two start-here views wrong, column views rewrite filters | Figures: 4 high, 14 medium, 23 low; dashboard: 3 high, 7 medium, 4 low |

Precision audit (n = 100 random from the 299 v3 binding embodied instruments): distinct instrument 67% (95% Wilson 57 to 75), binding 97%, substantive embodied provisions 56% (46 to 65), autonomy or AI content 67%, explicit AI 14% (9 to 22); all three of distinct, binding and substantive: 54% (44 to 63), implying about 161 instruments (132 to 190) rather than 299.

Round-2 reliability (160 stratified round-2 documents): median kappa over single and ordinal fields 0.86 against a second model (Claude Opus 5.5) and 0.91 for a same-model re-run, against round-1 values of 0.85 and 0.91; weakest round-2 fields against the second model: page quality (0.53), stance toward regulation (0.65), publication stage (0.66), date basis (0.70), solidarity level (0.72), instrument status (0.75); every other principle at or above 0.79.

## 2. Findings and decisions

### 2.1 Annotation inputs and labels

| # | Finding (reviewers) | Decision | v4 change |
|---|---|---|---|
| A1 | The v2 excerpt-cleaning rule (drop short lines near the top that carry no digit, capital or sentence punctuation) deletes Chinese, Japanese and Korean paragraphs because they have no whitespace words or ASCII full stops; a median of 24% of each Chinese document reached the model; 97 Chinese documents naming robots or AI had none of those terms in the model input, 83 of them labelled "not about AI" (AI) | Fixed | Character-aware cleaner in `04_annotate.py` and `04_annotate_r2.py` (lines with CJK characters or CJK punctuation are never dropped; policy tag `cjk_clean=v4`); all 376 round-2 and 46 round-1 Chinese, Japanese and Korean documents re-annotated (`annotations/round2`, `annotations/cjk_fix`); embodied-set membership of CJK documents changed for 57 of 422 |
| A2 | No reliability evidence for round 2 (92% of the embodied instrument stratum); the only check (collector metadata vs annotation) is not independent because the collectors were LLM agents and harvest-script constants (AI, DS, ICLR, JOUR) | Fixed | Stratified 160-document round-2 sample re-annotated by Claude Opus 5.5 and by a Sonnet re-run (`09b_reliability_round2.py`, tables S09b); collector-agreement table kept but relabelled as a consistency check, not validation |
| A3 | Promised "unweighted and level-2 kappa variants" did not exist (ICLR) | Fixed | `09c_reliability_variants.py`, table S09b, for all six comparisons |
| A4 | Truncated statutes labelled from parametric knowledge (robot articles beyond the 110,000-character excerpt) (AI) | Partly | `excerpt_is_truncated` and `full_text_chars` are now reported per document in the data dictionary and the supplement; depth statistics restricted to captures of at least 150 words; a full-text pass for statutes over 110,000 characters is listed as future work (cost) |
| A5 | Standards annotated on catalogue scope pages scored "in depth" (AI, DS, GOV, ICLR, JOUR) | Fixed | Catalogue and landing pages are a separate unit (`catalogue_page`) excluded from instrument counts and from all depth statistics (T09, F23 use content-analysed captures with at least 150 words) |
| A6 | 16 agent-abstract inputs carried the collector's header (AI) | Fixed | Header lines stripped by the cleaner before annotation on re-run; flagged in the registry (`meta_how`) |
| A7 | No run manifest, CLI version or stored round-2 inputs in the release (AI, ICLR) | Fixed | `annotations/round2/_inputs` included; `data/run_manifest.json` (models, prompt hashes, policies, counts, cost per folder, CLI version) |

### 2.2 Counting unit and construct

| # | Finding | Decision | v4 change |
|---|---|---|---|
| U1 | One document = one instrument: commencement orders, levy and fee acts, individual exemptions, directions and approvals, EEA incorporation decisions, language corrigenda, definitions parts, tables of contents and register pages counted as binding instruments; yearly renewals and successive versions counted separately (DS, GOV, JOUR, ICLR, precision audit) | Fixed | `07c_v4_units_and_tiers.py`: documented title and capture rules assign `instrument_unit` (principal, amendment, ancillary, incorporation, language_copy, catalogue_page, stub, duplicate_text, dependent); headline counts use principal instruments (principal + amendment); instrument families (`family_key`) reported as a further tier; T53b shows the collection under each unit |
| U2 | Construct: "embodied-AI governance" operationalised as regulation of drones, vehicles and machines regardless of AI content; 14% of binding instruments name AI (ICLR, JOUR, precision audit) | Fixed | Text-based tiers from the full text: `autonomy_terms` and `ai_explicit`; headline counts reported under the machine-class construct and both tiers (T53b); the paper states the construct as the governance of the machine classes in which embodied AI is deployed |
| U3 | 55 of 299 binding instruments enter the embodied set with relevance 0 or 1 through a category label (AI, DS) | Fixed | Robot-relevant tier (relevance 2 or 3) is the headline instrument count; the label-only tier is reported separately |
| U4 | Precision not audited (ICLR) | Fixed | Independent random-sample audit (n = 100, three criteria, Wilson intervals); T62 compares the rule-based unit with the audit on the same documents; precision-corrected counts reported with intervals |
| U5 | Byte-identical texts under different ids; StVG §1a/§1d split; AV Act plus commencement orders (AI, DS) | Fixed | `duplicate_text` unit from text hashes; commencement orders ancillary; instrument families |
| U6 | 86 near-duplicate title pairs survive de-duplication (DS) | Partly | Families group yearly renewals, successive versions and parts; stricter title merging was not applied because distinct parts of one regime are legitimately distinct documents |

### 2.3 Status, class and coverage

| # | Finding | Decision | v4 change |
|---|---|---|---|
| S1 | Standards drafts (AWI to FDIS) counted as published; mandatory GB standards as soft law; CCW working papers and chair's texts as draft instruments; proposals whose act is in the collection still "under consideration" (GOV, AI) | Fixed | Rules in `07c` (status under development for draft standards; GB mandatory standards binding, with the standard number matched anywhere in the title; CCW process documents reclassified as position documents; proposals superseded when the adopted act is present) |
| S2 | 159-row classification audit: 108 rows with an error (GOV) | Fixed | 157 documented doc-level corrections on 91 documents converted from the audit table (153 in the first conversion; the writers' cross-check against the expert's fix text then corrected six status values that the mechanical code-to-value mapping had inverted, among them the Machinery Directive 2006/42/EC, which is in force until 20 January 2027, and five class values for mandatory GB standards and a binding departmental notice, and the GB rule was widened to numbers anywhere in the title) (`data/manual_overrides_v4.csv`: unit, class, status, year, relevance) |
| S3 | Machinery Regulation coded "adopted, not yet in force" and Machinery Directive "repealed"; Beijing E-Town measure a 34-word stub counted as the only binding humanoid instrument (GOV, JOUR) | Fixed | Overrides from the audit; stubs under 150 words excluded from instrument counts |
| S4 | Reference list: Taiwan dated 2025; R157 and R171 one row with R171 not captured; US state AV statutes "captured" through a web page; list mixes general-AI instruments (GOV, DS) | Fixed | Taiwan dated 2018; R157 and R171 separate rows; stricter pattern for state AV statutes; "captured" now means a principal instrument with a content-analysed capture; the audit reports 22 of 39 on the strict criterion (31 on the looser title-family match used in v3; v2: 11 and 12) of 39 |
| S5 | 190 collector-verified binding candidates never read (Hangzhou robot statute, Shenzhen ICV and AI regulations, Hong Kong AV regulation, Korea Robots Act and AV decrees, DoD 3000.09, California SB 243, India Drone Rules, PLD 2024/2853, Toy Safety Regulation, French AV ordinance and decree, ANSI/A3 R15.06, GB/T 48317.1) (GOV) | Partly | Every failed fetch retried with the improved routes (4 texts recovered: the Tanzania RPAS amendment regulations 2020, the GB/T 43370-2023 catalogue page and two Korean ministry press pages; the Product Liability Directive 2024/2853, the Toy Safety Regulation 2025/2509 and Directive 2009/48/EC still returned no text); the Korean, Chinese NPC, Hong Kong, Légifrance, defense.gov and Indian hosts still block the environment or serve script-only pages; the remaining items are named in the limitations and in the round-3 plan |
| S6 | Consolidated statutes dated at enactment (1951, 1952, 1960) or at consolidation (2026) (DS, ICLR) | Reframed | Time analyses already restricted to 2014 to 2026 with 2026 partial; sector-law "first appearance" years dropped from the narrative; the dating rule and its effect on F06 are stated; version dating deferred to round 3 |

### 2.4 Analysis and inference

| # | Finding | Decision | v4 change |
|---|---|---|---|
| I1 | The embodied-vs-general contrast is confounded with collection round (and text length and capture tier); the "ethical core deficit" (11 of 14 core principles lower) does not exist within round 1 and is driven by round-2 legal texts (ICLR, DS, AI) | Fixed / Reframed | Collection round added to the adjusted models (T20) and trend models (T30 round rows); T20b reports the contrast within round 1 and within round 2, all documents and instruments; the paper and brief present the pooled reversal as a composition effect and lead with the within-round result |
| I2 | Trend claims (proximity and liability decline, cybersecurity absence) are round-composition artefacts; tiering and conformity growth intact within round 1 (DS) | Fixed | T30 adds "round-1 only" and "round covariate" specifications and the proximity and liability outcomes (flat within round 1 at 1.00); the narrative reports trends only where they survive within round |
| I3 | Regional "differ on values" is a genre-mix effect (DS) | Fixed / Reframed | T29b computes regional divergence within research outputs and within principal instruments (regions with at least 20 documents of the genre; a first build dropped every item when any region was thin and produced no table, caught by the writers): within research outputs 2 of 14 core principles differ by region, within principal instruments 12 of 14, with the standards-heavy international layer at the low end; the claim is retained only for the instrument layer and qualified by instrument-type mix. Region set aligned (at least 30 embodied documents) across F31, T23, T29 and T31b |
| I4 | Binding-share test and "jurisdictions 30 to 60" reported as findings although they follow from the design (ICLR) | Reframed | Reported as consequences of collection design in the companion report, not as findings |
| I5 | OR 170 rests on three general documents under near-separation (DS) | Fixed | Sparse-cell flag in T20; such odds ratios are reported as not estimable |
| I6 | Three denominators for one concept (804/808/812); brief and paper disagree (ICLR, JOUR, VIZ) | Fixed | One instrument base in `analysis_common.load` (principal instruments) used by every table, figure, the dashboard and the narratives; every count names its unit |
| I7 | Table 9 includes 177 landing pages; abstract's 47% and 13 to 37% depend on it (ICLR, JOUR, DS) | Fixed | T09 and F23 on content-analysed captures with at least 150 words |
| I8 | Holm families undefined; abstract of 60 numbers; percentage lists in prose (ICLR) | Fixed | Stated once in the methods; abstract rewritten to at most 300 words; percentage lists moved to tables |

### 2.5 Figures and dashboard

| # | Finding | Decision | v4 change |
|---|---|---|---|
| V1 | Computed titles overflow and shrink the plot area in 36 of 44 figures (VIZ) | Fixed | Titles wrapped to the figure width (three lines at most) in `title()`; font capped at 9.5 pt |
| V2 | F40 hard-coded and false; F23 title inverted; F39 double axis inversion; F28 shares sum to 101% (VIZ) | Fixed | F40 computed from T22; F23 computed from the lowest in-depth principle; single inversion on the shared axis; F28 numerator restricted to plotted periods |
| V3 | F31 unreadable (leaf labels overprint, order reversed, eight regions vs six in the tables) (VIZ, ICLR, JOUR) | Fixed | Heatmap order follows the dendrogram, row labels on the right with n, region set aligned |
| V4 | Title-generator grammar ("drones uas", "proposal or bills"), F08 "Japan 65 binding" on the wrong basis, legends inside data (F04, F28), drafts colour, v3/v4 colours (VIZ) | Fixed | Category label dictionary and plural dictionary; F08 on the embodied principal basis; legends moved under the axes; drafts muted; F51 and F52 recoloured |
| V5 | Dashboard methods panel is v1 text contradicting the brief; Technical-standards view is a substring search; column views rewrite filters; round-2 records labelled "general AI"; 577 not-AI documents in the default view; no robot-type or drone filter; no before/after (VIZ, JOUR) | Fixed | Methods panel generated from data (shares, kappas incl. round 2, round-2 counts); start-here views on document type and robot category; column views no longer touch filters; "Collected as" labels per round; not-AI documents hidden by default with an explicit option; 23-category robot-type and instrument-kind filters; counting-unit filter; round-2 tile and view; drawer shows unit, family and AI-content flags |

### 2.6 Narrative and presentation

| # | Finding | Decision | v4 change |
|---|---|---|---|
| N1 | Version history in the paper's title, abstract and author line; v2 comparisons throughout (ICLR) | Fixed | Removed from the paper; comparisons moved to supplement S10; the collection-strategy contrast added as a contribution |
| N2 | Brief: 192 numbers in 52 sentences; jargon before definition; "no human read every document" understates; collectors and reviewers not identified as AI agents; the jump from 5 binding rules invites "regulation exploded" (JOUR) | Fixed | Brief rewritten to at most 900 words and about 1.5 numbers per sentence, definitions first, plain disclosure of AI labelling and AI collectors/reviewers, and the artefact explained in the lead |
| N3 | "El Salvador the only robot-titled statute" false (GOV, DS) | Fixed | Withdrawn; Hangzhou (unread) and Beijing (stub) named |
| N4 | Three cost figures; availability claims not matching the release (ICLR, AI) | Fixed | Run manifest is the single source; availability section matches the package |
| N5 | Human validation of labels (ICLR, AI, DS; carried from v1) | Not done | No human coders are available in this setting; the S4.5 protocol remains the stated next step; every label is model-produced and the narratives say so |

## 3. Effect on the headline numbers

| Measure | v2 | v3 | v4, all legal texts (comparable unit) | v4, principal instruments | v4, robot-relevant principal (relevance 2 or 3) |
|---|---:|---:|---:|---:|---:|
| Documents annotated / usable | 1,656 / 1,538 | 3,291 / 3,148 | 3,295 / 3,165 | | |
| Embodied-AI set | 675 | 1,589 | 1,603 | | |
| Governance instruments in the embodied set | 65 | 808 | 810 | 505 | 408 |
| of which with autonomy or AI provisions in the text / naming AI explicitly | | | | 395 / 153 | |
| Binding instruments in the embodied set | 5 | 299 | 291 | 195 | 168 |
| of which counted once per instrument family / with autonomy or AI provisions / naming AI explicitly | | | | 194 / 140 / 15 | |
| Precision audit of the v3 binding set (random n=100): distinct, binding and substantive | | 54% (44 to 63), about 161 (132 to 190) | | rule-based unit on the same sample: 61% (51 to 70); agreement 0.77, kappa 0.53 | |
| Jurisdictions with an embodied instrument (comparable unit) | 30 | 60 | 60 | | |
| Reference instruments captured (strict: principal instrument with content-analysed capture; loose: title-family match) | 11 / 12 of 39 | 22 / 31 of 39 | 22 / 31 of 39 | | |
| Core principles lower in embodied than general instruments (Holm) | none of 14 | 11 of 14 (pooled) | within round-1 instruments: 0 of 14; within round-2 instruments: 10 of 14 (composition effect) | | |
| Trends | tiering and conformity rising about 30% per year | proximity and liability declining 7% per year; tiering and conformity not significant | within round 1: tiering OR 1.31 and conformity 1.26 per year; proximity and liability flat (1.00); with round as covariate: tiering 1.10, conformity 1.05 | | |
| CJK documents (422): rated not about AI | | 205 | 160 (57 documents changed embodied-set membership after the character-aware cleaner) | | |
| Round-2 reliability (160 documents), median kappa | not measured | not measured | 0.86 second model, 0.91 re-run | | |

The order-of-magnitude increase reported in v3 survives on the comparable unit (65 to 810 embodied instruments; 5 to 291 binding) but is a property of where the collection searched, not of the world; on the v4 headline unit the collection holds 505 principal embodied instruments, 195 of them binding, 168 of those rated robot-relevant, and only 15 binding instruments that name AI explicitly.

## 4. Files

Reviews: `review/v3_reviews/*_review.md`, `precision_audit.md`, `precision_audit_sample.csv`, `governance_audit_rows.csv`, `shots/`. Rules and corrections: `scripts/07c_v4_units_and_tiers.py`, `data/manual_overrides_v4.csv`, `data/reference_instruments.csv`. Reliability: `scripts/09b_reliability_round2.py`, `09c_reliability_variants.py`, `data/reliability_fields_r2opus.csv`, `_r2rerun.csv`, `data/reliability_variants.csv`. Change logs per document: `review/v4_changes_*.md`; numbers audit: `review/v4_numbers_audit.md` (1,714 claims checked, 81 corrected).
