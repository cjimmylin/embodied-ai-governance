*Companion to the analysis report. Round 3 executed the items of the round-3 plan that an agent can do alone: re-fetching blocked and missing instruments by official alternative routes, a harvest with service-robot terms, a full-text re-read of truncated statutes, a supplementary schema (whom an instrument binds, dates, legal effect of standards, provision dating), a second precision audit, and a source split of the governance-gap index. Items that need a person are listed in HUMAN_ASSISTANCE.md.*

## Summary

Round 3 added 160 usable documents to the collection: 108 round-2 candidates whose text could now be read (80 of them principal binding embodied instruments) and 52 new documents, 9 of them reference-list instruments fetched from their titles and the rest from the harvest with service-robot, care, exoskeleton, humanoid and collaborative-robot terms and EuroVoc concepts. The harvest itself added little: of its 43 usable documents only 8 fall in the embodied set and 8 are principal instruments, so the open legal databases hold few service-robot instruments that rounds 1 and 2 had not already found, and the gains of round 3 come from reading texts that were already known. Of the reference-list instruments, 4 are now principal embodied instruments in the collection. The collection now holds 3,320 usable documents, 1,704 in the embodied set, 598 principal embodied instruments and 278 principal binding ones (v4: 3,165 / 1,603 / 505 / 195). Of the 206 round-3 targets, the collectors saved a text for 121, found 74 blocked at official hosts, judged 9 irrelevant and could not locate 2 (Table 80).

The collectors' own reports, with the alternative routes that worked (Publications Office CELEX resolver for EUR-Lex, state legislatures' PDF endpoints, Riigi Teataja and legislation.govt.nz rendered pages, the Kremlin acts bank, Gazzetta Ufficiale issue PDFs) and the metadata corrections they noticed (act numbers, repeal dates, mislabelled gazette copies), are in collection_round3/status/report_*.md.

{{T80}}

The blocked targets are the manual-download list for a person with ordinary browser access (Table 81).

{{T81}}

## Full-text re-reads of truncated instruments

The excerpt policy stops at 110,000 characters; 104 principal embodied instruments exceeded it. Re-reading them with up to 400,000 characters under the same prompt left the document class unchanged in 96.2% and the relevance rating in 87.5%; principle levels agreed exactly in 89.7% of field-document pairs, and the full text raised a level in 6.4% of pairs (Table 74). The full-text labels replace the excerpt labels for these documents. The documents whose set-defining labels changed are listed in Table 75.

{{T74}}

{{T75}}

## Supplementary fields: whom a rule binds, when it applies, what a standard's legal effect is, when the robot provision arrived

A second, smaller annotation pass asked five questions the codebook had not asked, of every principal embodied instrument, with a quote required for every answer. Among the 278 principal binding instruments the text names whom the rule binds in 267 cases (operators or deployers and public bodies most often; Table 71), an entry-into-force date in 181, a later application date in 49 and a repeal or expiry date in 15 (Table 70). The year the robot-relevant provision arrived could be given for 226 binding instruments, but mostly because the whole instrument is about such systems (182 cases), so the provision year is the document year; an amendment history in the text dated the provision in 26 cases and the provision itself stated its date in 16; in 54 the year could not be determined from the captured text. Only 7 binding instruments carry a provision year later than the document's recorded year (Table 73). The consolidated statutes dated before 2010 are the case that matters for trend analyses, and for 15 of the 16 the captured consolidation carries no amendment history, so the model could not date their automated-driving or drone articles: these need a person with the amendment record (HUMAN_ASSISTANCE.md, the legal-check item). Among the technical standards, 45 state on their public page that they are voluntary and 1 that they are harmonised or designated under a law (Table 72).

{{T70}}

{{T71}}

{{T72}}

{{T73}}

## Second precision audit

An independent agent re-read a random sample of 100 of the 195 principal binding embodied instruments of v4 (seed 2027) against the five criteria of the v3 audit. Shares: distinct instrument 85%, binding 99%, substantive embodied provisions 76%, autonomy or AI content 73%, explicit AI 9%; all three main criteria jointly 73% (Wilson 64 to 81), implying about 142 genuine instruments (124 to 157) in the set of 195. The v3 audit of the earlier set of 299 found 54% (44 to 63). The sample was drawn from the v4 set before round 3; applied to the v5 set of 278 principal binding instruments the same share implies about 203 (177 to 224). The failures are mostly binding instruments without a substantive embodied provision (a drone or robot named only in a list of functions or definitions), then register, tracking and catalogue pages and date-only amendments that the counting-unit rules let through. The audit report with the failing documents is review/v5_audit/precision_audit_v5.md.

## The governance gap, split by collection source

Because round 2 searched legal databases for drones, vehicles and machinery, the instrument side of the governance-gap index could inherit the search terms. Table 7b computes the index separately against the round-1 instruments (web search of robot-specific and general-AI sources) and against the round-2 and round-3 instruments (database harvests and recovered texts). The gap is positive against both sources for social companion robots (+35 and +41 points), humanoid general purpose (+6 and +20 points), educational robots (+5 and +6 points), sex robots (+3 and +4 points), other embodied (+3 and +4 points): research attention to these machine classes exceeds their share of instruments whichever way the instruments were found, so the headline gap for service, companion and humanoid robots is not an artefact of the round-2 terms. The instrument surplus is present against both sources for drones uas (-31 and -38), autonomous road vehicles (-55 and -26), mobile industrial logistics (-16 and -5), agricultural robots (-18 and -3), autonomous maritime or rail (-6 and -4), rehabilitation exoskeleton prosthetic (-2 and -2). The gap appears against only one source for care assistive robots (+0 against round-1 instruments, +21 against harvested ones): for these classes the round-1 robot-specific sources supplied standards and guidance that the database harvests did not, so the size of the gap depends on how instruments were found. The sign flips for surgical medical robots (-8 against round-1 instruments, +10 against harvested ones), professional service robots (-15 against round-1 instruments, +10 against harvested ones), collaborative robots (-16 against round-1 instruments, +3 against harvested ones), industrial manipulators (-41 against round-1 instruments, +3 against harvested ones): the round-1 instrument set, drawn from robot-specific sources, is rich in standards for these classes, and the harvested set is not, so for them the gap depends on the source and should not be read as a finding.

{{T07b}}

## What round 3 did not do

No person labelled any document (the human-validation kit is in data/human_validation/); hosts that refuse the identified crawler were not circumvented (Table 81 lists them for manual download); technical standards are still read from scope pages; and the labels of the new and recovered documents carry the same model limits as the rest.
