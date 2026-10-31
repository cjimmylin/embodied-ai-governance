#!/usr/bin/env python3
"""Assemble the master document table: registry + text features + lexicons + OpenAlex + LLM annotations + derived fields.
Outputs data/master_table.csv, data/master_table.xlsx (with data dictionary), data/data_dictionary.csv."""
import os, re, json, glob, sys, pandas as pd, numpy as np
sys.path.insert(0,"/home/user/embodied-ai-governance-v4/scripts"); from regions import lookup
B="/home/user/embodied-ai-governance-v4/"
ANN=sys.argv[1] if len(sys.argv)>1 else "annotations/main"
reg=pd.read_csv(B+"data/registry.csv")
feat=pd.read_csv(B+"data/text_features.csv").set_index("file_rel")
lex=pd.read_csv(B+"data/lexicon_features.csv").set_index("doc_id")
def load_oa():
    rows={}
    if not os.path.exists(B+"data/openalex.jsonl"): return pd.DataFrame()
    for ln in open(B+"data/openalex.jsonl"):
        j=json.loads(ln); w=j["work"] or {}
        rows[j["doc_id"]]={"oa_matched":bool(w),"oa_match_type":w.get("match_type"),"oa_year":w.get("publication_year"),"oa_date":w.get("publication_date"),"oa_type":w.get("type"),"oa_venue":w.get("venue"),
            "oa_cited_by":w.get("cited_by_count"),"oa_first_author_country":w.get("first_author_country"),"oa_n_authors":len(w.get("authors") or []),
            "oa_authors":"; ".join(x["name"] for x in (w.get("authors") or []) if x.get("name")),"oa_author_countries":"; ".join(sorted({x["country"] for x in (w.get("authors") or []) if x.get("country")})),
            "oa_doi":w.get("doi"),"oa_id":w.get("openalex_id"),"oa_topics":"; ".join(w.get("topics") or [])}
    return pd.DataFrame.from_dict(rows,orient="index")
oa=load_oa()
OA_COLS=["oa_matched","oa_match_type","oa_year","oa_date","oa_type","oa_venue","oa_cited_by","oa_first_author_country","oa_n_authors","oa_authors","oa_author_countries","oa_doi","oa_id","oa_topics"]
L1={"industrial_manipulators":"Industrial & logistics","collaborative_robots":"Industrial & logistics","mobile_industrial_logistics":"Industrial & logistics","delivery_robots":"Industrial & logistics",
    "professional_service_robots":"Service & social","domestic_household_robots":"Service & social","social_companion_robots":"Service & social","educational_robots":"Service & social",
    "care_assistive_robots":"Service & social","toys_entertainment_robots":"Service & social","sex_robots":"Service & social",
    "surgical_medical_robots":"Medical & body-integrated","rehabilitation_exoskeleton_prosthetic":"Medical & body-integrated","biohybrid_or_cyborg":"Medical & body-integrated",
    "humanoid_general_purpose":"Humanoid & general-purpose","autonomous_road_vehicles":"Vehicles & field","drones_uas":"Vehicles & field","autonomous_maritime_or_rail":"Vehicles & field",
    "agricultural_robots":"Vehicles & field","space_or_extreme_environment":"Vehicles & field","military_autonomous_weapons":"Security & military","security_policing_robots":"Security & military",
    "other_embodied":"Other embodied","none":"None"}
PR=["transparency","justice_fairness","non_maleficence","responsibility_accountability","privacy","beneficence","freedom_autonomy","trust","sustainability","dignity","solidarity","human_oversight","robustness_security","inclusive_growth","physical_safety","human_robot_proximity","liability_for_physical_damage","autonomy_level_control","conformity_assessment_certification","dual_use_military"]
ann={}
for folder in [ANN, ANN+"_clean", "annotations/gov_extended", "annotations/round2", "annotations/cjk_fix"]:   # v4: CJK re-annotations with the character-aware cleaner override everything   # cleaned-excerpt re-annotations override the originals; extended-excerpt annotations of governance documents override both
    for p in sorted(glob.glob(B+folder+"/D*.json"))+sorted(glob.glob(B+folder+"/R2-*.json")):
        j=json.load(open(p)); ann[j["doc_id"]]={**j["annotation"],"_model":j["model"],"_prompt_hash":j["prompt_hash"],"_cost_usd":(j.get("usage") or {}).get("cost_usd"),"_excerpt_cleaned":folder.endswith("_clean"),"_excerpt_extended":folder.endswith("gov_extended") or folder.endswith("round2") or folder.endswith("cjk_fix"),"_policy":j.get("policy")}
