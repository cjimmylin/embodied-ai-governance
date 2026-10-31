---
title: "Governing machines that act in the world: a content analysis of embodied-AI governance documents from eight world regions (v2)"
author: "Jimmy Lin (Centre for Enterprise Innovation) with the CEI regional collection teams; analysis prepared with Claude Code. Version 2, revised after six independent adversarial reviews."
date: "31 October 2026 (working paper, venue-agnostic)"
---

<div class="abstract">

**Abstract.** Artificial-intelligence governance has been studied intensively for software systems; much less is known, quantitatively, about how *embodied* AI (robots, autonomous vehicles, drones, medical and industrial machines) is governed. We analyse a purposive multilingual collection of 1,656 unique documents (1,538 usable) gathered by eight regional teams: laws, bills, strategies, standards, guidelines, government reports, research outputs and communications from 110 countries, the European Union and the international standards layer. Every document was labelled by a language model under a fixed 39-field codebook; governance documents were re-labelled from up to 110,000 characters of text with the collectors' metadata removed. Label consistency was measured five ways (second model, re-run, full text, metadata-blind input, extended input; median kappa 0.83 to 0.91); no human coding was available, and the labels are treated as consistent rather than certified. Comparisons between the 675 embodied-AI documents and the 806 general-AI documents are made within document genre and with covariate adjustment, because the collection design confounds the two sets with genre. Within this collection, embodied AI is governed by 65 instruments (34 robot-specific), of which four binding instruments are in force, reached through sector law (vehicles, security) and general AI law rather than robotics statutes, with one exception (El Salvador, 2025); a coverage audit against 38 reference instruments shows that several known binding vehicle, drone and industrial-robot laws were not captured, so instrument counts are lower bounds. Research and instruments attend to different robots: companion and social robots are 43% of embodied research outputs and 6% of embodied instruments (gap +37 points, bootstrap interval 29 to 44), autonomous vehicles 12% and 66% (−54, −66 to −42). The considerations that distinguish embodied governance, physical safety, human-robot proximity, liability for physical damage, autonomy-level control, conformity assessment and dual use, survive adjustment for genre, region and year (adjusted odds ratios 4 to 166), whereas most differences on the ethical core do not, and accountability is lower in embodied documents within every genre. Among instruments, embodied rules refer to technical standards (72% vs 36%), testing (60% vs 33%) and conformity assessment (32% vs 12%). Technical standards specify physical safety in depth; autonomy-level control is raised by 43 to 70% of instruments of every type and specified by few. On a common population, regions do not differ on the ethical core but do on liability and control (bias-corrected Cramér's V 0.19 to 0.33); Europe and North America are indistinguishable, the Middle East (liability-led) and the standards layer distinct. Between 2020 to 2024 and 2025 to 2026, adjusted for genre and region, cybersecurity rises (odds ratio 2.7) and legal personhood falls (0.38); risk-based tiering and conformity assessment grow about 30% per year; the terms "embodied AI" and "physical AI" rise from 2% to 23% of embodied documents. We release the codebook, annotations, master table, figures, dashboard and code, together with the six reviews and a log of what changed.

</div>

## 1. Introduction

A large literature maps the principles and instruments of AI governance. Reviews of ethics guidelines found convergence on a small set of principles alongside divergence in implementation (Jobin, Ienca and Vayena 2019; Fjeld et al. 2020; Hagendorff 2020; Schiff et al. 2021; Corrêa et al. 2023), and the European Union's AI Act has become the reference point for binding regulation (Veale and Zuiderveen Borgesius 2021; Regulation (EU) 2024/1689). That literature is about software. An older literature on robot law and robot ethics argues that machines which act physically in the world raise distinct problems (Calo 2015; Leenes et al. 2017; Winfield and Jirotka 2018): bodily harm, proximity to people, liability for physical damage, the autonomy that may be delegated to a machine, and certification before market access. The RoboLaw guidelines (Palmerini et al. 2014), the European Parliament's 2017 resolution (European Parliament 2017; Nevejans 2016), the ISO safety standards for industrial, collaborative and personal-care robots (ISO 10218; ISO/TS 15066; ISO 13482), the Korean Intelligent Robots Act (2008), and sector regulation for vehicles (Taeihagh and Lim 2019) and drones (Stöcker et al. 2017) are the usual reference points; Holder et al. (2016), Bertolini (2020), Fosch-Villaronga and Mahler (2021) and Salvini et al. (2021) map the legal and safety regimes in detail.

