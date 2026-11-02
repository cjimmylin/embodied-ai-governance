"""v2 additions: genre-stratified and covariate-adjusted comparisons, bootstrap CIs for the governance-gap index and
region distances, within-embodied term trends, k-means stability, coverage audit against reference instruments,
excerpt coverage statistics. Figures F38-F43, tables T20-T25. Merges into data/results.json."""
import sys, json, re, os, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts")
from analysis_common import *
import statsmodels.api as sm
from scipy.spatial.distance import cosine
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
if os.path.exists(B+"data/results.json"): RESULTS.update(json.load(open(B+"data/results.json")))
rng=np.random.default_rng(42)
m=load(); u=m[m.usable].copy(); emb=u[u.embodied_set]; gen=u[u.general_set]
MECH=sorted(x for x in set(labels_of(u.governance_mechanisms)) if x not in ("none","other",""))
PREG=[r for r in REGIONS if (emb.study_region==r).sum()>=30]   # v4: data-driven, identical to F31
def both(fn):
    for th in ["light","dark"]: fn(th)

# ---------- T20/F38: adjusted logistic models, embodied vs general, controlling for class, region, year
M=u[u.setname.isin(["Embodied-AI set","General-AI set"])&u.year.between(2010,2026)].copy()
M["emb"]=M.embodied_set.astype(float); M["yc"]=(M.year-2022).astype(float); M["r2"]=M.round2.astype(float)   # v4: collection round as a covariate
Xb=pd.get_dummies(M[["doc_class","study_region"]],drop_first=False).astype(float)
Xb=Xb.drop(columns=[c for c in Xb.columns if c.endswith("research_output") or c.endswith("Europe")],errors="ignore")
X=sm.add_constant(pd.concat([M[["emb","yc","r2"]],Xb],axis=1))
rows=[]
for p in PR:
    y=(M["pr_"+p]>=1).astype(int)
    crude=np.log(((y[M.emb==1].mean()/(1-y[M.emb==1].mean()))/(y[M.emb==0].mean()/(1-y[M.emb==0].mean()))))
    try:
        fit=sm.Logit(y,X).fit(disp=0,maxiter=300); ci=fit.conf_int().loc["emb"]
        ev_e,ev_g=int(y[M.emb==1].sum()),int(y[M.emb==0].sum()); sparse=min(ev_e,ev_g,int((M.emb==1).sum())-ev_e,int((M.emb==0).sum())-ev_g)<5   # v4: near-separation flag
        rows.append(dict(item="principle: "+PRL[p],group="core" if p in PR_CORE else "embodied-specific",n=len(M),events=int(y.sum()),events_embodied=ev_e,events_general=ev_g,sparse_cell=sparse,crude_or=round(float(np.exp(crude)),2),adjusted_or=round(float(np.exp(fit.params["emb"])),2),ci_low=round(float(np.exp(ci[0])),2),ci_high=round(float(np.exp(ci[1])),2),p=float(fit.pvalues["emb"])))
    except Exception as e:
        rows.append(dict(item="principle: "+PRL[p],group="core" if p in PR_CORE else "embodied-specific",n=len(M),events=int(y.sum()),crude_or=round(float(np.exp(crude)),2),adjusted_or=None,ci_low=None,ci_high=None,p=None))
for mech in MECH:
    y=has(M.governance_mechanisms,mech).astype(int)
    if y.sum()<15: continue
    pe,pg=y[M.emb==1].mean(),y[M.emb==0].mean()
    crude=np.log((pe/(1-pe))/(pg/(1-pg))) if 0<pe<1 and 0<pg<1 else np.nan
    try:
        fit=sm.Logit(y,X).fit(disp=0,maxiter=300); ci=fit.conf_int().loc["emb"]
        rows.append(dict(item="mechanism: "+nice(mech),group="mechanism",n=len(M),events=int(y.sum()),crude_or=round(float(np.exp(crude)),2) if not np.isnan(crude) else None,adjusted_or=round(float(np.exp(fit.params["emb"])),2),ci_low=round(float(np.exp(ci[0])),2),ci_high=round(float(np.exp(ci[1])),2),p=float(fit.pvalues["emb"])))
    except Exception: pass
t20=pd.DataFrame(rows); t20["p_holm"]=holm(t20.p.fillna(1)); t20["significant_holm_05"]=t20.p_holm<0.05
write_table("T20_adjusted_models",t20.round(4),"Embodied-AI set vs general-AI set: crude and covariate-adjusted odds ratios (logistic regression adjusting for document class, jurisdiction region, collection round and publication year; usable documents with a known year)")

# ---------- T20b (v4): the embodied-vs-general principle contrast within each collection round and within instruments per round
rows=[]
for stratum,sel in [("Round 1, all usable documents",~u.round2),("Round 2, all usable documents",u.round2),("Round 1, governance instruments",(~u.round2)&u.instrument),("Round 2, governance instruments",u.round2&u.instrument)]:
    E=u[sel&u.embodied_set]; G=u[sel&u.general_set]; pv=[]; tmp=[]
    for p in PR:
        e=(E["pr_"+p]>=1); g=(G["pr_"+p]>=1); tab=np.array([[e.sum(),(~e).sum()],[g.sum(),(~g).sum()]]); test,pval=chi2_or_fisher(tab); pv.append(pval)
        tmp.append(dict(stratum=stratum,principle=PRL[p],group="core" if p in PR_CORE else "embodied-specific",n_embodied=len(E),n_general=len(G),embodied_pct=round(100*e.mean(),1) if len(E) else np.nan,general_pct=round(100*g.mean(),1) if len(G) else np.nan,diff_pp=round(100*(e.mean()-g.mean()),1) if len(E) and len(G) else np.nan,test=test,p=pval))
    ph=holm([x if x==x else 1.0 for x in pv])
    for r_,h in zip(tmp,ph): r_["p_holm"]=float(h); r_["significant_holm_05"]=bool(h<0.05); rows.append(r_)
