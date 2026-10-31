# Journalist's review: understandability, story and impact

**Reviewer role:** technology and policy journalist, data-journalism desk, reviewing for a general educated audience.
**Package reviewed:** `report/analysis_report.md` (executive summary and section 10 in full, remainder skimmed), `report/paper.md` (abstract, introduction, discussion, limitations, conclusion), figures F05, F06, F07, F11, F18, F20, F24, F31, F33, F34 (light) plus F18 and F31 dark variants, and `dashboard/index.html` rendered in headless Chromium at 1280 px and 400 px, light and dark, with one filter applied and one record drawer opened.
**Date:** 30 October 2026.

Verdict in one line: there is a strong, publishable story in here, but it is buried under 113 numbers in 33 sentences, the headline counts disagree with each other across the package, and the dashboard's first screen tells the reader the corpus starts with a Shakespeare poem from 1594.

---

## 1. The story, and three headlines

### The story in one sentence

Around the world robots are being studied far more than they are being regulated: the few binding rules that reach them are borrowed from car, aviation, factory and medical-device law or written as voluntary ISO standards, and the robots people actually live with (companions, carers, humanoids) have almost none.

### Three headlines I could file from this material

1. **"Scientists study companion robots. Lawmakers regulate cars."**
   Supporting number: companion and social robots are the subject of 43% of robot-governance research papers (219 of 509) but 3% of robot-governance rules (2 of 63, neither binding); self-driving cars are 12% of research and 46% of rules (29 of 63, 5 binding). Source: Table 7, Figure 18.

2. **"Only six laws in the world bind robots as robots, and just one is a robotics statute."**
   Supporting number: of 1,703 documents, 674 address robots or embodied AI; 63 are rules of any kind; 7 "captures" are legally binding, and one of those is the EU AI Act counted twice, so six distinct laws. Only El Salvador's 2025 Robotic Technologies Law is a general robotics statute. Source: executive summary finding 2, section 3.2. (See critical finding C3: say "six".)

3. **"Everyone talks about how much control a robot should keep. Nobody has written it down."**
   Supporting number: "autonomy level and control" is raised in roughly 40% of robot documents of every kind (binding laws 43%, voluntary guidance 42%, ISO standards 42%, research 42%), but specified in detail in none of the binding laws, none of the standards, and at most 8% of any type. Source: Table 9, section 5.3.

Runner-up: **"'Physical AI' goes from 1% of documents to 10% in two years"** (1.2% in 2024, 4.0% in 2025, 9.7% in 2026; section 7.1). Hold this one until the 2018 spike in Figure 33 is explained (see M6).