The two literatures have rarely been brought together with numbers. Existing document collections, such as the OECD.AI policy observatory and the AlgorithmWatch inventory of ethics guidelines, do not separate embodied from general AI or code documents for the considerations that matter for machines. This paper asks five questions of a purpose-built collection: (Q1) what the documented governance of embodied AI consists of; (Q2) which robots are governed and which are only studied; (Q3) which considerations, tools and framings distinguish embodied-AI governance from general-AI governance once genre is accounted for; (Q4) how regions differ; (Q5) what is changing. It is a second version: the first was reviewed adversarially from six perspectives, and this version reports what survived.

## 2. Background

**From principles to law.** Jobin et al. (2019) coded 84 guidelines; Fjeld et al. (2020) organised 36 into eight themes; Schiff et al. (2021) showed sectoral differences; Corrêa et al. (2023) extended the exercise to 200 documents and documented geographic concentration. Hagendorff (2020) argued the guidelines had little effect, which motivated binding instruments and the mechanisms of risk-based tiering, conformity assessment, audits, transparency obligations and oversight bodies. The OECD (2019) and UNESCO (2021) recommendations supply the intergovernmental layer.

**Robot law and standards.** Calo (2015) identified embodiment, emergence and social valence as what makes robots legally distinctive. Leenes et al. (2017) set out the regulatory challenges; Fosch-Villaronga and Heldeweg (2018) proposed iterative regulation. Specific debates concern care robots (Sharkey and Sharkey 2012; van Wynsberghe 2013), the privacy implications of social robots (Lutz, Schöttler and Hoffmann 2019), autonomous weapons (Sparrow 2007) and legal personality (Bryson, Diamantis and Grant 2017; Solaiman 2017). The standards community produced the operative texts: ISO 10218-1 and -2 (2011, revised 2025), ISO/TS 15066 (2016), ISO 13482 (2014) and, recently, ISO 3691-4, ISO 31101, ISO/PAS 8800 and ISO/IEC TR 5469; the EU Machinery Regulation (Regulation (EU) 2023/1230) and the AI Act's Annex I treat robots as products subject to harmonised standards.

**Language models as annotators.** Large language models can match crowd workers on text-annotation tasks (Gilardi, Alizadeh and Kubli 2023; Törnberg 2024), but their output is unstable across prompts and versions (Reiss 2023), requires validation against human labels (Pangakis, Wolken and Fasching 2023; Thalken et al. 2023), raises reproducibility concerns for proprietary models (Ollion et al. 2024), and carries measurement error that biases downstream estimates unless corrected (Egami et al. 2023; Angelopoulos et al. 2023). We meet part of that bar (fixed codebook, structured output, five consistency checks, stored inputs, repaired lexicons) and not the rest (no human gold standard, no measurement-error correction); Section 7 states the consequences.

## 3. Data

**Collection.** Eight regional teams (Africa; Asia; Europe; Latin America and the Caribbean; Middle East; North America; Oceania; and an international layer assembled across teams) ran a *sprint* for robot-specific sources and a *database* of general AI-governance instruments between 2025 and October 2026, recording 2,160 sources in manifests and capturing 1,894 as 2,557 files; 266 sources could not be captured (109 in the European sprint).

**Processing.** Files were converted to text; 34 oversized or restricted files were recovered as text where possible (26). Duplicates were merged by content hash, URL, normalised title, truncated-title prefix and MinHash similarity on prose (Broder 1997), and, after review, by a second pass on normalised title and jurisdiction with years within one, yielding 1,656 canonical documents; 46 duplicate captures (the AI Act three times, its 2021 proposal twice, the Civil Law Rules twice, twelve copies of one Commission press release among them) are listed in the release. Documented corrections from the legal review (46 field changes, including the revocation of Executive Order 14110, the reclassification of catalogue pages as web pages and of bills as non-binding) were applied through a versioned override file. Of the canonical documents, 1,538 have readable text and are on topic. Language was detected on full text (79% English; Chinese 7 documents). DOIs were resolved against OpenAlex (Priem, Piwowar and Orr 2022) for 373 research outputs.

