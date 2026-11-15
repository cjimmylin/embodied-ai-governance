#!/usr/bin/env python3
"""Database export: one row per usable document with every collection, metadata and annotation field,
plus the analysis flags the reports count by. Writes
  data/export/embodied_ai_governance_documents.csv   (UTF-8, comma-separated, RFC 4180 quoting, header row)
  data/export/data_dictionary.csv                     (column, type, description, allowed_values)
Conventions: multi-value fields are JSON arrays; booleans are true/false; missing values are empty;
years and counts are integers; dates are as stated (ISO where the document gives a full date).
Usable = the 3,328 documents the analysis counts (readable text, not an error page, not classed unusable)."""
import json, os, re, sys
import pandas as pd
B = "/home/user/embodied-ai-governance-v5/"
sys.path.insert(0, B + "scripts")
from analysis_common import load

OUT = B + "data/export/"
os.makedirs(OUT, exist_ok=True)
m = load()
m = m[m.usable].sort_values("doc_id").reset_index(drop=True)

# how the source URL was obtained
su = pd.read_csv(B + "data/source_url_recovery.csv", dtype=str, keep_default_na=False).set_index("doc_id")
def url_basis(d):
    if d in su.index and su.at[d, "used_in_master_table"] == "True":
        return su.at[d, "basis"]
    return "collector manifest or harvest record"
m["source_url_basis"] = m.doc_id.map(url_basis)

DROP = ["_cost_usd", "_excerpt_cleaned", "_excerpt_extended", "_fulltext_v5", "family_key", "words_ok", "annotated",
        "text_usable", "usable", "content_capture", "setname", "round2", "round3", "legal_text", "binding_text", "year"]
RENAME = {"_model": "annotation_model", "_prompt_hash": "annotation_prompt_hash", "_policy": "annotation_policy",
          "gov": "in_governance_set", "embodied_set": "in_embodied_set", "general_set": "in_general_ai_set",
          "binding": "principal_binding_instrument", "instrument": "principal_instrument_unit", "period": "analysis_period"}
m = m.drop(columns=[c for c in DROP if c in m.columns]).rename(columns=RENAME)
if "principal_instrument_unit" in m.columns and "principal_instrument" in m.columns and m.principal_instrument_unit.equals(m.principal_instrument):
    m = m.drop(columns=["principal_instrument_unit"])

LISTS = ["regions_listed", "sets_listed", "oa_authors", "oa_author_countries", "oa_topics", "countries_discussed",
         "embodied_categories", "application_sectors", "governance_topics", "governance_mechanisms",
         "named_instruments_referenced", "bound_parties", "embodied_l1"]
def to_list(v):
    if v is None or (isinstance(v, float) and pd.isna(v)) or str(v).strip() == "":
        return ""
    return json.dumps([x.strip() for x in str(v).split(";") if x.strip()], ensure_ascii=False)
for c in LISTS:
    if c in m.columns:
        m[c] = m[c].map(to_list)

INTS = ["collection_points", "n_files", "text_chars", "words", "oa_year", "oa_cited_by", "oa_n_authors", "pub_year", "pub_month",
        "year_final", "robot_provision_year", "lex_words", "ai_explicit_n", "autonomy_n", "family_size"]
for c in INTS:
    if c in m.columns:
        m[c] = pd.to_numeric(m[c], errors="coerce").round().astype("Int64")
for c in m.columns:
    if m[c].dtype == bool or set(m[c].dropna().unique()) <= {True, False} and m[c].dropna().size and m[c].dtype == object:
        m[c] = m[c].map(lambda v: "" if pd.isna(v) else ("true" if bool(v) else "false"))

front = ["doc_id", "title_en", "title_clean", "source_url", "source_url_basis", "authors_or_issuer", "issuer_type", "jurisdiction_country",
         "jurisdiction_country_name", "study_region", "year_final", "language", "doc_class", "doc_type", "in_embodied_set",
         "in_governance_set", "principal_binding_instrument"]
cols = [c for c in front if c in m.columns] + [c for c in m.columns if c not in front]
m = m[cols]
m.to_csv(OUT + "embodied_ai_governance_documents.csv", index=False, encoding="utf-8")

# ---- data dictionary
base = pd.read_csv(B + "data/data_dictionary.csv").set_index("column").description.to_dict()
schema = json.load(open(B + "codebook/schema.json")); props = schema.get("properties", schema)
supp = json.load(open(B + "codebook/supplement_v5_schema.json")).get("properties", {})
def enum_of(c):
    p = props.get(c) or supp.get(c) or {}
    e = p.get("enum") or (p.get("items") or {}).get("enum")
    return " | ".join(str(x) for x in e if x is not None) if e else ""
