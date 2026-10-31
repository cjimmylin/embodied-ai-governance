---
title: "Document discovery and inclusion in version 3: methods"
subtitle: "How the second collection round found, verified, de-duplicated, acquired and admitted governance instruments"
author: "Centre for Enterprise Innovation (CEI) AI Robotics project, with Claude Code"
date: "31 October 2026"
---

## 1. Rationale and design

Version 2 of the study rested on a collection assembled by eight regional teams in two exercises: a *sprint* for robot-specific sources and a *database* of general AI-governance instruments. Its coverage audit showed the limitation of that design for the question the study asks: of 38 reference instruments known to govern robots, drones or automated vehicles, only 12 had been captured as documents, and the collection held 65 governance instruments in the embodied-AI set, 5 of them legally binding. The instruments that bind robots in practice (aviation rules, road-traffic law, machinery and product-safety law, workplace-safety rules, technical standards) are catalogued in legal databases that are rarely surfaced by topical web search, and they are spread across many jurisdictions and languages.

The second collection round therefore inverted the search strategy. Instead of asking regional teams to search the web for material *about* embodied AI, it (a) queried official legal databases and catalogues programmatically for instruments whose text or subject tags name the technologies, and (b) briefed nine specialised collector agents to work from legal repositories, treaty archives, standards catalogues and regulator sites with explicit lists of the instruments and instrument families to look for. Discovery was separated from judgement: every candidate that could be fetched was annotated by the same metadata-blind procedure as the rest of the collection, and only the annotation decides whether a document is an instrument, whether it concerns embodied AI, and how it is classified. Candidates that could not be fetched are recorded in an inventory and are not counted anywhere.

## 2. Sources

### 2.1 Scripted harvests of legal databases

Seven databases were harvested by script (eight runs; `collection_round2/scripts/harvest_apis.py`). Each harvester returns rows in the common candidate schema (section 3).

- **EUR-Lex through the CELLAR SPARQL endpoint**, in two ways: (i) a title search over the English expression titles of regulations, directives, decisions (including implementing and delegated acts), resolutions, proposals, communications and recommendations, using 25 terms covering robots, unmanned aircraft and drones, automated and autonomous driving, driver assistance, machinery, toy safety, product liability, medical devices, lifts, cyber resilience, general product safety, U-space, type-approval, autonomous and lethal autonomous weapons, and artificial intelligence; (ii) a subject search for every work tagged with the EuroVoc concepts *robotics*, *industrial robot*, *autonomous vehicle*, *drone* and *artificial intelligence*, which is independent of title wording. Corrigenda, case law, national transposition measures, parliamentary questions and administrative notices (merger notifications, state aid, vacancies) were excluded.
- **legislation.gov.uk**, title search over 15 terms (automated vehicles, unmanned aircraft, drone, robot, autonomous, air navigation, product safety, machinery, vehicle technology, self-driving, remotely piloted, toy safety, medical devices), excluding retained EU instruments.
- **Japan's e-Gov law API**, full-text search with nine Japanese terms (specified automated operation, unmanned aircraft, remotely operated small vehicles, industrial robots, automated driving, robots, automated operation devices, care robots, drones), returning the consolidated law text.
- **China's State Council policy library** (gov.cn), full-text search with twelve Chinese terms (humanoid robots, embodied intelligence, robots, automated driving, unmanned aircraft, intelligent connected vehicles, drones, low-altitude economy, elderly-care robots, surgical robots, industrial robots, service robots).
- **Australia's Federal Register of Legislation** (OData API), title search with nine terms.
- **The US Code of Federal Regulations** (eCFR search API), quoted-phrase searches for twenty terms aggregated to the level of a CFR part, retaining parts in titles where such rules plausibly live or with several matching sections, and retrieving the part text through the versioner API.
- **Brazil's Câmara dos Deputados open-data API**, keyword search in Portuguese (low yield; the Latin America collector covered Brazil from the Senate and Chamber sites instead).

Harvests of the Swiss Fedlex gazette and the Korean law portal were attempted and dropped (JavaScript-only pages and a registration-only API respectively). Several further databases could not be reached from the execution environment (GovInfo and regulations.gov without an API key, the Federal Register API, FAOLEX, NATLEX, OECD STIP Compass, New Zealand legislation, Taiwan and Korean English law portals).

### 2.2 Collector agents

Nine collector agents ran in parallel, each with a written brief that stated the scope, the target number of rows, the candidate schema, the list of round-1 holdings to exclude, a long enumeration of instruments and instrument families to look for in that scope, the databases and hubs to use, and the rule that every primary URL must have been verified to resolve. The scopes were: the United States (federal, state and city); the European Union, the United Kingdom, Ireland and the Nordic countries; continental European national instruments; East Asia including Chinese provinces and municipalities; South and Southeast Asia and Oceania; the Middle East, Africa, Latin America and Canada; technical standards (ISO/IEC, IEEE, SAE, UL, ASTM, BSI and national bodies); intergovernmental, military and national-strategy instruments (the CCW process on lethal autonomous weapons, UN resolutions and reports, NATO, REAIM, national defence AI policies, national robotics strategies); and medical, workplace, consumer and care-robot rules (medical-device guidance, occupational-safety rules on industrial and collaborative robots, toy and companion-robot rules, municipal delivery-robot rules). A tenth agent collected the public scope or abstract text of standards whose catalogue pages block automated access.

