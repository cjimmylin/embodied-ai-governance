# Round-3 report: slice C (Americas and international)

59 targets worked; every fetch went through `scripts/r3fetch.py` with the project crawler identification. Outcomes are in `status/agent_C_americas_int.csv`.

## Counts by outcome

| outcome | n |
|---|---|
| saved | 38 |
| saved_partial | 4 |
| blocked | 17 |
| not_found | 0 |
| irrelevant | 0 |

## Blocked targets (URL a person should open)

| id | instrument | URL for a human | why |
|---|---|---|---|
| IG-112 | DoD Directive 3000.09 (2023) | https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/300009p.pdf | esd.whs.mil 403; defense.gov release also 403 |
| ML-032 | UAE Federal Decree-Law 26/2022 (unmanned aircraft) | https://uaelegislation.gov.ae/en/legislations/1587 (PDF: `/download`) | page is a JS shell for the crawler; `/download` 403; GCAA Laws page JS-only |
| ML-033 | UAE Cabinet Resolution 110/2023 (drone products scheme) | https://uaelegislation.gov.ae/en/legislations/2177 | same as ML-032 |
| ML-041 | Saudi GACAR Part 107 v4 | https://gaca.gov.sa/-/media/Files/PDF/LawsAndRegulation/Aviation-Safety-and-Environmental-Sustainability/GACAR-Safety-Regulations/107-v4.pdf | all gaca.gov.sa hosts reset the connection / fail at the proxy |
| ML-096 | Chile DAN 151 | https://www.dgac.gob.cl/ (normativa); amendment in Diario Oficial: https://www.diariooficial.interior.gob.cl/publicaciones/2021/03/05/42897/01/1905323.pdf | DGAC resets the connection; Diario Oficial 403 |
| US-086 | Cal. Veh. Code 38750 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=VEH&sectionNum=38750. | leginfo 403; openstates SB 1298 (2012) timed out twice |
| US-108 | Ind. Code 9-21-11.5 | https://iga.in.gov/laws/2024/ic/titles/9#9-21-11.5 | iga.in.gov returns an empty page to the crawler and to headless Chromium |
| US-109 | Ind. Code 35-33-5-9 | https://iga.in.gov/laws/2024/ic/titles/35#35-33-5-9 | as US-108 |
| US-122 | Michigan SAVE Act (MCL 257.665 et seq.) | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-257-665 | legislature.mi.gov 403 for HTML, PDF and render |
| US-123 | Michigan UAS Act (PA 436 of 2016) | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Act-436-of-2016 | as US-122 |
| US-134 | N.H. RSA 265:163 | https://gc.nh.gov/rsa/html/XXI/265/265-163.htm | gc.nh.gov and gencourt.state.nh.us unreachable through the sandbox proxy |
| US-182 | Wisconsin EO #245 (2017) | https://docs.legis.wisconsin.gov/code/executive_orders/2011_scott_walker/2017-245.pdf | connection reset twice |
| REF-06 | ISO/TS 15066:2016 | https://www.iso.org/standard/62996.html | iso.org 403; webstore.ansi.org 403 |
| REF-08 | ISO 26262-1:2018 | https://www.iso.org/standard/68383.html | iso.org 403; webstore.ansi.org 403 |
| REF-09 | ISO 21448:2022 | https://www.iso.org/standard/77490.html | iso.org 403; webstore.ansi.org 403 |
| REF-12 | ANSI/RIA R15.06-2012 | https://webstore.ansi.org/standards/ria/ansiriar15062012 (or a3automate.org) | a3automate.org TLS failure; ANSI webstore 403 |
| REF-13 | ANSI/A3 R15.08-1-2020 | https://webstore.ansi.org/standards/ria/ansia3r15082020 (or a3automate.org) | as REF-12 |

## saved_partial

- US-104 Georgia SB 219 (2017): only the introduced bill text (legis.ga.gov document 165992) and the Senate-passed CSFA (167556) are reachable; the final "AP" document id was not found. Not the enacted text. The primary URL (lexisnexis.com) is not an acceptable source.
- REF-07 IEC 61508-1:2010, REF-10 ISO/IEC 42001:2023 (both IEC webstore abstracts), REF-11 IEEE 7001-2021 (IEEE SA page): scope pages only.

## Irrelevant candidates

None in this slice.

## Surprises and caveats

- **ML-075 (Brazil RBAC 100)**: the ANAC page cites *Resolução nº 805* of 15 June 2026, not 806. The pergamum PDF host now shows an "Acesso Externo Suspenso" notice (external access suspended) for every file; the HTML versions on anac.gov.br/assuntos/legislacao are complete and were used for ML-075 and ML-076.
- **US-098 (DC B25-0709)**: this bill is the Autonomous Vehicle Testing Permit Requirement *Temporary* Amendment Act of 2024 (D.C. Law 25-168, effective 1 Jun 2024, expired 12 Jan 2025), not the Emergency act as titled in the target. Saved from the Council's D.C. Law Library (code.dccouncil.gov).
- **US-128 (Montana SB 67, 2025)**: enacted short title is "Montana Automated Driving Systems Act" (Ch. 355, L. 2025), not "Autonomous Vehicle Act".
- **US-155 (R.I. ch. 1-8)**: the 2016 chapter (saved as enacting bill S 3099) was repealed and rewritten in 2023 (H 5420); the live sections are 1-8-1.1 and 1-8-1.2.
- **US-158 (S.D. ch. 50-15)**: chapter is now titled "Drones"; 50-15-1 repealed by SL 2018 ch. 269.
- **US-137 (N.Y. GBL Art. 47)**: nysenate.gov consolidated-law pages refuse the crawler; saved the enacted FY2026 budget bill S3008-C (Chapter 58 of 2025, ~76k words), Part U of which adds Article 47. The identical standalone bill A6767 was also fetched.
- **US-112 (Iowa 321.492B)**: the code section is one sentence (57 words), below the 150-word save threshold; the enrolled HF 2289 (2014) was saved instead.
- **ML-016 (Quebec)**: legisquebec consolidated code is 403; saved the full annual statute S.Q. 2018 c. 7 (Bill 165, French) from Publications du Quebec.
- **ML-053 (Kenya LN 76/2019)** needed `--render` (plain fetch returns 202); **REF-15 (OECD AI Principles)** likewise (plain fetch 0 words), rendered text contains the full amended Recommendation.
- **ST-199 / REF-17 (UN Regulation No 171)**: same instrument; both saved from the Publications Office via CELEX 42024X2689 (OJ L 2024/2689). The 2025 amendment (OJ L 2025/1899) was not fetched.
- **California (US-090/092/093/094/095)**: openstates.org now redirects to pluralpolicy.com; the rendered pages carry the chaptered bill text, which is what was saved (leginfo, the official site, is 403). US-086 (2012 session) would not render.
- **Idaho, Utah, Louisiana, Oklahoma, Maryland, Montana, New Mexico, Oregon**: statute/bill-info pages are JS shells or empty to the crawler, but the legislatures' own PDF endpoints (enrolled bills / chapter laws) work and were used.
- Hosts that are unreachable rather than refusing (gaca.gov.sa, dgac.gob.cl, gc.nh.gov, docs.legis.wisconsin.gov, assembly.ny.gov) are reported as blocked with the URL; they may simply be geo- or proxy-blocked from the sandbox.
