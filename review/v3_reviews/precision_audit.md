# Precision audit of S01 "binding instruments reaching embodied AI" (v3)

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Independent re-reading of a random sample of the 299 documents in `tables/S01_binding_embodied.csv`, judged against five yes/no criteria from the documents' own texts. Date of audit: 2026-10-31. Auditor: independent (model-assisted) review for v4; no project file other than the two outputs in `review/v3_reviews/` was modified.

## 1. Sampling statement

Population: the 299 `doc_id`s in `/home/user/embodied-ai-governance-v3/tables/S01_binding_embodied.csv` (294 round-2 `R2-` ids, 5 round-1 `D` ids). Sampling frame: the doc_ids sorted alphabetically. Sample: simple random sample of 100 without replacement, drawn with `numpy.random.default_rng(2026).choice(sorted_ids, 100, replace=False)`. The drawn ids are listed in `precision_audit_sample.csv` (sorted). Re-running the draw reproduces the sample exactly (asserted in the build script).

For each sampled document the auditor read (i) the document's own text at the path given in `data/registry.csv` (`/home/user/collection-round-2/texts/<id>.txt` for R2 ids; the round-1 Markdown export for D ids), at least the first 6,000 characters plus the tail, (ii) keyword hit counts and context snippets for robot, autonomous/automated, self-driving, drone/UAS/unmanned/remotely piloted, AI, machine learning, algorithm, exoskeleton, humanoid, weapon, software, and for the ancillary-paperwork markers (commencement, exemption/permit/approval, EEA Joint Committee, corrigendum, bill/draft, guidance, levy/fee), with Japanese and Chinese equivalents (自動運転, 自動運行, 特定自動運行, 遠隔操作, 無人航空機, ロボット, 人工知能, 无人机, 自动驾驶, 机器人, 人工智能, 具身智能, 算法) for the 14 ja/zh texts, and (iii) the master-table row (title_en, jurisdiction_country, year_final, doc_class, instrument_status, summary_en, key_provisions_or_claims, embodied_categories, primary_embodied_category, relevance_to_embodied_ai_governance, page_quality, words, source_url). The master-table summary was used as a guide only; every judgment below was checked against the text.

### Criteria as applied

- **(a) distinct_instrument**: principal legal instrument or substantive amendment. Judged *no* for: commencement orders; individual or event-specific exemptions, approvals, directions, named-person instruments and device-specific classification orders; definitions-only sections; table-of-contents, index, catalogue, register or legislative-tracking pages with no operative text (the criterion lists "catalogue or status page", so a capture that consists only of such a page fails (a) even where the underlying instrument is principal); EEA Joint Committee incorporation decisions; language-version corrigenda; amendments that only move dates; Commission decisions that merely publish references of harmonised standards; a duplicate of a rule already in the population under another id. Amendments that change operative rules (e.g. new UAS classes, EU-Exit institutional substitutions) were judged *yes*, with the borderline noted.

- **(b) binding**: legally binding as captured. Executive orders, ministerial resolutions, CASA legislative instruments, civil-aviation directives/standards documents that the parent Act makes mandatory, DGT instructions setting authorisation conditions, and Chinese State Council decrees/regulations were judged binding. Chinese "measures", "plans" and "replies" that only allocate subsidies or policy tasks were judged *not* binding.

- **(c) embodied_substantive**: the text contains obligations, prohibitions, requirements or authorisations specific to robots, automated/autonomous vehicles, drones, delivery robots, surgical/medical robots, exoskeletons, humanoids or autonomous weapons. Judged *no* where embodied systems appear only as a mention, a list entry, an eligible-business category, a scope clause, or where the captured text has no provisions at all. ADAS-level automation rules (AEBS, platooning) were accepted; export-control lists in which UAVs/robots appear as controlled items were not.

