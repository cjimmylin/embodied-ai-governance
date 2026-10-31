"""Supplementary tables S01-S13 (markdown) for the supplement and per-type synthesis numbers."""
import pandas as pd, numpy as np, json, sys
sys.path.insert(0,"/home/user/embodied-ai-governance-v4/scripts")
from analysis_common import load, write_table, EMB, L1
m=load()
u=m[m.usable]; e=u[u.embodied_set]
def tidy(d,cols):
    d=d[cols].copy()
    if "year_final" in d: d["year_final"]=d["year_final"].apply(lambda y:"" if pd.isna(y) else str(int(y)))
    if "title_en" in d: d["title_en"]=d["title_en"].fillna("").str.slice(0,110)
    if "embodied_categories" in d: d["embodied_categories"]=d["embodied_categories"].fillna("").str.replace("; ",", ")
    return d.rename(columns={"title_en":"title","jurisdiction_country":"jurisdiction","year_final":"year","instrument_status":"status","embodied_categories":"categories"})
base=["doc_id","title_en","jurisdiction_country","year_final","doc_type","instrument_status","embodied_categories"]
g=e[e.is_governance_document==True]
write_table("S01_binding_embodied",tidy(g[g.doc_class=="governance_instrument_binding"].sort_values("year_final"),base),"Legally binding instruments in the embodied-AI set (usable documents)")
write_table("S02_soft_embodied",tidy(g[g.doc_class=="governance_instrument_soft"].sort_values(["doc_type","year_final"]),base),"Soft-law instruments and technical standards in the embodied-AI set")
write_table("S03_drafts_embodied",tidy(g[g.doc_class=="governance_proposal_or_draft"].sort_values("year_final"),base),"Proposals, bills and consultations in the embodied-AI set")
write_table("S04_govreports_embodied",tidy(e[e.doc_class=="government_report_or_parliamentary"].sort_values("year_final"),base),"Government and parliamentary reports in the embodied-AI set")
prov=u[(u.ai_scope=="general_ai_with_embodied_provisions")&(u.is_governance_document==True)]
write_table("S05_general_with_embodied_provisions",tidy(prov.sort_values(["doc_class","year_final"]),["doc_id","title_en","jurisdiction_country","year_final","doc_type","embodied_categories"]),"General-AI governance instruments that contain embodied-AI provisions")
qa=pd.read_csv("/home/user/embodied-ai-governance-v4/data/qa_flags.csv")
fl=qa["flags"].str.split(";").explode().str.strip().value_counts().reset_index(); fl.columns=["flag","documents"]
write_table("S06_qa_flags",fl,"Quality-assurance flags on annotated documents")
dd=pd.read_csv("/home/user/embodied-ai-governance-v4/data/data_dictionary.csv")
write_table("S07_data_dictionary",dd,"Master table data dictionary")
# full country table
t4=pd.read_csv("/home/user/embodied-ai-governance-v4/tables/T04_countries.csv")
write_table("S08_all_countries",t4,"All national jurisdictions with document counts")
rel=pd.read_csv("/home/user/embodied-ai-governance-v4/figures/data/F35_reliability.csv")
rel=rel[["lab","type","percent_agreement_model","kappa_model","percent_agreement_retest","kappa_retest","note"]].round(3).rename(columns={"lab":"field","percent_agreement_model":"agreement (Sonnet vs Opus)","kappa_model":"kappa (Sonnet vs Opus)","percent_agreement_retest":"agreement (test-retest)","kappa_retest":"kappa (test-retest)"})
write_table("S09_reliability_full",rel.fillna(""),"Reliability per field: inter-model (160 documents) and same-model test-retest (161 documents)")
cc=pd.read_csv("/home/user/embodied-ai-governance-v4/data/reliability_team_crosscheck.csv").round(3)
write_table("S10_collector_crosscheck",cc.fillna(""),"Cross-checks of annotations against the collectors' own labels")
oa=e[(e.doc_class=="research_output")&e.oa_cited_by.notna()].sort_values("oa_cited_by",ascending=False).head(25)
write_table("S11_most_cited",tidy(oa,["doc_id","title_en","year_final","oa_cited_by","oa_match_type","venue"]).rename(columns={"oa_cited_by":"OpenAlex citations","oa_match_type":"match"}),"Most cited embodied-AI research outputs by OpenAlex citation count (indicative; see caveat)")
# per-L1 synthesis
rows=[]
for l1 in ["Industrial & logistics","Service & social","Medical & body-integrated","Humanoid & general-purpose","Vehicles & field","Security & military","Other embodied"]:
    cats=[c for c,v in L1.items() if v==l1]
    def has_any(df): return df.embodied_categories.fillna("").apply(lambda s:any(c in s.split("; ") for c in cats))
    d=e[has_any(e)]; gi=g[has_any(g)]
    rows.append({"group":l1,"documents":len(d),"research":int((d.doc_class=="research_output").sum()),"governance_instruments":len(gi),
                 "binding":int((gi.doc_class=="governance_instrument_binding").sum()),"standards":int((gi.doc_type=="technical_standard").sum()),
                 "drafts":int((gi.doc_class=="governance_proposal_or_draft").sum()),
                 "median_year":int(d.year_final.median()) if d.year_final.notna().any() else "",
                 "physical_safety_any_pct":round(100*(d.pr_physical_safety>=1).mean(),1),
                 "liability_any_pct":round(100*(d.pr_liability_for_physical_damage>=1).mean(),1),
                 "proximity_any_pct":round(100*(d.pr_human_robot_proximity>=1).mean(),1),
                 "conformity_any_pct":round(100*(d.pr_conformity_assessment_certification>=1).mean(),1),
                 "calls_for_regulation_pct":round(100*(d.stance_toward_regulation=="calls_for_new_regulation").mean(),1),
                 "top_regions":"; ".join(f"{k} {v}" for k,v in d.study_region.value_counts().head(3).items())})
write_table("S12_by_robot_group",pd.DataFrame(rows),"Synthesis by robot group (level-1 taxonomy): documents, instruments and principle emphasis")
# per L2 category synthesis
rows=[]
for c in EMB:
    d=e[e.embodied_categories.fillna("").apply(lambda s:c in s.split("; "))]
    if len(d)<7: continue
    gi=g[g.embodied_categories.fillna("").apply(lambda s:c in s.split("; "))]
    named=gi.named_instruments_referenced.fillna("").str.split(";").explode().str.strip()
    named=named[named!=""].value_counts().head(3)
    rows.append({"category":c,"docs":len(d),"instruments":len(gi),"binding":int((gi.doc_class=="governance_instrument_binding").sum()),"standards":int((gi.doc_type=="technical_standard").sum()),
                 "physical_safety_any_pct":round(100*(d.pr_physical_safety>=1).mean(),1),"liability_any_pct":round(100*(d.pr_liability_for_physical_damage>=1).mean(),1),
                 "privacy_any_pct":round(100*(d.pr_privacy>=1).mean(),1),"dignity_any_pct":round(100*(d.pr_dignity>=1).mean(),1),
                 "top_primary_topic":d.primary_topic.value_counts().index[0] if len(d) else "","top_mechanism_in_instruments":(gi.governance_mechanisms.fillna("").str.split("; ").explode().value_counts().drop("",errors="ignore").index[0] if len(gi) and gi.governance_mechanisms.fillna("").str.len().sum() else ""),
                 "instruments_most_cited":"; ".join(f"{k} ({v})" for k,v in named.items())})
write_table("S13_by_category",pd.DataFrame(rows).sort_values("docs",ascending=False),"Synthesis by embodied category: documents, instruments and emphasis")
print("done")
