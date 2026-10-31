#!/usr/bin/env python3
"""Collection round 2: discovery inventory, fetch funnel, before/after counts against v2, collector-metadata vs blind
annotation agreement, and the list of newly captured embodied instruments. Writes tables T30-T37, figures F50-F52 and
report/src/collection_round2.md. Run after 07/07b (v3 master table) and 18 (coverage audit)."""
import os, re, json, sys, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v4/scripts")
from analysis_common import *
import figstyle as fs
from matplotlib.patches import Patch
from sklearn.metrics import cohen_kappa_score
def kappa(a,b):
    a=pd.Series(list(a)).astype(str); b=pd.Series(list(b)).astype(str)
    return float(cohen_kappa_score(a,b)) if len(a)>1 and (a.nunique()>1 or b.nunique()>1) else np.nan
V2="/home/user/embodied-ai-governance-v2/"; R2="/home/user/collection-round-2/"
TD=B+"tables/"; FD=B+"figures/data/"; os.makedirs(FD,exist_ok=True)

def load_master(path):
    m=pd.read_csv(path,low_memory=False); a=m[m.annotated].copy()
    a["embodied_set"]=((a.relevance_to_embodied_ai_governance>=2)|(a.embodied_categories.fillna("")!=""))&(a.ai_scope!="not_ai")
    a["general_set"]=(~a.embodied_set)&a.ai_scope.isin(["general_ai_only","general_ai_with_embodied_provisions"])
    a["usable"]=a.text_usable&(a.page_quality!="error_or_blocked_page")&(a.doc_class!="unusable")
    a["gov"]=a.is_governance_document.astype(bool); a["binding"]=a.doc_class=="governance_instrument_binding"
    a["content_capture"]=a.page_quality.isin(["substantive_document","partial_or_excerpt"])
    a["instrument"]=a.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])
    a["robot_specific"]=a.instrument&a.embodied_set&(a.relevance_to_embodied_ai_governance>=2)   # subset of the embodied set (same definition as T33)
    a["binding_text"]=a.binding.copy()
    if "principal_instrument" in a.columns: a["legal_text"]=a.instrument; a["instrument"]=a.principal_instrument.astype(bool); a["robot_specific"]=a.instrument&a.embodied_set&(a.relevance_to_embodied_ai_governance>=2); a["binding"]=a.binding_text&a.instrument
    a["gov_report"]=a.doc_class=="government_report_or_parliamentary"
    for c in ["embodied_categories","governance_topics","governance_mechanisms","application_sectors"]: a[c]=a[c].fillna("")
    return m,a
m2,a2=load_master(V2+"data/master_table.csv"); m3,a3=load_master(B+"data/master_table.csv")
inv=pd.read_csv(B+"data/round2_inventory.csv",dtype=str,keep_default_na=False)
inv["has_text"]=inv.has_text=="True"; inv["content_analysed"]=inv.content_analysed=="True"
u2=a2[a2.usable]; u3=a3[a3.usable]
r3=u3[u3.collection_set=="round2"]          # usable round-2 additions
o3=u3[u3.collection_set!="round2"]          # original collection as re-processed in v3

# ---------- T30: discovery sources
SRC={"API_eurlex":"EUR-Lex (CELLAR SPARQL, title search)","API_eurovoc":"EUR-Lex (EuroVoc concept search)","API_uk":"legislation.gov.uk (title search)","API_japan":"Japan e-Gov law API (full-text search)","API_brazil":"Brazil Camara dados abertos","API_govcn":"gov.cn State Council policy library (full-text)","API_australia":"Federal Register of Legislation (AU)","API_ecfr":"eCFR (US Code of Federal Regulations search)","API_korea":"law.go.kr (not reachable)",
     "US":"Collector: United States federal and state","EU":"Collector: EU, UK, Ireland, Nordics","EN":"Collector: continental European national","AS":"Collector: East Asia incl. Chinese provinces","AP":"Collector: South/Southeast Asia and Oceania","ML":"Collector: Middle East, Africa, Latin America, Canada","ST":"Collector: technical standards (ISO/IEC, IEEE, SAE, UL, national)","IG":"Collector: intergovernmental, military and strategies","MW":"Collector: medical, workplace, consumer and care robots"}
inv["source"]=inv.source_file.str.replace(".csv","",regex=False)
rows=[]
for s,g in inv.groupby("source"):
    rows.append(dict(source=SRC.get(s,s),kind="scripted database harvest" if s.startswith("API_") else "collector agent",candidates=len(g),text_obtained=int(g.has_text.sum()),content_analysed=int(g.content_analysed.sum()),
                     usable=int(g.doc_id.isin(r3.doc_id).sum()),embodied=int(g.doc_id.isin(r3[r3.embodied_set].doc_id).sum()),instruments=int(g.doc_id.isin(r3[r3.instrument].doc_id).sum()),embodied_instruments=int(g.doc_id.isin(r3[r3.instrument&r3.embodied_set].doc_id).sum())))
t30=pd.DataFrame(rows).sort_values("candidates",ascending=False)
t30.loc[len(t30)]=dict(source="All sources",kind="",candidates=len(inv),text_obtained=int(inv.has_text.sum()),content_analysed=int(inv.content_analysed.sum()),usable=len(r3),embodied=int(r3.embodied_set.sum()),instruments=int(r3.instrument.sum()),embodied_instruments=int((r3.instrument&r3.embodied_set).sum()))
write_table("T50_round2_sources",t30,"Round-2 discovery sources: candidates after de-duplication, texts obtained, documents content-analysed, and what the blind annotation made of them")

# ---------- T31: fetch outcomes and blocked hosts
import urllib.parse
inv["host"]=inv.url_primary.map(lambda u: urllib.parse.urlparse(u).netloc if u else "")
fo=inv.fetch_status.where(inv.has_text,inv.fetch_status).copy()
fo=np.where(inv.has_text,np.where(inv.text_status=="agent_abstract","text: scope/abstract via mirror","text: fetched"),np.where(inv.fetch_status=="blocked_host","no text: host blocks the sandbox",np.where(inv.fetch_status.str.match(r"^\d"),"no text: HTTP error or thin page","no text: fetch failed")))
inv["outcome"]=fo
t31=inv.groupby("outcome").size().reset_index(name="candidates").sort_values("candidates",ascending=False)
write_table("T51_round2_fetch",t31,"Round-2 fetch outcomes for all de-duplicated candidates")
bh=inv[~inv.has_text].groupby("host").size().sort_values(ascending=False).head(15).reset_index(name="candidates_without_text")
write_table("T52_round2_blocked_hosts",bh,"Hosts accounting for most candidates without text (sandbox network policy, bot challenges, JavaScript-only pages)")