- **(d) autonomy_or_ai_content**: any provision (including a definition or operating condition) about automation, autonomy, automated driving/flight, remote piloting, algorithms, machine learning or AI. A UAS statute that only says "operates an unmanned aircraft" with no definition of how it is controlled was judged *no*; one that defines the aircraft by absence of an onboard pilot, remote control link, visual line of sight or autonomous operation was judged *yes*.

- **(e) explicit_ai**: artificial intelligence, machine learning, AI systems or algorithms named explicitly in an AI/automation sense. Cryptographic "algorithms" (UN R155), generic software-modification "algorithms" (MDR), facial-recognition technology not named as AI, Malay/English false positives for "AI", and AI appearing only inside entity names (Entity List) were judged *no*.

- **(f) counting_unit_note**: whether the text belongs to a family present in S01 (yearly renewal, successive version, parent/implementing act, parts or amendments of one regime), with sibling ids found by title in S01.

## 2. Results: shares with 95% Wilson intervals (n = 100)

| Criterion | Yes | Share | 95% Wilson CI |
|---|---|---|---|
| (a) distinct_instrument | 67 | 0.67 | 0.57 to 0.75 |
| (b) binding | 97 | 0.97 | 0.92 to 0.99 |
| (c) embodied_substantive | 56 | 0.56 | 0.46 to 0.65 |
| (d) autonomy_or_ai_content | 67 | 0.67 | 0.57 to 0.75 |
| (e) explicit_ai | 14 | 0.14 | 0.09 to 0.22 |
| (a) and (b) jointly | 64 | 0.64 | 0.54 to 0.73 |
| **(a) and (b) and (c) jointly** | **54** | **0.54** | **0.44 to 0.63** |
| (a), (b), (c) and (d) jointly | 53 | 0.53 | 0.43 to 0.62 |

Among the 54 documents that pass (a), (b) and (c) jointly, 53 also pass (d) and 8 pass (e).

## 3. Implied precision-corrected count

The population of 299 documents, multiplied by the joint share of 0.54, implies **about 161 binding instruments with substantive embodied provisions** (95% Wilson interval of the share: 0.44 to 0.63, i.e. **132 to 190**). This is a precision correction only: it removes documents that are not distinct instruments, not binding or not embodied-substantive. It does not consolidate families (section 6), and it does not add instruments the collection missed (recall), so the two corrections pull in opposite directions and should be reported separately.

If instruments that only pass (a) and (b) are also required to contain automation or AI content (d), the count falls to about 158 (129 to 187). Explicit AI/ML/algorithm language is rare: 14 of 100 sampled documents, and only 8 of the 54 joint passes.

## 4. Breakdown by jurisdiction region (study_region) and by primary embodied category

Shares are the joint (a)(b)(c) share within the sampled documents of that group; "Pop." is the number of S01 documents in the group and "Implied" is Pop. x share. Groups with fewer than 10 sampled documents have very wide intervals and are indicative only.

### 4.1 By study region

| Region | Sampled | Joint pass | Share | 95% CI | Pop. in S01 | Implied count |
|---|---|---|---|---|---|---|
| Europe | 28 | 15 | 0.54 | 0.36 to 0.70 | 97 | 52.0 |
| North America | 26 | 16 | 0.62 | 0.43 to 0.78 | 79 | 48.6 |
| Asia | 18 | 14 | 0.78 | 0.55 to 0.91 | 41 | 31.9 |
| Oceania | 18 | 2 | 0.11 | 0.03 to 0.33 | 52 | 5.8 |
| Latin America & Caribbean | 5 | 3 | 0.60 | 0.23 to 0.88 | 14 | 8.4 |
| Africa | 3 | 3 | 1.00 | 0.44 to 1.00 | 5 | 5.0 |
| International | 1 | 0 | 0.00 | 0.00 to 0.79 | 6 | 0.0 |
| Middle East | 1 | 1 | 1.00 | 0.21 to 1.00 | 5 | 5.0 |

### 4.2 By primary embodied category

