---
title: "Governing machines that act in the world: analysis report (v2)"
subtitle: "How embodied AI and robotics are governed, from 1,656 documents in eight world regions, after six independent adversarial reviews"
author: "Prepared with Claude Code for Jimmy Lin, Centre for Enterprise Innovation (CEI) AI Robotics project"
date: "31 October 2026"
---

## Key numbers

| | |
|---|---|
| Files collected by eight regional teams | 2,557 (1,894 of 2,160 listed sources captured) |
| Unique documents after deduplication and corrections | 1,656 (46 duplicates merged after review) |
| Usable documents (text readable, on topic) | 1,538 |
| About robots or embodied AI ("embodied-AI set") | 675 (508 research papers, 65 rules and policies) |
| About AI in general ("general-AI set") | 806 (50 research papers, 261 rules and policies) |
| Rules and policies that reach robots | 65: 34 robot-specific, 31 general-AI instruments with robot provisions |
| Legally binding and in force, reaching robots | 4 in this collection (El Salvador 2025, Dubai 2023, Argentina 2024, EU AI Act 2024); one further executive order revoked |
| Countries with any document / with an instrument / with a binding instrument | 110 / 65 / 17 |
| Share of documents from Europe / in English / in Chinese | 43% / 79% / 0.5% (7 documents) |
| Labelling | AI model under a fixed 39-field codebook; no human coding; four reliability checks (see Part F) |

**How to read this report.** Everything was labelled by a language model, so the labels are consistent across models and re-runs but not certified by human coders. The collection sought research on robots and official texts on AI in general, so comparisons between the two sets are made within document genre or adjusted for it wherever they matter. Counts of instruments are counts *in this collection*, which an audit shows is missing several known binding laws; they are lower bounds. Percentages are given as counts wherever a group has fewer than 30 documents. Plain-language definitions are in the glossary at the end; the full codebook and every supporting table are in the supplement.

## Five findings

1. **Robots are governed by voluntary guidance and standards; binding law reaches them through sector and general-AI law, not robotics statutes.** Of 65 rules and policies that reach robots, 44 are voluntary guidance, 8 are technical standards, 8 are proposals and 5 are binding. The binding ones are a general robotics statute (El Salvador), a vehicle law (Dubai), a security-ministry resolution (Argentina), the EU AI Act, and a revoked United States executive order. (Figures 4 and 6; Tables 2 and 33b.)
2. **Research and rules point at different robots.** Companion and social robots are the subject of 43% of robot research papers but 4 of the 65 instruments; self-driving vehicles are 12% of research and 66% of instruments (43), industrial arms 10% and 46%, drones 6% and 34%. These gaps are far outside their bootstrap intervals. Humanoids have 141 documents, 9 policy papers, one bill and no binding law. (Figures 18 and 40; Tables 7 and 22.)
3. **What is distinctive about robot governance is the body, and it survives the genre confound.** Physical safety, human-robot proximity, liability for physical damage, autonomy-level control, conformity assessment and dual use are raised far more often in robot documents than in general-AI documents of the same type (adjusted odds ratios 4 to 166). Differences on the ethical core mostly vanish once genre is accounted for: only transparency and fairness remain lower, and accountability is lower, not equal. Among instruments, robot rules refer to standards (72% vs 36%), testing (60% vs 33%) and conformity assessment (32% vs 12%); general-AI rules rely on audits, labelling and data governance. (Figures 20, 24, 38, 39; Tables 20, 21, 34.)
4. **Specification lags mention.** Technical standards set out physical safety in detail; binding rules do so in two of five cases; voluntary guidance in one of fourteen. Autonomy-level control is raised by 43 to 70% of instruments of every type and set out in detail by one binding rule in five and one voluntary guideline in twenty, even after re-reading every governance document from up to 110,000 characters of text. (Figure 23; Tables 9 and 35.)
5. **Regions agree on values and differ on liability and control; the newest shift is toward cybersecurity.** On a common population, the ethical core does not differ by region, while liability for physical damage, human oversight, autonomy-level control, physical safety and the use of liability regimes and standards references do (bias-corrected V 0.19 to 0.33). Europe and North America are indistinguishable; the Middle East and the standards layer stand apart. Between 2020 to 2024 and 2025 to 2026, after adjustment for genre and region, cybersecurity rises (odds ratio 2.7) and legal personhood falls (0.38); human oversight rises at the margin; the apparent turn to industrial policy is a change in document mix. Risk-based tiering and conformity assessment grow about 30% per year in robot documents; humanoids and "embodied AI" vocabulary surge in 2025 to 2026. (Figures 21, 25, 29 to 34, 42; Tables 28 to 31.)

