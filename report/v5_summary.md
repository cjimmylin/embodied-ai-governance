# Version 5 summary: what collection round 3 did (2 November 2026)

Round 3 executed, without a person in the loop, the items of the round-3 plan that an agent can do alone. Everything that needs a person is in `HUMAN_ASSISTANCE.md`. The companion report is `report/collection_round3.md`; the counts below are from the v5 tables (`data/results.json`, `tables/`).

## What was done

1. **Recovering blocked and missing instruments.** Four collector agents (East Asia; Europe; Americas and international; India, Oceania and other) re-fetched the 189 round-2 candidates that had been verified as binding instruments but never read, plus the 17 reference-list instruments the strict test had missed, by official alternative routes: the Publications Office CELEX resolver for EUR-Lex pages that return 202, state legislatures' PDF endpoints, rendered pages on Riigi Teataja and legislation.govt.nz, the KLRI English statutes, the Shenzhen and Hangzhou gazettes, the Japan e-Gov law API, the Kremlin acts bank. The crawler identified itself honestly (`CEI-AI-Robotics-collector/1.0`) and did not imitate a browser or bypass bot checks; the hosts that refuse it (Legifrance, Lovdata, flk.npc.gov.cn and most Chinese provincial databases, law.go.kr, sso.agc.gov.sg, iso.org, several US state legislatures) are listed for manual download.
2. **A harvest with new terms** (service robot, care robot, exoskeleton, humanoid, collaborative robot, delivery robot, and EuroVoc concepts) over EUR-Lex, legislation.gov.uk, the Japan e-Gov API, the gov.cn policy library, the Federal Register of Legislation, eCFR and the Brazilian Chamber. It found little that rounds 1 and 2 had not: the open legal databases hold few service-robot instruments.
3. **Full-text re-reads** of the 104 principal instruments whose text exceeded the 110,000-character excerpt, with up to 400,000 characters under the same prompt; the full-text labels replace the excerpt labels (Tables 74 and 75).
4. **A supplementary schema** on every principal embodied instrument: whom the rule binds, entry-into-force, application and repeal dates, the legal effect of a standard, and the year the robot-relevant provision arrived, each with a quote (Tables 70 to 73; new columns in the master table; shown in the dashboard's record drawer).
5. **A second independent precision audit** of 100 of the 195 principal binding instruments (seed 2027): joint precision 73% (64 to 81), up from 54% in v3 (`review/v5_audit/`).
6. **Analysis additions**: the governance-gap index split by collection source (Table 7b), the collection round as a covariate in the adjusted models (Table 28), a round-1-only line in the trend figure (Figure 42).
7. **A human-validation kit**: 200 stratified documents, a coding sheet with drop-downs, instructions and a sealed answer key (`data/human_validation/`).
8. **Rebuild**: v5 master table, tables, figures, dashboard (with a round-3 view and the new fields), the round-3 companion report, and `HUMAN_ASSISTANCE.md`.

## Headline counts (v4 to v5)

| Count | v4 | v5 |
|---|---|---|
| Usable documents | 3,165 | 3,320 |
| Embodied-AI set | 1,603 | 1,704 |
| Principal embodied instruments | 505 | 598 |
| Principal binding embodied instruments | 195 | 278 |
| ... of which naming AI explicitly | 15 | 25 |
| ... with autonomy or automation provisions | 140 | 201 |
| Round-3 targets saved / partial / blocked / irrelevant / not found | | 113 / 8 / 74 / 9 / 2 of 206 |
| Round-3 documents added (usable / principal / binding) | | 160 / 98 / 85 |
| Full-text re-reads: document class unchanged | | 96.2% of 104 (relevance 87.5%) |
| Precision audit, joint share (a)(b)(c) | 54% (v3, n=100 of 299) | 73% (64 to 81; n=100 of 195) |

The binding count rises because round 3 read 80 binding instruments that round 2 had verified but could not fetch; it is not a change in the world. The precision audit implies that about three quarters of the binding set are distinct binding instruments with substantive embodied provisions.

## What was not done

- The narrative documents (brief, analysis report, paper, supplement) were not rewritten: their tables and figures are regenerated and a v5 note at the top says that their sentences still state the v4 counts. Rewriting and re-auditing the narrative is the next writing task.
- No person has labelled any document; the audits are model-on-model. The validation kit is ready.
- Technical standards are still read from their public scope pages.
- The 86 blocked targets, the one not found and the paid standards need a person (`HUMAN_ASSISTANCE.md`).

## Cost of the round (API, in US dollars)

| Pass | Documents | Cost |
|---|---|---|
| Full-text re-reads (up to 400,000 characters) | 104 | $46.16 |
| Supplementary schema | 603 | $31.14 |
| Round-3 annotation (recovered and new documents) | 165 | $14.28 |
| Total API cost | | $91.58 |

The five agents (four collectors and the auditor) ran as Claude Code subagents: about 1.4 million tokens in all (collectors 176k, 183k, 181k and 439k; auditor 415k).