| Primary category | Sampled | Joint pass | Share | 95% CI | Pop. in S01 | Implied count |
|---|---|---|---|---|---|---|
| drones_uas | 51 | 30 | 0.59 | 0.45 to 0.71 | 162 | 95.3 |
| autonomous_road_vehicles | 30 | 19 | 0.63 | 0.46 to 0.78 | 93 | 58.9 |
| delivery_robots | 5 | 3 | 0.60 | 0.23 to 0.88 | 9 | 5.4 |
| none | 5 | 0 | 0.00 | 0.00 to 0.43 | 11 | 0.0 |
| industrial_manipulators | 2 | 1 | 0.50 | 0.09 to 0.91 | 9 | 4.5 |
| surgical_medical_robots | 2 | 0 | 0.00 | 0.00 to 0.66 | 2 | 0.0 |
| autonomous_maritime_or_rail | 1 | 1 | 1.00 | 0.21 to 1.00 | 1 | 1.0 |
| care_assistive_robots | 1 | 0 | 0.00 | 0.00 to 0.79 | 1 | 0.0 |
| humanoid_general_purpose | 1 | 0 | 0.00 | 0.00 to 0.79 | 1 | 0.0 |
| rehabilitation_exoskeleton_prosthetic | 1 | 0 | 0.00 | 0.00 to 0.79 | 2 | 0.0 |
| security_policing_robots | 1 | 0 | 0.00 | 0.00 to 0.79 | 1 | 0.0 |

Australia alone accounts for 15 of the 100 sampled documents and 15 of them fail (a) or (c): every Australian document in the sample was captured from legislation.gov.au as a register metadata page or table of contents with no operative text, and 12 of the 15 are individual CASA/ACMA approvals, directions, exemptions or naming instruments. The Oceania share is therefore driven by one collection artefact (the legislation.gov.au landing-page capture) and one counting-unit artefact (instrument series), not by the quality of Australian law; the three non-Australian Oceania documents (PNG Part 102, Fiji RPAS standards document, NZ Part 101 page) split 2 passes, 1 fail.

## 5. Failure types

46 of 100 sampled documents fail at least one of (a), (b), (c). Primary failure type (one per document; the tag in square brackets at the start of each `reason` in the CSV):

