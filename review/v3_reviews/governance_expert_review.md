# Adversarial governance-law review of version 3: are the instruments and their classifications right?

Reviewer role: AI and robotics governance expert (law and policy of automated vehicles, drones, industrial and service robots, medical devices, autonomous weapons; technical standards and their legal effect across jurisdictions).
Scope: `report/brief.md`, `report/paper.md` (results, discussion, limitations), `report/collection_round2.md` (including T59 and T60), `report/methods_document_discovery.md`, tables S01, S02, S03, S05, T04, T25, T52, `data/reference_instruments.csv`, `data/round2_inventory.csv`, `collection_round2/COLLECTOR_REPORTS.md`, and `data/master_table.csv` for every document named below (fields read: title, jurisdiction, year, class, status, binding nature, relevance, categories, page quality, word count, confidence, summary, key provisions, source URL). Context: the v1 governance review and `review/adversarial_review_and_changes.md`.
Method: (a) a risk-stratified audit of 159 instruments drawn from S01/T59 (106), S02/T60 (34) and S03 (19), stratified by region (EU, European states, US federal and state, Australia and New Zealand, Japan, China, Korea and Taiwan, Latin America, Africa, Middle East, international) and robot type (drones, vehicles, industrial and collaborative arms, delivery, medical and rehabilitation, humanoid and embodied-AI policy, weapons, service and companion); (b) structural checks run over the whole of S01, S02 and S03 (word counts, page quality, title patterns, status and year fields); (c) a check of the round-2 inventory for important candidates that were found but not read. No project file was modified. Where I rely on legal facts outside the collection I say so and mark anything I could not verify from the collection "verify".

---

## 1. Verdict

Version 3 fixed the specific v1 errors that were named (the AI Act duplicates, the revoked executive order, the Taiwan stub, the catalogue pages, the bills coded binding) and then re-created every one of them at twenty times the scale through round 2, because the same failure modes were not turned into rules before 1,637 new documents were admitted. The headline "299 legally binding instruments reach robots" is not a count of instruments: by my structural checks 168 of the 299 (56%) fall into at least one of five buckets that a lawyer would not count as a distinct binding robot rule (71 are metadata stubs under 300 words, 56 of which say in their own summary that only a register entry or table of contents was read; 79 are amendments, corrigenda, EEA incorporation decisions, commencement orders, levy acts, exemptions, directions and area approvals; 21 are index pages, single definition sections or excerpts; 55 are general transport, fiscal, export-control or procurement law rated relevance 0 or 1; 24 are AEB type-approval, export lists and the like), and 46 of the 48 Australian "binding instruments" that make Oceania a "distinct" region are ~100-word register entries for CASA exemptions and approvals. Of the 159 instruments I audited individually, 108 (68%) carry at least one classification error and 98 (62%) a material one (wrong class, wrong status, not an instrument, duplicate of an instrument already counted, or not about embodied AI); the sample was chosen to find problems, so this is an upper bound for the whole set, but the population-level 56% figure is not. Three errors reach the brief's first paragraph: the only "binding" humanoid instrument is a 34-word stub of a Beijing development-zone subsidy notice; the Machinery Regulation (in force since July 2023) is "adopted, not yet in force" while the Machinery Directive that actually governs robots until 20 January 2027 is "repealed"; and the "127 general-AI instruments with robot provisions" are mostly Japanese road and freight law, US export-control and procurement regulations and an Australian drone levy, not AI law. On the other side of the ledger: the direction of the central finding (binding law reaches robots through aviation, road-traffic, machinery, workplace-safety and medical-device law, not through robotics statutes) is correct and would survive a clean inventory, the discourse analyses are unaffected, and the round-2 inventory already contains the raw material (the Hangzhou embodied-robot regulation, the Shenzhen ICV and AI regulations, Hong Kong's AV regulation, DoD Directive 3000.09, the Toy Safety Regulation, the revised PLD, California SB 243) that would fix most coverage gaps if the hosts were read through a browser. Recommendation: major revision before policy use; the paper should not state any instrument count until an instrument-level inventory (one row per instrument, with capture tier, binds-whom, legal form, lifecycle and applicability dates) replaces the document-level count.

---

## 2. Did the v2 fixes hold?

| v2 fix (from `adversarial_review_and_changes.md`) | Held for the round-1 documents? | Re-created by round 2? |
|---|---|---|
| D1 duplicates of the AI Act, its proposal, the Civil Law Rules | Yes (D1010, D1022, D1023 excluded; D1103, D1290, D1142 superseded) | Yes: the EP's June 2023 AI Act amendments are captured again as R2-e91f8719 and coded "under consideration"; the Digital Omnibus exists as proposal (R2-e09b2ee1, "under consideration"), EP amendments (R2-b497d818, "under consideration") and adopted act (R2-0c29bfda); 2019/945 and 2019/947 each appear as EU act, UK retained copy, three or four amending acts, two corrigenda and five EEA Joint Committee decisions |
| D2 EO 14110 revoked | Yes (D0915 superseded) | Not applicable |
| D3 Taiwan login stub excluded | Yes (D0480 out of S01) | Yes, at scale: 71 binding instruments under 300 words; five Chinese "binding" rules of 30 to 49 words; 45 Australian register entries of 88 to 167 words; all counted |
| D4 catalogue and committee pages reclassified | Yes for D0045, D0218 | Yes: R2-2dc27108 (ISO/TC 299 catalogue via LVS) is again a "technical standard" with relevance 3; seven Chinese standards-portal pages whose titles say "(page)" are standards; 179 of 241 embodied standards are landing pages |
| D6 bills cannot be binding; drafts enacted since capture | Yes for the listed bills | Yes: Machinery Regulation proposal (R2-f48a8103), Digital Europe amendments (R2-c5f8f802), Euro 7 proposal (R2-960229c7), India Draft Drone Rules (R2-99a032c7), Tennessee 2013 bill (R2-95cb0662) all enacted and still "under consideration" or "consultation open"; AV START Act and S.1394 lapsed with their Congresses |
| F9 "in force" is not "applicable" | Not done (acknowledged in Limitations) | The field now carries 268 "in force" and 7 "adopted" with the Machinery Regulation on the wrong side and the Directive "repealed" |
| F11 Argentina Res. 710/2024 is an internal organisational act | Not done: D0016 is still a binding "security_policing_robots" instrument in S01 | Round 2 adds two gubernatorial executive orders creating councils and a Uruguayan authorisation of one company, all "legally binding regulations" |
| F22 standards' legal effect (harmonised, mandated) | Not done; `technical_standard_mandated` is now used for 11 documents but they are counted as soft law | GB 11291.1/.2, GB 42590-2023, GB 44495/44496 (mandatory national standards) are "soft-law instruments" |
| Reference list year for Taiwan | Not done: `reference_instruments.csv` still says 2025 | |

---

## 3. Classification audit

### 3.1 Sample and headline numbers

159 instruments inspected (106 from S01/T59, 34 from S02/T60, 19 from S03/T60). Judgements use the recorded summary and key provisions, the capture metadata (page quality, word count, URL) and my knowledge of the instruments. Error types: **A** duplicate or dependent act (amendment, corrigendum, commencement order, EEA incorporation, retained copy, national adoption, successive version) counted as a separate instrument while the base act is present or should be; **B** not an instrument (landing, catalogue or register page, metadata stub, table of contents, single definitions section, announcement, web form); **C** wrong binding class or doc class (mandatory standard as soft; statute as guideline; subsidy notice or executive act creating a body as binding regulation; working paper or position paper as draft instrument; private association agenda as national strategy); **D** wrong lifecycle status (enacted proposal still a draft; lapsed bill under consideration; in-force act "adopted not yet in force" or "repealed"; stale consultation); **E** wrong or missing year (consolidation date instead of enactment; blank); **F** wrong jurisdiction or issuer; **G** not genuinely about embodied-AI governance (incidental mention, relevance 0 or 1, AEB or EMC rule labelled "autonomous vehicle"). "OK" means I would keep the row as it stands; "OK*" means keep with the stated caveat.

Result: 108 of 159 (68%) have at least one error; 98 (62%) have a material error (A, B, C, D or G). By stratum: S01 66 of 106 (62%; 59 material), S02 25 of 34 (74%; 23 material), S03 17 of 19 (89%; 16 material). The sample was risk-stratified, not random, so these are upper bounds for the whole tables; the population-level checks in 3.3 are not.

### 3.2 Audit table

**S01 / T59: binding instruments in the embodied set**