# ---------- T33: before/after
def counts(u,a):
    e=u[u.embodied_set]; lt=u.legal_text if "legal_text" in u.columns else u.instrument
    d=dict(documents=len(a),usable=len(u),embodied_set=len(e),general_set=int(u.general_set.sum()),governance_documents=int(u.gov.sum()),
                instruments_all=int(lt.sum()),instruments_embodied=int((lt&u.embodied_set).sum()),instruments_robot_specific=int((lt&u.embodied_set&(u.relevance_to_embodied_ai_governance>=2)).sum()),
                binding_all=int((u.binding_text&lt).sum()),binding_embodied=int((u.binding_text&lt&u.embodied_set).sum()),binding_robot_specific=int((u.binding_text&lt&u.embodied_set&(u.relevance_to_embodied_ai_governance>=2)).sum()),
                soft_embodied=int(((u.doc_class=="governance_instrument_soft")&u.embodied_set).sum()),drafts_embodied=int(((u.doc_class=="governance_proposal_or_draft")&u.embodied_set).sum()),
                gov_reports_embodied=int((u.gov_report&u.embodied_set).sum()),jurisdictions_with_embodied_instrument=int(u[lt&u.embodied_set].jurisdiction_country.nunique()))
    if "principal_instrument" in u.columns:   # v4 tiers (not available for v2)
        pi=u.principal_instrument.astype(bool); fam=u.family_rep.astype(bool); ai=u.ai_explicit.astype(bool); au=u.autonomy_terms.astype(bool)
        bt=u.binding_text
        d.update(principal_embodied=int((pi&u.embodied_set).sum()),principal_robot_specific=int((pi&u.embodied_set&(u.relevance_to_embodied_ai_governance>=2)).sum()),principal_binding_embodied=int((pi&bt&u.embodied_set).sum()),
                 principal_binding_robot_specific=int((pi&bt&u.embodied_set&(u.relevance_to_embodied_ai_governance>=2)).sum()),families_binding_embodied=int((pi&fam&bt&u.embodied_set).sum()),
                 binding_embodied_autonomy_or_ai=int((pi&bt&u.embodied_set&au).sum()),binding_embodied_ai_explicit=int((pi&bt&u.embodied_set&ai).sum()),
                 principal_embodied_autonomy_or_ai=int((pi&u.embodied_set&au).sum()),principal_embodied_ai_explicit=int((pi&u.embodied_set&ai).sum()))
    return d
c2=counts(u2,a2); c3=counts(u3,a3)
LAB={"documents":"Documents (annotated)","usable":"Usable documents","embodied_set":"Embodied-AI set","general_set":"General-AI set","governance_documents":"Governance documents (incl. reports)","instruments_all":"Governance instruments, all","instruments_embodied":"Governance instruments, embodied-AI set","instruments_robot_specific":"Robot-specific instruments (relevance 2+)","binding_all":"Binding instruments, all","binding_embodied":"Binding instruments, embodied-AI set","binding_robot_specific":"Binding instruments, robot-specific","soft_embodied":"Soft-law instruments, embodied-AI set","drafts_embodied":"Proposals and drafts, embodied-AI set","gov_reports_embodied":"Government reports, embodied-AI set","jurisdictions_with_embodied_instrument":"Jurisdictions with an embodied instrument"}
t33=pd.DataFrame([dict(measure=LAB[k],v2=c2[k],v3=c3[k],added=c3[k]-c2[k],ratio=round(c3[k]/c2[k],2) if c2[k] else np.nan) for k in LAB])
write_table("T53_before_after",t33,"Before/after on the comparable unit (every text of instrument class): v2 (original collection) versus v3/v4 (original plus round 2), content-analysed documents only")
TIER={"instruments_embodied":"All legal texts of instrument class, embodied-AI set","principal_embodied":"Principal instruments (amendments kept; commencement, levy, exemption, incorporation, corrigenda, stubs and catalogue pages excluded)","principal_robot_specific":"Principal instruments rated robot-relevant (relevance 2 or 3)","principal_embodied_autonomy_or_ai":"Principal embodied instruments whose text contains autonomy or AI provisions","principal_embodied_ai_explicit":"Principal embodied instruments whose text names AI explicitly",
      "binding_embodied":"Binding legal texts, embodied-AI set","principal_binding_embodied":"Principal binding instruments, embodied-AI set","principal_binding_robot_specific":"Principal binding instruments rated robot-relevant (relevance 2 or 3)","families_binding_embodied":"Principal binding instruments counted once per instrument family","binding_embodied_autonomy_or_ai":"Principal binding instruments with autonomy or AI provisions in the text","binding_embodied_ai_explicit":"Principal binding instruments naming AI explicitly"}
t33b=pd.DataFrame([dict(tier=v,count=c3.get(k)) for k,v in TIER.items()])
write_table("T53b_counting_units",t33b,"How many instruments reach robots depends on the counting unit and the construct: the same collection under successively stricter definitions (v4)")
R("counting_units",t33b.to_dict("records"))
R("round2_before_after",t33.to_dict("records"))

# by region
rows=[]
for reg in REGIONS+["Unknown"]:
    rows.append(dict(region=reg,v2_embodied_instruments=int((u2.instrument&u2.embodied_set&(u2.study_region==reg)).sum()),v3_embodied_instruments=int((u3.instrument&u3.embodied_set&(u3.study_region==reg)).sum()),
                     v2_binding_embodied=int((u2.binding&u2.embodied_set&(u2.study_region==reg)).sum()),v3_binding_embodied=int((u3.binding&u3.embodied_set&(u3.study_region==reg)).sum()),
                     v2_embodied_docs=int((u2.embodied_set&(u2.study_region==reg)).sum()),v3_embodied_docs=int((u3.embodied_set&(u3.study_region==reg)).sum())))
