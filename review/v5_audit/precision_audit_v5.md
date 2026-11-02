# Precision audit of the v4 "principal binding instruments in the embodied-AI set" (v5 audit)

Independent re-reading of a random sample of 100 of the 195 documents that the study counts as principal binding instruments in the embodied set, judged against five yes/no criteria from the documents' own texts. Date of audit: 2026-11-02. Auditor: independent (model-assisted) review; no project file other than `review/v5_audit/precision_audit_v5_results.csv` and this report was modified. The study's own labels were not consulted beyond the four rule-based columns carried in the sample file (`ai_explicit`, `autonomy_terms`, `relevance_to_embodied_ai_governance`, `instrument_unit`), which were recorded but not used in forming the judgments.

## 1. Sampling statement

From `review/v5_audit/SAMPLING.txt`:

> Population: the 195 principal binding instruments in the embodied set (analysis_common.load: embodied_set & binding), v4 master table of 2026-11-02.
> Sample: numpy.random.default_rng(2027).choice(sorted_ids, 100, replace=False).

The 100 sampled ids, with title, jurisdiction, year and the study's rule-based flags, are in `precision_audit_v5_sample.csv` (97 round-2 `R2-` ids and 3 round-1 `D` ids). By jurisdiction the sample holds 27 US, 19 EU, 10 JP, 7 GB, 5 CA, 3 AU, 3 INT, 2 each for CN, DK, ES, IS, TZ, and one each for AR, DE, EC, FJ, FR, GH, MX, NG, NL, NZ, OM, RW, SE, SV, TT, VN.

## 2. Methods

