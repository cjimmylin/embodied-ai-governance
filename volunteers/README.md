# Volunteer tasks

← Back to the **[project hub](https://cjimmylin.github.io/embodied-ai-governance/docs/index.html)**

Ten pieces of work a volunteer team can take on, ordered by how much they would change the study's results. **Sign up and log progress on the live sheet:** https://claude.ai/artifact/21o6idnP14fyQPwA7LsZ6i (tag yourself by email on a task, then raise its counter and post short updates). This page is the written copy of the same briefs, for anyone who cannot open the sheet.

General rules for every task: work from official sources; never work around a login, payment or bot check; never commit source texts or standards to this public repository (send them to the coordinator or the shared folder); fill the task's template in `volunteers/templates/` and return it.

## Changes the results

### 1. Hand-label the 200-document validation sample

No person has labelled a document yet; every number in the study rests on model labels. Two independent human coders give the first human check of each field and let the headline counts be corrected.

- **Skill:** Policy or legal reading. One coder who reads Japanese or Chinese helps (20 of the 200).
- **Effort:** About 30 hours per coder (8 to 15 minutes a document)
- **People:** 2
- **Progress is counted in:** 400 documents coded (200 per coder)

**What to do**

1. Read the coder instructions and the codebook sections they point to.
2. Download the coding sheet and save your own copy as coding_sheet_<your initials>.xlsx. The two coders work independently and do not compare answers until both are finished.
3. For each row of the sample, open its source URL and read at least the first 6,000 characters and the end. Fill your row: the six drop-down fields, the robot types, the twelve principles at 0, 1 or 2, and the minutes taken.
4. Do not open the answer key (answer_key_model_labels.csv) until both sheets are finished.
5. After each session, raise the counter on this card and post a one-line update.
6. When both sheets are done, meet to settle each disagreement and record the agreed value in a third, adjudicated sheet.

**Files**

- [Coder instructions](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/human_validation/INSTRUCTIONS.md)
- [The 200 documents (sample.csv)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/human_validation/sample.csv)
- [Coding sheet (coding_sheet.xlsx)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/human_validation/coding_sheet.xlsx)
- [Codebook](https://github.com/cjimmylin/embodied-ai-governance/blob/main/codebook/codebook.md)
- [Taxonomies](https://github.com/cjimmylin/embodied-ai-governance/blob/main/codebook/taxonomies.md)

**Hand back:** The two completed coding sheets and the adjudicated sheet, sent to the coordinator or added through a pull request to data/human_validation/returned/.

**Note:** The stored texts are not in the public repository; work from the source URL. Machine translation is acceptable only as an aid, and should be noted on the row.

### 2. Download the 74 instruments the crawler could not reach

Official sites in France, Norway, Korea, Taiwan, several Chinese provinces and elsewhere refuse the study's research crawler. A person with an ordinary browser can save the texts, and each one may change a count.

- **Skill:** An ordinary web browser. Reading French, Chinese, Korean or Norwegian helps.
- **Effort:** 5 to 10 minutes per instrument; one to two days in all
- **People:** 2
- **Progress is counted in:** 74 instruments saved

**What to do**

1. Open the human-assistance list, item 1, which gives each instrument with its official URL. Claim a group by tagging yourself on this card and posting an update such as 'taking Legifrance (16)'.
2. Open each official URL in your browser. If the page asks for a login, a payment or a check you cannot pass as an ordinary visitor, skip it and note why. Never work around access controls.
3. Save the instrument as <candidate_id>.pdf, or copy its text into <candidate_id>.txt whose first line is SOURCE_URL: followed by the address you used.
4. Record each instrument in the download log template, including the ones you had to skip.
5. Put the files and the log in the team's shared folder, or send them to the coordinator. Do not commit the texts to the public repository: source texts are not redistributed.
6. Raise the counter on this card as you go.

**Files**

- [Human-assistance list (item 1)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/HUMAN_ASSISTANCE.md)
- [Download log template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/blocked_downloads_log.csv)
- [Collector reports with the routes already tried](https://github.com/cjimmylin/embodied-ai-governance/tree/main/collection_round3/status)

**Hand back:** The saved files and the completed download log.

### 3. Obtain the 44 obtainable technical standards through a library

Technical standards say how to make a robot safe, but the study could read only their public preview pages. Full texts would let the standards be labelled properly.

- **Skill:** A university, school or institutional library login.
- **Effort:** A few days
- **People:** 1
- **Progress is counted in:** 44 standards obtained

**What to do**

1. Open the human-assistance list, item 3, and the list of standard ids. Set aside the 13 unpublished ISO drafts (marked PWI, AWI, WD, CD, DTS or DPAS): no one outside the committees can obtain them.
2. Check your library for these routes. ASTM Compass, or the ASTM academic programme (ASTM, 19 standards). British Standards Online, IHS/Accuris or Techstreet (the 9 published ISO standards and BS 8611). BSI's free download after registering, offered for the government-sponsored PAS documents (PAS 1881, 1882, 1884, 1885; check each). SAE Mobilus (SAE, 4; J3016 is also free from SAE). UL's free digital view after registering (UL, 3). The Korean standards portal, which shows KS standards online (the KS copies of ISO 13482 and 10218-1). The Singapore Standards eShop (TR 68-2).
3. Before anything is analysed, read the licence: confirm that it permits text analysis for research. If it does not, note the instrument's legal effect and scope by hand in the log instead.
4. Record each standard in the access log: route, licence answer, date.
5. Store permitted copies only where the coordinator says (data/texts_private/ on the project machine). Never commit a standard to the repository or share the PDF.

**Files**

- [Human-assistance list (item 3)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/HUMAN_ASSISTANCE.md)
- [Standard ids (ids_standards.txt)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/ids_standards.txt)
- [Access log template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/standards_access_log.csv)

**Hand back:** The completed access log, and the permitted texts stored privately.

**Note:** Library licences cover their own members only and usually forbid redistribution.

### 4. Rule on the audit failures and check the uncertain legal readings

The second precision audit would exclude 27 sampled instruments, and the model was unsure about whom 99 instruments bind, their dates, the legal effect of standards or when the robot provision arrived. A ruling on each corrects the counts directly.

- **Skill:** Legal training, or experience reading statutes and regulations.
- **Effort:** About a week, split between two people
- **People:** 2
- **Progress is counted in:** 126 rulings recorded (27 audit + 99 checks)

**What to do**

1. Agree a split: one person takes the 27 audit failures, the other the 99 legal-check ids, or divide by jurisdiction.
2. Audit failures: read section 5 of the audit report and the failing rows of the results file. For each, rule keep, exclude or relabel (for example 'amendment', 'general-AI instrument') with a one-line reason.
3. Legal checks: for each id in ids_legal_check.txt, open annotations/supplement_v5/<doc_id>.json to see what the model answered and the quote it relied on, and open the instrument at its source_url (in data/master_table.csv). Confirm or correct: whom it binds, the entry-into-force, application and repeal dates, the legal effect of a standard, and the year the robot-relevant provision was added.
4. Record every ruling in the rulings template with the source you relied on (article, gazette page or amendment history).
5. Raise the counter on this card and post an update when you finish a jurisdiction.

**Files**

- [Second precision audit (section 5 lists the failures)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/review/v5_audit/precision_audit_v5.md)
- [Audit results (CSV)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/review/v5_audit/precision_audit_v5_results.csv)
- [Ids to check (ids_legal_check.txt)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/ids_legal_check.txt)
- [Model answers with quotes](https://github.com/cjimmylin/embodied-ai-governance/tree/main/annotations/supplement_v5)
- [Master table (source URLs)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/master_table.csv)
- [Rulings template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/legal_rulings.csv)

**Hand back:** The completed rulings file.

### 5. Settle the reference list of instruments every collection should have

The study measures what it missed against a list of key instruments that the AI agent compiled. The list should be the team's judgement, not the machine's.

- **Skill:** Knowledge of AI or robot governance; three people form the panel.
- **Effort:** An hour of reading each and a one-hour meeting
- **People:** 3
- **Progress is counted in:** 39 instruments reviewed

**What to do**

1. Each panellist reads the 39 instruments in the reference list and fills a copy of the review template: keep or drop each, and add instruments that are missing, with the jurisdiction and a reason.
2. Meet for an hour to agree the final list.
3. One panellist records the agreed list in reference_instruments.csv and opens a pull request, or sends it to the coordinator.

**Files**

- [Current reference list](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/reference_instruments.csv)
- [Review template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/reference_list_review.csv)

**Hand back:** The agreed reference list.

## Extends the study

### 6. Fill the thin regions: Africa, the Middle East, Latin America, Oceania

These regions hold 36 of the 278 binding instruments, partly because their legal portals are hard to search automatically. People who know a country's legal publishing can find what the harvests missed.

- **Skill:** Familiarity with a country's legal system or language.
- **Effort:** A few hours per country
- **People:** 2
- **Progress is counted in:** candidate instruments recorded

**What to do**

1. Choose a country and post an update to claim it, so two people do not search the same one.
2. See what the collection already has: open the explorer and search the country, or filter data/master_table.csv on jurisdiction_country.
3. Search the official sources: the national gazette or legislation portal, the civil aviation authority (drone rules), the transport ministry (automated vehicles), the labour or industry ministry (industrial and service robots).
4. Record each instrument found in the new-instruments template, following the candidate schema. The official URL must open.
5. Raise the counter and post a one-line summary per country.

**Files**

- [Candidate schema (what to record)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/collection_round2/CANDIDATE_SCHEMA.md)
- [New-instruments template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/new_instruments.csv)
- [Master table](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/master_table.csv)
- [Explorer](https://cjimmylin.github.io/embodied-ai-governance/docs/explorer/index.html)

**Hand back:** The completed new-instruments file for each country searched.

### 7. Keep watch for new instruments each week

The collection stops at October 2026 and 2026 is already its largest year. A weekly watch keeps the map current between collection rounds.

- **Skill:** Comfort searching official legal databases.
- **Effort:** About an hour a week
- **People:** 1
- **Progress is counted in:** weekly checks done

**What to do**

1. Once a week, search the sources the study already uses for new instruments on robots, automated driving, drones, exoskeletons and humanoids: EUR-Lex, legislation.gov.uk, the US Federal Register and state legislature sites, Japan's e-Gov law database and China's State Council policy library.
2. Check each find against the explorer to see whether it is already in the collection.
3. Record new finds in the new-instruments template, with the date found.
4. Raise the counter and post 'week of <date>: N new'.

**Files**

- [New-instruments template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/new_instruments.csv)
- [Candidate schema](https://github.com/cjimmylin/embodied-ai-governance/blob/main/collection_round2/CANDIDATE_SCHEMA.md)
- [Explorer](https://cjimmylin.github.io/embodied-ai-governance/docs/explorer/index.html)

**Hand back:** A running new-instruments file.

### 8. Check the labels of Japanese, Chinese and Korean documents

The East Asian documents were labelled from the original language. Native readers can test whether the model read them correctly.

- **Skill:** Native or fluent reading of Japanese, Chinese or Korean.
- **Effort:** About a day per language
- **People:** 2
- **Progress is counted in:** 36 documents checked (12 per language)

**What to do**

1. Open data/master_table.csv and filter the language column to ja, zh or ko. Choose 12 documents per language, at least half of them binding instruments (doc_class governance_instrument_binding).
2. Read each document at its source_url.
3. Compare five model labels with your own reading: doc_class, binding_nature, instrument_status, embodied_categories and relevance_to_embodied_ai_governance, plus the English summary in summary_en.
4. Record each comparison in the translation-check template.
5. Raise the counter on this card.

**Files**

- [Master table](https://github.com/cjimmylin/embodied-ai-governance/blob/main/data/master_table.csv)
- [Translation-check template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/translation_check.csv)
- [Codebook (what each label means)](https://github.com/cjimmylin/embodied-ai-governance/blob/main/codebook/codebook.md)

**Hand back:** The completed translation-check file.

### 9. Rewrite the reports with the version-5 numbers

The brief, analysis report, paper and supplement still state the version-4 counts, while their tables and figures are version 5.

- **Skill:** Clear writing; the checker needs care with numbers.
- **Effort:** A few days for the writer, a day for the checker
- **People:** 2
- **Progress is counted in:** 4 documents updated

**What to do**

1. Read the version-5 summary to see what changed.
2. Writer: in report/src/<document>.md, replace each version-4 number with the value in the table the sentence cites (tables/ folder), and remove the 'Version 5 note' at the top when a document is done.
3. Checker: verify every number against its table, as the version-4 numbers audit did, and list any mismatch.
4. Submit each document as a pull request; the coordinator rebuilds the PDFs.

**Files**

- [Version-5 summary](https://github.com/cjimmylin/embodied-ai-governance/blob/main/report/v5_summary.md)
- [Report sources](https://github.com/cjimmylin/embodied-ai-governance/tree/main/report/src)
- [Tables](https://github.com/cjimmylin/embodied-ai-governance/tree/main/tables)
- [Example numbers audit](https://github.com/cjimmylin/embodied-ai-governance/blob/main/review/v4_numbers_audit.md)

**Hand back:** Four updated report sources and a numbers-audit note.

### 10. Test the database entry designs with five real users

Seven layouts for one instrument entry are ready. Watching intended users find answers shows which layout works before the recommended design is built for real.

- **Skill:** Running a short interview; no technical background needed.
- **Effort:** About a week, including recruiting
- **People:** 1
- **Progress is counted in:** 5 users tested

**What to do**

1. Recruit five intended users of the CEI database: researchers, policy staff or students.
2. Give each three questions about the example instrument (the EU Machinery Regulation): Whom does it bind? Is it in force, and since when? What does it require on physical safety?
3. Let them answer first on the Current tab, then on two of the five designs, then on Recommended. Note the time taken and whether the answer was right on each tab.
4. Record the sessions in the user-testing notes template and summarise which layout answered fastest and most reliably.

**Files**

- [The clone with the seven tabs](https://cjimmylin.github.io/embodied-ai-governance/docs/pages/clone/index.html#record)
- [The five designs side by side](https://cjimmylin.github.io/embodied-ai-governance/docs/pages/instrument_entry_proposals.html)
- [User-testing notes template](https://github.com/cjimmylin/embodied-ai-governance/blob/main/volunteers/templates/user_testing_notes.md)

**Hand back:** The completed notes with a one-paragraph recommendation.
