---
title: "Governing machines that act in the world: analysis report (v3)"
subtitle: "How embodied AI and robotics are governed, from 3,291 documents in eight world regions, after six independent adversarial reviews"
author: "Prepared with Claude Code for Jimmy Lin, Centre for Enterprise Innovation (CEI) AI Robotics project"
date: "31 October 2026"
---

## Key numbers

| | |
|---|---|
| Files collected by eight regional teams (round 1) | 2,557 (1,894 of 2,160 listed sources captured) |
| Round-2 candidates / with text / usable after annotation | 2,075 / 1,716 / 1,611 (Tables 50, 51, 53) |
| Unique documents after deduplication and corrections | 3,291 annotated (128 duplicate captures removed: 49 round-1, 79 round-2) |
| Usable documents (text readable, on topic) | 3,148 |
| About robots or embodied AI ("embodied-AI set") | 1,589 (509 research papers, 808 rules and policies) |
| About AI in general ("general-AI set") | 982 (50 research papers, 372 rules and policies) |
| In neither set (rated not about AI; 520 of them round-2 sector law) | 577, excluded from every set comparison |
| Rules and policies that reach robots | 808: 681 robot-specific, 127 general-AI instruments with robot provisions (Table 53; Table 33 tiers the 804 also flagged as governance documents) |
| Legally binding and in force, reaching robots | 268 of the 299 binding instruments (Table S01; Table 2 counts 271 legally binding texts in force on the binding-nature basis), mostly vehicle, aviation, workplace and product-safety law and national drone and automated-driving rules |
| Countries with any document / with an instrument / with a binding instrument | 116 / 78 / 45 |
| Share of documents from Europe / in English / in Chinese | 42% / 75% / 8% (266 documents, 259 of them from round 2) |
| Labelling | AI model under a fixed 39-field codebook; no human coding; five reliability checks (see Part F) |

**How to read this report.** Everything was labelled by a language model, so the labels are consistent across models and re-runs but not certified by human coders. Round 1 of the collection sought research on robots and official texts on AI in general; round 2 sought the instruments round 1 had missed, so comparisons between the two sets are made within document genre or adjusted for it wherever they matter. Counts of instruments are counts *in this collection*: an audit shows it now captures 31 of 38 reference instruments (12 in version 2 by the same corrected patterns; the v2 audit reported 10), but they remain lower bounds. Percentages are given as counts wherever a group has fewer than 30 documents. Plain-language definitions are in the glossary at the end; the full codebook and every supporting table are in the supplement; the second collection round has its own companion report.

## Five findings

1. **Binding law reaches robots through sector law, and after round 2 it is no longer rare in the collection.** Of 808 rules and policies that reach robots, 299 are legally binding, 196 voluntary guidance, 238 technical standards and 75 drafts; 268 of the binding ones are in force (Table S01). The binding layer is sector law: 223 regulations or decrees and 72 statutes (Table S01), 271 of the 299 addressing vehicles, drones or other field machines (Table 55); general robotics statutes such as El Salvador's remain exceptions. Robot instruments are now more often binding than general-AI instruments (304 of 764 vs 55 of 323 with a settled nature; Cramér's V 0.44), reversing the v2 reading that the sets differed in volume but not in propensity to legislate. (Figures 4 and 6; Tables 2, 33, 53, 59.)
2. **Research and rules point at different robots.** Companion and social robots are the subject of 43% of robot research papers (219 of 509) but 13 of the 808 instruments, none binding; drones are 6% of research and 38% of instruments (312; 172 binding); self-driving vehicles 12% and 36% (293; 100 binding). These gaps are far outside their bootstrap intervals (+41 points, interval 37 to 46; −32, −36 to −28; −23, −28 to −19). Humanoids have 164 documents, 27 instruments and one binding instrument (gap +19, interval 16 to 23); industrial manipulators, "governed far more than studied" in v2, are at parity (−3, interval −6 to +1). (Figures 18 and 40; Tables 7 and 22.)
3. **What is distinctive about robot governance is the body; the ethical core is thinner in robot rules even within genre.** Within governance instruments (804 vs 367), physical safety (81% vs 8%), autonomy-level control (53% vs 9%), conformity assessment (59% vs 17%), human-robot proximity (28% vs 0.3%) and liability for physical damage (18% vs 2%) are far more often raised in robot instruments (adjusted odds ratios 4 to 170), while transparency (33% vs 74%), fairness (14% vs 67%), privacy (24% vs 66%) and eight other core principles are raised less often; after adjustment for genre, region and year, 13 of 14 core principles differ. Robot rules refer to standards (65% vs 35%) and use licensing (36% vs 7%), conformity assessment (32% vs 11%) and insurance (10% vs 2%); general-AI rules rely on audits (55% vs 30%), oversight bodies (51% vs 23%), labelling (41% vs 15%) and risk tiering (23% vs 12%). (Figures 20, 24, 38, 39; Tables 20, 21, 34.)
4. **Specification lags mention, but less than in v2.** Physical safety is set out in detail by 47% of technical standards (n = 238), 46% of binding instruments (n = 299), 35% of voluntary guidance (n = 196) and 24% of drafts (n = 75). Autonomy-level control is raised by 43 to 69% of instruments of every type and set out in detail by 18% of binding instruments, 21% of guidance, 13% of standards and 37% of drafts; liability for physical damage is absent from standards. (Figure 23; Tables 9 and 35.)
5. **Regions differ on values as well as on liability and control; the newest shift is away from ethics discourse, not toward cybersecurity.** On a common population of 1,527 embodied documents in six regions, 33 of 38 principles and mechanisms differ after Holm correction (bias-corrected V 0.08 to 0.34), led by beneficence, standards references, licensing, trust and liability regimes; only the procedural toolkit (audits, self-regulation, oversight requirements, labelling, the conformity-assessment mechanism) does not. Between 2020 to 2024 and 2025 to 2026, after adjustment for genre and region, legal personhood falls (odds ratio 0.39) and industrial policy rises at the margin (1.6, Holm p = 0.08); the v2 rise in cybersecurity is absent (1.1). Risk-based tiering grows about 9% a year, not significantly after correction; "embodied AI" vocabulary rises from 1% of embodied documents in 2024 to 12% in 2026. (Figures 21, 25, 29 to 34, 42; Tables 28 to 31.)