t20b=pd.DataFrame(rows); write_table("T20b_within_round",t20b.round(4),"Principle presence (level 1 or 2), embodied-AI set vs general-AI set, within each collection round and within governance instruments of each round (Holm within stratum): shows which contrasts depend on the round-2 additions")
R("within_round_principles",t20b.to_dict("records"))
R("adjusted_models",t20.to_dict("records"))
def F38(th):
    t=fs.setup(th); d=t20[t20.adjusted_or.notna()].copy(); d["ord"]=d.group.map({"embodied-specific":0,"core":1,"mechanism":2}); d=d.sort_values(["ord","adjusted_or"],ascending=[True,False])
    fig,ax=plt.subplots(figsize=(7.4,8.2)); y=np.arange(len(d))
    cols={"embodied-specific":t["cat"][1],"core":t["cat"][0],"mechanism":t["cat"][2]}
    ax.axvline(1,color=t["ink"],lw=0.8)
    for yi,(_,r) in enumerate(d.iterrows()):
        c=cols[r.group]; ax.plot([r.ci_low,r.ci_high],[yi,yi],color=c,lw=1.4,zorder=2); ax.scatter([r.adjusted_or],[yi],color=c,s=22,zorder=3)
        if r.crude_or: ax.scatter([r.crude_or],[yi],facecolors="none",edgecolors=t["muted"],s=22,zorder=2,lw=0.8)
    ax.set_yticks(y); ax.set_yticklabels([x.split(": ",1)[1]+(" *" if s else "") for x,s in zip(d.item,d.significant_holm_05)],fontsize=7.2); ax.invert_yaxis(); ax.set_xscale("log")
    ax.set_xticks([0.05,0.1,0.25,0.5,1,2,4,10,40,160]); ax.set_xticklabels(["0.05","0.1","0.25","0.5","1","2","4","10","40","160"]); ax.yaxis.grid(False)
    ax.set_xlabel("Odds ratio, embodied vs general (log scale; filled = adjusted for class, region, year; hollow = crude)")
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([],[],color=cols["embodied-specific"],marker="o",lw=1.4,label="Embodied-specific principle"),Line2D([],[],color=cols["core"],marker="o",lw=1.4,label="Core principle"),Line2D([],[],color=cols["mechanism"],marker="o",lw=1.4,label="Mechanism"),Line2D([],[],color=t["muted"],marker="o",markerfacecolor="none",lw=0,label="Crude odds ratio")],loc="lower right",fontsize=7)
    sig=d[d.significant_holm_05&(d.adjusted_or>1)].sort_values("adjusted_or",ascending=False); tops=[x.split(": ",1)[1] for x in sig.item.head(3)]
    ax.set_title(f"After adjusting for genre, region and year, embodied documents still favour {', '.join(t_.lower() for t_ in tops)}\n({int(d.significant_holm_05.sum())} of {len(d)} items Holm-significant; * marks them)",loc="left",fontsize=9.5)
    fs.save(fig,"F38_adjusted_odds",th); d.to_csv(FD+"F38_adjusted_odds.csv",index=False)
both(F38)

# ---------- T21/F39: genre-stratified comparison (within research outputs; within governance instruments)
rows=[]
for stratum,sel in [("Research outputs",u.doc_class=="research_output"),("Governance instruments",u.instrument&u.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])),("Government reports",u.doc_class=="government_report_or_parliamentary"),("News and communications",u.doc_class=="communication_or_news")]:
    S=u[sel]; E=S[S.embodied_set]; G=S[S.general_set]
    for p in PR:
        ke,kg=int((E["pr_"+p]>=1).sum()),int((G["pr_"+p]>=1).sum())
        tab=[[ke,len(E)-ke],[kg,len(G)-kg]]; test,pv=chi2_or_fisher(tab) if len(E) and len(G) else ("",np.nan)
        rows.append(dict(stratum=stratum,item=PRL[p],kind="principle",n_embodied=len(E),n_general=len(G),embodied_pct=round(100*ke/len(E),1) if len(E) else np.nan,general_pct=round(100*kg/len(G),1) if len(G) else np.nan,diff_pp=round(100*(ke/len(E)-kg/len(G)),1) if len(E) and len(G) else np.nan,test=test,p=pv))
    for mech in MECH:
        ke,kg=int(has(E.governance_mechanisms,mech).sum()),int(has(G.governance_mechanisms,mech).sum())
        if ke+kg<8: continue
        tab=[[ke,len(E)-ke],[kg,len(G)-kg]]; test,pv=chi2_or_fisher(tab) if len(E) and len(G) else ("",np.nan)
        rows.append(dict(stratum=stratum,item=nice(mech),kind="mechanism",n_embodied=len(E),n_general=len(G),embodied_pct=round(100*ke/len(E),1) if len(E) else np.nan,general_pct=round(100*kg/len(G),1) if len(G) else np.nan,diff_pp=round(100*(ke/len(E)-kg/len(G)),1) if len(E) and len(G) else np.nan,test=test,p=pv))
