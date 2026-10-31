# Review: "Governing machines that act in the world: a bibliometric and content analysis of embodied-AI governance across 110 jurisdictions"

Track: Datasets and Benchmarks / AI and Society. Reviewer read `report/paper.md` (15-page PDF), `report/analysis_report.md`, `report/supplement.md`, `codebook/codebook.md`, all tables, seven figures (F05, F18, F20, F23, F31, F34, F35), `data/results.json`, the scripts in `scripts/`, and ran read-only checks on `data/master_table.csv` and the `annotations/` folders. Where I cite a number that is not in the paper, it comes from those checks and I say so.

---

## 1. Summary

The paper assembles a corpus of 1,703 deduplicated documents (1,589 with usable text) that eight regional teams collected on AI and robotics governance, annotates every document with a single LLM (Claude Sonnet 5.5) against a 39-field codebook that includes a 23-category embodied-AI taxonomy, 20 principles scored 0–2, 19 mechanisms and 27 topics, and then compares an "embodied-AI set" (n = 674) with a "general-AI set" (n = 859). It reports that embodied-AI governance is mostly a research discourse (509 research outputs, 63 instruments, 7 binding), that research and governance attend to different robots (social robots 43% of research vs 3% of instruments; autonomous vehicles 12% vs 46%), that embodied documents have a harm-avoidance principle profile and a product-safety mechanism profile, that regions converge on principles and diverge on mechanisms, and that 2025–26 documents shift toward industrial policy, oversight and cybersecurity. Validation is LLM-vs-LLM agreement on 160 documents (median kappa 0.89), same-model test-retest (0.95) and regex lexicons on full text (Spearman rho 0.93 on principle rankings). Code, master table, annotations and a dashboard are provided.

## 2. Strengths

- **A genuinely under-studied question.** The gap between the AI-principles literature (Jobin et al.; Fjeld et al.; Corrêa et al.) and robot-law scholarship (Calo; Leenes et al.) is real, and asking "which robots are governed vs studied" with a document corpus is a good idea.
- **A reusable codebook and taxonomy.** The 39-field codebook (supplement S2) with a 23-category, 7-group embodied taxonomy, six embodied-specific principles added to the Jobin/OECD core, and an explicit 0/1/2 "mentioned vs operationalised" scale is well specified, has decision rules, and could be adopted by others. The schema-enforced JSON output is a sound engineering choice.
- **Unusually complete release of the pipeline.** Every figure has a CSV twin, every number traces to `results.json`, the prompt hash and per-document cost are stored, and the scripts run end to end. This made the review possible and is rare in this literature.
- **Several validation layers rather than none.** Second-model agreement, test-retest, cross-checks against the collectors' own labels (Table S10), lexicon comparison on full text and an 11-subset sensitivity table (T19) are more than most LLM-annotation papers provide.
- **Honest limitations section.** §7 and report §9.4 acknowledge the sprint/database design, the European and English skew, excerpt-based coding, inferred years and the duplicate AI Act.
- **Some findings are plausibly robust and interesting**: the near-absence of embodied-specific principles (proximity, physical safety, autonomy level) from general-AI documents (Table 8), the standards-vs-audits mechanism contrast among instruments (Table 10, right columns), and the research-vs-instrument asymmetry for social robots (Fig. 18) are the kind of result the community would cite if they were properly supported.

## 3. Weaknesses (ranked by importance)

### W1. The sampling frame confounds the central embodied-vs-general comparison, and the abstract reports the confound as a finding. (§3.1, §3.3, §5.1, §6 para 1, Table 19)

The collectors ran two exercises: a *sprint* for robotics sources and a *database* for general AI instruments. From the master table: sprint documents fall 640 embodied / 216 general; database documents fall 34 embodied / 643 general. Research outputs: 568 from the sprint, 14 from the database. So "embodied set" and "sprint" are nearly the same partition, and the ratio "509 research : 63 instruments : 7 binding vs 50 : 301 : 29" (abstract, §6) is the ratio of what two differently-instructed collection exercises were told to gather. The paper's own Table 19 shows it: in the database-only subset the research share of embodied documents is 2.9%, not 75.5%. The paper calls this "partly a collection artefact and partly real" (§6) but offers no evidence for the "partly real" half, and the abstract's first finding ("embodied-AI governance is predominantly a research discourse") is stated without qualification.

