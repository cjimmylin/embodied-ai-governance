# Collection round 2 runbook (for agents extending the collection)

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Written 31 October 2026 after round 2 of the embodied-AI governance study. This file is the operational record: what was built, where it lives, exactly how each source was queried, what failed, and how to run a round 3. The human-readable methods narrative is `report/src/methods_document_discovery.md` in the v3 package. Numbers below are the final v3 figures.

## 1. Outcome in one table

| Stage | Count |
|---|---:|
| Candidate rows written by collectors and harvesters (before merge, including the dropped Fedlex file) | 2,918 |
| Candidates after schema validation, relevance filter, within-round and against-round-1 de-duplication | 2,075 (collector agents 1,157; scripted harvests 918) |
| Text obtained | 1,716 (1,700 fetched from the issuing source, 16 standards scope texts from the abstract agent) |
| No text (kept in inventory, counted nowhere) | 359 (273 HTTP error or thin/script-only page, 46 blocked host, 40 fetch failed) |
| Annotated (metadata-blind, extended excerpt, same policy as v2) | 1,716 (about 125 USD of model cost, Claude Sonnet 5.5) |
| Entered the v3 master table after the assembly de-duplication passes | 1,637 (79 round-2 rows removed as duplicates) |
| Usable captures | 1,611 |
| In the embodied-AI set | 914 |
| Governance instruments (binding, soft or draft class) | 1,346; embodied 743; robot-specific 647; binding and embodied 294 |
| Effect on the study (v2 to v3) | embodied instruments 65 to 808; robot-specific 34 to 681; binding embodied 5 to 299; jurisdictions with an embodied instrument 30 to 60; coverage audit 12 to 31 of 38 |

Everything ran inside one Claude Code session on 30 October 2026 (about 4.5 hours wall-clock from brief to delivery), with nine collector agents, one text-acquisition agent, three narrative writers and one numbers auditor as subagents.

## 2. Layout

```
/home/user/collection-round-2/            round-2 workspace (copied into the v3 package as collection_round2/, minus texts, raw, texts_agent, logs, annotations)
  CANDIDATE_SCHEMA.md                     17-column candidate schema and inclusion rules (give this to every collector)
  COLLECTOR_REPORTS.md                    condensed final reports of the nine collectors and the standards text agent
  existing_documents.csv / existing_instruments.csv   round-1 holdings used as the exclusion list (title/URL)
  candidates/<AGENT>.csv                  US, EU, EN, AS, AP, ML, ST, IG, MW (agents) and API_<source>.csv (harvesters)
  candidates_merged.csv                   merged, filtered, de-duplicated candidates with stable ids R2-<md5(url)[:8]>
  fetch_status.csv                        one row per fetched doc_id: url actually used, HTTP status, bytes, words, note
  texts/<doc_id>.txt, raw/<doc_id>.pdf    fetched texts (not redistributed) and raw PDFs
  texts_agent/ST-xxx.txt, _standards_log.csv   scope/abstract texts collected by the standards agent for blocked catalogue pages
  data/registry.csv, data/text_features.csv    registry rows in the v2 annotator format; ids_with_text*.txt = annotation batches
  annotations/round2/R2-*.json (+ _inputs/)    one JSON per document with model, prompt hash, policy tag, cost and the exact model input
  scripts/harvest_apis.py                 scripted harvesters (one function per database)
  scripts/merge_candidates.py             schema validation, relevance filter, de-duplication, stable ids
  scripts/fetch_texts.py                  fetch + convert with host routing and fallbacks
  scripts/build_registry.py               registry + language/word features; agent-abstract fallback
  scripts/04_annotate_r2.py               copy of v2 04_annotate.py pointed at this workspace (same codebook, schema, policy)
  scripts/incremental.sh <tag>            merge -> fetch -> registry -> annotate only the new texted ids
/home/user/embodied-ai-governance-v3/     v3 project (copy of v2 plus round 2)
  scripts/merge_round2.py                 appends round-2 registry rows, text features and annotations; writes data/round2_inventory.csv
  scripts/07_assemble.py                  loads annotations/round2/R2-*.json (glob fixed in v3); collector-code fallback accepts INT/EU
  scripts/07b_apply_overrides.py          second pass (identical normalised title + jurisdiction, year within 1) and third pass (cross-round fuzzy + act-number rule)
  scripts/21_round2_report.py             tables T50-T60, figures F50-F52, report/src/collection_round2.md, results.json round2_* keys
  scripts/run_v3.sh / run_v3_post.sh / run_v3_figs.sh / run_v3_cov.sh   pipeline runners
  data/round2_inventory.csv               every candidate with fetch outcome, text status, content_analysed flag, study region
```

