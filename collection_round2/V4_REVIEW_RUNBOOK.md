# Runbook: the v3 adversarial review and the v4 revision (for agents)

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Written 31 October 2026. This is the operational record of how the six adversarial reviews of version 3 were run, how their findings were triaged into data rules, overrides, code changes and narrative rewrites, and how to repeat the cycle on a later version. Read it together with `review/adversarial_review_v3_and_changes_v4.md` (the finding-by-finding log) and `collection_round2/ROUND2_RUNBOOK.md` (how round 2 was collected). The human-readable methods narrative is `report/methods_review_and_revision.md`.

## 1. Outcome in one table

| Step | What was produced |
|---|---|
| Six reviews of v3 (parallel subagents, 14 to 25 minutes each, 300k to 530k tokens each) | `review/v3_reviews/{data_scientist,ai_researcher,iclr,journalist,governance_expert,viz_dashboard}_review.md`; 39 dashboard and figure screenshots in `review/v3_reviews/shots/`; a 165-row classification audit table in the governance review |
| Two follow-up measurements commissioned from the findings | precision audit of 100 random v3 binding embodied instruments (`precision_audit.md`, `precision_audit_sample.csv`); round-2 reliability sample of 160 documents re-annotated by Claude Opus 5.5 and by a Sonnet re-run (`annotations/reliability_round2_*`, `data/reliability_fields_r2*.csv`) |
| Data and definition changes | counting unit (`instrument_unit`, `principal_instrument`, `family_key`), AI-content tiers (`ai_explicit`, `autonomy_terms`), status and class rules, text-hash duplicates, 157 audited overrides (`data/manual_overrides_v4.csv`), reference-list repairs, character-aware excerpt cleaner and re-annotation of 422 CJK documents |
| Analysis changes | collection round as a covariate (T20, T30), within-round contrasts (T20b), within-genre regional divergence (T29b), sparse-cell flags, one instrument denominator, capture-tier rule for depth statistics (T09, F23), stricter coverage criterion (T25) plus the loose one for comparison, precision-vs-rules comparison (T62), counting-unit tiers (T53b), run manifest |
| Figures and dashboard | wrapped computed titles, four false titles replaced, F31 rebuilt, label dictionaries, legends moved, colours fixed; dashboard methods panel generated from data, principal-unit tiles, round-2 tile and view, robot-type and instrument-kind filters, not-AI documents hidden by default, drawer shows unit, family and AI-content flags |
| Narratives | brief, paper, analysis report, supplement, companion report and discovery methods rewritten by writer agents from a written brief (`review/v4_writer_brief.md`), each with a change log (`review/v4_changes_*.md`), then audited for numbers |
| Headline effect | embodied instruments 808 (v3, all legal texts) to 505 principal instruments, 408 robot-relevant; binding embodied 299 to 195 principal (168 robot-relevant, 140 with autonomy or AI provisions, 15 naming AI); precision audit implies about 161 (132 to 190) genuine binding embodied instruments in the v3 set of 299; the pooled "ethical core deficit" of v3 does not exist within round 1 |

## 2. How the reviews were run

Six `general-purpose` subagents were launched in one response with the v4 folder already created (a copy of v3 with paths repointed) so that they could write into `review/v3_reviews/` without touching v3. Each brief had the same skeleton:

1. Role and stance: "You are an adversarial reviewer acting as <perspective>. Be sceptical, specific and verifiable; your job is to find what is wrong, overstated, inconsistent or fragile, not to summarise. Do not edit any project file."
2. What to read, with absolute paths, ordered by importance for that perspective (the journalist starts with the brief and the dashboard; the governance expert with the instrument lists S01 to S05 and T59/T60; the AI researcher with the codebook, the annotation scripts, the stored inputs and the reliability folders; the data scientist with the master table and analysis scripts; the ICLR reviewer with the paper and supplement; the visualisation reviewer with every figure, its data twin, the figure scripts and the dashboard).
3. Context on what earlier rounds fixed (`review/adversarial_review_and_changes.md`, `review/v3_changes_*.md`, the v3 numbers audits) with the instruction not to re-raise fixed items unless the fix is wrong or regressed, and to check that earlier fixes held.
4. A focus list of specific risks to test (definitions and denominators, selection effects of round 2, statistical procedures, de-duplication, time, recomputation of any number).
5. A deliverable format: verdict paragraph; findings table with id, severity (critical/major/minor), location, problem, evidence (recomputed numbers or doc_ids), suggested fix; the five changes that would most improve validity; a final message with counts by severity and the three most important findings. The ICLR brief asked for scores (soundness, presentation, contribution, overall, confidence). The visualisation brief asked for a figure-by-figure table and screenshots saved under `shots/`. The governance brief asked for a classification audit of at least 60 instruments with doc_id-level judgements and a missing-instruments list.

