#!/usr/bin/env python3
"""Stage 2 analysis infrastructure: loads the master table, defines analysis sets, and provides figure/table helpers.
Run with --smoke to produce the two landscape figures as a pipeline test."""
import sys, os, json, argparse, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v4/scripts"); import figstyle as fs
import matplotlib.pyplot as plt
B="/home/user/embodied-ai-governance-v4/"; FD=B+"figures/data/"
def load():
    m=pd.read_csv(B+"data/master_table.csv"); a=m[m.annotated].copy()
    a["embodied_set"]=(a.relevance_to_embodied_ai_governance>=2)|(a.embodied_categories.fillna("")!="")
    a["embodied_set"]&=~a.ai_scope.isin(["not_ai"])
    a["general_set"]=~a.embodied_set & a.ai_scope.isin(["general_ai_only","general_ai_with_embodied_provisions"])
    a["usable"]=a.text_usable & (a.page_quality!="error_or_blocked_page") & (a.doc_class!="unusable")
    return a
DCL={"governance_instrument_binding":"Binding instrument","governance_instrument_soft":"Soft-law instrument","governance_proposal_or_draft":"Proposal or draft","government_report_or_parliamentary":"Gov. report / parliamentary","research_output":"Research output","grey_literature":"Grey literature","communication_or_news":"Communication / news","unusable":"Unusable capture"}
DCO=list(DCL)
def wilson(k,n,z=1.96):
    if n==0: return (np.nan,np.nan)
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return (c-h,c+h)
def fig_composition(a,theme="light"):
    t=fs.setup(theme); sets=[("Embodied-AI set",a[a.embodied_set&a.usable]),("General-AI set",a[a.general_set&a.usable])]
    fig,ax=plt.subplots(figsize=(7.2,2.6)); rows=[]
    for i,(name,g) in enumerate(sets):
        left=0; n=len(g)
        for j,k in enumerate(DCO):
            v=(g.doc_class==k).mean()*100 if n else 0; ax.barh(name,v,left=left,color=t["cat"][j] if j<7 else t["muted"],height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=7: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7.5,color="#ffffff" if j not in (3,) else "#0b0b0b")
            rows.append(dict(set=name,doc_class=k,share_pct=round(v,1),n=int((g.doc_class==k).sum()),n_total=n)); left+=v
    ax.set_xlim(0,100); ax.set_xlabel("Share of documents (%)"); ax.invert_yaxis(); ax.yaxis.grid(False)
    ax.set_title(f"Document class composition (embodied n={len(sets[0][1])}, general n={len(sets[1][1])})",loc="left")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j] if j<7 else t["muted"]) for j in range(len(DCO))],[DCL[k] for k in DCO],ncol=4,loc="upper center",bbox_to_anchor=(0.5,-0.35),frameon=False)
    fs.save(fig,"F01_composition_by_set",theme); pd.DataFrame(rows).to_csv(FD+"F01_composition_by_set.csv",index=False)
def fig_timeline(a,theme="light"):
    t=fs.setup(theme); u=a[a.usable&a.year_final.notna()&(a.year_final>=2010)&(a.year_final<=2026)].copy(); u["year"]=u.year_final.astype(int)
    yrs=list(range(2010,2027)); emb=[int((u[u.year==y].embodied_set).sum()) for y in yrs]; gen=[int((~u[u.year==y].embodied_set).sum()) for y in yrs]
    fig,ax=plt.subplots(figsize=(7.2,3)); ax.bar(yrs,emb,color=t["cat"][0],width=0.72,label="Embodied-AI set"); ax.bar(yrs,gen,bottom=emb,color=t["cat"][1],width=0.72,label="Other AI governance",edgecolor=t["surface"],linewidth=1)
    ax.set_xticks(yrs); ax.set_xticklabels([str(y) if y%2==0 else "" for y in yrs]); ax.yaxis.grid(True); ax.xaxis.grid(False); ax.set_ylabel("Documents"); ax.legend(loc="upper left")
    ax.set_title(f"Documents per publication year, 2010 to 2026 (n={len(u)})",loc="left"); fs.save(fig,"F02_timeline",theme)
    pd.DataFrame({"year":yrs,"embodied":emb,"other":gen}).to_csv(FD+"F02_timeline.csv",index=False)
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--smoke",action="store_true"); args=ap.parse_args()
    a=load(); print("annotated",len(a),"embodied set",int(a.embodied_set.sum()),"general set",int(a.general_set.sum()),"usable",int(a.usable.sum()))
    if args.smoke:
        for th in ("light","dark"): fig_composition(a,th); fig_timeline(a,th)
        print("smoke figures written")
