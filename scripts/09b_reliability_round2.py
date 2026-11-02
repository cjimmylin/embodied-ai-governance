#!/usr/bin/env python3
"""Reliability on a stratified sample of round-2 documents: second model (Opus) and same-model re-run versus the final round-2 annotations.
Usage: python3 09b_reliability_round2.py annotations/reliability_round2_opus _r2opus"""
import json, glob, sys, numpy as np, pandas as pd
from sklearn.metrics import cohen_kappa_score
B="/home/user/embodied-ai-governance-v5/"
def load(d): return {json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+d+"/R2-*.json")}
SECOND=sys.argv[1]; OUTTAG=sys.argv[2] if len(sys.argv)>2 else "_r2"
A=load("annotations/round2"); R=load(SECOND); ids=sorted(set(A)&set(R)); print("overlap docs:",len(ids))
SINGLE=["issuer_type","date_basis","jurisdiction_country","jurisdiction_scope","doc_type","doc_class","is_governance_document","instrument_status","binding_nature","publication_stage","ai_scope","embodiment_status","primary_embodied_category","page_quality","stance_toward_regulation","dominant_governance_framing","language","legal_personhood_position"]
MULTI=["embodied_categories","application_sectors","governance_topics","governance_mechanisms"]
PR=list(A[ids[0]]["principles"].keys())
def kappa(a,b,weights=None):
    try: return cohen_kappa_score(a,b,weights=weights)
    except Exception: return np.nan
rows=[]
for f in SINGLE:
    if f not in A[ids[0]]: continue
    a=[str(A[i].get(f)) for i in ids]; b=[str(R[i].get(f)) for i in ids]
    rows.append(dict(field=f,type="single",n=len(ids),percent_agreement=float(np.mean([x==y for x,y in zip(a,b)])),kappa=kappa(a,b)))
a=[A[i].get("pub_year") for i in ids]; b=[R[i].get("pub_year") for i in ids]; both=[(x,y) for x,y in zip(a,b) if x is not None and y is not None]
rows.append(dict(field="pub_year (within 1 year)",type="numeric",n=len(both),percent_agreement=float(np.mean([abs(x-y)<=1 for x,y in both])) if both else np.nan,kappa=np.nan))
a=[A[i]["relevance_to_embodied_ai_governance"] for i in ids]; b=[R[i]["relevance_to_embodied_ai_governance"] for i in ids]
rows.append(dict(field="relevance_to_embodied_ai_governance",type="ordinal",n=len(ids),percent_agreement=float(np.mean([x==y for x,y in zip(a,b)])),kappa=kappa(a,b,weights="quadratic")))
for f in MULTI:
    labs=sorted({x for i in ids for x in (A[i].get(f) or [])+(R[i].get(f) or [])})
    for l in labs:
        a=[int(l in (A[i].get(f) or [])) for i in ids]; b=[int(l in (R[i].get(f) or [])) for i in ids]
        if sum(a)+sum(b)<6: continue
        rows.append(dict(field=f"{f}:{l}",type="multi",n=len(ids),percent_agreement=float(np.mean([x==y for x,y in zip(a,b)])),kappa=kappa(a,b)))
for p in PR:
    a=[A[i]["principles"][p] for i in ids]; b=[R[i]["principles"][p] for i in ids]
    rows.append(dict(field=f"principle:{p} (any)",type="binary",n=len(ids),percent_agreement=float(np.mean([(x>0)==(y>0) for x,y in zip(a,b)])),kappa=kappa([int(x>0) for x in a],[int(y>0) for y in b])))
    rows.append(dict(field=f"principle:{p} (level)",type="ordinal",n=len(ids),percent_agreement=float(np.mean([x==y for x,y in zip(a,b)])),kappa=kappa(a,b,weights="quadratic")))
d=pd.DataFrame(rows); d.to_csv(B+f"data/reliability_fields{OUTTAG}.csv",index=False)
print(d[d.type.isin(["single","ordinal"])][["field","n","percent_agreement","kappa"]].round(3).to_string()); print("median kappa (single+ordinal):",round(d[d.type.isin(["single","ordinal"])].kappa.median(),3))