## 1. Scope, questions and definitions

The brief asked for a metric-heavy analysis of AI governance in the context of robotics, physical AI and embodied AI: development over time, regional differences, dominant views and principles, the newest trends, and how different robot types are governed, with a taxonomy of robots, a taxonomy of documents (including governance-instrument status) and a document dashboard. Version 1 delivered these; six independent adversarial reviews (data science, AI research, conference reviewing, journalism, AI governance and law, visualisation) found the discourse-level findings defensible and the instrument-level and reliability claims not. Version 2 corrects the data, restricts every embodied-versus-general comparison to within-genre or adjusted estimates, re-annotates every governance document from much longer text without the collectors' labels, repairs the statistics and the lexicons, and rewrites the claims. The review log maps every finding to a change.

Definitions used throughout:

- **Usable documents** (1,538): annotated documents with readable text that are neither failed captures nor off-topic.
- **Embodied-AI set** (675): usable documents rated at least moderately relevant to embodied-AI governance (2 or 3 on a 0 to 3 scale) or carrying at least one robot-type label; 550 by relevance alone, 125 by category label alone. A strict definition (relevance only) is reported as a sensitivity.
- **General-AI set** (806): usable documents rated 0 or 1 with no robot-type label; 57 further documents are off-topic.
- **Rules and policies** ("governance instruments", 326 usable): statutes, regulations, decrees, strategies, guidelines, codes, standards, resolutions and consultations, with a lifecycle status and a binding nature. Government and parliamentary reports (112) are counted separately. **Robot-specific instruments** are those rated relevance 2 or 3 (34); **general-AI instruments with robot provisions** are rated 0 or 1 but carry robot-type labels (31).
- **Regions** follow the issuing jurisdiction (first author's country for research; Europe for EU bodies; International for ISO, IEC, IEEE, UN, OECD, UNESCO and WHO): Europe (including Russia), Asia, North America (United States, Canada, Greenland), Latin America and the Caribbean, Middle East, Africa (including Egypt and the African Union), Oceania, International.
- **Content-analysed captures** are substantive or partial captures; catalogue, committee and landing pages count in the instrument inventory but are excluded from statements about what instruments say.

## 2. Data and methods in brief

The full pipeline is in the supplement (S1). In outline: the eight regional teams listed 2,160 sources and captured 1,894 as 2,557 files; files were converted to text, deduplicated (hash, URL, title, prefix and prose similarity, then a second pass on normalised title and jurisdiction after review), and every document was annotated by Claude Sonnet 5.5 against a 39-field codebook as a fixed system prompt with a JSON schema. In version 2 every governance document was re-annotated with the collectors' cover block stripped, minimal metadata and up to 110,000 characters of text (first 100,000, a 6,000-character middle slice and the last 4,000), which covers 74% of governance documents in full (median share of text seen 1.0, against 0.36 in version 1). Forty-six documented field corrections and 46 duplicate merges from the reviews were applied through a versioned override file. Reliability was measured five ways: a second model on the same excerpt (160 documents), the same model re-run (161), the same model on the full text (160), the same model with the collectors' labels removed (160), and the extended re-annotation against the original for governance documents (351). Full-text keyword lexicons, repaired after review, provide a model-free check. Statistics use Wilson intervals; chi-square tests with Monte-Carlo p-values for sparse tables and Fisher's exact test for sparse 2 by 2 tables; bias-corrected Cramér's V with bootstrap intervals; Holm correction within each family; logistic regression adjusting for document class, region and year; Mantel-Haenszel tests stratified by class; bootstrap intervals for the governance-gap index and for regional distances, with split-half noise floors.

## 3. Part A. The document landscape

{{F01}}

The embodied-AI set is three quarters research papers (508 of 675) and three quarters academic in origin (514 issuers); the general-AI set is 47% news, web pages and press releases and 22% voluntary guidance, with 50 research papers. The split mirrors the collection design (a sprint for robot-specific sources that drew on academic literature; a database of general-AI instruments), which is why every comparison in Parts C and D is made within genre or adjusted for it.

{{T01}}

{{F03}}

Regulators and agencies issue 109 general-AI documents and 10 embodied ones; legislatures 58 and 14. The institutions that will apply robot rules are present mainly as authors of general-AI rules.

### 3.1 Instruments: lifecycle and binding nature

{{F04}}

{{T02}}

Of the 65 instruments that reach robots, 45 are published and current, 5 in force, 4 drafts or bills, 4 superseded (the 2021 AI Act proposal texts), 3 open consultations and 2 proposals; 44 are voluntary guidance, 8 technical standards and 5 legally binding (8 drafts have no binding nature yet). The general-AI pipeline is more legislative: 34 bills under consideration, 26 open consultations, 26 in force, 23 binding. The binding share of instruments with a settled nature is similar in the two sets (5 of 57 vs 25 of 220; chi-square p = 0.11), so the difference is in volume, not in the propensity to legislate.

{{T33}}

{{T33b}}

Table 33 splits the 65 by tier and capture quality. The 34 robot-specific instruments are 4 binding, 24 voluntary and 6 drafts; 9 of the 24 voluntary ones are partial or catalogue captures. The 31 general-AI instruments with robot provisions are mostly national strategies and guidelines that list vehicles, drones, surgical or industrial robots as examples or as Annex items. Table 33b lists the binding five: the Salvadoran Robotic Technologies Law (relevance 3), the Dubai autonomous-vehicle law (3), the Argentine security-unit resolution (2, an internal organisational act), the EU AI Act (2, reaching robots through its product lists) and Executive Order 14110 (1, revoked January 2025).

{{F06}}

Figure 6 accumulates dated instruments. Voluntary guidance grows from 1 in 2014 to 44 in 2026; technical standards from ISO 13482 (2014) to 7 with a known year; binding instruments appear from 2023 (Dubai, the executive order), 2024 (AI Act, Argentina) and 2025 (El Salvador). Two cautions: the Taiwanese industrial-robot hazard rules (1987, amended 2018) and the Taiwan AI Basic Act (2026) exist but were captured only as login stubs and are excluded; and the coverage audit (Part F) shows that the collection lacks several older binding instruments for vehicles, drones and industrial robots, so "binding law from 2023" describes the collection, not the world.

### 3.2 Development over time

{{F02}}

{{F05}}

The collection is recent: a tenth of documents date from 2019 or earlier, the median is 2024, and 41% date from 2025 or later (2026 to October). The embodied share of each year's documents falls from above 60% before 2023 to 31% in 2025 (logistic odds ratio 0.80 per year), because general-AI strategies and AI Act material flood in; absolute embodied counts rise every year (65 in 2022, 97 in the first ten months of 2026), and embodied instruments arrive at 6 to 10 per year from 2020.

{{T03}}

Table 3 dates each robot type's entry. Industrial manipulators have the oldest governance text (Israel's SI 395, 1993); care, companion and professional service robots enter governance in 2014 to 2017 (ISO 13482; the Civil Law Rules on Robotics); vehicles and drones in 2014; humanoids in 2017. The youngest entries are educational and delivery robots; biohybrid systems and toy robots have research attention and no instrument. Median years show where attention is now: mobile logistics robots (2025), humanoids and surgical robots (2024).