The same confound contaminates every all-document comparison: the principle contrasts in Table 8 (inclusive growth 75% vs 34%; transparency 60% vs 41%) and the left two columns of Table 10 are largely research-vs-instrument-and-news genre contrasts, not embodied-vs-general contrasts. The report (§9.4) says the instrument-only comparisons are "the safer reading", but the paper leads with the all-document numbers.

The collection protocol itself is not described: no search strategy, inclusion criteria, per-team instructions, date range, or inter-team consistency check appears in the paper or supplement, so the frame cannot be assessed.

*What would resolve it:* (a) document the collection protocol; (b) make every embodied-vs-general comparison within genre (instrument vs instrument, research vs research), or stratify/reweight by `collection_set` and `doc_class`; (c) rewrite the abstract so that counts are "in this collection" and the research-to-instrument ratio is presented as a property of the sample; (d) if the claim that embodied governance is research-heavy is to be kept, test it on a frame built the same way for both topics (e.g., a matched search of OECD.AI or a legislation tracker).

### W2. The "binding layer" of seven instruments does not survive inspection, and the corpus is missing the obvious binding robot law, so the headline about *how* law reaches robots is not supportable. (§5.1 para 2, Table S01, §5.5, §6, §8)

Checking the seven documents in Table S01 against the master table and annotations:

- **EU AI Act is counted twice** (D1060, a 2,206-word partial capture; D1291, the 97k-word full text). The paper notes "two captures" but still reports 7.
- **EO 14110 is coded `published_current` / `legally_binding`** (D0915), yet the corpus itself contains D0918, "Removing Barriers to American Leadership in AI" (EO 14148, January 2025), whose annotated summary says it revokes EO 14110. One of the seven binding instruments was repealed before the paper's date and the pipeline did not notice.
- **D0480, "Taiwan's Industrial Robot Hazard Prevention Standards (2025)"** is a 204-word capture whose annotation says: "The extracted text contains only page markers and a login notice ... The annotation relies on the title and URL", confidence 0.40, `pub_year` null; the 2025 date comes from the PDF-creation timestamp of the login page. The paper nonetheless lists it among "the newest instruments" (§5.5) and uses it to argue that new instruments "come from outside the traditional AI-governance centres". These Taiwanese standards were, as far as I know, promulgated decades ago and amended in 2018; the authors should check.
- **Two of the seven (D0915, D1060) were rated relevance = 1, "tangential"** by the annotator and enter the embodied set only because a category label was attached. Including them is a choice the set definition in §3.3 makes silently.

That leaves three or four binding instruments (Dubai AV law, El Salvador decree, the full AI Act, arguably the Argentine ministerial resolution creating a unit). The paper's claims that binding law reaches robots "through sector law ... not through robotics statutes" and "only the Salvadoran decree is a robotics statute" are then statements about four documents.

More fundamentally, the corpus does not contain the binding robot/vehicle/drone law a reader would expect: there is no document for the Korean Intelligent Robots Act (11 documents *mention* it in their titles; none is the instrument), no UK Automated Vehicles Act 2024, no German Autonomous Driving Act 2021, no EU drone rules (2019/947), no FAA Part 107, no EU Machinery Regulation 2023/1230 as a document, no Chinese humanoid guidance (MIIT 2023) or Shenzhen AI regulation (title searches of `title_en`). The world has dozens of binding AV and drone statutes. So "seven binding instruments", the instrument denominators of the gap index (Table 7), and the cumulative curve in Fig. 06 describe the collectors' reach, not the regulatory landscape, and the paper's §8 claim to give "the governance of embodied AI its first quantitative map" overreaches.

*What would resolve it:* manual verification of all 381 governance documents (status, binding nature, date, duplicates) by a person with legal training; a deliberate census of binding instruments for at least the AV, drone, industrial-safety and medical-device sectors in the top 20 jurisdictions, or a clear statement that binding counts are not analysed; removal of the duplicate and the stub; re-running Fig. 06, Table 7, Table 9/Fig. 23 and §5.5.

### W3. There is no human-coded ground truth, and the reliability numbers reported were computed on annotations that are not the ones analysed. (§4.2, §5.6, Table S09, Fig. 35)