## 1. Scope, questions and definitions

The brief asked for a metric-heavy analysis of AI governance in the context of robotics, physical AI and embodied AI: development over time, regional differences, dominant views and principles, the newest trends, and how different robot types are governed, with a taxonomy of robots, a taxonomy of documents (including governance-instrument status) and a document dashboard. Version 1 delivered these; six independent adversarial reviews found the discourse-level findings defensible and the instrument-level and reliability claims not. Version 2 corrected the data, restricted every embodied-versus-general comparison to within-genre or adjusted estimates, re-annotated every governance document from much longer text without the collectors' labels, repaired the statistics and the lexicons, and rewrote the claims. Version 3 adds a second collection round aimed at the instruments the first collection had missed and re-runs every analysis on the merged collection; the companion report (`report/src/collection_round2.md`) describes the round and Section 3 summarises what it changed. The review log maps every finding to a change.

Definitions used throughout:

- **Usable documents** (3,148): annotated documents with readable text that are neither failed captures nor off-topic.
- **Embodied-AI set** (1,589): usable documents rated at least moderately relevant to embodied-AI governance (2 or 3 on a 0 to 3 scale) or carrying at least one robot-type label; 1,345 by relevance, 244 by category label alone. A strict definition (relevance only) is reported as a sensitivity.
- **General-AI set** (982): usable documents rated 0 or 1 with no robot-type label. A further 577 usable documents, 569 of them rated not about AI at all (520 round-2 captures of sector law), are in neither set and enter only the all-document counts.
- **Rules and policies** ("governance instruments", 1,691 usable): statutes, regulations, decrees, strategies, guidelines, codes, standards, resolutions and consultations, with a lifecycle status and a binding nature. Government and parliamentary reports (251) are counted separately. **Robot-specific instruments** are those rated relevance 2 or 3 (681 in the embodied set; 677 of the 804 that also carry the governance-document flag in Table 33); **general-AI instruments with robot provisions** are rated 0 or 1 but carry robot-type labels (127).
- **Regions** follow the issuing jurisdiction (first author's country for research; Europe for EU bodies; International for ISO, IEC, IEEE, UN, OECD, UNESCO and WHO): Europe (including Russia), Asia, North America (United States, Canada, Greenland), Latin America and the Caribbean, Middle East, Africa (including Egypt and the African Union), Oceania, International.
- **Content-analysed captures** are substantive or partial captures; catalogue, committee and landing pages count in the instrument inventory but are excluded from statements about what instruments say. Technical standards from round 2 are annotated on their public scope text only.

## 2. Data and methods in brief

The full pipeline is in the supplement (S1). In outline: in round 1 the eight regional teams listed 2,160 sources and captured 1,894 as 2,557 files; files were converted to text, deduplicated (hash, URL, title, prefix and prose similarity, then a second pass on normalised title and jurisdiction after review), and every document was annotated by Claude Sonnet 5.5 against a 39-field codebook as a fixed system prompt with a JSON schema. In version 2 every governance document was re-annotated with the collectors' cover block stripped, minimal metadata and up to 110,000 characters of text, which covers 74% of governance documents in full.

Round 2 searched for instruments rather than discourse. Nine collector agents worked from regional, thematic and standards briefs with exclusion lists of the round-1 holdings, and scripted harvests of seven legal databases (eight runs) queried EUR-Lex (CELLAR SPARQL), legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register of Legislation, the US eCFR and the Brazilian Câmara API; title-searched harvests were keyword-filtered before fetching, full-text harvests were not. Candidates were de-duplicated on normalised URL and on normalised title plus jurisdiction, within the round and against the round-1 registry; the assembly step's title pass across the merged collection then removed a further 79 round-2 candidates as duplicates of round-1 documents. Texts were fetched from the primary URL with a documented fallback route where it failed; for standards only the public scope text is available. Of 2,075 candidates, 1,716 yielded text and 359 did not (273 HTTP errors or thin pages, 46 blocked hosts, 40 failed fetches; Tables 51 and 52); candidates without text stay in an inventory (`data/round2_inventory.csv`) and are counted nowhere. All 1,716 were annotated under the same blind, extended-excerpt policy, model and prompt hash as the v2 governance re-annotation, with no manual overrides; 1,611 are usable. The blind labels agree with the collectors' catalogue metadata on binding nature in 93% of 1,593 documents (kappa 0.85), on jurisdiction in 98% (n = 1,609), on year within one year in 93% (n = 1,527) and on document class in 80% (kappa 0.71; Tables 57 and 58).

Seventy-nine documented field corrections on 27 documents and 128 duplicate captures removed (49 round-1, 79 round-2) were applied through a versioned override file. Reliability was measured five ways on round-1 samples: a second model on the same excerpt (160 documents), the same model re-run (161), the same model on the full text (160), the same model with the collectors' labels removed (160), and the extended re-annotation against the original for governance documents (351). Full-text keyword lexicons, repaired after review, provide a model-free check. Statistics use Wilson intervals; chi-square tests with Monte-Carlo p-values for sparse tables and Fisher's exact test for sparse 2 by 2 tables; bias-corrected Cramér's V with bootstrap intervals; Holm correction within each family; logistic regression adjusting for document class, region and year; Mantel-Haenszel tests stratified by class; bootstrap intervals for the governance-gap index and for regional distances, with split-half noise floors.

## 3. What collection round 2 changed

{{T53}}

{{F51}}

The companion report gives the round in full; here is what matters for reading the rest. The blind annotation classed 1,346 of the 1,611 usable round-2 documents as governance instruments, 647 of them robot-specific, and one as a research output (Table 56; Figure 50 shows the funnel). Across the merged collection, embodied-AI instruments rose from 65 to 808, robot-specific instruments from 34 to 681, binding instruments reaching robots from 5 to 299 (binding and robot-specific from 4 to 244), voluntary guidance and standards from 50 to 434, drafts from 10 to 75 and government reports from 24 to 90; jurisdictions with an embodied instrument doubled from 30 to 60 (Table 53). The general-AI set grew by 176 documents and the research literature by one paper, so the research-side numbers of v2 are essentially unchanged; the coverage audit moved from 10 to 31 of 38 reference instruments captured (12 to 31 once the corrected title patterns are applied to v2 as well). The additions are concentrated by region (Table 54, Figure 51): Europe's embodied instruments went from 26 to 220, Asia's from 10 to 170, North America's from 6 to 122, the international standards layer's from 9 to 197 and Oceania's from 1 to 56, whereas Latin America (7 to 23), Africa (2 to 11) and the Middle East (4 to 9) gained little; and by robot group (Table 55), where vehicles and field machines absorbed most of it (48 to 589 instruments, binding 5 to 271) and service and social robots least (28 to 111, binding 2 to 7). Three consequences run through the report: every instrument-level comparison now rests on a layer twelve times larger and dominated by sector regulation; the general-AI comparison set is nearly the same as in v2; and 520 round-2 captures rated not about AI sit outside both sets.

## 4. Part A. The document landscape

{{F01}}

The embodied-AI set is now half governance instruments (808 of 1,589) and a third research papers (509), with news and web pages (161) and government reports (90) making up the rest; its issuers are academic (516) but also national executives (265), standards bodies (230), intergovernmental bodies (228), regulators (165) and legislatures (91). The general-AI set is 39% news, web pages and press releases (381 of 982), 25% voluntary guidance (241) and 15% government reports (148), with 50 research papers. The split still mirrors the collection design: round 1's robot sprint drew on academic literature and its database on official sources, and round 2 added instruments almost exclusively (743 of the 808 embodied instruments are round-2 captures), which is why every comparison in Parts C and D is made within genre or adjusted for it.

{{T01}}

{{F03}}

Regulators and agencies issue 165 embodied documents and 119 general-AI ones; legislatures 91 and 62; standards bodies 230 and 25. In v2 the institutions that apply robot rules were present mainly as authors of general-AI rules; after round 2 they are present as authors of robot rules.

### 4.1 Instruments: lifecycle and binding nature

{{F04}}

{{T02}}

Of the 812 governance documents in the embodied set, 362 are published and current, 276 in force, 47 under development (standards in preparation), 40 superseded, 32 drafts or bills, 21 proposals, 21 adopted but not yet in force and 10 open consultations; 304 are legally binding, 237 technical standards, 223 voluntary guidance and 48 have no binding nature yet. The general-AI pipeline (373) remains more legislative in its pending items (45 bills, 27 open consultations) but far less binding in its settled ones (51 in force; 247 voluntary, 55 binding). The binding share among instruments with a settled nature is 40% in the embodied set (304 of 764) against 17% in the general set (55 of 323; chi-square p < 0.001, Cramér's V 0.44); in v2 the shares were similar (5 of 57 vs 25 of 220, p = 0.11). The difference is what round 2 found, vehicle, drone, workplace and product law, not a change in anyone's propensity to legislate.

{{T33}}

{{T33b}}

Table 33 splits the 804 embodied instruments that also carry the governance-document flag (four robot-specific instruments lack it, hence 677 here against 681 in Table 53). The 677 robot-specific instruments are 244 binding, 370 voluntary guidance or standards and 63 drafts; 171 of the 370 voluntary ones are catalogue pages and 106 partial captures, because the standards layer is annotated on scope text, whereas 175 of the 244 binding ones are substantive captures. The 127 general-AI instruments with robot provisions (55 binding, 64 voluntary, 8 drafts) are mostly AI acts, strategies and guidelines that list vehicles, drones, surgical or industrial robots as examples or Annex items. Table 33b lists the 299 binding instruments: 223 regulations or decrees, 72 statutes, three court decisions and one treaty, issued above all by the United States (69), the European Union (56), Australia (48), Japan (26) and the United Kingdom (14). The v2 five remain in the list, now alongside road-traffic and automated-driving law, civil-aviation and drone regulations, occupational-safety rules for industrial robots and machinery, product-safety and medical-device regulation.

{{F06}}

Figure 6 accumulates dated instruments. Binding instruments reaching robots grow from 4 in 2012 to 283 in 2026, half of them since 2022, at 18 to 44 a year since 2018; voluntary guidance reaches 220, technical standards 231 and drafts 61. Two cautions remain: the Taiwanese industrial-robot hazard rules were captured only as login stubs and are neither captured nor cited (Table 25), and the collection still lacks several instruments the corpus cites (Part F). The oldest binding texts are now road-traffic and aviation laws from the 1950s whose consolidated versions govern automated vehicles and unmanned aircraft, so the v2 caution that "binding law from 2023" described the collection rather than the world no longer applies.

### 4.2 Development over time

{{F02}}

{{F05}}

The collection is recent: a tenth of documents date from 2017 or earlier, the median is 2024, 38% date from 2025 or later and 2026 (to October) is the largest year with 622 usable documents. The embodied share of each year's documents falls from above 60% before 2023 (63% in 2022) to 39% in 2025 and 42% in 2026 (logistic odds ratio 0.84 per year), because general-AI strategies and AI Act material arrive in volume from 2023; absolute embodied counts rise every year (135 in 2022, 260 in the first ten months of 2026), and governance-flagged embodied documents, by final year, arrive at 57 to 86 a year in 2021 to 2024, 105 in 2025 and 148 in 2026.

{{T03}}

Table 3 dates each robot type's entry. With round 2 the oldest governance texts are the sector laws that automated machines now fall under: road vehicles (1951), unmanned aircraft (1952), delivery vehicles (1960), agricultural machinery (1965), industrial manipulators (1985), exoskeletons (1990), mobile logistics (1991) and surgical devices (1993). Care, companion, domestic and humanoid robots enter governance in 2013, educational robots in 2016 and intimate robots in 2017; biohybrid systems have research attention and no instrument. Median years show where attention is now: humanoids (2024), with most other types at 2022 to 2023.

### 4.3 Geography and language

{{F07}}

Europe supplies 1,332 usable documents (42%), of which 645 are embodied (48%); Asia 661 (296); the international layer 374 (241); North America 345 (217); Latin America and the Caribbean 149 (36); Oceania 113 (83); the Middle East 98 (45); Africa 75 (26). The embodied share varies by region (Cramér's V 0.21), highest in Oceania (73%), the international layer (64%) and North America (63%) and lowest in Latin America (24%) and Africa (35%): Europe and North America contribute embodied documents through research and, after round 2, vehicle and drone law; Oceania and the international layer through Australian regulation and standards; Latin America and Africa still mainly through general-AI instruments.

{{F08}}

{{T04}}

Across 116 countries with any document, 78 contribute an instrument, 58 an instrument that reaches robots and 45 a binding instrument of any kind (40 a binding instrument that reaches robots). Among national jurisdictions the United States has 100 embodied instruments, China 94, Japan 53, Australia 50 and the United Kingdom 49, where no country had more than five in v2; the international standards layer (197, Table 54) and the European Union (106) hold more than any country. China (293 documents), the United States (286) and the United Kingdom (233) lead on documents; counts measure the collectors' and databases' reach as much as national activity, and China's position rests on one full-text harvest of the State Council policy library (259 of its 293 documents are in Chinese).

{{F10}}

{{T05}}

English is 75% of usable documents; Chinese (266), Spanish (109), Japanese (105), Portuguese (44), French (41), Korean (35) and German (26) follow. Non-English documents are more often instruments (68% vs 49%) but, among governance documents, less often binding (34% vs 44%): the multilingual legal record and the English research literature remain different populations. Research venues are robot-ethics venues; median OpenAlex citations are 1.

## 5. Part B. What is governed

{{F11}}

{{F12}}

{{F13}}

{{F14}}

Autonomous road vehicles are the most addressed type (432 documents, 27% of the embodied set), then drones (406), companion and social robots (239), care robots (211), industrial manipulators (208), professional service robots (200), military weapons (193), humanoids (164), surgical robots (145) and collaborative robots (114). Regions attend to different machines (Figure 12): social robots are a European (26%) and North American (15%) topic; humanoids lead in the Middle East (22%) and Asia (15%); surgical robots in the Middle East (33%); drones in Oceania (66%), Africa (62%) and Latin America (53%). Genres attend to different machines (Figure 13): research is social-robot heavy (43%); binding instruments address drones (58%) and vehicles (33%); voluntary guidance mentions vehicles (37%) and industrial arms (18%); drafts mention vehicles (36%) and military systems (35%). Over time within the embodied set (Figures 14 and 42): social robots fall from 20% of documents in 2020 to 2022 to 11% in 2025 to 2026; humanoids rise from 8% to 16%; mobile logistics robots from 5% to 9%; vehicles hold at 24 to 28%.

{{F16}}

{{T06}}

{{F17}}

Companion and care robots co-occur in 118 documents (Jaccard 0.36) and industrial manipulators and collaborative robots in 76 (lift 5.1); vehicles and drones co-occur in 70 documents but less often than independence predicts (lift 0.63), because the sector laws round 2 added address one machine at a time, so the v2 observation that instruments enumerate vehicles, arms and drones together no longer holds. Topics form two poles, ethics with human-robot interaction and physical safety with liability, standards and oversight (Figure 17).

{{F18}}

{{F40}}

{{T22}}

The governance-gap index (research share minus instrument share) with bootstrap intervals (Table 22) separates three groups. Studied far more than governed: social and companion robots (+41 points, interval 37 to 46; 13 instruments, none binding), care robots (+22; 49 instruments, 4 binding), humanoids (+19, interval 16 to 23; 27 instruments, one binding), professional service and surgical robots (+9 each) and educational, domestic and intimate robots (+4 to +5). Near parity: military weapons, collaborative robots, industrial manipulators (−3, interval −6 to +1), space, security and rehabilitation robots. Governed far more than studied: drones (−32, interval −36 to −28; 312 instruments, 172 binding), autonomous road vehicles (−23, interval −28 to −19; 293 instruments, 100 binding) and, by small margins, logistics, maritime, agricultural and delivery robots. The pattern has an explanation: vehicles, drones and field machines inherited transport and aviation regimes, whereas social robots raise questions (deception, attachment, dignity, vulnerable users) without a regulatory home of their own. The governance expert's review notes that general regimes (the AI Act's transparency and vulnerability provisions, product-safety and toy rules, data protection) do apply to them; the gap is in robot-specific instruments, not in the absence of any law. The v2 finding that industrial manipulators are governed far more than studied does not survive: their 105 instruments (13%) are matched by 10% of research papers.

{{F19}}

Embodied documents are sectoral (logistics and transport 46%, health 24%, manufacturing 18%, defence 17%, elder and social care 10%); general-AI documents are cross-cutting (73%) and about public administration (46%).

## 6. Part C. How robots are governed: principles, tools, framings

### 6.1 Principles: pooled, stratified and adjusted

{{F20}}

{{T08}}

Pooled over all documents, 17 of 20 principle differences between the sets survive Holm correction (accountability, robustness and dignity do not). Pooled comparisons are, however, mostly comparisons of genres. Three further analyses settle what survives.

{{F39}}

{{T21}}

Within governance instruments (804 vs 367), the embodied-specific considerations differ sharply: physical safety 81% vs 8%, autonomy-level control 53% vs 9%, conformity assessment 59% vs 17%, proximity 28% vs 0.3%, liability for physical damage 18% vs 2% (all Holm-significant; dual use, 15% vs 11%, is not). Unlike in v2, the core principles also differ within instruments, all in one direction: transparency (33% vs 74%), justice and fairness (14% vs 67%), privacy (24% vs 66%), beneficence (30% vs 78%), trust (17% vs 63%), inclusive growth (35% vs 71%), accountability (53% vs 75%) and four further core principles are raised less often in robot instruments; non-maleficence (80% vs 77%), human oversight (43% vs 47%) and robustness (63% vs 71%) do not differ. Within research papers (509 vs 50), four of the six embodied-specific items differ (conformity assessment and dual use do not), inclusive growth is lower in robot papers (22% vs 52%) and no other core principle differs.

{{F38}}

{{T20}}

{{T34}}

Adjusting for document class, region and year (Table 20), the embodied-specific considerations keep very large odds ratios (physical safety 75, proximity 170, liability 27, autonomy-level control 21, conformity 7, dual use 4). Among the core principles, 13 of 14 now differ: non-maleficence (2.0) and human oversight (1.5) are higher in embodied documents, transparency (0.30), justice and fairness (0.18), privacy (0.28), beneficence (0.26), trust (0.31), inclusive growth (0.30), solidarity (0.32), freedom (0.45), sustainability (0.51), dignity (0.55) and accountability (0.68) lower; only robustness (1.04) does not differ. The Mantel-Haenszel analysis stratified by class (Table 34) agrees. The v2 reading that core differences "mostly vanish once genre is accounted for" rested on 65 robot instruments; with 804, regulations and standards for machines carry much less of the ethical vocabulary than AI strategies and guidelines even within genre; accountability is lower within instruments (53% vs 75%, Holm-significant) and research outputs (69% vs 84%, not significant) and does not differ within government reports or communications.

{{F21}}

{{F22}}

By region (Figure 21), liability for physical damage runs from 4% (international) to 58% (Middle East), human oversight from 37% to 76% and autonomy-level control from 40% (Oceania) to 80% (Middle East); unlike in v2, the core also varies (beneficence 18% to 64%, trust 9% to 45%). By class (Figure 22), in-depth treatment follows function: drafts operationalise accountability (43%), non-maleficence (40%), human oversight and autonomy-level control (37% each); binding instruments physical safety (46%) and conformity assessment (38%); research proximity (34%) and accountability (32%).

### 6.2 Operationalisation of the embodied-specific considerations

{{F23}}

{{T09}}

{{T35}}

After the extended, blind re-annotation of every governance document (Table 35, unchanged from v2: mechanisms per document rose from 4.9 to 5.6, robot types from 0.4 to 0.7, named instruments from 1.3 to 1.8; binding and in-force labels changed for fewer than 5% of documents), Figure 23 and Table 9 show which document types move the six considerations from mention to specification. Technical standards (n = 238) mention physical safety in 80% of cases and specify it in 47%, proximity in 31% and 8%; binding instruments (n = 299) mention physical safety in 87% and specify it in 46%, conformity assessment in 62% and 38%, liability in 24% and 12%; voluntary guidance (n = 196) mentions physical safety in 73% and specifies it in 35%; drafts (n = 75) in 83% and 24%. Autonomy-level control is mentioned by 43 to 69% of every instrument type and specified in depth by 18% of binding instruments, 21% of voluntary guidance, 13% of standards and 37% of drafts, so the v2 observation that nothing yet specified it no longer holds, although it remains the consideration with the widest gap between mention and specification in binding law. Liability for physical damage is absent from standards (2% mention, none in depth), as is dual use.

### 6.3 Tools: governance mechanisms

{{F24}}

{{T10}}

Among instruments (the fair comparison: 804 vs 367 with Holm tests in Table 21; Table 10 gives the same shares on 812 vs 373 governance documents), robot instruments refer to technical standards (65% vs 35%) and use licensing and registration (36% vs 7%), conformity assessment (32% vs 11%) and insurance requirements (10% vs 2%) significantly more often; prohibitions, incident reporting, liability regimes, testing and sandboxes and human-oversight requirements are used at rates that do not differ; general-AI instruments rely on audits (55% vs 30%), international cooperation (53% vs 22%), oversight bodies (51% vs 23%), education, funding, labelling (41% vs 15%), data governance (34% vs 13%), risk tiering (23% vs 12%) and self-regulation (24% vs 4%). The adjusted models (Table 20) confirm licensing and registration (odds ratio 10.2), insurance (9.7), conformity assessment (4.6), standards references (3.6), liability regimes (3.1) and prohibitions (2.3) as the mechanisms associated with embodied documents after genre, region and year, and audits (0.62), risk tiering (0.67), funding (0.53) and the institution-building tools as those of general-AI documents; the v2 association of funding with embodied documents (1.9) reverses.

{{F25}}

{{T29}}

{{T15}}

On a common population (1,527 embodied documents in six regions; Table 29), 33 of 38 items diverge by region after Holm correction (bias-corrected V 0.08 to 0.34): beneficence (0.34), references to standards (0.33), licensing and registration (0.33), trust (0.30), liability regimes (0.28), privacy, freedom, accountability, liability for physical damage, fairness and proximity (0.23 to 0.27) lead; physical safety (0.15), autonomy-level control (0.13) and human oversight (0.12) differ less. What does not differ detectably is the procedural toolkit: audits (0.01), self-regulation codes (0.04), human-oversight requirements (0.05), labelling (0.05) and the conformity-assessment mechanism (0.07). The v2 statement that regions differ on liability and control and not on the ethical core is therefore withdrawn: on the larger population the core diverges at least as much, because regions now differ in the mix of standards, sector regulation and strategies they contribute. Among all governance documents (Figure 25, Table 15), the contrasts in tools are larger (standards references from 18% in Latin America to 86% in the international layer; licensing from 5% in the international layer to 72% in Oceania; education, oversight bodies and funding in Africa, the Middle East and Latin America), with the caveat that Africa (26), the Middle East (44), Latin America (74) and Oceania (75) have fewer than 80 governance documents each.

{{T24}}

K-means bundles of mechanisms (Table 24) have silhouettes of 0.22 or less at every k and are not interpreted.

### 6.4 Framing, stance and the personhood debate

{{F26}}

{{F27}}

{{F28}}

{{T12}}

Framing follows the document mix each region contributes. Principle-or-ethics framing still leads in Europe (35% of 554 framed documents, risk-based 26%); North America is risk-based (31%) before ethics (23%); Asia is risk-based (37%) and innovation-framed (33%) with ethics at 15%; Oceania (64%), the international layer (61%), Africa (45%) and Latin America (45%) are risk-based; the Middle East is liability-framed (59%, a legal-doctrinal literature on civil liability for smart robots); the association is moderate (Cramér's V 0.23). Among the 480 embodied research papers that take an applicable stance (29 are rated not applicable), 56% take no regulatory position, 31% call for new regulation, 9% prefer self-regulation or standards and 4% argue existing law suffices. Legal personhood is discussed in 173 documents (19 supportive, 34 opposed, 120 without a position); its share of embodied documents falls from 10% in 2020 to 2024 to 5% in 2025 to 2026 (adjusted odds ratio 0.39).

### 6.5 Which instruments are cited

{{F29}}

{{T13}}

{{F30}}

General-AI documents cite the EU AI Act (29%), the GDPR (21%), the OECD principles (14%) and the UNESCO Recommendation (10%). Embodied documents cite the GDPR (9%), the UN CCW process (6%) and the AI Act (6%) and then a robotics canon the general set does not: the Civil Law Rules on Robotics (4% vs 0.6%), the Machinery Regulation (3% vs 0.7%), the Product Liability Directive (2.6%), ISO 10218 (2.6%), ISO 13482 (2.1%), the IEEE 7000 series (1.8%) and ISO/TS 15066 (1.5%). Asimov's fictional laws are cited by 2.5% of embodied documents and are not an instrument. Only 28% of embodied documents cite any named instrument, against 53% of general-AI documents, because standards and sector regulations rarely cite other instruments by name. By region, the AI Act (22%) and the GDPR (23%) are Europe's references, the OECD principles are Latin America's (20%) and Africa's (23%), the Civil Law Rules are cited most in the Middle East (13%) and the CCW process in the international layer (12%). No ISO robot standard is cited by more than 4% of any region's usable documents (Figure 30); within embodied documents alone, ISO 10218 reaches 8% in Latin America (3 of 36).

## 7. Part D. Regional comparison

{{T14}}

{{F31}}

{{T23}}

{{T23b}}

{{T31b}}

{{T31}}

Regional profiles are in Table 14. The cosine distances between regional principle, topic and mechanism profiles (Figure 31) place Asia and North America 0.04 apart and Europe and North America 0.04 apart (bootstrap intervals 0.03 to 0.06), above North America's split-half noise floor of 0.02 (Table 31b), so these pairs are now distinguishable where Europe and North America were not in v2, but they remain the closest. Europe and Asia are 0.07 apart, the Middle East 0.10 from Europe, Oceania 0.18 and the international layer 0.19; the international layer stands furthest from everyone (mean distance 0.17). Nearest neighbours are stable under bootstrap for Europe, Asia, the Middle East and the international layer (Table 23b: 99 to 100% of resamples) and unstable for North America (53%) and Oceania (74%). Restricting to research papers (Table 31) brings Europe and North America back to 0.01 apart, so their separation is a difference in instruments (United States and Canadian vehicle and drone regulation against EU law and standards), whereas the Middle East's distinctiveness (0.18 from Europe) is in the research literature itself.

In words: Europe and North America share a social- and care-robot research literature with an ethics framing and now a large body of vehicle and drone law; Asia is instrument-heavy (428 governance documents, 170 embodied instruments) and addresses vehicles, drones and industrial robots under risk and innovation framings; the Middle East is a liability-doctrine literature (research is 69% of its embodied documents) with Dubai's vehicle law; Latin America is a legislative region (23 embodied instruments, 14 binding, drones in 53% of its embodied documents) with thin robot research; Africa is drone regulation (62%) and capacity-building strategy; Oceania is Australian and New Zealand drone and vehicle regulation (56 embodied instruments, 52 binding) with 12 research papers; the international layer is the standards layer (199 embodied governance documents, 6 binding).

## 8. Part E. Trends and the newest documents

{{F33}}

{{F42}}

Within the embodied set (composition-free), the terms "embodied AI" or "physical AI" appear in 1% of 2024 documents, 8% of 2025 documents and 12% of 2026 documents; humanoid vocabulary is present in 10 to 18% of embodied documents in every year since 2018, highest in 2025 (18%); social-robot vocabulary falls from 30% in 2020 to 10% in 2026; autonomous-vehicle vocabulary holds at 23 to 28%. Robot-type shares (Figure 42) show humanoids and logistics robots rising after 2024 and social robots receding.

{{F34}}

{{T28}}

{{T16}}

Comparing 476 embodied documents from 2025 to 2026 with 737 from 2020 to 2024, the crude shares of industrial policy (+9 points), conformity assessment (+7), physical safety (+6) and standards (+6) rise and those of ethics principles (−14), human-robot interaction (−10), human dignity (−6), legal personhood (−5), civil liability (−5) and trust (−5) fall; after Holm correction only industrial policy, ethics principles, human-robot interaction and personhood remain, and cybersecurity, which rose by 12 points in v2, moves by 2 points. Adjusted for document class and region (Table 28), personhood (odds ratio 0.39, Holm p = 0.04) survives; industrial policy (1.6, p = 0.08) is at the margin, with research-only shares moving from 9% to 13%; ethics principles (0.64, p = 0.16) does not. The "turn to industrial policy" is therefore partly a change in which documents were written in 2025 to 2026 (strategies, action plans and sector regulation rather than research papers) and partly a change within genres; the retreat of ethics discourse is composition.

{{T17}}

{{T30}}

Trend models on the embodied set (Tables 17 and 30) no longer show the v2 growth of 30% a year in compliance machinery. The risk-based-tiering mechanism rises by about 9% a year (odds ratio 1.09, interval 1.02 to 1.17) but not significantly after correction (Holm p = 0.10), and the estimate is 1.07 to 1.10 when 2026 is excluded or only documents with a stated date are used; the conformity-assessment mechanism (1.05) and consideration (1.03) are flat. Human-robot proximity (0.93 per year, interval 0.90 to 0.97) and liability for physical damage (0.93, 0.89 to 0.97) decline as instruments that mention neither arrive; physical safety, autonomy-level control and dual use are flat.

The 2025 to 2026 layer of the collection is, read document by document: industrial strategies for humanoids and embodied intelligence (Shanghai, Beijing's development-area measures, Japan's second AI Basic Plan, Israel's draft strategy) and Brazil's humanoid bill; research on oversight and cybersecurity of agentic and multi-robot systems; the conformity layer catching up (ISO/PAS 8800, ISO/IEC TR 5469, ISO 31101, ISO 3691-4, draft ISO 26058, the Commission's draft high-risk guidelines); and, from round 2, the binding sector layer in motion: commencement and marketing regulations under the UK Automated Vehicles Act 2024, Denmark's revised self-driving trial scheme, Japan's consolidated road-traffic and vehicle-safety rules, China's MIIT notice on access, recall and over-the-air upgrades for intelligent connected vehicles, drone regulations in Vietnam, Rwanda, Argentina, Brazil and Peru, and EU regulations on non-road mobile machinery and on amending the AI Act, machinery and aviation rules (Table 59).

## 9. How different robot types are governed

{{S12}}

{{S13}}

Counts below follow Table S12, which counts governance-flagged documents; Table 55 counts instrument classes and runs one to five lower per group (vehicles and field 589 against 594).

- **Industrial and logistics robots.** 337 documents, 171 instruments (33 binding, 56 standards): ISO 10218 and ISO/TS 15066 (now captured as well as cited), ISO 3691-4 and draft ISO 26058, Israel's SI 395, the EU machinery rules and national occupational-safety rules for industrial robots; physical safety is present in 74% of documents and proximity in 60%; the dominant tool is the reference to standards. Governance here is occupational-safety governance.
- **Service and social robots.** 501 documents and the least governed per document: 113 instruments, 7 binding. ISO 13482, ISO 31101 and El Salvador's decree reach professional service and care robots (73 and 49 instruments); social, educational and domestic robots are reached by 13, 11 and 22 instruments and intimate robots by four, mainly guidance. Proximity (77%) and dignity dominate; the GDPR is the instrument most cited, so data-protection law governs by default.
- **Medical and body-integrated robots.** 192 documents, 68 instruments (12 binding): medical-device law and guidance (EU, FDA, Health Canada, MHRA, MFDS, WHO) and the proposed liability instruments; the highest physical-safety (79%) and liability (38%) presence; the strongest Middle Eastern presence.
- **Humanoid and general-purpose robots.** 164 documents, 27 instruments and one binding instrument (a Beijing development-area measure for embodied intelligence); legal personhood is the most common primary topic. The gap between the 2025 to 2026 surge in discourse and the thinness of instruments is widest here.
- **Vehicles and field robots.** The most instrument-dense group (827 documents, 594 instruments, 271 binding, 132 standards): road-traffic and automated-driving acts, civil-aviation and drone rules, type-approval and machinery regulation, plus the AI strategies and the AI Act that reference them. The most under-counted group in v2, it now holds nine in ten of the binding instruments reaching robots, and its documents carry physical safety (82%) and conformity assessment (53%) more than any other group.
- **Security and military robots.** 229 documents, 98 instruments (21 binding): the UN CCW process, national security and policing law, drone and counter-drone rules and humanitarian-law commentary; the highest share of documents calling for new regulation (35%).

## 10. Part F. Reliability, validation and coverage

### 10.1 Reliability of the labels

{{F35}}

{{F43}}

{{F44}}

{{T26}}

{{T27}}

{{T27b}}

Five comparisons (Table 26), all on round-1 samples and computed against the annotations the analysis uses: a different model on the same input agrees at a median kappa of 0.85 (minimum 0.61 for page quality; 11 of 46 fields below 0.80, mainly the multi-label fields, stance, framing, date basis and three principle levels); the same model re-run agrees at 0.91 (minimum 0.66); the same model reading the full text instead of the excerpt agrees at 0.88 (minimum 0.71) and finds slightly more of everything (0.1 to 0.4 more labels per document; principle presence 0 to 6 points higher), with lower agreement on documents the excerpt truncated (median principle kappa 0.75 vs 0.84); the same model with the collectors' cover block and metadata removed agrees at 0.90 (minimum 0.65 for date basis), so the label leakage identified in review changed country, issuer and language labels little and page quality, date basis and stance most; and the extended blind re-annotation of governance documents agrees with the original at 0.83, with the largest movements in robot-type labels (0.60), stance (0.55) and publication stage (0.49). Round-2 documents were not in these samples; their blind labels are checked against the collectors' catalogue metadata instead (Section 2; Tables 57 and 58). The confidence field is a page-quality proxy and is not used. No human coded any document; the protocol for a human validation sample is in the supplement.

### 10.2 Model-free check: full-text lexicons

{{F36}}

{{T18}}

After repairing the lexicon bugs found in review (a case-insensitive acronym pattern that matched the word "laws", unbounded dual-use terms, a harm pattern that matched "harmonised"), lexicon presence agrees with annotated presence at 70 to 89% for principles and 88 to 99% for robot types, except military weapons (72%) (median kappa 0.40 to 0.43, moderate), best for distinctive vocabularies (social and care robots; trust, privacy and dignity) and worst for diffuse concepts (domestic robots, autonomy-level control, liability for physical damage, security robots). The Spearman correlation between annotated and lexicon-based embodied-minus-general differences across the 20 principles is 0.88.

### 10.3 Sensitivity

{{T19}}

{{T32}}

Headline quantities are stable across subsets (Table 19) and across definitions of the embodied set (Table 32): under the strict definition (relevance only, 1,345 documents) the research share is 33%, governance documents fall to 682 (244 binding) and the social-robot gap is unchanged (44% of research, 11 instruments); restricting to substantive captures (905 documents) leaves 424 governance documents (221 binding) and the same ordering of robot types.

### 10.4 Coverage and known gaps

{{F37}}

{{F41}}

{{T25}}

In round 1 the collectors could not capture 266 of 2,160 listed sources, 109 of them in the European robot sprint; 34 captured files were oversized or restricted, 27 recovered. In round 2, 359 of 2,075 candidates yielded no text, most on hosts that serve bot challenges or sit outside the sandbox network policy (eur-lex.europa.eu catalogue pages, the Chinese national law database, the UNODA library, Légifrance, the Korean and Taiwanese law portals; Table 52). The coverage audit (Table 25, Figure 41) checks 38 reference instruments and standards named by the governance expert: {{AUDIT}}. The two US executive orders of 2023 and 2025 are in the collection (D0915, D0918) and count as captured once the audit's title patterns were corrected. The instruments cited but still not captured (the revised Product Liability Directive, Korea's Intelligent Robots Act and AI Basic Act, ANSI/RIA R15.06 and R15.08, the OECD principles) and the uncaptured Taiwanese industrial-robot standards are the targets for any further round, and their absence, with the jurisdictions round 2 could not reach, is why every instrument count in this report remains a lower bound.

## 11. Limitations

The corpus is a purposive multilingual collection, not a census, and its composition drives several ratios: Europe is 42% of usable documents, English 75% and Chinese 8%, the last almost entirely one round-2 harvest of the State Council policy library; the research-to-instrument ratio reflects the sprint, database and round-2 designs; known binding instruments are still missing. Round 2 adds limits of its own: several official portals block the sandbox or serve bot challenges (Table 52; the collector reports in `COLLECTOR_REPORTS.md` list them by jurisdiction); the collectors' shared search budget was exhausted part-way through every brief, so later discovery relied on official databases and direct fetches; technical standards (259 round-2 captures) are annotated on their public scope text only, never on the normative text, and are flagged as such in the registry; the 359 inventory items without text are excluded from every count; jurisdiction coverage is uneven (669 usable round-2 documents from Europe and 403 from Asia against 21 from Latin America, 14 from Africa and 12 from the Middle East; the collector reports list the portals and jurisdictions, France, Singapore, Korea, Taiwan, Brazil and Chile among them, that could not be reached); unfiltered full-text harvests brought 520 usable documents rated not about AI, which sit outside both sets; and round-2 texts are shorter (median 882 words against 2,646), 251 of them landing pages. Labels were assigned by a language model with no human gold standard; they are consistent across models, re-runs, full text and blind inputs on round-1 samples and agree with the collectors' catalogue metadata on round-2 documents, but they are not certified. The extended re-annotation still truncates the longest quarter of governance documents. Dates are inferred from content for 16% of documents; 2026 is partial. OpenAlex enrichment is DOI-only and some citation counts are implausible. The six embodied-specific items are considerations scored like principles, not principles in the ethical sense; the relevance field used to define the sets was produced by the same model that produced the outcomes. Small groups (Africa, the Middle East, Latin America, humanoid and social-robot instruments) are reported as counts, and conclusions about them are correspondingly tentative.

## 12. Conclusions

Within this collection, embodied AI is governed by sector law, technical standards and voluntary guidance, and by the enumeration of robots inside general-AI law: 299 binding instruments reach robots, 268 of them in force, almost all vehicle, aviation, workplace, machinery and medical-device rules rather than robotics statutes. The robot literature's own considerations, physical safety, proximity, physical liability and autonomy-level control, are what distinguish it from general-AI governance once genre is accounted for, and its tools are those of product and transport safety: standards, licensing and registration, conformity assessment and insurance; the ethical vocabulary of AI governance is thinner in robot rules even within genre. Standards and binding law specify physical safety in roughly half of cases; autonomy-level control is specified by one binding instrument in five. Research and rules point at different robots, with companion and social robots the clearest case of attention without instruments and drones and vehicles of instruments without research. Regions differ on values, liability and tools alike, while sharing the procedural toolkit. The frontier is moving toward industrial policy, humanoids and the vocabulary of "physical AI", and away from ethics discourse and personhood. For governance practice: the operative texts for robots are sector regulation, standards and product law, so attention to transport, aviation and occupational-safety regimes, to ISO/TC 299 and IEC, and to the AI Act's harmonised-standards mandate buys more than new principles; robots that live with people still have almost no instruments of their own; and autonomy-level control needs the specification that most binding instruments and all standards still leave open.

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
- **Collection round 2.** The targeted search of legal databases, treaty archives, standards catalogues and regulator sites that added 1,716 content-analysed documents, 1,637 of which entered the collection after duplicate removal; described in the companion report.

## Appendix. Figure and table index

Figures 1 to 44 (9, 15 and 32 were merged into neighbours) and the round-2 figures 50 to 52 are in `figures/` as PNG and SVG in light and dark variants with their data in `figures/data/`; tables T01 to T35, the round-2 tables T50 to T60 and S01 to S13 are in `tables/`; every statistic is in `data/results.json`. The supplement holds the codebook, taxonomies, reliability detail, instrument lists, coverage audit, datasheet and the review log; the companion report holds the round-2 inventory, funnel and collector-metadata checks.