**Analysis sets.** The embodied-AI set (n = 675) comprises usable documents rated 2 or 3 on a 0 to 3 relevance scale or carrying any robot-type label (125 enter by label alone); the general-AI set (n = 806) comprises documents rated 0 or 1 with no label; 57 are off-topic. Governance instruments (n = 326) are statutes, regulations, decrees, bills, strategies, standards, guidelines, resolutions and consultations with a lifecycle status and binding nature; government reports (112) are separate. Embodied instruments (65) are split into robot-specific (relevance 2 or 3; 34) and general-AI instruments with robot provisions (31). Regions follow the issuing jurisdiction; North America combines the United States, Canada and Greenland.

## 4. Methods

**Codebook.** Thirty-nine fields (supplement S2): bibliographic fields; jurisdiction and scope; 28 document types in 8 classes; governance-instrument status (nine states) and binding nature; AI scope and embodiment status; 23 robot types in 7 groups; 16 sectors; 27 topics; 14 core principles (Jobin et al.; OECD) and 6 embodied-specific considerations (physical safety, human-robot proximity, liability for physical damage, autonomy level and control, conformity assessment, dual use), each scored 0 absent, 1 mentioned, 2 specified in depth; 19 mechanisms; named instruments cited; personhood position; framing; stance; methodology; capture quality; relevance.

**Annotation.** Claude Sonnet 5.5 through the Claude Code command-line interface, codebook as system prompt, JSON schema enforcing every field, no tools; prompt hash recorded. Version 1 used a 14,000-character excerpt (first 10,000, middle 2,500, last 1,500) and passed the collectors' folder, title and language as metadata; review found that 483 texts also carried the collectors' labels in a cover block. Version 2 re-annotated all 351 governance documents with the cover block stripped, metadata reduced to a document id and word count, and up to 110,000 characters of text (74% of governance documents seen in full; median share seen 1.0 against 0.36 before), with the exact inputs stored. Cost: 120 USD (v1) plus 32 USD (v2 runs).

**Consistency checks.** Against the annotations the analysis uses: Claude Opus 5.5 on the same v1 input (160 documents); Sonnet re-run (161); Sonnet on the full text (160); Sonnet metadata-blind and cover-stripped (160); and the v2 extended annotation against v1 for governance documents (351). Cohen's kappa, quadratic-weighted for ordinal fields, mean per-label for multi-label fields; unweighted and level-2 variants in the supplement. Cross-checks against the collectors' labels are reported but overstate independence because the labels were visible to the v1 annotator.

**Lexicons.** Multilingual regular-expression lexicons for robot types, named instruments and principles over full text, repaired after review (a case-insensitive acronym matched the word "laws"; unbounded dual-use and harm patterns; the AI Act pattern absorbed state AI acts).

**Statistics.** Wilson intervals; chi-square with Monte-Carlo p-values when more than a fifth of expected counts are below five and Fisher's exact test for sparse 2 by 2 tables; bias-corrected Cramér's V (Bergsma 2013) with percentile-bootstrap intervals on a common population; Holm correction within families; logistic regression of each outcome on set membership adjusting for document class, region and year; Mantel-Haenszel tests stratified by class; genre-stratified comparisons; bootstrap intervals for the governance-gap index (research share minus instrument share) and for regional cosine distances, with split-half noise floors; logistic trend models with sensitivities (excluding the partial year 2026; stated-date documents only). K-means bundles were examined and not interpreted (silhouette 0.18 at every k).

## 5. Results

### 5.1 What the documented governance of embodied AI consists of (Q1)

{{F01}}

The embodied-AI set is 75% research outputs and 76% academic in origin; the general-AI set is 47% communications and 22% voluntary guidance with 50 research outputs (Figure 1). This mirrors the collection design and is why Sections 5.3 to 5.5 compare within genre.

{{F04}}

{{T33}}

