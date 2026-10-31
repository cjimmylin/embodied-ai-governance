# Candidate instrument CSV schema (one row per instrument; UTF-8; header exactly as below)

candidate_id,title_original,title_en,jurisdiction,subnational,issuer,year,instrument_type,binding_nature,status,robot_types,language,url_primary,url_secondary,source_database,confidence,notes

- candidate_id: <agentprefix>-<3 digits>, e.g. US-001
- jurisdiction: ISO 3166-1 alpha-2 (US, GB, DE, JP, KR, CN, ...), EU for European Union, INT for international/standards bodies
- subnational: state/province/city if applicable (e.g. California, Shenzhen, Dubai), else empty
- instrument_type: one of statute_or_act | regulation_or_decree | bill_or_draft_law | technical_standard | national_strategy_or_action_plan | policy_guideline_or_code_of_practice | ethical_framework_or_principles | intergovernmental_recommendation_or_resolution | consultation_or_white_paper | parliamentary_material | procurement_or_internal_policy | court_decision | government_report_or_review
- binding_nature: legally_binding | voluntary_soft_law | technical_standard_voluntary | technical_standard_mandated | not_applicable (use not_applicable for bills, drafts, consultations, reports)
- status: in_force | published_current | draft_or_bill_under_consideration | consultation_open | adopted_not_yet_in_force | superseded_or_repealed | under_development | unknown
- robot_types: semicolon-separated codes from: industrial_manipulators; collaborative_robots; mobile_industrial_logistics; delivery_robots; professional_service_robots; domestic_household_robots; social_companion_robots; educational_robots; care_assistive_robots; toys_entertainment_robots; sex_robots; surgical_medical_robots; rehabilitation_exoskeleton_prosthetic; biohybrid_or_cyborg; humanoid_general_purpose; autonomous_road_vehicles; drones_uas; autonomous_maritime_or_rail; agricultural_robots; space_or_extreme_environment; military_autonomous_weapons; security_policing_robots; other_embodied
- language: ISO 639-1 of the primary text
- url_primary: the official/primary source URL of the instrument text (government gazette, legislature, regulator, standards body catalogue page). Must have been verified to resolve.
- url_secondary: a second URL (English translation, consolidated version, or an authoritative mirror), optional
- source_database: where you found it (e.g. "Law Library of Congress report", "NCSL AV tracker", "EUR-Lex", "ICAO UAS toolkit", "web search")
- confidence: high (instrument verified at the primary URL) | medium (verified via a secondary source) | low (inferred; needs checking)
- notes: one line: what the instrument does for embodied AI (max 200 characters)

Rules: governance instruments only (laws, regulations, bills, standards, strategies, official guidelines, resolutions, formal national positions, official reports); no news, no research papers. One row per instrument (a law amended several times is one row; a regulation and its implementing ordinance are two rows). Prefer instruments with substantive provisions on physical AI (robots, vehicles with automated driving, drones, exoskeletons, surgical robots, delivery robots, humanoids, autonomous weapons). Do not include instruments already in existing_instruments.csv (match on title or URL); if unsure, include and set notes to "possible duplicate of Dxxxx".