t21=pd.DataFrame(rows)
for s_ in t21.stratum.unique():
    idx=t21.stratum==s_; t21.loc[idx,"p_holm"]=holm(t21.loc[idx,"p"].fillna(1))
write_table("T21_stratified_by_genre",t21.round(4),"Embodied vs general comparison within each document genre (Holm correction within stratum)")
R("stratified_by_genre",t21.to_dict("records"))
def F39(th):
    t=fs.setup(th); fig,axes=plt.subplots(1,2,figsize=(9.6,6.2),sharey=True)
    for ax,stratum in zip(axes,["Research outputs","Governance instruments"]):
        d=t21[(t21.stratum==stratum)&(t21.kind=="principle")].set_index("item").loc[[PRL[p] for p in PR]].reset_index()
        y=np.arange(len(d))
        for yi,(e,g) in enumerate(zip(d.embodied_pct,d.general_pct)): ax.plot([g,e],[yi,yi],color=t["grid"],lw=2,zorder=1)
        ax.scatter(d.general_pct,y,color=t["cat"][1],s=30,zorder=2,label=f"General-AI (n={int(d.n_general.iloc[0])})"); ax.scatter(d.embodied_pct,y,color=t["cat"][0],s=30,zorder=3,label=f"Embodied-AI (n={int(d.n_embodied.iloc[0])})")
        ax.set_yticks(y); ax.set_yticklabels([x+(" *" if ph<0.05 else "") for x,ph in zip(d.item,d.p_holm)],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlim(0,100)
        ax.axhline(13.5,color=t["ink"],lw=0.8); ax.set_xlabel("Share of documents mentioning the principle (%)"); ax.set_title(f"Within {stratum.lower()}",loc="left",fontsize=9); ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.08),ncol=2,frameon=False,fontsize=7)
    axes[0].set_ylim(len(PR)-0.5,-0.5)   # one inversion on the shared axis (core principles above the line)
    gi_=t21[(t21.stratum=="Governance instruments")&(t21.kind=="principle")].assign(ad=lambda x:x.diff_pp.abs()).sort_values("ad",ascending=False)
    fig.suptitle(f"Within instruments the largest embodied-vs-general gaps are {', '.join(x.lower() for x in gi_.item.head(3))}; within research papers most core principles are alike\n(* = Holm-significant within stratum; core principles above the line)",x=0.02,ha="left",fontsize=9.5,fontweight="semibold")
    fs.save(fig,"F39_stratified_principles",th); t21[t21.kind=="principle"].to_csv(FD+"F39_stratified_principles.csv",index=False)
both(F39)

# ---------- T22/F40: bootstrap CIs for the governance-gap index
rs=emb[emb.doc_class=="research_output"]; gi=emb[emb.instrument]
Rm=np.array([[c in s.split("; ") for c in EMB] for s in rs.embodied_categories]); Gm=np.array([[c in s.split("; ") for c in EMB] for s in gi.embodied_categories])
B_=2000; boots=np.empty((B_,len(EMB)))
for b in range(B_):
    ri=rng.integers(0,len(rs),len(rs)); gi_=rng.integers(0,len(gi),len(gi))
    boots[b]=100*(Rm[ri].mean(0)-Gm[gi_].mean(0))
lo,hi=np.percentile(boots,[2.5,97.5],axis=0); point=100*(Rm.mean(0)-Gm.mean(0))
t22=pd.DataFrame(dict(category=EMB,level1=[L1[c] for c in EMB],research_pct=np.round(100*Rm.mean(0),1),n_research=Rm.sum(0),instrument_pct=np.round(100*Gm.mean(0),1),n_instruments=Gm.sum(0),gap_index=np.round(point,1),ci_low=np.round(lo,1),ci_high=np.round(hi,1)))
t22["ci_excludes_zero"]=(t22.ci_low>0)|(t22.ci_high<0); t22=t22.sort_values("gap_index",ascending=False)
write_table("T22_governance_gap_bootstrap",t22,f"Governance-gap index with 95% bootstrap confidence intervals (2,000 resamples of research outputs n={len(rs)} and governance instruments n={len(gi)} separately)")
R("governance_gap_bootstrap",t22.to_dict("records"))
def F40(th):
    t=fs.setup(th); d=t22[(t22.n_research+t22.n_instruments)>=8]; y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.4,5.2))
    cols=[t["cat"][0] if g>0 else t["cat"][1] for g in d.gap_index]
    ax.axvline(0,color=t["ink"],lw=0.8)
    for yi,(_,r) in enumerate(d.iterrows()): ax.plot([r.ci_low,r.ci_high],[yi,yi],color=cols[yi],lw=1.6,zorder=2)
    ax.scatter(d.gap_index,y,color=cols,s=30,zorder=3)
    ax.set_yticks(y); ax.set_yticklabels([nice(c)+(" *" if ex else "") for c,ex in zip(d.category,d.ci_excludes_zero)],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False)
    ax.set_xlabel("Research share minus instrument share (percentage points, 95% bootstrap CI)")
    ax.text(0.98,0.02,"blue: more studied than governed\norange: more governed than studied\n* = interval excludes zero",transform=ax.transAxes,ha="right",va="bottom",fontsize=7,color=t["muted"])
    up=d[d.ci_excludes_zero&(d.gap_index>0)].sort_values("gap_index",ascending=False); dn=d[d.ci_excludes_zero&(d.gap_index<0)].sort_values("gap_index")
    ax.set_title(f"More studied than governed (interval excludes zero): {', '.join(nice(c).lower() for c in up.category.head(3))}{' and '+str(len(up)-3)+' more' if len(up)>3 else ''};\nmore governed than studied: {', '.join(nice(c).lower() for c in dn.category.head(3))}{' and '+str(len(dn)-3)+' more' if len(dn)>3 else ''} (n={len(rs)} papers, {len(gi)} principal instruments)",loc="left",fontsize=9)
    fs.save(fig,"F40_gap_bootstrap",th); d.to_csv(FD+"F40_gap_bootstrap.csv",index=False)
