*Companion to the v3 analysis report. All counts refer to content-analysed documents unless stated otherwise.*

## Summary

The first collection (v2) contained 1,656 documents, of which 65 were governance instruments in the embodied-AI set and 34 were robot-specific. Round 2 searched official legal databases, government repositories, standards catalogues, treaty-body archives and regulator sites for instruments that the collectors had not captured. After de-duplication against the first collection and within the round, 2,075 candidates remained (1,157 from nine specialised collector agents and 918 from scripted harvests of seven legal databases). Text could be obtained for 1,716 of them, and 1,716 were annotated with the same metadata-blind, extended-excerpt policy as v2.

The blind annotation confirms that most additions are instruments rather than commentary: 1346 of the 1611 usable round-2 documents are governance instruments and 647 are robot-specific. Across the merged collection, embodied-AI governance instruments rose from 65 to 808 (x12.4), robot-specific instruments from 34 to 681, and binding embodied instruments from 5 to 299. The coverage audit against the 38 reference instruments moved from 12 captured in v2 to 31 in v3 (still missing: Korea Intelligent Robots Development and Distribution Promotion Act (2008); EU revised Product Liability Directive (EU) 2024/2853; ANSI/RIA R15.06 industrial robot safety; ANSI/A3 R15.08 industrial mobile robots; Korea AI Basic Act (2024/2025, applies Jan 2026); OECD AI Principles (2019, rev. 2024); Taiwan Industrial Robot Hazard Prevention Standards).

{{T53}}

## Where the candidates came from

{{T50}}

{{F50}}

## What could and could not be fetched

{{T51}}

{{T52}}

Candidates without text remain in the inventory (data/round2_inventory.csv) with their metadata but are not part of any content-analysed count. The main losses are catalogue pages behind bot challenges or outside the sandbox network policy (46 candidates on blocked hosts; 273 with HTTP errors or JavaScript-only pages).

## Before and after, by region and robot group

{{F51}}

{{T54}}

{{T55}}

## What the blind annotation made of the additions

{{F52}}

{{T56}}

## Do the collectors' catalogue labels agree with the blind reading of the text?

{{T57}}

{{T58}}

## Newly captured instruments

{{T59}}

{{T60}}

## Method notes and limitations

- Discovery combined nine collector agents (regional, thematic and standards briefs with explicit exclusion lists of the v2 holdings) and scripted harvests of EUR-Lex (CELLAR SPARQL), legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register of Legislation, the US eCFR and the Brazilian Camara API. Title-searched harvests were filtered with an inclusion/exclusion keyword list before fetching; full-text harvests were not.
- Candidates were de-duplicated on normalised URL and on normalised title plus jurisdiction, within the round and against the v2 registry; the assembly step applies a second title-based pass across the merged collection.
- Texts were fetched from the primary URL with a secondary fallback (CELLAR for EUR-Lex, the UN document API for UNODA and undocs links, the ISO committee mirror for ISO catalogue pages, XML for legislation.gov.uk). For ISO and other standards only the public scope or abstract page is available, so those documents are annotated on a short text and are flagged as such in the registry.
- The collectors' shared web-search budget was exhausted part-way through several briefs; later verification relied on direct fetches of official sites. Jurisdictions the agents could not reach from the sandbox (for example legifrance, the Singapore statutes site, Korean law portal, several ministry sites) are under-represented and are listed in the agent reports.
- Annotation used the v2 blind policy (metadata stripped, first 100,000 characters plus middle and tail excerpts), so round-2 and v2 documents are directly comparable; no manual overrides were applied to round-2 rows.