t34=pd.DataFrame(rows); write_table("T54_before_after_region",t34,"Embodied-AI instruments and documents by jurisdiction region, v2 versus v3")
# by robot group (L1)
rows=[]
for g in ["Industrial & logistics","Service & social","Medical & body-integrated","Humanoid & general-purpose","Vehicles & field","Security & military","Other embodied"]:
    def n(u,flag): return int(sum(1 for cats,f in zip(u.embodied_categories,flag) if f and any(L1.get(c)==g for c in cats.split("; ") if c)))
    rows.append(dict(robot_group=g,v2_documents=n(u2,u2.embodied_set),v3_documents=n(u3,u3.embodied_set),v2_instruments=n(u2,u2.instrument&u2.embodied_set),v3_instruments=n(u3,u3.instrument&u3.embodied_set),v2_binding=n(u2,u2.binding&u2.embodied_set),v3_binding=n(u3,u3.binding&u3.embodied_set)))
t35=pd.DataFrame(rows); write_table("T55_before_after_robot_group",t35,"Embodied-AI documents and instruments by robot group (any category mention), v2 versus v3")

# ---------- T36: round-2 annotation outcomes (what the blind annotator made of the candidates)
r3all=a3[a3.collection_set=="round2"]
t36=r3all.groupby("doc_class").size().reindex(DCO).fillna(0).astype(int).reset_index().rename(columns={"index":"doc_class",0:"documents"})
t36["doc_class"]=t36.doc_class.map(DCL); t36["embodied_set"]=[int((r3all.embodied_set&(r3all.doc_class==k)).sum()) for k in DCO]; t36["robot_specific"]=[int((r3all.robot_specific&(r3all.doc_class==k)).sum()) for k in DCO]
write_table("T56_round2_classes",t36,"Round-2 additions by annotated document class, with the embodied-AI and robot-specific subsets")

# ---------- T37: collector metadata vs blind annotation
cj=inv.set_index("doc_id")
x=r3all.join(cj[["binding_nature","instrument_type","jurisdiction","year","confidence","status"]].rename(columns={"status":"collector_status","year":"collector_year","jurisdiction":"collector_jurisdiction","binding_nature":"collector_binding","confidence":"collector_confidence"}),on="doc_id")
x=x[x.usable]
rows=[]
# binding nature
b=x[x.collector_binding.isin(["legally_binding","voluntary_soft_law","technical_standard_voluntary","not_applicable"])]
agree=((b.collector_binding=="legally_binding")==(b.doc_class=="governance_instrument_binding"))
rows.append(dict(field="Binding nature (collector legally_binding vs annotated binding instrument)",n=len(b),agreement=round(agree.mean(),3),kappa=round(kappa(b.collector_binding=="legally_binding",b.doc_class=="governance_instrument_binding"),3) if len(b) else np.nan))
# jurisdiction
j=x[(x.collector_jurisdiction!="")&(x.jurisdiction_country_annotated!="XX")]
rows.append(dict(field="Jurisdiction (collector code vs annotated from text)",n=len(j),agreement=round((j.collector_jurisdiction==j.jurisdiction_country_annotated).mean(),3),kappa=np.nan))
# year
y=x[(x.collector_year.str.match(r"^\d{4}$"))&x.pub_year.notna()]
rows.append(dict(field="Year (collector vs annotated, within 1 year)",n=len(y),agreement=round(((y.collector_year.astype(int)-y.pub_year.astype(int)).abs()<=1).mean(),3),kappa=np.nan))
# instrument type -> class
TY2C={"statute_or_act":"governance_instrument_binding","regulation_or_decree":"governance_instrument_binding","bill_or_draft_law":"governance_proposal_or_draft","policy_guideline_or_code_of_practice":"governance_instrument_soft","technical_standard":"governance_instrument_soft","ethical_framework_or_principles":"governance_instrument_soft","national_strategy_or_action_plan":"governance_instrument_soft","government_report_or_review":"government_report_or_parliamentary","parliamentary_material":"government_report_or_parliamentary","consultation_or_white_paper":"governance_proposal_or_draft","procurement_or_internal_policy":"governance_instrument_soft","international_agreement_or_resolution":"governance_instrument_soft","court_decision":"government_report_or_parliamentary"}
t=x[x.instrument_type.isin(TY2C)]
rows.append(dict(field="Document class (collector instrument type mapped to class vs annotated class)",n=len(t),agreement=round((t.instrument_type.map(TY2C)==t.doc_class).mean(),3),kappa=round(kappa(t.instrument_type.map(TY2C),t.doc_class),3) if len(t) else np.nan))
t37=pd.DataFrame(rows); write_table("T57_collector_vs_annotation",t37,"Agreement between the collectors' metadata (recorded from catalogue pages) and the metadata-blind annotation of the document text, round-2 usable documents")
ct=pd.crosstab(t.instrument_type,t.doc_class.map(DCL)); ct.index.name="collector instrument type"
write_table("T58_collector_type_vs_class",ct.reset_index(),"Collector instrument type versus annotated document class (round-2 usable documents)")

# ---------- T39: newly captured binding embodied instruments; T40: new robot-specific instruments
def inst_table(df):
    d=df.sort_values(["study_region","jurisdiction_country","year_final"])
    return pd.DataFrame(dict(doc_id=d.doc_id,title=d.title_en.fillna(d.collection_title).str.slice(0,110),jurisdiction=d.jurisdiction_country,year=d.year_final.astype("Int64"),doc_class=d.doc_class.map(DCL),status=d.instrument_status,relevance=d.relevance_to_embodied_ai_governance,primary_category=d.primary_embodied_category.fillna("").map(lambda s: nice(s) if s else ""),source=d.source_url.str.slice(0,80)))
nb=r3[r3.binding&r3.embodied_set]; write_table("T59_new_binding_embodied",inst_table(nb),f"Binding instruments in the embodied-AI set added by round 2 (n={len(nb)})")
nr=r3[r3.robot_specific]; write_table("T60_new_robot_specific",inst_table(nr),f"Robot-specific governance instruments (relevance 2+) added by round 2 (n={len(nr)})")