both(F40)

# ---------- T23: region distance bootstrap and cluster stability
def profile(df):
    v=[(df["pr_"+p]>=1).mean() for p in PR]
    tops=sorted(set(labels_of(u.governance_topics))); v+=[has(df.governance_topics,x).mean() for x in tops]
    v+=[has(df.governance_mechanisms,x).mean() for x in MECH]
    return np.array(v)
E_by={r:emb[emb.study_region==r] for r in PREG}
P0={r:profile(E_by[r]) for r in PREG}
D0=np.array([[cosine(P0[a],P0[b]) if a!=b else 0 for b in PREG] for a in PREG])
Bd=300; Dstack=np.empty((Bd,len(PREG),len(PREG)))
for b in range(Bd):
    P={r:profile(E_by[r].iloc[rng.integers(0,len(E_by[r]),len(E_by[r]))]) for r in PREG}
    Dstack[b]=[[cosine(P[a],P[c]) if a!=c else 0 for c in PREG] for a in PREG]
lo=np.percentile(Dstack,2.5,axis=0); hi=np.percentile(Dstack,97.5,axis=0)
rows=[]
for i,a in enumerate(PREG):
    for j,c in enumerate(PREG):
        if j<=i: continue
        rows.append(dict(region_a=a,region_b=c,n_a=len(E_by[a]),n_b=len(E_by[c]),distance=round(D0[i,j],3),ci_low=round(lo[i,j],3),ci_high=round(hi[i,j],3)))
t23=pd.DataFrame(rows).sort_values("distance")
# nearest-neighbour stability: how often is each region's nearest neighbour the same as in the point estimate
nn0={a:PREG[int(np.argsort(D0[i])[1])] for i,a in enumerate(PREG)}
stab={a:float(np.mean([PREG[int(np.argsort(Dstack[b,i])[1])]==nn0[a] for b in range(Bd)])) for i,a in enumerate(PREG)}
t23b=pd.DataFrame([dict(region=a,n=len(E_by[a]),nearest_region=nn0[a],stability=round(stab[a],2)) for a in PREG])
write_table("T23_region_distance_bootstrap",t23,"Pairwise cosine distances between regional embodied-AI profiles with 95% bootstrap intervals (300 resamples within region)")
write_table("T23b_nearest_region_stability",t23b,"Nearest-neighbour region in the point estimate and the share of bootstrap resamples in which it is unchanged")
R("region_distance_bootstrap",{"pairs":t23.to_dict("records"),"stability":t23b.to_dict("records")})

# ---------- T24: k-means stability across k
G=u[u.gov]; Xm=np.array([[mech in s.split("; ") for mech in MECH] for s in G.governance_mechanisms]).astype(float)
Xm=Xm[Xm.sum(1)>0]
rows=[]
for k in range(2,7):
    km=KMeans(n_clusters=k,n_init=10,random_state=0).fit(Xm); s=silhouette_score(Xm,km.labels_)
    # co-assignment stability on 50 bootstrap resamples
    agree=[]
    for b in range(50):
        idx=rng.integers(0,len(Xm),len(Xm)); km2=KMeans(n_clusters=k,n_init=5,random_state=b).fit(Xm[idx]); lab2=km2.predict(Xm)
        from sklearn.metrics import adjusted_rand_score
        agree.append(adjusted_rand_score(km.labels_,lab2))
    rows.append(dict(k=k,silhouette=round(float(s),3),mean_adjusted_rand_vs_bootstrap=round(float(np.mean(agree)),3),smallest_cluster=int(np.bincount(km.labels_).min())))
t24=pd.DataFrame(rows); write_table("T24_kmeans_stability",t24,f"K-means on mechanism vectors of governance documents (n={len(Xm)}): silhouette and bootstrap stability by k (exploratory)")
R("kmeans_stability",t24.to_dict("records"))

# ---------- T25/F41: coverage audit against reference instruments (captured as document? cited in text?)
ref=pd.read_csv(B+"data/reference_instruments.csv")
titles=u.title_en.fillna("")+" "+u.collection_title.fillna("")
texts={}
for _,r in u.iterrows():
    tp=r.get("text_path") if "text_path" in u.columns else None
reg=pd.read_csv(B+"data/registry.csv")[["doc_id","text_path"]].set_index("doc_id")
def fulltext(doc_id):
    p=reg.text_path.get(doc_id)
    if isinstance(p,str) and os.path.exists(p):
        try: return open(p,encoding="utf8",errors="replace").read()
        except Exception: return ""
    return ""
rows=[]
FT={d:fulltext(d) for d in u.doc_id}
for _,r in ref.iterrows():
    pat=re.compile(r.pattern,re.I)
    cap=[d for d,ti,gv in zip(u.doc_id,titles,(u.instrument&u.content_capture)) if pat.search(ti) and gv]   # v4: captured means a principal instrument with a content-analysed capture
    cited=[d for d,txt in FT.items() if txt and pat.search(txt)]
    rows.append(dict(instrument=r.instrument,jurisdiction=r.jurisdiction,year=r.year,nature=r.nature,status=r.status,captured_as_document=len(cap)>0,n_title_matches=len(cap),n_documents_citing=len(cited),pct_citing=round(100*len(cited)/len(u),1)))
