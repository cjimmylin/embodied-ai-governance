#!/usr/bin/env python3
"""v4: reliability variants promised in the methods: unweighted kappa for ordinal fields and level-2 (in depth) agreement for principles,
for every reliability folder (round-1 samples and the round-2 samples). Writes data/reliability_variants.csv and tables/S09b_reliability_variants."""
import json, glob, numpy as np, pandas as pd, sys
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts"); from analysis_common import write_table, PRL
from sklearn.metrics import cohen_kappa_score
B="/home/user/embodied-ai-governance-v5/"
def load(d,pat): return {json.load(open(p))["doc_id"]:json.load(open(p))["annotation"] for p in glob.glob(B+d+"/"+pat)}
A1=load("annotations/main","D*.json"); A1.update(load("annotations/main_clean","D*.json")); A1.update(load("annotations/gov_extended","D*.json")); A2=load("annotations/round2","R2-*.json")
runs=[("Opus, round-1 sample","annotations/reliability_opus","D*.json",A1),("Sonnet re-run, round-1 sample","annotations/reliability_sonnet_rerun","D*.json",A1),("Sonnet full text, round-1 sample","annotations/reliability_fulltext","D*.json",A1),("Sonnet blind, round-1 sample","annotations/reliability_blind","D*.json",A1),("Opus, round-2 sample","annotations/reliability_round2_opus","R2-*.json",A2),("Sonnet re-run, round-2 sample","annotations/reliability_round2_rerun","R2-*.json",A2)]
def k(a,b,w=None):
    try: return float(cohen_kappa_score(a,b,weights=w))
    except Exception: return np.nan
rows=[]
for name,folder,pat,A in runs:
    R=load(folder,pat); ids=sorted(set(A)&set(R))
    if not ids: continue
    a=[A[i]["relevance_to_embodied_ai_governance"] for i in ids]; b=[R[i]["relevance_to_embodied_ai_governance"] for i in ids]
    rows.append(dict(comparison=name,n=len(ids),field="relevance (0-3)",kappa_quadratic=k(a,b,"quadratic"),kappa_unweighted=k(a,b),agreement_level2=np.nan))
    PR=list(A[ids[0]]["principles"].keys()); kq=[]; ku=[]; a2=[]; k2=[]
    for p in PR:
        a=[A[i]["principles"][p] for i in ids]; b=[R[i]["principles"][p] for i in ids]
        kq.append(k(a,b,"quadratic")); ku.append(k(a,b)); a2.append(float(np.mean([(x==2)==(y==2) for x,y in zip(a,b)]))); k2.append(k([int(x==2) for x in a],[int(y==2) for y in b]))
        rows.append(dict(comparison=name,n=len(ids),field="principle: "+PRL[p],kappa_quadratic=kq[-1],kappa_unweighted=ku[-1],agreement_level2=a2[-1],kappa_level2=k2[-1]))
    rows.append(dict(comparison=name,n=len(ids),field="principles (median over 20)",kappa_quadratic=float(np.nanmedian(kq)),kappa_unweighted=float(np.nanmedian(ku)),agreement_level2=float(np.nanmedian(a2)),kappa_level2=float(np.nanmedian(k2))))
d=pd.DataFrame(rows); d.to_csv(B+"data/reliability_variants.csv",index=False)
write_table("S09b_reliability_variants",d[d.field.str.contains("median|relevance")].round(3),"Reliability variants: quadratic-weighted and unweighted kappa for ordinal fields, and agreement/kappa on the level-2 (treated in depth) threshold for principles, per comparison (round-1 and round-2 samples)")
print(d[d.field.str.contains("median|relevance")].round(3).to_string())