- **No human coding anywhere.** The "independent model" is the same vendor's larger model, run on the same excerpt with the same prompt; its errors are not independent of the main annotator's. The cross-checks against collectors' labels (S10) are the only human signal, and they are weak where it matters: kappa 0.56 for sprint-vs-database against relevance, 0.33 for "Core" tier against `is_governance_document`.
- **Reliability was computed on pre-cleaning annotations.** `09_reliability.py` reads only `annotations/main`; `07_assemble.py` overrides 499 of those with `annotations/main_clean` (re-annotated after boilerplate removal). 54 of the 160 reliability documents are among the 499. On those 54, the pre- and post-cleaning principle scores agree at median kappa 0.78 (minimum 0.32), and across the 499 re-cleaned documents 15 changed embodied-set membership, 36 changed `doc_class` and 15 changed `is_governance_document`. The Opus run (15:19) also predates the cleaning (15:50). So the kappa of 0.89 describes a version of the data that the analysis does not use.
- **Rare classes are not validated.** The reliability sample has 4 binding instruments and 27 soft-law instruments; kappa on `binding_nature` and `instrument_status` is dominated by "not applicable" agreement and says little about the 63 embodied instruments the paper is about. Multi-label kappa drops labels with fewer than six positives, which removes exactly the rare mechanisms (insurance, licensing, incident reporting) that §5.3 reports as embodied-specific.
- **The lexicon validation is weaker than the abstract implies, and the described statistic is not what the code computes.** Document-level kappa between lexicon and annotation is 0.27–0.65 for principles (T18); the abstract foregrounds rho = 0.93, a rank correlation over 20 aggregate numbers. §4.3 and §5.6 say rho compares "the ranking of principles by annotated share with the ranking by lexicon share"; `15_analysis_C.py` computes `spearmanr(diff_ann, diff_lex)`, i.e., the correlation of embodied-minus-general *differences* across principles. Either is defensible; the text should say which.
- **The lexicon has a bug that the paper misdiagnoses.** `lex_military_laws` contains `\bLAWS\b` and `05_lexicons.py` compiles all patterns with `re.I`, so it matches the word "laws". That is why the lexicon fires on 29.1% of documents against 4.8% annotated (kappa 0.14) and why, among lexicon-positive documents, only 12% carry the military category. Report §9.2 attributes this to "passing references to autonomous weapons". The same column drives the "Autonomous weapons" panel of Fig. 33. The dual-use lexicon (`arma`, `weapon`, `defen[cs]e` without boundaries) has the same problem.
- **LLM labels are treated as error-free in downstream tests.** Every chi-square, V and logistic regression in §5 uses the labels as observed outcomes. With measurement error of the size shown in T18, standard errors and effect sizes are wrong in a known direction (Egami et al. 2023, "design-based supervised learning"; Angelopoulos et al. 2023, "prediction-powered inference").

*What would resolve it:* human double-coding by two domain coders of a stratified sample (at least 200 documents, including all 63 embodied instruments, all binding documents, and non-English documents in proportion), with human-vs-LLM kappa per field; recomputation of LLM-vs-LLM reliability on the final annotations; a second annotator from a different model family; corrected lexicons; and PPI/DSL-corrected estimates for at least the headline contrasts in Tables 8, 10 and 16.

### W4. Instruments are annotated from a 14,000-character excerpt, which cannot support "operationalisation" or mechanism coding of long legal texts. (§4.2, Fig. 23, Table 9, Table 10, §6 para 2)

The excerpt is the first 10,000 characters plus a 2,500-character middle slice and the last 1,500. From the master table, median excerpt coverage of governance documents is 38%; 148 of 381 are covered below 25% and 70 below 10%; the full AI Act capture is covered at 2.3%. Yet the codebook asks whether a principle is "a required element, a dedicated section" and which mechanisms the document "establishes, requires or recommends". For a statute, these live in the operative articles and annexes, not in the recitals that fill the first 10,000 characters. The "autonomy-level control is mentioned everywhere and operationalised nowhere" finding (§6, abstract) is exactly the kind of result an opening-pages excerpt would produce.

Separately, 20 of the 63 embodied instruments are landing or partial pages (7 landing, 13 partial), and of the 12 "technical standards" in Fig. 23, seven are ISO catalogue, committee or store pages ("ISO - Robotics", "ISO Store", "ISO/TC 299 Robotics", two of which are not even coded as governance documents) and three are partial captures; one (Israeli SI 395) is a substantive text. §7 says "three ISO catalogue pages". The claim that standards "specify physical safety substantively in 83.3%" (10/12; Wilson 55–95%) and are "the only type to operationalise human-robot proximity" is therefore based on catalogue abstracts, and the abstract's "the operative layer is technical standards" is unsupported by the texts the model actually saw.