### 3.3 Geography and language

{{F07}}

Europe supplies 664 usable documents (43%), of which 383 are embodied (58%); Asia 258 (106 embodied); North America 160 (83); Latin America and the Caribbean 128 (16); the Middle East 86 (35); the international layer 140 (24); Africa 61 (12); Oceania 40 (16). The embodied share varies strongly by region (Cramér's V 0.33): Europe and North America contribute embodied documents through research; Latin America, Africa and the international layer contribute general-AI instruments.

{{F08}}

{{T04}}

Across 110 countries with any document, 65 contribute an instrument, 17 a binding instrument and 12 a robot-specific instrument. No country has more than five robot-specific instruments (United States 5; United Kingdom, Japan and China 4). The United Kingdom (141 documents) and the United States (128) lead on documents because of their research output; counts measure the collectors' reach as much as national activity, and the collection's largest blind spot is China: 33 documents, 7 in Chinese.

{{F10}}

{{T05}}

English is 79% of usable documents; Spanish (91), Portuguese (41), French, Korean, Arabic, Russian and Japanese follow. Non-English documents are more often instruments (33% vs 19%) and, among instruments, more often binding (14% vs 9%): the multilingual legal record and the English research literature are different populations. Research venues are robot-ethics venues (International Journal of Social Robotics, Frontiers in Robotics and AI, Ethics and Information Technology, the Robophilosophy volumes, AI & Society); median OpenAlex citations are 1.

## 4. Part B. What is governed

{{F11}}

{{F12}}

{{F13}}

{{F14}}

Companion and social robots are the most addressed type (230 documents, 34% of the embodied set), then care robots (174), humanoids (142), autonomous road vehicles (134), professional service robots (132), industrial manipulators (114), surgical robots (108), military weapons (83), drones (70) and collaborative robots (67). Regions attend to different machines (Figure 12): social robots are a European (43%) and North American (37%) topic; humanoids lead in the Middle East (29%) and Asia (26%); surgical robots in the Middle East (43%); industrial manipulators in the international standards layer (38%). Genres attend to different machines (Figure 13): research is social-robot heavy (43%); voluntary guidance mentions vehicles (62%) and industrial arms (44%); drafts mention vehicles in 8 of 10. Over time within the embodied set (Figure 14, Figure 42): social robots fall from 42% of documents in 2020 to 2022 to 26% in 2025 to 2026; humanoids rise from 17% to 29%; mobile logistics robots from 3% to 14%; vehicles fall from 27% to 14%.

{{F16}}

{{T06}}

{{F17}}

Companion and care robots co-occur in 111 documents (Jaccard 0.38); vehicles, arms and drones co-occur in the lists that instruments enumerate (lifts 2.2 to 3.7); topics form two poles, ethics with human-robot interaction and physical safety with liability, standards and oversight (Figure 17).

{{F18}}

{{F40}}

{{T22}}

The governance-gap index (research share minus instrument share) with bootstrap intervals (Table 22) separates three groups. Studied far more than governed: social and companion robots (+37 points, interval 29 to 44; 4 instruments, none binding). Near parity: humanoids (+9, interval includes zero), care robots, domestic and educational robots. Governed far more than studied: autonomous road vehicles (−54, interval −66 to −42; 43 instruments, 4 binding), industrial manipulators (−36), drones (−28), agricultural and logistics robots (−16 and −15), collaborative, surgical and military robots (−12, −12, −10). The pattern has an explanation: vehicles, arms, drones and medical robots inherited product-safety, transport, aviation and medical-device regimes that AI strategies now reference, whereas social robots raise questions (deception, attachment, dignity, vulnerable users) without a regulatory home of their own. The governance expert's review notes that general regimes (the AI Act's transparency and vulnerability provisions, product-safety and toy rules, data protection) do apply to them; the gap is in robot-specific instruments, not in the absence of any law.