## 3. Discovery sources, exactly as used

### 3.1 Scripted database harvests (`scripts/harvest_apis.py`)

All functions write `candidates/API_<name>.csv` in the candidate schema. `get()` retries with back-off. Yields are candidates after merge -> texts -> usable -> embodied instruments (from T50).

| Source | Endpoint and query | Yield | Notes and gotchas |
|---|---|---|---|
| EUR-Lex by title (`eurlex`) | CELLAR SPARQL `https://publications.europa.eu/webapi/rdf/sparql`, `?format=json`; `cdm:expression_title` CONTAINS each keyword (25 keywords: robot, unmanned aircraft, drone, automated driving/vehicle/lane, autonomous vehicle, driver assistance, lane keeping, remotely piloted, machinery, toy safety, product liability, medical devices, lifts, emergency braking, unmanned, vehicle automation, artificial intelligence, cyber resilience, general product safety, u-space, type-approval of motor vehicles, autonomous weapon, lethal autonomous), resource types REG/DIR/DEC (+IMPL/DEL), RES, RES_EP, PROP_REG, PROP_DIR, COM, RECO, REC; LIMIT 400 per keyword | 265 -> 251 -> 251 -> 43 | eur-lex.europa.eu serves a bot challenge; text comes from CELLAR `https://publications.europa.eu/resource/celex/<CELEX>` with `Accept: application/xhtml+xml`, falling back to `application/pdf` then `text/html` on 404 (old acts, EP positions). HTTP 300 lists manifestations: pick the ENG link. Corrigenda `R(nn)` and sectors 6/7/9 dropped. Low precision (16%) because generic terms (machinery, medical devices, AI) pull general acts; the annotator sorts them. |
| EUR-Lex by EuroVoc concept (`eurovoc`) | same endpoint; `?work cdm:work_is_about_concept_eurovoc <http://eurovoc.europa.eu/{id}>` for ids 3740 robotics, 3848 industrial robot, c_05303ddd autonomous vehicle, c_681e6d24 drone, 3030 artificial intelligence; LIMIT 1000 | 256 -> 224 -> 222 -> 48 | Concept ids found with `?c skos:prefLabel "robotics"@en`. Filter out merger notifications, non-opposition notices, state aid, calls for proposals, vacancy notices, parliamentary questions. Topic tagging is independent of title wording, so this catches acts the title search misses. |
| legislation.gov.uk (`uk`) | `https://www.legislation.gov.uk/title/<keyword>/data.csv?page=N` (15 keywords); columns are TITLE, LINK, DocumentMainType, YEAR; skip EuropeanUnion* types | 46 -> 37 -> 37 -> 10 | Text: append `/data.xml` to the item URL (HTML pages are thin). |
| Japan e-Gov law API v2 (`japan`) | `https://laws.e-gov.go.jp/api/2/keyword?keyword=<kw>` full-text search (9 Japanese keywords: 特定自動運行, 無人航空機, 遠隔操作型小型車, 産業用ロボット, 自動運転, ロボット, 自動運行装置, 介護ロボット, ドローン); law text `https://laws.e-gov.go.jp/api/2/law_data/<law_id>` | 64 -> 64 -> 64 -> 26 | Returns JSON/XML; strip tags. Full-text search, so no title filter; 100% fetch success. |
| gov.cn State Council policy library (`govcn`) | `https://sousuo.www.gov.cn/search-gov/data?t=zhengcelibrary_gw|zhengcelibrary_bm&q=<kw>&searchfield=&p=&n=50&type=gwyzcwjk` (12 Chinese keywords: 人形机器人, 具身智能, 机器人, 自动驾驶, 无人驾驶航空器, 智能网联汽车, 无人机, 低空经济, 养老机器人, 手术机器人, 工业机器人, 服务机器人); results in `searchVO.listVO` | 192 -> 188 -> 178 -> 27 | `searchfield=title` returns null; use empty. Article body is in `#UCAP-CONTENT`. CJK texts fail a word-count thinness test: use `words>=80 or cjk_chars>=400`. |
| Federal Register of Legislation, Australia (`australia`) | OData `https://api.prod.legislation.gov.au/v1/titles?$filter=contains(tolower(name),'<kw>')&$top=200` (9 keywords) | 38 -> 38 -> 38 -> 34 | Highest precision of the harvests (CASA instruments, UA levy acts, vehicle standards). `isInForce` and `collection` fields give status and type. |
| US eCFR (`ecfr`) | search `https://www.ecfr.gov/api/search/v1/results?query="<phrase>"&per_page=100&page=N` with quoted phrases (20 phrases), aggregated to parts; text `https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-<T>.xml?part=<P>` (requests must accept gzip) | 55 -> 55 -> 53 -> 18 | The first version used unquoted queries (word-level OR matching) and the `ecfr.gov/current/...` pages, which return an access-denied page to crawlers: 193 useless candidates had to be purged (delete texts, JSONs, fetch_status rows, queued ids). Keep a part only if a strong phrase hit it and either the title is in a plausible list (14, 49, 21, 29, 47, 15, 32, 33, 46, 48, 23, 16, 10, 19, 31, 22, 40, 24, 28, 6, 8, 2) or it has 3+ section hits or a robot/vehicle/aircraft word in the heading. |
| Brazil Câmara dados abertos (`brazil`) | `https://dadosabertos.camara.leg.br/api/v2/proposicoes?keywords=<kw>` (15 Portuguese keywords) | 2 -> 1 -> 1 -> 1 | Keyword search is unreliable; the Latin America collector did the real work from Senado/Câmara pages. LexML (SRU) and planalto.gov.br are behind JavaScript bot checks. |
| Switzerland Fedlex (`fedlex`) | SPARQL on fedlex.admin.ch | 93 rows, dropped at merge | Hits are Federal Gazette items behind a JS app; Switzerland was covered by the continental collector instead. |
| Korea law.go.kr (`korea`) | open API needs a registered OC key; HTML search is JavaScript | 0 | Left to the East Asia collector, who used law.go.kr pages with WebFetch (17 of its URLs still failed to fetch for the pipeline). |