*What would resolve it:* chunked full-text annotation with document-level aggregation for all governance documents; obtaining the standards' text (or dropping them from Fig. 23 and saying so); reporting coverage per document class; and a sensitivity analysis comparing excerpt vs full-text labels on the instruments.

### W5. Statistical methodology: effect sizes compared across non-comparable tables, unadjusted trend contrasts, small cells, and a clustering result that contradicts its own selection rule. (§4.4, §5.3–5.5, Tables 15–17, Fig. 31)

1. **"The largest regional effects are all mechanisms" (abstract, Table 15) compares Cramér's V across tables of different dimension and sample size.** Principle tests use embodied documents in 6 regions (n ≈ 640); mechanism tests use governance documents in 8 regions (n ≈ 370) with cells such as Oceania 0/15 (conformity), 1/15 (standards, funding), Africa 1/17. V is biased upward with small n and more rows (Bergsma 2013), no bias-corrected V or confidence interval is given, and chi-square is applied to tables with zero cells (the Fisher rule in `chi2_or_fisher` only triggers for 2×2 tables and uses observed, not expected, counts, contrary to §4.4). The headline "regions converge on principles and diverge on mechanisms" could be an artefact of this.
2. **"The core ethical principles do not differ significantly" (abstract) is selective.** In Table 15, five of the 14 core principles are Holm-significant across regions (human oversight, robustness, inclusive growth, trust, dignity); the sentence holds only for the five the text names.
3. **Table 16 (topic change) is unadjusted for genre, while Table 17 is adjusted and disagrees.** In the embodied set the research share falls from 82% (2020–24) to 69% (2025–26) while news rises 7→12%, soft law 4→6%, grey literature 1→3% (master table). A shift toward "industrial policy" and away from "ethics principles" is what a genre shift produces. The adjusted trend models (Table 17) find no trend for physical safety, proximity, liability or autonomy level; the paper reports both tables as evidence of a discourse turn.
4. **k-means bundles (§5.3, Table 11).** Silhouette 0.18 indicates essentially no cluster structure. Re-running the script's own loop with k = 2 gives silhouette 0.189 > 0.183 for k = 3; the code searches k = 3..6 while the supplement says 2..6. The three-bundle narrative therefore does not follow from the stated rule.
5. **Regional distances (Fig. 31)** have no uncertainty; Oceania (n = 16) and the Middle East (n = 37) are placed in the dendrogram with the same confidence as Europe (n = 382); the paper says regions with < 20 embodied documents were excluded, the code uses ≥ 15. Cosine distance on concatenated prevalence vectors is dominated by the high-prevalence shared items, which mechanically makes Europe–US "nearly identical (0.012)".
6. **The gap index (Table 7, Fig. 18) has no interval.** Social robots among instruments is 2/63 (Wilson 0.9–10.9%); autonomous vehicles 29/63 (34–58%). Several rows rest on 0–3 instruments.
7. **Dates.** 389 documents are dated by the annotator "from content" and 56 are unknown; the "embodied AI / physical AI in a tenth of 2026 documents" claim is 28 of 289 documents, 83 of which are content-dated by the same model that reads the vocabulary. A document is dated 2027.
8. **Fisher/chi-square description** in §4.4 ("expected counts below five") does not match the code.

*What would resolve it:* bias-corrected V with bootstrap CIs computed on the same population for principles and mechanisms; genre-adjusted (or research-only) topic-change models; CIs on the gap index; permutation tests for the region distances; either dropping k-means or searching k ≥ 2 and reporting that structure is weak; date-source sensitivity for every trend; and a corrected Methods description.

### W6. Novelty and positioning: no engagement with existing governance-document datasets or robot-law corpora, and "bibliometric" is not delivered. (§1, §2, §8, title)