{{F19}}

Embodied documents are sectoral (health 45%, manufacturing 22%, elder and social care 20%, logistics 20%); general-AI documents are cross-cutting (73%) and about public administration (48%).

## 5. Part C. How robots are governed: principles, tools, framings

### 5.1 Principles: pooled, stratified and adjusted

{{F20}}

{{T08}}

Pooled over all documents, 17 of 20 principle differences between the sets survive Holm correction. Pooled comparisons are, however, mostly comparisons of genres. Three further analyses settle what survives.

{{F39}}

{{T21}}

Within governance instruments (65 vs 258), the six embodied-specific considerations differ sharply: physical safety 60% vs 7%, autonomy-level control 49% vs 11%, human-robot proximity 40% vs 0.4%, conformity assessment 59% vs 18%, dual use 35% vs 10%, liability for physical damage 23% vs 1% (all Holm-significant); none of the 14 core principles differs significantly. Within research papers (508 vs 50), the same six differ, inclusive growth is lower in robot papers (22% vs 52%) and no other core principle differs.

{{F38}}

{{T20}}

{{T34}}

Adjusting for document class, region and year (Table 20), the embodied-specific considerations keep very large odds ratios (physical safety 63, proximity 166, liability 87, autonomy-level control 13, dual use 5, conformity 4). Among core principles only transparency (0.49) and justice and fairness (0.47) remain significantly lower in embodied documents; the Mantel-Haenszel analysis stratified by class (Table 34) adds accountability (0.63), inclusive growth (0.57) and non-maleficence (1.76). The v1 claim that accountability "does not differ" was a Simpson's paradox: it is lower within every genre.