Things that made the reviews useful:
- Reviewers recomputed numbers from `data/master_table.csv` with the definitions in `scripts/analysis_common.py`; every brief said so explicitly and named the definition fields.
- Reviewers read model inputs (`annotations/round2/_inputs/*.txt.gz`) against raw texts; this is how the CJK cleaner defect was found (the AI researcher measured the share of each document that reached the model).
- The six perspectives overlapped on the biggest problems (counting unit, round confound, landing pages, stale dashboard text), which is the signal that a finding is structural rather than taste.
- Each reviewer's final message was short and ranked; the long detail stayed in the file.

## 3. Triage: from findings to changes

Every finding was placed in one of five bins, each with its own implementation path:

| Bin | Examples | Implementation |
|---|---|---|
| Admission or unit rule (applies to every document by a stated regex or threshold) | commencement orders, levies, exemptions, EEA incorporation decisions, corrigenda, stubs under 150 words, catalogue pages, byte-identical texts, standards drafts, mandatory GB standards, CCW working papers, enacted proposals | `scripts/07c_v4_units_and_tiers.py`, run after `07b`; rules are regexes on `title_en` plus capture fields; every rule prints its counts |
| Doc-level correction with a named source | the governance expert's audit table (165 rows with error codes A to G) | parsed into `data/manual_overrides_v4.csv` by `review/v3_reviews/governance_audit_rows.csv` -> field/value mapping (A -> unit dependent; B -> catalogue_page; C -> class from the fix text; D -> status; E -> year; G -> relevance 1 and no categories); applied last in `07c`; every row keeps the reason and source |
| Definition used by the analyses | one instrument denominator; binding on the principal unit; content capture with at least 150 words for depth statistics; round flag | `scripts/analysis_common.py::load()` (`legal_text`, `instrument`, `binding_text`, `binding`, `content_capture`, `words_ok`, `round2`) |
| Analysis or figure change | round covariate, within-round and within-genre tables, sparse-cell flag, stricter coverage criterion, computed titles, legends, label dictionaries | `18_analysis_D.py`, `14_analysis_B.py`, `13_analysis_A.py`, `20_figures_v2.py`, `21_round2_report.py`, `24_precision_vs_rules.py` |
| Measurement gap | no round-2 reliability; promised variants missing; precision never measured; CJK inputs truncated | new runs: `09b_reliability_round2.py`, `09c_reliability_variants.py`, the precision-audit agent, the CJK re-annotation (`04_annotate*.py` cleaner fix, policy tag `cjk_clean=v4`) |

Findings that were reframed rather than fixed (claims withdrawn or rewritten) and the ones not done (human validation; version dating of consolidated statutes; reading the 189 verified-but-unread instruments behind blocked hosts) are listed with reasons in the review log.

## 4. Scripts touched, in run order

```
scripts/04_annotate.py, collection_round2/scripts/04_annotate_r2.py   cleaner: never drop lines carrying CJK characters or CJK punctuation; policy tag cjk_clean=v4
scripts/merge_round2.py                                               unchanged logic (inventory, registry rows, annotation copy); run after the CJK JSONs overwrite annotations/round2 in the round-2 workspace
scripts/05_lexicons.py                                                cached by doc_id + text length (unchanged)
scripts/07_assemble.py                                                overlay order: main, main_clean, gov_extended, round2, cjk_fix
scripts/07b_apply_overrides.py                                        second pass (identical title) and third pass (cross-round, token-sort >= 90 with length guard, or same EU act number) unchanged from v3
scripts/07c_v4_units_and_tiers.py                                     NEW: instrument_unit, principal_instrument, family_key/size/rep, ai_explicit, autonomy_terms (cached in data/ai_content_flags.csv), words_ok, status/class rules, text_hash duplicates, manual_overrides_v4.csv
scripts/analysis_common.py                                            legal_text, instrument (principal), binding_text, binding (principal), content_capture, words_ok, round2
scripts/09b_reliability_round2.py, 09c_reliability_variants.py        NEW
scripts/13_analysis_A.py                                              gap and country tables on the instrument base; T04 gains embodied_instruments_principal and binding_embodied
scripts/14_analysis_B.py                                              T09 on content captures; region thresholds 30
scripts/18_analysis_D.py                                              round covariate; T20b; sparse flags; T30 round rows; T29b; T25 strict; F39/F40/F41 titles
scripts/20_figures_v2.py                                              title wrapping; EMBL and PLUR dictionaries; F04/F06/F08/F23/F28/F31 fixes
scripts/21_round2_report.py                                           T53 on the comparable unit; T53b tiers; both coverage criteria; consistent binding units; narrative strings
scripts/24_precision_vs_rules.py, 23_run_manifest.py                  NEW
scripts/10_dashboard.py                                               principal-unit tiles, round-2 tile/view, robot-type and instrument-kind filters, counting-unit filter, not-AI handling, drawer flags, computed methods panel
scripts/16_build_reports.py                                           v4 titles, captions, new documents
scripts/run_v4.sh, run_v4_post.sh, run_v4_analyses.sh, package_v4.sh  runners and packaging
```