- The paper cites no prior *dataset* of AI governance documents against which to position itself, although several exist and some already include robotics: the OECD.AI Policy Observatory (1,000+ policies), AlgorithmWatch's AI Ethics Guidelines Global Inventory, the Stanford AI Index legislation tracker, the IAPP Global AI Law and Policy Tracker, JRC's AI Watch, Digital Policy Alert. Without a comparison, "first quantitative map" (§8) is unsupported and the reader cannot judge coverage.
- Robot-law scholarship with explicit regulatory mapping is missing: the RoboLaw project (Palmerini et al. 2014 "Guidelines on Regulating Robotics"), Nevejans (2016, European Parliament study), Bertolini (2020, EP study on AI and civil liability), Fosch-Villaronga & Mahler (2021, cybersecurity/safety of robots under EU law), the AV regulation reviews (e.g., Taeihagh & Lim 2019), drone-regulation surveys (Stöcker et al. 2017), BS 8611 and IEEE 7001. Several of these are, in effect, hand-coded versions of what the paper automates and would be natural baselines.
- The LLM-annotation literature is reduced to two citations; the works that set the validation bar the paper should meet are absent (Pangakis, Wolken & Fasching 2023; Törnberg 2024; Reiss 2023 on instability; Ollion et al. 2024 on proprietary models; Egami et al. 2023; Angelopoulos et al. 2023).
- The title promises a bibliometric analysis. There is none in the paper: OpenAlex matched 374 of 582 research outputs, the median citation count is 1, there is no citation, co-authorship, venue or country-collaboration analysis, and the only bibliometric table (venues, T05) is in the supplement.

