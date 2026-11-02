"""Excerpt-vs-full-text validation on the reliability sample: T26 (per field), T27 (label inflation and set membership), F43."""
import sys, json, glob, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts")
from analysis_common import *
from sklearn.metrics import cohen_kappa_score
RESULTS.update(json.load(open(B+"data/results.json")))
r1=pd.read_csv(B+"data/reliability_fields.csv"); r2=pd.read_csv(B+"data/reliability_fields_retest.csv"); r3=pd.read_csv(B+"data/reliability_fields_fulltext.csv")
import os
r4=pd.read_csv(B+"data/reliability_fields_blind.csv") if os.path.exists(B+"data/reliability_fields_blind.csv") else None
r5=pd.read_csv(B+"data/reliability_fields_govext.csv") if os.path.exists(B+"data/reliability_fields_govext.csv") else None
t=r1[["field","type","n","percent_agreement","kappa"]].rename(columns={"percent_agreement":"agreement_inter_model","kappa":"kappa_inter_model"})
t=t.merge(r2[["field","percent_agreement","kappa"]].rename(columns={"percent_agreement":"agreement_retest","kappa":"kappa_retest"}),on="field",how="left")
t=t.merge(r3[["field","percent_agreement","kappa"]].rename(columns={"percent_agreement":"agreement_fulltext","kappa":"kappa_fulltext"}),on="field",how="left")
if r4 is not None: t=t.merge(r4[["field","percent_agreement","kappa"]].rename(columns={"percent_agreement":"agreement_blind","kappa":"kappa_blind"}),on="field",how="left")
if r5 is not None: t=t.merge(r5[["field","percent_agreement","kappa"]].rename(columns={"percent_agreement":"agreement_gov_extended","kappa":"kappa_gov_extended"}),on="field",how="left")
t=t[~t.field.str.startswith("pub_year")]
write_table("T26_reliability_three_way",t.round(3),"Per-field agreement and kappa against the v1 final annotations: independent model on the same excerpt (160 docs); same model re-run (161 docs); same model on the full text (160 docs); same model metadata-blind with the collector cover block stripped (160 docs); and, for governance documents only, the v2 blind extended-excerpt annotation (up to 110,000 characters)")
def F44(th):
    if r4 is None: return
    t_=fs.setup(th); d=T3[["field","kappa_inter_model","kappa_blind"]].dropna().copy(); d["lab"]=d.field.str.replace("principle:","P: ").str.replace("_"," "); d=d.sort_values("kappa_blind"); y=np.arange(len(d))
    fig,ax=plt.subplots(figsize=(7.4,9.4)); ax.axvspan(0.8,1.0,color=t_["grid"],alpha=0.5,lw=0)
    ax.scatter(d.kappa_inter_model,y,color=t_["cat"][0],s=22,label="Different model, same excerpt and metadata",zorder=3)
    ax.scatter(d.kappa_blind,y,color=t_["cat"][1],s=26,marker="D",label="Same model, metadata-blind, cover block stripped",zorder=4)
    ax.set_yticks(y); ax.set_yticklabels(d.lab,fontsize=6.8); ax.yaxis.grid(False); ax.set_xlim(0.3,1.0); ax.set_xlabel("Cohen's kappa vs the original annotation (shaded: 0.8 and above)"); ax.legend(loc="lower left",fontsize=7)
    ax.set_title("Removing the collectors' labels from the input changes country, issuer and language labels little;\nthe fields that move are page quality, date basis and stance",loc="left",fontsize=9.5)
    fs.save(fig,"F44_blind_reannotation",th); d.to_csv(FD+"F44_blind_reannotation.csv",index=False)
A={json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+"annotations/main/D*.json")}
Fx={json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+"annotations/reliability_fulltext/D*.json")}
ids=sorted(set(A)&set(Fx)); pr=list(A[ids[0]]["principles"].keys())
m=pd.read_csv(B+"data/master_table_v1.csv",low_memory=False).set_index("doc_id")
rows=[]
for p in pr:
    a=np.array([A[i]["principles"][p]>=1 for i in ids]); b=np.array([Fx[i]["principles"][p]>=1 for i in ids])
    rows.append(dict(item="principle: "+PRL[p],excerpt_pct=round(100*a.mean(),1),fulltext_pct=round(100*b.mean(),1),diff_pp=round(100*(b.mean()-a.mean()),1),kappa=round(float(cohen_kappa_score(a,b)),3)))