Runner-up: **"Humanoid robots: 143 documents, 12 policy papers, zero binding laws, one bill"** (section 8; the bill is Brazil's PL 391/2026).

---

## 2. Findings, ranked

Severity: **Critical** = would stop me publishing or would be caught by a fact-checker on first pass. **Major** = materially hurts understanding or trust. **Minor** = polish.

### Critical

**C1. The headline numbers disagree across the package.**
*Location:* dashboard tiles; `analysis_report.md` executive summary finding 1; Figure 6 legend; Table 9 / section 5.3; section 3.1.
*Problem:* A reader who opens the dashboard and the report side by side sees different totals with no reconciliation. Dashboard tiles: 1,703 documents, 407 governance instruments, 44 binding, 611 embodied-AI focused. Report: 1,589 usable documents, 381 instruments, 36 binding (7 embodied + 29 general), 674 in the embodied set. Technical standards among embodied instruments are "10" in finding 1, "n=7" in the Figure 6 legend, and "n=12" in Table 9 and section 3.1. Soft-law instruments are 37 in finding 1 and Figure 6 but n=33 in Table 9. Humanoid documents are 143 in the report but the dashboard's "Humanoid & general-purpose" filter returns 78. Each number has a defensible definition (dated vs undated standards, binding nature vs document type, any-mention vs primary category, all captures vs usable), but the reader is never told which one is in play.
*Fix:* Add a single "key numbers" box at the top of the report and the dashboard, with one denominator convention and the alternative counts in a footnote. Pick one count for standards and use it everywhere (I would use "12 technical standards, 9 of them dated" or similar). Label the dashboard tiles "all captured documents" and add a toggle or sub-line: "1,589 usable". Make the dashboard category filter match the report's definition (any mention), or label it "primary category".

**C2. The dashboard's first screen destroys trust: "Year span 1594–2027".**
*Location:* dashboard tile row; first row of the document table.
*Problem:* The 1594 document is *The Rape of Lucrece* (D1446, Shakespeare), classified as "communication / news" in the European robotics sprint. The first row of the table, sorted by year descending, is a German book chapter dated 2027, i.e. the future. These are the first two things a visitor reads. A journalist's immediate reaction is "if a Shakespeare poem is in the robot-governance corpus, what else is?"
*Fix:* Remove or quarantine non-AI and unusable records from the default view (keep them reachable via a "show excluded records" switch). Clamp implausible years and flag them ("year unverified"). Default the table sort to relevance or to instruments-first, not to year descending. Change the tile to the usable range ("2014–2026").

**C3. "Seven binding instruments" is six.**
*Location:* executive summary findings 1 and 2; abstract; conclusions; Figure 6 legend.
*Problem:* The EU AI Act is "captured twice" and both captures are counted. The report admits this in a parenthesis but still headlines "7" everywhere, including the abstract. Any fact-checker will say the number is inflated by a deduplication failure and will ask what else was double-counted.
*Fix:* Deduplicate and say "six binding laws (seven captures)". Rewrite finding 2's opening: "Six laws in the collection bind robots, and only one of them is about robots as such."

**C4. No human has read any of the 1,703 documents, and the summary does not say so plainly.**
*Location:* executive summary (paragraph 1 mentions "a large language model"; finding 10 calls the annotation "reliable enough"); section 2; paper section 4.2.
*Problem:* Every label was assigned by Claude Sonnet 5.5; the "independent" check is Claude Opus 5.5 (same vendor, same family); test-retest is the same model re-run. There is no human-coded sample and no gold standard anywhere in the package (I searched for "human annot", "hand-coded", "gold standard"). Finding 10's "median Cohen's kappa 0.89" will be read by a lay reader as "89% accurate", which it is not. The 119.60 USD annotation cost is a detail a sceptical reader will seize on.
*Fix:* State it in the first paragraph in plain words: "Every document was read and labelled by an AI model; a second AI model agreed with it on about nine labels in ten; no human has checked the labels except on spot checks." Then hand-code 50 to 100 documents (especially the 63 embodied instruments, which carry the headline) and report human-model agreement. Until then, soften "reliable enough" to "consistent".

**C5. The biggest headline is partly built into the collection design, and the summary hides this.**
*Location:* executive summary finding 1 ("mostly written by academics, not legislators"); paper discussion ("partly a collection artefact") and limitations.
*Problem:* The regional teams ran a "sprint" that sought research about robots and a "database" that sought general-AI instruments. So of course the robot set is 75% research and the general-AI set is full of instruments. The discussion admits this; the executive summary, abstract and conclusions do not. A reviewer or rival researcher will call the research-to-law ratio an artefact of the brief.
*Fix:* Carry the caveat into finding 1 in one sentence ("The collection sought research on robots and official texts on AI in general, so the ratio overstates the gap; the comparison that survives this is instruments-only: 63 rules for robots versus 301 for AI in general, 6 binding versus 29"). Lead with the instrument-only numbers, which are robust to the design.

### Major

**M1. The ten findings are too dense to read: 3.4 numbers per sentence, up to 12 in one sentence.**
*Location:* executive summary.
*Problem:* I counted: 774 words, 33 sentences, 113 numbers. Finding 6's second sentence has 12 numbers in 49 words. Findings 4, 6, 8 and 9 each carry 16, 16, 11 and 16 numbers. No general reader will get past finding 3.
*Fix:* One bold number per finding; everything else goes to a table under the summary. Sample rewrite of finding 6:
> **Robot rules are product-safety rules; AI rules are audit-and-transparency rules.** Six in ten robot instruments lean on technical standards (versus three in ten for general AI) and one in three requires conformity assessment, the pre-market safety check used for machinery; general-AI instruments instead require audits, labelling and data rules. (Figure 24, Table 10.)

**M2. Findings 4, 5, 6 and 7 are indistinguishable to a lay reader.**
*Location:* executive summary.
*Problem:* "Principle profile", "operationalisation lags mention", "mechanisms", "regions differ in mechanism more than in principle" are four variations on one idea (what the documents value vs what they actually require). Ten findings is too many; five would land.
*Fix:* Merge into five: (1) who writes the rules and how few bind; (2) which robots get rules and which get papers; (3) robots are governed as machinery, AI as software, with the control gap; (4) regions agree on values, disagree on tools, nobody leads; (5) what is changing in 2025-26 and the arrival of "physical AI". Put reliability and blind spots in a boxed caveat, not a "finding".

**M3. Jargon runs through every section with no explanations.**
*Location:* everywhere; worst in finding 1 ("chi-square p = 0.003, Cramér's V = 0.19"), finding 4 ("Holm correction"), finding 8 ("odds ratio 1.47 per year"), finding 10 ("Cohen's kappa", "Spearman rho"), section 6 ("cosine distance", "average-linkage clustering"), and the figure titles ("Wilson intervals", "Holm-significant").
*Problem:* Statistical machinery is presented to a lay reader as if it were the finding. "Operationalise", "soft law", "conformity assessment", "governance instrument", "salience", "gap index", "lexicon", "level 1 / level 2" are used as if self-evident.
*Fix:* Move the test statistics to tables and footnotes; in prose replace with plain-language equivalents (see glossary, section 4). Sample: "The difference is statistically significant (chi-square p = 0.003, Cramér's V = 0.19) but modest in size" becomes "The difference is real but modest: robot documents are about twice as likely as general-AI documents to be research papers rather than rules, after allowing for chance."

**M4. Figure titles are labels, not findings.**
*Location:* all reviewed figures.
*Problem:* "Embodied-AI categories addressed", "Governance mechanisms by set", "Cumulative embodied-AI governance documents by binding nature" tell the reader what was plotted, not what it shows. A general reader needs the headline in the title and the variable in the subtitle.
*Fix (suggested titles):*
- F06: "Voluntary guidance on robots has grown fivefold since 2017; binding law has reached six" (subtitle: cumulative embodied-AI governance documents by binding nature, 2010–2026).
- F07: "Europe supplies four in ten documents; Latin America and Africa contribute AI strategies, not robot research".
- F11: "Companion, care and humanoid robots dominate the literature; delivery and farm robots barely appear".
- F18: "Researchers study companion robots; regulators write rules for cars" (keep subtitle "share of research papers vs share of rules mentioning each robot type").
- F20: "Robot documents talk about bodies (safety, proximity, liability); AI documents talk about growth, fairness and transparency".
- F24: "Robot rules lean on standards and testing; AI rules lean on audits and data".
- F34: "Since 2025 the robot debate has shifted from ethics to industrial policy, oversight and cybersecurity".

**M5. Figures to print and figures to cut.**
*Print (with retitling):* F18 (the one chart that carries the whole story; dark variant is legible), F06 (clear step chart; fix the legend counts, see M7), F07 left panel, F34 trimmed to the five significant rows plus three context rows, F11 trimmed to the top ten.
*Cut for a general audience:* F05 (see M6), F31 (a dendrogram and a cosine-distance heatmap for six regions; replace with one sentence: "Europe, the United States and Oceania are near-identical in how they talk about robot governance; the Middle East, which leads with liability, and the ISO standards layer, which leads with certification, stand apart"), F33 (see M6), F20 right panel and the bottom half of F20's left panel, F24 below the top ten rows.

**M6. Two figures will mislead a general reader into the opposite of the finding.**
*Location:* Figure 5 (embodied share by year, falling from 83% to 34%) and Figure 33 (every robot term's share falling since 2018, including "humanoid", from 23% to 12%).
*Problem:* Both decline because the corpus fills up with general-AI documents after 2023, not because interest in robots fell. Finding 9 says humanoids are rising (16.9% to 28.7% of embodied documents) while the figure the reader is shown has the humanoid line going down. The text explains it is "density, not share", but the figure plots share. Figure 33's first panel also shows "embodied AI / physical AI" at about 7% in 2018, which contradicts finding 9's framing of it as new vocabulary (the text quotes only 2024-26).
*Fix:* Cut F05. Re-draw F33 over the embodied set only, or as mentions per 1,000 words, and keep only three panels (embodied/physical AI, humanoid, cobot). Explain the 2018 spike (presumably a handful of robotics papers using "embodied AI" in its older academic sense) or restate finding 9 as "the terms re-emerge in policy documents from 2024".

**M7. Figure defects a reader will notice.**
- F24 caption (report and paper) says the figure shows "all documents and governance instruments only"; the image has one panel (all documents). Finding 6 quotes numbers from the missing panel (60.3% vs 30.6%). Add the panel or fix the caption.
- F34: the legend box sits on top of the data for the bottom two rows ("Ethics principles", "Human robot interaction"), which happen to be the two largest declines. Move the legend.
- F31: region labels ("USA", "Europe", "Oceania") are drawn over the dendrogram lines.
- F06: legend says "Technical standards (n=7)"; text says 10 (three undated). Put "10 (7 dated)" in the legend.
- F20: twenty rows with asterisks and "Holm correction" in the title; the asterisks are on 17 of 20 rows so they carry no information. Drop them and say in the subtitle "all differences except accountability, trust and conformity are larger than chance would produce".

**M8. "Which country leads?" is never answered, and the honest answer is a finding.**
*Location:* section 3.4; Table 4.
*Problem:* The report ranks the UK first by documents (142) and then says counts "reflect the collectors' reach as much as national activity", which leaves the reader with nothing. Counting robot-specific rules, the maximum any country has is four (Japan, United States), then three (China, Israel). Nobody leads.
*Fix:* Say it: "No country has more than four robot-specific instruments in the collection. The countries with binding robot rules are an unexpected list: El Salvador, the United Arab Emirates (Dubai), Taiwan, Argentina, plus the EU and the United States by way of general AI law." Drop the document-count league table from anything public-facing; it measures the collectors.

**M9. "The only general robotics statute in force" will be read as "the world's only", and that is wrong.**
*Location:* section 6, Latin America bullet; executive summary finding 2.
*Problem:* South Korea's Intelligent Robots Development and Distribution Promotion Act (2008) is in force, is cited by five documents in this very corpus (Table in section 5.7, "Korea Intelligent Robots Act: 5"), and is named in the paper's own introduction. It is simply not captured as a document. A Korean reader, or any robot-law academic, will flag this in the first hour.
*Fix:* "the only general robotics statute *captured in this collection*; South Korea's 2008 Intelligent Robots Act is the notable absence". Add a "known absences" list (Korea 2008, Japan's robot safety guidelines, China's 2023-25 humanoid standards and guidance) to the limitations box.

**M10. China and Chinese-language sources are the collection's largest blind spot, and the humanoid story leans on them.**
*Location:* section 3.5 (languages), section 6 (Asia), finding 9.
*Problem:* Chinese is not among the eight languages listed (Spanish, Portuguese, French, Korean, Arabic, Russian, Japanese follow English); China has 33 documents, 3 robot-specific instruments. Yet finding 9 attributes the humanoid surge to "Asian and Middle Eastern industrial strategies" and the Shanghai plan is cited repeatedly. Any technology journalist will ask: where are Beijing's humanoid standards, the MIIT guidance, the Shenzhen and Beijing plans?
*Fix:* Say explicitly that Chinese-language documents are essentially absent (give the count) and that conclusions about Asia rest on Japan, Korea, Taiwan, Singapore, India and a handful of English-language Chinese documents.

**M11. Percentages over tiny denominators are presented as if precise.**
*Location:* findings 3 and 5; Table 7; Table 9; Figure 18.
*Problem:* "3.2% of instruments" is two documents. "85.7% of binding instruments mention physical safety" is six of seven. "46.0%" is 29 of 63. The gap index "+39.9" has one decimal place on a quantity the paper's own limitations say "should be read as a direction and order of magnitude".
*Fix:* Where n < 30, give counts, not percentages ("2 of 63 rules; 219 of 509 papers"). Round the gap index to whole points or drop it in favour of the two shares. In Figure 18 add the count next to the instrument dot for the top and bottom rows.

**M12. 2026 is a partial year and the summary does not say so.**
*Location:* findings 8 and 9; section 7; paper limitations (where it is admitted).
*Problem:* The report is dated 30 October 2026. "9.7% of 2026 documents" and the 2025-26 vs 2020-24 comparison are presented without the partial-year flag, and the 2027 record (see C2) suggests year inference is noisy.
*Fix:* "2026 (to October)" wherever 2026 appears; note that year was inferred from content for 389 documents.

**M13. There is no human angle: not one named robot, not one company, and the named laws are listed rather than told.**
*Location:* whole package. I searched the report and paper for Optimus, Tesla, Figure, Unitree, Boston Dynamics, Atlas, Digit, Waymo, Pepper, Paro: zero hits.
*Problem:* A reader arrives thinking of Optimus, Figure 02, Unitree's G1, Waymo, the robot vacuum in their hallway. The package never meets them there. The named laws are gold (El Salvador's statute; Brazil's humanoid bill, which, per the dashboard drawer, bans sales to minors, requires an emergency shutdown and tamper-proof logs and amends the penal code; Taiwan's factory-robot hazard rules; Dubai's self-driving law) but appear as list items.
*Fix:* Open the brief with one of these. Sample lead: "In June 2025 El Salvador became the first country with a law that governs robots as robots. Everywhere else, the rules that bind a humanoid, a surgical arm or a delivery robot were written for cars, factories, aircraft or medical devices." Add a sidebar "Three laws you have not heard of" and, if the corpus permits, connect robot types to products readers know ("companion robots such as Pepper and Paro", "humanoids such as Optimus and Figure") while being clear that the study did not code by product.

**M14. "What does this mean for me?" is unanswered.**
*Location:* conclusions and discussion address "governance practice" only.
*Fix:* Add a short "if you are..." box: a factory worker beside a cobot (your protection is ISO 10218/15066 and, in the EU, the Machinery Regulation); someone buying a companion robot for a parent (the only rule that reaches it is data-protection law); a city buying delivery robots (nothing robot-specific; road and product law); a hospital buying a surgical robot (medical-device law, the AI Act's medical annex). Each is supported by section 8.

**M15. Claims a fact-checker would challenge as overblown.**
- Paper conclusion: "its first quantitative map". Priority claims invite rebuttal (Corrêa et al. 2023 and others have coded hundreds of AI documents; robot-law bibliometrics exist). Say "the first at this scale that separates embodied from general AI".
- Paper title: "across 110 jurisdictions". Many of the 110 have one or two documents; Europe is 44% of the corpus. Use "1,703 documents from eight world regions".
- "Autonomy-level control is discussed everywhere and specified nowhere" (conclusion 2): the table shows 6-8% specification in soft law, drafts and research. "Almost nowhere".
- Paper discussion: standards "are cited by almost nobody". Section 5.7 shows ISO 13482 and ISO 10218 are cited; give the numbers instead.
- Finding 10: "reliable enough to support these comparisons" (see C4).
- Table 13 lists "Asimov's Laws of Robotics" as an instrument cited (twice). Fiction in a list of governance instruments will be quoted back at you; footnote it or remove it.

### Minor

**m1. Internal project labels leak into public-facing titles.** "Stage 2", "Stage 1", "CEI *AI Robotics (Filtered Sources)* collection", "prompt hash 8d4d83e9", "scripts/01 to scripts/17". Keep in the supplement; remove from the summary, abstract and dashboard header.

**m2. Two different titles.** The paper's "Governing machines that act in the world" is good and human; the report's "Global governance of embodied AI and robotics: a quantitative analysis of 1,703 documents" is not. Use the paper's title everywhere.

**m3. "Embodied AI" is used as if the reader knows it.** Define it in the first sentence of anything public: "AI in a body: robots, self-driving vehicles, drones, surgical and factory machines".

**m4. The sign of the gap index is unexplained in the summary.** Positive means more research than rules. Say "research-heavy" and "rules-heavy" in words.

**m5. Accessibility of figures.** The blue/orange pair is colour-blind safe and dark variants are legible (checked F18, F31). But significance is encoded by asterisks only, n-labels in F05 are light grey on white, F31 dark mode draws the 0.00 diagonal in black on near-black, and all figures use axis text at roughly 11-12 px when rendered at column width. Set a 12 pt floor and encode significance in words.

**m6. Section 10's conclusion 1 is a 60-word sentence of acronyms** ("ISO 10218, 13482, 15066, 3691-4, 8800; the Machinery Regulation; Taiwan's rules"). For a general reader: "a handful of ISO safety standards for factory, collaborative and care robots, the EU's machinery rules, and Taiwan's workplace rules".

**m7. "Non-English documents are more often binding (21.3% vs 9.7%)"** (section 3.5) is one of the most interesting lines in the report and appears nowhere in the summary. It tells the reader where the law actually lives.

---

## 3. Proposed structure for a one-page plain-language brief

Working title: **"Who governs the robots? What 1,703 documents from around the world say."**

1. **Lead (3 sentences).** El Salvador's 2025 law as the hook; the sentence-long story; what the study did ("we had an AI model read 1,703 laws, standards, strategies and research papers from eight world regions and label each one").
2. **The big number.** Six binding laws reach robots as robots; one is a robotics statute. Boxed: 1,703 documents, 674 about robots, 63 rules, 6 binding, 1 robotics law.
3. **Who writes the rules.** Three in four robot-governance documents are academic papers. The texts that actually specify what is safe are ISO standards (physical safety set out in detail in 83% of standards, 43% of laws, 9% of guidance).
4. **The mismatch.** Companion robots: 43% of research, 3% of rules. Self-driving cars: 12% of research, 46% of rules. One chart: Figure 18, retitled.
5. **Humanoids.** 143 documents, 12 policy papers, zero binding laws, one bill (Brazil, 2026: bans sale to minors, requires a kill switch).
6. **The unanswered question.** "How much control may a robot keep?" raised in about 40% of documents of every type, specified in detail in under 8%.
7. **Where.** Europe, the US and Oceania sound alike; the Middle East governs through liability; the ISO layer through certification. No country has more than four robot-specific instruments.
8. **What is changing.** Since 2025: industrial policy up 13 points, human oversight up 12, cybersecurity up 10; ethics and human-robot interaction down 14-16. "Physical AI" from 1% to 10% of documents.
9. **What it means for you.** Four one-line scenarios (worker, carer, city, hospital).
10. **Read with care (box).** 44% of documents are European, 78% English, Chinese-language sources essentially absent; the collection sought research on robots and laws on AI in general, so the research-to-law ratio is partly by design; every label was assigned by an AI model and checked by a second AI model, not by people; 2026 is to October only.

---

## 4. Glossary: the 12 terms a general reader most needs

1. **Embodied AI / physical AI** — AI that controls a machine with a body: robots, self-driving vehicles, drones, surgical and factory machines. Contrast with AI that only produces text, images or decisions on a screen.
2. **Governance instrument** — any official text meant to steer behaviour: a law, regulation, bill, national strategy, guideline, code of conduct or technical standard. Research papers and news articles are not instruments.
3. **Binding vs soft law** — binding: breaking it has legal consequences (statutes, regulations, decrees). Soft law: voluntary guidance, principles, strategies and codes that nobody can be fined for ignoring.
4. **Technical standard** — a detailed, voluntary engineering specification (for example ISO 10218 for factory robots, ISO 13482 for care robots) that says how to make a machine safe; laws often make them binding by pointing to them.
5. **Conformity assessment** — the pre-market check (testing, certification, the CE mark in Europe) that a product meets the safety rules before it may be sold.
6. **Mention vs "operationalise"** — a document *mentions* a principle if it names it; it *operationalises* (in this review: "sets out in detail") a principle if it says what must be done, by whom, and how it is checked.
7. **Governance mechanism** — the tool a rule uses to get its way: an audit, a licence, a liability regime, a sandbox, an oversight body, a ban, a funding programme.
8. **Governance gap index** — the share of research papers about a robot type minus the share of rules about it. Positive: studied more than governed. Negative: governed more than studied.
9. **Cohen's kappa** — a score from 0 to 1 for how often two readers (here two AI models) gave the same label, after discounting agreement expected by chance. Above 0.8 is conventionally called "almost perfect"; 0.59 (the score for "stance toward regulation") is "moderate".
10. **Statistically significant / Holm correction** — a difference is "significant" if it is larger than chance would produce. When many comparisons are made at once (here 20 principles), some will look significant by luck; the Holm correction raises the bar to allow for that.
11. **Cramér's V (effect size)** — how *big* an association is, from 0 (none) to 1 (perfect), independent of sample size. Roughly: 0.1 small, 0.3 medium, 0.5 large. A result can be statistically significant yet have a small V.
12. **95% Wilson interval / confidence interval** — the shaded band or error bar around a percentage; the range within which the true figure would most likely fall if the sample were drawn again. Wide bands mean few documents.

Three more that appear in headlines: **odds ratio 1.47 per year** = each year the odds of a document using risk tiers are 47% higher than the year before; **cosine distance** = how different two regions' mix of topics is, 0 identical, higher more different; **lexicon** = a fixed list of keywords searched across the full text, used as a model-free check on the AI's labels.

---

## 5. Dashboard: prioritised usability fixes

Context: `dashboard/index.html` is a single-file, self-contained data browser (3.4 MB, data embedded). The filters, tile recalculation and record drawer all work and the drawer's plain-language summary of each document is the best piece of writing in the package. The problems are the first screen, the markup basics, phone rendering and labels.

**P0: fix before anyone outside the team sees it**

1. **Add the missing HTML basics.** The file begins with `<title>`; there is no `<!doctype html>`, no `<meta charset="utf-8">` and no `<meta name="viewport" content="width=device-width, initial-scale=1">` (only a `claude:viewport-fit-sides` meta). Consequences observed: in dark mode the header rendered as "1594â€“2027" and "CEI AI ROBOTICS CORPUS Â· DOCUMENT DASHBOARD" (encoding mis-sniffed), and at 400 px the page lays out at 980 px (scrollWidth 980 = clientWidth 980), so a phone shows a zoomed-out desktop page with 6 px text.
2. **Kill the trust-destroyers on the first screen.** "Year span 1594–2027" (Shakespeare and a future-dated chapter); first table row dated 2027; rows labelled "Unusable capture", "Not AI" and jurisdiction "Unknown" within the first page. Default-exclude excluded records, clamp years, sort by relevance or by instruments first, and show "2014–2026".
3. **Reconcile the tiles with the report** (see C1): 407/44/611 vs 381/36/674. Either label the tiles "all captured" with a "usable only" toggle, or make usable the default.
4. **Clipped value labels at the right edge of every bar chart.** Europe reads "70" (it is 706), "Social companion robots" reads "22" (228), "Beneficence" reads "117" (1,175). A reader will take the clipped number as the value. Add right padding or put values inside the bars.

**P1: needed for a non-expert to use it**

5. **A "start here" strip under the title**: three to five one-line findings, each a button that applies the matching filter ("Show the 6 binding laws", "Show humanoid robots", "Show companion robots", "Show ISO standards"). Today the page is a database with no story.
6. **Plain-language labels and a one-line "what is this?" on each panel.** "AI scope" options ("Embodied AI robotics general", "General AI with embodied provisions") are codebook strings. "Principle salience" → "Which values do the documents discuss?"; "Substantive (2) / Mentioned (1)" → "discussed in depth / mentioned in passing"; "Governance doc: Instruments only" → "Rules and policies only"; "Soft-law instrument" → "Voluntary guidance"; "Grey literature" → "Reports (NGO, industry, think-tank)"; "Collection set: Robotics sprint / General AI database" → "Collected as: robot-specific / general AI".
7. **Truncated category labels**: "Military autonomous weapo…", "Responsibility & accounta…", "Liability for physical da…", "North America (Canada, Gr…". Widen the label column, wrap, or shorten the names ("Canada & Greenland").
8. **Filter options need counts** ("Binding instrument (44)") so users know what they are about to get, and a visible "N documents match" that updates in the filter bar, not only above the table.
9. **Phone layout for the table.** Even with the viewport fixed, a 12-column table does not fit 400 px; "Primary topic", "Relevance" and "Language" were cut off. Switch to a card list under 600 px (title, year, country, type, one tag) with the drawer for the rest.
10. **Font sizes.** Body and table text is 11-12.5 px, axis labels 11 px. Raise to 14 px for text and 12 px for axes; the tiles can stay at 26-28 px.

**P2: polish**

11. **Relevance column** is a colour-only bar with no number; add "3/3" or words ("high / medium / low").
12. **The region chart** stacks eight colour classes into thin segments nobody can read; collapse to three (binding, voluntary, research/other) with the eight available on hover or in the table view.
13. **Export and share**: no CSV download of the filtered table and no permalink of a filter state. Both are expected of a public data tool and cheap to add (URL hash for filters; Blob download for CSV).
14. **Drawer**: add a link to the source document or URL if captured, and a one-line "summary written by an AI model from an excerpt" disclosure.
15. **Header**: drop "CEI AI ROBOTICS CORPUS · DOCUMENT DASHBOARD · STAGE 1" and the codebook sentence; replace with the one-sentence story and "1,703 documents, 8 regions, labelled by an AI model, checked on a sample".
16. **Dark mode** otherwise reads well (checked at 1280 px); contrast is adequate once the mojibake is fixed.

---

## Appendix: what was checked and how

- Counts of numbers per sentence were computed over the ten executive-summary findings with a short script (774 words, 33 sentences, 113 numeric tokens).
- Dashboard was rendered with Playwright/Chromium at 1280×900 (light and dark) and 400×800 (mobile emulation); screenshots are in the reviewer's scratchpad. One filter (Embodied category = Humanoid & general-purpose → 78 documents, 8 instruments, 0 binding) and one drawer (D0003, Brazil PL 391/2026) were exercised. No console errors.
- Figure defects (F34 legend overlap, F31 label overlap, F24 single panel vs two-panel caption, F06 legend n) were confirmed by viewing the PNGs.
- Searches for named products and companies (Optimus, Tesla, Figure, Unitree, Boston Dynamics, Atlas, Digit, Waymo, Pepper, Paro) returned no hits in the report or paper; "Intelligent Robots Act" appears in the paper's introduction and as a cited instrument (5 citations) but not as a captured document.