rows=[]
for _,d in reg.iterrows():
    r={"doc_id":d.doc_id,"collection_region":d.region,"collection_set":d.set_primary,"collection_tier":d.meta_tier,"collection_points":d.meta_points,
       "collection_country":d.meta_country,"collection_robot_focus":d.meta_robot_focus,"collection_type":d.meta_type,"collection_title":d.title_best,
       "source_url":d.meta_url,"filename":d.filename,"file_ext":d.ext,"n_files":d.n_files,"regions_listed":d.regions_listed,"sets_listed":d.sets_listed,
       "text_status":d.text_status,"text_usable":bool(d.text_usable),"text_chars":d.text_chars}
    f=feat.loc[d.file_rel] if d.file_rel in feat.index else None
    r.update({"lang_detected":(f["lang"] if f is not None else None),"words":(int(f["words"]) if f is not None else 0),"doi_extracted":(f["doi_first"] if f is not None else None),
              "pdf_creation_date":(f["pdf_creation"] if f is not None else None)})
    for c in OA_COLS: r[c]=None
    if len(oa) and d.doc_id in oa.index:
        o=oa.loc[d.doc_id]
        for c in OA_COLS: r[c]=o.get(c)
    a=ann.get(d.doc_id)
    r["annotated"]=a is not None
    if a:
        for k,v in a.items():
            if k=="principles":
                for p in PR: r["pr_"+p]=v.get(p)
            elif isinstance(v,list): r[k]="; ".join(map(str,v))
            else: r[k]=v
        r["n_embodied_categories"]=len(a.get("embodied_categories",[])); r["n_topics"]=len(a.get("governance_topics",[])); r["n_mechanisms"]=len([m for m in a.get("governance_mechanisms",[]) if m!="none"])
        r["principles_sum"]=sum(a["principles"].values()); r["n_principles_substantive"]=sum(1 for v in a["principles"].values() if v==2); r["n_principles_any"]=sum(1 for v in a["principles"].values() if v>0)
        r["embodied_l1"]=L1.get(a.get("primary_embodied_category","none"),"None")
        # jurisdiction: annotation, else OpenAlex first-author country (DOI match), else collectors' 2-letter code
        jc=a.get("jurisdiction_country","XX") or "XX"; jsrc="annotation"
        r["jurisdiction_country_annotated"]=jc
        if jc=="XX":
            if r.get("oa_match_type")=="doi" and isinstance(r.get("oa_first_author_country"),str) and len(r["oa_first_author_country"])==2: jc,jsrc=r["oa_first_author_country"],"openalex"
            else:
                cc=str(d.meta_country) if pd.notna(d.meta_country) else ""
                mm=re.match(r"^([A-Z]{2,3})(;|$)",cc)
                if mm: jc,jsrc=mm.group(1),"collector"
        r["jurisdiction_country"]=jc; r["jurisdiction_source"]=jsrc if jc!="XX" else "unknown"
        g=lookup(jc); r.update({"jurisdiction_country_name":g["country_name"],"continent":g["continent"],"un_subregion":g["un_subregion"],"study_region":g["study_region"]})
        # final year: annotation > OpenAlex (DOI match, or research output) > PDF creation (plausible)
        y=a.get("pub_year"); src="annotation"
        oa_ok=(r.get("oa_match_type")=="doi") or (a.get("doc_class")=="research_output")
        if y is None and oa_ok and pd.notna(r.get("oa_year")): y,src=int(r["oa_year"]),"openalex"
        if y is None and isinstance(r.get("pdf_creation_date"),str):
            m=re.search(r"(19[89]\d|20[0-2]\d)",r["pdf_creation_date"])
            if m and int(m.group(1))<=2026: y,src=int(m.group(1)),"pdf_metadata"
        r["year_final"]=y; r["year_source"]=src if y is not None else "unknown"
    lx=lex.loc[d.doc_id] if d.doc_id in lex.index else None
    if lx is not None:
        for c in lex.columns:
            if c.endswith("_pk") or c=="lex_words": r[c]=lx[c]
    rows.append(r)