for k,lab in [("embodied_categories","labels: embodied categories"),("governance_mechanisms","labels: mechanisms"),("governance_topics","labels: topics"),("application_sectors","labels: sectors"),("named_instruments_referenced","labels: named instruments")]:
    a=np.array([len(A[i][k]) for i in ids]); b=np.array([len(Fx[i][k]) for i in ids])
    rows.append(dict(item=lab+" (mean per document)",excerpt_pct=round(a.mean(),2),fulltext_pct=round(b.mean(),2),diff_pp=round(b.mean()-a.mean(),2),kappa=np.nan))
a=np.array([(A[i]["relevance_to_embodied_ai_governance"]>=2 or len(A[i]["embodied_categories"])>0) for i in ids]); b=np.array([(Fx[i]["relevance_to_embodied_ai_governance"]>=2 or len(Fx[i]["embodied_categories"])>0) for i in ids])
rows.append(dict(item="embodied-set membership",excerpt_pct=round(100*a.mean(),1),fulltext_pct=round(100*b.mean(),1),diff_pp=round(100*(b.mean()-a.mean()),1),kappa=round(float(cohen_kappa_score(a,b)),3)))
a=np.array([A[i]["is_governance_document"] for i in ids]); b=np.array([Fx[i]["is_governance_document"] for i in ids])
rows.append(dict(item="governance document",excerpt_pct=round(100*a.mean(),1),fulltext_pct=round(100*b.mean(),1),diff_pp=round(100*(b.mean()-a.mean()),1),kappa=round(float(cohen_kappa_score(a,b)),3)))
big=[i for i in ids if m.loc[i,"text_chars"]>14500]; small=[i for i in ids if m.loc[i,"text_chars"]<=14500]
split=[]
for name,sub in [("truncated by the excerpt",big),("fully contained in the excerpt",small)]:
    ks=[cohen_kappa_score([A[i]["principles"][p]>=1 for i in sub],[Fx[i]["principles"][p]>=1 for i in sub]) for p in pr if len(set([A[i]["principles"][p]>=1 for i in sub]))>1]
    split.append(dict(subset=name,n=len(sub),median_principle_kappa=round(float(np.nanmedian(ks)),3),doc_class_agreement=round(float(np.mean([A[i]["doc_class"]==Fx[i]["doc_class"] for i in sub])),3),exact_category_set_agreement=round(float(np.mean([set(A[i]["embodied_categories"])==set(Fx[i]["embodied_categories"]) for i in sub])),3),governance_flag_agreement=round(float(np.mean([A[i]["is_governance_document"]==Fx[i]["is_governance_document"] for i in sub])),3)))
