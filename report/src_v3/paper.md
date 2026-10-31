---
title: "Governing machines that act in the world: a content analysis of embodied-AI governance documents from eight world regions (v3)"
author: "Jimmy Lin (Centre for Enterprise Innovation) with the CEI regional collection teams; analysis prepared with Claude Code. Version 3, revised after six independent adversarial reviews and extended by a second collection round."
date: "31 October 2026 (working paper, venue-agnostic)"
---

<div class="abstract">

**Abstract.** Artificial-intelligence governance has been studied intensively for software systems; much less is known, quantitatively, about how *embodied* AI (robots, autonomous vehicles, drones, medical and industrial machines) is governed. We analyse a purposive multilingual collection of 3,291 unique documents (3,148 usable) from 116 countries, the European Union and the international standards layer, gathered by eight regional teams (laws, bills, strategies, standards, guidelines, government reports, research outputs and communications) and by a second round of nine collector agents and scripted harvests of seven legal databases, standards catalogues and treaty archives that added the instruments the first round had missed. Every document was labelled by a language model under a fixed 39-field codebook; governance documents were labelled from up to 110,000 characters of text with the collectors' metadata removed. Label consistency was measured five ways (second model, re-run, full text, metadata-blind input, extended input; median kappa 0.83 to 0.91); no human coding was available, and the labels are treated as consistent rather than certified. Comparisons between the 1,589 embodied-AI documents and the 982 general-AI documents are made within document genre and with covariate adjustment, because the collection design confounds the two sets with genre. Within this collection, embodied AI is governed by 808 instruments (681 robot-specific), of which 299 are legally binding and 268 in force; the binding layer is reached through sector law (aviation and drones, road traffic and automated driving, machinery and workplace safety, medical devices) and general AI law rather than robotics statutes, with one exception (El Salvador, 2025). A coverage audit against 38 reference instruments finds 31 captured (12 in the first collection); Korea's Intelligent Robots Act and the revised Product Liability Directive are among those still missing, so instrument counts remain lower bounds. Research and instruments attend to different robots: companion and social robots are 43% of embodied research outputs and 1.6% of embodied instruments (gap +41 points, bootstrap interval 37 to 46), drones 6% and 38% (−32, −36 to −28), autonomous vehicles 12% and 36% (−23, −28 to −19). The considerations that distinguish embodied governance (physical safety, human-robot proximity, liability for physical damage, autonomy-level control, conformity assessment and dual use) survive adjustment for genre, region and year (adjusted odds ratios 3.8 to 170), and, unlike in the first collection, most of the ethical core is less present in embodied documents of the same genre (odds ratios 0.18 to 0.68), with non-maleficence and human oversight the exceptions. Among instruments, embodied rules refer to technical standards (64% vs 36%), licensing and registration (36% vs 6%), conformity assessment (31% vs 11%) and insurance (10% vs 2%). Technical standards and binding instruments specify physical safety in depth in 47% and 46% of cases; autonomy-level control is raised by 43 to 69% of instruments of every type and specified in depth by 13 to 37%. On a common population, regions differ on the ethical vocabulary (beneficence, trust, privacy; bias-corrected Cramér's V 0.27 to 0.34) and on licensing and liability (0.28 to 0.33) more than on physical safety (0.15); Europe and North America are now distinguishable but remain nearest neighbours, and the Middle East (liability-led) and the international standards layer are distinct. Between 2020 to 2024 and 2025 to 2026, adjusted for genre and region, legal personhood falls (odds ratio 0.39) and industrial policy rises at the margin (1.61); the rise in cybersecurity reported from the first collection does not survive; risk-based tiering and conformity assessment grow about 9% and 5% per year, not significantly after correction; the terms "embodied AI" and "physical AI" rise from 1% to 12% of embodied documents. We release the codebook, annotations, master table, figures, dashboard and code, together with the six reviews, the round-2 companion report and a log of what changed.

</div>

## 1. Introduction

A large literature maps the principles and instruments of AI governance. Reviews of ethics guidelines found convergence on a small set of principles alongside divergence in implementation (Jobin, Ienca and Vayena 2019; Fjeld et al. 2020; Hagendorff 2020; Schiff et al. 2021; Corrêa et al. 2023), and the European Union's AI Act has become the reference point for binding regulation (Veale and Zuiderveen Borgesius 2021; Regulation (EU) 2024/1689). That literature is about software. An older literature on robot law and robot ethics argues that machines which act physically in the world raise distinct problems (Calo 2015; Leenes et al. 2017; Winfield and Jirotka 2018): bodily harm, proximity to people, liability for physical damage, the autonomy that may be delegated to a machine, and certification before market access. The RoboLaw guidelines (Palmerini et al. 2014), the European Parliament's 2017 resolution (European Parliament 2017; Nevejans 2016), the ISO safety standards for industrial, collaborative and personal-care robots (ISO 10218; ISO/TS 15066; ISO 13482), the Korean Intelligent Robots Act (2008), and sector regulation for vehicles (Taeihagh and Lim 2019) and drones (Stöcker et al. 2017) are the usual reference points; Holder et al. (2016), Bertolini (2020), Fosch-Villaronga and Mahler (2021) and Salvini et al. (2021) map the legal and safety regimes in detail.

The two literatures have rarely been brought together with numbers. Existing document collections, such as the OECD.AI policy observatory and the AlgorithmWatch inventory of ethics guidelines, do not separate embodied from general AI or code documents for the considerations that matter for machines. This paper asks five questions of a purpose-built collection: (Q1) what the documented governance of embodied AI consists of; (Q2) which robots are governed and which are only studied; (Q3) which considerations, tools and framings distinguish embodied-AI governance from general-AI governance once genre is accounted for; (Q4) how regions differ; (Q5) what is changing. It is a third version: the first was reviewed adversarially from six perspectives, the second reported what survived, and this version adds a second collection round that went looking for the binding instruments the second version's coverage audit showed were missing.

## 2. Background

**From principles to law.** Jobin et al. (2019) coded 84 guidelines; Fjeld et al. (2020) organised 36 into eight themes; Schiff et al. (2021) showed sectoral differences; Corrêa et al. (2023) extended the exercise to 200 documents and documented geographic concentration. Hagendorff (2020) argued the guidelines had little effect, which motivated binding instruments and the mechanisms of risk-based tiering, conformity assessment, audits, transparency obligations and oversight bodies. The OECD (2019) and UNESCO (2021) recommendations supply the intergovernmental layer.

**Robot law and standards.** Calo (2015) identified embodiment, emergence and social valence as what makes robots legally distinctive. Leenes et al. (2017) set out the regulatory challenges; Fosch-Villaronga and Heldeweg (2018) proposed iterative regulation. Specific debates concern care robots (Sharkey and Sharkey 2012; van Wynsberghe 2013), the privacy implications of social robots (Lutz, Schöttler and Hoffmann 2019), autonomous weapons (Sparrow 2007) and legal personality (Bryson, Diamantis and Grant 2017; Solaiman 2017). The standards community produced the operative texts: ISO 10218-1 and -2 (2011, revised 2025), ISO/TS 15066 (2016), ISO 13482 (2014) and, recently, ISO 3691-4, ISO 31101, ISO/PAS 8800 and ISO/IEC TR 5469; the EU Machinery Regulation (Regulation (EU) 2023/1230) and the AI Act's Annex I treat robots as products subject to harmonised standards.

**Language models as annotators.** Large language models can match crowd workers on text-annotation tasks (Gilardi, Alizadeh and Kubli 2023; Törnberg 2024), but their output is unstable across prompts and versions (Reiss 2023), requires validation against human labels (Pangakis, Wolken and Fasching 2023; Thalken et al. 2023), raises reproducibility concerns for proprietary models (Ollion et al. 2024), and carries measurement error that biases downstream estimates unless corrected (Egami et al. 2023; Angelopoulos et al. 2023). We meet part of that bar (fixed codebook, structured output, five consistency checks, stored inputs, repaired lexicons) and not the rest (no human gold standard, no measurement-error correction); Section 7 states the consequences.

## 3. Data

**Collection round 1.** Eight regional teams (Africa; Asia; Europe; Latin America and the Caribbean; Middle East; North America; Oceania; and an international layer assembled across teams) ran a *sprint* for robot-specific sources and a *database* of general AI-governance instruments between 2025 and October 2026, recording 2,160 sources in manifests and capturing 1,894 as 2,557 files; 266 sources could not be captured (109 in the European sprint).

**Collection round 2.** Prompted by the first round's coverage audit, a second round searched official legal databases, government repositories, standards catalogues, treaty-body archives and regulator sites for instruments the teams had not captured. Nine collector agents worked from regional, thematic and standards briefs, each given the round-1 holdings as an exclusion list, and seven legal databases were harvested by script (EUR-Lex through CELLAR, legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register of Legislation, the US eCFR and the Brazilian Câmara API). Candidates were de-duplicated on normalised URL and on normalised title plus jurisdiction, within the round and against the round-1 registry, leaving 2,075 (1,157 from the collector agents and 918 from the harvests; Table 50). Texts were fetched from the issuing source with secondary fallbacks: 1,716 texts were obtained, 16 of them standards' scope or abstract pages through a mirror, while 273 candidates returned HTTP errors or JavaScript-only pages, 46 sat on hosts that block the sandbox and 40 failed otherwise (Tables 51 and 52). Candidates without text remain in an inventory with their metadata and are not counted anywhere in this paper. All 1,716 texts were annotated with the same metadata-blind, extended-excerpt policy as the round-1 governance documents (Section 4); after a second title-based de-duplication pass across the merged collection, which also removed two round-1 documents, 1,637 entered the v3 collection (a net growth of 1,635, Table 53). The companion report describes the round in full.

**Processing.** Round-1 files were converted to text; 34 oversized or restricted files were recovered as text where possible (27). Duplicates were merged by content hash, URL, normalised title, truncated-title prefix and MinHash similarity on prose (Broder 1997), and, after review, by a second pass on normalised title and jurisdiction with years within one, yielding 1,656 canonical round-1 documents; 49 round-1 duplicate captures (the AI Act three times, its 2021 proposal twice, the Civil Law Rules twice, twelve copies of one Commission press release among them) and 79 round-2 duplicate captures are listed in the release. Documented corrections from the legal review (46 field changes, including the revocation of Executive Order 14110, the reclassification of catalogue pages as web pages and of bills as non-binding) were applied through a versioned override file; no manual overrides were applied to round-2 documents. With round 2 the collection holds 3,291 canonical documents, of which 3,148 have readable text and are on topic. Language was annotated from the text (75% English); Chinese, with 266 documents in the Asian set, is now the collection's second language (Table 14). DOIs were resolved against OpenAlex (Priem, Piwowar and Orr 2022) for 373 of the 582 research outputs.

**Analysis sets.** The embodied-AI set (n = 1,589) comprises usable documents rated 2 or 3 on a 0 to 3 relevance scale or carrying any robot-type label (244 enter by label alone; the strict set rated 2 or 3 has 1,345 documents, Table 32 in the report); the general-AI set (n = 982) comprises documents rated 0 or 1 with no label; 577 usable documents are in neither set because the annotation judged them not to be about AI at all (511 of them are governance instruments, 337 of them binding, mostly harvested legal texts; Table 1). Governance instruments (n = 1,691) are statutes, regulations, decrees, bills, strategies, standards, guidelines, resolutions and consultations with a lifecycle status and binding nature; government reports (251) are separate. Embodied instruments (808) are split into robot-specific (relevance 2 or 3; 681) and general-AI instruments with robot provisions (127). Regions follow the issuing jurisdiction; North America combines the United States, Canada and Greenland.

## 4. Methods

**Codebook.** Thirty-nine fields (supplement S2): bibliographic fields; jurisdiction and scope; 28 document types in 8 classes; governance-instrument status (nine states) and binding nature; AI scope and embodiment status; 23 robot types in 7 groups; 16 sectors; 27 topics; 14 core principles (Jobin et al.; OECD) and 6 embodied-specific considerations (physical safety, human-robot proximity, liability for physical damage, autonomy level and control, conformity assessment, dual use), each scored 0 absent, 1 mentioned, 2 specified in depth; 19 mechanisms; named instruments cited; personhood position; framing; stance; methodology; capture quality; relevance.

**Annotation.** Claude Sonnet 5.5 through the Claude Code command-line interface, codebook as system prompt, JSON schema enforcing every field, no tools; prompt hash recorded. Version 1 used a 14,000-character excerpt (first 10,000, middle 2,500, last 1,500) and passed the collectors' folder, title and language as metadata; review found that 483 texts also carried the collectors' labels in a cover block. Version 2 re-annotated all 351 round-1 governance documents with the cover block stripped, metadata reduced to a document id and word count, and up to 110,000 characters of text (74% of governance documents seen in full; median share seen 1.0 against 0.36 before), with the exact inputs stored. The 1,716 round-2 documents were annotated once under the same version-2 policy, so they are directly comparable with the re-annotated round-1 governance documents; technical standards were annotated on their public scope or abstract text, never on the normative text, and are flagged as such in the registry. Cost: 120 USD (v1), 32 USD (v2 runs) and 122 USD (round-2 runs, summed from the stored per-document cost fields).

**Consistency checks.** Against the annotations the analysis uses: Claude Opus 5.5 on the same v1 input (160 documents); Sonnet re-run (161); Sonnet on the full text (160); Sonnet metadata-blind and cover-stripped (160); and the v2 extended annotation against v1 for governance documents (351). Cohen's kappa, quadratic-weighted for ordinal fields, mean per-label for multi-label fields; unweighted and level-2 variants in the supplement. Cross-checks against the collectors' labels are reported but overstate independence because the labels were visible to the v1 annotator. The five checks draw on round-1 samples; for round 2 the only independent reference is the collectors' catalogue metadata, which the blind annotation did not see (Table 57).

**Lexicons.** Multilingual regular-expression lexicons for robot types, named instruments and principles over full text, repaired after review (a case-insensitive acronym matched the word "laws"; unbounded dual-use and harm patterns; the AI Act pattern absorbed state AI acts).

**Statistics.** Wilson intervals; chi-square with Monte-Carlo p-values when more than a fifth of expected counts are below five and Fisher's exact test for sparse 2 by 2 tables; bias-corrected Cramér's V (Bergsma 2013) with percentile-bootstrap intervals on a common population; Holm correction within families; logistic regression of each outcome on set membership adjusting for document class, region and year; Mantel-Haenszel tests stratified by class; genre-stratified comparisons; bootstrap intervals for the governance-gap index (research share minus instrument share) and for regional cosine distances, with split-half noise floors; logistic trend models with sensitivities (excluding the partial year 2026; stated-date documents only). K-means bundles were examined and not interpreted (silhouette 0.17 at k = 5).

## 5. Results

**What round 2 changed.** Table 53 sets the two collections side by side. Round 2 doubled the collection (1,656 to 3,291 annotated documents) and left the research side untouched (581 to 582 research outputs) and the general-AI set nearly so (806 to 982), but it multiplied the governance side: embodied-AI instruments rose from 65 to 808, robot-specific instruments from 34 to 681, binding embodied instruments from 5 to 299 and jurisdictions with an embodied instrument from 30 to 60. Of the 1,611 usable round-2 documents, 1,346 are governance instruments and 647 are robot-specific (Table 56); the additions are concentrated in Europe (26 to 220 embodied instruments), the international layer (9 to 197), Asia (10 to 170), North America (6 to 122) and Oceania (1 to 56), and in the vehicles-and-field robot group (48 to 589 instruments; Tables 54 and 55 in the companion report). The coverage audit moved from 12 to 31 of 38 reference instruments captured. Every result below is for the merged collection, and the text says where a v2 finding changed; the companion report documents sources, fetch outcomes, blocked hosts and collector-metadata agreement and is not repeated here.

{{T53}}

### 5.1 What the documented governance of embodied AI consists of (Q1)

{{F01}}

The embodied-AI set is 32% research outputs (509 of 1,589) and 51% governance instruments (808); academic issuers account for 32% of it (516), national executives 17% (265), standards bodies 14% (230) and intergovernmental organisations 14% (228). The general-AI set is 39% communications (381 of 982) and 25% voluntary guidance (241), with 50 research outputs (Figure 1). The composition mirrors the two collection rounds (round 1 supplied the research, round 2 the instruments) and is why Sections 5.3 to 5.5 compare within genre.

{{F04}}

{{T33}}

Of the 808 instruments that reach robots, 434 are soft law (238 technical standards and 196 guidelines, strategies and codes), 75 proposals or drafts and 299 legally binding; among instruments with a settled nature the binding share is now far higher in the embodied set than in the general set (304 of 764 vs 55 of 323; chi-square p < 0.001, V = 0.44), where v2 had found the two shares similar. Of the 299 binding instruments, 223 are regulations or decrees and 72 statutes (plus 3 court decisions and 1 treaty); 268 are in force, 24 superseded or repealed and 7 adopted but not yet in force. They are dominated by aviation and drone rules (172 mention drones) and by road-traffic and automated-driving law (100 mention autonomous road vehicles), with smaller sets on machinery and workplace safety (17 mention industrial manipulators), personal-delivery devices (15), policing drones (14) and surgical or medical robots (9); the United States (69), the European Union (56), Australia (48) and Japan (26) supply two thirds (supplement Table S1). The set also holds the general-AI instruments that reach robots through their product lists: the EU AI Act, Executive Order 14110 (revoked January 2025) and Regulation (EU) 2026/1744 amending the AI Act and the Machinery Regulation. El Salvador's Robotic Technologies Law (2025, in force) remains the only binding instrument with "robot" in its title. Of the 677 robot-specific instruments among the 804 content-analysed captures in Table 33, 320 are substantive captures, 175 partial and 182 landing or catalogue pages, the last concentrated among standards annotated on their public scope text.

{{F06}}

{{F41}}

Dated instruments from 2010 onwards accumulate as in Figure 6: binding instruments from 4 (2012) to 283 by 2026, voluntary guidance from 1 (2010) to 220, technical standards from 1 (2011) to 231 and drafts from 1 (2013) to 61; a further 16 binding instruments predate 2010 (Japanese road, vehicle and aviation statutes of the 1950s and 1960s, EU machinery and medical-device directives). The coverage audit (Figure 41, Table 25) remains the necessary corrective even after round 2: of 38 reference instruments and standards relevant to embodied AI, {{AUDIT}}. Round 2 brought in the UK Automated Vehicles Act 2024, Germany's 2021 autonomous-driving law, Japan's Level-4 regime, UN Regulation 157, the EU drone rules, the Machinery Regulation, ISO 10218 and ISO/TS 15066, all missing in v2. Still missing are seven: Korea's Intelligent Robots Act, the revised Product Liability Directive (EU) 2024/2853, ANSI/RIA R15.06, ANSI/A3 R15.08, Korea's AI Basic Act, the OECD AI Principles as a document and Taiwan's industrial-robot hazard-prevention standards. Instrument counts in this paper therefore remain lower bounds, and what the collection shows reliably is the *route* by which binding law reaches robots: sector law (aviation, road traffic, machinery and workplace safety, medical devices) and general AI law, not robotics statutes.

{{F07}}

Europe supplies 42% of usable documents (1,332 of 3,148) and 48% of them are embodied; Asia 661 (45% embodied); North America 345 (63%); Latin America 149 (24%); the Middle East 98 (46%); the international layer 374 (64%); Africa 75 (35%); Oceania 113 (73%) (V = 0.21). Of 116 countries with a document, 78 contribute an instrument, 58 an embodied instrument and 45 a binding instrument of any kind (40 a binding embodied instrument); the United States (100), China (94), Japan (53), Australia (50) and the United Kingdom (49) hold the most embodied instruments (Table 4). Non-English documents are more often governance documents (67% vs 49%; n = 776 and 2,372).

### 5.2 Which robots are governed and which are studied (Q2)

{{F11}}

{{F40}}

{{T22}}

Autonomous road vehicles are now the most addressed type (432 documents), then drones (406), companion and social robots (239), care robots (211), industrial manipulators (208), professional service robots (200), military weapons (193), humanoids (164), surgical robots (145) and collaborative robots (114). The governance-gap index with bootstrap intervals (Figure 40, Table 22) separates three groups: studied far more than governed (social and companion robots, +41, 37 to 46, with 13 instruments and none binding; care robots +22, 18 to 26; humanoids +19, 16 to 23, no longer within sampling error of zero; professional service and surgical robots +9 each; educational, domestic and sex robots +4 to +5); near parity, with intervals including zero (military weapons +2, collaborative robots +1, security and rehabilitation robots, industrial manipulators −3, −6 to 1); governed far more than studied (drones −32, −36 to −28; vehicles −23, −28 to −19; mobile logistics, maritime and rail, agricultural and delivery robots −2 to −4, all intervals excluding zero). Round 2 rearranged the groups: v2, with 65 embodied instruments, had industrial manipulators (−36), collaborative, surgical and military robots governed far more than studied; with the instrument side now dominated by drone and vehicle law those gaps closed, the vehicle gap shrank from −54 to −23 and the social-robot gap widened from +37 to +41. Regions and genres attend to different machines: social robots are European (26% of Europe's embodied documents) and North American (15%); humanoids have their highest shares in the Middle East (22%) and Asia (15%); drones dominate Oceania (66%), Africa (62%) and Latin America (53%); voluntary guidance mentions vehicles in 37% of cases and research in 12%, and binding instruments mention drones in 58%. Within the embodied set, social robots fall from 20% of documents in 2020 to 2022 to 11% in 2025 to 2026 and humanoids rise from 8% to 16% (Figure 42 in the report).

### 5.3 Considerations, tools and framings (Q3)

{{F39}}

{{F38}}

{{T20}}

{{T34}}

Pooled over all documents, 17 of 20 principle differences are Holm-significant, but pooled differences are genre differences. Within governance instruments (804 vs 367; Figure 39, Table 21 in the report), five of the six embodied-specific considerations differ sharply (physical safety 81% vs 8%, conformity assessment 59% vs 17%, autonomy-level control 53% vs 9%, proximity 28% vs 0.3%, liability for physical damage 18% vs 2%; all Holm-significant; dual use, 15% vs 11%, does not), and, unlike in v2, eleven of the fourteen core principles are lower among embodied instruments (from accountability, 53% vs 75%, to justice and fairness, 14% vs 67%; all Holm-significant), while non-maleficence (80% vs 77%), human oversight (43% vs 47%) and robustness (63% vs 71%) do not differ. Within research outputs (509 vs 50) four of the six considerations differ (physical safety 43% vs 0%, proximity 71% vs 4%, liability 25% vs 0%, autonomy-level control 42% vs 6%; conformity assessment and dual use do not at these sizes) and inclusive growth is lower (22% vs 52%). Adjusting for class, region and year (Table 20), the embodied-specific considerations keep very large odds ratios (proximity 170, physical safety 75, liability 27, autonomy-level control 21, conformity assessment 7.3, dual use 3.8); among core principles eleven are lower after adjustment (odds ratios from 0.18 for justice and fairness to 0.68 for accountability), non-maleficence (2.0) and human oversight (1.5) are higher, and robustness does not differ (1.04). The Mantel-Haenszel analysis stratified by class (Table 34) agrees (accountability 0.60, inclusive growth 0.28, non-maleficence 1.84, human oversight 1.32, robustness 0.91 and not significant). The v1 claim that accountability did not differ was a Simpson's paradox.

{{F23}}

{{T09}}

Figure 23 (content-analysed captures only) and Table 9 show which document types specify the embodied considerations. Technical standards (238, annotated on scope text) mention physical safety in 80% of cases and specify it in depth in 47%; binding instruments (299) mention it in 87% and specify it in 46%, with conformity assessment specified in 38% and liability in 12%; voluntary guidance (196) mentions physical safety in 73% and specifies it in 35%. Autonomy-level control is mentioned by 43 to 69% of every instrument type and specified in depth by 37% of drafts, 21% of voluntary instruments, 18% of binding instruments and 13% of standards; standards almost never address liability (1.7%, none in depth) or dual use (0.4%). These statements rest on the extended annotation: for the 351 round-1 governance documents it raised the number of mechanisms, robot types and named instruments found per document by 15 to 60% while leaving binding and status labels unchanged for more than 95% of documents (Table 35 in the report), and the round-2 documents were annotated under the same policy from the start.

{{F24}}

{{T10}}

Among instruments, embodied rules refer to technical standards (64% vs 36%), use licensing and registration (36% vs 6%), conformity assessment (31% vs 11%) and insurance requirements (10% vs 2%) significantly more often (Figure 24, left, and Table 10, shares among 812 embodied and 373 general governance documents; Holm significance from the instrument stratum of 804 vs 367 in Table 21 in the report, whose shares differ by at most one point); testing and sandboxes, which differed in v2, no longer do (27% vs 30%); international cooperation (23% vs 54%), audits (30% vs 55%), oversight bodies (24% vs 52%), education, funding, labelling, data governance, risk-based tiering (12% vs 24%) and self-regulation are lower; human-oversight requirements, incident reporting, prohibitions and liability regimes do not differ at these sizes. The adjusted models confirm licensing (10.2), insurance (9.7), conformity assessment (4.6), standards references (3.6), liability regimes (3.1) and prohibitions (2.3), and reverse the v2 result for funding (0.53, lower after adjustment).

{{F29}}

Two reference ecosystems: general-AI documents cite the AI Act (29%), the GDPR (21%), the OECD principles (14%) and the UNESCO Recommendation (10%); embodied documents cite the GDPR (9%), the UN CCW process (6% vs 0.2%), the AI Act (6%), the Civil Law Rules on Robotics (4% vs 0.6%), the Machinery Regulation (3%), the Product Liability Directive and ISO 10218 (2.6% each), ISO 13482 (2.1%), the IEEE 7000 series (1.8%) and ISO/TS 15066 (1.5%); any named instrument is cited by 28% of embodied and 53% of general documents. Framing is ethics-led in Europe (35% of 554 framed documents), risk-led in North America (31% of 167), Oceania (64% of 53), Latin America, Africa and the international layer, split between risk and innovation promotion in Asia (37% and 33% of 235) and liability-led in the Middle East (59% of 41) (V = 0.23); of the 480 embodied research outputs that take a stance (excluding "not applicable"), 56% take no regulatory position, 31% call for new regulation and 4% argue existing law suffices.

### 5.4 Regional comparison (Q4)

{{T29}}

{{F31}}

On a common population (embodied documents, six regions, n = 1,527; Table 29), regions differ most on beneficence (bias-corrected V 0.34, interval 0.30 to 0.38), references to standards (0.33), licensing (0.33), trust (0.30), liability regimes as a tool (0.28, 0.20 to 0.36), privacy and freedom (0.27), accountability (0.25), liability for physical damage and justice (0.24); the physical-harm vocabulary varies less (physical safety 0.15, non-maleficence and conformity assessment 0.14, autonomy-level control 0.13, human oversight 0.12), and five procedural tools (the conformity-assessment mechanism, labelling, human-oversight requirements, self-regulation, audits; V 0.01 to 0.07, Holm p ≥ 0.18) not detectably. The v2 finding that regions agree on the ethical core and differ on liability and control does not survive the larger collection: on the common population the ethical vocabulary now varies by region more than the physical-safety vocabulary does, and liability varies with it. Cosine distances (Figure 31) place Europe and North America 0.039 apart (0.028 to 0.061), above both split-half noise floors (0.008 and 0.021), so the two regions v2 could not tell apart are now distinguishable, though North America remains Europe's nearest neighbour in 99% of resamples; the Middle East sits 0.071 from North America, within its own noise floor (0.078), and 0.104 from Europe; the international layer (0.194 from Europe) and Oceania (0.175) are distinct, with nearest neighbours stable in 100% and 74% of resamples. Restricting to research outputs returns Europe and North America to 0.010 apart, so their separation comes from the instrument layer, while the Middle East stays distinct (0.18 from Europe); the international layer has no research outputs and drops out of that comparison.

### 5.5 Trends (Q5)

{{F34}}

{{T28}}

{{T30}}

Comparing 476 embodied documents from 2025 to 2026 with 737 from 2020 to 2024, crude shares rise for industrial policy (+9 points), certification and conformity assessment (+7), physical safety (+6) and standards (+6) and fall for ethics principles (−14), human-robot interaction (−10), human dignity (−6) and personhood (−5); industrial policy, ethics principles, human-robot interaction and personhood are the Holm-significant crude changes (Table 16 in the report), and cybersecurity, which rose 12 points in v2, moves 2 points. Adjusted for document class and region (Table 28), personhood (odds ratio 0.39, Holm p = 0.04) survives, industrial policy is at the margin (1.61, p = 0.08; its research-only share moves from 9% to 13%), ethics principles do not (0.64, p = 0.16), and cybersecurity (1.14) and human oversight (1.06) are flat, so the v2 cybersecurity finding was a property of the smaller collection. Trend models (Table 30) show the risk-based-tiering mechanism rising about 9% per year (odds ratio 1.09, 1.02 to 1.17; 1.10 excluding 2026, 1.07 on stated-date documents) and the conformity-assessment mechanism about 5% (1.05, 1.00 to 1.10; 1.05 and 1.06), far below the 30% per year of v2 and neither Holm-significant in the main model (Table 17 in the report); physical safety (1.00) and autonomy-level control (0.97) are flat, while proximity (0.93) and liability for physical damage (0.93) decline by about 7% per year after adjustment (Holm p = 0.003 and 0.007). Within the embodied set, the terms "embodied AI" and "physical AI" appear in 1.0% of 2024 documents (2 of 191), 7.9% of 2025 documents (17 of 216) and 11.9% of 2026 documents (31 of 260) (Figure 33 in the report), lower than the v2 shares (2%, 14%, 23%) because the embodied set now includes the round-2 instruments.

### 5.6 Consistency of the labels

{{F43}}

{{T26}}

Against the annotations used (round-1 samples), a second model agrees at a median kappa of 0.85 (minimum 0.61, page quality; 11 of 46 fields below 0.80); a re-run at 0.91 (0.66); full text at 0.88 (0.71), finding 0.1 to 0.4 more labels per document and agreeing less on documents the excerpt truncated (median principle kappa 0.75 vs 0.84); the metadata-blind, cover-stripped input at 0.90 (0.65, date basis), with country, issuer and language labels little changed; and the v2 extended annotation of governance documents at 0.83 against v1, moving robot-type labels (0.60), stance (0.55) and publication stage (0.49) most. Round-2 documents were not in these samples; against the collectors' catalogue metadata, which the annotator did not see, the blind annotation agrees on binding nature in 93% of 1,593 documents (kappa 0.85), on jurisdiction in 98% (1,609), on year within one year in 93% (1,527) and on document class in 80% (kappa 0.71; 1,593), the disagreements concentrated in parliamentary material, consultations and guidelines (Table 58 in the companion report). Repaired lexicons agree with the annotations at median kappa 0.40 to 0.43 over 2,696 documents, and the Spearman correlation of embodied-minus-general differences across principles is 0.88. Headline quantities are reported under eleven subsets and a strict set definition (Tables 19 and 32 in the report); the strict set (n = 1,345) gives the same research share (33%), a higher physical-safety share (72% vs 67%) and the same social-robot gap (44% of research outputs against 11 instruments).

## 6. Discussion

**Embodied-AI governance has a binding sectoral layer, a standards spine and a research discourse, and the binding layer still reaches robots sideways.** Round 2 changed the count and not the route. Half of the embodied documents are now instruments, 299 of them binding, and almost all of that binding law is aviation and drone regulation, road-traffic and automated-driving law, machinery and workplace-safety rules and medical-device law, joined by general AI law that reaches robots through its product lists; the one robotics statute is still Salvadoran. The v2 count of four binding instruments in force was an artefact of a collection built by teams searching for robot-specific texts; with 31 of 38 reference instruments now captured and Korea's Intelligent Robots Act, the revised Product Liability Directive and the ANSI/RIA standards still missing, a reader should take the route as the finding and the count as a floor.

**The body is what distinguishes embodied governance, and it survives the confound; the ethical vocabulary does not travel with it.** Once genre, region and year are accounted for, the six embodied-specific considerations remain the largest differences in the data (odds ratios 3.8 to 170). What changed with round 2 is the core: in v2, no core principle differed within governance instruments; with 804 embodied instruments against 367 general ones, eleven of fourteen core principles are less present in embodied documents of the same genre, and only non-maleficence and human oversight are more present. Earlier guideline reviews found convergence on transparency, fairness and non-maleficence; our results say that the harm-avoidance part of that convergence extends to robots, while the rights-and-fairness part is largely absent from the vehicle, drone and machinery law that governs them. Robots are governed in the language of product safety more than in the language of AI ethics.

**Specification lags mention, and standards and binding law are the specifiers.** With the instruments read nearly in full, standards specify physical safety in depth in 47% of cases and binding instruments in 46%, binding instruments specify conformity assessment in 38% and liability in 12%, voluntary guidance mentions more than it specifies, and autonomy-level control, raised by 43 to 69% of every instrument type, is specified in depth by 13 to 37%, highest among drafts. The vehicle laws that the governance expert's review named as the place where autonomy levels are specified (the German and UK statutes, UN Regulation 157) are now in the collection; even so, binding instruments specify autonomy-level control in depth in only 18% of cases, so most of the binding layer still mentions the level of autonomy without specifying it, and the standards' shares describe their public scope statements rather than their normative clauses.

**Research and rules point at different robots.** Vehicles, drones, arms and medical robots inherited regimes; companion and social robots did not, and after two decades of research they have thirteen instruments in this collection, none binding. The gap widened with round 2 because the instrument side grew around drones and vehicles. General regimes (product safety, toys, data protection, the AI Act's transparency and vulnerability provisions) apply to social robots; the gap is in robot-specific instruments and in the research community's engagement with existing law (4% of papers argue it suffices).

**Regions differ on values and on tools, and the differences are now measurable.** The common-population analysis of v2, on 647 embodied documents, found agreement on the ethical core and disagreement on liability and control. On 1,527 documents the picture reverses: beneficence, trust, privacy, freedom, accountability and justice vary by region (V 0.24 to 0.34), as do references to standards, licensing and liability regimes, while the items that vary least are four procedural tools (audits, self-regulation codes, human-oversight requirements and labelling; V 0.01 to 0.05, not significant after Holm correction) and, among principles, dual use (0.09) and human oversight (0.12). Europe and North America can now be told apart, though they remain each other's closest profiles; the Middle East's liability-led literature, Oceania's drone-licensing law and the international standards layer are distinct. Part of that signal is which instruments each region's databases made available to round 2 (Section 7).

**The frontier.** After adjustment, the 2025 to 2026 shift is away from the personhood debate and, at the margin, toward industrial policy; the rise in cybersecurity that v2 reported does not survive the larger collection, and the growth of risk tiers and conformity assessment is slower than v2 estimated and not significant after correction. The physical-harm considerations are constant or, for proximity and liability for physical damage, declining by about 7% per year after adjustment for genre and region; the vocabulary of "physical AI" is arriving in the documents, at 12% of embodied documents in 2026 (6% of all documents) rather than the 23% v2 saw in a research-heavy collection.

## 7. Limitations

The collection is purposive, European and English-heavy (75% English), still missing known binding instruments, and its design confounds the embodied and general sets with genre twice over: the round-1 sprint-versus-database split confounded them in one direction, and round 2 added instruments without adding research, so the within-genre and adjusted analyses address a larger confound than in v2 and cannot remove it. All labels come from one proprietary model family without a human gold standard; the five consistency checks bound instability but not validity, were run on round-1 samples, and downstream estimates are not corrected for measurement error (Egami et al. 2023; Angelopoulos et al. 2023). The relevance field that defines the sets was produced by the same model as the outcomes. The extended annotation still truncates the longest governance documents. About one in six dated embodied documents has a date inferred from content (Table 30); 2026 is partial. Small groups are reported as counts and conclusions about them are tentative. The instrument scheme does not record whom an instrument binds, applicability dates or the legal effect of standards (harmonised, incorporated, mandatory), which the governance review recommends for a policy-grade inventory.

Round 2 adds limitations of its own. Its coverage is bounded by what the sandbox could reach: 46 candidates sat on hosts that block automated access and 273 returned errors or script-only pages, EUR-Lex (59), the Chinese NPC law database (27), the UNODA library, Légifrance and the Korean law portal (17 each) among them (Table 52), so France, Korea, Taiwan, Singapore and several ministry sites are under-represented, and the 359 inventory items without text are not counted anywhere. Every collector agent reported that the shared web-search budget was exhausted part-way through its brief, after which it worked only from official databases and direct fetches; each agent's list of instruments it could not find or verify is in the companion report. Technical standards were annotated on their public scope or abstract text, never on the normative text, so their principle and mechanism shares describe what a scope statement says. The round-2 labels have no reliability sample; the collectors' catalogue metadata, the only independent reference, agrees with the blind annotation on binding nature (93%, kappa 0.85) and jurisdiction (98%) but less well on document class (80%, kappa 0.71; Table 57), and comparisons that depend on class labels inherit that uncertainty. Finally, the scripted harvests returned many legal texts that are not about AI; the 577 usable documents in neither analysis set were excluded by relevance labels from the same model as everything else.

## 8. Conclusion

With 3,291 documents from eight regions collected in two rounds, a 39-field codebook, model annotation checked five ways, repaired lexicons and genre-aware statistics, this study gives a quantitative map of embodied-AI governance as it appears in a purpose-built collection and states clearly where the collection ends. The map shows a binding sectoral layer that reaches robots sideways, a standards spine, a research discourse, a harm-avoidance vocabulary that survives every adjustment, an ethical vocabulary that largely does not, a product-safety toolkit, a social-robot gap, regional differences on values and tools alike, and a frontier moving away from personhood and toward industrial policy and physical AI. The release, the six reviews, the round-2 companion report and the change log allow each claim to be re-examined and the collection to be extended where the audit shows it is still thin.

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

Analysis report (all figures and tables with narrative, including the three round-2 figures and eleven round-2 tables), the round-2 companion report (sources, fetch outcomes, blocked hosts, before-and-after tables, collector-metadata agreement and the lists of newly captured instruments), supplement (codebook, taxonomies, five-way reliability, instrument lists, coverage audit, datasheet, human-validation protocol), the six reviews and the review-and-changes log, master table, round-2 inventory, dashboard, per-document annotations with stored inputs, and all scripts are provided in the release.