{{F21}}

{{F22}}

By region (Figure 21), the core looks alike everywhere; liability for physical damage runs from 8% (international) to 63% (Middle East), human oversight from 29% to 77%, autonomy-level control from 31% to 77%. By class (Figure 22), in-depth treatment follows function: drafts operationalise transparency, accountability and conformity (the AI Act pipeline), strategies inclusive growth, research proximity and accountability.

### 5.2 Operationalisation of the embodied-specific considerations

{{F23}}

{{T09}}

{{T35}}

After the extended, blind re-annotation of every governance document (Table 35: mechanisms per document rose from 4.9 to 5.6, robot types from 0.4 to 0.7, named instruments from 1.3 to 1.8; binding and in-force labels changed for fewer than 5% of documents), Figure 23 and Table 9 show which document types move the six considerations from mention to specification. Technical standards specify physical safety in depth in every content-captured case and proximity in half; binding instruments specify physical safety in 2 of 5, conformity assessment in 3 of 5 and liability in 2 of 5; voluntary guidance mentions physical safety in 45% and specifies it in 7%; drafts mention it in 8 of 10 and specify it in 1. Autonomy-level control is mentioned by 43 to 70% of every instrument type and specified in depth by 1 of 5 binding instruments, 1 of 10 drafts, 2 of 42 voluntary instruments and no standard. Liability for physical damage is absent from standards.

### 5.3 Tools: governance mechanisms

{{F24}}

{{T10}}

Among instruments (the fair comparison), robot instruments refer to technical standards (72% vs 36%), use testing and sandboxes (60% vs 33%) and conformity assessment (32% vs 12%) significantly more often, and international cooperation more often at the margin (72% vs 50%); funding, licensing and registration, liability regimes and insurance are higher but not significantly so at these sizes; audits, risk tiering and human-oversight requirements are used at the same rates; transparency and labelling and data governance are lower but not significantly. The adjusted models (Table 20) confirm standards references (odds ratio 3.8), conformity assessment (3.2), licensing (3.5), liability regimes (5.4) and funding (1.9) as the mechanisms associated with embodied documents after genre, region and year.

{{F25}}

{{T29}}

{{T15}}

On a common population (embodied documents in six regions; Table 29), the items that diverge by region are liability regimes (bias-corrected V 0.33), liability for physical damage (0.23), references to standards (0.21), human oversight (0.20), physical safety (0.20), autonomy-level control (0.19), robustness (0.17) and proximity (0.15); transparency, data governance, incident reporting, risk tiering, prohibitions and oversight bodies do not differ detectably (V 0.00 with intervals reaching 0.13 to 0.20). The v1 statement that "regions differ in mechanism more than in principle" compared effect sizes across different populations and is withdrawn; the defensible statement is that regions differ on liability and control, in both principle and tool, and not on the ethical core or on most procedural tools. Among all governance documents (Figure 25, Table 15), the regional contrasts in tools are larger (standards references from 7% in Oceania to 69% in the international layer; institution-building and funding in Africa and Latin America), with the caveat that Africa, Oceania and the Middle East have fewer than 40 governance documents each.

{{T24}}

K-means bundles of mechanisms (Table 24) have silhouettes of 0.18 or less at every k and are not interpreted.

### 5.4 Framing, stance and the personhood debate

{{F26}}

{{F27}}

{{F28}}

{{T12}}

Principle-or-ethics framing dominates Europe (55%), North America (54%) and Oceania (57%); Asia is plural (ethics 36%, liability 22%, innovation 20%); the Middle East is liability-framed (a legal-doctrinal literature on civil liability for smart robots). Among research papers, 56% take no regulatory position, 31% call for new regulation, 9% prefer self-regulation or standards and 4% argue existing law suffices. Legal personhood is discussed in 158 documents (19 supportive, 25 opposed, 114 without a position); its share of embodied documents falls from 21% in 2020 to 2024 to 11% in 2025 to 2026 (adjusted odds ratio 0.38).

### 5.5 Which instruments are cited

{{F29}}

{{T13}}

{{F30}}

