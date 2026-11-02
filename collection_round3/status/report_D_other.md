# Round-3 collector report — slice D (India, Oceania and other)

12 targets worked; every fetch went through `scripts/r3fetch.py` with the research-crawler identification. Outcome rows are in `status/agent_D_other.csv`.

## Counts by outcome

| outcome | n | candidates |
|---|---|---|
| saved | 3 | AP-003, AP-101, EN-046 |
| saved_partial | 2 | AP-001, ML-067 |
| blocked | 6 | AP-002, AP-009, AP-087, AP-088, AP-089, EN-086 |
| not_found | 1 | ML-069 |
| irrelevant | 0 | — |

## Saved texts

- **AP-101** NZ Civil Aviation Act 2023 — full Act, latest version as at 23 Oct 2026, 162,425 words, rendered from `https://www.legislation.govt.nz/act/public/2023/10/en/latest/` (the original whole.html URL redirects there; `--render` required).
- **EN-046** Estonia — official Riigi Teataja English translation of the consolidated Traffic Act (`https://www.riigiteataja.ee/en/eli/501122025002/consolide`), 112,490 words, containing the self-driving delivery robot (robotliikur) definitions and rules introduced by the 14 June 2017 amendment. The original English ID 523062017001 and the Estonian secondary ID 117032017001 both 404; plain requests get 2 words on this host, `--render` works.
- **AP-003** India, Drone (Amendment) Rules 2023, G.S.R. 715(E) — the gazette notification (234 words, complete) from `https://www.thc.nic.in/Central%20Governmental%20Rules/Drone%20Rules,%202021.pdf`, a High Court of Telangana (nic.in) copy that is mislabelled "Drone Rules, 2021". MoCA copy 403, MEA copy redirects to an error page.

## Partial (official scope/summary only)

- **AP-001** Drone Rules 2021 — only the PIB official backgrounder (28 Jan 2022, 3,286 words) could be read. The rules text is on MoCA (403 on every path), ffo.gov.in (denied at the egress proxy, 502 on CONNECT) and eGazette (blocked); DigitalSky hosts only the July 2021 draft.
- **ML-067** Namibia NAMCAR Part 101 — only the NCAA guidance page on RPAS Letters of Approval (`https://ncaa.com.na/fullarticle.php?for=83`, 502 words, quotes NAMCAR 101.03.1). The primary `rpas.php` is now 404. Part 101 was gazetted as GN 89 in Government Gazette No 7157 (27 Mar 2020); the only online copy found is the non-official `archive.gazettes.africa` mirror, which was not fetched.

## Blocked — URLs for a person to open

| id | URL | what happened |
|---|---|---|
| AP-002 | https://www.civilaviation.gov.in/sites/default/files/2023-10/Drone%20%28Amendment%29%20Rules%2C%202022%20dated%2011%20Feb%202022_0.pdf (also `/2025-11/drone-amendment-rules-2022-dated-11-feb-2022.pdf`) | civilaviation.gov.in 403 to the crawler on every path, www and non-www |
| AP-009 | https://www.civilaviation.gov.in/node/3286 (orders archive: https://www.civilaviation.gov.in/ministry-documents/orders-documents/archive-document) | 403; node 3286 is "Conditional exemption to Government of Telangana for BVLOS drone trials" (7 May 2021); original node 3246 also 403 |
| AP-087 | https://www.legislation.sa.gov.au/_legislation-documents/lz/v/a/2016/motor-vehicles-trials-of-new-automotive-technologies-amendment-act-2016_10/2016.10.un.pdf | 403 on page, PDF and RTF paths; render times out; Act is No 10 of 2016 |
| AP-088 | https://legislation.nsw.gov.au/view/pdf/asmade/act-2017-41 (alt: https://www.parliament.nsw.gov.au/bill/files/3415/Passed%20by%20both%20Houses.pdf) | 403 from legislation.nsw.gov.au and parliament.nsw.gov.au; renders time out |
| AP-089 | https://www.legislation.vic.gov.au/as-made/acts/road-safety-amendment-automated-vehicles-act-2018 (authorised PDF "18-008aa authorised.pdf" linked there) | site serves a 22-word stub to the crawler, plain and rendered; guessed content paths 404 |
| EN-086 | https://web.shgm.gov.tr/documents/sivilhavacilik/files/mevzuat/SHT-IHA_Rev-05.pdf | TLS handshake fails through the egress proxy (SSLEOFError) on three attempts; `iha.shgm.gov.tr` redirects to a login page; the TKGM mirror returns an HTML app page, not a PDF |

## Not found

- **ML-069** Mauritius Civil Aviation (Unmanned Aircraft System) Regulations 2024 — the DCA "Drone Requirement" SharePoint page (`https://civil-aviation.govmu.org/Pages/DRONE/Drone-Requirement.aspx`) returns 200 with no extractable text, plain and rendered, three attempts; no copy of the regulations on civil-aviation.govmu.org, attorneygeneral.govmu.org or a gazette; secondary sources disagree on commencement (1 Jan 2025 vs 1 Jan 2026).

## Surprises and corrections to the target rows

- The thc.nic.in file named "Drone Rules, 2021.pdf" is the **2023 amendment**, not the principal rules (used for AP-003, not AP-001).
- **AP-088** is Act **No 41** of 2017, not No 22; it inserted Part 5.6 (ss 148L–148V) into the Road Transport Act 2013 and is now listed as repealed/spent on the NSW site.
- **AP-087** is Act No 10 of 2016 (assented 31 Mar 2016); the original URL's `_18` suffix is wrong.
- **AP-009**: coverage dates the Telangana VLOS/BVLOS exemptions to April–May 2021, not 4 August 2021; the MoCA listing shows an end date of 31 Dec 2022, so the order has likely lapsed.
- **EN-086**: an SHGM form cites a rewritten SHT-İHA dated 19/12/2025, reported in force from mid-2026; Rev-05 may no longer be current.
- **EN-046**: the saved text is the official English *consolidated* Traffic Act, not the amending act of 14 June 2017 as a standalone document.
- Web search also surfaced a **Drone (Amendment) Rules, 2024 (G.S.R. 515(E))** for India that is not in the target list.
- **ML-067** has no jurisdiction code in the targets file; it should be NA (Namibia).
- `raw/EN-086.pdf` is actually the TKGM HTML page saved by r3fetch under a .pdf name.

## Host behaviour seen this round

- Refuse the crawler (403): civilaviation.gov.in (all paths), pib.gov.in press pages (static.pib.gov.in PDFs are fine), legislation.sa.gov.au, legislation.nsw.gov.au, parliament.nsw.gov.au, mea.gov.in (redirects to error.htm).
- Egress proxy denial (502 on CONNECT): ffo.gov.in.
- TLS failure through proxy: web.shgm.gov.tr.
- Empty 200 / bot stub: legislation.vic.gov.au (22 words), civil-aviation.govmu.org (0 words).
- Work with `--render` only: legislation.govt.nz, riigiteataja.ee.
