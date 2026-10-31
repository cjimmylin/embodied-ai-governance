# Change log: supplement, v2 -> v3

Numbers are from `report/results_digest.md`, `data/results.json`, `tables/*.md`, `data/round2_inventory.csv`, `data/overrides_applied.csv`, `data/duplicates_removed.csv` and `data/master_table.csv` (column count and round-2 annotation metadata).

## Structure

- Title "(v2)" -> "(v3)"; S1 heading "what changed in v2" -> "what changed in v3".
- S1 pipeline table: rows added for `merge_round2.py` (round-2 registry rows, inventory) and `21_round2_report.py` (T50-T60, F50-F52, companion report); annotation row now names the `round2` run; override row notes the cross-round deduplication; `run_v3.sh` named as the driver.
- S1: new "What changed in v3" paragraph (2,075 candidates, 1,716 texts, registry 3,419 rows, 3,291 annotated, 3,148 usable, 81 cross-round merges, T50-T60 and F50-F52 added, audit re-run, reliability samples unchanged).
- S1 annotation paragraph: round-2 runs use the same model, prompt hash `8d4d83e909f0` and excerpt policy string; all 1,611 usable round-2 rows carry them; no overrides on round-2 rows; collector metadata never shown to the model.
- S4.1: sentence added that the five samples (160, 161, 160, 160, 351) are round-1 documents and unchanged in v3 (no n changed).
- S4.5: human-validation protocol now also stratifies by collection round and includes scope-text-only standards.
- New S4.6 "Round-2 documents: the collectors' catalogue metadata versus the blind annotation": binding nature 93% / kappa 0.85 (n = 1,593), jurisdiction 98% (n = 1,609), year within one year 93% (n = 1,527), class 80% / kappa 0.71 (n = 1,593); points to T57 and T58 in the companion report (not re-embedded).
- S5: introduction paragraph added for the instrument lists (see below); mentions `R2-` identifiers, T59 and T60 and the scope-text status of round-2 standards.
- S6: audit summary 10 of 38 captured (v2) -> 29 of 38; the eight cited-but-not-captured and the one neither are named (T25).
- S7: last row now says the AV and drone regulation reviews document the sectoral layer that round 2 brought into the collection.
- S8: corrections stated as 79 rows on 27 round-1 documents; duplicates 128 rows, 81 cross-round (v2 text gave no counts in S8).
- New S9.1 "Collection round 2: inventory and collector reports": describes `data/round2_inventory.csv` (2,075 rows; columns; 1,716 content-analysed; 359 without text), T50-T52 and `COLLECTOR_REPORTS.md` in the round-2 workspace.
- S12 figure index: rows 50, 51, 52 added; F37 marked as round-1 lists only.

## Numbers changed

- Instrument lists: S01 binding instruments (v2: five) -> 299 (223 regulations/decrees, 72 statutes, 3 court decisions, 1 treaty); S02 soft law and standards (v2: 44 + 8) -> 434 (238 standards, 196 others); S03 drafts (v2: 8) -> 71 rows; S04 reports (v2: 24) -> 90; S05 general-AI instruments with embodied provisions (v2: 31) -> 181 rows, of which 127 counted in the embodied set (T33).
- Datasheet composition: "1,703 captured documents reduced to the canonical set" -> 3,419 registry rows (round-1 captures plus 1,716 round-2 texts), 3,291 annotated, 3,148 usable; "180+ fields" -> 185 fields; "Chinese-language documents essentially absent" -> 8%, almost all from one round-2 harvest; Europe and English over-representation quantified (42%, 75%); inventory of 2,075 candidates (359 without text) added.
- Datasheet collection process: round-1 numbers unchanged (2,557 files; 266 not captured); round-2 process added (nine agents, seven harvests, de-duplication, fetch fallbacks, standards as scope text).
- Datasheet labelling: round-2 documents annotated under the v2 blind policy; corrections apply to round-1 documents only; collector-metadata cross-check added.
- Datasheet distribution: round-2 URLs in `data/round2_inventory.csv` added.
- Coverage audit: 10 -> 29 of 38 captured; cited-not-captured 8; neither 1.

## Kept unchanged (verified)

- Reliability tables T26, T27, T27b, T35 and the text of S4.1 to S4.4 (same samples; n = 160 / 161 / 160 / 160 / 351; "483 texts" with a visible cover block).
- Statistics paragraph, codebook and taxonomy embeds, S7 rows other than the last, S10 extended tables, S9 stage-1 checkpoint embed, licence and ethics entries.

## Dropped

- No v2 sentence was dropped without replacement; the v2 phrase "Chinese-language documents are essentially absent" was replaced rather than removed.

## Corrections after audit (review/v3_numbers_audit_brief_paper.md)

- S6 coverage audit: "29 of 38 captured (10 in v2); eight cited but not captured (incl. Executive Orders 14110 and 14179)" -> "31 of 38 (12 in v2); six cited but not captured (PLD 2024/2853, Korea Intelligent Robots Act 2008 and AI Basic Act, ANSI/RIA R15.06, ANSI/A3 R15.08, OECD AI Principles); one neither (Taiwan)"; sentence added that D0915 and D0918 are in the collection and that the patterns in `data/reference_instruments.csv` were corrected. The embedded T25 was regenerated (seeded re-run of `scripts/18_analysis_D.py`) and now agrees: 31 captured, 6 cited but not captured, 1 neither.
- S5 instrument-list introduction: round-2 robot-specific instruments 655 -> 647 (T60; embodied-set rule). The 127 general-AI instruments with robot provisions and the 677-of-804 figure for T33 are unchanged.
- S1 and S8 duplicates: "81 round-2 candidates merged into round-1 documents" -> "79 round-2 candidates and 49 round-1 captures removed as duplicates" (128 rows in `data/duplicates_removed.csv`).
- No term-trend, stance or mechanism-share numbers appear in the supplement; nothing else changed.

### Second audit (review/v3_numbers_audit_report_supplement.md, part 2)

- S5: the S05 sentence no longer equates S05 with the 127-instrument tier. Now: S05 holds the 181 usable governance documents with ai_scope general-AI with embodied provisions (64 binding, 90 soft-law, 23 drafts, 4 reports); 166 carry a robot-type label, 169 are in the embodied set, 66 at relevance 2 or 3; 100 of the 127 "with provisions" tier members are in S05, the other 27 carry other scope labels (19 embodied-AI specific, 8 general-AI only; verified on the master table).
- S5: "S03 the 71 proposals" -> "the 71 ... that carry the governance-document flag (75 draft-class instruments in all)".
- S11: "seven scripted harvests of legal databases" -> "scripted harvests of seven legal databases (eight runs)".
- S6: "(12 in v2)" -> "(12 in v2 by the same corrected patterns; the v2 audit reported 10)".