General-AI documents cite the EU AI Act (24%), the OECD principles (16%), the GDPR (15%) and the UNESCO Recommendation (13%). Embodied documents cite the GDPR (10%) and the AI Act (9%) and then a robotics canon the general set does not: the Civil Law Rules on Robotics (8% vs 0.4%), the Product Liability Directive and the Machinery Regulation (3% each), the IEEE 7000 series and the UN CCW process (3%), ISO 13482 (2.7%), ISO 10218 (2.5%) and ISO/TS 15066 (1.9%). Asimov's fictional laws are cited by 6% of embodied documents and are not an instrument. By region, the AI Act is Europe's reference (27%), the OECD principles are Latin America's (23%) and Africa's (28%), and the Civil Law Rules are cited most in the Middle East (15%). No ISO robot standard is cited by more than 4% of any region's documents.

## 6. Part D. Regional comparison

{{T14}}

{{F31}}

{{T23}}

{{T23b}}

{{T31b}}

{{T31}}

Regional profiles are in Table 14. The cosine distances between regional principle, topic and mechanism profiles (Figure 31) place Europe and North America 0.008 apart, below North America's own split-half noise floor (0.033; Table 31b), so they are indistinguishable; Oceania (0.027 from Europe) and Asia (0.042) are within or at the noise floor of their sample sizes. The Middle East (0.15 from Europe, 0.08 from Asia), Latin America (0.12) and the international layer (0.19) are distinguishable, and their nearest neighbours are stable under bootstrap (Table 23b: Middle East to Asia in 91% of resamples; International to Asia 91%), whereas Asia's and Oceania's nearest neighbours are not (33% and 22%). Restricting to research papers (Table 31) removes most of the international layer's distinctiveness, which is a genre effect (it contains no research), but not the Middle East's.

In words: Europe and North America share a social- and care-robot research literature with an ethics framing; Asia (Japan, Korea, Taiwan, Singapore, India and the English-language Chinese documents present) adds humanoids, service and industrial robots and the most active instrument issuers; the Middle East is a liability-doctrine literature with Dubai's vehicle law; Latin America is a legislative region (Brazil's humanoid bill, El Salvador's statute, Peruvian and Argentine bills) with thin robot content; Africa is a capacity-building strategy layer; Oceania is too small (16 embodied documents) to characterise; the international layer is the standards layer.

## 7. Part E. Trends and the newest documents

{{F33}}

{{F42}}

Within the embodied set (composition-free), the terms "embodied AI" or "physical AI" appear in 2% of 2024 documents, 14% of 2025 documents and 23% of 2026 documents; humanoid vocabulary is present in roughly a third of embodied documents in every year and rises slightly in 2025 to 2026. Robot-type shares (Figure 42) show humanoids and logistics robots rising after 2024 and social robots receding.

{{F34}}

{{T28}}

{{T16}}

Comparing 198 embodied documents from 2025 to 2026 with 342 from 2020 to 2024, the crude shares of cybersecurity (+12 points), industrial policy (+11), human oversight (+10), physical safety (+10), risk management (+9) and standards (+9) rise and those of human-robot interaction (−13), ethics principles (−11) and personhood (−10) fall. Adjusted for document class and region (Table 28), cybersecurity (odds ratio 2.7, Holm p = 0.03) and personhood (0.38, p = 0.03) survive; human oversight (2.0, p = 0.09) is at the margin; industrial policy (1.5, p = 1.0) does not, and its research-only shares move from 9% to 13% only. The "turn to industrial policy" is therefore largely a change in which documents were written in 2025 to 2026 (more strategies and communications, fewer European research papers), not a change in what any genre says.

{{T17}}

{{T30}}

Trend models on the embodied set (Tables 17 and 30) show the risk-based-tiering mechanism (odds ratio 1.32 per year, interval 1.09 to 1.60) and the conformity-assessment mechanism (1.29, 1.11 to 1.51) rising, and the result holds when 2026 is excluded and when only documents with a stated date are used (1.21 to 1.31). The conformity-assessment consideration (1.13) and dual-use framing (0.91) are not significant after correction; physical safety, proximity, liability and autonomy-level control are flat. The compliance machinery around robots is growing; the physical-harm considerations are a constant.

The 2025 to 2026 layer of the collection is, read document by document: industrial strategies for humanoids and embodied intelligence (Shanghai, Japan's second AI Basic Plan, Israel's draft strategy) and Brazil's humanoid bill; research on oversight and cybersecurity of agentic and multi-robot systems; the conformity layer catching up (ISO/PAS 8800, ISO/IEC TR 5469, ISO 31101, ISO 3691-4, draft ISO 26058, the Commission's draft high-risk guidelines); and sector-specific binding law from outside the traditional AI-governance centres (El Salvador, Dubai, Argentina).