t25=pd.DataFrame(rows); write_table("T25_coverage_audit",t25,"Coverage audit: reference list of binding instruments and standards relevant to embodied AI, whether each is captured in the collection as a principal instrument with a content-analysed capture (title match) and how many usable documents cite it (full-text regex)")
R("coverage_audit",t25.to_dict("records"))
def F41(th):
    t=fs.setup(th); d=t25.sort_values("n_documents_citing",ascending=False); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.6,8.4))
    cols=[t["cat"][0] if c else t["cat"][1] for c in d.captured_as_document]
    ax.barh(y,d.n_documents_citing,color=cols,height=0.72)
    ax.set_yticks(y); ax.set_yticklabels([x[:60] for x in d.instrument],fontsize=7); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Usable documents citing the instrument (full-text match)")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=t["cat"][0],label="Captured in the collection"),Patch(color=t["cat"][1],label="Not captured (cited only)")],loc="lower right",fontsize=7)
    ax.set_title(f"Coverage audit: {int(d.captured_as_document.sum())} of {len(d)} reference instruments are captured as documents;\nthe rest are cited in the corpus but not captured",loc="left",fontsize=9.5)
    fs.save(fig,"F41_coverage_audit",th); d.to_csv(FD+"F41_coverage_audit.csv",index=False)
both(F41)

# ---------- F42: within-embodied-set category/term trends (composition-free)
def F42(th):
    t=fs.setup(th); E=emb[emb.year.between(2018,2026)]
    cats=["humanoid_general_purpose","social_companion_robots","care_assistive_robots","autonomous_road_vehicles","industrial_manipulators","mobile_industrial_logistics","surgical_medical_robots","military_autonomous_weapons","drones_uas"]
    fig,axes=plt.subplots(3,3,figsize=(9.6,7.2),sharex=True)
    for ax,c in zip(axes.flat,cats):
        yrs=list(range(2018,2027)); sh=[]; lo=[]; hi=[]
        for yv in yrs:
            d=E[E.year==yv]; k=int(has(d.embodied_categories,c).sum()); n=len(d); sh.append(100*k/n if n else np.nan); l,h=wilson(k,n); lo.append(100*l); hi.append(100*h)
        ax.fill_between(yrs,lo,hi,color=t["cat"][0],alpha=0.15,lw=0); ax.plot(yrs,sh,color=t["cat"][0],marker="o",ms=3,label="all embodied documents")
        E1=E[~E.round2]; sh1=[(100*has(E1[E1.year==yv].embodied_categories,c).mean() if (E1.year==yv).sum()>=10 else np.nan) for yv in yrs]
        ax.plot(yrs,sh1,color=t["cat"][1] if len(t["cat"])>1 else "#888888",ls="--",marker="s",ms=2.5,label="round-1 documents only")   # v5: round-1-only line (composition check)
        ax.set_title(nice(c),loc="left",fontsize=8); ax.set_ylim(0,60); ax.xaxis.grid(False); ax.set_xticks([2018,2020,2022,2024,2026]); ax.tick_params(labelsize=7)
    fig.supylabel("% of the year's embodied-AI documents (95% Wilson band)",fontsize=8)
    axes.flat[0].legend(fontsize=6.5,loc="upper left",frameon=False)
    ch=sorted(((c,has(E[E.year>=2025].embodied_categories,c).mean()-has(E[E.year<=2022].embodied_categories,c).mean()) for c in cats),key=lambda z:-z[1])
    fig.suptitle(f"Within the embodied set, {', '.join(nice(c).lower() for c,_ in ch[:2])} rise most after 2024 while {', '.join(nice(c).lower() for c,_ in ch[-2:])} recede",x=0.02,ha="left",fontsize=10,fontweight="semibold")
    fig.text(0.02,0.935,f"Embodied-AI documents per year: "+", ".join(f"{yv}: {int((E.year==yv).sum())}" for yv in range(2018,2027)),fontsize=7,color=t["muted"])
    fs.save(fig,"F42_category_trends_within_embodied",th)
both(F42)

# ---------- excerpt coverage statistics
tf=pd.read_csv(B+"data/text_features.csv")
if "file_rel" in tf.columns:
    reg2=pd.read_csv(B+"data/registry.csv")[["doc_id","file_rel"]]
    tf=tf.merge(reg2,on="file_rel",how="inner")
chars=u.text_chars.fillna(0)
seen=np.minimum(chars,14000+500); frac=np.where(chars>0,seen/np.maximum(chars,1),np.nan)
R("excerpt_coverage",{"n":int(len(u)),"median_chars":float(chars.median()),"share_fully_seen":float((chars<=14500).mean()),"median_fraction_seen":float(np.nanmedian(frac)),"share_seen_lt_25pct":float(np.nanmean(frac<0.25))})
dump_results(); print("done D")