Of the 65 instruments that reach robots, 44 are voluntary guidance, 8 technical standards, 8 proposals and 5 legally binding; the binding share among instruments with a settled nature is similar in the two sets (5 of 57 vs 25 of 220, chi-square p = 0.11). The binding five are El Salvador's Robotic Technologies Law (2025, in force, the only robotics statute), Dubai's autonomous-vehicle law (2023), Argentina's resolution creating a security-AI unit (2024), the EU AI Act (2024, reaching robots through its product lists) and United States Executive Order 14110 (2023, revoked January 2025). Of the 34 robot-specific instruments, 9 are partial or catalogue captures.

{{F06}}

{{F41}}

Dated instruments accumulate as in Figure 6: voluntary guidance from 1 (2014) to 44, standards to 7, binding from 2023. The coverage audit (Figure 41, Table 25) is the necessary corrective: of 38 reference instruments and standards relevant to embodied AI, {{AUDIT}}. The missing items include binding vehicle and drone law (the UK Automated Vehicles Act 2024, Germany's 2021 autonomous-driving law, Japan's Level-4 regime, UN R157, EU drone rules), the EU Machinery Regulation and revised Product Liability Directive, Korea's Intelligent Robots Act and ISO 10218 and ISO/TS 15066. Instrument counts in this paper are therefore lower bounds, and what the collection shows reliably is the *route* by which binding law reaches robots in the documents that were captured: sector law and general AI law, not robotics statutes.

{{F07}}

Europe supplies 43% of usable documents and 58% of them are embodied; Asia 258 (41% embodied); North America 160 (52%); Latin America 128 (13%); the Middle East 86 (41%); the international layer 140 (17%); Africa 61 (20%); Oceania 40 (40%) (V = 0.33). Of 110 countries with a document, 65 contribute an instrument, 17 a binding instrument and 12 a robot-specific instrument; no country has more than five robot-specific instruments. Non-English documents are more often instruments (33% vs 19%).

### 5.2 Which robots are governed and which are studied (Q2)

{{F11}}

{{F40}}

{{T22}}