Probed and rejected (do not retry without a browser or an API key): GovInfo and regulations.gov with DEMO_KEY (rate-limited/no response), Federal Register API (no response through the proxy), FAOLEX, NATLEX and OECD STIP Compass (Cloudflare challenge), New Zealand legislation (bot challenge 202), Taiwan law.moj.gov.tw English search (error page), KLRI English law search (404 on the guessed path), droneregulations.info (301 loop), openstd.samr.gov.cn detail pages (connection reset through the proxy; the list page returns 301).

### 3.2 Collector agents (nine, in parallel, `general-purpose` subagents)

Briefs follow one template (the US brief is reproduced verbatim in Appendix A; the structure is):

1. Role and scope: "legal-research collector building a candidate list of GOVERNANCE INSTRUMENTS for embodied AI ... in <region or theme>"; target row count (100 to 200).
2. Read first: `CANDIDATE_SCHEMA.md` and `existing_instruments.csv` (exclusion list; grep by title words).
3. Scope and ideas: an explicit, long list of instruments and instrument families the agent should look for (named statutes, rule numbers, known trackers), so the agent does not rely on search for the obvious items.
4. How to work: WebSearch (standard, extended for hard items) and WebFetch for discovery; `curl -sL -A "Mozilla/5.0" <url>` for verification; a list of hubs (NCSL, IIHS, Law Library of Congress, govinfo, Federal Register API, state legislature sites); the rule that every `url_primary` must resolve; confidence levels high/medium/low.
5. Deliverable: `candidates/<PREFIX>.csv`, ids `<PREFIX>-001...`, schema-exact, written in batches so partial work survives; a 10-line final summary with breakdowns and what could not be found.