Agents used web search for discovery while a shared search budget lasted (it was exhausted part-way through every brief) and thereafter worked from official databases and site listings (for example the National People's Congress law database, the SAMR standards platform, law.go.kr, the Sejm and Legilux legal-data interfaces, the UK Parliament committees API, the UNODA document library, Senate and Chamber open-data APIs). Each agent returned a schema-exact CSV written in batches and a report listing what it had looked for and could not find; those reports are reproduced in condensed form in the package (`collection_round2/COLLECTOR_REPORTS.md`) because they bound what the round can claim.

## 3. Candidate schema and verification

Every candidate row carries 17 fields: identifier; original and English titles; jurisdiction (ISO 3166-1 alpha-2, EU or INT) and subnational unit; issuer; year; instrument type (13 values from statute to court decision); binding nature (legally binding, voluntary soft law, voluntary or mandated technical standard, not applicable); lifecycle status (eight values); robot types addressed (from the study's 23-category taxonomy); language; primary and secondary URLs; the source database; a confidence level (high if verified at the primary URL, medium if verified through a secondary source, low if inferred); and a one-line note. The inclusion rule was governance instruments only (laws, regulations, bills, standards, strategies, official guidelines, resolutions, formal national positions, official reports), one row per instrument, preferring instruments with substantive provisions on physical AI. Collectors were asked to include medium- and low-confidence rows with their official URL rather than omit them. Across the merged inventory, 977 rows were recorded as high confidence, 1,008 as medium and 90 as low.

## 4. Merging and de-duplication

Candidate files were merged with a fixed procedure (`merge_candidates.py`). Rows without a title or a primary URL were dropped, as were the Fedlex gazette hits and EUR-Lex corrigenda. For the title-searched harvests only (EUR-Lex by title, legislation.gov.uk, Fedlex, Australia), a keyword relevance filter kept titles naming the technologies or the relevant product-safety regimes and removed administrative noise (anti-dumping, customs, mergers, state aid, appointments, autonomous-region place names); full-text harvests and collector rows were not filtered by title, so that the annotation, not a keyword list, judges them. Titles were normalised (Unicode NFKC, case, parentheticals, punctuation, leading articles) and URLs canonicalised (scheme, `www`, fragment, trailing slash). Duplicates were removed within the round on URL and then on normalised title plus jurisdiction, and against the round-1 collection on URL or on normalised title of at least 20 characters. Each surviving candidate received a stable identifier derived from its canonical URL, so that re-runs added only new rows. The merged inventory holds 2,075 candidates: 1,157 from collector agents and 918 from scripted harvests, across 88 jurisdiction codes.

Two further de-duplication passes run when the round-2 documents are assembled with the round-1 documents into the master table: documents with an identical normalised title in the same jurisdiction and years within one are merged (the fullest capture is kept; 119 rows, 78 of them from round 2), and a round-2 document is removed when a round-1 document has a token-sort title similarity of at least 90 with comparable length, or when both titles open with the same EU act number and neither is an amendment, opinion, guideline or report about the act (2 rows: the AI Act captured again from EUR-Lex, and a duplicate web page). A looser similarity rule tried first would have removed 69 distinct documents by matching them to short generic round-1 titles; every removal is listed in `data/duplicates_removed.csv`. In all, 79 round-2 rows were removed in assembly and 1,637 entered the master table.

## 5. Text acquisition

Texts were fetched from the primary URL with the secondary URL as fallback (`fetch_texts.py`), with routing rules for sources that block or mis-serve automated clients: EUR-Lex links are resolved through the Publications Office's CELLAR service (XHTML, falling back to PDF or HTML for older acts); UN and UNODA links are resolved through the UN document API by document symbol; legislation.gov.uk items are read as XML; ISO catalogue pages are read from the ISO committee mirror; hosts that reject the execution environment are skipped by exact host name. PDFs were converted with pdftotext; HTML with a content-area extractor; Japanese and British XML by tag stripping. A text was accepted when it had at least 80 words or 400 CJK characters. Where a standards catalogue page could not be fetched, the scope or abstract text collected by the standards agent was used instead and flagged in the registry.

Text was obtained for 1,716 candidates (1,700 fetched, 16 standards scope texts). The 359 candidates without text (273 HTTP errors or script-only pages, 46 on hosts that block the environment, 40 failed transfers) remain in the inventory with their metadata. The hosts accounting for most losses were eur-lex.europa.eu for items with no English expression, the National People's Congress law database, the UNODA library for documents without a UN symbol, Légifrance, the Korean and Taiwanese law portals, and the US FAA and OSHA sites.

## 6. Annotation and inclusion

Every fetched text was annotated with the procedure used for the version-2 governance documents: the 39-field codebook, a fixed JSON schema, Claude Sonnet 5.5 through the Claude Code command-line interface, the collector's cover block stripped and only minimal metadata shown, and an extended excerpt of up to 110,000 characters (the first 100,000, 6,000 from the middle, 4,000 from the end). The model, prompt hash, excerpt policy, cost and the exact input are stored with each annotation. Annotation cost about 125 US dollars for the round.

Inclusion in the analysis then follows the study's standing definitions: a document is *usable* if its text was obtained and the annotation did not judge the capture to be an error page or otherwise unusable (1,611 of the 1,637 round-2 documents in the master table); it belongs to the *embodied-AI set* if it is rated at least moderately relevant to embodied-AI governance or carries a robot-type label and is not judged to be unrelated to AI (914); it is a *governance instrument* if its document class is binding instrument, soft-law instrument or proposal/draft (1,346; 743 in the embodied set); it is *robot-specific* if it is an embodied-set instrument rated at least moderately relevant (647); and it is *binding* if its class is binding instrument (294 in the embodied set). Documents rated as not about AI at all, mostly harvested legal texts in which the technology terms appear incidentally, fall outside both analysis sets.

## 7. Quality checks

Three checks bear on discovery and inclusion. First, the collectors' catalogue metadata were compared with the blind annotation of the text for the 1,611 usable round-2 documents: agreement was 92.7% on whether an instrument is legally binding (kappa 0.85), 98.1% on jurisdiction, 93.3% on year within one, and 80.2% on document class (kappa 0.71), the main disagreements being guidelines that the annotation reads as binding and strategies or consultations that it reads as communications. Second, the coverage audit against the 38 reference instruments was repeated with the merged collection: 31 are now captured as documents (12 in version 2); the seven still missing are the Korean Intelligent Robots Act of 2008, the revised EU Product Liability Directive, the two American industrial-robot standards (ANSI/RIA R15.06, ANSI/A3 R15.08), the Korean AI Basic Act, the OECD AI Principles and the Taiwanese industrial-robot hazard standards. Third, an independent numbers audit recomputed every quantitative statement in the narrative documents from the master table and the tables, and the discrepancies it found (including a definition inconsistency in the robot-specific count and two reference-instrument patterns that failed to match captured executive orders) were corrected and logged.

## 8. Yield by source

| Source | Candidates | Texts | Usable | Embodied instruments |
|---|---:|---:|---:|---:|
| Technical standards collector | 244 | 231 | 231 | 202 |
| EUR-Lex, title search | 265 | 251 | 251 | 43 |
| EUR-Lex, EuroVoc concepts | 256 | 224 | 222 | 48 |
| China State Council policy library | 192 | 188 | 178 | 27 |
| United States collector | 176 | 131 | 85 | 60 |
| Intergovernmental, military and strategy collector | 148 | 115 | 79 | 37 |
| East Asia collector | 146 | 73 | 71 | 59 |
| EU, UK, Ireland and Nordics collector | 102 | 77 | 75 | 43 |
| Middle East, Africa, Latin America, Canada collector | 97 | 68 | 66 | 43 |
| South and Southeast Asia and Oceania collector | 95 | 64 | 63 | 35 |
| Continental European collector | 85 | 46 | 45 | 34 |
| Japan e-Gov law API | 64 | 64 | 64 | 26 |
| Medical, workplace, consumer and care collector | 64 | 53 | 52 | 23 |
| US eCFR | 55 | 55 | 53 | 18 |
| legislation.gov.uk | 46 | 37 | 37 | 10 |
| Australian Federal Register of Legislation | 38 | 38 | 38 | 34 |
| Brazil Câmara API | 2 | 1 | 1 | 1 |
| All sources | 2,075 | 1,716 | 1,611 | 743 |

Precision differs by design: the standards collector and the Australian register yield embodied instruments for most candidates, while the broad EUR-Lex and gov.cn harvests contribute many general-AI or non-AI legal texts that the annotation sets aside. The two strategies are complementary: scripted harvests supplied the bulk of binding EU, Japanese, Chinese, Australian and US federal rules, and the collectors supplied national and subnational instruments, standards and treaty-body material that no single database indexes.

## 9. Limitations of the discovery method

Coverage is bounded by what the execution environment could reach: portals that block automated access (among them Légifrance, the Singapore statutes site, the Korean and Taiwanese law portals, the ISO store, UNECE, ICAO, OSHA) could be cited but not read, and 359 verified candidates therefore remain outside every count. The shared web-search budget was exhausted in every collector brief, so discovery leaned on databases with usable interfaces and under-represents jurisdictions whose instruments are not indexed in such databases. Title-searched harvests depend on the keyword lists given above and miss instruments whose titles do not name the technology; full-text harvests depend on the same vocabulary in the body. Technical standards were annotated on their public scope text rather than the normative text. The collectors' metadata were used only for the agreement check and for the inventory, never for classification, which rests on the model annotation with the reliability documented in the supplement. All counts are lower bounds within this collection.