# ---------- coverage audit comparison (T25 produced by 18_analysis_D in each version)
# recomputed here for both versions with the same (corrected) reference list and the title-match rule used by 18_analysis_D
ref=pd.read_csv(B+"data/reference_instruments.csv"); cov={}
for tag,(uu,_a) in [("v2",(u2,a2)),("v3",(u3,a3))]:
    titles=uu.title_en.fillna("")+" "+uu.collection_title.fillna(""); cap=0; cap_loose=0; missing=[]
    strict=(uu.instrument&uu.content_capture) if "content_capture" in uu.columns else uu.gov   # same criterion as T25: a principal instrument with a content-analysed capture
    for _,rr in ref.iterrows():
        pat=re.compile(rr.pattern,re.I); hit=any(pat.search(t) and g for t,g in zip(titles,strict)); hit_loose=any(pat.search(t) and g for t,g in zip(titles,uu.gov))
        cap+=int(hit); cap_loose+=int(hit_loose)
        if not hit: missing.append(rr.instrument)
    cov[tag]=dict(n=len(ref),captured=cap,captured_loose=cap_loose,missing=missing)
R("round2_coverage",cov)

# ---------- figures
# F50 funnel
stages=[("Candidates discovered (after de-duplication)",len(inv)),("Text obtained",int(inv.has_text.sum())),("Content-analysed (annotated)",int(inv.content_analysed.sum())),("Entered the master table (assembly de-duplication)",int((a3.collection_set=="round2").sum())),("Usable captures",len(r3)),("Embodied-AI set",int(r3.embodied_set.sum())),("Governance instruments (embodied)",int((r3.instrument&r3.embodied_set).sum())),("Robot-specific instruments",int(r3.robot_specific.sum())),("Binding, embodied",int((r3.binding&r3.embodied_set).sum()))]
pd.DataFrame(stages,columns=["stage","n"]).to_csv(FD+"F50_round2_funnel.csv",index=False)
for th in ("light","dark"):
    t=fs.setup(th); fig,ax=plt.subplots(figsize=(7.2,3.6))
    fs.hbar(ax,[s for s,_ in stages],[n for _,n in stages],color=t["cat"][0],theme=th)
    ax.set_xlabel("Documents"); ax.set_title(f"Round 2: {len(inv):,} candidates discovered, {int(inv.has_text.sum()):,} with text, {int(r3.robot_specific.sum())} robot-specific instruments after blind annotation",loc="left",fontsize=9.5)
    fs.save(fig,"F50_round2_funnel",th)
# F51 before/after by region (embodied instruments)
d=t34[t34.region!="Unknown"]; d.to_csv(FD+"F51_before_after_region.csv",index=False)
for th in ("light","dark"):
    t=fs.setup(th); fig,ax=plt.subplots(figsize=(7.2,3.6)); y=np.arange(len(d)); h=0.38
    ax.barh(y-h/2,d.v2_embodied_instruments,height=h,color=t["cat"][0],label="v2 (original collection)"); ax.barh(y+h/2,d.v3_embodied_instruments,height=h,color=fs.SEQ[6],label="v3 (with round 2)")
    for yy,v in zip(y-h/2,d.v2_embodied_instruments): ax.text(v+0.5,yy,f"{v}",va="center",fontsize=7,color=t["ink2"])
    for yy,v in zip(y+h/2,d.v3_embodied_instruments): ax.text(v+0.5,yy,f"{v}",va="center",fontsize=7,color=t["ink2"])
    ax.set_yticks(y); ax.set_yticklabels(d.region.map(RSHORT)); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Embodied-AI governance instruments (usable, content-analysed)"); ax.set_xlim(0,d.v3_embodied_instruments.max()*1.25); ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=2,frameon=False)
    gain=t34.assign(g=t34.v3_embodied_instruments-t34.v2_embodied_instruments).sort_values("g",ascending=False); ax.set_title(f"Embodied-AI instruments rose from {c2['instruments_embodied']} to {c3['instruments_embodied']} after round 2; {RSHORT.get(gain.region.iloc[0],gain.region.iloc[0])} and {RSHORT.get(gain.region.iloc[1],gain.region.iloc[1])} gained most",loc="left",fontsize=9.5)
    fs.save(fig,"F51_before_after_region",th)
# F52 round-2 classes stacked by embodied/not
d=t36.copy(); d["other"]=d.documents-d.embodied_set; d.to_csv(FD+"F52_round2_classes.csv",index=False)
for th in ("light","dark"):
    t=fs.setup(th); fig,ax=plt.subplots(figsize=(7.2,3.2)); y=np.arange(len(d))
    ax.barh(y,d.embodied_set,color=t["cat"][0],height=0.62,label="Embodied-AI set"); ax.barh(y,d.other,left=d.embodied_set,color=t["cat"][1],height=0.62,label="General-AI or other")
    for yy,(a_,b_) in enumerate(zip(d.embodied_set,d.documents)): ax.text(b_+1,yy,f"{b_} ({a_} embodied)",va="center",fontsize=7,color=t["ink2"])
    ax.set_yticks(y); ax.set_yticklabels(d.doc_class); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Round-2 documents (annotated)"); ax.legend(loc="lower right")
    ax.set_title("What the blind annotation made of the round-2 candidates: most are instruments, not commentary",loc="left",fontsize=9.5)
    fs.save(fig,"F52_round2_classes",th)