## 8. How different robot types are governed

{{S12}}

{{S13}}

- **Industrial and logistics robots.** The most mature regime in the collection: ISO 10218 and ISO/TS 15066 (cited, not captured), ISO 3691-4 and draft ISO 26058, Israel's SI 395 and the EU machinery rules; physical safety is present in most documents and proximity in two thirds; the dominant tool in instruments is the reference to standards. Governance here is occupational-safety governance.
- **Service and social robots.** The largest group and the least governed per document: ISO 13482, ISO 31101 and El Salvador's decree reach professional service and care robots; social, companion, educational and domestic robots are reached by 4, 2 and 5 instruments and intimate robots by one. Proximity and dignity dominate; the GDPR is the instrument most cited, so data-protection law governs by default.
- **Medical and body-integrated robots.** Medical-device law (the MDR-AI Act interplay guidance, WHO guidance) and the proposed liability instruments; the highest physical-safety and liability presence; the strongest Middle Eastern presence.
- **Humanoid and general-purpose robots.** Industrial strategies and one bill; legal personhood the most common primary topic; no binding law. The gap between the 2025 to 2026 surge in discourse and the absence of instruments is widest here.
- **Vehicles and field robots.** The most instrument-dense group in the collection (43 instruments mention vehicles) because transport and aviation regimes are referenced by AI strategies and the AI Act; the coverage audit shows the binding vehicle and drone laws themselves (UK, Germany, Japan, EU drone rules, UN R157) are largely absent, so this group is under-counted most.
- **Security and military robots.** The UN CCW process, national security law and humanitarian-law commentary; the highest share of documents calling for new regulation.

## 9. Part F. Reliability, validation and coverage

### 9.1 Reliability of the labels

{{F35}}

{{F43}}

{{F44}}

{{T26}}

{{T27}}

{{T27b}}

Five comparisons (Table 26), all computed against the annotations the analysis uses: a different model on the same input agrees at a median kappa of 0.85 (minimum 0.61 for page quality; 11 of 46 fields below 0.80, mainly the multi-label fields, stance, framing, date basis and three principle levels); the same model re-run agrees at 0.91 (minimum 0.66); the same model reading the full text instead of the excerpt agrees at 0.88 (minimum 0.71) and finds slightly more of everything (0.1 to 0.4 more labels per document; principle presence 0 to 6 points higher), with lower agreement on documents the excerpt truncated (median principle kappa 0.75 vs 0.84); the same model with the collectors' cover block and metadata removed agrees at 0.90 (minimum 0.65 for date basis), so the label leakage identified in review changed country, issuer and language labels little and page quality, date basis and stance most; and the extended blind re-annotation of governance documents agrees with the original at 0.83, with the largest movements in robot-type labels (0.60), stance (0.55) and publication stage (0.49). The confidence field is a page-quality proxy and is not used. No human coded any document; the protocol for a human validation sample is in the supplement.

### 9.2 Model-free check: full-text lexicons

{{F36}}

{{T18}}

After repairing the lexicon bugs found in review (a case-insensitive acronym pattern that matched the word "laws", unbounded dual-use terms, a harm pattern that matched "harmonised"), lexicon presence agrees with annotated presence at 65 to 86% for principles and 73 to 99% for robot types (median kappa 0.42 to 0.46, moderate), best for distinctive vocabularies (social, care, sex and surgical robots; trust and transparency) and worst for diffuse concepts. The Spearman correlation between annotated and lexicon-based embodied-minus-general differences across the 20 principles is 0.92; the rank correlation of the shares themselves is 0.82.

### 9.3 Sensitivity

{{T19}}

{{T32}}

Headline quantities are stable across subsets (Table 19) and across definitions of the embodied set (Table 32): under the strict definition (relevance only, 550 documents) the research share rises to 80%, instruments fall to 34 (4 binding) and the social-robot gap is unchanged (44% of research, 3 instruments).

### 9.4 Coverage and known gaps

{{F37}}

{{F41}}

{{T25}}

