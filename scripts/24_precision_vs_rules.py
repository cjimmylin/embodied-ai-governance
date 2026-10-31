#!/usr/bin/env python3
"""v4: compare the rule-based counting unit (principal instrument, robot-relevant, substantive capture) with the independent precision audit
of 100 randomly sampled v3 binding embodied instruments, and derive precision-corrected counts with Wilson intervals. Writes T62 and results keys."""
import sys, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v4/scripts"); from analysis_common import *
a=load(); m=a.set_index("doc_id")
s=pd.read_csv(B+"review/v3_reviews/precision_audit_sample.csv",dtype=str,keep_default_na=False)
yes=lambda col: s[col].str.strip().str.lower().str.startswith("y")
s["audit_joint"]=yes("a")&yes("b")&yes("c"); s["audit_autonomy"]=s.audit_joint&yes("d"); s["audit_distinct"]=yes("a"); s["audit_substantive"]=yes("c")
s["rule_principal"]=s.doc_id.map(lambda d: bool(m.loc[d,"instrument"]) if d in m.index else False)
s["rule_robot"]=s.doc_id.map(lambda d: bool(m.loc[d,"instrument"]) and bool(m.loc[d,"embodied_set"]) and int(m.loc[d,"relevance_to_embodied_ai_governance"])>=2 if d in m.index else False)
s["rule_autonomy"]=s.rule_robot&s.doc_id.map(lambda d: bool(m.loc[d,"autonomy_terms"]) if d in m.index else False)
rows=[]
def wl(k,n): lo,hi=wilson(k,n); return f"{100*k/n:.0f}% ({100*lo:.0f} to {100*hi:.0f})"
for name,aud,rule in [("distinct instrument (audit a)","audit_distinct","rule_principal"),("distinct, binding and embodied-substantive (audit a+b+c)","audit_joint","rule_robot"),("a+b+c and autonomy/AI provision (audit a+b+c+d)","audit_autonomy","rule_autonomy")]:
    A=s[aud].astype(bool); Rr=s[rule].astype(bool); n=len(s)
    rows.append(dict(criterion=name,audit_share=wl(int(A.sum()),n),rule_share=wl(int(Rr.sum()),n),agreement=round(float((A==Rr).mean()),2),kappa=round(float(cohen_kappa(A,Rr)),2) if 'cohen_kappa' in globals() else np.nan,rule_passes_audit_fails=int((Rr&~A).sum()),audit_passes_rule_fails=int((A&~Rr).sum())))
from sklearn.metrics import cohen_kappa_score
for r_,(aud,rule) in zip(rows,[("audit_distinct","rule_principal"),("audit_joint","rule_robot"),("audit_autonomy","rule_autonomy")]): r_["kappa"]=round(float(cohen_kappa_score(s[aud].astype(int),s[rule].astype(int))),2)
t62=pd.DataFrame(rows); write_table("T62_precision_audit_vs_rules",t62,"Independent precision audit of 100 randomly sampled v3 binding embodied instruments versus the v4 rule-based counting unit, on the same documents (Wilson 95% intervals)")
# precision-corrected estimates for the v3 population (299) and the v4 principal population
u=a[a.usable]; N3=299; pj=s.audit_joint.mean(); lo,hi=wilson(int(s.audit_joint.sum()),len(s))
R("precision_audit",{"n":len(s),"joint_share":float(pj),"joint_ci":[float(lo),float(hi)],"v3_binding_embodied":N3,"corrected_count":round(N3*pj),"corrected_ci":[round(N3*lo),round(N3*hi)],"rule_principal_binding_embodied":int((u.binding&u.instrument&u.embodied_set).sum()),"rule_principal_binding_robot":int((u.binding&u.instrument&u.embodied_set&(u.relevance_to_embodied_ai_governance>=2)).sum())})
print(t62.to_string()); print("corrected",round(N3*pj),round(N3*lo),round(N3*hi))
import json
try:
    res=json.load(open(B+"data/results.json")); res.update({k:v for k,v in RESULTS.items()}); json.dump(res,open(B+"data/results.json","w"),indent=1,ensure_ascii=False,default=str)
except Exception as e: print("results merge skipped",e)