# ---------- narrative (every number in the companion report is a computed variable; the generated Markdown is never edited by hand)
om=c3["instruments_embodied"]/c2["instruments_embodied"] if c2["instruments_embodied"] else np.nan
blocked_n=int((~inv.has_text&(inv.fetch_status=="blocked_host")).sum()); thin_n=int((~inv.has_text&inv.fetch_status.str.match(r"^\d")).sum())
n_notext=int((~inv.has_text).sum()); fail_n=n_notext-blocked_n-thin_n
n_bind_notext=int(((~inv.has_text)&(inv.binding_nature=="legally_binding")).sum())
agents_rows=int((~inv.source.str.startswith("API_")).sum()); api_rows=int(inv.source.str.startswith("API_").sum())
n_agents=int(inv[~inv.source.str.startswith("API_")].source.nunique()); n_api_runs=int(inv[inv.source.str.startswith("API_")].source.nunique())
n_fetched=int((inv.has_text&(inv.text_status!="agent_abstract")).sum()); n_scope=int((inv.has_text&(inv.text_status=="agent_abstract")).sum())
n_r2_master=int((a3.collection_set=="round2").sum()); n_removed_assembly=int(inv.content_analysed.sum())-n_r2_master
# counting unit within the usable round-2 documents: legal_text = every text of instrument class; instrument = principal instruments (principal + amendment)
rel2=r3.relevance_to_embodied_ai_governance>=2
n_legal_r2=int(r3.legal_text.sum()); n_principal_r2=int(r3.instrument.sum())
n_emb_legal_r2=int((r3.legal_text&r3.embodied_set).sum()); n_emb_principal_r2=int((r3.instrument&r3.embodied_set).sum())
n_bind_emb_legal_r2=int((r3.binding_text&r3.legal_text&r3.embodied_set).sum()); n_bind_emb_principal_r2=int((r3.binding&r3.embodied_set).sum())
n_bind_emb_robot_r2=int((r3.binding&r3.embodied_set&rel2).sum()); n_bind_emb_auto_r2=int((r3.binding&r3.embodied_set&r3.autonomy_terms.astype(bool)).sum()); n_bind_emb_ai_r2=int((r3.binding&r3.embodied_set&r3.ai_explicit.astype(bool)).sum())
unit_r2=r3[r3.legal_text&r3.embodied_set].instrument_unit.value_counts()
n_cat_r2=int(unit_r2.get("catalogue_page",0)); n_stub_r2=int(unit_r2.get("stub",0)); n_anc_r2=int(sum(unit_r2.get(k,0) for k in ["ancillary","dependent","incorporation","language_copy","duplicate_text"]))
MIN_WORDS=int(a3[a3.words_ok.astype(bool)].words.min()); assert bool((a3.words_ok.astype(bool)==(a3.words.fillna(0)>=MIN_WORDS)).all())   # capture-tier floor set in 07c (words_ok), checked against the data
excerpt_chars=sum(int(v) for v in re.findall(r"(?:head|mid|tail)=(\d+)",str(r3._policy.dropna().iloc[0])))
n_std_r2=int((r3.doc_type=="technical_standard").sum()); n_std_landing_r2=int(((r3.doc_type=="technical_standard")&(r3.page_quality=="landing_or_index_page")).sum())
# CJK re-annotation (character-aware cleaner, policy tag cjk_clean=v4), measured against the previous version's master table where it is available
V3="/home/user/embodied-ai-governance-v3/"; a4i=a3.set_index("doc_id")
def _emb(d): return ((d.relevance_to_embodied_ai_governance>=2)|(d.embodied_categories.fillna("")!=""))&(d.ai_scope!="not_ai")
if os.path.exists(V3+"data/master_table.csv"):
    m3v=pd.read_csv(V3+"data/master_table.csv",low_memory=False); a3v=m3v[m3v.annotated].set_index("doc_id")
    common=a4i[a4i._policy.fillna("").str.contains("cjk_clean")].index.intersection(a3v.index)   # documents actually re-annotated with the character-aware cleaner and present in the previous version
    n_cjk_r2=int((a3v.loc[common].collection_set=="round2").sum()); n_cjk_r1=len(common)-n_cjk_r2
    n_cjk_changed=int((_emb(a4i.loc[common])!=_emb(a3v.loc[common])).sum()); n_cjk_notai_before=int((a3v.loc[common].ai_scope=="not_ai").sum()); n_cjk_notai_after=int((a4i.loc[common].ai_scope=="not_ai").sum())
    cjk_change_txt=f"; of these {len(common)} documents, {n_cjk_changed} changed embodied-set membership and the number rated as not about AI fell from {n_cjk_notai_before} to {n_cjk_notai_after}"
    new_r2=sorted(set(a3[a3.collection_set=="round2"].doc_id)-set(m3v[m3v.collection_set=="round2"].doc_id)); n_new_texts=len(new_r2)
    u3v=a3v[a3v.text_usable&(a3v.page_quality!="error_or_blocked_page")&(a3v.doc_class!="unusable")]; N3_binding_emb=int(((u3v.doc_class=="governance_instrument_binding")&_emb(u3v)).sum())
else:
    cjkpol=a3._policy.fillna("").str.contains("cjk_clean")&a3.language.isin(["zh","ja","ko"])
    n_cjk_r2=int((cjkpol&(a3.collection_set=="round2")).sum()); n_cjk_r1=int((cjkpol&(a3.collection_set!="round2")).sum()); cjk_change_txt=" (the change in set membership is not recomputed here because the previous version's master table is not available)"
    n_new_texts=int(((a3.collection_set=="round2")&~a3.language.isin(["zh","ja","ko"])&a3._policy.fillna("").str.contains("cjk_clean")).sum())   # texts annotated after the cleaner change that are not CJK re-annotations
    N3_binding_emb=int(json.load(open(B+"data/results.json")).get("precision_audit",{}).get("v3_binding_embodied",0))