# ======================= v2 additions after review (part 2) =======================
# ---------- T28: genre- and region-adjusted topic change (2025-26 vs 2020-24) in the embodied set
TOP=sorted(set(labels_of(emb.governance_topics)))
E2=emb[emb.year.between(2020,2026)].copy(); E2["new"]=(E2.year>=2025).astype(float)
Xb=pd.get_dummies(E2[["doc_class","study_region"]],drop_first=False).astype(float)
Xb=Xb.drop(columns=[c for c in Xb.columns if c.endswith("research_output") or c.endswith("Europe")],errors="ignore")
Xb["r2"]=E2.round2.astype(float).values   # v5: collection round as a covariate
X2=sm.add_constant(pd.concat([E2[["new"]],Xb],axis=1))
rows=[]
for tp in TOP:
    y=has(E2.governance_topics,tp).astype(int)
    if y.sum()<20: continue
    p_old=y[E2.new==0].mean(); p_new=y[E2.new==1].mean()
    try:
        fit=sm.Logit(y,X2).fit(disp=0,maxiter=300); ci=fit.conf_int().loc["new"]
        # research-only crude change
        Rr=E2[E2.doc_class=="research_output"]; yr=has(Rr.governance_topics,tp).astype(int)
        rows.append(dict(topic=lab(tp),pct_2020_2024=round(100*p_old,1),pct_2025_2026=round(100*p_new,1),change_pp=round(100*(p_new-p_old),1),
                         research_only_2020_2024=round(100*yr[Rr.new==0].mean(),1),research_only_2025_2026=round(100*yr[Rr.new==1].mean(),1),
                         adjusted_or=round(float(np.exp(fit.params["new"])),2),ci_low=round(float(np.exp(ci[0])),2),ci_high=round(float(np.exp(ci[1])),2),p=float(fit.pvalues["new"])))
    except Exception: pass
t28=pd.DataFrame(rows); t28["p_holm"]=holm(t28.p.fillna(1)); t28=t28.sort_values("adjusted_or",ascending=False)
write_table("T28_topic_change_adjusted",t28.round(4),f"Topic change 2025-26 vs 2020-24 in the embodied set: crude shares, research-only shares, and odds ratios adjusted for document class, region and collection round (n={len(E2)})")
R("topic_change_adjusted",t28.to_dict("records"))

# ---------- T29: regional divergence on a common population with bias-corrected V and bootstrap CIs (embodied documents, 6 regions)
Ep=emb[emb.study_region.isin(PREG)]
rows=[]
# v4: the same divergence statistics on research outputs only and on principal instruments only, so that genre mix cannot masquerade as regional difference
for _pop,_sel in [("research outputs",Ep.doc_class=="research_output"),("principal instruments",Ep.instrument)]:
    _E=Ep[_sel]; _rows=[]
    _regs=[r for r in PREG if (_E.study_region==r).sum()>=20]   # v4: regions with at least 20 documents of this genre (not the whole item dropped when one region is thin)
    if len(_regs)<3: continue
    _E=_E[_E.study_region.isin(_regs)]
    for p in PR:
        tab=pd.crosstab(_E.study_region,_E["pr_"+p]>=1).reindex(index=_regs,fill_value=0)
        if tab.shape[1]<2: continue
        test,pv=chi2_or_fisher(tab.values); _rows.append(dict(population=_pop,item="principle:"+p,label=PRL[p],n=len(_E),cramers_v=round(cramers_v_bc(tab.values),3),p=pv,min_region_pct=round(tab[True].div(tab.sum(1)).min()*100,1),max_region_pct=round(tab[True].div(tab.sum(1)).max()*100,1)))
    for mm in MECH:
        hv=has(_E.governance_mechanisms,mm); tab=pd.crosstab(_E.study_region,hv).reindex(index=_regs,fill_value=0)
        if tab.shape[1]<2 or hv.sum()<15: continue
        test,pv=chi2_or_fisher(tab.values); _rows.append(dict(population=_pop,item="mechanism:"+mm,label=nice(mm),n=len(_E),cramers_v=round(cramers_v_bc(tab.values),3),p=pv,min_region_pct=round(tab[True].div(tab.sum(1)).min()*100,1),max_region_pct=round(tab[True].div(tab.sum(1)).max()*100,1)))
    if _rows:
        _t=pd.DataFrame(_rows); _t["p_holm"]=holm(_t.p.fillna(1)); _t["significant_holm_05"]=_t.p_holm<0.05
        _t["regions"]=", ".join(f"{r} ({int((_E.study_region==r).sum())})" for r in _regs)
        write_table("T29b_regional_divergence_within_genre_"+_pop.split()[0],_t.round(4),f"Regional divergence within one genre ({_pop}, n={len(_E)}; regions with at least 20 documents of that genre: {', '.join(_regs)}): bias-corrected Cramer's V, Holm correction")
        R("regional_divergence_"+_pop.split()[0],_t.to_dict("records"))
for p in PR:
    v,lo_,hi_=v_bootstrap(Ep.study_region.values,(Ep["pr_"+p]>=1).values,B=300)
    tab=[[int(((Ep.study_region==g)&(Ep["pr_"+p]>=1)).sum()),int(((Ep.study_region==g)&(Ep["pr_"+p]<1)).sum())] for g in PREG]
    test,pv=chi2_or_fisher(tab); rows.append(dict(item="principle: "+PRL[p],population="embodied documents, 6 regions",n=len(Ep),v_bias_corrected=round(v,3),ci_low=round(lo_,3),ci_high=round(hi_,3),test=test,p=pv))
for mech in MECH:
    f=has(Ep.governance_mechanisms,mech).values
    if f.sum()<15: continue
    v,lo_,hi_=v_bootstrap(Ep.study_region.values,f,B=300)
    tab=[[int(((Ep.study_region==g).values&f).sum()),int(((Ep.study_region==g).values&~f).sum())] for g in PREG]
    test,pv=chi2_or_fisher(tab); rows.append(dict(item="mechanism: "+lab(mech),population="embodied documents, 6 regions",n=len(Ep),v_bias_corrected=round(v,3),ci_low=round(lo_,3),ci_high=round(hi_,3),test=test,p=pv))