| doc_id | title (abridged) | judgement | error | fix |
|---|---|---|---|---|
| R2-6e60e906 | Convention on Road Traffic (Vienna 1968), UN Treaty Collection status page | A 286-word depositary status page counted as the collection's one "treaty"; the Convention and its automated-driving amendments (Art. 8(5bis) 2016; Art. 34bis 2022, verify) are the instrument | B | capture the consolidated Convention text; record the amendments as the robot-relevant events |
| R2-74a1e723 | AutomatFahrV (AT), RIS open-data search listing | Landing page of metadata (487 words, "operative text not shown"); the ordinance BGBl. II 402/2016 is real | B | fetch the consolidated text from RIS |
| R2-a6b6bddb | EEA JC Decision 142/2023 | Incorporates a language corrigendum (2022/525) into the EEA Agreement; not a robot rule; jurisdiction is EEA/EFTA, not EU | A, F | fold all 10 EEA JC decisions into an "extension to EEA" attribute of the base act |
| R2-b8211d02 | EEA JC Decision 116/2023 | Incorporates U-space regs already captured | A, F | as above |
| R2-9bf493ed | EEA JC Decision 12/2024 | Incorporates 2022/1426 (captured) | A, F | as above |
| R2-1d8b5ad8 | EEA JC Decision 164/2026 | Incorporates 2026/481 (captured) | A, F | as above |
| R2-46c15ddb | Reg. 2022/525 correcting language versions of 2019/947 | Corrigendum; summary says "no substantive change"; methods say corrigenda were excluded | A | drop or attach to 2019/947 |
| R2-942fad57 | Reg. 2022/851 correcting Portuguese version of 2019/945 | Corrigendum | A | drop or attach |
| R2-08a1ad4b | Reg. 2019/945, UK retained version | A distinct UK instrument (retained, amended 2025); acceptable, but it doubles the EU text in cross-jurisdiction counts | OK* | flag as retained-EU copy |
| R2-e8e3e681 | Reg. 2019/947, UK retained version | As above | OK* | flag |
| R2-6c14c9c2 | Reg. 2019/945 (EU) | Correct | OK | |
| R2-ddd7d9c2 | Reg. 2019/947 (EU) | Correct | OK | |
| R2-d30c6489 | Reg. 2020/1058 amending 2019/945 (classes C5, C6) | Substantive amendment of a base act that is present | A | record as amendment event of 2019/945 |
| R2-7e63cdeb | DFARS Part 228 Bonds and Insurance | Procurement insurance rule with an incidental risk-of-loss clause for UAVs; relevance 1 | G | out of the embodied instrument count |
| R2-bd03a374 | 6 CFR Part 139 Conduct on Federal Property | Incidental drone take-off prohibition; relevance 1 | G | out |
| R2-ac756a44 | FCC PSHSB public notice adding UAS to the Covered List | Binding effect is real (bar on equipment authorisation) but the document is an agency public notice, not a regulation | OK* | doc_type "agency determination/notice" |
| R2-e8c05124 | Radiocommunications (Named Person: DroneShield) Instrument 2023 | 107-word register entry naming one company under an exemption; relevance 1 | B, G | out |
| R2-f991965a | Radiocommunications (Commonwealth Games anti-drone) Exemption 2018 | 108-word register entry; event-specific jamming exemption; superseded | B, G | out |
| R2-02911ea9 | CASA 57/22 area approval, 3 NM of aerodromes | 148-word register entry; one of four near-identical area approvals (R2-2c00b35b, R2-226c89bd, R2-77ef4544) | B, A | fetch texts; count the CASR Part 101/MOS regime once and list approvals as instruments of application |
| R2-c5eb5314 | Civil Aviation Safety Regulations 1998 | The real Australian drone regime (Part 101, Part 47), but dated 2026 (compilation date) and captured as a table of contents | E | year 1998; record Part 101 amendment dates (2016, 2019) |
| R2-873de2ab | Part 101 MOS 2019 | Dated 2026 (compilation) | E | year 2019 |
| R2-3aa8ed40 | Civil Aviation (Unmanned Aircraft Levy) Act 2020 | Fiscal levy; 116-word TOC; relevance 1; one of four levy acts/regs | G, B, A | out of the robot-rule count |
| R2-3ce1939d | Road Vehicles Act (JP) 1951 | Correct; Art. 41 automated operation device (2019 amendment) is the robot-relevant event | OK* | add amendment date |
| R2-d40a0c7b | Road Act (JP) | Road administration law; "automated operation assistance facilities" as appurtenances; relevance 1 | G | general law, out of robot-rule count |
| R2-118bce75 | Road Traffic Act (JP) | Key instrument (Level 4 permits; remote-operated small vehicles) but dated 2026, the consolidation date; the Act is 1960, amended 2019 and 2022 | E | year 1960; events 2019, 2022 |
| R2-f57251ed | Ordinance on Industrial Safety and Health (JP) | One of the oldest binding robot-safety rules (Arts. 150-3 to 151, 1983) dated 2026 | E | year 1972; robot provisions 1983 |
| R2-a043fa96 | Safety Regulations for Road Vehicles (JP) | 1951 ordinance dated 2026; relevance 1 | E, G | year 1951; general tier |
| R2-7b1de0c8 | Enforcement Regulations of the Road Transport Act (JP) | Dated 2026; relevance 1 | E, G | |
| R2-3a58754c | Ordinance on Occupancy Fees for Development Roads (JP) | Fee schedule; relevance 1 | G | out |
| R2-b294bc4b | Motor Vehicle Inspection Standards (JP) | Passing reference; relevance 1 | G | out |
| R2-2df9d719 | METI export-control ordinance | Dual-use list; "robots for hazardous environments"; relevance 1 | G | out (or a separate "export control" family) |
| R2-fac50890 | 15 CFR Part 744 (EAR end-use controls) | Export control; relevance 1 | G | out |
| R2-e852c9b8 | 22 CFR Part 121 US Munitions List | Arms export list; incidental | G | out |
| R2-a7defad2 | 15 CFR Part 772 Definitions | Definitions part of the EAR | G, B | out |
| R2-cc07782a | Reg. 2021/694 Digital Europe Programme | Funding programme; robots in recitals; relevance 1 | G | out |
| R2-b54ba4c0 | Reg. 2025/2653 amending Digital Europe and other programmes | Funding programme amendment | A, G | out |
| R2-98aa0eab | Reg. 2025/14 non-road mobile machinery on public roads | Correct and relevant (automated and remotely operated NRMM) | OK* | category: field/agricultural machinery, not "other" |
| R2-2ef1a6ea | Directive 2005/49/EC (24 GHz short-range radar) | EMC rule for radar sensors, not automated driving; superseded | G | out |
| R2-175079cb | Reg. 347/2012 AEBS type approval | Driver assistance (AEB), labelled "autonomous_road_vehicles" | G | add an ADAS category or drop |
| R2-80ec293b, R2-34d7721c | AEBS amending regs 2015/562, 2019/543 | Amendments of the above | A, G | drop |
| R2-07b317f5, R2-0adddb0a | ADR 98/00 and 97/00 (AEB) | 100 to 112-word TOC stubs; AEB | B, G | drop |
| R2-9d7e136e | Implementing Decision 2019/436 harmonised machinery standards | OJ list of standard references; relevance 1; valuable for the legal effect of standards, not a robot rule | G | move to a "standards legal effect" record |
| R2-885d8000, R2-710c5344, R2-77acbca3 | Implementing Decisions 2024/1329, 2026/2015, 2024/2103 | Same; 2026/2015 harmonises EN ISO 10218-1/-2:2025 under the Machinery Directive (a finding the paper misses) | G | same |
| R2-9afd6f5a | FDA De Novo order ReWalk exoskeleton | Correct (special controls codified at 21 CFR 890.3480) | OK* | overlaps R2-3b76fc99 |
| R2-3b76fc99 | 21 CFR Part 890 Physical Medicine Devices | Whole classification part; relevance 1; the robot-relevant section is the De Novo order above | G, A | keep the section, not the part |
| R2-2f360ae8 | State Council Reply on Beijing services-sector zone | Relevance 0; 86 words; enters via "rehabilitation assistive device industry pilot" | G, B | out |
| R2-c05a984c | State Council measures, Shanghai FTZ (excerpt) | Relevance 1; 121 words | G, B | out |
| R2-383a3bd2 | State Council notice, Inner Mongolia FTZ | Relevance 1; 54 words | G, B | out |
| R2-250c1f41 | Beijing E-Town "Several Measures" for the embodied robot industry | A 34-word stub of a local subsidy policy (若干措施: subsidies, data vouchers, insurance premium support) coded as a legally binding regulation and tagged with five robot types; this is the brief's only "binding" humanoid instrument | C, B | reclassify as soft industrial policy; fetch full text; remove the humanoid claim |
| R2-48a5e09b | MIIT Circular 2023 No. 217, ICV access pilots | 49 words captured; binding nature defensible (normative document) | B | fetch full text and annexes |
| R2-71c985a8 | MIIT Notice No. 45 [2025] access, recall, OTA | 32 words captured | B | fetch |
| R2-74fc8ea0 | Beijing AV road-testing measures (Article 2 only) | 30 words | B | fetch |
| R2-44dd9188 | Beijing UA storage-site provisions (excerpt) | 49 words | B | fetch |
| R2-2e97da82 | Interim Regulations on UA Flights (CN, Decree 761) | Correct and important; 284-word promulgation page | OK* | fetch full text |
| R2-e11cb5f7 | Illinois EO 2018-13 Autonomous Illinois | Gubernatorial order creating a voluntary programme; binds state agencies | C | binds = public bodies; not "regulation" |
| R2-f5e63b92 | Minnesota EO 18-04 advisory council | Creates an advisory council | C | as above |
| R2-dddcec43 | Nebraska 60-3301 "Terms, defined" | One definitions section of LB 989; operative sections not captured | A, B | capture the Act (60-3301 to 60-3308) |
| R2-a846a9fc, R2-0f7421dd, R2-785c9ea7 | Iowa 321.514, DC 50-2351, NC 20-400 definitions | Same pattern | A, B | capture the chapters |
| R2-fc6a2ffd | WV Code 17C-24 table of contents | Index page; blank year | B, E | capture 17C-24 and 17H |
| R2-cb3f9817, R2-2b73010a, R2-d7556225, R2-31dea29c | Commencement orders (AV Act 2024 No. 1 and 3; ATMUA Act; Irish RTRA 2023) | Commencement orders of captured or uncaptured Acts | A | attach as commencement events |
| R2-6ecde273, R2-fcdcfae6 | Conseil constitutionnel decisions 2021-817 DC, 2021-834 DC | Genuine binding decisions on police drones; status "in_force" is the wrong field for a judgment | OK* | status "decided"; doc_class court decision |
| R2-4cac38c9 | Conseil d'État order 440442 (2020) | Same | OK* | |
| D0016 | Argentina Res. 710/2024 (UIAAS) | Internal organisational act of the Ministry of Security; v1 finding F11 not implemented | C | binds = public body; not a robot rule |
| D0005 | El Salvador Robotic Technologies Law | Correct; but `source_url` is empty and the decree number and Diario Oficial reference are still unverified | OK* | add provenance |
| D0228 | Dubai Law No. 9 of 2023 | Correct | OK | |
| R2-6a0072d6 | NZ CAR Part 102 | 221-word consolidation page; dated 2025 (amendment date); Part 102 is 2015 | B, E | fetch the rule; year 2015 |
| R2-35fea8b3 | NZ CAR Part 101 | Dated 2025; Part 101 is 2015 | E | |
| R2-7bb2229f | Machinery Regulation 2023/1230 | Status "adopted_not_yet_in_force" is wrong: in force 19 July 2023, applicable 20 January 2027; doc_type "statute" while other regulations are "regulation" | D | add applicability field |
| R2-80171de4 | Machinery Directive 2006/42/EC | Status "superseded_or_repealed" is wrong as of October 2026: repealed with effect from 20 January 2027; it is the robot-safety law in force today (v1 F25 not fixed) | D | in_force until 2027-01-20 |
| R2-0c29bfda | Digital Omnibus 2026/1744 | Correct; its application dates (2 Dec 2027, 2 Aug 2028) are in the capture but unused by the paper | OK* | use them |
| D1291 | AI Act 2024/1689 | "in_force" correct; no applicability recorded; categories include vehicles and drones reached only via Arts. 102 to 109 | OK* | applicability field; annotate Section B route |
| R2-f16a72e1 | UN Regulation No 157 (ALKS) | Correct | OK | |
| R2-7c6034a5, R2-77e55f86 | UN R155, R156 | Correct (cybersecurity, software updates) | OK | |
| R2-4b67cd64 | StVG §1d (DE) | A single 199-word section captured as the "Gesetz zum autonomen Fahren"; §§1e to 1l absent | A, B | capture the Act of 12 July 2021 |
| R2-75af7981 | StVG §1a (DE) | Same pattern for the 2017 amendment | A, B | |
| R2-10fefcfb | AFGBV (DE) | 177-word stub of the ordinance | B | fetch |
| R2-d97f5421 | Automated Vehicles Act 2024 (GB) | Correct | OK | |
| R2-5a3159c0 | AV (Marketing Restrictions) Regulations 2026 | Correct (made July 2026, in force 7 Jan 2027) | OK | |
| R2-66142fe4 | Automated and Electric Vehicles Act 2018 | Correct | OK | |
| R2-d0d19353 | Vietnam Law on People's Air Defense 2024 | Correct (drone licensing regime) | OK | |
| R2-9c282a09 | 49 CFR Part 830 NTSB notification | General aviation law with a UA accident definition | OK* | general tier |
| R2-eadb3869 | Türkiye ADS type-approval regulation 2024 | Correct | OK | |
| R2-c1a0fce3 | NR-12 (BR) | Correct and important (deems ISO 10218/TS 15066 compliance); 2022 is a consolidation date | OK* | year of the robot clause |
| R2-322c6200 | Manitoba WSH Regulation 217/2006 | Correct (Part 16 robots) | OK | |
| R2-06573313, R2-fd1469ee | BC OHS Part 12; Alberta OHS Code | Correct (general OSH with robot sections) | OK* | general tier |
| R2-5a3ba5cd | Arkansas Act 1019 (2015) | Correct | OK | |
| R2-ed0d2da3 | Kentucky HB 7 (2024) | "adopted_not_yet_in_force"; enacted over veto April 2024, effective July 2024 (verify) | D | in_force |
| R2-ab778283 | Ontario O. Reg. 306/15 | Dated 2025; made 2015 (in force 2016), amended | E | |
| R2-aa7a13a1 | BC Motor Vehicle Act RSBC 1996 | Dated 2026; table of contents only; Part 12.1 added 2023/24 | E, B | capture Part 12.1 |
| R2-f8449ddf | ANAC Res. 319/2025 (AR) | Superseded within months by 550/2025; three successive versions of RAAC Part 100 counted (880/2019, 319/2025, 550/2025); 194 words | A, B | one instrument, three versions |
| R2-abd30cb1 | ANAC Res. 550/2025 | Correct instrument; 133-word stub | B | fetch |
| R2-18066a4a | Danish EO supplementing 2019/947 | Correct | OK | |
| R2-4300b76f | Danish Act No. 566/2025 | Correct | OK | |
| R2-0d0ca0f5 | 6 CFR/28 CFR Part 124 counter-UAS | Correct | OK | |
| R2-e0b61aab, R2-fb1d4b44 | 49 USC 44810, 44809 | Code sections dated by last amendment; fragments of FAA Reauthorization Acts that are also present as slip-law headers | A, E | one instrument per Act |
| R2-03dffb43, R2-98d55e2b, R2-b2c62399 | FAA Reauthorization 2018, 2024; AAM Coordination Act | Slip-law headers and legislative history only (143 to 1,055 words) | B | fetch the UAS titles |
| R2-91089001 | Arizona 13-3729 | Blank year (2016) | E | |
| R2-eac3219d | LuftVO §21a (DE) | Blank year (2021); an ordinance coded "statute" | E | |
| R2-7d33c29c | National Strategic Special Zones Act (JP) | Acceptable (sandbox statute enabling vehicle and drone demonstrations) | OK* | |
| R2-59a29a12, R2-ce2171ab | NSSZ enforcement ordinances | Robots as eligible businesses; relevance 1 | G | general tier or out |
| R2-0f2220b7 | Cabinet Office Order, small electric vehicles (repealed) | Not robots | G | out |
| R2-9c4dc434 | Mexico Civil Aviation Law | General aviation law with UAS provisions; dated 2025 (last reform; enacted 1995) | OK*, E | |
| R2-82f8813a | Malaysia CAR 2016 (Part XVI UAS) | Correct general law with drone part | OK* | |
| R2-f8592e32 | UK Air Navigation Order 2016 | Correct general law with drone articles | OK* | |
| R2-3f3f9934 | Delegated Reg. 2026/1188 amending Annex II of 2018/858 | Amendment adding R171 and AVP to type-approval lists; relevance 1 | A, G | attach to 2018/858 |
| R2-0e639229 | Florida 316.2071 PDD | Correct | OK | |
| R2-f51b01be | Florida 330.41 UAS Act | Dated 2026 (compilation); statute 2015/2017 | E | |
| R2-c3888d81 | Peru DS 012-2026-MTC | Correct | OK | |
| R2-83a4b662 | DECEA ICA 100-40 (2026) | Effective 1 July 2026, so "adopted_not_yet_in_force" is stale | D | in_force |
| R2-d012a8fb | Uruguay presidential resolution approving DINACIA authorisations | Individual authorisation of one operator (DRONFIES LABS), not a general rule | C | binds = one addressee; out of rule count |
| R2-87faf76a, R2-833ba7e9 | MDR 2017/745; MDD 93/42 (repealed) | Correct as general product law with embodied relevance 1 | OK* | general tier |
| R2-4d7d2faa | Implementing Reg. 2017/2185 notified-body codes | Administrative list | A, G | out |
| R2-7fa23c8d, R2-4fa6065a, R2-e957136a | Russia Res. 1415; Sweden 2017:309; Spain RD 1036/2017 | Superseded, correctly | OK | (verify Sweden's extension to 2025) |

**S02 / T60: soft-law instruments and standards in the embodied set**

| doc_id | title (abridged) | judgement | error | fix |
|---|---|---|---|---|
| R2-2dc27108 | ISO/TC 299 catalogue of standards (via LVS) | Catalogue page counted as a technical standard with relevance 3 (repeat of v1 D0045/D0218) | B | web page, not instrument |
| R2-00d51a66, R2-0ed7a070, R2-7aac393d, R2-1e489dd3, R2-082af2fd, R2-11676574, R2-0d161ef6 | GB/T 44719, 45312, 46958, 46896, 47025, 47031, 44091 "(portal page)" | Standards-portal pages whose titles and contents the annotator could not see; category inferred from ICS code | B, G | drop until texts are read |
| R2-28ac5c19 | GB 11291.1-2011 (= ISO 10218-1:2006) | Mandatory national standard (`technical_standard_mandated`) counted as soft law; "superseded" rests on a listed 2026 revision project, not a published replacement | C, D | class "mandatory standard"; status current (verify) |
| R2-7b02f71b | GB 11291.2-2013 (= ISO 10218-2:2011) | Mandatory standard counted as soft law | C | |
| R2-26467338 | GB 42590-2023 civil UAS safety requirements | Mandatory standard (effective 1 June 2024) counted as soft law; status "in_force" inconsistent with class | C | |
| R2-4785e2b0 | GB 44495-2024 vehicle cybersecurity | Mandatory; effective 1 Jan 2026 so "adopted_not_yet_in_force" is stale; counted as soft | C, D | |
| R2-124ca4e0 | GB 44496-2024 software updates | Mandatory; `binding_nature` legally_binding but class soft | C | |
| R2-b6bf58d3, R2-b74a9cad, R2-bdae7a53 | KS B ISO 10218-2, 10218-1, KS ISO 13482 | Identical national adoptions counted as separate instruments and as Korea's robot instruments | A | record as adoptions of the ISO instrument |
| R2-3eabedc7, R2-5b4afb4e | CNS 14490-1/-2 (TW) | Adoptions; 110-word store pages | A, B | |
| R2-a10a190a | MHLW 2013 notice on Art. 150-4 (collaborative operation) | The key Japanese collaborative-robot interpretation; 69 words; coded "superseded_or_repealed" (verify: it remains the operative notice) | B, D | fetch; status |
| R2-2406d6c8 | Greek circular on Law 4784/2021 (Art. 42 automated vehicles) | A statute's automated-vehicle amendment reaches the collection only as a ministry circular coded "guideline"; the law is binding and uncaptured | C, B | capture Law 4784/2021 |
| R2-7382c1ae | SACAA Part 101 information page | Web guidance coded soft; the binding CAR Part 101 (2015) is uncaptured | C, B | capture Part 101 |
| R2-1d696723 | Botswana CAA RPA registration page | Web page; `binding_nature` legally_binding, class soft; year 2026 (the S.I. 71 of 2024 at the source URL is the instrument) | B, C, E | capture S.I. 71/2024 |
| R2-f945e7d0 | Qatar RPAS application terms and conditions | Web form; blank year | B | out |
| R2-a856068b | ICV road-testing norms (MIIT/MPS/MOT 2021) | Departmental normative document binding on applicants, coded soft; 190 words | C (borderline), B | fetch; add binds-whom |
| R2-b83cc260 | FBI public service announcement on connected toys | Not a governance instrument | B | out |
| R2-fd1a6bf3 | SPARC Strategic Research Agenda (euRobotics) | Private association's research agenda coded "national strategy" | C | industry report, not instrument |
| R2-35e40c62 | Adra SRIDA 2025-2027 | Same; also class "proposal" with status "published" | C, D | |
| R2-5d4993b3 | PAS 1883:2020 | Correctly "superseded" (withdrawn 2025) | OK | |
| R2-e84bd353 | ISO/AWI 15066-1 | Approved work item (stage 20.00) counted among the 238 published standards | D | "under development" rows out of instrument counts |
| R2-fcda4045 | ISO/FDIS 13482 | FDIS counted as an instrument alongside ISO 13482:2014 | D, A | |
| R2-b28779fd | WP.1 report with 2018 resolution on automated vehicles | Correct soft instrument; TOC-only capture | OK* | |
| R2-d7dae4f6 | UNGA Resolution 79/62 | Correct; title should carry the number | OK | |
| R2-99350112 | Agricultural machinery scrapping subsidy notice (CN) | Subsidy; relevance 1; 21 words | G, B | out |
| R2-6a04779a | EP resolution on minors online | Relevance 1; one paragraph on AI toys | G | general tier |
| R2-15d84608 | EP resolution on Russian airspace violations | Security-policy resolution; relevance generous | G | general tier |
| R2-1bd06d34 | State Council 2023 legislative work plan | A list of planned regulations; relevance 1 | G | out |
| D0460 | Shanghai embodied-intelligence plan | Correct (v2 fix held) | OK | |
| R2-59b89486 | Beijing embodied-intelligence action plan 2025-27 | Correct type; 55 words captured | B | fetch |
| R2-ffa639b7, R2-c0935bcb | ISO 10218-1:2025; ISO/TS 15066:2016 | Correct (store pages) | OK | |
| R2-7da8b467 | UL 3300 SCIEE robots | Correct; the one consumer, companion and education robot safety standard, unused by the brief | OK | cite it in the companion-robot box |
| R2-0488701b | UL 4600 | Correct | OK | |
| R2-db872005 | IEEE 1872-2015 | "Superseded" from "inactivated 2026" is acceptable | OK | |

**S03 / T60: proposals and drafts**

| doc_id | title (abridged) | judgement | error | fix |
|---|---|---|---|---|
| R2-f48a8103 | Proposal for a Regulation on machinery products (2021) | Enacted as 2023/1230 (in S01); still "under consideration" | D | superseded (enacted) |
| R2-e91f8719 | EP amendments of 14 June 2023 on the AI Act | Enacted; duplicate of D1064, which v2 did fix | D, A | superseded |
| R2-e09b2ee1 | Digital Omnibus proposal (2025) | Enacted as 2026/1744 (in S01) | D | superseded |
| R2-b497d818 | EP amendments on the Omnibus (March 2026) | Enacted | D, A | superseded |
| R2-c5f8f802 | EP amendments, Digital Europe (2018) | Enacted as 2021/694; relevance 1 | D, G | superseded |
| R2-960229c7 | Euro 7 proposal (2022) | Enacted as 2024/1257; emissions, not automated driving | D, G | out |
| R2-99a032c7 | India Draft Drone Rules 2021 | Final Drone Rules notified 25 Aug 2021 (G.S.R. 589(E), in the inventory as AP-001, fetch 403); "consultation_open" | D | superseded; capture the final rules |
| R2-11cb34e4 | AV START Act S.1885 (2017) | Died with the 115th Congress; 182-word metadata page | D, B | withdrawn_or_lapsed |
| R2-7b9dcf74 | S.1394 Block Nuclear Launch by Autonomous AI Act (2023) | Lapsed with the 118th Congress; 135 words | D, B | lapsed |
| R2-95cb0662 | Tennessee HB 591/SB 796 (2013) | Enacted as the Freedom from Unwarranted Surveillance Act (Pub. Ch. 470 of 2013, verify) | D | enacted |
| D1140 | EU White Paper on AI (2020) | "consultation_open" six years on (v2 did not fix) | D | closed; superseded by the AI Act |
| R2-5da1a6e6 | France and Germany CCW working paper 2017 | A negotiating submission, not a proposal of an instrument | C | class "position paper"; out of the drafts stratum |
| R2-c2fb53b6 | US CCW working paper 2018 | Same; status "not_applicable" | C | |
| R2-c94bd401 | Brazil CCW paper on IEEE 7007 | Discussion paper | C | |
| R2-278452d3 | Draft articles on AWS (WP.7, 2025) | Acceptable as a proposed text; issuer coded national executive with jurisdiction INT | OK*, F | |
| R2-8287ac55 | Draft Protocol on AWS (seven states) | Acceptable; blank year (2022 per URL) | E | |
| R2-33fd0145 | Proposal for a Council Decision on the EU position at ICAO (2021) | Adopted (verify); an EU negotiating-position decision, not a draft robot rule | D, C | out |
| R2-46d2a2e2 | Food and feed omnibus proposal (drone spraying exemption) | Acceptable as a draft with an embodied provision | OK | |
| R2-d6f8ff36 | CCMTA white paper 2016 | Class "proposal" with status "not_applicable" | C, D | soft or report |

### 3.3 Population-level structural checks (all rows, not the sample)

- **S01 (299):** 71 under 300 words (median of the set 1,926; the v2 rule that excluded the 204-word Taiwan stub was not applied); 56 whose own summary says only register metadata or a table of contents was read; 79 whose title marks them as amending, correcting, EEA incorporation, commencement, levy, exemption, direction, approval or harmonised-standards decisions; 21 index pages, definition sections or excerpts; 55 rated relevance 0 or 1; 24 export-control, procurement, EMC, AEB, noise, registration and fee rules. Union: 168 of 299 (56%). The 131 that remain are 69 drone rules, 45 automated-driving rules, 7 delivery-device statutes, 5 industrial-robot rules and 5 others; by jurisdiction 40 US, 13 EU, 11 Japan, 10 UK, 9 Canada. The paper's "265 of 299 (89%) govern drones or vehicles" survives as a share (114 of 131, 87%) but not as a count.
- **Australia:** 45 of 48 binding rows are under 300 words and 32 are exemptions, directions, approvals or levies. Oceania's "52 binding instruments" and its "distinct" regional profile (paper 5.4, discussion) rest on this.
- **EU:** 38 of 56 binding rows are amending, correcting, incorporating or list acts; 16 are relevance 0 or 1.
- **Japan:** 14 of 26 are relevance 0 or 1; 7 of 26 are dated 2026 because the e-Gov API serves consolidated texts, which also moves 1951 to 1972 laws into the 2025 to 2026 bins of Figure 6 and Table 28.
- **S02 standards (241 in the embodied set):** 179 landing pages, 59 partial captures, 3 substantive; 47 "under development" (46 carry AWI, WD, CD, DIS, FDIS or P-draft designations in the title) and are counted among the "238 technical standards"; 9 `technical_standard_mandated` and 1 `legally_binding` are counted as soft law; 11 are national adoptions of ISO/IEC texts.
- **S03 drafts (71 rows; paper says 75):** 18 are CCW GGE working papers, chair's texts or national submissions; at least 9 are enacted, adopted or lapsed texts still coded as drafts or open consultations; 3 "superseded" and 2 "withdrawn" rows sit inside the drafts table.
- **Scheme consistency:** 6 soft instruments are "in_force"; 3 soft instruments have `binding_nature` legally_binding; court decisions are "in_force"; the Machinery Regulation and Directive have their statuses reversed relative to the law in force on the review date.

---

## 4. Findings

Severity: **critical** (a headline claim is wrong or unsupported), **major** (a section-level claim or the classification scheme is unsound), **minor** (local error or presentation).

| id | severity | location | problem | evidence | suggested fix |
|---|---|---|---|---|---|
| F1 | critical | brief ¶1-2; paper abstract, 5.1, Table 33, 6; report key numbers | "299 legally binding instruments reach robots (268 in force)" is a count of captured documents, not instruments: 56% are stubs, dependent acts, fragments or incidental law (3.3). Every number derived from it (265 drones/vehicles, 17 industrial arms, 15 delivery, 9 surgical, Table 9 binding shares, Figure 6, Oceania 52, Europe 97, T04 "binding" column) is inflated by roughly two-fold | 168/299 in at least one bucket; 71 under 300 words; 79 administrative by title; 55 relevance 0-1 | Build an instrument-level inventory (one row per instrument; captures, amendments, corrigenda, commencement orders, EEA decisions and national adoptions as child records); recompute all instrument counts on it; report the stub share and exclude stubs from content statistics as v2 did for Taiwan |
| F2 | critical | brief ¶4 ("Humanoids ... one text labelled binding (a 2025 Beijing development-zone measure)"); paper 5.2; report Part E | The only "binding" humanoid instrument is R2-250c1f41, a 34-word stub of Beijing E-Town's "Several Measures" granting subsidies (humanoid sales subsidy 10%, insurance premium subsidy 50%); it imposes no obligation on anyone and is not a regulation. The Chinese "binding" set also includes four other 30 to 49-word stubs | master_table rows R2-250c1f41 (words 34), R2-74fc8ea0 (30), R2-71c985a8 (32), R2-48a5e09b (49), R2-44dd9188 (49) | Reclassify as soft industrial policy; state that no binding humanoid-specific rule was captured; note the uncaptured Hangzhou regulation (inventory AS-028) and the GB/T 48317 humanoid series (voluntary) |
| F3 | critical | paper 5.1 and 5.3 (standards "specify physical safety in depth in 47%"), Table 9, discussion ¶3; brief ¶6 | The standards layer is 241 documents of which 179 are catalogue pages and 3 substantive; 47 are drafts (AWI to FDIS) counted as published; 10 are mandatory or binding standards counted as "soft law"; 11 are national adoptions double-counting ISO texts. The "47% specify in depth" statistic is computed on scope statements and catalogue blurbs, and the paper says so only in passing | S02 page_quality counts; titles with ISO/AWI, ISO/CD, ISO/DIS, ISO/FDIS, IEEE P; `technical_standard_mandated` rows in S02 | Separate published / under development / withdrawn; add `standard_legal_effect` (voluntary; harmonised with presumption of conformity, with OJ decision; incorporated by reference; mandatory national); drop Table 9's standards row or label it "scope statements" |
| F4 | critical | paper 5.1 ("75 proposals or drafts"), Table 9 drafts row ("autonomy-level control specified in depth by 37% of drafts", "dual use 41%"), discussion ¶3 | The drafts stratum is one quarter CCW GGE working papers and national submissions (18 of 71) and includes at least 9 enacted or lapsed texts still coded as live drafts (Machinery Regulation proposal, EP AI Act amendments, Omnibus proposal and amendments, Digital Europe, Euro 7, India Draft Drone Rules, AV START, S.1394, Tennessee 2013). The "drafts specify autonomy and dual use most" finding is a LAWS-negotiation artefact | S03 rows listed in 3.2 | Re-code working papers as position papers (a new class) and enacted proposals as superseded; recompute Table 9 |
| F5 | major | paper 5.1 (268 in force, 7 adopted); brief ¶2 ("7 adopted but not yet applying"); rows R2-7bb2229f, R2-80171de4, D1291 | "In force" and "applicable" are still conflated (v1 F9). The Machinery Regulation is coded not yet in force (it entered into force 19 July 2023 and applies from 20 January 2027); the Machinery Directive is coded repealed although it governs robots until that date; the AI Act is "in force" with no record that its high-risk obligations for machinery apply from 2 August 2028 under the captured Omnibus (R2-0c29bfda) | master_table statuses; R2-0c29bfda key provisions | Add `entry_into_force` and `applicability_date(s)`; recompute "in force" on the review date; state in 5.1 that as of October 2026 no AI Act high-risk obligation yet applies to a robot as a machinery product |
| F6 | major | brief ¶2 ("the other 127 are general-AI instruments with robot provisions"); paper 3, Table 33; report §key numbers | The tier "general-AI instrument with embodied provisions (relevance 0-1)" is mislabelled: of its 55 binding members, most are not AI instruments at all (Japan's Road Act, freight-transport ordinances, inspection standards and occupancy-fee ordinance; US export-control parts, DFARS, FAR, federal-property conduct rules; an Australian drone levy; EU corrigenda and list acts; the MDR and MDD). Only the AI Act, EO 14110 and the Omnibus fit the label | list of 55 relevance 0-1 binding rows (3.3) | Rename the tier "sector or general law with an incidental embodied provision" and split out the genuinely general-AI instruments (3) |
| F7 | major | paper 5.4, discussion ¶5; report Part D ("Oceania is Australian and New Zealand drone and vehicle regulation (56 embodied instruments, 52 binding)") | Oceania's distinct profile is produced by 45 Australian register entries of 88 to 167 words (CASA exemptions, directions, area approvals, levies, radiocommunications exemptions). A region whose instruments are metadata stubs cannot have a measurable principle or mechanism profile | S01 Australian rows; words column | Exclude stubs from regional profiles; report Oceania's binding layer as one regime (CASR Part 101 and MOS, with instruments of application) |
| F8 | major | 3.1 Analysis sets; T04; brief ("Sixty jurisdictions hold a robot instrument") | Jurisdiction counts and the EU's 56 are inflated by administrative acts; 10 EEA Joint Committee decisions are coded jurisdiction EU (they bind Iceland, Norway and Liechtenstein); Korea's and Taiwan's "robot instruments" are national adoptions of ISO 10218 and 13482 and store pages; Botswana's and Qatar's are web pages | S01 EU rows; S02 KR/TW/BW/QA rows | Jurisdiction EEA for JC decisions; count adoptions as adoptions; count a jurisdiction only when a substantive instrument is captured |
| F9 | major | paper 5.1 Figure 6 ("283 by 2026", "half since 2022"); 5.5 trends (industrial policy rising; humanoid and physical-AI shares 2025-26); Table 28 | Consolidated texts are dated by consolidation: Japan's Road Traffic Act, Road Vehicles Act safety regulations and Industrial Safety and Health Ordinance (1951 to 1972) are "2026"; CASR 1998 and MOS 2019 are "2026"; BC's 1996 Motor Vehicle Act is "2026"; NZ Parts 101/102 (2015) are "2025"; O. Reg. 306/15 is "2025"; US Code sections carry their last amendment year. 84 of 299 binding rows fall in 2025-26 | master_table year_final vs titles | Year = enactment (or the amendment that introduced the robot provision); add `consolidation_date`; rerun Figure 6 and Table 28 |
| F10 | major | paper 5.1 and 3; S01 | No `binds` field (v1 F3, F11, F26 recommendation): gubernatorial executive orders creating programmes or councils (R2-e11cb5f7, R2-f5e63b92), Argentina's unit-creation resolution (D0016), a Uruguayan company-specific authorisation (R2-d012a8fb), constitutional-court judgments and export-control lists are pooled with statutes as "legally binding regulations" | rows cited | Add `binds` (private parties / public bodies / single addressee / internal) and `legal_form` (statute, secondary regulation, executive act, court decision, individual decision) |
| F11 | major | paper 5.1 ("El Salvador's Robotic Technologies Law remains the only binding instrument with 'robot' in its title"); brief ¶1 | False within the collection (R2-250c1f41's title names the "Embodied Intelligent Robot Industry") and known to be false outside it: the Korean Intelligent Robots Development and Distribution Promotion Act (2008) and the Hangzhou Regulations on Promoting the Development of the Embodied Intelligent Robot Industry (2026, inventory AS-028, fetched with HTTP 200 but no text) are binding robot-titled laws | title search; inventory | Say "the only robotics statute captured"; name the two uncaptured ones |
| F12 | major | brief ¶4 and ¶9 (companion robots: "13 instruments, none binding"; "what reaches the purchase is general AI law, data-protection law and ... ISO 13482"); paper discussion ¶4 | Within the collection the count is right, but the regimes that actually bind a companion robot are not named although several are captured: the GPSR (R2-d47b1feb, relevance 0-1, unused), the CRA (R2-ded4c023), UL 3300 (R2-7da8b467, the consumer-robot safety standard), BS 8611, GB/T personal-care and entertainment-robot standards (R2-f13c76d2, R2-492928d7), the EP's 2025 resolution noting AI toys as high-risk under the Toy Safety Regulation (R2-6a04779a); the Toy Safety Regulation (EU) 2025/2509 and California SB 243 are in the inventory unread (EU-024/MW-068, US-095) | rows cited | Add the regime-coverage matrix the v1 review proposed; rewrite the companion-robot paragraph as "no robot-specific instrument; governed by product-safety, toy, cybersecurity, data-protection and AI-transparency law" |
| F13 | major | `reference_instruments.csv`; T25; paper 5.1 ("31 of 38 captured") | The reference list is unbalanced and partly wrong: 10 of 38 entries are general-AI instruments (two executive orders, NIST RMF, OECD, UNESCO, CoE Convention, ISO/IEC 42001, IEEE 7001, Japan and Korea AI acts); Taiwan's standards are still dated 2025 (promulgated 1987, amended 2018); "UN R157 and R171" is marked captured although only R157 is; "US state AV statutes" is marked captured on the strength of a DMV news page (R2-6b4fb33d, communication) and a 2025 rulemaking notice; the list lacks the instruments a robot lawyer would check first (DoD Directive 3000.09; Japan's ISH Ordinance robot provisions; Korea's Autonomous Vehicles Act; Singapore's AMV Rules; Taiwan's Unmanned Vehicles Act; China's Interim Regulations on UA Flights and GB 11291; India's Drone Rules; UN R155/R156; SAE J3016; IEC 80601-2-77/-78; the Toy Safety Regulation; FAA Part 89) | T25 rows; master_table title search (R171: 0 hits; Singapore AMV Rules: 0; Taiwan UV Act: 0; DoD 3000.09: 0) | Rebuild the list in two parts (robot-binding law and standards: ~50 items; general-AI controls: ~10 items); mark "captured" only when a substantive capture of the instrument itself exists |
| F14 | major | coverage; `round2_inventory.csv`; T52 | Important binding instruments were found by collectors and lost at the fetch stage, including several that would change conclusions: Hangzhou embodied-robot regulations (AS-028), Shenzhen ICV regulations (AS-013), Shenzhen AI industry regulations (AS-029), Shenzhen low-altitude economy regulations (AS-030), Hong Kong Road Traffic (Autonomous Vehicles) Regulation (AS-152), Korea Intelligent Robots Act and decree (AS-100/101), Korea AV Act decrees (AS-103/104), DoD Directive 3000.09 (IG-112), France ordonnance 2021-443 and décret 2021-873 (EN-017/018), Toy Safety Regulation (EU-024, MW-068), PLD 2024/2853 (EU-020), California SB 243 (US-095), India Drone Rules 2021 (AP-001), ANSI/A3 R15.06-2025 (ST-190), GB/T 48317.1 (ST-232); 190 of the 359 unread candidates are coded legally binding by the collectors | inventory rows; fetch_status | Read the 190 binding candidates through a browser session or a human; they are already identified and verified |
| F15 | major | brief ¶1 ("only one ... national law written for robots as such"); paper discussion ¶1 | The route finding is right but the qualifier is missing: general product-safety law (GPSR 2023/988, applicable since December 2024; Directive 2001/95/EC before it, captured R2-01ddcdaa), machinery law (Directive 2006/42/EC in force), OSH framework law (89/391/EEC, not captured), data-protection law (GDPR, cited by 9% of embodied documents, not captured), liability law (PLD 85/374 and 2024/2853, not captured; AEV Act 2018 captured) and consumer law bind every robot without naming it. The study treats "mentions a robot type" as the test of reaching robots, so it undercounts horizontal law and overcounts incidental mentions | T25; master_table | Add a short "horizontal law" section and the coverage matrix; state the test used |
| F16 | major | codebook; paper 3 ("robot-specific if ... rated at least moderately relevant") | "Robot-specific" is a relevance score (≥2) assigned to a capture, not a property of an instrument's scope. An EEA incorporation decision, a corrigendum and a CASA area approval are "robot-specific instruments"; the GPSR and MDR are not | S01/S02 relevance values | Rename to "embodied-focused capture"; derive instrument scope from the inventory (robot-specific statute / sector regime with robot provisions / horizontal law) |
| F17 | minor | taxonomy | AEB type-approval acts (Reg. 347/2012 and amendments, ADR 97/98, 49 CFR 596) and UN R79 steering are labelled `autonomous_road_vehicles`; the taxonomy has no driver-assistance (SAE L1-2) category and therefore conflates ADAS with automated driving | rows cited | Add `driver_assistance_adas` or restrict `autonomous_road_vehicles` to L3+ |
| F18 | minor | taxonomy | `other_embodied` holds non-road mobile machinery (Reg. 2025/14), small rental EVs and the Digital Europe programme; field, construction and mining machinery (ISO 17757, GB/T on autonomous mining machines R2-45a27a25 coded "space_or_extreme") lack a home (v1 F20d) | rows cited | Add `field_construction_mining_machinery` |
| F19 | minor | doc_type | Regulations coded "statute" (Machinery Regulation, MDD) and statutes coded "regulation"; LuftVO §21a coded statute; CCW working papers issued by "national_government_executive" with jurisdiction INT; FCC public notice as regulation | rows cited | Consistency pass with `legal_form` |
| F20 | minor | S01 "24 superseded" | Includes CASA exemptions of 2012 to 2016 and three successive Argentine Part 100 resolutions; the Machinery Directive is wrongly among them while the AI Act proposals are correctly so | S01 status column | Recompute after F1 |
| F21 | minor | paper 5.1 (standards harmonisation) | Implementing Decision (EU) 2026/2015 (R2-710c5344) harmonises EN ISO 10218-1/-2:2025 and EN ISO 18497 under the Machinery Directive: the "standards are voluntary" sentence is contradicted by a captured document that the analysis treats as a drone/vehicle "binding instrument" | R2-710c5344 key provisions | Use the four harmonised-standards decisions as evidence of legal effect |
| F22 | minor | D0005 | Source URL empty; Diario Oficial reference and decree number unverified since v1 | master_table | Add provenance |
| F23 | minor | T59 and brief | Two Beijing documents are "excerpts" of one article; the Vienna Convention and AutomatFahrV rows are explicitly "status page" and "search result listing" in their own titles yet pass the usability filter | titles | Make "landing_or_index_page" exclude from instrument counts, as v2 did for content statistics |

---

## 5. Substantive claims: correct as stated, or needing qualification?

1. **"Sector law reaches robots; only El Salvador has a robotics statute."** Direction correct; count wrong (F1); "only" wrong (F11: Korea 2008, Hangzhou 2026, both found by collectors and unread). Needs the horizontal-law qualification (F15): machinery, general product safety, OSH framework, data protection, product liability and consumer law bind robots without naming them, and three of these are not even in the collection as documents. The paper's own captured Decision 2026/2015 shows EN ISO 10218:2025 harmonised under the Machinery Directive, which is the single most important fact about how industrial robots are governed in Europe and is absent from the text.
2. **"Drones and vehicles dominate (89%)."** Correct as a share even after cleaning (87% of the 131 substantive, relevance ≥2, non-administrative binding rows), but it must be stated as a property of (a) a harvest that queried databases with drone and vehicle keywords, and (b) legal granularity: one Australian drone regime appears as 46 instruments, one Japanese robot-safety regime as one ordinance article group. "Dominate" should be replaced by "most binding texts that name a robot type are aviation and road-traffic texts".
3. **"Companion, care and humanoid robots lack binding rules."** Defensible only as "no robot-specific binding instrument captured" and false as a statement about law: the GPSR, Toy Safety Regulation, CRA and RED delegated act, GDPR and COPPA, AI Act Arts. 5 and 50 and California SB 243 bind them; UL 3300 and BS 8611 are the specific standards; the "one binding humanoid text" is a subsidy stub (F2). Care robots: ISO 13482 (and its FDIS successor), Japan's AMED/MHLW guidance and the Korean and Chinese adoptions are captured but the brief's "4 binding" for care robots are the AI Act, 21 CFR 890, a Japanese zone ordinance and El Salvador's law, none of which is a care-robot rule.
4. **"Regional differences, Oceania and the standards layer distinct, Europe and North America now distinguishable."** Oceania is an artefact (F7); Europe's instrument count is inflated by 38 administrative EU acts and 10 EEA decisions (F8); Asia's 41 binding includes 14 Japanese general transport texts; the Middle East remains a research literature plus two Dubai laws. The distances computed on documents rather than instruments should be labelled "as captured" and recomputed without stubs.
5. **"Trends: industrial policy rising, personhood falling, 283 binding by 2026, physical AI vocabulary rising."** The 2025-26 bins contain consolidation-dated 1950s to 1990s laws, 2026 compilations and dozens of 2025-26 Chinese policy notices, which is exactly the "industrial policy" topic; the rise is at the edge of significance and should not be reported until years are corrected (F9). Personhood decline is a research-discourse finding and stands.
6. **"Autonomy-level control is specified in depth by 18% of binding rules."** With R157, the StVG fragments, the UK Act, Japan's Road Traffic Act and 2022/1426 now present the claim is better founded than in v2, but the denominator still contains ~170 rows that cannot specify anything (stubs, corrigenda, levies). Recompute on substantive captures only.

---

## 6. Terminology and taxonomy

- **Instrument vs document vs capture.** The whole package uses "instrument" for a captured document. Define instrument (a legal act with its own identity), capture (a file), and dependent act (amendment, corrigendum, commencement, incorporation, adoption), and count only instruments.
- **"Binding instrument" needs `legal_form` and `binds`.** Statute, secondary regulation, executive act binding public bodies, individual administrative decision, court decision, treaty, mandatory standard. The present scheme puts a Minnesota advisory-council order, a Uruguayan one-company authorisation, a corrigendum and the UK AV Act in one class.
- **"Robot-specific" (F16).** Replace with scope categories: robot-specific statute or regulation; sector regime with robot provisions (aviation, road traffic, machinery, OSH, medical devices); horizontal law reaching robots (product safety, liability, data protection, cybersecurity, consumer, toys); AI law with embodied provisions.
- **"Soft law" absorbs three different things:** voluntary standards, mandatory or harmonised standards (legal effect), policy strategies and subsidy notices, and administrative guidance that is binding on its addressees in practice (Chinese departmental "norms", Japanese tsūtatsu). Add `standard_legal_effect` and `administrative_guidance_binding_on_addressees`.
- **"Proposal or draft"** should exclude negotiating submissions and position papers (new class) and should expire: a proposal enacted or lapsed is "superseded", "enacted" or "lapsed", with the date.
- **Lifecycle:** split into `adopted`, `entry_into_force`, `applicable_from`, `amended`, `repealed_from`; "in_force" for court decisions and soft law is a category error.
- **Robot types:** add driver-assistance (ADAS) distinct from automated driving; add field, construction and mining machinery; separate "humanoid morphology" from "embodied foundation model" (v1 F20b); `other_embodied` should not hold funding programmes.
- **Jurisdiction:** add EEA; distinguish "international (treaty body)" from "international (standards body)" from "state submission to an international body".
- **"Technical standard":** published; under development (with stage); withdrawn; national adoption (of what); harmonised (under which act, which OJ decision); mandatory.

---

## 7. Coverage: missing instruments and the reference list

### 7.1 Important instruments or jurisdictions still missing (beyond the seven in T25)

In the inventory but unread (fix first; each is identified and verified by a collector):
- Hangzhou Municipal Regulations on Promoting the Development of the Embodied Intelligent Robot Industry (Hangzhou People's Congress, 2026), AS-028: a binding robot-titled statute.
- Shenzhen SEZ Regulations on the Administration of Intelligent Connected Vehicles (Shenzhen People's Congress, 2022), AS-013; Shenzhen SEZ Regulations on Promoting the AI Industry (2022), AS-029; Shenzhen SEZ Regulations on Promoting the Low-Altitude Economy Industry (2024), AS-030.
- Hong Kong Road Traffic (Autonomous Vehicles) Regulation, Cap. 374AF (Transport and Logistics Bureau, 2024), AS-152.
- Korea: Intelligent Robots Development and Distribution Promotion Act and Enforcement Decree (2008, as amended), AS-100/101; Enforcement Decree and Rule of the Act on Promotion of and Support for Commercialisation of Autonomous Vehicles (MOLIT, 2020), AS-103/104.
- United States: DoD Directive 3000.09, Autonomy in Weapon Systems (2023), IG-112; California SB 243 companion chatbots (2025), US-095; Drone Rules 2021 (India, MoCA, G.S.R. 589(E)), AP-001.
- EU: Product Liability Directive (EU) 2024/2853, EU-020; Toy Safety Regulation (EU) 2025/2509, EU-024/MW-068; Toy Safety Directive 2009/48/EC, EU-025.
- France: Ordonnance 2021-443 and Décret 2021-873 on criminal liability for automated vehicles, EN-017/018.
- Switzerland: DETEC Ordinance on Aircraft of Special Categories (VLK) 2022, EN-024.
- Standards: ANSI/A3 R15.06-2025, ST-190; GB/T 48317.1-2026 humanoid robots Part 1, ST-232.

Not in the inventory at all (name, issuer, year):
- UN Regulation No. 171 Driver Control Assistance Systems (UNECE WP.29, 2024); the reference list marks it captured, it is not.
- Vienna Convention on Road Traffic as amended: Art. 8(5bis) (2016) and Art. 34bis (2022) (UNECE WP.1); only a status page is held.
- NHTSA Standing General Order 2021-01 on ADS and Level-2 crash reporting (NHTSA, 2021, amended 2023, 2025); FMVSS occupant-protection amendments for vehicles without manual controls (NHTSA, final rule March 2022); 49 CFR Part 555 exemptions; 14 CFR Part 108 BVLOS (FAA, NPRM August 2025, verify status).
- California DMV autonomous-vehicle regulations, 13 CCR §§227.00 to 228.28 (2014 to 2024; the collection holds a news page and the 2025 NPRA only); Arizona ARS 28-9701 to 9705 (2021); Texas SB 2205 (2017).
- Singapore Road Traffic (Autonomous Motor Vehicles) Rules 2017 (LTA) and TR 68 parts 1 to 4 (the collector reports them verified; no capture matched).
- Taiwan Unmanned Vehicles Technology Innovative Experimentation Act (2018) and Industrial Robot Hazard Prevention Standards (MOL, 1987, amended 2018).
- Japan: Act No. 32 of 2022 amending the Road Traffic Act (Level 4 "specified automated operation" and remote-operated small vehicles) as an identifiable amendment event; MHLW 1983 Technical Guidelines for industrial robot safety (captured without a year); Road Transport Vehicle Act amendment 2019 (automated operation devices).
- Beijing Autonomous Vehicles Regulations (Beijing Municipal People's Congress, 2024, in force 1 April 2025); Shanghai Pudong New Area Regulations on Driverless ICVs (2022); Wuhan and Chongqing ICV rules (verify).
- Korea Robot Ethics Charter (MOTIE, 2007/2018); Korea 4th Intelligent Robot Basic Plan (2024).
- Germany: BNetzA prohibition of the "My Friend Cayla" doll (2017); Autonomous driving ordinance AFGBV full text (captured as a 177-word stub).
- Italy: Decreto "Smart Road" (MIT, 28 Feb 2018) is captured; Law 132/2025 on AI (collector verified; check capture).
- Framework Directive 89/391/EEC and Work Equipment Directive 2009/104/EC (EU, OSH); RED Delegated Regulation (EU) 2022/30 (cybersecurity of connected consumer devices and toys).
- COPPA Rule amendments (FTC, 2025); New York companion-AI provisions (2025).
- IEC 61508 series and ISO 13849-1:2023 are captured; add IEC 62061:2021, ISO 12100:2010 and ISO 17757:2019 (earth-moving autonomy) as standards records.
- IMO MASS Code (non-mandatory, MSC 2025, verify); ICAO Annex amendments on RPAS (Annexes 1, 2, 6 Part IV, 8, 10; 2024 to 2026) as instruments rather than via the EU position proposal.
- CCW GGE 2019 Guiding Principles are captured inside the 2019 Final Document; add the 2023 and 2024 GGE reports' consensus conclusions as the instrument-level record (they are present as government reports).
- Africa: Kenya Civil Aviation (Unmanned Aircraft Systems) Regulations 2020 and the Kenya Robotics and AI Society Bill 2023 (collector verified; check capture); Nigeria Part 21 is captured.
- Latin America: Brazil RBAC-E 94 (ANAC, 2017, amended) and Decreto 9.557/2018 (collector could not find); Chile AV testing regulation (not found); Mexico NOM-107 is captured.
- Middle East: Ras Al Khaimah AV law (2026), Abu Dhabi AV permit rules, Saudi SASO AV regulation (collector verified; check capture), Israel Traffic Ordinance Amendment 130 (verified; check capture).

### 7.2 Is the reference list of 38 adequate?

No. It mixes two populations (robot-binding law and standards; general-AI instruments) so that "31 of 38 captured" reports on both; it carries a wrong year (Taiwan 2025); two "captured" rows rest on a news page and a notice of proposed rulemaking (US state AV statutes) or on one of two named regulations (R157/R171); and it omits the instruments a robotics regulator would list first. Proposed removals from the robot list (move to a separate general-AI control list): EO 14110, EO 14179, NIST AI RMF, Japan AI Promotion Act, Korea AI Basic Act, OECD AI Principles, UNESCO Recommendation, Council of Europe Framework Convention, ISO/IEC 42001, IEEE 7001. Proposed additions (binding or quasi-binding, with issuer and year): DoD Directive 3000.09 (2023); NHTSA SGO 2021-01; FMVSS 2022 ADS amendments; 14 CFR Parts 89 (2021) and 108 (proposed); California 13 CCR §227 (2014/2018); Virginia §46.2-908.1:1 (2017); Japan ISH Ordinance Arts. 150-3 to 151 (1983) and Act No. 32 of 2022; Korea Autonomous Vehicles Act (2019); Singapore AMV Rules (2017); Taiwan Unmanned Vehicles Act (2018); China Interim Regulations on UA Flights (2023), GB 11291.1/.2 (2011/2013), GB 42590-2023, Shenzhen ICV Regulations (2022), Hangzhou embodied-robot regulations (2026); Hong Kong Cap. 374AF (2024); India Drone Rules (2021); UN R155/R156 (2021) and R171 (2024); Vienna Convention Art. 34bis (2022); Toy Safety Regulation (EU) 2025/2509; RED DA 2022/30; Framework Directive 89/391; France ordonnance 2021-443; Netherlands Experimenteerwet (2018, captured); Australia CASR Part 101 (1998/2016) as one regime; SAE J3016 (2021); IEC 80601-2-77 and -78 (2019); ISO 13849-1:2023; UL 3300 (2024); BS 8611:2023. Fix the Taiwan year and the R171 capture flag; mark "captured" only for a substantive capture of the instrument itself.

---

## 8. The five changes that would most improve credibility with policy readers

1. **Replace the document count with an instrument inventory and recount.** One row per instrument with legal form, binds-whom, jurisdiction (EEA where applicable), enactment, entry into force, applicability, amendment and repeal dates, capture tier and child records for amendments, corrigenda, commencement orders, EEA decisions, retained copies and national adoptions. Exclude stubs (<300 words or self-declared metadata) from every count as v2 did for Taiwan. Re-state the brief's first paragraph from the result (my estimate: about 130 substantive binding robot rules, 87% aviation and road traffic).
2. **Read the 190 binding candidates that were found and not fetched** (inventory `has_text = False`, `binding_nature = legally_binding`), starting with the fifteen named in F14. They are already verified; they include the two findings that would change the headline (Hangzhou's robot statute; Korea's Act) and the horizontal regimes the companion-robot paragraph needs (Toy Safety Regulation, PLD, SB 243).
3. **Fix the status model**: entry into force vs applicability (Machinery Regulation, Directive, AI Act under the Omnibus), expire enacted or lapsed proposals, move CCW working papers and national submissions out of "drafts", move mandatory GB standards out of "soft law", and separate published from under-development standards. Then recompute Table 9, Figure 6, Table 28 and the regional profiles.
4. **Add the regime-coverage matrix** (robot category × machinery / product safety / type approval / aviation / medical devices / OSH / toys / data protection / cybersecurity / liability / AI law / standards) and rewrite the "what it means for you" box and the companion-robot gap from it, naming UL 3300, BS 8611, the GPSR, the Toy Safety Regulation, the CRA and SB 243.
5. **Correct years to enactment and add the dates of the robot-relevant amendments**, so that 1951 to 1972 Japanese laws, CASR 1998 and BC's 1996 Act stop appearing in the 2025-26 bins; then re-test the "industrial policy rising" and "283 binding by 2026" statements, and date Figure 6 by entry into force and by applicability.

---

## 9. Counts

- Findings: 4 critical (F1 to F4), 12 major (F5 to F16), 7 minor (F17 to F23).
- Classification audit: 159 instruments inspected; 108 (68%) with at least one error, 98 (62%) with a material error; by stratum S01 66/106, S02 25/34, S03 17/19. Risk-stratified sample, so an upper bound.
- Population checks: 168 of 299 binding rows (56%) are stubs, dependent acts, fragments or incidental law; 179 of 241 standards are catalogue pages, 47 are drafts, 10 are mandatory or binding; 18 of 71 drafts are CCW working papers; 9 or more drafts are enacted or lapsed texts.
- v2 fixes: all held for the round-1 documents; every one of them recurs in the round-2 documents because none was turned into an admission rule.