## 5. Measurements added and what they showed

- Round-2 reliability: 160 round-2 documents stratified over standards, EU legal texts, East Asian texts, intergovernmental documents, US texts and other national texts (`collection_round2/data/ids_reliability_round2.txt`, seed 42). Median kappa over single and ordinal fields 0.86 (Opus) and 0.91 (re-run) against the final labels, after the CJK re-annotation. Weak fields: page quality (0.53), stance (0.65), publication stage (0.66), date basis (0.70), solidarity level (0.72), instrument status (0.75).
- Precision audit: 100 of the 299 v3 binding embodied instruments drawn with `numpy.random.default_rng(2026)`; five yes/no criteria judged from the document text by an independent agent; 54% (Wilson 44 to 63) pass distinct + binding + substantive; the rule-based v4 unit passes 61% on the same documents (agreement 0.77, kappa 0.53; 15 documents the rule keeps and the auditor rejects, 8 the reverse). Rules cannot see whether a text has an operative robot provision; the audit can. Report both.
- CJK re-annotation: 57 of 422 CJK documents changed embodied-set membership; "not about AI" fell from 205 to 160.
- Coverage: strict criterion 22 of 39, loose 31 of 39 (v2: 11 and 12).

## 6. Checks that caught errors during the v4 run (repeat them)

- Pandas dtype errors when applying overrides to numeric columns: cast values by column dtype before assignment.
- Waiter loops that `pgrep`/`grep` for a pattern contained in their own command line spin until timeout; use `^python3 ...` anchors, the `[0]4_annotate` bracket trick, or a DONE marker file.
- A re-run of a script with cached results (`18_analysis_D.py`'s `dump_results` loads `results.json` first) can overwrite keys written later by another script (`21`); run `21` and `24` after `18`.
- After changing a definition in `analysis_common.load()`, re-run everything from `13` onward; the digest (`15`) and the dashboard (`10`) read the same definitions.
- After changing the coverage criterion in `18`, align `21`'s own recomputation (it reports both versions).
- Inspect `data/duplicates_removed.csv` and the `07c` unit counts after any rule change; print the family keys with the largest families.

## 7. How to repeat the cycle on v5

1. Copy the project folder, repoint paths with `sed`, delete `scripts/__pycache__`.
2. Launch the six reviewers with the brief skeleton in section 2, pointing them at the new deliverables and at this cycle's review log so that they check whether v4 fixes held.
3. Commission measurements the reviews ask for before rewriting (reliability on any new population; precision on any new instrument set; input-share checks for any new language or source type).
4. Triage findings into the five bins; implement rules in `07c`, doc-level corrections in a new `manual_overrides_v5.csv`, definitions in `analysis_common.load()`, analyses in `13` to `21`.
5. Run `run_v4.sh`-style pipeline; QA figures with a contact sheet and the dashboard with `scripts/shot.js`; fill the review log; launch writers with a written brief; run the numbers audit; build, package, publish, deliver.
6. Budget: reviews about 2.5 million tokens and 2 hours wall-clock in parallel; measurements about 70 USD of annotation; writers and audit about 1.5 million tokens.

## 8. What the writers and the numbers audit caught after the pipeline was "done" (add to the checklist)

- A table the design promised did not exist: `18_analysis_D.py` dropped a whole within-genre item whenever one region had fewer than ten documents, so no T29b file was written and no script complained. Check that every table the review log names exists before writers start (`ls tables/ | grep T29b`); restrict the region set per population instead of skipping items.
- Trend rows promised in the log were absent (proximity and liability in T30). Same check: grep the table for every outcome the narrative will cite.
- Mechanical code-to-value conversion of the expert's audit inverted eleven values (an in-force directive marked superseded; mandatory GB standards marked soft; two lapsed bills marked superseded). Always print the override rows beside the expert's `fix` text and read them; a rule-based parse of free-text fixes is a draft, not a result.
- A title-anchored regex (`^GB \d`) missed standards whose number is at the end of the title; test admission regexes on the full title list and print the misses.
- Round-2 weak-field kappas in the log were copied from an earlier run; after any re-annotation, regenerate every number in the log from the CSVs.
- A claim about which texts a retry recovered was wrong (the EU acts were still 404); state recovery by `doc_id` from `fetch_status.csv`, never from memory.
- Each late correction changed comparable-unit counts (binding embodied texts 282 to 291) after the writers had finished; the numbers audit then fixed 81 values across ten files. Order matters: freeze data, verify the promised tables exist, then launch writers, then audit.