# precision audit of the previous version's binding embodied instruments (random n = 100), recomputed from the auditor's sample file, and the rule-based unit on the same documents
pa=pd.read_csv(B+"review/v3_reviews/precision_audit_sample.csv",dtype=str,keep_default_na=False)
def _Y(c): return pa[c].str.strip().str.upper().str.startswith("Y")
pa_n=len(pa); pa_a=int(_Y("a").sum()); pa_b=int(_Y("b").sum()); pa_c=int(_Y("c").sum()); pa_d=int(_Y("d").sum()); pa_e=int(_Y("e").sum())
aud=(_Y("a")&_Y("b")&_Y("c")).astype(bool); pa_joint=int(aud.sum()); pa_lo,pa_hi=wilson(pa_joint,pa_n)
pa_corr=round(N3_binding_emb*pa_joint/pa_n); pa_corr_lo=round(N3_binding_emb*pa_lo); pa_corr_hi=round(N3_binding_emb*pa_hi)
rule=pa.doc_id.map(lambda d: bool(a4i.loc[d,"instrument"]) and bool(a4i.loc[d,"embodied_set"]) and int(a4i.loc[d,"relevance_to_embodied_ai_governance"])>=2 if d in a4i.index else False).astype(bool)
rule_n=int(rule.sum()); rule_lo,rule_hi=wilson(rule_n,pa_n); rule_agree=int((rule.values==aud.values).sum()); rule_kappa=kappa(aud,rule)
# collector metadata versus annotation (T57) and the same check split by collector agents and scripted harvesters
agr_bind=float(t37.agreement.iloc[0]); kap_bind=float(t37.kappa.iloc[0]); n_bind_cmp=int(t37.n.iloc[0])
agr_jur=float(t37.agreement.iloc[1]); n_jur_cmp=int(t37.n.iloc[1]); agr_year=float(t37.agreement.iloc[2]); n_year_cmp=int(t37.n.iloc[2])
agr_class=float(t37.agreement.iloc[3]); kap_class=float(t37.kappa.iloc[3]); n_class_cmp=int(t37.n.iloc[3])
bs=b.join(cj[["source"]],on="doc_id"); isapi=bs.source.fillna("").str.startswith("API_")
def _agr(d):
    cb=d.collector_binding=="legally_binding"; ab=d.doc_class=="governance_instrument_binding"; return len(d),float((cb==ab).mean()),kappa(cb,ab)
n_bind_agent,agr_bind_agent,kap_bind_agent=_agr(bs[~isapi]); n_bind_api,agr_bind_api,kap_bind_api=_agr(bs[isapi])
# round-2 reliability sample (second model and same-model re-run), median kappa over single-label and ordinal fields and the weakest fields
def _rel(path):
    d=pd.read_csv(path); s=d[d.type.isin(["single","ordinal"])]; return float(s.kappa.median()),s[s.type=="single"].nsmallest(5,"kappa")