t29=pd.DataFrame(rows); t29["p_holm"]=holm(t29.p.fillna(1)); t29=t29.sort_values("v_bias_corrected",ascending=False)
write_table("T29_regional_divergence_common",t29.round(4),"Regional divergence of principles and mechanisms on the same population (embodied documents in six regions): bias-corrected Cramer's V with bootstrap 95% CIs, Monte-Carlo chi-square where cells are sparse, Holm correction")
R("regional_divergence_common",t29.to_dict("records"))

# ---------- T30: trend-model sensitivities (without 2026; stated dates only; collapsed regions)
def trend_fit(df,outcome_fn,label,note,round_cov=False):
    df=df.copy(); df["yc"]=df.year-2022
    reg3=df.study_region.map(lambda r:"Europe" if r=="Europe" else ("Asia" if r=="Asia" else "Other")); cls3=df.doc_class.map(lambda c:"research" if c=="research_output" else ("instrument" if c in ["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"] else "other"))
    Xb=pd.get_dummies(pd.DataFrame({"reg":reg3,"cls":cls3}),drop_first=True).astype(float)
    if round_cov: Xb["r2"]=df.round2.astype(float).values
    X=sm.add_constant(pd.concat([df[["yc"]].astype(float),Xb],axis=1))
    y=outcome_fn(df).astype(int)
    try:
        fit=sm.Logit(y,X).fit(disp=0,maxiter=300); ci=fit.conf_int().loc["yc"]
        return dict(outcome=label,sensitivity=note,n=len(df),events=int(y.sum()),odds_ratio_per_year=round(float(np.exp(fit.params["yc"])),3),ci_low=round(float(np.exp(ci[0])),3),ci_high=round(float(np.exp(ci[1])),3),p=float(fit.pvalues["yc"]))
    except Exception as e: return dict(outcome=label,sensitivity=note,n=len(df),events=int(y.sum()),odds_ratio_per_year=None,ci_low=None,ci_high=None,p=None)
Mt=emb[emb.year.between(2015,2026)]
outs=[("mechanism: Risk-based tiering",lambda d:has(d.governance_mechanisms,"risk_based_tiering")),("mechanism: Conformity assessment & certification",lambda d:has(d.governance_mechanisms,"conformity_assessment_certification")),
      ("principle: Conformity assessment",lambda d:d.pr_conformity_assessment_certification>=1),("principle: Dual use & military",lambda d:d.pr_dual_use_military>=1),("principle: Physical safety",lambda d:d.pr_physical_safety>=1),("principle: Autonomy level & control",lambda d:d.pr_autonomy_level_control>=1),
      ("principle: Human-robot proximity",lambda d:d.pr_human_robot_proximity>=1),("principle: Liability for physical damage",lambda d:d.pr_liability_for_physical_damage>=1)]
rows=[]
for lbl,fn in outs:
    rows.append(trend_fit(Mt,fn,lbl,"all years, collapsed covariates"))
    rows.append(trend_fit(Mt[Mt.year<=2025],fn,lbl,"excluding partial year 2026"))
    rows.append(trend_fit(Mt[Mt.date_basis=="stated_in_document"],fn,lbl,"documents with a stated date only"))
    rows.append(trend_fit(Mt[~Mt.round2],fn,lbl,"round-1 documents only"))                      # v4
    rows.append(trend_fit(Mt,fn,lbl,"all years, collection round as covariate",round_cov=True))   # v4
t30=pd.DataFrame(rows); write_table("T30_trend_sensitivity",t30.round(4),"Trend models (odds ratio per year) under five specifications: collapsed region and class covariates; excluding 2026; stated-date documents only; round-1 documents only; collection round as a covariate")
R("trend_sensitivity",t30.to_dict("records"))

# ---------- T31: regional distance sensitivity: research outputs only, and a split-half noise floor
def dist_matrix(df_by):
    P={r:profile(df_by[r]) for r in df_by}; keys=list(df_by)
    return pd.DataFrame([[cosine(P[a],P[b]) if a!=b else 0 for b in keys] for a in keys],index=keys,columns=keys)
Rb={r:emb[(emb.study_region==r)&(emb.doc_class=="research_output")] for r in PREG}
Rb={r:d for r,d in Rb.items() if len(d)>=15}
Dr=dist_matrix(Rb).round(3)
write_table("T31_region_distance_research_only",Dr.reset_index().rename(columns={"index":"region"}),f"Cosine distances between regional profiles using research outputs only (regions with at least 15 embodied research outputs: {', '.join(Rb)})")
floors=[]
for r in PREG:
    d=E_by[r]
    if len(d)<30: continue
    vals=[]
    for b in range(100):
        idx=rng.permutation(len(d)); h=len(d)//2; vals.append(cosine(profile(d.iloc[idx[:h]]),profile(d.iloc[idx[h:]])))
    floors.append(dict(region=r,n=len(d),split_half_distance_median=round(float(np.median(vals)),3),p95=round(float(np.percentile(vals,95)),3)))
t31b=pd.DataFrame(floors); write_table("T31b_split_half_noise_floor",t31b,"Split-half cosine distance within each region (100 random halves): the noise floor below which between-region distances are not distinguishable from sampling variation")
R("region_distance_sensitivity",{"research_only":Dr.to_dict(),"split_half":t31b.to_dict("records")})

