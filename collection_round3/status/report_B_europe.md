# Round-3 report — slice B (Europe), 62 targets

Collector: agent B. All requests went through `scripts/r3fetch.py` with the project's crawler identification; no browser impersonation, cookies, proxies or bot-check circumvention. Outcomes are in `status/agent_B_europe.csv`; every request is in `status/fetch_log.csv`.

## Counts by outcome

| outcome | n |
|---|---|
| saved | 27 |
| saved_partial | 2 |
| blocked | 24 |
| irrelevant | 9 |
| not_found | 0 |
| **total** | **62** |

## Routes that worked

- **EUR-Lex (14 targets, all 202):** `https://publications.europa.eu/resource/celex/<CELEX>` resolves to the cellar HTML manifestation and saved 11 of them directly (EU-010, EU-014, EU-019, EU-020, EU-021, EU-024, EU-025, EU-027, EU-029, EU-030, MW-068, REF-03). Exceptions: Regulation 2018/858 (EU-017) needed the `.0006.01/DOC_1` PDF manifestation (the default `.0006.03` is an empty index page); Directive 86/312/EEC (EUA-218) needed `.0008.01/DOC_1`; the 2023 Digital Rights Declaration (EUA-161) resolved only through the OJ resource `publications.europa.eu/resource/oj/JOC_2023_023_R_0001`.
- **JS portals read with `--render`:** fedlex.admin.ch (EN-021, EN-022, EN-024), legilux.public.lu (EN-075, EN-076), finlex.fi (EU-129).
- **PDF manifestations:** retsinformation.dk `…/eli/lta/2024/1312/pdf` (EU-136, also on lovtidende.dk); gazzettaufficiale.it full-issue PDFs `…/eli/gu/<date>/<n>/sg/pdf` (EN-028, EN-026 — the HTML pages and normattiva return only stubs to the crawler).
- **Germany:** gesetze-im-internet.de whole StVG for REF-01 (§§ 1a–1l present). bgbl.de's archive is a JS/PDF viewer the crawler cannot read, so the 2017 amending act (EN-002) was taken from the Bundesrat print 299/17 (Gesetzesbeschluss of the Bundestag, promulgated unchanged).
- **Russia:** publication.pravo.gov.ru serves only page images; the signed text of 258-FZ was found in the President's acts bank at `kremlin.ru/acts/bank/45796` by probing the ids of 31 July 2020.

## Blocked targets (URL for a person to open)

Legifrance (HTTP 403 to the crawler, known blocked host), 16 targets:
- EN-014 https://www.legifrance.gouv.fr/eli/ordonnance/2016/8/3/2016-1057/jo/texte
- EN-015 https://www.legifrance.gouv.fr/eli/decret/2018/3/28/2018-211/jo/texte
- EN-016 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039666574 (LOM arts 31–32)
- EN-018 https://www.legifrance.gouv.fr/eli/decret/2021/6/29/2021-873/jo/texte
- EN-019 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033293745
- EN-050 https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031044385/
- EN-051 https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036868691/
- EN-052 https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000038496320
- EN-053 https://www.legifrance.gouv.fr/loda/id/JORFTEXT000043370884
- EN-054 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046081252
- EN-055 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046151685
- EN-056 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046216833
- EN-057 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046828949
- EN-058 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047867363
- EN-059 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050662872
- EN-060 https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051484894
- (EN-017 is `saved_partial`: the ministry's official synthesis from ecologie.gouv.fr; full text at https://www.legifrance.gouv.fr/eli/ordonnance/2021/4/14/2021-443/jo/texte)

Norway (lovdata.no answers HTTP 405; luftfartstilsynet.no pages expose no text even when rendered), 5 targets:
- EU-130 https://lovdata.no/dokument/NL/lov/2017-12-15-112
- EU-131 https://lovdata.no/dokument/SF/forskrift/2017-12-19-2240
- EU-132 https://lovdata.no/dokument/SF/forskrift/2024-11-01-2777
- EU-133 https://lovdata.no/dokument/SF/forskrift/2015-11-30-1404
- EU-134 https://lovdata.no/dokument/SF/forskrift/2024-10-23-2572

Portugal (diariodarepublica.pt redirects every crawler request, including the files.diariodarepublica.pt PDFs, to /dr/error; nothing on anac.pt), 2 targets:
- EN-084 https://diariodarepublica.pt/dr/detalhe/decreto-lei/58-2018-115898563
- EN-085 https://diariodarepublica.pt/dr/detalhe/regulamento/1093-2016-105367104

Belgium, 1 target:
- EN-038 https://www.ejustice.just.fgov.be/eli/arrete/2016/04/10/2016014132/justel — the ELI resolver returns its "not found in our databases" help page (the numac may be wrong); the Justel cgi route and the Moniteur daily PDF (https://www.ejustice.just.fgov.be/mopdf/2016/04/15_1.pdf) close the connection on the crawler. A person should search Justel for the arrêté royal of 10 April 2016 "aéronefs télépilotés" or open the Moniteur belge of 15 April 2016.

## Irrelevant candidates (keyword false positives on legislation.gov.uk)

- UKA-020, UKA-021: 2013 Northern Ireland road orders for the A26 dualling scheme; "Drones Road" is a place name at the A44 junction.
- UKA-092, UKA-093, UKA-094, UKA-096: 1799–1816 acts authorising the export of coin-mint machinery (Matthew Boulton) to the USA, Brazil, Denmark and Russia.
- UKA-095: Cartwright's Woolcombing Machinery Act 1801 (textile-machine patent).
- UKA-104, UKA-105: 1948–49 revocations of post-war farm-machinery and office-machinery supply-control orders.

## Things to know

- **EN-007 (German 2017 drone ordinance) is `saved_partial`:** the text saved is the Government's draft as Bundesrat print 39/17 (with Begründung). The Bundesrat approved it with amendments (Drs. 39/17(B)), so the promulgated wording (BGBl. I 2017 S. 683, only in the bgbl.de viewer) differs in places.
- **EN-002:** the saved Bundesrat print 299/17 is the Bundestag's adopted text, which the Bundesrat passed unchanged; it should match BGBl. I 2017 S. 1648. The current consolidated StVG (REF-01) is a separate, later text.
- **REF-01** is the whole consolidated StVG (last amended 22 Oct 2026), not the 2021 amending act itself; §§ 1e–1l are in it.
- **EN-026 and EN-028** are full Gazzetta Ufficiale issues (a 205k-word supplement for the 2018 Budget Law; GU n. 223 for the 2025 AI law) — the target provisions are inside, with other acts.
- **EN-071:** the kremlin.ru body carries the title "в сфере цифровых и технологических инноваций" while the header says "цифровых инноваций" — original 2020 wording, not consolidated. An earlier capture of acts-bank id 45800 was a different law (280-FZ on refugees) and has been overwritten.
- **EUA-218** is a 1986 lifts directive (repealed by 95/16/EC); **EUA-161** is a non-binding interinstitutional declaration, although the target row calls it a binding regulation.
- **Duplicates:** EU-024 = MW-068 (Toy Safety Regulation 2025/2509); EU-020 = REF-03 (PLD 2024/2853). Each has its own text file.
- Housekeeping inside the round-3 folder: the misleading ELI help-page capture `texts/EN-038.txt` and two empty error-page files `raw/EN-084.pdf`, `raw/EN-085.pdf` were deleted; the earlier junk captures for EN-002/EN-007 (bgbl.de viewer chrome) were overwritten by the Bundesrat prints. Nothing outside `/home/user/collection-round-3/` was touched.