k_r2_opus,weak_opus=_rel(B+"data/reliability_fields_r2opus.csv"); k_r2_rerun,_w=_rel(B+"data/reliability_fields_r2rerun.csv"); n_rel_r2=int(pd.read_csv(B+"data/reliability_fields_r2opus.csv").n.max())
weak_txt="; ".join(f"{f.replace('_',' ')} {k:.2f}" for f,k in zip(weak_opus.field,weak_opus.kappa))
# document-level corrections from the governance expert's audit, and that audit's own error rate from its released row table
ov=pd.read_csv(B+"data/manual_overrides_v4.csv",dtype=str,keep_default_na=False); n_ov=len(ov); n_ov_docs=int(ov.doc_id.nunique()); n_ov_r2=int(ov.doc_id.str.startswith("R2").sum())
ga=pd.read_csv(B+"review/v3_reviews/governance_audit_rows.csv",dtype=str,keep_default_na=False); gcodes=ga.error.str.upper().str.findall(r"\b([A-G])\b")
n_gaud=len(ga); n_gaud_err=int(gcodes.map(lambda c: len(c)>0).sum()); n_gaud_mat=int(gcodes.map(lambda c: any(x in "ABCDG" for x in c)).sum())
_W={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}; _w=lambda n: _W.get(int(n),f"{int(n):,}")   # small counts as words in prose
md=f"""*Companion to the analysis report. All counts refer to content-analysed documents unless stated otherwise. The headline counting unit is the principal instrument: a text of instrument class that is not a commencement order, levy or fee instrument, individual exemption, direction, approval or permit, definitions-only part, table of contents, EEA incorporation decision, language-version corrigendum, byte-identical duplicate, catalogue page or metadata stub under {MIN_WORDS} words; amendments count. Every count that uses another unit says so. The round-2 collectors, the reviewers of the previous version and the auditors were AI agents (Claude) running in one Claude Code session; no person read or labelled any document.*

## Summary

The first collection contained {c2['documents']:,} documents, of which {c2['instruments_embodied']} were texts of instrument class in the embodied-AI set and {c2['instruments_robot_specific']} were robot-specific. Round 2 searched official legal databases, government repositories, standards catalogues, treaty-body archives and regulator sites for instruments that the first collection had not captured. After de-duplication against the first collection and within the round, {len(inv):,} candidates remained ({agents_rows:,} from {_w(n_agents)} specialised collector agents and {api_rows:,} from {_w(n_api_runs)} scripted harvester runs over official legal databases). Text could be obtained for {int(inv.has_text.sum()):,} of them ({n_fetched:,} fetched from the issuing source and {n_scope} standards scope texts; {_w(n_new_texts)} of these were recovered in a retry pass after the review of the previous version), {int(inv.content_analysed.sum()):,} were annotated with the same metadata-blind, extended-excerpt policy as the first collection's governance documents (up to {excerpt_chars:,} characters), and {n_r2_master:,} entered the master table after {n_removed_assembly} duplicates were removed (identical normalised title and jurisdiction, mostly against other round-2 rows).

The blind annotation confirms that most additions are legal texts rather than commentary, and the counting unit then matters. Of the {len(r3):,} usable round-2 documents, {n_legal_r2:,} are texts of instrument class and {n_principal_r2} are principal instruments; {n_emb_legal_r2} of the instrument-class texts are in the embodied-AI set, of which {n_emb_principal_r2} are principal instruments and {int(r3.robot_specific.sum())} are principal instruments rated robot-relevant (relevance 2 or 3). The {n_emb_legal_r2-n_emb_principal_r2} embodied-set texts that are not principal instruments are {n_cat_r2} catalogue or register pages, {n_stub_r2} metadata stubs and {n_anc_r2} ancillary, dependent, incorporation or language-copy acts. Among binding texts, {n_bind_emb_legal_r2} embodied-set texts resolve into {n_bind_emb_principal_r2} principal binding instruments, {n_bind_emb_robot_r2} of them robot-relevant, {n_bind_emb_auto_r2} with autonomy or AI provisions in the text and {n_bind_emb_ai_r2} naming AI explicitly: most binding rules that reach robots in this collection are machine-class rules (aviation, road vehicle, machinery, product safety) with no AI content.

Across the merged collection, on the comparable unit (every text of instrument class), embodied-AI governance instruments rose from {c2['instruments_embodied']} to {c3['instruments_embodied']} (x{om:.1f}), robot-specific instruments from {c2['instruments_robot_specific']} to {c3['instruments_robot_specific']}, and binding embodied instruments from {c2['binding_embodied']} to {c3['binding_embodied']}. These ratios describe where the two collections searched, not a change in the world: the first collection searched the web for material about embodied AI; the second searched legal databases for the machine-class rules. On the headline unit the merged collection holds {c3['principal_embodied']} principal embodied instruments ({c3['principal_robot_specific']} robot-relevant; {c3['principal_embodied_autonomy_or_ai']} with autonomy or AI provisions and {c3['principal_embodied_ai_explicit']} naming AI explicitly) and {c3['principal_binding_embodied']} principal binding instruments ({c3['principal_binding_robot_specific']} robot-relevant; {c3['families_binding_embodied']} when counted once per instrument family; {c3['binding_embodied_autonomy_or_ai']} with autonomy or AI provisions and {c3['binding_embodied_ai_explicit']} naming AI explicitly; T53b). The coverage audit against the {cov['v3']['n']} reference instruments moved from {cov['v2']['captured']} captured in the first collection to {cov['v3']['captured']} on the strict criterion (a principal instrument with a content-analysed capture) and from {cov['v2']['captured_loose']} to {cov['v3']['captured_loose']} on the looser title-family match used previously. Still missing under the strict criterion: {'; '.join(cov['v3']['missing'])}.

{{{{T53}}}}

## Where the candidates came from

The table gives, per source, the candidates after de-duplication, the texts obtained, the usable documents and what the blind annotation made of them; "instruments" are principal instruments. The Australian register shows the effect of the counting unit: its candidates are usable and mostly in the embodied-AI set, but they are register pages and individual approvals, directions and exemptions, so almost none is a principal instrument.

{{{{T50}}}}

{{{{F50}}}}

## What could and could not be fetched

{{{{T51}}}}

{{{{T52}}}}

Candidates without text remain in the inventory (data/round2_inventory.csv) with their metadata but are not part of any content-analysed count. The main losses are catalogue pages behind bot challenges or outside the sandbox network policy ({blocked_n} candidates on blocked hosts; {thin_n} with HTTP errors or JavaScript-only pages; {fail_n} failed transfers). A retry pass with the improved routes after the review of the previous version recovered {_w(n_new_texts)} texts; {n_bind_notext} of the {n_notext} candidates still without text were recorded by their collectors as legally binding. They include instruments a collector verified but the environment could not read (the Hangzhou embodied-robot regulations, the Shenzhen intelligent-connected-vehicle, AI-industry and low-altitude-economy regulations, Hong Kong Cap. 374AF, the Korean Intelligent Robots Act and autonomous-vehicle decrees, DoD Directive 3000.09, California SB 243, India's Drone Rules 2021, the EU Product Liability Directive and Toy Safety Regulation, the French automated-vehicle ordinance and decree, ANSI/A3 R15.06-2025 and GB/T 48317.1-2026); the methods document lists them as the first targets of a third round.

## Before and after, by region and robot group

These comparisons are on the comparable unit (every text of instrument class) because the first collection carries no counting-unit flags; they measure the change of collection strategy, not a change in the world.

{{{{F51}}}}

{{{{T54}}}}

{{{{T55}}}}

## What the blind annotation made of the additions

The excerpt cleaner used for the previous version deleted most of the text of Chinese, Japanese and Korean documents before the model saw it (a rule for Latin-script navigation menus dropped every line without a digit, capital letter or ASCII sentence punctuation). The cleaner was made character-aware and {n_cjk_r2} round-2 and {n_cjk_r1} round-1 documents in those languages were re-annotated{cjk_change_txt}. Four rules then correct status and class labels the annotation got wrong at scale (standards in development are drafts, mandatory GB standards are binding, CCW working papers and chair's texts are position documents, proposals whose adopted act is present are superseded), and {n_ov} document-level corrections on {n_ov_docs} documents ({n_ov_r2} rows concern round-2 documents) were converted from the governance expert's audit of the previous version; in that audit's released row table, {n_gaud_err} of {n_gaud} risk-stratified rows carry an error code and {n_gaud_mat} a material one, so these are upper bounds for the tables as a whole. The class counts below are after these corrections.

{{{{F52}}}}

{{{{T56}}}}

## Do the collectors' catalogue labels agree with the blind reading of the text?

This is a consistency check, not a validation. The collector agents were AI agents of the same model family as the annotator, the {api_rows:,} harvested rows carry one constant label per source written into the harvester, and no person recorded any of the reference values. On the usable round-2 documents the annotation agrees with the collector label on whether an instrument is legally binding in {100*agr_bind:.1f}% of cases (kappa {kap_bind:.2f}, n = {n_bind_cmp:,}), on jurisdiction in {100*agr_jur:.1f}% (n = {n_jur_cmp:,}), on year within one in {100*agr_year:.1f}% (n = {n_year_cmp:,}) and on document class in {100*agr_class:.1f}% (kappa {kap_class:.2f}, n = {n_class_cmp:,}). Split by origin, binding-nature agreement is {100*agr_bind_agent:.1f}% (kappa {kap_bind_agent:.2f}, n = {n_bind_agent:,}) for collector-agent rows and {100*agr_bind_api:.1f}% (kappa {kap_bind_api:.2f}, n = {n_bind_api:,}) for harvested rows. The reliability evidence for round-2 labels is a stratified sample of {n_rel_r2} round-2 documents re-annotated by a second model and by a same-model re-run: median kappa over single-label and ordinal fields {k_r2_opus:.2f} and {k_r2_rerun:.2f}; the weakest fields against the second model are {weak_txt} (tables S09 and S09b).

{{{{T57}}}}

{{{{T58}}}}

## Newly captured instruments

T59 lists the {n_bind_emb_principal_r2} principal binding instruments in the embodied-AI set added by round 2 and T60 the {int(r3.robot_specific.sum())} principal instruments rated robot-relevant. Their precision is bounded by an independent audit of the previous version's binding embodied list: of {pa_n} randomly sampled documents from that list of {N3_binding_emb}, {pa_a} were distinct instruments, {pa_b} binding, {pa_c} carried substantive embodied provisions, {pa_d} contained autonomy or AI content and {pa_e} named AI explicitly; {pa_joint} met all of distinct, binding and substantive (95% Wilson interval {100*pa_lo:.0f} to {100*pa_hi:.0f}%), which implies about {pa_corr} such instruments ({pa_corr_lo} to {pa_corr_hi}) in that list rather than {N3_binding_emb}. The rule-based unit used here (principal instrument, embodied set, relevance 2 or 3) passes {rule_n} of the same {pa_n} documents ({100*rule_lo:.0f} to {100*rule_hi:.0f}%) and agrees with the audit on {rule_agree} (kappa {rule_kappa:.2f}; T62). The counts in these tables are therefore upper bounds on precision, and the unread candidates above make them lower bounds on coverage.

{{{{T59}}}}

{{{{T60}}}}

## Method notes and limitations

- Discovery combined {_w(n_agents)} collector agents (regional, thematic and standards briefs with explicit exclusion lists of the first collection's holdings) and scripted harvests of EUR-Lex (CELLAR SPARQL, by title and by EuroVoc concept), legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register of Legislation, the US eCFR and the Brazilian Camara API ({_w(n_api_runs)} harvester runs). Title-searched harvests were filtered with an inclusion/exclusion keyword list before fetching; full-text harvests were not. The collector agents were Claude subagents running in one Claude Code session; the harvesters' instrument type, binding nature and status fields are constants per source.
- Candidates were de-duplicated on normalised URL and on normalised title plus jurisdiction, within the round and against the first collection's registry; the assembly step applies a second title-based pass across the merged collection ({n_removed_assembly} round-2 rows removed). Byte-identical texts of instrument class count once, and titles that differ only in year, act number, version or amendment wording within one jurisdiction form an instrument family, offered as a further counting unit.
- Counting unit: headline counts use principal instruments; T53b gives the merged collection under each unit and under the two text-based AI-content tiers (autonomy or AI provisions; AI named explicitly). Comparisons with the first collection (T53 to T55) stay on the comparable unit, every text of instrument class, and are consequences of collection design rather than findings about the world; the same holds for the number of jurisdictions with an embodied instrument and for the share of instruments that are binding.
- Capture tier: statistics about what instruments specify in depth use content-analysed captures with at least {MIN_WORDS} words; catalogue and landing pages are a separate unit and never enter depth statistics. For ISO and other standards only the public scope or abstract page is available ({n_std_landing_r2} of the {n_std_r2} round-2 standards are catalogue or landing pages), so those documents are annotated on a short text, flagged as such in the registry, and reported as a separate measurement.
- Texts were fetched from the primary URL with a secondary fallback (CELLAR for EUR-Lex, the UN document API for UNODA and undocs links, the ISO committee mirror for ISO catalogue pages, XML for legislation.gov.uk), and every failed fetch was retried once more after the review of the previous version ({_w(n_new_texts)} texts recovered). The collectors' shared web-search budget was exhausted part-way through several briefs; later verification relied on direct fetches of official sites. Jurisdictions whose law is not exposed through a reachable database (for example Légifrance, the Singapore statutes site, the Korean, Taiwanese and Hong Kong law portals, the National People's Congress database and several ministry sites) are under-represented, and {n_bind_notext} verified candidates recorded as legally binding remain unread.
- Annotation used the metadata-blind extended-excerpt policy (collector metadata stripped, first {excerpt_chars:,} characters in three slices), so round-2 and first-collection governance documents are directly comparable. The character-aware cleaner (policy tag cjk_clean=v4) replaced the rule that deleted Chinese, Japanese and Korean text, and {n_cjk_r2+n_cjk_r1} documents were re-annotated. Four status and class rules and {n_ov} documented document-level corrections from the governance expert's audit are applied after annotation; the statement in the previous version that no manual overrides touched round-2 rows no longer holds ({n_ov_r2} of the {n_ov} correction rows concern round-2 documents). Statutes harvested as consolidated texts carry the year the annotation found, which may be the enactment or the consolidation year; time analyses are restricted to 2014 to 2026 with 2026 partial.
- Validity: every label is model-produced. The collector-agreement tables are a consistency check between AI-agent labels, harvester constants and the annotation; the round-2 reliability sample (n = {n_rel_r2}; median kappa {k_r2_opus:.2f} against a second model, {k_r2_rerun:.2f} for a re-run) measures stability between models, not correctness. No person read or labelled any document, and no human validation exists. The precision audit shows that about {100*pa_joint/pa_n:.0f}% of the previous version's binding embodied instruments were distinct, binding and substantive, so every instrument count here is an upper bound on precision; the unread candidates make every count a lower bound on coverage within this collection.
- Not addressed: human validation of labels (no human coders available in this setting); full-text annotation of statutes longer than the {excerpt_chars:,}-character excerpt, whose robot provisions may lie beyond it; stricter merging of near-duplicate title pairs beyond the instrument-family grouping.
"""
os.makedirs(B+"report/src",exist_ok=True); open(B+"report/src/collection_round2.md","w",encoding="utf8").write(md)
R("round2_counts",{"candidates":len(inv),"with_text":int(inv.has_text.sum()),"annotated":int(inv.content_analysed.sum()),"usable":len(r3),"embodied":int(r3.embodied_set.sum()),"instruments":int(r3.instrument.sum()),"embodied_instruments":int((r3.instrument&r3.embodied_set).sum()),"robot_specific":int(r3.robot_specific.sum()),"binding_embodied":int((r3.binding&r3.embodied_set).sum())})
# merge into results.json
try:
    res=json.load(open(B+"data/results.json")); res.update({k:v for k,v in RESULTS.items()}); json.dump(res,open(B+"data/results.json","w"),indent=1,ensure_ascii=False,default=str)
except Exception as e: print("results.json merge skipped:",e)
print(json.dumps(c2)); print(json.dumps(c3)); print("coverage",cov)