t27=pd.DataFrame(rows); write_table("T27_fulltext_vs_excerpt",t27,"Excerpt vs full-text annotation (same model, 160 documents): label prevalence, label counts and agreement")
t27b=pd.DataFrame(split); write_table("T27b_fulltext_by_truncation",t27b,"Excerpt vs full-text agreement by whether the v1 excerpt truncated the document")
R("fulltext_validation",{"median_kappa_fulltext":float(r3.kappa.median()),"min_kappa_fulltext":float(r3.kappa.min()),"min_field":str(r3.sort_values("kappa").field.iloc[0]),"prevalence":t27.to_dict("records"),"by_truncation":split})
T3=t.copy()
def F43(th):
    t=fs.setup(th); d=T3[["field","kappa_inter_model","kappa_retest","kappa_fulltext"]].dropna().copy()
    d["lab"]=d.field.str.replace("principle:","P: ").str.replace("_"," "); d=d.sort_values("kappa_fulltext"); y=np.arange(len(d))
    fig,ax=plt.subplots(figsize=(7.4,9.4)); ax.axvspan(0.8,1.0,color=t["grid"],alpha=0.5,lw=0)
    ax.scatter(d.kappa_inter_model,y,color=t["cat"][0],s=22,label="Sonnet vs Opus (different model)",zorder=3)
    ax.scatter(d.kappa_retest,y,color=t["cat"][2],s=22,marker="s",label="Sonnet re-run (same excerpt)",zorder=3)
    ax.scatter(d.kappa_fulltext,y,color=t["cat"][1],s=26,marker="D",label="Sonnet full text vs excerpt",zorder=4)
    ax.set_yticks(y); ax.set_yticklabels(d.lab,fontsize=6.8); ax.yaxis.grid(False); ax.set_xlim(0.4,1.0); ax.set_xlabel("Cohen's kappa (shaded: 0.8 and above)")
    ax.legend(loc="lower left",fontsize=7)
    ax.set_title("Reading the full text instead of the excerpt changes labels less than switching model does;\nthe weakest fields are date basis, page quality and mechanisms",loc="left",fontsize=9.5)
    fs.save(fig,"F43_reliability_three_way",th); d.to_csv(FD+"F43_reliability_three_way.csv",index=False)
for th in ["light","dark"]: F43(th)
T3=t.copy()
for th in ["light","dark"]: F44(th)
# ---------- T35: effect of the v2 extended, blind re-annotation on governance-document labels
G1={}; G1.update(A); G1.update({json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+"annotations/main_clean/D*.json")})
G2={json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+"annotations/gov_extended/D*.json")}
gid=sorted(set(G1)&set(G2)); rows=[]
def share(D,ids,fn): return round(100*np.mean([fn(D[i]) for i in ids]),1)
for lab_,fn in [("legally binding (binding_nature)",lambda x:x["binding_nature"]=="legally_binding"),("in force (instrument_status)",lambda x:x["instrument_status"]=="in_force"),("is governance document",lambda x:bool(x["is_governance_document"])),
                ("any embodied category",lambda x:len(x["embodied_categories"])>0),("relevance >= 2",lambda x:x["relevance_to_embodied_ai_governance"]>=2),("physical safety mentioned",lambda x:x["principles"]["physical_safety"]>=1),("physical safety in depth",lambda x:x["principles"]["physical_safety"]>=2),
                ("autonomy-level control mentioned",lambda x:x["principles"]["autonomy_level_control"]>=1),("autonomy-level control in depth",lambda x:x["principles"]["autonomy_level_control"]>=2),("conformity assessment mechanism",lambda x:"conformity_assessment_certification" in x["governance_mechanisms"]),
                ("risk-based tiering mechanism",lambda x:"risk_based_tiering" in x["governance_mechanisms"]),("technical standards referenced",lambda x:"technical_standards_reference" in x["governance_mechanisms"]),("liability regime mechanism",lambda x:"liability_regime" in x["governance_mechanisms"])]:
    rows.append(dict(label=lab_,v1_excerpt_pct=share(G1,gid,fn),v2_extended_blind_pct=share(G2,gid,fn),agreement=round(float(np.mean([fn(G1[i])==fn(G2[i]) for i in gid])),3)))
for k,lab_ in [("governance_mechanisms","mechanisms per document (mean)"),("governance_topics","topics per document (mean)"),("embodied_categories","robot types per document (mean)"),("named_instruments_referenced","named instruments per document (mean)")]:
    rows.append(dict(label=lab_,v1_excerpt_pct=round(float(np.mean([len(G1[i][k]) for i in gid])),2),v2_extended_blind_pct=round(float(np.mean([len(G2[i][k]) for i in gid])),2),agreement=np.nan))
t35=pd.DataFrame(rows); write_table("T35_gov_extended_effect",t35,f"Governance documents (n={len(gid)}): label prevalence under the v1 excerpt annotation and the v2 extended, metadata-blind annotation, with per-document agreement")
R("gov_extended_effect",{"n":len(gid),"rows":t35.to_dict("records")})
dump_results(); print("done 19")