| Failure type | Sampled docs | Examples (doc_id: title) |
|---|---|---|
| Individual exemption/approval/direction instrument (also captured only as register page) | 14 | R2-1fa07634: CASA 326/12 - Approval of area of operation - unmanned aerial vehicles; R2-3a69a74f: CASA 28/26 — Operation of RPA in Sydney Harbour Restricted Areas, R407; R2-5108d498: Radiocommunications (Police Forces – Disruption of Unmanned Aircraft)  |
| Binding instrument with no embodied-specific provision (generic regime or marginal mention) | 10 | D0016: Resolution 710/2024 - Creation of the Unit of Artificial Intelligence ; D0915: Executive Order on the Safe, Secure, and Trustworthy Development and U; R2-3f3f9934: Commission Delegated Regulation (EU) 2026/1188 amending Annex II to Re |
| Register, catalogue, index or table-of-contents page without operative text | 9 | R2-0adddb0a: Vehicle Standard (Australian Design Rule 97/00 – Advanced Emergency Br; R2-35fea8b3: Part 101 Gyrogliders and Parasails, Unmanned Aircraft (including Ballo; R2-74a1e723: Automated Driving Ordinance (AutomatFahrV) – RIS Open Government Data  |
| Ancillary EU/UK act (standards-list decision, corrigendum, date postponement, EEA incorporation, commencement order) | 8 | R2-710c5344: Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 am; R2-77acbca3: Commission Implementing Decision (EU) 2024/2103 of 30 July 2024 on har; R2-9d7e136e: Commission Implementing Decision (EU) 2019/436 of 18 March 2019 on the |
| Non-binding policy or industrial-support document | 3 | R2-250c1f41: Several Measures of Beijing Economic-Technological Development Area to; R2-2f360ae8: State Council Reply on the Work Plan for Deepening the Construction of; R2-383a3bd2: State Council Notice on the Implementation Scope and Tasks of the Chin |
| Definitions-only section | 2 | R2-0f7421dd: Code of the District of Columbia § 50–2351. Definitions; R2-a846a9fc: Iowa Code §321.514 Definitions (automated driving systems) |

Observations:

1. **Capture failures masquerade as instruments.** 21 sampled documents have no operative text at all: legislation.gov.au register headers (CASA 326/12, 28/26, 86/20, 66/24, 96/17, 22/22, EX45/24, EX67/20, EX85/20, ADR 97/00, two ACMA exemption determinations, the DroneShield naming instrument, the 2019 RPA registration amendment TOC, and the whole of CASR 1998 captured as a 5,075-line table of contents), the NZ Part 101 consolidation page, the Austrian RIS open-data JSON listing, the govinfo page for Public Law 112-95, the Utah HB 217 tracking page, the West Virginia Code index, and the Dziennik Ustaw metadata page. Most are flagged `partial_or_excerpt` or `landing_or_index_page` in `page_quality`, so the table could have excluded them mechanically.

2. **The CASA/ACMA instrument family inflates Oceania.** 12 of the 100 sampled documents are Australian legislative instruments made under CASR 1998 or the Radiocommunications Act: area approvals, directions and their yearly renewals, BVLOS and populous-area exemptions, named-person instruments. In S01 as a whole there are 35 documents whose title begins with "CASA" or contains "Radiocommunications". Each is an individual or periodically renewed administrative act, not a distinct regulatory regime, and the parent regulation (CASR 1998 Part 101) is itself only captured as a table of contents.

3. **EU ancillary acts.** Harmonised-standards publication decisions (2019/436, 2024/2103, 2026/2015), the language corrigendum 2023/1675, the two date-postponing amendments of 2019/947 (2020/746, 2022/425), the EEA Joint Committee decision 103/2025 and the UK commencement regulations are binding but carry no rule of their own; by inspection of the S01 titles, the population contains 10 EEA JC decisions, 5 harmonised-standards decisions, 4 language corrigenda and 5 commencement orders or orders in council bringing acts into force.

4. **Generic regimes counted as embodied.** EO 14110, the Medical Devices Directive and Regulation, UN R155, two EAR parts (15 CFR 742, 744), the AEB test-device part, the NSSZ enforcement ordinance and Delegated Regulation 2026/1188 are binding instruments whose embodied content is a mention, a scope clause or a list entry. These are the documents the model rated relevance 1 to 2; a relevance threshold of 2 or more would have removed most but not all of them.

5. **Non-binding Chinese policy documents.** Three State Council / development-zone documents (subsidy measures for embodied-intelligence robots, an FTZ plan, a services-sector work-plan approval) were classed `regulation_or_decree` although they create no obligations.

6. **Definitions-only sections.** The DC Code and Iowa Code captures are definitions sections whose operative neighbours (permits, operation rules) are not in the population, so the regime is represented by its least substantive part.

## 6. Counting-unit observations from (f)

60 of the 100 sampled documents belong to a family that has at least one other member in S01. The main families found by title:

- Japan Road Traffic Act + Enforcement Order + Enforcement Regulations (3 ids); Road Vehicles Act + Safety Regulations + Enforcement Regulations + Type Designation ordinance + Inspection Standards (5); NSSZ Act + 4 ordinances/orders (5); freight-transport ordinances (3); Road Act + Enforcement Regulations (2).
- EU 2019/947 and its amendments 2020/639, 2020/746, 2021/1166, 2022/425 (+ GB retained copy) (6-7); 2019/945 and amendments 2020/1058, 2024/1108 (+ GB copy) (4); the 2024 certified-UAS package 2024/1107, 1108, 1109, 1110 (4); harmonised-standards decisions (4 under 2006/42/EC, one under 2019/945); EEA JC decisions (10); 2018/858 annex amendments and 2022/1426 + 2026/481 (4).
- UK Automated Vehicles Act 2024 + Commencement No. 1 and No. 3 + Marketing Restrictions Regulations (4); Automated and Electric Vehicles Act 2018 as predecessor; ATMUA Act 2021 + its commencement regulations (2).
- Australian CASA directions renewed yearly (96/17, 55/20, 86/20, 22/21, 22/22, 20/25), BVLOS exemptions renewed yearly (EX67/20, EX46/21, EX27/23, EX51/24, EX63/26), area approvals (57/22, 29/22, 64/23, 03/24, 66/24, 67/24, 28/26, 23/23, 17/26), ACMA radiocommunications exemptions (2018, 2019, 2020, 2022) and CASR 1998 with its Part 101 MOS and amendment regulations.
- US 14 CFR Parts 48, 89, 107 (one FAA small-UAS regime); 15 CFR Parts 742, 744, 772, 774 (one EAR); FAA reauthorisation acts 2012, 2018, 2024 and 18 USC 39B enacted by the 2018 act; Nevada NRS 482A + NAC 482A; 21 CFR 890 + the ReWalk de novo order it codifies.
- Vietnam Law on People's Air Defense + Decree 288/2025; Netherlands 2018 Act + permit regulation; Malaysia Civil Aviation Regulations 2016 + CAD 6011 Parts I, II, V; Iceland 2017 regulation replaced by the 2024 regulation; EU MDD 93/42 replaced by MDR 2017/745; Machinery Directive 2006/42 replaced by Regulation 2023/1230 and amended by 2026/1744.

## 7. Rules the study should adopt for the counting unit

1. **Count regimes, not documents.** The unit should be a principal instrument (act, regulation, decree, binding standard) together with its implementing, amending, correcting, commencing and incorporating acts. Report the number of regimes and, separately, the number of documents captured per regime.

2. **Exclude ancillary paperwork from the instrument count by rule, not by model judgment**: commencement orders, levy/fee acts, EEA Joint Committee decisions, language-version corrigenda, date-only amendments, harmonised-standards publication decisions, definitions-only or table-of-contents sections, legislative-tracking and catalogue pages. Keep them in the corpus as metadata of the parent regime.

3. **Exclude individual administrative acts** (exemptions, approvals, directions, permits, named-person instruments, device-specific classification orders, company authorisations) unless they are the only way a jurisdiction regulates the activity; where kept, count a yearly-renewed series once and record the series length as an attribute.

4. **Require operative text.** A document whose capture is a register header, landing page, index or TOC (page_quality `partial_or_excerpt`, `landing_or_index_page`, or text under roughly 2,000 characters with no article/section text) must not enter the instrument count until the full text has been fetched; it should be listed as "instrument identified, text not captured".

5. **Require an embodied-specific operative provision** (relevance 2 or more *and* at least one obligation, prohibition, requirement or authorisation naming the embodied system), not a mention in a recital, scope clause, list entry or eligible-business category. Generic product-safety, cybersecurity, medical-device and export-control regimes belong in S05 (general instruments with embodied provisions) only when such a provision exists.

6. **Separate binding from policy for Chinese and similar administrative documents**: State Council decrees, regulations (条例) and ministerial rules (规定/办法 with sanctions or licensing conditions) are binding; "measures" that only allocate subsidies, "plans", "replies" and "notices issuing plans" are policy and belong in S02.

7. **De-duplicate across ids** when the same rule appears as a de novo order and its codified CFR section, as an EU regulation and its retained GB copy, or as successive versions of one regulation; keep the current version as the counting unit and record predecessors as history.

8. **Report precision-corrected counts with the sampling interval**, and keep the recall audit (missing instruments) separate so that the two corrections are not netted against each other.

## 8. Files

- `review/v3_reviews/precision_audit_sample.csv`: the 100 sampled ids with title, jurisdiction, year, the five judgments (Y/N), the counting-unit note (f) and a one-line reason (failure-type tag in square brackets where the document fails a, b or c).
- `review/v3_reviews/precision_audit.md`: this report.