For each sampled document the auditor read the text at its `text_path` (the round-2 plain-text capture or the round-1 Markdown export): at least the first 6,000 characters and the last 2,000, plus keyword hit counts and context snippets for robot, autonomous/automated, self-driving, drone, UAS/UA, unmanned, remotely piloted/remote pilot, artificial intelligence, machine learning, algorithm, exoskeleton, humanoid, weapon and software, and for the ancillary-paperwork markers (commencement, exemption/approval/permit, guidance/voluntary), with the Chinese (机器人, 自动驾驶, 无人机, 无人驾驶航空器, 人工智能, 算法), Japanese (ロボット, 自動運転, 自動運行, 特定自動運行, 遠隔操作, 無人航空機, 人工知能), Korean, French, German, Spanish, Dutch, Danish, Swedish and Icelandic equivalents where the text required them. Where the keyword snippets did not settle a judgment, the operative articles were read in full (for example the Digital Omnibus's amending articles, the Japanese e-Gov JSON captures' article text, the Conseil constitutionnel's reasoning on police drones). Every judgment is recorded in `precision_audit_v5_results.csv` with a one- or two-sentence reason citing what was seen, with a short quote where decisive, and a failure-type tag in square brackets at the start of the reason where the document fails (a), (b) or (c).

The criteria were applied exactly as in the v3 audit (`review/v3_reviews/precision_audit.md`, "Criteria as applied"):

- **(a) distinct_instrument**: a principal legal instrument or substantive amendment. Judged no for commencement orders, individual or device-specific orders and approvals, definitions-only sections, table-of-contents, index, catalogue, register, landing and legislative-tracking pages with no operative text (even where the underlying instrument is principal), harmonised-standards publication decisions, date-only amendments, and a duplicate of a rule already in the population under another id (which, following the v3 rule, includes the UK retained copies of EU regulations). EU-Exit institutional substitutions and amendments that change operative rules were judged yes, with the borderline noted.
- **(b) binding**: legally binding as captured. Executive orders, ministerial resolutions and decisions, civil-aviation directives and standards documents that the parent Act makes mandatory, DGT instructions setting authorisation conditions, Chinese State Council regulations and a Conseil constitutionnel decision (binding under Art. 62 of the Constitution) were judged binding; Chinese provincial "policy measures" that only allocate subsidies were judged not binding. Instruments since repealed (RD 1036/2017, Iceland 990/2017, EO 14110) were judged binding as captured.
- **(c) embodied_substantive**: an obligation, prohibition, requirement or authorisation specific to robots, automated or autonomous vehicles, drones, delivery robots, surgical or medical robots, exoskeletons, humanoids or autonomous weapons; no where the embodied system is only a mention, list entry, scope clause, eligible-business category or where the capture has no provisions at all. ADAS-level automation rules (ISA, ACSF in UN R79) were accepted, as the v3 audit accepted AEBS and platooning.
- **(d) autonomy_or_ai_content**: any provision, including a definition or operating condition, about automation, autonomy, automated driving or flight, remote piloting, algorithms, machine learning or AI. A UAS statute that only says "operates an unmanned aircraft" with no definition of how the aircraft is controlled was judged no; one that defines the aircraft by absence of an onboard pilot, a control link, visual line of sight or autonomous operation was judged yes.
- **(e) explicit_ai**: artificial intelligence, machine learning, AI systems or algorithms named explicitly in an AI or automation sense. Cryptographic algorithms (UN R155), generic software-modification algorithms and the "Application Identifier" abbreviation (MDR), and facial-recognition technology not named as AI were judged no; "algoritmos de conducción autónoma" (DGT instruction) and a single promotional mention of 人工智能 (Chinese UAS regulations) were judged yes.
- **(f) family_note**: whether the text belongs to a family of related captures (parent and implementing act, successive version, amendment series, retained copy), with sibling titles where noticed.

Wilson 95% intervals were computed in Python (`z = 1.96`), with n = 100 throughout.

## 3. Results

| Criterion | Yes | Share | 95% Wilson CI |
|---|---|---|---|
| (a) distinct_instrument | 85 | 0.85 | 0.77 to 0.91 |
| (b) binding | 99 | 0.99 | 0.95 to 1.00 |
| (c) embodied_substantive | 76 | 0.76 | 0.67 to 0.83 |
| (d) autonomy_or_ai_content | 73 | 0.73 | 0.64 to 0.81 |
| (e) explicit_ai | 9 | 0.09 | 0.05 to 0.16 |
| (a) and (b) jointly | 84 | 0.84 | 0.76 to 0.90 |
| **(a), (b) and (c) jointly** | **73** | **0.73** | **0.64 to 0.81** |
| (a), (b), (c) and (d) jointly | 64 | 0.64 | 0.54 to 0.73 |

Among the 73 documents that pass (a), (b) and (c) jointly, 64 also pass (d) and 6 pass (e) (D0005 El Salvador robotics law, Regulation (EU) 2023/1230 on machinery, the ISA Delegated Regulation 2021/1958, the Chinese Interim Regulations on unmanned aircraft flights, DGT Instruction VEH 2022/07, Oman CAA Decision 1412/2023). The three other explicit-AI documents (EO 14110, Argentina Resolution 710/2024, the Digital Omnibus on AI) are AI instruments without an embodied-specific provision.

### 3.1 Implied precision-corrected count

The population of 195 multiplied by the joint share of 0.73 implies **about 142 binding instruments with substantive embodied provisions** (95% Wilson interval of the share 0.64 to 0.81, i.e. **124 to 157**). If automation or AI content (d) is also required, the count falls to about 125 (106 to 142). As in v3, this is a precision correction only: it removes documents that are not distinct instruments, not binding or not embodied-substantive. It does not consolidate families (section 6) and it does not add instruments the collection missed, so the recall correction should be reported separately.

Sensitivity to the borderline calls: counting the two UK retained copies of 2019/945 and 2019/947 as distinct instruments (they are distinct in GB law, but the v3 rule treats a retained copy as a duplicate) gives 75 of 100 (0.66 to 0.83; implied 146, 128 to 161). Treating the three borderline (a) acceptances as ancillary (the EU-Exit substitution regulations, B.C. Reg. 63/2024, which is a commencement order that also sets the automated-vehicle fines, and the Conseil constitutionnel decision, which is a judicial act) gives 70 of 100 (0.60 to 0.78; implied 137, 118 to 152). The joint share therefore lies between 0.70 and 0.75 under any reasonable reading of the borderline cases.

### 3.2 Comparison with the v3 audit (n = 100 of 299)

| Criterion | v3 share (S01, 299 docs) | v5 share (195 docs) | Change |
|---|---|---|---|
| (a) distinct_instrument | 0.67 | 0.85 | +0.18 |
| (b) binding | 0.97 | 0.99 | +0.02 |
| (c) embodied_substantive | 0.56 | 0.76 | +0.20 |
| (d) autonomy_or_ai_content | 0.67 | 0.73 | +0.06 |
| (e) explicit_ai | 0.14 | 0.09 | -0.05 |
| (a), (b), (c) jointly | 0.54 (0.44 to 0.63) | 0.73 (0.64 to 0.81) | +0.19 |

The joint share rose by 19 points; a two-proportion test gives z = 2.79 (p = 0.005), and the two intervals barely overlap, so the improvement is not sampling noise. In absolute terms the v3 population of 299 implied about 161 true instruments (132 to 190) and the v4 population of 195 implies about 142 (124 to 157): the v4 trimming removed 104 documents, of which the audit evidence suggests roughly four-fifths were ancillary or non-embodied and roughly one-fifth were genuine instruments (the implied count fell by about 19). The categories that drove the v3 failures have largely gone: no CASA or ACMA individual approval, direction or exemption, no EEA Joint Committee decision, no corrigendum and no Chinese State Council policy plan was drawn in this sample. What remains are (i) generic regimes in which the embodied content is a scope clause or mention (11 of 100), (ii) capture artefacts, that is register, table-of-contents, landing, catalogue and bill-tracking pages with no operative text (7), (iii) EU ancillary acts (two harmonised-standards decisions, two date-only amendments), (iv) the two UK retained copies, a definitions-only section, a device-specific FDA order and one subsidy policy. The fall in explicit AI (0.14 to 0.09) is consistent with the trimming having removed AI-policy documents (EO-type instruments, export-control lists) that mention embodied systems only in passing.

## 4. Agreement with the study's own flags

Every sampled document carries `instrument_unit` = principal or amendment and is counted as binding by the study, so the comparison is with the study's proxies: `relevance_to_embodied_ai_governance >= 2` for (c) and the joint (a)(b)(c) judgment, `autonomy_terms` for (d), and `ai_explicit` for (e).

| Comparison | audit Y / flag Y | audit Y / flag N | audit N / flag Y | audit N / flag N | Agreement | Cohen's kappa |
|---|---|---|---|---|---|---|
| joint (a)(b)(c) vs relevance >= 2 | 68 | 5 | 21 | 6 | 0.74 | 0.19 |
| (c) alone vs relevance >= 2 | 71 | 5 | 18 | 6 | 0.77 | (not computed) |
| joint (a)(b)(c) vs relevance >= 3 | 28 | 45 | 3 | 24 | 0.52 | (not computed) |
| (d) vs autonomy_terms | 56 | 17 | 17 | 10 | 0.66 | 0.14 |
| (e) vs ai_explicit | 7 | 2 | 2 | 89 | 0.96 | 0.76 |

Observations:

1. **The relevance >= 2 threshold is permissive.** 89 of the 100 sampled documents are rated 2 or more by the study, but 21 of those fail the audit. The relevance score cannot see the capture problems (it rates CASR 1998, the Part 101 MOS, the NZ Part 101 page, the Nigeria catalogue entry and the two US bill-tracking pages at 2 or 3) and it rates several generic or ancillary documents at 2 (the two harmonised-standards decisions, the two date-only amendments, UN R155 and R156, the Digital Omnibus, the Hunan subsidy measures, the ReWalk order, the NSSZ demonstration-project ordinance). Conversely, the five documents the audit passes but the study rates 1 are real but low-density captures: the Mexican Civil Aviation Law (RPAS registration and fines inside a general aviation code), the BC OHS Part 12 (one industrial-robot section), the Delaware criminal-code subchapter (one UAS section), and two Japanese MLIT ordinances whose automated-transport provisions are procedural. A threshold of 3 is too strict (it would drop 45 true passes). The relevance score is therefore not a usable proxy for (c) on its own; the mechanical exclusions in section 7 of the v3 report are needed first.

2. **`autonomy_terms` is only weakly related to (d).** It misses 17 documents that the audit judges to contain autonomy or remote-piloting provisions: 13 in languages other than English (five Japanese texts using 特定自動運行 and 自動運行装置, and one each in German, Dutch, French, Swedish, Icelandic (two) and Danish (two)), three US personal-delivery-device statutes that use "with or without the active control or monitoring of a natural person" rather than an autonomy keyword, and Florida's F.S. 934.50, whose drone definition reads "Can fly autonomously or be piloted remotely". It fires on 17 documents where the term occurs only in a title, heading, table-of-contents line or catalogue summary (CASR 1998, Part 101 MOS, the NZ page, the Nigeria page, the Kentucky bill page, the two standards decisions, the 2020/746 date amendment), where "unmanned" appears without any provision on how the aircraft is controlled (18 U.S.C. 39B, 49 U.S.C. 44810, the Tanzanian 2023 amendment, the UK minimum-age regulations, Va. Code 18.2-121.3, N.C. 14-401.24), or where the term is incidental in a generic text (the MDR, the NSSZ enforcement ordinance, the Hunan subsidy measures). The flag should be re-run with the multilingual term list used here and restricted to the operative text.

3. **`ai_explicit` agrees well with (e)** (kappa 0.76). Its four disagreements are the two false positives the v3 audit already identified (cryptographic "algorithms" in UN R155; "algorithms" and "AI" as Application Identifier in the MDR) and two misses, the DGT instruction's "algoritmos de conducción autónoma" and the Chinese 人工智能 in the Interim Regulations.

## 5. Documents that fail, grouped by failure type

27 of 100 sampled documents fail at least one of (a), (b), (c). The primary failure type is the tag at the start of each `reason` in the CSV.

### 5.1 Binding instrument with no embodied-specific provision (11; fail (c) only)

| doc_id | Document | Reason |
|---|---|---|
| D0016 | Argentina, Resolution 710/2024 creating the UIAAS | Creates a unit; drones and robots appear only as listed functions ("Patrullar mediante drones", "desactivación de explosivos, mediante robots"); no requirement specific to them. |
| D0915 | US, EO 14110 on safe, secure and trustworthy AI | Agency-wide AI order; embodied content is one phrase on "autonomous mobility ecosystems". Revoked Jan. 2025. |
| R2-833ba7e9 | EU, Medical Devices Directive 93/42/EEC | Generic device regime; no robot or automation provision. |
| R2-87faf76a | EU, Medical Devices Regulation 2017/745 | Generic device regime; "algorithms" only as software modifications, "AI" only as Application Identifier. |
| R2-34d7721c | EU, Regulation 2019/543 updating UN Regulation references | List-update amendment; AEBS and LDWS appear only as table entries. Borderline on (a) as well. |
| R2-0c29bfda | EU, Regulation 2026/1744 (Digital Omnibus on AI) | Amends the AI Act, 2018/1139 and 2023/1230, but only to require that AI-Act requirements "be taken into account" in future implementing and delegated acts on AI safety components; no robot, vehicle or drone rule (the UAS articles 57-58 of 2018/1139 are untouched). |
| R2-03e6e0ff | JP, Cabinet Office Ordinance under NSSZ Act Art 25-2 | Three-article ordinance designating which demonstration projects (automated driving, UAS remote or automatic piloting) qualify for radio-law special provisions; an eligibility designation, not a requirement on the vehicles. |
| R2-59a29a12 | JP, Ordinance for Enforcement of the NSSZ Act | Robots appear only as eligible business categories (medical and care robots R&D); no automated-driving or UAS provision. |
| R2-7c6034a5 | INT, UN Regulation No 155 (cybersecurity) | Automated driving appears only in the scope extension to L6/L7 vehicles with level-3 functions. |
| R2-77e55f86 | INT, UN Regulation No 156 (software updates) | Generic process requirements; nothing on automation, robots or drones. |
| R2-f5e63b92 | US (MN), Executive Order 18-04 | Establishes an advisory council to study connected and automated vehicles; no requirement, prohibition or authorisation on the vehicles. |

### 5.2 Register, table-of-contents, landing, catalogue or legislative-tracking page without operative text (7; fail (a) and (c))

| doc_id | Document | Reason |
|---|---|---|
| R2-c5eb5314 | AU, Civil Aviation Safety Regulations 1998 | legislation.gov.au register header and table of contents only (headings such as "101.097 Autonomous aircraft—launch or release without approval prohibited"). |
| R2-873de2ab | AU, Part 101 Manual of Standards 2019 | Table of contents only. |
| R2-295bf91b | AU, Air Navigation (Aircraft Noise) Regulations 2018 | Table of contents only; even the headings show a noise regime with one RPA approval heading. |
| R2-35fea8b3 | NZ, Civil Aviation Rules Part 101 | CAA NZ landing page listing subparts and amendment history. |
| R2-b72982f8 | NG, Nig.CARs 2023 Part 21 RPAS | NCAA catalogue entry: one-paragraph summary and related-items list. |
| R2-ed0d2da3 | US (KY), House Bill 7 of 2024 | Legislature bill page with actions and a summary of the enacted version; no enacted text. |
| R2-ac001dfe | US (UT), H.B. 217 Personal Delivery Devices | Legislature bill-status page; no statutory text. |

### 5.3 Ancillary EU act (4; fail (a) and (c))

| doc_id | Document | Reason |
|---|---|---|
| R2-77acbca3 | EU, Implementing Decision 2024/2103 | Publishes the reference of EN 4709-002:2023 (direct remote ID) "with restriction"; no rule of its own. |
| R2-885d8000 | EU, Implementing Decision 2024/1329 | Amends the list of harmonised machinery standards; "driverless industrial trucks" only as a standard's title. |
| R2-ada72e0e | EU, Implementing Regulation 2020/746 | Replaces dates in 2019/947 only (COVID postponement). |
| R2-3e221bc0 | EU, Implementing Regulation 2021/1166 | Postpones the date of application of the standard scenarios only. |

### 5.4 Duplicate of a rule already in the population (2; fail (a) only)

| doc_id | Document | Reason |
|---|---|---|
| R2-e8e3e681 | GB, retained Implementing Regulation 2019/947 | Same operative rules as the EU version (R2-ddd7d9c2, also in the sample) with CAA substituted; judged a duplicate under the v3 rule although it is a distinct instrument in GB law. |
| R2-08a1ad4b | GB, retained Delegated Regulation 2019/945 | Same rules as R2-6c14c9c2 (also in the sample); as above. |

### 5.5 Other (3)

| doc_id | Document | Fails | Reason |
|---|---|---|---|
| R2-2344fe88 | CN, Hunan "Several Policy Measures" for the low-altitude economy | (b), (c) | Provincial subsidy and reward measures (per-flight-hour subsidies, rewards for drone logistics routes); creates no obligation or licensing condition. |
| R2-9afd6f5a | US, FDA De Novo order for the ReWalk exoskeleton (K131798) | (a) | Device-specific classification letter to one manufacturer; the special controls it sets are exoskeleton-specific, so (c) is Y, but it is an individual administrative order codified at 21 CFR 890.3480. |
| R2-785c9ea7 | US (NC), G.S. 20-400 Definitions | (a), (c) | Definitions-only section; the operating rules in 20-401 are not captured. |

### 5.6 Borderline passes worth a second look

These pass under the v3 criteria but a stricter reading could reverse them: R2-2abf00a7 (UK EU-Exit substitution regulations, accepted as substantive as in v3); R2-4a23d4bc (B.C. Reg. 63/2024, a commencement order that also inserts the automated-vehicle offence fines); R2-fcdcfae6 (Conseil constitutionnel decision 2021-834 DC, a judicial act with binding effect on the police-drone provisions); R2-eac3219d (a single section, § 21a LuftVO, captured alone but with operative text); R2-f47247d3 and R2-ce2171ab (Japanese MLIT ordinances whose automated-transport content is an application-document requirement); R2-31fedef2 (a whole Delaware criminal-code subchapter in which one section concerns UAS); R2-b6c5f44e and R2-a586cca8 (ISA and ACSF, ADAS-level automation accepted as in v3).

## 6. Counting-unit observations from (f)

89 of the 100 sampled documents belong to a family with at least one other member noticed by title (parent and implementing act, amendment series, successive version or retained copy); only 11 stand alone (mostly single US state statutes). Families with several members inside this sample alone: Implementing Regulation 2019/947 with its three amendments 2020/639, 2020/746, 2021/1166 and its GB retained copy (5 of 100); Delegated Regulation 2019/945 with 2024/1108, the standards decision 2024/2103 and its GB copy (4); the 2024 certified-UAS package 2024/1108 and 2024/1109 (2); the U-space pair 2021/664 and 2021/665 (2); the machinery trio 2023/1230, the standards decision 2024/1329 and the Digital Omnibus 2026/1744 (3); MDD 93/42 and MDR 2017/745 (2); CASR 1998 and its Part 101 MOS (2); the Japanese Road Traffic Act and its Enforcement Order (2) and the three NSSZ ordinances (3); the UK Automated Vehicles Act 2024 and the C&U (Automated Vehicles) Order 2022 (2); the EU-Exit regulations and the two retained copies (3); the Icelandic 990/2017 and its successor 1360/2024 (2); the two Tanzanian RPAS amendments of 2020 and 2023 (2); UN R155 and R156 (2); N.C. 15A-300.1 and 14-401.24 (2); 49 U.S.C. 44810 and 14 CFR Part 124 (2). Counting regimes rather than documents would therefore reduce the 73 joint passes in this sample to roughly 55 to 60 regimes, and the v3 recommendation to report regimes and documents-per-regime separately still applies.

Two further counting-unit issues appear in this sample: (i) three repealed instruments are counted alongside their successors (RD 1036/2017, Iceland 990/2017, EO 14110), so the population mixes current and historical versions; (ii) two captures are whole codes or subchapters in which the embodied content is a single section (Delaware Title 11 Subchapter VII; the Mexican Civil Aviation Law), while elsewhere the same kind of content is captured as a single section (Va. Code 18.2-121.3), so the document unit is not comparable across jurisdictions.

## 7. Files

- `review/v5_audit/precision_audit_v5_results.csv`: the 100 sampled documents with doc_id, title, jurisdiction, year, the five judgments (Y/N), the family note (f) and the reason (failure-type tag in square brackets where the document fails (a), (b) or (c)).
- `review/v5_audit/precision_audit_v5.md`: this report.
