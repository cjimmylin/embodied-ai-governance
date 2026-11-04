# Collection round 2 and version 3: summary (31 October 2026)

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Version 3 adds a second collection round to the version-2 study of how embodied AI (robots, automated vehicles, drones, medical and industrial machines) is governed. Round 2 searched official legal databases, treaty-body archives, standards catalogues and regulator sites for the instruments the first collection had missed, using nine collector agents and scripted harvests of seven legal databases (EUR-Lex by title and by EuroVoc concept, legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register of Legislation, the US eCFR and the Brazilian Camara API). Candidates were de-duplicated against round 1, fetched from the issuing source, and annotated with the same metadata-blind extended-excerpt policy as version 2.

## Funnel

- Candidates after de-duplication: 2,075
- Text obtained and annotated: 1,716
- Usable captures: 1,611; in the embodied-AI set: 914
- Governance instruments among them: 1,346; in the embodied-AI set: 743; robot-specific: 647; binding and embodied: 294

## Before and after (content-analysed documents only)

| measure                                   |   v2 |   v3 |   added |   ratio |
|:------------------------------------------|-----:|-----:|--------:|--------:|
| Documents (annotated)                     | 1656 | 3291 |    1635 |    1.99 |
| Usable documents                          | 1538 | 3148 |    1610 |    2.05 |
| Embodied-AI set                           |  675 | 1589 |     914 |    2.35 |
| General-AI set                            |  806 |  982 |     176 |    1.22 |
| Governance documents (incl. reports)      |  343 | 1695 |    1352 |    4.94 |
| Governance instruments, all               |  345 | 1691 |    1346 |    4.9  |
| Governance instruments, embodied-AI set   |   65 |  808 |     743 |   12.43 |
| Robot-specific instruments (relevance 2+) |   34 |  681 |     647 |   20.03 |
| Binding instruments, all                  |   34 |  689 |     655 |   20.26 |
| Binding instruments, embodied-AI set      |    5 |  299 |     294 |   59.8  |
| Binding instruments, robot-specific       |    4 |  244 |     240 |   61    |
| Soft-law instruments, embodied-AI set     |   50 |  434 |     384 |    8.68 |
| Proposals and drafts, embodied-AI set     |   10 |   75 |      65 |    7.5  |
| Government reports, embodied-AI set       |   24 |   90 |      66 |    3.75 |
| Jurisdictions with an embodied instrument |   30 |   60 |      30 |    2    |

Coverage audit against the 38 reference instruments: 12 captured in v2, 31 in v3. Still missing: Korea Intelligent Robots Development and Distribution Promotion Act (2008); EU revised Product Liability Directive (EU) 2024/2853; ANSI/RIA R15.06 industrial robot safety; ANSI/A3 R15.08 industrial mobile robots; Korea AI Basic Act (2024/2025, applies Jan 2026); OECD AI Principles (2019, rev. 2024); Taiwan Industrial Robot Hazard Prevention Standards.

## Fetch outcomes

| outcome                          |   candidates |
|:---------------------------------|-------------:|
| text: fetched                    |         1700 |
| no text: HTTP error or thin page |          273 |
| no text: host blocks the sandbox |           46 |
| no text: fetch failed            |           40 |
| text: scope/abstract via mirror  |           16 |

Candidates without text stay in the inventory (data/round2_inventory.csv) with their metadata and are counted nowhere.

## Where the candidates came from

| source                                                            | kind                      |   candidates |   text_obtained |   content_analysed |   usable |   embodied |   instruments |   embodied_instruments |
|:------------------------------------------------------------------|:--------------------------|-------------:|----------------:|-------------------:|---------:|-----------:|--------------:|-----------------------:|
| EUR-Lex (CELLAR SPARQL, title search)                             | scripted database harvest |          265 |             251 |                251 |      251 |         43 |           249 |                     43 |
| API_eurovoc                                                       | scripted database harvest |          256 |             224 |                224 |      222 |         70 |           131 |                     48 |
| Collector: technical standards (ISO/IEC, IEEE, SAE, UL, national) | collector agent           |          244 |             231 |                231 |      231 |        203 |           230 |                    202 |
| gov.cn State Council policy library (full-text)                   | scripted database harvest |          192 |             188 |                188 |      178 |         27 |           178 |                     27 |
| Collector: United States federal and state                        | collector agent           |          176 |             131 |                131 |       85 |         71 |            70 |                     60 |
| Collector: intergovernmental, military and strategies             | collector agent           |          148 |             115 |                115 |       79 |         76 |            37 |                     37 |
| Collector: East Asia incl. Chinese provinces                      | collector agent           |          146 |              73 |                 73 |       71 |         68 |            60 |                     59 |
| Collector: EU, UK, Ireland, Nordics                               | collector agent           |          102 |              77 |                 77 |       75 |         65 |            49 |                     43 |
| Collector: Middle East, Africa, Latin America, Canada             | collector agent           |           97 |              68 |                 68 |       66 |         63 |            43 |                     43 |
| Collector: South/Southeast Asia and Oceania                       | collector agent           |           95 |              64 |                 64 |       63 |         59 |            36 |                     35 |
| Collector: continental European national                          | collector agent           |           85 |              46 |                 46 |       45 |         38 |            39 |                     34 |
| Japan e-Gov law API (full-text search)                            | scripted database harvest |           64 |              64 |                 64 |       64 |         26 |            64 |                     26 |
| Collector: medical, workplace, consumer and care robots           | collector agent           |           64 |              53 |                 53 |       52 |         42 |            31 |                     23 |
| eCFR (US Code of Federal Regulations search)                      | scripted database harvest |           55 |              55 |                 55 |       53 |         18 |            53 |                     18 |
| legislation.gov.uk (title search)                                 | scripted database harvest |           46 |              37 |                 37 |       37 |         10 |            37 |                     10 |
| Federal Register of Legislation (AU)                              | scripted database harvest |           38 |              38 |                 38 |       38 |         34 |            38 |                     34 |
| Brazil Camara dados abertos                                       | scripted database harvest |            2 |               1 |                  1 |        1 |          1 |             1 |                      1 |
| All sources                                                       | nan                       |         2075 |            1716 |               1716 |     1611 |        914 |          1346 |                    743 |

## What changed in the findings (details in the change logs)

- Binding rules that reach robots are no longer rare in the collection: 299 binding instruments in the embodied set (5 in v2), 265 of them governing drones or automated road vehicles; El Salvador's Robotic Technologies Law remains the only national law written for robots as such.
- The research-versus-governance gap persists for companion and care robots and reverses for drones and vehicles; the industrial-robot gap is no longer significant.
- Robot rules lean on technical standards, conformity assessment and licensing; general-AI rules on audits, labelling and data governance. Core ethical principles are now less frequent in robot documents even within genre, reversing a v2 claim.
- Regions differ on tools and, in v3, on values; Europe and North America are now distinguishable but remain nearest neighbours.
- The v2 trend claims about cybersecurity and human oversight do not hold in v3; the fall of the robot-personhood debate does.

## Limitations specific to round 2

Every collector's shared web-search budget was exhausted part-way through its brief; 46 candidates sat on hosts the sandbox cannot reach and 273 returned errors or script-only pages; technical standards are annotated on their public scope text only; the inventory items without text are not counted. The collector reports list what was looked for and not found, jurisdiction by jurisdiction.

## Deliverables

Dashboard (v3): https://claude.ai/artifact/MJhHXAtHcJqTVXRVzjxCjH. Package: embodied-ai-governance-v3.zip (reports, figures, tables, master table, inventory, annotations, scripts, collection round-2 workspace).