Companion and social robots are the most addressed type (230 documents), then care robots (174), humanoids (142), autonomous road vehicles (134), professional service robots (132), industrial manipulators (114), surgical robots (108), military weapons (83), drones (70) and collaborative robots (67). The governance-gap index with bootstrap intervals (Figure 40, Table 22) separates three groups: studied far more than governed (social and companion robots, +37, 29 to 44; 4 instruments, none binding); near parity (humanoids +9 with an interval including zero; care, domestic, educational robots); governed far more than studied (vehicles −54, industrial manipulators −36, drones −28, agricultural and logistics robots −16 and −15, collaborative, surgical and military robots −12, −12, −10, all intervals excluding zero). Regions and genres attend to different machines: social robots are European (43% of Europe's embodied documents) and North American (37%); humanoids lead in the Middle East and Asia; voluntary guidance mentions vehicles in 62% of cases and research in 12%. Within the embodied set, social robots fall from 42% of documents in 2020 to 2022 to 26% in 2025 to 2026 and humanoids rise from 17% to 29% (Figure 42 in the report).

### 5.3 Considerations, tools and framings (Q3)

{{F39}}

{{F38}}

{{T20}}

{{T34}}

Pooled over all documents, 17 of 20 principle differences are Holm-significant, but pooled differences are genre differences. Within governance instruments (65 vs 258; Figure 39, Table 21 in the report), the six embodied-specific considerations differ sharply (physical safety 60% vs 7%, autonomy-level control 49% vs 11%, proximity 40% vs 0.4%, conformity assessment 59% vs 18%, dual use 35% vs 10%, liability for physical damage 23% vs 1%; all Holm-significant) and no core principle does; within research outputs the same six differ and inclusive growth is lower (22% vs 52%). Adjusting for class, region and year (Table 20), the embodied-specific considerations keep very large odds ratios (physical safety 63, proximity 166, liability 87, autonomy-level control 13, dual use 5.4, conformity 4.2); among core principles only transparency (0.49) and justice and fairness (0.47) remain lower, and the Mantel-Haenszel analysis (Table 34) adds accountability (0.63), inclusive growth (0.57) and non-maleficence (1.76). The v1 claim that accountability did not differ was a Simpson's paradox.

{{F23}}

{{T09}}

Figure 23 (content-analysed captures only) and Table 9 show which document types specify the embodied considerations. Technical standards specify physical safety in depth in every captured case; binding instruments in 2 of 5, with conformity assessment in 3 of 5 and liability in 2 of 5; voluntary guidance mentions physical safety in 45% and specifies it in 7%. Autonomy-level control is mentioned by 43 to 70% of every instrument type and specified in depth by 1 of 5 binding instruments, 1 of 10 drafts and 2 of 42 voluntary instruments; no standard specifies it and no standard addresses liability. These statements follow the extended re-annotation, which raised the number of mechanisms, robot types and named instruments found per governance document by 15 to 60% while leaving binding and status labels unchanged for more than 95% of documents (Table 35 in the report).

{{F24}}

{{T10}}

Among instruments, embodied rules refer to technical standards (72% vs 36%), use testing and sandboxes (60% vs 33%) and conformity assessment (32% vs 12%) significantly more often (Figure 24, left); international cooperation is higher at the margin (72% vs 50%, Holm p = 0.05); funding, licensing, liability regimes and insurance are higher but not significantly at these sizes; audits, risk tiering and oversight requirements are used at the same rates; labelling and data governance are lower but not significantly. The adjusted models confirm standards references (3.8), conformity assessment (3.2), licensing (3.5), liability regimes (5.4) and funding (1.9).

{{F29}}

Two reference ecosystems: general-AI documents cite the AI Act (24%), the OECD principles (16%), the GDPR (15%) and the UNESCO Recommendation (13%); embodied documents cite the GDPR (10%), the AI Act (9%), the Civil Law Rules on Robotics (8% vs 0.4%), the Product Liability Directive and the Machinery Regulation (3% each), the IEEE 7000 series and the UN CCW process (3%), ISO 13482 (2.7%), ISO 10218 (2.5%) and ISO/TS 15066 (1.9%); no ISO robot standard is cited by more than 4% of any region's documents. Framing is ethics-led in Europe, North America and Oceania, plural in Asia and liability-led in the Middle East (V = 0.24); 56% of embodied research takes no regulatory position, 31% calls for new regulation and 4% argues existing law suffices.

### 5.4 Regional comparison (Q4)

{{T29}}

{{F31}}

On a common population (embodied documents, six regions; Table 29), regions differ on liability regimes as a tool (bias-corrected V 0.33, interval 0.24 to 0.45), liability for physical damage (0.23), references to standards (0.21), human oversight (0.20), physical safety (0.20), autonomy-level control (0.19), robustness (0.17) and proximity (0.15), and not detectably on transparency, data governance, incident reporting, risk tiering, prohibitions or oversight bodies (V 0.00). The earlier claim that "regions differ in mechanism more than in principle" compared effect sizes across different populations and is withdrawn. Cosine distances between regional profiles (Figure 31) place Europe and North America 0.008 apart, below North America's split-half noise floor (0.033), so they are indistinguishable; Asia and Oceania sit at their own noise floors; the Middle East (0.15 from Europe), Latin America (0.12) and the international layer (0.19) are distinguishable, and their nearest neighbours are stable under bootstrap (91% of resamples for the Middle East and the international layer). Restricting to research outputs removes the international layer's distinctiveness (a genre effect) but not the Middle East's.

### 5.5 Trends (Q5)

{{F34}}

{{T28}}

{{T30}}

Comparing 198 embodied documents from 2025 to 2026 with 342 from 2020 to 2024, crude shares rise for cybersecurity (+12 points), industrial policy (+11), human oversight (+10), physical safety (+10), risk management (+9) and standards (+9) and fall for human-robot interaction (−13), ethics principles (−11) and personhood (−10). Adjusted for document class and region (Table 28), cybersecurity (odds ratio 2.7, Holm p = 0.03) and personhood (0.38, p = 0.03) survive, human oversight is at the margin (2.0, p = 0.09), and industrial policy does not (1.5, p = 1.0; its research-only share moves from 9% to 13%). Trend models (Table 30) show the risk-based-tiering mechanism (odds ratio 1.32 per year) and the conformity-assessment mechanism (1.29) rising, robust to excluding 2026 (1.31, 1.28) and to stated-date documents (1.23, 1.21); physical safety, proximity, liability and autonomy-level control are flat. Within the embodied set, the terms "embodied AI" and "physical AI" appear in 2% of 2024 documents, 14% of 2025 documents and 23% of 2026 documents (Figure 33 in the report).

### 5.6 Consistency of the labels

{{F43}}

{{T26}}

Against the annotations used, a second model agrees at a median kappa of 0.85 (minimum 0.61, page quality; 11 of 46 fields below 0.80); a re-run at 0.91 (0.66); full text at 0.88 (0.71), finding 0.1 to 0.4 more labels per document and agreeing less on documents the excerpt truncated (median principle kappa 0.75 vs 0.84); the metadata-blind, cover-stripped input at 0.90 (0.65, date basis), with country, issuer and language labels little changed; and the v2 extended annotation of governance documents at 0.83 against v1, moving robot-type labels (0.60), stance (0.55) and publication stage (0.49) most. Repaired lexicons agree with the annotations at median kappa 0.42 to 0.46; the Spearman correlation of embodied-minus-general differences across principles is 0.92 and the rank correlation of shares 0.82. Headline quantities are stable across eleven subsets and across a strict set definition (Tables 19 and 32 in the report).

## 6. Discussion

**Embodied-AI governance is a research discourse with a standards spine, and the binding layer reaches robots sideways.** Three quarters of the embodied documents are research; the instruments that exist are voluntary guidance and standards; and the binding instruments that were captured reach robots through vehicle law, security law and general AI law. The one robotics statute is Salvadoran. The audit adds the important qualification that the collection missed the sectoral binding layer for vehicles, drones and industrial robots that exists in Europe, Japan, the United Kingdom and under UN regulations; a reader should take the route (sector and general-AI law) as the finding and the count (four in force) as a lower bound.

**The body is what distinguishes embodied governance, and it survives the confound.** Once genre, region and year are accounted for, the six embodied-specific considerations remain the largest differences in the data, while the core ethical vocabulary is shared, with transparency, fairness and accountability somewhat *less* present in embodied documents of the same type. Earlier guideline reviews found convergence on transparency, fairness and non-maleficence; our results say that convergence extends to robots, and that what robots add is a harm-avoidance vocabulary and a product-safety toolkit: standards references, testing, conformity assessment.

**Specification lags mention, and standards are the specifiers.** With the governance documents read nearly in full, the result holds: standards specify physical safety; binding instruments specify conformity and liability in some cases; voluntary guidance mentions and rarely specifies; and autonomy-level control, raised by nearly half of all instruments, is specified by very few. The governance expert's review notes that autonomy levels are specified outside this collection (SAE J3016, UN R157, the German and UK vehicle laws), which is consistent: the specification exists in vehicle law and standards, not in the AI-governance texts that the teams captured.

**Research and rules point at different robots.** Vehicles, arms, drones and medical robots inherited regimes; companion and social robots did not, and after two decades of research they have four instruments in this collection, none binding. General regimes (product safety, toys, data protection, the AI Act's transparency and vulnerability provisions) apply to them; the gap is in robot-specific instruments and in the research community's engagement with existing law (4% of papers argue it suffices).

**Regions share values and differ on liability and control.** The common-population analysis replaces the earlier mechanism-versus-principle contrast with a narrower and better-supported one: liability (as a consideration and as a tool), oversight, autonomy level and physical safety vary by region; the ethical core and most procedural tools do not. Europe and North America cannot be told apart; the Middle East's liability-led literature and the standards layer can.

**The frontier.** After adjustment, the 2025 to 2026 shift is toward cybersecurity and away from the personhood debate, with human oversight rising at the margin; the industrial-policy turn is a change in the document mix. The compliance machinery (risk tiers, conformity assessment) is growing around a constant set of physical-harm considerations, and the vocabulary of "physical AI" has arrived.

## 7. Limitations

The collection is purposive, European and English-heavy, nearly without Chinese-language documents, and missing known binding instruments; its sprint-versus-database design confounds the embodied and general sets with genre, which the within-genre and adjusted analyses address but cannot remove. All labels come from one proprietary model family without a human gold standard; the five consistency checks bound instability but not validity, and downstream estimates are not corrected for measurement error (Egami et al. 2023; Angelopoulos et al. 2023). The relevance field that defines the sets was produced by the same model as the outcomes. The extended re-annotation still truncates the longest quarter of governance documents. About a quarter of dates are inferred from content; 2026 is partial. Small groups are reported as counts and conclusions about them are tentative. The instrument scheme does not record whom an instrument binds, applicability dates or legal effect of standards (harmonised, incorporated, mandatory), which the governance review recommends for a policy-grade inventory.

## 8. Conclusion

With 1,656 documents from eight regions, a 39-field codebook, model annotation checked five ways, repaired lexicons and genre-aware statistics, this study gives a quantitative map of embodied-AI governance as it appears in a purpose-built collection and states clearly where the collection ends. The map shows a research discourse, a standards spine, a sideways binding layer, a harm-avoidance vocabulary that survives every adjustment, a product-safety toolkit, a social-robot gap, regional agreement on values and disagreement on liability and control, and a frontier moving toward cybersecurity, conformity and physical AI. The release, the six reviews and the change log allow each claim to be re-examined and the collection to be extended where the audit shows it is thin.

## References

Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T. (2023). Prediction-powered inference. *Science*, 382(6671), 669–674.

Bergsma, W. (2013). A bias-correction for Cramér's V and Tschuprow's T. *Journal of the Korean Statistical Society*, 42(3), 323–328.

Bertolini, A. (2020). *Artificial Intelligence and Civil Liability*. Study for the European Parliament JURI Committee.

Broder, A. Z. (1997). On the resemblance and containment of documents. *Proceedings of Compression and Complexity of Sequences*, 21–29.

Bryson, J. J., Diamantis, M. E., & Grant, T. D. (2017). Of, for, and by the people: the legal lacuna of synthetic persons. *Artificial Intelligence and Law*, 25(3), 273–291.

Calo, R. (2015). Robotics and the lessons of cyberlaw. *California Law Review*, 103(3), 513–563.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Corrêa, N. K., et al. (2023). Worldwide AI ethics: A review of 200 guidelines and recommendations for AI governance. *Patterns*, 4(10), 100857.

Egami, N., Hinck, M., Stewart, B. M., & Wei, H. (2023). Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models. *Advances in Neural Information Processing Systems*, 36.

European Parliament (2017). Resolution of 16 February 2017 with recommendations to the Commission on Civil Law Rules on Robotics (2015/2103(INL)).

Fjeld, J., Achten, N., Hilligoss, H., Nagy, A., & Srikumar, M. (2020). *Principled Artificial Intelligence*. Berkman Klein Center Research Publication 2020-1.

Fosch-Villaronga, E., & Heldeweg, M. (2018). "Regulation, I presume?" said the robot. *Computer Law & Security Review*, 34(6), 1258–1277.

Fosch-Villaronga, E., & Mahler, T. (2021). Cybersecurity, safety and robots: Strengthening the link between cybersecurity and safety in the context of care robots. *Computer Law & Security Review*, 41, 105528.

Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86–92.

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences*, 120(30), e2305016120.

Hagendorff, T. (2020). The ethics of AI ethics: An evaluation of guidelines. *Minds and Machines*, 30(1), 99–120.

Holder, C., Khurana, V., Harrison, F., & Jacobs, L. (2016). Robotics and law: Key legal and regulatory implications of the robotics age (Part I of II). *Computer Law & Security Review*, 32(3), 383–402.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

ISO 10218-1 and ISO 10218-2. *Robotics — Safety requirements for industrial robots* (2011; revised 2025). ISO 13482:2014. *Robots and robotic devices — Safety requirements for personal care robots*. ISO/TS 15066:2016. *Robots and robotic devices — Collaborative robots*.

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389–399.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

Leenes, R., Palmerini, E., Koops, B.-J., Bertolini, A., Salvini, P., & Lucivero, F. (2017). Regulatory challenges of robotics. *Law, Innovation and Technology*, 9(1), 1–44.

Lutz, C., Schöttler, M., & Hoffmann, C. P. (2019). The privacy implications of social robots. *Mobile Media & Communication*, 7(3), 412–434.

Nevejans, N. (2016). *European civil law rules in robotics*. Study for the European Parliament JURI Committee.

OECD (2019). *Recommendation of the Council on Artificial Intelligence*, OECD/LEGAL/0449.

Ollion, É., Shen, R., Macanovic, A., & Chatelain, A. (2024). The dangers of using proprietary LLMs for research. *Nature Machine Intelligence*, 6, 4–5.

Palmerini, E., et al. (2014). *Guidelines on Regulating Robotics*. RoboLaw project deliverable D6.2.

Pangakis, N., Wolken, S., & Fasching, N. (2023). Automated annotation with generative AI requires validation. arXiv:2306.00176.

Priem, J., Piwowar, H., & Orr, R. (2022). OpenAlex: A fully-open index of scholarly works. arXiv:2205.01833.

Regulation (EU) 2023/1230 on machinery. *Official Journal of the European Union* L 165. Regulation (EU) 2024/1689 (Artificial Intelligence Act). *Official Journal of the European Union* L, 12 July 2024.

Reiss, M. V. (2023). Testing the reliability of ChatGPT for text annotation and classification: A cautionary remark. arXiv:2304.11085.

Republic of Korea (2008). *Intelligent Robots Development and Distribution Promotion Act*, Act No. 9014.

Rousseeuw, P. J. (1987). Silhouettes. *Journal of Computational and Applied Mathematics*, 20, 53–65.

Salvini, P., Paez-Granados, D., & Billard, A. (2021). On the safety of mobile robots serving in public spaces: Identifying gaps in EN ISO 13482:2014 and calling for a new standard. *ACM Transactions on Human-Robot Interaction*, 10(3), 1–27.

Schiff, D., Borenstein, J., Biddle, J., & Laas, K. (2021). AI ethics in the public, private, and NGO sectors. *IEEE Transactions on Technology and Society*, 2(1), 31–42.

Sharkey, A., & Sharkey, N. (2012). Granny and the robots. *Ethics and Information Technology*, 14(1), 27–40.

Solaiman, S. M. (2017). Legal personality of robots, corporations, idols and chimpanzees. *Artificial Intelligence and Law*, 25(2), 155–179.

Sparrow, R. (2007). Killer robots. *Journal of Applied Philosophy*, 24(1), 62–77.

Stöcker, C., Bennett, R., Nex, F., Gerke, M., & Zevenbergen, J. (2017). Review of the current state of UAV regulations. *Remote Sensing*, 9(5), 459.

Taeihagh, A., & Lim, H. S. M. (2019). Governing autonomous vehicles. *Transport Reviews*, 39(1), 103–128.

Thalken, R., Stiglitz, E. H., Mimno, D., & Wilkens, M. (2023). Modeling legal reasoning: LM annotation at the edge of human agreement. *Proceedings of EMNLP 2023*.

Törnberg, P. (2024). Best practices for text annotation with large language models. *Sociologica*, 18(2), 67–85.

UNESCO (2021). *Recommendation on the Ethics of Artificial Intelligence*.

van Wynsberghe, A. (2013). Designing robots for care. *Science and Engineering Ethics*, 19(2), 407–433.

Veale, M., & Zuiderveen Borgesius, F. (2021). Demystifying the Draft EU Artificial Intelligence Act. *Computer Law Review International*, 22(4), 97–112.

Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209–212.

Winfield, A. F. T., & Jirotka, M. (2018). Ethical governance is essential to building trust in robotics and AI systems. *Philosophical Transactions of the Royal Society A*, 376(2133), 20180085.

## Appendix. Materials

Analysis report (all 44 figures and 35 tables with narrative), supplement (codebook, taxonomies, five-way reliability, instrument lists, coverage audit, datasheet, human-validation protocol), the six reviews and the review-and-changes log, master table, dashboard, per-document annotations with stored inputs, and all scripts are provided in the release.