*What would resolve it:* a related-datasets paragraph with a coverage comparison (how many of OECD.AI's robotics-tagged instruments are in the corpus?); engagement with the robot-law mapping literature; either real bibliometrics or a different title.

### W7. Abstract claims checked against the results

| Abstract claim | Status |
|---|---|
| 1,703 unique documents, 1,589 usable, 110 jurisdictions | Counts reproduce. "110 jurisdictions" counts any document's country including first-author affiliation of papers; only 65 countries have a governance instrument, 26 an embodied one, 16 a binding one; 17 appear only through research papers. Title and abstract overstate governance coverage. |
| 39-field codebook, LLM under fixed prompt | Reproduces (one model, one prompt hash). |
| Median kappa 0.89 over 46 fields; test-retest 0.95 | Numbers reproduce but were computed on pre-cleaning annotations (W3). |
| rho 0.93 for principle rankings | Code computes the correlation of embodied-minus-general differences, not rankings of shares (W3). Document-level kappa is 0.27–0.65. |
| 674 / 63 / 7 vs 859 / 301 / 29 | Reproduces; 7 includes a duplicate, a repealed order and a login-page stub (W2); ratio is the collection design (W1). |
| Binding layer via sector law and AI Act, "not through robotics statutes"; operative layer is standards | Rests on 3–4 documents and on catalogue pages (W2, W4). |
| Social robots 43% of research vs 3% of instruments; AVs 12% vs 46% | Reproduces; instrument shares are 2/63 and 29/63 with wide intervals (W5.6); the instrument population is incomplete (W2). |
| Embodied harm-avoidance principle profile; general-AI socio-economic profile | Embodied-specific principles reproduce and are credible; the core-principle differences are largely genre (W1). |
| "Largest regional effects are all mechanisms (V 0.26–0.34)"; "core ethical principles do not differ" | V not comparable across tables; 5 of 14 core principles are significant (W5.1–2). |
| Europe/US/Oceania cluster; Middle East and international distinct | Reproduces as descriptive; no uncertainty; Oceania n = 16 (W5.5). |
| 2025–26 shift to industrial policy, oversight, cybersecurity, risk tiers, conformity, humanoids, logistics | Risk tiers and conformity are not Holm-significant in Table 16 (p_holm 0.13, 1.0); the shift is unadjusted for genre (W5.3); humanoid/logistics claims come from Fig. 14, not shown in the paper. |
| "embodied AI"/"physical AI" in a tenth of 2026 documents | 28/289; 2026 is partial and partly content-dated (W5.7). |
| Autonomy-level control "mentioned everywhere and operationalised nowhere" | Excerpt artefact risk (W4). |

### W8. Reproducibility of the annotation step is partial. (§4.2, supplement S1, Appendix)

Model identifiers are given without snapshot dates or version strings; the `--effort` setting is unspecified; annotation ran through an interactive CLI rather than an API with pinned parameters; the released package (`package_stage2.sh`) does not include the converted texts (`registry.text_path` points to `/home/user/drive-md-out/...`, outside the package), so neither the annotation nor the lexicon step can be re-run from the release; there is no README, LICENSE, environment file or datasheet; the MinHash threshold (0.65) missed the AI Act duplicate; the stochastic re-annotation of 499 documents means the main annotation is a mixture of two runs.

### W9. Ethical and licensing considerations are not addressed. (none in paper)

The corpus includes paywalled journal articles, news articles, bot-walled pages and 34 "permission-restricted" Drive files recovered through a document reader; copyrighted full texts were sent to a commercial API; the release includes per-document summaries and key provisions derived from them. No statement on redistribution rights, source licences, terms-of-service compliance, dataset licence, or a datasheet (Gebru et al. 2021) is provided. The collection teams' protocol and credit are not described. The reliability sample is 75% English and no analysis asks whether the model codes non-English or Global-South documents differently (the non-English subset in T19 behaves quite differently: 21% embodied, top category humanoids), which is a fairness question for a dataset that will be used to characterise regions.

### W10. Writing and presentation. (whole paper)

- Length and density: ~9,000 words plus five full-width tables in the main text; Table 15 has 38 rows and 7 columns, Tables 8 and 10 have 11 and 8 columns. The paper reads as an abridged report rather than a conference paper.
- Figure and table numbers are inherited from the report and are non-sequential (Figures 01, 05, 06, 07, 11, 18, 20, 23, 24, 31, 34; Tables 07, 08, 10, 15, 16, 17), which confuses cross-reference.
- The paper does not stand alone: regional profiles ("are in the report and supplement"), the category-by-period results, the stance figure, the instrument lists and the sensitivity table are all referred to but not shown.
- Internal inconsistencies: 10 technical standards and 37 soft-law instruments in §5.1 vs n = 12 and n = 33 in Fig. 23/§5.3 (different operationalisations in `14_analysis_B.py`); "regions with fewer than 20 embodied documents excluded" vs ≥ 15 in code; Fisher rule in §4.4 vs code; k range 2–6 (supplement) vs 3–6 (code); "three ISO catalogue pages" vs seven landing pages.
- Fig. 23: x-axis labels overlap; the "Proposals/drafts" and "Technical standards" bars for conformity assessment reverse the paper's narrative and are not discussed.
- Models used are not in the reference list; "Claude Sonnet 5.5" has no citation or card.

## 4. Questions for the authors

1. What were the collectors' instructions and search strategy for the sprint and database exercises, and were they the same across the eight teams? Can you show that any embodied-vs-general contrast survives when comparing within `collection_set`?
2. Please confirm the status of each of the seven binding documents: is the AI Act meant to be counted twice; is EO 14110 "in force" given D0918 in your own corpus; what is the actual promulgation/amendment date of Taiwan's Industrial Robot Hazard Prevention Standards; and what is "Decree No. 340 – Robotic Technologies Law" of El Salvador (we could not verify it)?
3. Why does the corpus contain no binding AV or drone statute from the UK, Germany, Japan, the EU (2019/947) or the US, and no document for the Korean Intelligent Robots Act, when §2.2 presents these as the reference points? Does this reflect the collectors' remit or capture failures?
4. Were the reliability statistics (Table S09, Fig. 35) recomputed after the 499-document re-annotation? If not, what are they on the final annotations, and what is the human–LLM kappa on any subset?
5. How were the 160 reliability documents sampled (simple random, stratified)? How many binding instruments and non-English documents does the sample contain per field being validated?
6. Was the `\bLAWS\b` / `re.I` interaction in the military lexicon known? After fixing it, do the Fig. 33 "autonomous weapons" trend and the T18 row change?
7. §4.3 and §5.6 describe rho = 0.93 as a correlation of principle rankings; the code correlates embodied-minus-general differences. Which is intended, and what is the other value?
8. Why were principle divergence (6 regions, embodied documents) and mechanism divergence (8 regions, governance documents) tested on different populations, and can you provide bias-corrected V with confidence intervals on a common population?
9. Does the 2025–26 topic shift (Table 16) persist within research outputs only, or after adjusting for `doc_class` as Table 17 does?
10. With k = 2 scoring higher on silhouette than k = 3, and all silhouettes below 0.2, what is the basis for the three mechanism bundles?
11. What `--effort`/sampling settings were used, what model snapshot dates, and can the converted texts (or at least URLs with content hashes and the cleaned excerpts) be released so the annotation step can be reproduced?
12. What are the redistribution terms for the captured documents, and under what licence is the dataset released?

## 5. Minor issues, typos and presentation nits

- Title: "across 110 jurisdictions" (see W7); "bibliometric" (see W6).
- Abstract: "Reliability was assessed against an independent model" — the second model is from the same family under the same prompt; say "a second model".
- §3.1: "1,894 were captured as files (2,557 files in total ...)" — clarify that 2,557 counts formats, not sources.
- §3.2: "Duplicates were resolved ... yielding 1,703 canonical documents" — note that the AI Act survived as two documents.
- §3.3: the embodied set includes 120 documents rated relevance ≤ 1 (two of them binding instruments); state this and justify.
- §3.3: 27 `general_ai_with_embodied_provisions` documents sit in the *general* set because they carry no category label; by the codebook's definition they contain robot provisions. Explain.
- §4.1: "39-field codebook" — supplement S2 header says "v1.0"; give a version and date and say whether the codebook changed after the test batch (`annotations/test`, 8 documents).
- §4.2: give the exact excerpt rule in words (first 10,000 characters *after cleaning*, middle 2,500, last 1,500) and the share of documents truncated.
- §4.4: "Fisher's exact test where expected counts are below five" — code uses observed counts, 2×2 only.
- §4.4: "regions with fewer than 20 embodied documents excluded" — code: fewer than 15.
- §4.4: state the k range for silhouette selection; it differs between supplement (2–6) and code (3–6).
- §5.1: "7 are legally binding, 37 voluntary soft law, 10 voluntary technical standards and 9 of inapplicable binding nature" sums to 63; Fig. 23 uses 7 / 33 / 12 / 12. Reconcile.
- §5.1: "Regulators and agencies author 116 general-AI documents and 9 embodied ones" — add denominators.
- §5.1: "Non-English documents are more often instruments (34.6% vs 21.0%)" — this is a property of the database exercise (which collected instruments) and language, not a finding about languages.
- §5.2: Table 7 should carry Wilson intervals, at least for `instrument_pct`.
- §5.2: "Sex robots (23 papers)" — `category_any` gives 24 and Table 7 gives 23 (research only); say which.
- §5.3: "Seventeen of twenty principle differences survive Holm correction" — with n ≈ 1,500, almost any difference will; report effect sizes (Cramér's V or risk ratios) alongside.
- §5.3: the mechanism cluster "examples" column in Table 11 lists Brazilian bills on Marco Civil and the Penal Code as the "light-touch standards-referencing bundle"; this suggests the clusters are not interpretable.
- §5.3: "Rights-based framing never exceeds 14.8%" — of what?
- §5.3: "The legal-personhood question is discussed in 156 documents" — this is across all usable documents, not the embodied set; say so.
- §5.4: "Europe and the United States are nearly identical (0.012)" — add that the vectors are 54-dimensional prevalence profiles and that no test is performed.
- §5.5: "humanoid vocabulary peaks in density in 2025" — Fig. 33 is not in the paper.
- §5.5: "The newest instruments ... (El Salvador, Dubai, Argentina, Taiwan)" — Taiwan date is a PDF timestamp.
- §5.6: "41 fields above 0.80" — 0.80 is an informal Landis–Koch threshold; present the distribution.
- §5.6: the sensitivity paragraph says social robots remain the top category "except where the regional findings predict otherwise"; the database-only subset (top category AVs) is not a regional finding.
- §6 para 3: "after two decades of research they have seven instruments among them" — Table 7 gives 2 + 1 + 0 + 4 = 7 for social/educational/sex/domestic; care robots have 16; state the categories.
- §6 para 3: "the GDPR is the instrument most cited for them" — not shown anywhere in the paper.
- §7: "Three ISO catalogue pages" — seven landing pages among the 12 standards.
- §7: a document is dated 2027 (D1462).
- Figures: numbering (W10); Fig. 23 overlapping x-labels; Fig. 18 would benefit from intervals; Fig. 31 colour bar label is rotated and small; Fig. 35 is a full page for one number.
- Tables: Table 15 should be a figure or move to the appendix; drop `p` when `p_holm` is shown; round to two decimals.
- References: add model cards; "ISO 10218-1 and -2 (2011, revised 2025)" — check; Korea Act No. 9014 — the Act is usually cited as Act No. 8865 (2008) with later amendments, please verify.
- Author line: "analysis prepared with Claude Code" — fine, but then the annotation model and the analysis assistant are the same vendor; disclose in a contributions/AI-use statement.
- Supplement S1 says "silhouette over 2 to 6"; code says 3 to 6.
- `codebook.md` decision rule 3 says catalogue pages are `technical_standard` with `landing_or_index_page`; the paper should then never treat them as texts that "specify" anything.

## 6. Scores

- **Soundness: 2 (fair).** The central comparison is confounded by design, the binding-instrument layer is partly wrong on inspection, reliability was computed on superseded annotations, and several effect-size comparisons are statistically invalid.
- **Presentation: 2 (fair).** Clear prose, but the paper is an abridged report: over-long, table-dense, non-sequential figure numbers, dependent on external documents, and internally inconsistent on several n's and method descriptions.
- **Contribution: 2 (fair).** The codebook, embodied taxonomy and pipeline are useful and reusable; the corpus is not a frame from which the headline conclusions follow, and there is no human ground truth, which for a datasets-and-benchmarks submission is the main deliverable.
- **Overall: 3 (reject).** The question is good and the engineering is careful, but the paper's stated findings about how embodied AI is governed in the world are, on the evidence in the authors' own files, findings about how two collection exercises were run and how one model reads the first 10,000 characters of a document. The specific errors in the seven binding instruments, the reliability computed on the wrong annotations, and the absence of any human coding mean I cannot recommend acceptance in this form. A revised version that documents the frame, verifies the instruments by hand, adds human-coded ground truth and restricts claims to within-genre comparisons could be a strong D&B paper.
- **Confidence: 4.** I read the code and re-ran checks on the released data; I did not re-annotate documents or verify every instrument against primary legal sources.

## 7. Ten changes that would most raise the score (prioritised)

| # | Change | Effort | New data / annotation? |
|---|---|---|---|
| 1 | Human double-coding of a stratified sample (≥ 200 documents: all 63 embodied instruments, all binding, non-English in proportion) by two domain coders; report human–LLM kappa per field and use it to correct downstream estimates (PPI/DSL). | 60–100 h | Yes (human annotation) |
| 2 | Manual verification of all 381 governance documents: status, binding nature, date, duplicates; remove the AI Act duplicate, the EO 14110 "in force" coding and the Taiwan stub; re-run Fig. 06, Tables 7, 9, 10 and §5.5. | 30–40 h | Light (legal lookups) |
| 3 | Document the collection protocol and reframe all embodied-vs-general comparisons within genre (instrument vs instrument, research vs research) or stratified by `collection_set`; rewrite abstract and §6 para 1 accordingly. | 15–20 h | No |
| 4 | Full-text (chunked) annotation of all governance documents, and acquisition of the standards' text or their removal from Fig. 23; report excerpt-vs-full-text sensitivity. | 20 h + API cost | Yes (re-annotation) |
| 5 | Recompute LLM–LLM reliability on the final annotations; add a second annotator from a different model family; report rare-class reliability for binding/status/mechanisms. | 10–15 h + API cost | Yes (re-annotation of 160 docs) |
| 6 | Fix the statistics: bias-corrected Cramér's V with bootstrap CIs on a common population for principles and mechanisms; genre-adjusted topic change; CIs on the gap index; permutation test for regional distances; k ≥ 2 or drop k-means; date-source sensitivity for trends; correct the Fisher description. | 10–15 h | No |
| 7 | Fix the `\bLAWS\b`/`re.I` and unbounded dual-use lexicon bugs, re-run T18/Fig. 33, and state correctly what rho = 0.93 measures. | 3 h | No |
| 8 | Add related-datasets and robot-law positioning (OECD.AI, AlgorithmWatch inventory, IAPP tracker, RoboLaw, Nevejans, Bertolini, AV/drone regulation surveys) with a coverage comparison; either deliver bibliometrics or change the title. | 8–10 h | Light (coverage comparison) |
| 9 | Release package: README, LICENSE, datasheet, model snapshot IDs and settings, environment file, converted texts where licensed (otherwise URLs + hashes + cleaned excerpts), and an ethics/licensing statement. | 8 h | No |
| 10 | Cut to venue length; sequential figure/table numbering; move Tables 8, 10, 15 to the appendix with compact summaries; reconcile all inconsistent n's; include the regional profiles and sensitivity table the text relies on. | 10 h | No |