Regions and themes: US (federal/state/city), EU+UK+Ireland+Nordics, continental European national, East Asia incl. Chinese provinces, South/Southeast Asia and Oceania, Middle East+Africa+Latin America+Canada, technical standards (ISO/IEC, IEEE, SAE, UL, ASTM, BSI, national), intergovernmental+military+national robotics strategies (CCW/LAWS, UN, NATO, REAIM, national defence AI policies), medical+workplace+consumer+care robots (FDA/MFDS/MHLW guidance, OSHA/DGUV/INRS/KOSHA, toy and companion rules, delivery-robot municipal rules).

Yields (candidates -> texts -> usable -> embodied instruments): ST 244/231/231/202; US 176/131/85/60; IG 148/115/79/37; AS 146/73/71/59; EU 102/77/75/43; ML 97/68/66/43; AP 95/64/63/35; EN 85/46/45/34; MW 64/53/52/23. Confidence as recorded by the collectors across the merged inventory: high 977, medium 1,008, low 90; 88 jurisdiction codes.

Important operating facts learned:
- The web-search budget is shared across concurrent agents (200 searches per turn). With nine collectors it ran out roughly 15 to 45 minutes into every brief; all agents then fell back to official databases, site listings and direct fetches. For a round 3, stagger collectors or give each an explicit search allocation and a longer list of database endpoints that need no search.
- Agents that were given concrete endpoints (NPC law database API `flk.npc.gov.cn`, SAMR standards platform, e-Gov API, law.go.kr, Sejm ELI API, Legilux SPARQL, RIS open-data API, Câmara/Senado APIs, UNODA library, committees API for UK Parliament) produced the most rows after the search budget died.
- Ask collectors to include medium/low-confidence rows with the official URL rather than dropping them; the fetch step and the blind annotation decide.
- A separate text-acquisition agent for blocked catalogue pages (standards) is worth it: 201 scope/abstract texts in 28 minutes, written as `texts_agent/<candidate_id>.txt` with a header (TITLE, DESIGNATION, ISSUER, YEAR, STATUS, SOURCE_URL) then ABSTRACT/SCOPE. In the end most ISO pages were fetched directly through `committee.iso.org` once the host-blocking bug was fixed, so only 16 agent texts were used.
- Send a wrap-up message (`SendMessage`) with a deadline when a collector overruns; all five late collectors delivered within 10 to 15 minutes of it.

### 3.3 What was looked for and not found

