# Adversarial governance-law review of "Global governance of embodied AI and robotics" (Stage 2 report, paper and supplement)

Reviewer role: senior AI-governance and technology-law reviewer (EU AI Act, product-safety and machinery law, robot law, ISO/IEC standards, international AI policy).
Scope: `report/analysis_report.md` (whole), `report/paper.md` (sections 1, 2, 5.1, 5.3, 6, 7), `report/supplement.md` (S2, S3, S5), tables S01, S02, S03, S05, T02, T13, T14, and read-only spot-checks of `data/master_table.csv` (37 governance documents inspected individually, plus corpus-wide searches). No project file other than this review was modified.
Date of review: 30 October 2026. External facts were checked against primary or official sources where stated (Taiwan Ministry of Justice law database; ISO catalogue; EU Official Journal numbers; Salvadoran press reports of the Diario Oficial publication). Where I could not verify a fact I say so.

---

## 1. Verdict (ten lines)

1. The pipeline, codebook, reliability design and reporting discipline are of high quality, and the findings about the *discourse* (principle profiles, topic shifts, regional convergence on ethics, the rise of "physical AI" vocabulary) are defensible and genuinely new.
2. The findings about the *instrument layer*, which carry the headline claims, are not yet defensible: the seven "binding embodied instruments" are six instruments, one of which was revoked in January 2025 (EO 14110), one is dated 38 years wrong (Taiwan's rule was promulgated in 1987 and last amended in 2018, not 2025), one is captured three times plus two article pages (the AI Act), and one is an internal unit-creation resolution (Argentina).
3. The "technical standards are the operational layer" finding rests on ten documents, of which nine are ISO catalogue, committee or project landing pages and four are not standards at all; the operationalisation scores were assigned to abstracts.
4. The collection does not contain the binding law that actually governs embodied AI (automated-vehicle statutes and UNECE regulations, drone rules, machinery and product-liability law, mandatory Chinese GB standards, Korea's Intelligent Robots Act, ISO 10218:2025). Hence "binding governance of embodied AI is a 2023 to 2025 phenomenon", "the binding curve stays at zero until 2023", "autonomy-level control is specified nowhere" and "the newest binding law comes from outside the traditional centres" are artefacts of coverage, not findings about the world.
5. The "social-robot governance gap" conflates "no robot-specific instrument in this collection" with "no regulatory home"; horizontal regimes (AI Act Articles 5 and 50, GPSR, the 2025 Toy Safety Regulation, RED/CRA cybersecurity rules, GDPR, US companion-chatbot statutes) already reach these machines.
6. The status and binding-nature scheme is legally inconsistent: ten bills are coded "legally binding", a revoked executive order is "published current", soft law is "in force", and "in force" is not distinguished from "applicable" (the AI Act's robot-relevant obligations do not apply until 2028 after the 2026 Digital Omnibus).
7. Regional characterisations are mostly characterisations of what each team collected (the Middle East's "liability-led" profile is 25 journal articles and one statute; Africa's rests on one embodied strategy in which robots appear "incidentally").
8. Several documents are miscoded as governance instruments (an H2020 project deliverable, a JST funding-call appendix, a CPSC staff report, ISO committee pages), and one of them is the sole basis for a dated "first governance mention".
9. All of this is fixable: an instrument-level inventory with a coverage audit (list in section 4), a human legal audit of the 63 embodied and 55 binding documents, and reframing of the binding-layer claims as "within this collection" would make the work publishable and useful.
10. Recommendation: major revision before any policy use; the discourse analysis can stand with caveats, the instrument analysis cannot.

---

## 2. Findings ranked by severity

Severity scale: **Critical** (a headline claim is wrong or unsupported), **High** (a section-level claim or the classification scheme is unsound), **Medium** (local error, nuance or inconsistency), **Low** (presentation).

### Critical

**F1. The binding-instrument timeline and the "2023 to 2025 phenomenon" claim are collection artefacts.**
- Location: Executive summary item 2; §3.2 ("The binding curve stays at zero until 2023 ... the binding governance of embodied AI as captured in this collection is a 2023 to 2025 phenomenon"); Figure 6; §10 conclusion 5; paper abstract, §5.1, §6 and §8.
- Problem: three of the six distinct instruments behind the curve are misdated or misstatused (F2, F3, F4), and binding embodied law that predates 2023 is simply absent from the collection (Taiwan 1987/2018; Korea's Intelligent Robots Act 2008; Germany's StVG amendments 2017 and 2021; UK Automated and Electric Vehicles Act 2018; EU drone Regulations 2019/947 and 2019/945; UNECE R157 2021; Japan's Road Traffic Act Level-3 amendment 2019; Singapore's Autonomous Motor Vehicles Rules 2017; US state personal-delivery-device and AV statutes from 2017; Shenzhen's intelligent connected vehicle regulation 2022; China's mandatory GB 11291 robot-safety standards 2011/2013).
- Evidence: corpus-wide searches of titles, summaries, key provisions and named instruments return zero governance documents for "Automated Vehicles Act", "StVG", "UNECE/R157/ALKS", "2019/947", "Cyber Resilience", "Machinery Regulation" (as a document), "Product Liability Directive" (as a document), "Intelligent Robots Act" (as a document), "ISO 10218" (as a document), "ISO/TS 15066", "13849/62061/61508", "NHTSA/FMVSS", "FAA Part 107", "DoD 3000.09".
- Fix: re-state every binding-layer claim as a statement about the collection; run the coverage audit in section 4; after capture, redraw Figure 6 by instrument (not capture) and by date of entry into force and date of application.

**F2. Taiwan's Industrial Robot Hazard Prevention Standards (D0480) are dated 2025; they were promulgated on 19 January 1987 and last amended on 14 February 2018.**
- Location: Executive summary item 2 ("Taiwan's Industrial Robot Hazard Prevention Standards (2025)"); §3.2; §7.4 ("the conformity layer catching up ... Taiwan's industrial-robot hazard rules"); §8; Table S01; paper §5.1.
- Problem: the capture holds 204 words consisting of page markers and a login notice (`page_quality = partial_or_excerpt`, `confidence = 0.40`, `date_basis = unknown`, `pub_year = NaN`); `year_final` 2025 appears to be a fallback (file or capture date). The Ministry of Justice law database history page for pcode N0060025 lists: promulgated 1987-01-19 (Ministry of the Interior, 53 articles); amended 1998-06-30 (Council of Labor Affairs, 37 articles); amended 2014-06-30 (Arts. 1, 15, 34, 37); amended 2018-02-14 (Arts. 2, 5, 8, 18, 21-33, 37, adding collaborative-robot provisions by reference to CNS 14490/ISO 10218). This is one of the oldest binding robot-safety rules in the world, not one of the newest.
- Evidence: `data/master_table.csv` row D0480; https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=N0060025 .
- Fix: `year_final` → 1987 (with amendment years 1998, 2014, 2018 recorded); re-annotate from the actual text (the database serves the full text without login via LawAll.aspx in a browser; the capture failed, not the source); remove Taiwan from every "2025" and "newest" sentence; note that Taiwan's rule, Japan's 1983 Ordinance amendment and ANSI/RIA R15.06-1986 pre-date ISO 10218:1992.

**F3. Executive Order 14110 (D0915) is counted as a current binding embodied instrument; it was revoked on 20 January 2025 by EO 14148, and the collection itself contains the successor order (D0918, EO 14179, "Removing Barriers").**
- Location: Executive summary item 2; §3.2 and Figure 6 (2023 rise "with the Dubai autonomous-vehicle law and the United States Executive Order"); §8 (security robots "governed through ... the US Executive Order"); Table S01; paper §5.1 and §6 ("Executive Order 14110's examples").
- Problem: (a) `instrument_status = published_current` is the soft-law value and is wrong for a binding instrument in any case; the correct value is `superseded_or_repealed`. (b) An executive order binds federal agencies, not private parties; coding it as `regulation_or_decree`/`legally_binding` on a par with the Dubai statute without a "binds whom" field misleads. (c) Its embodied categories (autonomous vehicles, autonomous weapons, surgical robots) are passing examples; relevance is coded 1, yet the document enters S01 through the category labels.
- Evidence: row D0915 (`instrument_status = published_current`); row D0944 (EO 13859) is coded `superseded_or_repealed` although it was not revoked, which shows the annotator's status coding of US orders is unreliable in both directions.
- Fix: set D0915 to `superseded_or_repealed`; add a `binds` field (private parties / public bodies / internal organisational act); recompute the binding counts (embodied binding in force falls to five distinct instruments: Dubai 2023, AI Act 2024, Argentina 2024, El Salvador 2025, Taiwan 1987/2018).

**F4. The EU AI Act is captured at least ten times, not "twice", and its proposal-stage captures are counted as live drafts.**
- Location: Supplement S5 note ("appears twice ... counted as two documents throughout"); paper §7; §3.2 ("6 are drafts or bills under consideration"); Table S03; T02.
- Problem: adopted text is captured as D1010 (Publications Office catalogue record), D1060 (Finnish OJ text), D1291 (Council PE-24-2024 text), D1022 and D1023 (AI Act Service Desk pages for Articles 62 and 26, coded as separate `statute_or_act` documents dated 2026); proposal-stage text as D1103 (2021 annexes), D1290 (2021 proposal via OEIL), D1310 (2021 proposal, Italian), D1142 (2024 Coreper compromise note), D1064 (2023 EP compromise amendments). D1103 and D1290 are coded `draft_or_bill_under_consideration` although the proposal was enacted as Regulation (EU) 2024/1689; they are two of the six "embodied drafts under consideration" and drive the "proposals and drafts operationalise conformity assessment in 50%" statement (Table 9). Cross-language duplicates (FI, IT, BG, EN) defeat MinHash deduplication; the same happens for the Civil Law Rules (D1299 Bulgarian, D1304 English), the Salvadoran AI law (D0001, D0144), the Peruvian regulation (D0079, D0080, with contradictory statuses), the Israeli draft strategy (D0191, D1687), the UAE charter (D0285, D0287), the Italian strategy (D1698/D1701; D0103/D1217), the Vietnamese AI law (D0697, D0794) and ISO/IEC TR 24028 (D1231, D1232).
- Evidence: corpus title search for "Artificial Intelligence Act | 2024/1689 | harmonised rules on artificial" (output reproduced in reviewer notes); rows D1022/D1023 summaries explicitly say they reproduce Articles 62 and 26.
- Fix: introduce an instrument identifier (one row per instrument, many captures); set D1103, D1290, D1142, D1064 to `superseded_or_repealed` (enacted); merge D1010/D1022/D1023 into the D1291 instrument; recompute T02, S01, S03, Figure 6 and the "legislative pipeline" statements.

**F5. The "technical standards operationalise physical safety (83.3%) and proximity (50%)" finding is derived from catalogue abstracts and committee pages, not from standards.**
- Location: Executive summary item 5; §5.3 and Table 9; §8; §10 conclusion 2; paper §5.3 and §6 ("the standards are cited by almost nobody").
- Problem: of the ten technical-standard documents in the embodied set, D0045 is the ISO/TC 299 committee page, D0218 the ISO robotics sector landing page, D1337 a BSI project page for a preliminary work item, D0397 a catalogue entry for a working draft, D0129, D0162 and D0185/D0018/D1383 catalogue pages (`landing_or_index_page` or `partial_or_excerpt`, 693 to 1,531 words); only D0197 (SI 395, 1993) is a substantive text. All ten carry `pr_physical_safety = 2` ("substantively treated, operationalised or required"), including the committee page. The supplement's QA note counts three landing pages (D0218, D0398, D1382) but misses D0045, D1337 and D0397, and D0398/D1382 are not in the embodied set at all. Table 1's "12 technical standards" in the embodied set versus ten in S02 is a further inconsistency.
- Evidence: rows listed above; `page_quality` and `words` columns.
- Fix: reclassify committee/sector pages as `web_page_informational` (not governance documents); mark catalogue entries as "standard, metadata only" and exclude them from operationalisation statistics; if the claim about standards is to be kept, obtain the texts (ISO 10218-1/-2:2025, ISO/TS 15066, ISO 13482, ISO 3691-4, ANSI/A3 R15.06-2025, R15.08) under licence and annotate them, or restate the claim as "standards' scope statements name physical safety as their object".

**F6. "Autonomy level and control is discussed everywhere and specified nowhere" is contradicted by instruments outside the collection.**
- Location: Executive summary item 5; §5.3 ("operationalised nowhere above 8.3%"); §10 conclusion 2 and final paragraph; paper §6 ("the clearest gap is autonomy-level control ... specified in fewer than one in twelve").
- Problem: SAE J3016 (levels of driving automation), ISO 8373:2021 (robot autonomy definitions), UNECE R157 (ALKS: defined transition demands and minimum-risk manoeuvre), UNECE R171 (DCAS), Germany's StVG §1e (operation without a driver under a "technical supervisor"), the UK Automated Vehicles Act 2024 (the "self-driving test", "user-in-charge" and "no-user-in-charge" features), Japan's Road Traffic Act Level-4 permit regime ("specified automated operation"), California's DMV driverless-deployment rules, ISO 10218-2:2025 and ISO/TS 15066 (the four collaborative operation modes: safety-rated monitored stop, hand guiding, speed and separation monitoring, power and force limiting), and DoD Directive 3000.09 (levels of human judgment over the use of force) are precisely specifications of autonomy level and control transfer in binding or quasi-binding form. None is in the collection.
- Fix: restate as "not specified in the instruments captured"; add the above to the coverage audit; consider a dedicated "autonomy-level operationalisation" sub-code (defined levels; transition/takeover rules; remote supervision; minimal-risk condition; emergency stop).

### High

**F7. The social/companion-robot "governance gap" conflates "no robot-specific instrument" with "no regulatory home".**
- Location: Executive summary item 3; §4.4 ("without a regulatory home ... the clearest quantitative statement the collection permits about where embodied-AI governance is missing"); §7.4 ("What is not in the newest layer is any new instrument addressed to social, companion, educational or domestic robots"); §10 conclusion 3; paper abstract and §6.
- Problem: (a) the only two "instruments" that touch social robots are D1436 (an H2020 MARIO project deliverable written by academics; not a governance instrument, see F17) and D1008 (IEEE Ethically Aligned Design). (b) The horizontal regimes that already apply to a companion or educational robot are not acknowledged: AI Act Art. 5(1)(a)-(b) (manipulative or vulnerability-exploiting AI, with age and disability named), Art. 5(1)(f) (emotion recognition in education), Art. 50(1) (disclosure when an AI system interacts with a person), Annex III point 3 (education); the General Product Safety Regulation (EU) 2023/988 (applicable since 13 December 2024; it names connected products and children's mental health); the new Toy Safety Regulation (EU) 2025/2509 (published 12 December 2025, with connected/digital-toy provisions); the RED Delegated Regulation (EU) 2022/30 (cybersecurity of internet-connected consumer devices and toys, applicable 1 August 2025) and the Cyber Resilience Act (EU) 2024/2847; the Machinery Regulation (EU) 2023/1230, which classes "machinery with self-evolving behaviour" ensuring safety functions for third-party conformity assessment and applies to consumer robots; the GDPR (Art. 8 children; Art. 22) and COPPA; the Germany BNetzA prohibition of the "My Friend Cayla" doll (2017, Telecommunications Act §90), a binding enforcement action against a social toy robot; and the 2025 US state companion-chatbot statutes (California SB 243; New York's companion-AI provisions), which govern the conversational layer of any companion robot. ISO 13482 is captured and does cover "mobile servant" and "person carrier" robots in domestic use.
- Evidence: Table 7 (two instruments, both non-binding, for social robots); row D1436 (`issuer_type = academic_or_research`).
- Fix: rename the index "robot-specific instrument gap"; add a regime-coverage matrix (robot category × applicable horizontal regime, with "applies / applies with gaps / does not apply") and let the "gap" be the cells where neither a specific instrument nor a horizontal regime reaches a documented risk (deception, attachment, long-term emotional dependence are the real candidates).

**F8. The lifecycle-status and binding-nature scheme is applied inconsistently and conflates legal form with lifecycle stage.**
- Location: S2 codebook section C; T02; §3.2; Figure 4.
- Problem: (a) ten bills in the general set are coded `legally_binding` (D0066, D0085, D0055, D0057, D0002, D0059, D0071, D0075, D0699, D0459) while all embodied drafts are `not_applicable`; this is the source of the discrepancy between "29 binding in the general-AI set" (executive summary item 1; paper §5.1) and "39 (14.4%)" (§3.2, T02). (b) Binding instruments carry the soft-law status `published_current` (D0915, D0079). (c) Soft instruments carry `in_force` (D0460 Shanghai plan; D0331 NSW policy; D0930 OMB M-25-22, which actually binds agencies). (d) The same Peruvian regulation is `published_current` (D0079) and `adopted_not_yet_in_force` (D0080). (e) `technical_standard_mandated` is never used although mandatory standards exist (China's GB 11291.1-2011 and GB 11291.2-2013 are mandatory national adoptions of ISO 10218-1/-2; Taiwan's 2018 amendment makes CNS 14490/ISO 10218 the compliance route; harmonised EN ISO 10218 under the Machinery Directive confers presumption of conformity). (f) The scheme has no state for "adopted, phased application" (see F9).
- Fix: split into three fields: legal form (statute / secondary regulation / executive act binding public bodies only / court rule / soft law / standard), lifecycle (proposed / adopted / in force / applicable / amended / repealed) and applicability date(s); recode the ten bills; publish a reconciled count.

**F9. "In force" is not "applicable": the AI Act obligations that reach robots do not apply until 2028, and Annex I Section B products (vehicles, aircraft and drones, rail, marine) are outside the AI Act's Chapter III altogether.**
- Location: §3.2, §8, §10 conclusion 1 ("the AI Act's treatment of robots"), paper §2.2 and §6; rows D1060/D1291 (`in_force`); D1060's categories (autonomous vehicles, drones).
- Problem: Regulation (EU) 2024/1689 entered into force on 1 August 2024, but high-risk obligations were phased (Annex III 2 August 2026; Annex I Section A 2 August 2027), and the Digital Omnibus on AI, Regulation (EU) 2026/1744 (adopted 8 July 2026, in force 27 July 2026 according to multiple secondary sources; verify in the OJ), moved them to 2 December 2027 (Annex III) and 2 August 2028 (Annex I Section A: machinery, toys, lifts, medical devices, etc.). Annex I Section B products (type-approved vehicles under Regulation 2018/858 and 2019/2144, aircraft and unmanned aircraft under 2018/1139, rail, marine equipment) are excluded from Chapter III by Art. 2(2) and are reached only through the sectoral acts amended by Arts. 102-109. The annotator labelled D1060 with exactly the two categories (autonomous vehicles, drones) to which the AI Act's substantive obligations do not directly apply, because the Finnish OJ excerpt lists the amended vehicle and aviation acts. The Machinery Regulation applies from 20 January 2027 (the Machinery Directive 2006/42/EC governs robots until then), the revised Product Liability Directive (EU) 2024/2853 applies to products placed on the market from 9 December 2026, and the CRA's main obligations from 11 December 2027.
- Evidence: D1022/D1023 summaries note "Digital Omnibus amendments" in the consolidated text, so the pipeline saw the change without recording it.
- Fix: add applicability dates; state in §8 and §10 that, as of October 2026, no AI Act high-risk obligation yet applies to a robot as a machinery product; correct D1060's categories or annotate them "by amendment of sectoral acts".

**F10. "The AI Act treats robots as components of regulated products" is a mischaracterisation; "the AI Act's machinery annex/medical annex" do not exist.**
- Location: §10 conclusion 1; §8 (industrial and medical robots); paper abstract, §2.2, §6 and §8.
- Problem: under Art. 6(1) the high-risk trigger is an *AI system* that is a safety component of a product, or is itself a product, covered by Annex I legislation and subject to third-party conformity assessment; the robot is the product (under machinery, medical-device, toy or lift law) and its AI is the regulated system. Robots are also reached directly, irrespective of product law, by Art. 5 (prohibited practices), Art. 50 (transparency) and the Annex III use cases (education, employment, law enforcement, critical infrastructure, migration), and by the GPAI chapter where an embodied foundation model is involved. Annex I is a list of Union harmonisation legislation, not a "machinery annex".
- Fix: rewrite as "the AI Act reaches robots in three ways: as AI safety components of products under Annex I harmonisation law (machinery, medical devices, toys, lifts; Section B products via sectoral type-approval), as Annex III use cases, and through the horizontal Art. 5 and Art. 50 duties".

**F11. Argentina's Resolution 710/2024 (D0016) is described as "an Argentine security-robotics resolution"; it is a ministerial act creating an internal unit.**
- Location: Executive summary item 2; §8 ("Argentina's security-AI unit"); paper §5.1 ("creating a security-AI unit with drone and policing-robot competence").
- Problem: the instrument creates the Unidad de Inteligencia Artificial Aplicada a la Seguridad inside the Ministry of Security and lists tasks (social-media patrolling, facial recognition, drone patrols, bomb-disposal robots). It binds the ministry's own organisation, imposes no obligation on robot makers or operators, and contains no robot-specific rule. Counting it with the Dubai statute as "binding governance of robots" stretches the term.
- Fix: keep it, but code `binds = public body (internal organisational act)` and describe it accurately; do not list it among instruments that "govern" drones or policing robots.

**F12. The AI Liability Directive is treated as a live proposal; it was withdrawn (Commission Work Programme 2025, 11 February 2025).**
- Location: §5.3 ("the EU's proposed AI Liability Directive"); §8 (medical robots "governed through ... the proposed AI Liability Directive"); paper §2.2 background; T13 label "(proposal)".
- Problem: the proposal COM(2022) 496 was listed for withdrawal in February 2025 for lack of foreseeable agreement; its functions were partly taken over by the revised Product Liability Directive (EU) 2024/2853 (software and AI as "products", Art. 4; disclosure of evidence, Art. 9; rebuttable presumptions of defect and causation, Art. 10), which the report cites only by name and never engages with substantively although it is the single most important liability text for physical AI.
- Fix: mark the AILD as withdrawn; summarise the PLD's embodied-relevant provisions (software updates, substantial modification, defectiveness presumption, 25-year long-stop for latent bodily injury).

**F13. The regional characterisations are characterisations of each team's sample, and the Africa/International assignment is asymmetric.**
- Location: §6 Part D and Table 14; executive summary item 7; paper §5.4 and §6.
- Problem: (a) The Middle East's "liability-led" profile: 25 of its 37 embodied documents are journal articles (Iran 6, Iraq 6, Türkiye 5, Israel 5, Jordan 4), one statute (Dubai), one bill; it describes an Arabic/Persian legal-doctrinal literature, not governance. (b) Africa's profile rests on 17 general instruments and one embodied instrument (D0402 Mauritius, where "robotics and drones appear only incidentally"); the African Commission's Resolution 473 (D0368) that §6 names as Africa's robotics resolution is assigned to "International", whereas EU bodies are assigned to "Europe". (c) The United States' "11 binding instruments" are mostly executive orders plus a BIS rule and three state statutes (one a blocked capture); none regulates a robot; the US embodied binding layer (NHTSA Standing General Order 2021-01, FMVSS amendments for vehicles without manual controls, state AV and personal-delivery-device statutes, FAA Part 107/Part 89, DoD Directive 3000.09) is absent. (d) Europe's "conformity-led" profile reflects AI Act pipeline documents captured ten-plus times, not European robot law (Machinery Regulation, GSR 2019/2144 and Implementing Regulation 2022/1426 on automated driving systems, drone rules, StVG, UK AV Act, French ordonnance 2021-443). (e) Asia's "industrial" profile is fair for the captured strategies but omits binding Asian embodied law (Japan's Road Traffic Act Level-4 regime, Korea's Intelligent Robots Act and Autonomous Vehicles Act, Shenzhen 2022 and Beijing 2025 AV regulations, mandatory GB standards, MIIT's 2023 humanoid Guiding Opinions, Singapore's AMV Rules).
- Fix: label each regional profile "as captured"; assign AU/ACHPR, ASEAN, Arab League, CARICOM and OAS instruments to their regions for parity with the EU; add a "binding embodied law known but not captured" column to Table 14 from the section-4 list.

**F14. EU institutions are coded as "intergovernmental organisations" and the Civil Law Rules on Robotics as an "intergovernmental recommendation".**
- Location: S2 codebook (`issuer_type`: "EU institutions count as intergovernmental_org"); §3.1 issuer analysis ("legislatures 12"); D1299/D1304 (`intergovernmental_recommendation_or_resolution`).
- Problem: the European Parliament is a directly elected legislature and Regulation 2024/1689 is legislation of a supranational legal order with direct effect; coding them as IGO output understates "legislature" and "statute" in Europe and makes the EU look like the OECD. The 2017 resolution is an own-initiative legislative resolution under Art. 225 TFEU requesting a Commission proposal, i.e. a legislative-initiative act, not a recommendation of the UNESCO type.
- Fix: add `supranational_institution` to `issuer_type` and `legislative_initiative_resolution` (or map to `parliamentary_material`) to `doc_type`.

**F15. The canonical named-instrument list and the 27-term lexicon are biased against embodied instruments, so the citation findings are bounded by the list.**
- Location: S2 (`named_instruments_referenced` list); §5.7 and Table 13 ("Only 32.9% of embodied documents cite any named instrument"; "ISO robot-safety standards are cited by at most 3.4%"); §9.2.
- Problem: the list has ~30 entries of which only ISO 10218, 13482, 3691-4, ISO/TS 15066, ANSI/A3 R15.06, the Machinery Regulation, the PLD/AILD, the Civil Law Rules and Korea's Act are embodied; no AV, drone, medical-device, functional-safety or OSH instrument is listed, and the lexicon cannot catch what the list omits. The free-text fallback shows the annotator does add names when the text is explicit ("Medical Device Rules 2017", "UK Medical Devices Regulations 2002", "ISO 8373", "ISO 12100"), which means the deficit is in the list, not the model.
- Fix: extend the list with the ~60 instruments in section 4 and re-run the lexicon; report citation shares per list version.

**F16. Reliability (kappa 0.93 for instrument status between two LLMs on the same excerpt) does not validate the instrument layer.**
- Location: §9.1; paper §4.2 and §7 ("reliability is high for class, status, binding nature").
- Problem: inter-model agreement on a 204-word login stub (Taiwan), a Finnish OJ excerpt (AI Act) or a revoked order produces agreement on shared errors; the fields that carry the headline claims (status, year, binding nature) were never checked against ground truth by a lawyer. Nine of the fifteen documents I checked most closely have at least one field that is wrong or legally unsound.
- Fix: a human legal audit of the 63 embodied governance documents and the 55 `legally_binding` documents (a few hours' work); report human-model agreement separately for status, year and binding nature.

**F17. Several documents are miscoded as governance instruments, and one of them anchors a dated claim.**
- Location: S02; §3.3 ("Care and companion robots enter ... governance in 2014 to 2015 (ISO 13482; an Irish ethics framework for care robots)"); §4.4; Table 3; rows D1436, D0511, D0945, D0045, D0218.
- Problem: D1436 is deliverable D1.2 of the H2020 MARIO project (issuer academic; it is a research-ethics framework for a trial), not an Irish governance instrument; D0511 is the programme director's policy appendix to a JST Moonshot funding call; D0945 is a CPSC staff report that "has not been reviewed by the Commission"; D0045 and D0218 are ISO web pages. Conversely D0503 (White Paper on Embodied AI, Singapore Standards Council with ASTM International, 2026, a standards roadmap by a national standards body) is coded `industry_or_ngo_report`.
- Fix: recode as in section 3; the "first governance mention" for care robots then becomes ISO 13482 (2014) alone, and for social robots IEEE EAD (2017/2019).

### Medium

**F18. Year and status errors beyond Taiwan.**
- D0713 Taiwan AI Basic Act: `year_final = 2021`, `confidence = 0.35`, 205 words of login stub; the Act was passed in December 2025 and promulgated in January 2026 (verify on the same MOJ database). D0944 EO 13859 coded `superseded_or_repealed` although EO 14179 revoked only EO 14110. D1677 Charter of Fundamental Rights coded `international_treaty_or_convention`, year 2010 (proclaimed 2000; binding since 1 December 2009 as EU primary law). D0185 ISO 13482:2014 `published_current` without noting that the second edition is at FDIS/approval stage (ISO project 83498; FprEN ISO 13482 scheduled for 2026), so the "standard" may be superseded within the study's life. D1008 IEEE EAD dated 2017 is the version-2 draft; the first edition is 2019. D0699 (Japanese bill) should be `superseded_or_repealed` because it was enacted as Act No. 53 of 2025 (captured as D0712). D0005: the Salvadoran robotics law is real (approved 3 July 2025 with 59 votes; published in Diario Oficial No. 135, Tomo 448; in force 29 July 2025) but the decree number "340" and `source_url` (missing) should be verified against the Diario Oficial.
- Fix: as above; set `confidence < 0.5` documents aside from instrument-level counts unless human-verified.

**F19. "Industrial manipulators have the oldest governance text (Israel's SI 395, 1993)" and Table 3's first-appearance years are presented as facts about governance rather than about the collection.**
- Location: §3.3, Table 3.
- Problem: ANSI/RIA R15.06-1986, Japan's 1983 Ordinance on Industrial Safety and Health amendment (Arts. 150-3 to 151) and Ministry of Labour guideline, Taiwan's 1987 rule and ISO 10218:1992 all predate 1993; first-appearance years for vehicles (2014), drones (2014) and medical robots (2014) are likewise years of first *capture*.
- Fix: caption every "first appearance" as "in this collection"; add a column with the earliest known instrument from the coverage audit.

**F20. Taxonomy: defensible but with four weaknesses that bear on the results.**
- (a) Autonomous road vehicles and drones are inside "embodied AI" (defensible), but none of their governance regimes is captured, so the negative pole of the gap index (vehicles −33.7, drones −16.1) is produced by 29 strategies that *mention* vehicles, not by vehicle law; either capture the regimes or report the index without the vehicle categories. (b) `humanoid_general_purpose` merges morphology (humanoids) with model generality (embodied foundation models); the two have different regulatory hooks (machinery safety and pHRI limits versus GPAI obligations and systemic-risk duties). (c) `other_embodied` has more primary assignments (25) than any-mention counts (23) in S3 and is mostly Middle Eastern "smart robot" liability scholarship that belongs in `embodied_ai_robotics_general`. (d) Construction, mining and agricultural autonomous machinery are scattered across `space_or_extreme_environment` and `agricultural_robots`; a `field_and_construction_machinery` category would map onto the Machinery Regulation and ISO 17757 (earth-moving autonomy). Credit: software "robots" are correctly excluded; zero `software_agent_called_robot` documents leak into the embodied set.

**F21. Principle and mechanism lists omit items that are central to embodied AI.**
- Principles: deception and anthropomorphism limits (EPSRC Principles of Robotics 2010/2011 principle 4; EP 2017 Charter; AI Act Art. 50; BS 8611:2016), which is *the* social-robot principle and is absent; predictability/legibility of robot behaviour; necessity and proportionality in the use of force (policing and military); accessibility. Mechanisms: emergency stop, safe state and kill switch; protective separation distance, speed-and-separation monitoring and power-and-force limiting (the pHRI limits of ISO/TS 15066 and ISO 10218-2:2025); operational design domain and geofencing; remote supervision and teleoperation rules and remote-operator licensing; type approval, market surveillance, recall and post-market monitoring (AI Act Art. 72; PLD; GPSR); event data recorders and logging (AI Act Art. 12; StVG §63a; UK AV Act); registration, identification and owner linkage (EP 2017; Brazil PL 391/2026); cybersecurity and update obligations (CRA; UNECE R155/R156); worker information and consultation (AI Act Art. 26(7); Framework Directive 89/391 Art. 11; German Works Constitution Act §87); operating permits and pilot zones (Dubai; Beijing; Shenzhen; Japan's Level-4 permit); authorised self-driving entity and user-in-charge immunity (UK AV Act); compulsory insurance (exists, correctly). Evidence that the lists matter: corpus text searches find "emergency stop/shutdown" in two governance documents, "geofenc*" in none, "remote operation/teleoperation" in no governance document, "worker consultation" in one.
- Fix: add the items; re-annotate the (small) governance subset.

**F22. "ISO standards are voluntary" needs the harmonised-standard nuance, which is the whole point for policy readers.**
- Location: S2 (`technical_standard_voluntary`); §3.2; §10 ("the operative texts will be standards").
- Problem: harmonised EN ISO standards cited in the OJ confer presumption of conformity under the Machinery Directive and, in future, under the Machinery Regulation and the AI Act (Art. 40; standardisation request C(2023) 3215 to CEN-CENELEC); China's GB 11291 series is mandatory; Taiwan's rule and Japan's Ordinance incorporate CNS 14490/JIS B 8433 (ISO 10218) by reference; OSHA treats ANSI/A3 R15.06 as recognised practice under the general-duty clause. "Voluntary" is true de jure and misleading de facto; the study's strongest policy message ("standards are where embodied AI is governed") depends on this nuance and should state it.
- Fix: add a `standard_legal_effect` field (purely voluntary / harmonised with presumption of conformity / incorporated by reference / mandatory national standard).

**F23. Numeric inconsistencies in the text.**
- "29 binding in the general-AI set" (executive summary, paper §5.1) versus "39 (14.4%)" (§3.2) versus T02 (24 + 3 + 9 + 1 + 2 = 39); "12 technical standards" (Table 1, embodied column) versus 10 (S02); "63 instruments" includes D0945, a government report; the supplement says three landing pages inflate the standards count, but seven of the 63 embodied governance documents are `landing_or_index_page`; "5 open consultations" include two captures of the same Israeli draft (D0191/D1687) and the Commission's draft high-risk classification guidelines (D1053), which were due under Art. 6(5) by February 2026 and may already be adopted (verify); Egypt is assigned to the Middle East in §1 and to Africa in Table 4.
- Fix: reconcile after the recoding in F4 and F8.

**F24. Claims about the "newest layer" miss 2025 to 2026 instruments that address the very robots said to be unaddressed.**
- Location: §7.4; §10 conclusion 5; paper §6.
- Problem: the Toy Safety Regulation (EU) 2025/2509, the GPSR's application (December 2024), California SB 243 (2025) on companion chatbots, China's national humanoid-robot standards programme (captured only as a Beijing news item, D0650), the ISO 13482 second edition (FDIS 2025/26), ISO 10218-1/-2:2025 and ANSI/A3 R15.06-2025 (captured only as a blog, D0828) are all 2025 to 2026 instruments addressed to consumer, companion, humanoid or collaborative robots.
- Fix: capture and re-run §7.

**F25. Minor legal wording.** §8 says "ISO 10218 and ISO/TS 15066 for arms and cobots": ISO 10218-2:2025 absorbed the TS 15066 collaborative requirements (the TS remains published but is no longer the operative text). §8 says industrial robots are governed by "the EU Machinery Regulation": until 20 January 2027 it is the Machinery Directive. §5.7 "the EU Machinery Regulation (3.6%)": many of those citations in older papers are to the Directive. Paper §2.2 "the AI Act's Annex I treat[s] robots as products subject to harmonised standards": Annex I lists legislation; the harmonised-standards route is Art. 40.

### Low

**F26. Executive orders and court practice directions in the "binding" class without qualification.** Singapore's Registrar's Circular and the Canadian court notice on generative AI are practice directions binding on litigants; the OMB memoranda bind agencies; executive orders bind agencies. These are correctly "binding" on someone but are not regulation of AI products or services; the "US has the most binding AI instruments" sentence (§3.4, §6) would not survive a `binds` field.

**F27. Presentation.** Table 12/13 numbering is reused in §8 for S12/S13; Figure 6's caption should say "captures"; "Dubai autonomous-vehicle law" is emirate-level law (jurisdiction scope subnational) and is correctly coded, but the text alternates between "Dubai" and "the UAE".

---

## 3. Classification corrections for individual documents

| doc_id | field | current value | corrected value | reason / source |
|---|---|---|---|---|
| D0480 | year_final | 2025 | 1987 (amended 1998, 2014, 2018; last amendment 2018-02-14) | MOJ Laws & Regulations Database history page, pcode N0060025 (promulgated 1987-01-19 by Ministry of the Interior; amendments 1998-06-30, 2014-06-30, 2018-02-14 by Ministry of Labor) |
| D0480 | text / confidence | 204-word login stub, confidence 0.40 | re-capture full text (LawAll.aspx serves it); until then exclude from instrument-level statistics | annotation "relies on the title and URL" |
| D0915 | instrument_status | published_current | superseded_or_repealed | EO 14110 revoked by EO 14148 (20 Jan 2025); successor EO 14179 captured as D0918 |
| D0915 | binds (new field) | — | public bodies (federal agencies) | nature of executive orders |
| D0944 | instrument_status | superseded_or_repealed | in_force | EO 13859 (2019) was not revoked by EO 14179 |
| D1010 | duplicate handling | counted as separate statute | capture of the same instrument as D1291 (catalogue record, metadata only); exclude from counts | summary: "Only metadata and the purpose statement appear" |
| D1022, D1023 | doc_type / year_final | statute_or_act, 2026 | web_page_informational reproducing Arts. 62 and 26 of Reg. 2024/1689; link to instrument D1291; year 2024 | AI Act Service Desk pages |
| D1060 | embodied_categories | autonomous_road_vehicles; drones_uas | align with D1291 (AI safety components of Annex I Section A products; Section B vehicles/aircraft reached only via Arts. 102-109) or annotate "by amendment of sectoral acts" | Art. 2(2) and Annex I Section B of Reg. 2024/1689 |
| D1060, D1291 | instrument_status | in_force | in_force, phased application (Art. 5 and Art. 50 applicable; Annex III from 2 Dec 2027; Annex I Section A from 2 Aug 2028 per Reg. (EU) 2026/1744, verify in OJ) | Digital Omnibus on AI |
| D1103, D1290 | instrument_status | draft_or_bill_under_consideration | superseded_or_repealed (enacted as Reg. 2024/1689) | 2021 Commission proposal |
| D1142, D1064 | instrument_status | draft_or_bill_under_consideration | superseded_or_repealed (enacted) | 2023/2024 negotiating texts |
| D1310 | duplicate handling | separate document | Italian-language capture of D1290 | same COM(2021) 206 |
| D0016 | binds (new field) / narrative | "security-robotics resolution" | internal organisational act of the Ministry of Security creating a unit; binds public body only | text of Res. 710/2024 |
| D0005 | source_url / identifier | missing; "Decree No. 340" | add Diario Oficial reference (No. 135, Tomo 448; approved 3 Jul 2025; in force 29 Jul 2025); verify decree number | Salvadoran press reports of the DO publication; decree number not independently confirmed |
| D0001, D0144 | duplicate handling | two documents | one instrument (Decree 234, Ley para el Fomento de la IA y Tecnologías, 26 Feb 2025) | summaries |
| D0079, D0080 | instrument_status | published_current / adopted_not_yet_in_force | one instrument (DS 115-2025-PCM approving the Regulation of Law 31814); in_force (verify entry-into-force clause) | same decree captured twice |
| D0460 | instrument_status | in_force (with voluntary_soft_law) | published_current, or legally_binding if treated as a municipal normative document with effective dates (28 Jul 2025 to 27 Jul 2028); not both | consistency of scheme |
| D0511 | is_governance_document / doc_type | True / policy_guideline_or_code_of_practice | False / other (funding-call programme-director policy, JST Moonshot) | summary |
| D1436 | is_governance_document / doc_type / issuer | True / ethical_framework_or_principles / academic | False / industry_or_ngo_report or research deliverable (H2020 MARIO D1.2) | summary; issuer academic |
| D0945 | is_governance_document | True (status proposal_or_concept) | False (CPSC staff report "not reviewed by the Commission") | summary |
| D0045 | doc_type / is_governance_document | technical_standard / True | web_page_informational (ISO/TC 299 committee page) / False | summary |
| D0218 | doc_type / is_governance_document | technical_standard / True | web_page_informational (ISO sector landing page) / False | summary |
| D1337 | doc_type / status | technical_standard, under_development (2021) | standard project page (ISO/PWI 13482, BSI); keep status under_development but exclude from instrument counts; note the project is now at FDIS (ISO project 83498) | ISO catalogue |
| D0397 | status | under_development | under_development (ISO/WD 26058-1); exclude from operationalisation statistics (catalogue page) | ISO catalogue |
| D0185 | instrument_status | published_current | published_current, under revision (ISO/FDIS 13482 second edition at approval stage; FprEN ISO 13482 scheduled 2026) | ISO catalogue page itself says "to be replaced by ISO/FDIS 13482" |
| D0129, D0162 | page handling | technical_standard, published_current | keep, but flag "metadata only" and exclude from principle-operationalisation statistics | page_quality landing_or_index_page |
| D0197 | instrument_status | unknown | verify with the Standards Institution of Israel whether SI 395 is current and whether declared an official (mandatory) standard; if so binding_nature = technical_standard_mandated | Israeli Standards Law 1953 mechanism |
| D0713 | year_final / confidence | 2021 / 0.35 (login stub) | 2026 (Act passed Dec 2025, promulgated Jan 2026; verify); re-capture text | MOJ database |
| D0699 | instrument_status / binding_nature | draft_or_bill_under_consideration / legally_binding | superseded_or_repealed (enacted as Act No. 53 of 2025 = D0712) / not_applicable | same instrument |
| D0066, D0085, D0055, D0057, D0002, D0059, D0071, D0075, D0459 | binding_nature | legally_binding | not_applicable (bills under consideration), consistent with embodied-set drafts | codebook consistency |
| D1677 | doc_type / year_final | international_treaty_or_convention / 2010 | EU primary law (statute-equivalent) / 2000 proclaimed, binding 2009 | Art. 6(1) TEU |
| D1299, D1304 | doc_type / issuer_type / duplicates | intergovernmental_recommendation_or_resolution / intergovernmental_org / two documents | legislative-initiative resolution (Art. 225 TFEU) / supranational legislature / one instrument (BG and EN captures) | nature of the EP resolution |
| D0368 | study_region | International | Africa (African Commission on Human and Peoples' Rights is an AU organ; parity with EU → Europe) | §1 region rule |
| D0191, D1687 | duplicate handling | two consultations | one draft strategy captured twice | titles and summaries |
| D0503 | doc_type / is_governance_document | industry_or_ngo_report / False | policy white paper by a national standards body (Singapore Standards Council with ASTM); consider is_governance_document True as a standards roadmap | issuer_type standards_body |
| D0621 | note | governance doc, 0 words | keep excluded (stub); add the actual Korea Robot Industry Technology Roadmap and the Intelligent Robots Act to the capture list | text_status stub |
| D1008 | year_final | 2017 | 2017 (EAD v2) with note that the first edition is 2019 | IEEE |
| EG rows | study_region | Africa (Table 4) vs Middle East (§1 text) | choose one and apply consistently | §1 |

---

## 4. Reference list: binding or quasi-binding instruments relevant to embodied AI that are not in the collection (for a coverage audit)

Status is as of October 2026 to the best of my knowledge; items marked "verify" should be confirmed against the official source before use. "Not captured" was determined by title, summary, key-provision and named-instrument searches of `master_table.csv`; some instruments are *cited* by captured documents (noted) but no capture of the instrument itself exists.

### European Union

| Instrument | Jurisdiction | Year | Status | Why relevant |
|---|---|---|---|---|
| Machinery Regulation (EU) 2023/1230 | EU | 2023 | adopted; applies 20 Jan 2027 | the product-safety law for robots; new provisions on machinery with self-evolving behaviour and AI safety functions (third-party conformity assessment); cited by 25 captured documents, never captured |
| Machinery Directive 2006/42/EC | EU | 2006 | in force until 20 Jan 2027 | currently applicable robot law; EN ISO 10218 harmonised under it |
| Product Liability Directive (EU) 2024/2853 | EU | 2024 | in force; applies to products placed on the market from 9 Dec 2026 | software/AI as product; presumptions of defect; bodily-injury long-stop; cited by 23 documents, never captured |
| General Product Safety Regulation (EU) 2023/988 | EU | 2023 | applicable since 13 Dec 2024 | consumer robots outside sectoral law; connected products; children's mental health |
| Toy Safety Regulation (EU) 2025/2509 | EU | 2025 | published 12 Dec 2025; in force 1 Jan 2026; transition to 2030 (verify dates) | toy, entertainment and educational robots; digital/connected-toy provisions |
| Cyber Resilience Act (EU) 2024/2847 | EU | 2024 | in force; reporting duties from Sept 2026, main obligations 11 Dec 2027 | cybersecurity and update duties for connected robots |
| RED Delegated Regulation (EU) 2022/30 | EU | 2022 | applicable 1 Aug 2025 | cybersecurity of radio-connected consumer devices, toys, wearables |
| Medical Devices Regulation (EU) 2017/745 | EU | 2017 | applicable since 2021 | surgical and rehabilitation robots; MDCG/AIB guidance is captured (D1013) but not the Regulation |
| Regulation (EU) 2019/2144 (General Safety Regulation) and Implementing Regulation (EU) 2022/1426 | EU | 2019 / 2022 | in force | EU type-approval of automated and fully automated driving systems; AI Act Section B route |
| Regulation (EU) 2018/858 (vehicle type approval), amended by AI Act Art. 104 | EU | 2018 | in force | the route through which the AI Act reaches vehicles |
| Delegated Regulation (EU) 2019/945 and Implementing Regulation (EU) 2019/947 (drones); Implementing Regulation (EU) 2021/664 (U-space) | EU | 2019 / 2021 | applicable since 31 Dec 2020 / 26 Jan 2023 | the binding drone regime; 14 captured "drone" instruments are strategies |
| Regulation (EU) 2018/1139 (EASA Basic Regulation), amended by AI Act Art. 108 | EU | 2018 | in force | aircraft and unmanned aircraft |
| Digital Omnibus on AI, Regulation (EU) 2026/1744 | EU | 2026 | adopted July 2026 (verify number and dates in OJ) | changes AI Act application dates (Annex III 2 Dec 2027; Annex I 2 Aug 2028) |
| Commission Guidelines on prohibited AI practices (C(2025) 884) and on the definition of an AI system (Feb 2025) | EU | 2025 | published | captured only as ~25 duplicate news pages; the guidelines' examples on manipulation and emotion recognition bear on companion and educational robots |
| Standardisation request C(2023) 3215 to CEN-CENELEC (AI Act Art. 40) and CEN-CENELEC JTC 21 work programme | EU | 2023 (amended 2025, verify) | in progress | the harmonised-standards route for high-risk AI, including robots |
| Framework Directive 89/391/EEC; Work Equipment Directive 2009/104/EC | EU | 1989 / 2009 | in force | OSH law for robots at work; worker consultation |
| EP resolutions 2020/2014(INL) (civil liability regime for AI) and 2020/2012(INL) (ethics framework) | EU | 2020 | soft | the successors of the 2017 Civil Law Rules |
| EN ISO 10218-1/-2:2025, EN ISO 13482, EN ISO 3691-4, EN ISO 13849-1:2023, EN IEC 62061:2021, EN ISO 12100:2010 | EU/CEN | various | harmonised (presumption of conformity under the Machinery Directive; harmonisation under the Regulation pending) | the quasi-binding standards layer |

### European states

| Instrument | Jurisdiction | Year | Status | Why relevant |
|---|---|---|---|---|
| Gesetz zum autonomen Fahren (StVG §§1e-1l) and AFGBV ordinance | Germany | 2021 / 2022 | in force | first Level-4 statute: technical supervisor, approved operating areas, data duties |
| StVG amendment on automated driving functions (§1a-1c, §63a data recorder) | Germany | 2017 | in force | Level-3 rules and the event data recorder |
| Automated Vehicles Act 2024 | United Kingdom | 2024 | Royal Assent 20 May 2024; secondary legislation and statutory safety principles in progress | authorised self-driving entity, user-in-charge, incident investigation, marketing restrictions |
| Automated and Electric Vehicles Act 2018 | United Kingdom | 2018 | in force | insurer first-instance liability for automated vehicles |
| Ordonnance n° 2021-443 and Décret n° 2021-873 | France | 2021 | in force | criminal responsibility during automated driving; Level-4 shuttle services |
| Air Navigation Order 2016 and retained UAS Regulation 2019/947 | United Kingdom | 2016 / 2019 | in force | drones |
| BNetzA prohibition of the "My Friend Cayla" doll (Telecommunications Act §90) | Germany | 2017 | enforcement action | binding action against a social toy robot: the counter-example to "no instrument reaches social robots" |
| BS 8611:2016 Robots and robotic devices: guide to the ethical design and application | United Kingdom | 2016 | published (BSI) | first robot-ethics standard; deception and anthropomorphism |
| EPSRC/AHRC Principles of Robotics | United Kingdom | 2010/2011 | soft | source of the "no deception" principle |

### Asia-Pacific

| Instrument | Jurisdiction | Year | Status | Why relevant |
|---|---|---|---|---|
| Intelligent Robots Development and Distribution Promotion Act (Act No. 9014, as amended) | Korea | 2008 | in force | the only general robotics statute of long standing; certification, ethics charter basis; cited by 5 captured documents, not captured |
| Act on Promotion of and Support for Commercialisation of Autonomous Vehicles | Korea | 2019 (in force 2020) | in force | pilot zones, safety and insurance for AVs |
| Framework Act on the Development of AI and Establishment of Trust | Korea | 2024 (in force 22 Jan 2026) | in force | captured only as the Enforcement Decree (D0782); covers high-impact AI including robots |
| Robot Ethics Charter | Korea | 2007 draft / 2018 | soft | early robot-ethics instrument |
| Road Traffic Act amendment for Level-4 "specified automated operation" (Act No. 32 of 2022) | Japan | 2022 (in force 1 Apr 2023) | in force | permit regime for driverless operation; also creates the "remote-operated small vehicle" category for sidewalk delivery robots |
| Road Traffic Act and Road Transport Vehicle Act amendments (Level 3) | Japan | 2019 (in force 2020) | in force | first Level-3 regime |
| Ordinance on Industrial Safety and Health, Arts. 150-3 to 151 (industrial robots) and 2013 MHLW notification on collaborative operation | Japan | 1983 / 2013 | in force | oldest binding industrial-robot safety rule; collaborative operation under risk assessment |
| New Robot Strategy (Robot Revolution Realization Council) | Japan | 2015 | soft | captured only as a dead link (D0597) |
| Guiding Opinions on the Innovative Development of Humanoid Robots (MIIT) | China | 2023 | soft (policy) | the central humanoid-policy instrument; 2025/2027 targets |
| 14th Five-Year Plan for the Development of the Robotics Industry (MIIT and 14 ministries) | China | 2021 | soft (policy) | national robotics plan |
| GB 11291.1-2011 and GB 11291.2-2013 (mandatory adoption of ISO 10218-1/-2) | China | 2011 / 2013 | mandatory national standards | binding robot-safety standards; refutes "ISO standards are voluntary" as a global statement |
| Shenzhen Special Economic Zone Regulations on Intelligent Connected Vehicles | China (Shenzhen) | 2022 | in force 1 Aug 2022 | first binding Chinese AV regulation (liability allocation) |
| Beijing Autonomous Vehicles Regulations | China (Beijing) | 2024 (in force 1 Apr 2025) | in force | municipal AV statute |
| Beijing Humanoid Robot Innovation Development Action Plan (2023-2025); Shenzhen Action Plan for the Embodied Intelligent Robot Industry (2025-2027) | China | 2023 / 2025 | soft (policy) | peers of the captured Shanghai plan |
| National standards for humanoid robots (technical requirements series, under development) | China | 2025- | under development | captured only as a Beijing news item (D0650) |
| Road Traffic (Autonomous Motor Vehicles) Rules 2017 and Technical Reference TR 68 | Singapore | 2017 / 2019-2021 | in force / published | AV trial regime |
| Unmanned Vehicles Technology Innovative Experimentation Act | Taiwan | 2018 | in force | sandbox statute for autonomous vehicles, vessels and aircraft |
| Drone Rules 2021 | India | 2021 | in force | drones |
| Commonwealth Automated Vehicle Safety Law (NTC reform; legislation planned) | Australia | 2024-2026 | in preparation (verify) | national AV regime; Oceania's embodied binding layer |

### Americas

| Instrument | Jurisdiction | Year | Status | Why relevant |
|---|---|---|---|---|
| NHTSA Standing General Order 2021-01 (crash reporting for ADS and Level-2 systems), as amended 2023 and 2025 | United States | 2021 | in force | binding on named manufacturers; incident reporting for AVs |
| FMVSS amendments for vehicles without manual controls (final rule, Mar 2022); Part 555 exemptions; AV STEP (NPRM Jan 2025) and the April 2025 AV Framework | United States | 2022-2025 | in force / proposed | federal AV safety law |
| State AV statutes and rules (e.g. California 13 CCR §227-228; Arizona ARS 28-9701; Texas SB 2205; Florida HB 311) | United States (states) | 2017-2024 | in force | the actual binding AV layer in the US (about 30 states) |
| Personal delivery device statutes (Virginia 2017 and ~20 states) | United States (states) | 2017- | in force | sidewalk delivery robots |
| 14 CFR Part 107 (small UAS), Part 89 (Remote ID), Part 108 BVLOS (NPRM Aug 2025, verify) | United States | 2016 / 2021 / 2025 | in force / proposed | drones |
| DoD Directive 3000.09 Autonomy in Weapon Systems (reissued 25 Jan 2023) | United States | 2012 / 2023 | in force | the only binding national instrument on autonomous weapons; cited once |
| OSHA 29 CFR 1910.212 and 1910.147; OSHA Technical Manual Section IV Ch. 4 (industrial robots) | United States | various | in force / guidance | OSH law for industrial robots |
| ANSI/A3 R15.06-2025 (industrial robots), ANSI/A3 R15.08-1-2020 and -2-2023 (industrial mobile robots), UL 4600 (autonomous products), UL 3300 (service robots) | United States | 2020-2025 | published | US consensus standards; R15.06-2025 captured only as a blog (D0828) |
| California SB 243 (companion chatbots) and New York companion-AI law | United States (states) | 2025 | in force (verify effective dates) | govern the conversational layer of companion robots |
| COPPA Rule amendments | United States | 2025 | in force | connected toys |
| Ontario Automated Vehicle Pilot Program (O. Reg. 306/15, amended 2019); Transport Canada ADS Safety Framework | Canada | 2016 / 2019-2021 | in force / guidance | Canada's embodied layer (none captured) |
| PL 2338/2023 (AI framework bill, passed Senate Dec 2024) | Brazil | 2023-2026 | under consideration (verify) | Brazil's main AI bill is referenced once but should be checked for capture |

### International and standards

| Instrument | Jurisdiction | Year | Status | Why relevant |
|---|---|---|---|---|
| UNECE Regulation No. 157 (ALKS; amended 2022 to 130 km/h and lane change) | UN 1958 Agreement parties | 2021 | in force | first binding Level-3 type-approval regulation; defines control transfer |
| UNECE Regulation No. 171 (Driver Control Assistance Systems) | UN | 2024 | in force | Level-2 systems |
| UNECE Regulations No. 155 (cybersecurity management) and No. 156 (software updates) | UN | 2021 | in force | cybersecurity and update obligations for vehicles |
| ISO 10218-1:2025 and ISO 10218-2:2025 | ISO | 2025 | published Feb 2025 | the core industrial-robot safety standards; absorb ISO/TS 15066 content; cited by 16 documents |
| ISO/TS 15066:2016 | ISO | 2016 | published (largely absorbed into 10218-2:2025) | pHRI force and pressure limits |
| ISO 13482 second edition (ISO/FDIS 13482) | ISO | 2025-2026 | FDIS/approval stage | will replace the captured 2014 edition |
| ISO 13849-1:2023, IEC 62061:2021, IEC 61508 series | ISO/IEC | 2010-2023 | published | functional-safety lineage for robot control systems |
| ISO 12100:2010 | ISO | 2010 | published | risk assessment method presupposed by every robot standard |
| IEC 80601-2-77:2019 (robotically assisted surgical equipment) and IEC 80601-2-78:2019 (rehabilitation robots) | IEC | 2019 | published | the medical-robot safety standards (none captured) |
| ISO 22166-1:2021 (modular service robots), ISO 18646 series, ISO/TR 23482-1/-2 | ISO | 2019-2021 | published | service-robot standards |
| ISO 21448:2022 (SOTIF), ISO 26262:2018, ISO/SAE 21434:2021, ISO 34502:2022 | ISO/SAE | 2018-2022 | published | AV safety standards beside the captured ISO/PAS 8800 |
| SAE J3016 (levels of driving automation) | SAE | 2021 | published | the operationalisation of "autonomy level" |
| ISO 8373:2021 (robotics vocabulary) | ISO | 2021 | published | definitions of robot autonomy; cited 3 times |
| IEEE 7001-2021 (transparency of autonomous systems) | IEEE | 2021 | published | cited as P7001; the standard itself not captured |
| UN CCW GGE on LAWS rolling text; UNGA Resolutions 78/241 (2023) and 79/62 (2024) | UN | 2023-2025 | ongoing | the multilateral LAWS process; captured only as citations |
| IMO MASS Code (non-mandatory code approved 2025; mandatory code planned later this decade) | IMO | 2025 | non-mandatory (verify) | autonomous ships; category has one captured instrument |
| ISO 17757 (earth-moving machinery autonomy) | ISO | 2019 | published | field and construction machinery |

---

## 5. What is done well

- A pre-written 39-field codebook, fixed prompt hash, JSON schema enforcement, and full scripting from capture to figures: the study is reproducible and auditable, which is rare in this literature.
- The embodied-specific principle extensions (physical safety, human-robot proximity, liability for physical damage, autonomy level and control, conformity assessment, dual use) are a genuine contribution and the salience contrast with general AI (Table 8) is convincing and well-tested (Holm correction, Wilson intervals, Fisher where needed).
- The instrument-only comparison of mechanisms (Table 10) is the right design choice, and the "product-safety toolkit versus accountability toolkit" characterisation is correct in substance even if the instrument counts need repair.
- Correct exclusion of software "robots" (RPA, robo-advisers, chatbots): no leakage into the embodied set.
- The recognition of composition effects (sprint versus database), the sensitivity table (Table 19), the explicit flagging of ISO landing pages and the AI Act duplicate, and the limitations section show good faith; the problems above are mostly about scale (the problems are larger than acknowledged), not concealment.
- Multilingual capture surfaced material that Anglophone reviews miss: the Arabic and Persian civil-liability literature, the Salvadoran robotics law, the Dubai statute, Taiwan's rule (even if misdated), the Shanghai and Beijing plans, Japanese robot-ethics journals.
- Lexicon validation on full text against excerpt-based annotation (Spearman 0.93 on principle rankings) is a sensible check and honestly reported where it fails (military vocabulary).
- The observation that the standards layer governs robots "largely out of sight of the policy and research literature" is correct and important, and survives the corrections to the standards evidence.
- The dashboard and the per-figure CSV twins make the corrections recommended here cheap to implement.

---

## 6. Recommended additions for policy usefulness

1. **An instrument-level inventory** (one row per instrument, many captures): jurisdiction, legal form, binds whom, adoption date, entry into force, date(s) of application, amendment history, repeal, robot categories covered, provisions extracted (obligations, prohibitions, definitions of autonomy level, safety mechanisms), authorities named. Start from the 63 + 55 documents and the section-4 list.
2. **A regime-coverage matrix** (23 robot categories × regimes: machinery/product safety; type approval; aviation; medical devices; OSH; consumer and toy safety; data protection; cybersecurity; liability; sectoral AI law; standards), with cell values "specific instrument / horizontal regime applies / gap". This replaces the research-minus-instrument gap index as the policy deliverable and will show that the real gaps are deception and attachment harms, not "social robots".
3. **A crosswalk to the EU AI Act**: for each robot category, whether it is reached via Annex I Section A (which harmonisation act), Annex I Section B (which sectoral act and whether the Commission has used Arts. 102-109), Annex III (which use case), Art. 5 or Art. 50; with the post-Omnibus application dates.
4. **Time-to-adoption and time-to-application metrics**: proposal → adoption → entry into force → application (AI Act 2021 → 2024 → 2024 → 2027/28; Machinery Regulation 2021 → 2023 → 2027; PLD 2022 → 2024 → 2026; UK AV Act: Law Commissions' report Jan 2022 → Act May 2024 → secondary legislation 2026-27; ISO 13482 revision 2021 PWI → FDIS 2025 → 2026); standards development lags; this is what the current Figure 6 is trying to be.
5. **A standards map with legal effect**: for each standard, whether it is harmonised (OJ citation), incorporated by reference in national law, or mandatory (GB), and which regulation it supports; this is the "operative layer" claim made checkable.
6. **A `binds` and `scope-of-application` field** so that executive orders, internal resolutions, court practice directions and municipal plans are not pooled with statutes in "binding" counts.
7. **A human legal audit** of all governance documents in the embodied set and all `legally_binding` documents, with reported human-model agreement on status, year and binding nature, and a rule that documents with `confidence < 0.5` or `page_quality != substantive_document` are excluded from instrument-level statistics until verified.
8. **Capture of full texts for the core standards** (under licence) or, failing that, explicit relabelling of catalogue pages as "scope statements" and removal of the operationalisation claims for standards.
9. **A change log and versioning** of the inventory (instruments are revoked, delayed and amended within the life of the study: EO 14110, the Digital Omnibus, ISO 13482, the AILD).
10. **Reframing of the five conclusions** so that each distinguishes "what the collection shows" from "what the regulatory landscape is"; conclusions 1, 2 and 5 currently do not survive the coverage audit as written, while 3 and 4 survive in modified form (3: "no robot-specific instrument; governance by horizontal law"; 4: "regions converge on principles and diverge on mechanisms *in the documents captured*").
11. **Dashboard filters** for instrument-level view, applicability date, binds-whom, and verified/unverified status, so that policymakers can see the five currently applicable binding embodied instruments at a glance rather than seven captures.