m=pd.DataFrame(rows)
m.to_csv(B+"data/master_table.csv",index=False); m.to_csv(B+"data/master_table_raw.csv",index=False)
# data dictionary
DD=[("doc_id","Canonical document id after deduplication"),("collection_region","Regional folder the collectors filed the document under"),("collection_set","sprint = collectors' robotics subset; database = general AI governance set"),
("collection_tier","Collectors' rubric tier (Core/Supporting/Context only) where available"),("collection_points","Collectors' rubric points (Europe only)"),("collection_country","Collectors' country/issuer field"),
("collection_robot_focus","Collectors' robot-focus label (Europe only)"),("collection_type","Collectors' type label (Europe only)"),("collection_title","Best available collector title (may be a truncated filename slug)"),
("source_url","Source URL from collector manifests"),("filename","Primary captured file name"),("file_ext","Primary file extension"),("n_files","Number of captured files merged into this document"),("regions_listed","All regional folders listing the document"),
("text_status","Conversion status of the primary file: ok, copied, blocked-source (bot wall), stub (no text), reader (recovered via Drive reader)"),("text_usable","Usable text available for annotation"),("text_chars","Characters of converted text"),
("lang_detected","Language detected by fast-langdetect on the text"),("words","Word count of full text"),("doi_extracted","First DOI found in text"),("pdf_creation_date","PDF CreationDate metadata"),
("oa_*","OpenAlex match fields: year, date, type, venue, citations, authors, author countries"),
("title_clean/title_en","Document title (original / English) from annotation"),("language","Annotated main language (ISO 639-1)"),("authors_or_issuer","Authors (research) or issuing body (instruments)"),("issuer_type","Codebook issuer type"),
("pub_year/pub_month/date_basis","Annotated publication/adoption date and how it was determined"),("jurisdiction_country","Final ISO alpha-2 jurisdiction (EU, INT, XX allowed): annotation, else OpenAlex first-author country, else collector code"),("jurisdiction_country_annotated","Jurisdiction as annotated from the text only"),("jurisdiction_source","Where the final jurisdiction came from: annotation / openalex / collector / unknown"),("jurisdiction_scope","international/supranational_regional/national/subnational/not_applicable"),
("countries_discussed","Countries analysed or targeted"),("doc_type","Fine document genre (28 classes, codebook section C)"),("doc_class","Coarse document class"),("is_governance_document","Document itself governs/prescribes"),
("instrument_status","Lifecycle status for governance documents"),("binding_nature","Binding/soft/standard"),("publication_stage","Research publication stage"),("ai_scope","General AI vs embodied scope"),("embodiment_status","Physical vs software 'robot'"),
("embodied_categories/primary_embodied_category","Robotics & physical-AI taxonomy labels (codebook section D)"),("embodied_l1","Level-1 grouping of primary embodied category"),("application_sectors","Sectors addressed"),
("governance_topics/primary_topic","Governance topics addressed"),("pr_<principle>","Principle salience 0/1/2 (Jobin+OECD core; embodied-specific extensions)"),("principles_sum/n_principles_any/n_principles_substantive","Principle aggregates"),
("governance_mechanisms","Mechanisms established or recommended"),("named_instruments_referenced","Instruments cited"),("robot_legal_personhood_position","Stance on robot legal personhood"),("risk_framing","Dominant framing"),
("stance_toward_regulation","Regulatory stance"),("methodology","Research methodology"),("faith_or_religious_perspective","Religious standpoint flag"),("page_quality","Content quality of the capture"),
("relevance_to_embodied_ai_governance","0-3 relevance rating"),("summary_en","60-word English summary"),("key_provisions_or_claims","Up to 5 key provisions/claims"),("confidence","Annotator confidence 0-1"),
("jurisdiction_country_name/continent/un_subregion/study_region","Geography derived from jurisdiction_country"),("year_final/year_source","Best publication year and its source"),
("lex_*_pk","Lexicon hits per 1,000 words over full text (deterministic, multilingual)"),("_model/_prompt_hash/_cost_usd","Annotation provenance")]
dd=pd.DataFrame(DD,columns=["column","description"]); dd.to_csv(B+"data/data_dictionary.csv",index=False)
with pd.ExcelWriter(B+"data/master_table.xlsx",engine="openpyxl") as xw:
    m.to_excel(xw,sheet_name="documents",index=False); dd.to_excel(xw,sheet_name="data_dictionary",index=False)
print("master rows:",len(m)," annotated:",m.annotated.sum()," columns:",len(m.columns))
if m.annotated.sum():
    a=m[m.annotated]
    for c in ["doc_class","ai_scope","embodiment_status","study_region","page_quality"]:
        print(f"-- {c}:",a[c].value_counts().head(10).to_dict())
    print("-- year_final:",a.year_final.describe()[["count","min","50%","max"]].to_dict())