`COLLECTOR_REPORTS.md` lists, per region, the instruments the agents could not locate or verify (for example Korea's 2008 Intelligent Robots Act text, provincial Chinese humanoid action plans, CAAC drone rules, NMPA surgical-robot guidance, Lithuanian/Latvian/Romanian/Bulgarian AV provisions, Indian state drone policies, North and West African drone rules, Chilean AV regulation, ANSI/RIA R15.06 and R15.08). The coverage audit still misses 7 of 38 reference instruments: Korea Intelligent Robots Act (2008), EU Product Liability Directive 2024/2853, ANSI/RIA R15.06, ANSI/A3 R15.08, Korea AI Basic Act, OECD AI Principles, Taiwan Industrial Robot Hazard Prevention Standards. These are the first targets for a round 3.

## 4. Merge and de-duplication (`scripts/merge_candidates.py`)

1. Concatenate every `candidates/*.csv` (python engine, bad lines skipped); require a title and a `url_primary`; drop `API_fedlex.csv` and CELEX corrigenda.
2. Relevance filter only for title-searched harvests (`API_eurlex`, `API_uk`, `API_fedlex`, `API_australia`): keep titles matching the inclusion regex (robot, humanoid, unmanned, drone, remotely piloted, automated driving/vehicle/lane/valet, autonomous vehicle/driving/car/ship/vessel/weapon/system/mobile/machine, driver assistance, self-driving, driverless, lane keeping, emergency braking, machinery, surgical, exoskeleton, lethal autonomous, toy safety, product liability, medical device, cyber resilience, general product safety, u-space, type-approval, automatic lane, vehicle automation, automated system, machine safety, industrial truck, lift, plus Japanese, Chinese and Korean terms) and not the exclusion regex (anti-dumping, countervailing, concentration, merger, written question, customs, tariff, import, export licence, state aid, appointment, vehicle registration data exchange, fisheries, Automated Information Exchange, Autonomous Community/region/province/Republic). The exclusion regex applies to every source. Full-text-searched harvests and collector rows are not title-filtered; the annotation judges them.
3. Normalise: titles NFKC, lower-case, parentheticals removed, punctuation stripped, leading articles dropped; URLs lower-case without scheme, `www.`, fragment or trailing slash.
4. De-duplicate within the round on `url_key`, then on `title_key + jurisdiction`; against round 1 on URL or on normalised title (length 20+) against `existing_documents.csv` (title_en and title_clean).
5. Assign `doc_id = "R2-" + md5(url_key)[:8]`, stable across re-runs so incremental fetching and annotation work.
6. The v3 assembly adds two more passes (`07b_apply_overrides.py`): identical normalised title within the same jurisdiction with years within one (keep the fullest capture; 119 removed, 78 of them round-2 rows), and a cross-round pass that removes a round-2 document when a round-1 document has token-sort similarity 90+ with a length ratio of at least 0.6 (both titles 30+ characters) or the same EU act number at the head of both titles with neither being an amendment, opinion, guideline or report about the act (2 removed: the AI Act CELEX capture and a CDC page). An earlier token-set version of this rule wrongly matched 69 distinct documents to short generic round-1 titles ("Artificial Intelligence"); always inspect `data/duplicates_removed.csv` after changing it.

## 5. Text acquisition (`scripts/fetch_texts.py`)

- Thread pool of 6; `fetch_status.csv` is incremental (ids already present are skipped, whatever their status), so to retry failures delete their rows first (`fetch_status_before_retry.csv` keeps the previous state).
- Candidate URL order: secondary CELLAR before eur-lex; legislation.gov.uk gets `/data.xml`; `uri=CELEX:` links are rewritten to CELLAR; undocs.org and UNODA library links are rewritten to the UN document API `https://documents.un.org/api/symbol/access?s=<SYMBOL>&l=E` (symbol parsed from the URL path or the `CCW-GGE.1-2025-WP.9` style filename); blocked hosts are skipped by exact host name (substring matching once hid the reachable `committee.iso.org` mirror behind `iso.org`).
- Conversion: PDF via `pdftotext -layout`; e-Gov JSON/XML and legislation.gov.uk XML by tag stripping; HTML via BeautifulSoup after removing script/style/nav/header/footer/forms, preferring `#UCAP-CONTENT`, `.pages_content`, `main`, `article`; thinness rule `words >= 80 or cjk >= 400`.
- Hosts that block the sandbox (keep in `BLOCKED`): www.iso.org, ncsl.org, unece.org, legifrance.gouv.fr, sso.agc.gov.sg, docs-library.unoda.org (use the UN API), icao.int, osha.gov, loc.gov, bcn.cl, openstd.samr.gov.cn. Also failing in practice: flk.npc.gov.cn (27), law.go.kr (17), law.moj.gov.tw (11), faa.gov, fedlex, senado.leg.br, openstates, most defence.gov hosts, sae.org (JS shell; use saemobilus.sae.org/content/<id>), jisc.go.jp (502).
- `build_registry.py` copies `texts_agent/<candidate_id>.txt` to `texts/<doc_id>.txt` when no fetched text exists (status `agent_abstract`), so standards annotated on scope text are flagged in the registry (`meta_how`).

## 6. Annotation

`python3 scripts/04_annotate_r2.py --ids data/ids_with_text_<ts>.txt --out annotations/round2 --workers 3 --head 100000 --mid 6000 --tail 4000 --blind --policy v2` per batch (`incremental.sh` creates the batch from texted ids not yet annotated or queued). Model `claude-sonnet-5-5` through the Claude Code CLI in non-interactive mode (`claude -p --no-session-persistence --tools "" --system-prompt <codebook> --json-schema <schema> --output-format json`), prompt passed on stdin, prompt hash `8d4d83e909f0`, policy tag `v2|head=100000|mid=6000|tail=4000|blind=True`, inputs stored under `_inputs/`. Cost about 0.07 USD per document; 1,732 files produced (16 orphans from purged eCFR ids). Several batches can run concurrently (three workers each); they never annotate the same id because batch files exclude queued ids.

## 7. Integration into v3 and checks

Order: `merge_round2.py` -> `05_lexicons.py` (cached by doc_id + text length) -> `07_assemble.py` -> `07b_apply_overrides.py` -> `09_reliability.py` x5 -> 13/14/15/18/19/17/20 -> `21_round2_report.py` -> `10_dashboard.py` -> `11_stage1_report.py` -> `16_build_reports.py` (`run_v3.sh`). After a change to 07b use `run_v3_post.sh`; after a figure-title change `run_v3_figs.sh`.

Checks that caught real errors and should be repeated:
- Inspect `data/duplicates_removed.csv` after any de-duplication change (see section 4).
- Figure headlines in `20_figures_v2.py` and `18_analysis_D.py` were hard-coded v2 claims; v3 computes them from the data. Any new figure title must be computed or neutral.
- Definitions must nest: robot-specific instruments are `instrument & embodied_set & relevance >= 2` (12 instruments rated `not_ai` with relevance 2 caused a 689 vs 681 inconsistency between T53 and T33 until fixed).
- The coverage audit matches reference instruments by title regex; two US executive orders were in the collection but unmatched until the patterns included their titles (10/29 became 12/31 of 38). Check `data/reference_instruments.csv` patterns against actual titles whenever the collection changes.
- An independent numbers audit (a subagent recomputing every quantitative sentence from the master table and tables) found 24 issues in the brief and paper and 18 in the report and supplement; all were fixed and logged in `review/v3_changes_*.md` and `review/v3_numbers_audit_*.md`. Run it before delivery.
- Collector metadata vs blind annotation (T57): binding nature 92.7% agreement (kappa 0.85), jurisdiction 98.1%, year within one 93.3%, document class 80.2% (kappa 0.71). Disagreements are concentrated in guidelines labelled binding by annotators (51 of 280) and strategies/consultations read as news.

## 8. How to run a round 3

1. Copy this workspace layout; regenerate `existing_documents.csv` and `existing_instruments.csv` from the v3 master table (all documents, and governance documents plus reports) so the exclusion lists include round 2.
2. Re-run the harvesters with new keywords or concepts (EuroVoc candidates not yet used: "unmanned aircraft", "automation", "machinery", "artificial intelligence" sub-concepts; CELLAR also supports `cdm:work_is_about_concept_eurovoc` on national transposition measures, sector 7, which were excluded). Add harvesters where an API exists and a key can be supplied through environment secrets: LegiScan or OpenStates (US state bills), GovInfo and regulations.gov (API keys replace DEMO_KEY), law.go.kr open API (registered OC), Congress.gov.
3. Brief collectors per jurisdiction cluster that round 2 under-covered: Chinese provinces (Guangdong, Zhejiang, Jiangsu, Sichuan, Chongqing, Shanghai municipal measures), Korea (MOTIE, MOLIT, KOSHA), Japan (METI, kantei, MOD), India states, Southeast Asia (Thailand, Vietnam, Indonesia, Philippines bills), Gulf states (RAK, Abu Dhabi ITC, Saudi traffic law), North and West Africa, Chile, Mexico, Baltic and Balkan AV and drone rules, Australian states and New Zealand transport rules, US cities. Give each a list of concrete endpoints and ask for medium/low-confidence rows.
4. Give the standards agent the non-ISO catalogues first (IEC webstore, IEEE SA, SAE Mobilus, UL, ASTM, BSI Knowledge, DIN, JIS once jisc.go.jp is reachable, GB via the `newGbInfo?hcno=` detail route through a browser) and the 51 Chinese GB rows that still lack text.
5. For blocked hosts, use a browser-capable path (Claude in Chrome or the built-in browser) or ask the user to add hosts to the environment network allow-list: legifrance, sso.agc.gov.sg, law.go.kr, flk.npc.gov.cn, law.moj.gov.tw, unece.org, icao.int, osha.gov, iso.org, ncsl.org.
6. Then: `incremental.sh <tag>` per batch; `merge_round2.py` and `run_v3.sh` in a copied project folder (v4); re-run the numbers audit; update narratives from the change logs.

## 9. Known limitations to state in any write-up

Candidates without text (359) are inventory only; technical standards are annotated on scope text; search-budget exhaustion made coverage uneven across jurisdictions; title-searched harvests were filtered by keyword and therefore miss instruments whose titles do not name the technology; full-text harvests were limited to the keyword lists above; the annotation is model-based (see the supplement's reliability section); counts are lower bounds within this collection.

## Appendix A. Collector brief used for the United States (verbatim)

The other eight briefs had the same structure with their own scope lists and databases.

```text
You are a legal-research collector building a candidate list of GOVERNANCE INSTRUMENTS for embodied AI (robots, automated/autonomous vehicles, drones, delivery robots, surgical robots, exoskeletons, humanoids, autonomous weapons) in the UNITED STATES (federal, state, and major cities). Goal: as many verified instruments as possible (target 120 to 200 rows). Do not write project files other than those named below.

Read first: /home/user/collection-round-2/CANDIDATE_SCHEMA.md (the exact CSV schema and inclusion rules) and skim /home/user/collection-round-2/existing_instruments.csv (instruments already collected; do not duplicate; grep by title words).

Scope and ideas (be exhaustive and creative):
- Federal statutes and rules: FAA Part 107, the 2024/2025 BVLOS (Part 108) rulemaking, Remote ID rule, FAA Reauthorization Act 2024 UAS provisions; NHTSA: ADS exemption rules (FMVSS 2022 occupant-protection amendments for vehicles without manual controls), Standing General Order 2021-01 on ADS/ADAS crash reporting (and 2023/2025 amendments), AV STEP proposed rule (2025), FMVSS 127 AEB; DOT AV policy documents (AV 4.0, "Automated Vehicles Comprehensive Plan", 2025 AV Framework); FAA/UAS Integration Pilot; OSHA robotics guidance (OSHA Technical Manual Section IV Chapter 4, OSHA-RIA alliance); FDA guidance and classifications for computer-assisted/robotically-assisted surgical devices; DoD Directive 3000.09 (2023) on autonomy in weapon systems; Executive Orders 14179 (2025), 14110 (revoked), 13859, and any 2025 EO on drones ("Unleashing American Drone Dominance", June 2025) and on AI action plan; NIST documents on robotics/AV; Commerce/BIS rules on connected vehicle technology (ICTS rule, Jan 2025) and on Chinese drones; Congress: enacted statutes and major bills (SELF DRIVE Act versions, AV Accessibility Act, Drone Security Act, American Security Drone Act 2023 (enacted in NDAA FY2024), Countering CCP Drones Act, NDAA FY2025 sections on autonomous weapons/robotics), Senate/House committee reports if formal.
- State statutes and regulations: autonomous vehicle laws of every state that has one (NCSL tracker lists ~30+ states; California DMV AV regulations (testing and deployment, 2018, 2025 amendments incl. heavy-duty), Arizona EOs 2015/2018 and statutes, Florida s.316.85, Texas SB 2205, Nevada NRS 482A, Michigan, Georgia, Tennessee, Utah, Pennsylvania (2022 Act 130), Louisiana, North Carolina, Nebraska, Colorado, Washington, etc.); personal delivery device / sidewalk robot statutes (Virginia 2017 first, then ~25 states: Idaho, Wisconsin, Florida, Ohio, Arizona, Utah, Washington, Texas, Pennsylvania, Oklahoma, Tennessee, Kansas, Missouri, etc.); state drone laws (NCSL "Current Unmanned Aircraft State Law Landscape"; pick those with substantive provisions: privacy, law-enforcement use, critical infrastructure, weaponized drones bans (e.g., Oregon, North Carolina), police robot laws); state laws on robot/AI in policing (e.g., restrictions on armed robots: San Francisco 2022 ordinance saga, California AB 1003? "no armed robots" bills), companion/chatbot laws with embodiment (New York 2025 companion law, California SB 243 (2025)), robot/AI in nursing homes, "robot tax" bills, workplace robot/warehouse quota laws (California AB 701 warehouse quotas, New York Warehouse Worker Protection Act), humanoid or robot registration bills (2025 sessions), state DOT truck platooning laws.
- Cities: San Francisco (armed robot policy; AV permits via CPUC), Pittsburgh AV executive order, Boston/NYC drone and delivery-robot rules, Toronto is Canada (skip), Miami-Dade delivery robots, etc.

How to work: use WebSearch (standard mode; extended for hard items) and WebFetch to find and verify; the sandbox can also curl many sites directly (try `curl -sL -A "Mozilla/5.0" <url>` via Bash; ncsl.org and osha.gov are blocked for curl but work in WebFetch). Useful hubs: NCSL AV bill tracking database and PDD pages, IIHS "autonomous vehicle laws" page, Law Library of Congress reports, govinfo.gov, federalregister.gov (API: https://www.federalregister.gov/api/v1/documents.json?conditions[term]=...), state legislature sites, Justia/LegiScan pages. Verify each row's url_primary resolves (WebFetch or curl) and record year, status and type. For state statutes give the statute URL (state code site) or the enrolled bill PDF.

Deliverable: write /home/user/collection-round-2/candidates/US.csv with candidate_ids US-001, US-002, ... following the schema exactly (comma-separated, quote fields containing commas; no blank lines). Work in batches: append rows as you verify them so partial work is saved. When done, reply with a 10-line summary: rows written, breakdown by instrument_type and by federal/state/city, and what you could not find."},"caller":{"type":"direct"}}],"container":null,"stop_reason":"tool_use","stop_sequence":null,"stop_details":null,"usage":{"input_tokens":32,"cache_creation_input_tokens":12686,"cache_read_input_tokens":781847,"output_tokens":25297,"output_tokens_details":{"thinking_tokens":1772},"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":0,"ephemeral_5m_input_tokens":12686},"inference_geo":"global","iterations":[{"input_tokens":32,"output_tokens":25297,"cache_read_input_tokens":781847,"cache_creation_input_tokens":12686,"cache_creation":{"ephemeral_5m_input_tokens":12686,"ephemeral_1h_input_tokens":0},"type":"message"}],"speed":"standard","fallback_credit":null},"input_transformations":[{"type":"thinking_dropped","path":"messages.2.content.0","reason":"prefix_binding_mismatch"}],"diagnostics":null,"context_management":null},"wireToolInputs":{"toolu_01QoA5LHutLB9tdutn27VxST":{"description":"Discover US robot/AV/drone instruments
```
