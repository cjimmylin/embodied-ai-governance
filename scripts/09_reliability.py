#!/usr/bin/env python3
"""Inter-annotator reliability between the main model (Sonnet) and the second model (Opus) on the 10% sample,
plus cross-checks against collector labels. Outputs data/reliability_fields.csv and data/reliability_team_crosscheck.csv."""
import json, glob, os, numpy as np, pandas as pd
from sklearn.metrics import cohen_kappa_score
B="/home/user/embodied-ai-governance-v5/"
def load(d): return {json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+d+"/D*.json")}
import sys
SECOND=sys.argv[1] if len(sys.argv)>1 else "annotations/reliability_opus"
OUTTAG=sys.argv[2] if len(sys.argv)>2 else ""
A=load("annotations/main"); A.update(load("annotations/main_clean")); R=load(SECOND)
ids=sorted(set(A)&set(R)); print("overlap docs:",len(ids))
SINGLE=["issuer_type","date_basis","jurisdiction_country","jurisdiction_scope","doc_type","doc_class","is_governance_document","instrument_status","binding_nature","publication_stage","ai_scope","embodiment_status","primary_embodied_category","primary_topic","robot_legal_personhood_position","risk_framing","stance_toward_regulation","methodology","faith_or_religious_perspective","page_quality","language"]
MULTI=["embodied_categories","application_sectors","governance_topics","governance_mechanisms"]
ORD=["relevance_to_embodied_ai_governance"]
PR=list(A[ids[0]]["principles"].keys())
rows=[]
def kappa(a,b,weights=None):
    try: return cohen_kappa_score(a,b,weights=weights)
    except Exception: return np.nan
for f in SINGLE:
    a=[str(A[i][f]) for i in ids]; b=[str(R[i][f]) for i in ids]
    rows.append(dict(field=f,type="single",n=len(ids),percent_agreement=np.mean([x==y for x,y in zip(a,b)]),kappa=kappa(a,b)))
# pub_year
a=[A[i]["pub_year"] for i in ids]; b=[R[i]["pub_year"] for i in ids]
both=[(x,y) for x,y in zip(a,b) if x is not None and y is not None]
rows.append(dict(field="pub_year (exact, both known)",type="numeric",n=len(both),percent_agreement=np.mean([x==y for x,y in both]) if both else np.nan,kappa=np.nan))
rows.append(dict(field="pub_year (within 1 year)",type="numeric",n=len(both),percent_agreement=np.mean([abs(x-y)<=1 for x,y in both]) if both else np.nan,kappa=np.nan))
rows.append(dict(field="pub_year (known in both)",type="numeric",n=len(ids),percent_agreement=len(both)/len(ids),kappa=np.nan))
for f in ORD:
    a=[A[i][f] for i in ids]; b=[R[i][f] for i in ids]
    rows.append(dict(field=f,type="ordinal",n=len(ids),percent_agreement=np.mean([x==y for x,y in zip(a,b)]),kappa=kappa(a,b,weights="quadratic")))
for f in MULTI:
    labels=sorted({l for i in ids for l in A[i][f]+R[i][f]})
    jac=[]
    for i in ids:
        s1,s2=set(A[i][f]),set(R[i][f]); jac.append(1.0 if not s1 and not s2 else len(s1&s2)/len(s1|s2))
    ks=[]
    for l in labels:
        a=[l in A[i][f] for i in ids]; b=[l in R[i][f] for i in ids]
        if sum(a)+sum(b)>=6: ks.append(kappa(a,b))
    rows.append(dict(field=f,type="multi-label",n=len(ids),percent_agreement=np.mean(jac),kappa=np.nanmean(ks) if ks else np.nan,note=f"Jaccard mean; kappa = mean per-label kappa over {len(ks)} labels with >=6 positives"))
for p in PR:
    a=[A[i]["principles"][p] for i in ids]; b=[R[i]["principles"][p] for i in ids]
    rows.append(dict(field="principle:"+p,type="ordinal 0-2",n=len(ids),percent_agreement=np.mean([x==y for x,y in zip(a,b)]),kappa=kappa(a,b,weights="quadratic"),
                     note=f"presence agreement={np.mean([(x>0)==(y>0) for x,y in zip(a,b)]):.2f}"))
rel=pd.DataFrame(rows); rel.to_csv(B+f"data/reliability_fields{OUTTAG}.csv",index=False)
pd.set_option("display.width",200); print(rel[["field","type","n","percent_agreement","kappa"]].round(3).to_string())
# cross-check against collector labels
m=pd.read_csv(B+"data/master_table.csv")
m=m[m.annotated]
out=[]
eu=m[m.collection_robot_focus.notna()]
if len(eu):
    team=(eu.collection_robot_focus!="General AI"); mine=eu.ai_scope.isin(["embodied_ai_robotics_general","embodied_ai_specific_category","general_ai_with_embodied_provisions"])
    out.append(dict(check="Europe collector 'Robot focus' (Robotics/Humanoid/Embodied vs General AI) vs annotated ai_scope (embodied incl. provisions vs general)",n=len(eu),agreement=np.mean(team==mine),kappa=kappa(team,mine)))
    mine2=eu.embodiment_status.isin(["physical_embodied","mixed"])
    out.append(dict(check="Europe collector 'Robot focus' vs annotated embodiment_status (physical/mixed vs none/software)",n=len(eu),agreement=np.mean(team==mine2),kappa=kappa(team,mine2)))
    tmap={"Research paper":"research","Government":"government","Intergovernmental body":"intergovernmental","Standards body":"standards"}
    imap={"academic_or_research":"research","national_government_executive":"government","legislature":"government","regulator_or_agency":"government","court_or_judiciary":"government","subnational_government":"government","intergovernmental_org":"intergovernmental","standards_body":"standards"}
    sub=eu[eu.collection_type.isin(tmap)&eu.issuer_type.isin(imap)]
    out.append(dict(check="Europe collector 'Type' vs annotated issuer_type (4 collapsed classes)",n=len(sub),agreement=np.mean(sub.collection_type.map(tmap)==sub.issuer_type.map(imap)),kappa=kappa(sub.collection_type.map(tmap),sub.issuer_type.map(imap))))
cc=m[m.collection_country.astype(str).str.fullmatch(r"[A-Z]{2}")]
if len(cc): out.append(dict(check="Collector 2-letter country vs annotated jurisdiction_country (research papers, first-author country)",n=len(cc),agreement=np.mean(cc.collection_country==cc.jurisdiction_country),kappa=np.nan))
sp=m[m.collection_set.notna()]
team=(sp.collection_set=="sprint"); mine=sp.relevance_to_embodied_ai_governance>=2
out.append(dict(check="Collector set (sprint=robotics vs database=general AI) vs annotated relevance>=2",n=len(sp),agreement=np.mean(team==mine),kappa=kappa(team,mine)))
tier=m[m.collection_tier.isin(["Core","Supporting","Context only"])]
if len(tier):
    out.append(dict(check="Collector tier Core vs annotated is_governance_document",n=len(tier),agreement=np.mean((tier.collection_tier=="Core")==tier.is_governance_document.astype(bool)),kappa=kappa(tier.collection_tier=="Core",tier.is_governance_document.astype(bool))))
x=pd.DataFrame(out); x.to_csv(B+"data/reliability_team_crosscheck.csv",index=False); print(x.round(3).to_string())