# ---------- T32: embodied-set definition sensitivity (strict: relevance >= 2 only)
strict=u[(u.relevance_to_embodied_ai_governance>=2)&(u.ai_scope!="not_ai")]
rows=[]
for name,S in [("Embodied set (relevance >= 2 or any category)",emb),("Strict embodied set (relevance >= 2 only)",strict),("Embodied set, substantive captures only",emb[emb.page_quality=="substantive_document"])]:
    G=S[S.gov]; Rr=S[S.doc_class=="research_output"]
    rows.append(dict(definition=name,n=len(S),research_share_pct=round(100*(S.doc_class=="research_output").mean(),1),governance_documents=len(G),binding=int(S.binding.sum()),
                     physical_safety_any_pct=round(100*(S.pr_physical_safety>=1).mean(),1),proximity_any_pct=round(100*(S.pr_human_robot_proximity>=1).mean(),1),accountability_any_pct=round(100*(S.pr_responsibility_accountability>=1).mean(),1),
                     social_robots_research_pct=round(100*has(Rr.embodied_categories,"social_companion_robots").mean(),1) if len(Rr) else np.nan,social_robots_instruments=int(has(G.embodied_categories,"social_companion_robots").sum()),av_instruments=int(has(G.embodied_categories,"autonomous_road_vehicles").sum())))
t32=pd.DataFrame(rows); write_table("T32_set_definition_sensitivity",t32,"Headline quantities under alternative definitions of the embodied-AI set")
R("set_definition_sensitivity",t32.to_dict("records"))

# ---------- T33: instrument tiers (robot-specific vs general-AI with embodied provisions) and capture quality
gi_all=u[u.instrument]
gi_e=gi_all[gi_all.embodied_set].copy()
gi_e["tier"]=np.where(gi_e.relevance_to_embodied_ai_governance>=2,"robot-specific instrument (relevance 2-3)","general-AI instrument with embodied provisions (relevance 0-1)")
t33=gi_e.groupby(["tier","doc_class"]).agg(n=("doc_id","size"),substantive=("page_quality",lambda s:int((s=="substantive_document").sum())),partial=("page_quality",lambda s:int((s=="partial_or_excerpt").sum())),landing=("page_quality",lambda s:int((s=="landing_or_index_page").sum())),median_fraction_seen=("text_chars",lambda s:round(float(np.median(np.minimum(1,14500/np.maximum(s,1)))),2))).reset_index()
t33["doc_class"]=t33.doc_class.map(DCL)
write_table("T33_instrument_tiers",t33,f"Embodied-AI governance instruments by tier and capture quality (n={len(gi_e)}; 'fraction seen' is the share of the text inside the v1 excerpt)")
R("instrument_tiers",{"n_embodied_instruments":int(len(gi_e)),"robot_specific":int((gi_e.relevance_to_embodied_ai_governance>=2).sum()),"with_provisions":int((gi_e.relevance_to_embodied_ai_governance<2).sum()),"binding_robot_specific":int(((gi_e.relevance_to_embodied_ai_governance>=2)&gi_e.binding).sum()),"binding_with_provisions":int(((gi_e.relevance_to_embodied_ai_governance<2)&gi_e.binding).sum()),"table":t33.to_dict("records")})
lst=gi_e[gi_e.binding][["doc_id","title_en","jurisdiction_country","year_final","instrument_status","relevance_to_embodied_ai_governance","page_quality","embodied_categories"]].copy()
lst["title_en"]=lst.title_en.str.slice(0,100); write_table("T33b_binding_embodied_list",lst.rename(columns={"relevance_to_embodied_ai_governance":"relevance"}),"Binding instruments in the embodied-AI set after corrections, with relevance tier and capture quality")

# ---------- T34: Cochran-Mantel-Haenszel test for core principles stratified by document class
from statsmodels.stats.contingency_tables import StratifiedTable
rows=[]
M2=u[u.setname.isin(["Embodied-AI set","General-AI set"])]
for p in PR_CORE:
    tabs=[]
    for c in DCO:
        S=M2[M2.doc_class==c]
        if len(S)<10: continue
        a=int(((S.setname=="Embodied-AI set")&(S["pr_"+p]>=1)).sum()); b=int(((S.setname=="Embodied-AI set")&(S["pr_"+p]<1)).sum()); c_=int(((S.setname=="General-AI set")&(S["pr_"+p]>=1)).sum()); d=int(((S.setname=="General-AI set")&(S["pr_"+p]<1)).sum())
        if a+b==0 or c_+d==0: continue
        tabs.append(np.array([[a,b],[c_,d]]))
    try:
        st=StratifiedTable(tabs); res=st.test_null_odds(); orp=st.oddsratio_pooled; ci=st.oddsratio_pooled_confint()
        rows.append(dict(principle=PRL[p],strata=len(tabs),mh_odds_ratio=round(float(orp),2),ci_low=round(float(ci[0]),2),ci_high=round(float(ci[1]),2),p=float(res.pvalue)))
    except Exception as e: rows.append(dict(principle=PRL[p],strata=len(tabs),mh_odds_ratio=None,ci_low=None,ci_high=None,p=None))
t34=pd.DataFrame(rows); t34["p_holm"]=holm(t34.p.fillna(1))
write_table("T34_cmh_core_principles",t34.round(4),"Core principles: Mantel-Haenszel odds ratios (embodied vs general) stratified by document class, with Holm correction")
R("cmh_core_principles",t34.to_dict("records"))
dump_results(); print("done D part 2")