The collectors could not capture 266 of 2,160 listed sources, 109 of them in the European robot sprint; 34 captured files were oversized or restricted, 26 recovered. The coverage audit (Table 25, Figure 41) checks 38 reference instruments and standards named by the governance expert: {{AUDIT}}. The instruments cited by the corpus but not captured as documents (the Machinery Regulation, the revised Product Liability Directive, UN R157, ISO 10218 and ISO/TS 15066, Korea's Intelligent Robots Act among them) are the first targets for a further collection round, and their absence is why every instrument count in this report is a lower bound and why the vehicles and industrial groups are under-counted most.

## 10. Limitations

The corpus is a purposive multilingual collection, not a census, and its composition drives several ratios: Europe is 43% of usable documents, English 79%, Chinese 0.5%; the research-to-instrument ratio reflects the sprint-versus-database design; known binding instruments are missing. Labels were assigned by a language model with no human gold standard; they are consistent across models, re-runs, full text and blind inputs but not certified. The extended re-annotation still truncates the longest quarter of governance documents. Dates are inferred from content for about a quarter of documents; 2026 is partial. OpenAlex enrichment is DOI-only and some citation counts are implausible. The six embodied-specific items are considerations scored like principles, not principles in the ethical sense; the relevance field used to define the sets was produced by the same model that produced the outcomes. Small groups (binding instruments, standards, Oceania, Africa) are reported as counts, and conclusions about them are correspondingly tentative.

## 11. Conclusions

Within this collection, embodied AI is governed by voluntary guidance, technical standards and the enumeration of robots inside general-AI and sector law; four binding instruments in force reach robots, one of them a robotics statute. The robot literature's own considerations, physical safety, proximity, physical liability and autonomy-level control, are what distinguish it from general-AI governance once genre is accounted for, and its tools are those of product safety: standards, testing and conformity assessment. Standards specify physical safety; nothing yet specifies autonomy-level control. Research and rules point at different robots, with companion and social robots the clearest case of attention without instruments. Regions share an ethical core and differ on liability and control. The frontier is moving toward cybersecurity, oversight, conformity machinery, humanoids and the new vocabulary of "physical AI". For governance practice: the operative texts for robots are standards and product law, so attention to ISO/TC 299, IEC and the AI Act's harmonised-standards mandate buys more than new principles; robots that live with people have almost no instruments of their own; and autonomy-level control needs a specification that neither standards nor binding instruments yet provide.

## Glossary

- **Embodied AI, physical AI.** AI that controls a machine with a body: robots, self-driving vehicles, drones, surgical and factory machines.
- **Governance instrument, rule or policy.** A law, regulation, decree, bill, strategy, guideline, code, standard or resolution meant to steer behaviour. Research papers and news are not instruments.
- **Binding law vs voluntary guidance (soft law).** Binding: breaking it has legal consequences. Voluntary: guidance, principles, strategies and codes that cannot be enforced on their own.
- **Technical standard.** A detailed voluntary engineering specification (ISO 10218, ISO 13482) that laws often make binding by reference.
- **Conformity assessment.** The pre-market check (testing, certification, CE marking) that a product meets safety rules.
- **Mentioned vs specified in depth.** A principle or consideration is mentioned when named; specified in depth when the document says what must be done, by whom and how it is checked.
- **Governance-gap index.** Share of research papers about a robot type minus the share of instruments; positive means studied more than governed.
- **Cohen's kappa.** Agreement between two labellers after discounting chance; 0.8 and above is conventionally "almost perfect", 0.6 "substantial", 0.4 "moderate".
- **Holm correction.** Raises the bar for significance when many comparisons are made at once.
- **Cramér's V.** Strength of association from 0 to 1; 0.1 small, 0.3 medium; bias-corrected versions remove the inflation small samples produce.
- **Odds ratio.** How much more likely an outcome is in one group than another; 1 means no difference. Adjusted odds ratios allow for other differences between the groups (here document class, region and year).
- **Wilson interval, bootstrap interval.** The range within which a percentage or difference would most likely fall if the sample were drawn again.

## Appendix. Figure and table index

Figures 1 to 44 (9, 15 and 32 were merged into neighbours) are in `figures/` as PNG and SVG in light and dark variants with their data in `figures/data/`; tables T01 to T35 and S01 to S13 are in `tables/`; every statistic is in `data/results.json`. The supplement holds the codebook, taxonomies, reliability detail, instrument lists, coverage audit, datasheet and the review log.