D = {
 "source_url": "Web address of the document: the collectors' URL, or for 400 documents first collected without one, the URL recovered in November 2026 (see source_url_basis)",
 "source_url_basis": "How source_url was obtained: collector manifest or harvest record; or, for documents recovered in November 2026, the saved page's own address tag, team source list, DOI (checked against Crossref), web search, or re-collected",
 "sets_listed": "All collection sets the merged files came from (JSON array)",
 "oa_matched": "Matched to an OpenAlex record", "oa_match_type": "How the OpenAlex match was made (doi or title)",
 "oa_year": "Publication year per OpenAlex", "oa_date": "Publication date per OpenAlex", "oa_type": "OpenAlex work type",
 "oa_venue": "Venue per OpenAlex", "oa_cited_by": "OpenAlex citation count at harvest", "oa_first_author_country": "First author's institution country per OpenAlex",
 "oa_n_authors": "Number of authors per OpenAlex", "oa_authors": "Authors per OpenAlex (JSON array)", "oa_author_countries": "Author institution countries per OpenAlex (JSON array)",
 "oa_doi": "DOI per OpenAlex", "oa_id": "OpenAlex work id", "oa_topics": "OpenAlex topics (JSON array)",
 "title_clean": "Title in the original language, cleaned (annotation)", "title_en": "Title in English (annotation; translated where needed)",
 "pub_year": "Publication or adoption year stated or inferred by the annotation", "pub_month": "Publication month (annotation)",
 "date_basis": "Where the date came from (annotation)", "doi": "DOI of the document itself (annotation; distinct from DOIs it cites)", "venue": "Journal, gazette, website or outlet (annotation)",
 "embodied_categories": "Kinds of embodied AI or robot the document addresses (JSON array; annotation)", "primary_embodied_category": "Main embodied category (annotation)",
 "governance_topics": "Governance topics substantively addressed (JSON array; annotation)", "primary_topic": "Main governance topic (annotation)",
 "annotation_model": "Model that produced the annotation", "annotation_prompt_hash": "Hash of the codebook prompt used", "annotation_policy": "Excerpt policy used for the annotation (slice sizes, metadata-blind flag)",
 "n_embodied_categories": "Count of embodied_categories", "n_topics": "Count of governance_topics", "n_mechanisms": "Count of governance_mechanisms",
 "principles_sum": "Sum of the 20 principle scores (0-40)", "n_principles_substantive": "Principles scored 2 (substantive)", "n_principles_any": "Principles scored 1 or 2",
 "jurisdiction_country_name": "Country or body name for jurisdiction_country", "continent": "Continent of the jurisdiction", "un_subregion": "UN M49 sub-region of the jurisdiction",
 "study_region": "Region used in the analysis (from jurisdiction, not the collectors' folder)", "year_final": "Year used in the analysis (annotation, else metadata)", "year_source": "Source of year_final",
 "binding_nature_prospective": "Binding once adopted (bill or draft of binding law)", "capture_tier": "Quality of the captured text (substantive, partial, landing page)",
 "instrument_unit": "Counting unit: principal, amendment, or a paperwork type excluded from instrument counts", "text_hash": "Hash of the captured text (duplicate detection)",
 "ai_explicit_n": "Explicit AI-term mentions in the full text", "autonomy_n": "Autonomy and automation term mentions in the full text",
 "ai_explicit": "At least two explicit AI mentions", "autonomy_terms": "At least two autonomy terms, or ai_explicit", "principal_instrument": "Instrument-class text counted as a principal instrument or amendment",
 "family_size": "Number of captures of the same instrument family (versions, renewals, parts)", "family_rep": "Representative capture of its family (used for family-level counts)",
 "bound_parties": "Who the instrument binds (JSON array; supplementary pass, principal instruments only)", "bound_parties_text": "Who it binds, in the model's words",
 "entry_into_force_date": "Entry-into-force date (supplementary pass)", "applicability_date": "Date the obligations apply (supplementary pass)", "repeal_or_expiry_date": "Repeal or expiry date (supplementary pass)",
 "legal_effect_of_standard": "For standards: how law gives them effect (supplementary pass)", "robot_provision_year": "Year the robot-relevant provision was added (supplementary pass)",
 "robot_provision_basis": "How the robot-relevant provision was dated (supplementary pass)", "supp_confidence": "Supplementary-pass confidence (0-1)", "supp_model": "Supplementary-pass model", "supp_prompt_hash": "Supplementary-pass prompt hash",
 "embodied_l1": "Top-level embodied groups (JSON array)",
 "in_embodied_set": "In the embodied-AI (robot) set used by the analysis: relevance >= 2 or any embodied category, and about AI",
 "in_general_ai_set": "In the general-AI comparison set", "in_governance_set": "Governance document (is_governance_document)",
 "principal_binding_instrument": "Counted as a principal binding instrument (the headline binding unit)", "analysis_period": "Period bin used in trend analyses",
}
rows = []
for c in m.columns:
    desc = D.get(c) or base.get(c) or base.get(c.lstrip("_"))
    if not desc and c.startswith("pr_"):
        desc = f"Principle '{c[3:].replace('_', ' ')}': 0 absent, 1 mentioned, 2 substantive or required (annotation)"
    if not desc and c.startswith("lex_p_"):
        desc = f"Lexicon rate per 1,000 words for principle terms '{c[6:-3].replace('_', ' ')}'"
    if not desc and c.startswith("lex_") and c.endswith("_pk"):
        desc = f"Lexicon rate per 1,000 words for '{c[4:-3].replace('_', ' ')}' terms (multilingual patterns in codebook/lexicons.json)"
    if not desc and c == "lex_words":
        desc = "Words counted by the lexicon pass"
    s = m[c]
    if c in LISTS: typ = "json_array"
    elif str(s.dtype) == "Int64": typ = "integer"
    elif s.dtype.kind == "f": typ = "number"
    elif set(s.dropna().astype(str).unique()) <= {"true", "false", ""}: typ = "boolean"
    else: typ = "string"
    allowed = enum_of(c) if not c.startswith("pr_") else "0 | 1 | 2"
    rows.append(dict(column=c, type=typ, description=desc or "", allowed_values=allowed, non_empty=int((s.astype(str) != "").sum() - s.isna().sum())))
dd = pd.DataFrame(rows)
dd.to_csv(OUT + "data_dictionary.csv", index=False, encoding="utf-8")
print("rows", len(m), "columns", len(m.columns), "undescribed", list(dd[dd.description == ""].column))
