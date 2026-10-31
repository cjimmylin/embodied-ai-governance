#!/usr/bin/env python3
"""Stage 2 part B: how embodied AI is governed (10-15), regional comparison (16-17), trends (18-19)."""
from analysis_common import *
import re, statsmodels.api as sm
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
RESULTS.update(json.load(open(B+"data/results.json")))
a=load(); U=a[a.usable]; emb=U[U.embodied_set]; gen=U[U.general_set]; G=U[U.gov]; Ge=G[G.embodied_set]
def both(fn):
    for th in ("light","dark"): fn(th)
# ---------- C10 principle profiles
rows=[]; pv=[]
for p in PR:
    e1=(emb["pr_"+p]>=1); g1=(gen["pr_"+p]>=1); e2=(emb["pr_"+p]==2); g2=(gen["pr_"+p]==2)
    tab=np.array([[e1.sum(),(~e1).sum()],[g1.sum(),(~g1).sum()]]); test,pval=chi2_or_fisher(tab); pv.append(pval)
    rows.append(dict(principle=p,label=PRL[p],group="core" if p in PR_CORE else "embodied-specific",embodied_any_pct=round(e1.mean()*100,1),general_any_pct=round(g1.mean()*100,1),embodied_substantive_pct=round(e2.mean()*100,1),general_substantive_pct=round(g2.mean()*100,1),diff_any_pp=round((e1.mean()-g1.mean())*100,1),test=test,p=pval))
t8=pd.DataFrame(rows); t8["p_holm"]=holm(t8.p); t8["significant_holm_05"]=t8.p_holm<0.05
t8=t8.sort_values("embodied_any_pct",ascending=False); write_table("T08_principles_by_set",t8.round(4),f"Principle presence (level >= 1) and substantive treatment (level 2): embodied-AI set (n={len(emb)}) vs general-AI set (n={len(gen)}); chi-square/Fisher tests with Holm correction")
R("principles_by_set",t8.to_dict("records"))
def F20(th):
    t=fs.setup(th); d=t8; y=np.arange(len(d)); fig,axes=plt.subplots(1,2,figsize=(7.4,5.2),sharey=True)
    for ax,(ec,gc,title) in zip(axes,[("embodied_any_pct","general_any_pct","Present (level 1 or 2)"),("embodied_substantive_pct","general_substantive_pct","Substantive (level 2)")]):
        for yi,(ev,gv) in enumerate(zip(d[ec],d[gc])): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
        ax.scatter(d[gc],y,color=t["cat"][1],s=34,zorder=2,label="General-AI set"); ax.scatter(d[ec],y,color=t["cat"][0],s=34,zorder=3,label="Embodied-AI set")
        ax.set_xlabel("Share of documents (%)"); ax.set_title(title,loc="left",fontsize=9); ax.yaxis.grid(False); ax.set_xlim(0,100)
    axes[0].set_yticks(y); axes[0].set_yticklabels([f"{l}{' *' if s else ''}" for l,s in zip(d.label,d.significant_holm_05)],fontsize=7.5); axes[0].invert_yaxis(); axes[0].legend(loc="lower right",fontsize=7)
    fig.suptitle("Principle salience by set (* = difference significant after Holm correction)",x=0.02,ha="left",fontsize=10,fontweight="semibold")
    fs.save(fig,"F20_principles_by_set",th); d.to_csv(FD+"F20_principles_by_set.csv",index=False)
both(F20)
REGS=[r for r in REGIONS if (emb.study_region==r).sum()>=30]
def F21(th):
    t=fs.setup(th); mat=np.array([[(emb[emb.study_region==r]["pr_"+p]>=1).mean()*100 for r in REGS] for p in PR])
    fig,ax=plt.subplots(figsize=(7.2,6)); heatmap(ax,mat,[PRL[p] for p in PR],[f"{RSHORT[r]} (n={(emb.study_region==r).sum()})" for r in REGS],t,cbar_label="% of region's embodied documents")
    ax.axhline(13.5,color=t["ink"],lw=0.8); ax.set_title("Principle presence by jurisdiction region (embodied-AI documents; core above the line, embodied-specific below)",loc="left",fontsize=8.5)
    fs.save(fig,"F21_principles_by_region",th); pd.DataFrame(mat,index=PR,columns=REGS).round(1).reset_index().rename(columns={"index":"principle"}).to_csv(FD+"F21_principles_by_region.csv",index=False)
both(F21)
CLS=[c for c in ["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft","government_report_or_parliamentary","research_output","grey_literature","communication_or_news"] if (emb.doc_class==c).sum()>=10]
def F22(th):
    t=fs.setup(th); mat=np.array([[(emb[emb.doc_class==c]["pr_"+p]==2).mean()*100 for c in CLS] for p in PR])
    fig,ax=plt.subplots(figsize=(7.2,6)); heatmap(ax,mat,[PRL[p] for p in PR],[f"{DCL[c]} (n={(emb.doc_class==c).sum()})" for c in CLS],t,cbar_label="% with substantive treatment (level 2)")
    ax.axhline(13.5,color=t["ink"],lw=0.8); ax.set_title("Substantive treatment of principles by document class (embodied-AI documents)",loc="left",fontsize=9)
    fs.save(fig,"F22_principles_by_class",th); pd.DataFrame(mat,index=PR,columns=CLS).round(1).reset_index().rename(columns={"index":"principle"}).to_csv(FD+"F22_principles_by_class.csv",index=False)
both(F22)
# ---------- C11 embodied-specific principles operationalised
embc=emb[emb.content_capture]   # v4: content-analysed captures only (landing and catalogue pages excluded), consistent with F23
grp={"Binding instruments":embc[embc.binding],"Soft-law instruments":embc[(embc.doc_class=="governance_instrument_soft")&(embc.doc_type!="technical_standard")],"Technical standards":embc[embc.doc_type=="technical_standard"],"Proposals / drafts":embc[embc.doc_class=="governance_proposal_or_draft"],"Research outputs":emb[emb.doc_class=="research_output"]}
rows=[]
for name,g in grp.items():
    for p in PR_EMB: rows.append(dict(group=name,n=len(g),principle=p,label=PRL[p],any_pct=round((g["pr_"+p]>=1).mean()*100,1) if len(g) else None,substantive_pct=round((g["pr_"+p]==2).mean()*100,1) if len(g) else None))
t9=pd.DataFrame(rows); write_table("T09_embodied_principles_by_instrument_type",t9,"Embodied-specific principles by instrument type (embodied-AI documents, content-analysed captures only; catalogue and landing pages excluded)")
def F23(th):
    t=fs.setup(th); names=list(grp); fig,ax=plt.subplots(figsize=(7.2,3.4)); x=np.arange(len(PR_EMB)); w=0.15
    for i,name in enumerate(names):
        g=grp[name]; vals=[(g["pr_"+p]==2).mean()*100 if len(g) else 0 for p in PR_EMB]
        ax.bar(x+(i-2)*w,vals,width=w-0.02,color=t["cat"][i],label=f"{name} (n={len(g)})")
    ax.set_xticks(x); ax.set_xticklabels([PRL[p].replace(" & ","\n& ").replace("for physical","for\nphysical").replace("level ","level\n") for p in PR_EMB],fontsize=7.5); ax.set_ylabel("% with substantive treatment"); ax.xaxis.grid(False); ax.legend(fontsize=7,ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.18),frameon=False)
    ax.set_title("Embodied-specific principles operationalised, by instrument type",loc="left"); fs.save(fig,"F23_embodied_principles_by_type",th)
both(F23)
# ---------- C12 mechanisms
MECH=[m for m in sorted(set(labels_of(U.governance_mechanisms)),key=lambda m:-has(emb.governance_mechanisms,m).sum()) if m!="none"]
rows=[]; pv=[]
for m in MECH:
    e=has(emb.governance_mechanisms,m); g=has(gen.governance_mechanisms,m); tab=np.array([[e.sum(),(~e).sum()],[g.sum(),(~g).sum()]]); test,p=chi2_or_fisher(tab); pv.append(p)
    rows.append(dict(mechanism=m,embodied_pct=round(e.mean()*100,1),general_pct=round(g.mean()*100,1),embodied_instruments_pct=round(has(Ge.governance_mechanisms,m).mean()*100,1),general_instruments_pct=round(has(G[G.general_set].governance_mechanisms,m).mean()*100,1),test=test,p=p))
t10=pd.DataFrame(rows); t10["p_holm"]=holm(t10.p); write_table("T10_mechanisms_by_set",t10.round(4),f"Governance mechanisms by set (all usable documents; instrument-only shares for governance documents, embodied n={len(Ge)}, general n={len(G[G.general_set])})")
R("mechanisms_by_set",t10.to_dict("records"))
def F24(th):
    t=fs.setup(th); d=t10; y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,4.4))
    for yi,(ev,gv) in enumerate(zip(d.embodied_pct,d.general_pct)): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.general_pct,y,color=t["cat"][1],s=36,zorder=2,label=f"General-AI set (n={len(gen)})"); ax.scatter(d.embodied_pct,y,color=t["cat"][0],s=36,zorder=3,label=f"Embodied-AI set (n={len(emb)})")
    ax.set_yticks(y); ax.set_yticklabels([f"{nice(m)}{' *' if h<0.05 else ''}" for m,h in zip(d.mechanism,d.p_holm)],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents establishing or recommending the mechanism (%)"); ax.legend(loc="lower right",fontsize=7)
    ax.set_title("Governance mechanisms by set (* = Holm-significant difference)",loc="left"); fs.save(fig,"F24_mechanisms_by_set",th); d.to_csv(FD+"F24_mechanisms_by_set.csv",index=False)
both(F24)
GR=[r for r in REGIONS if (G.study_region==r).sum()>=12]
def F25(th):
    t=fs.setup(th); mat=np.array([[has(G[G.study_region==r].governance_mechanisms,m).mean()*100 for r in GR] for m in MECH])
    fig,ax=plt.subplots(figsize=(7.2,5.6)); heatmap(ax,mat,[nice(m) for m in MECH],[f"{RSHORT[r]} (n={(G.study_region==r).sum()})" for r in GR],t,cbar_label="% of region's governance documents")
    ax.set_title("Governance mechanisms by jurisdiction region (all governance documents)",loc="left"); fs.save(fig,"F25_mechanisms_by_region",th)
    pd.DataFrame(mat,index=MECH,columns=GR).round(1).reset_index().rename(columns={"index":"mechanism"}).to_csv(FD+"F25_mechanisms_by_region.csv",index=False)
both(F25)
# mechanism bundles: k-means on binary vectors of governance documents with >=1 mechanism
Gm=G[G.governance_mechanisms.str.contains("[a-z]")&~(G.governance_mechanisms=="none")].copy()
X=np.array([[1 if has(pd.Series([v]),m).iloc[0] else 0 for m in MECH] for v in Gm.governance_mechanisms])
best=None
for k in range(3,7):
    km=KMeans(n_clusters=k,n_init=10,random_state=0).fit(X); s=silhouette_score(X,km.labels_)
    if best is None or s>best[1]: best=(k,s,km)
k,sil,km=best; Gm["cluster"]=km.labels_
rows=[]
for c in range(k):
    g=Gm[Gm.cluster==c]; prof=sorted([(m,X[Gm.cluster.values==c][:,i].mean()) for i,m in enumerate(MECH)],key=lambda x:-x[1])[:4]
    rows.append(dict(cluster=c+1,n=len(g),embodied_pct=round(g.embodied_set.mean()*100,1),binding_pct=round(g.binding.mean()*100,1),median_year=int(g.year.median()) if g.year.notna().any() else None,top_regions="; ".join(f"{RSHORT.get(r,r)} {n}" for r,n in g.study_region.value_counts().head(3).items()),
                     defining_mechanisms="; ".join(f"{nice(m)} ({v*100:.0f}%)" for m,v in prof),examples="; ".join(f"{r.doc_id} {str(r.title_en)[:60]}" for _,r in g.sort_values("confidence",ascending=False).head(3).iterrows())))
t11=pd.DataFrame(rows); write_table("T11_mechanism_bundles",t11,f"Mechanism bundles: k-means clusters of governance documents on their mechanism vectors (k={k} chosen by silhouette={sil:.2f}, n={len(Gm)})")
R("mechanism_clusters",{"k":k,"silhouette":sil,"n":len(Gm)})
# ---------- C13 framing and stance
FR=["risk_based","rights_based","principle_or_ethics_based","innovation_promotion","liability_or_accountability_based","mixed"]
def F26(th):
    t=fs.setup(th); regs=[r for r in REGIONS if (emb.study_region==r).sum()>=30]; fig,ax=plt.subplots(figsize=(7.2,3.4)); rows=[]
    for i,r in enumerate(regs):
        g=emb[(emb.study_region==r)&(emb.risk_framing!="not_applicable")]; left=0
        for j,f in enumerate(FR):
            v=(g.risk_framing==f).mean()*100 if len(g) else 0; ax.barh(f"{RSHORT[r]} (n={len(g)})",v,left=left,color=t["cat"][j],height=0.6,edgecolor=t["surface"],linewidth=1.2)
            if v>=9: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#0b0b0b" if j==3 else "#ffffff")
            rows.append(dict(region=r,framing=f,pct=round(v,1),n=len(g))); left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of embodied-AI documents (%)"); ax.set_title("Dominant governance framing by region (embodied-AI documents)",loc="left")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j]) for j in range(len(FR))],[nice(f) for f in FR],ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.2),frameon=False,fontsize=7)
    fs.save(fig,"F26_framing_by_region",th); pd.DataFrame(rows).to_csv(FD+"F26_framing_by_region.csv",index=False)
both(F26)
tabf=pd.crosstab(emb[emb.risk_framing!="not_applicable"].study_region,emb[emb.risk_framing!="not_applicable"].risk_framing); R("framing_by_region_test",{"cramers_v":cramers_v(tabf.values),"p":chi2_or_fisher(tabf.values)[1],"table":tabf.to_dict()})
STN=["calls_for_new_regulation","existing_law_sufficient_or_adapt","self_regulation_or_standards_preferred","descriptive_or_neutral"]
def F27(th):
    t=fs.setup(th); cls=[c for c in ["research_output","grey_literature","government_report_or_parliamentary","communication_or_news","governance_proposal_or_draft"] if (emb.doc_class==c).sum()>=10]; fig,ax=plt.subplots(figsize=(7.2,3)); rows=[]
    for i,c in enumerate(cls):
        g=emb[(emb.doc_class==c)&(emb.stance_toward_regulation!="not_applicable")]; left=0
        for j,s in enumerate(STN):
            v=(g.stance_toward_regulation==s).mean()*100 if len(g) else 0; ax.barh(f"{DCL[c]} (n={len(g)})",v,left=left,color=t["cat"][j],height=0.6,edgecolor=t["surface"],linewidth=1.2)
            if v>=9: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#0b0b0b" if j==3 else "#ffffff")
            rows.append(dict(doc_class=c,stance=s,pct=round(v,1),n=len(g))); left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share (%)"); ax.set_title("Stance toward regulation by document class (embodied-AI documents)",loc="left")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j]) for j in range(len(STN))],[nice(s) for s in STN],ncol=2,loc="upper center",bbox_to_anchor=(0.5,-0.22),frameon=False,fontsize=7)
    fs.save(fig,"F27_stance_by_class",th); pd.DataFrame(rows).to_csv(FD+"F27_stance_by_class.csv",index=False)
both(F27)
R("stance_research",emb[emb.doc_class=="research_output"].stance_toward_regulation.value_counts(normalize=True).to_dict())
# ---------- C14 personhood
ph=U[U.robot_legal_personhood_position!="not_discussed"]
t12=pd.crosstab(ph.study_region,ph.robot_legal_personhood_position).reset_index(); write_table("T12_personhood_by_region",t12,f"Robot legal personhood: positions by jurisdiction region (documents discussing it, n={len(ph)})")
R("personhood",{"n_discussing":len(ph),"supports":int((ph.robot_legal_personhood_position=="supports").sum()),"opposes":int((ph.robot_legal_personhood_position=="opposes").sum()),"neutral":int((ph.robot_legal_personhood_position=="discusses_neutral").sum()),"by_period":pd.crosstab(ph.period,ph.robot_legal_personhood_position).to_dict()})
def F28(th):
    t=fs.setup(th); pers=["to 2014","2015-2019","2020-2022","2023-2024","2025-2026"]; fig,ax=plt.subplots(figsize=(6.4,2.8)); x=np.arange(len(pers)); POS=["supports","discusses_neutral","opposes"]; bottom=np.zeros(len(pers)); rows=[]
    for j,p in enumerate(POS):
        vals=np.array([int(((ph.period==pe)&(ph.robot_legal_personhood_position==p)).sum()) for pe in pers]); ax.bar(x,vals,bottom=bottom,color=[t["cat"][2],t["muted"],t["cat"][7]][j],width=0.6,label=nice(p),edgecolor=t["surface"],linewidth=1); bottom+=vals
        for pe,v in zip(pers,vals): rows.append(dict(period=pe,position=p,n=int(v)))
    ax.set_xticks(x); ax.set_xticklabels(pers); ax.xaxis.grid(False); ax.set_ylabel("Documents discussing personhood"); ax.legend(loc="upper left"); ax.set_title("Positions on robot legal personhood over time",loc="left")
    fs.save(fig,"F28_personhood_over_time",th); pd.DataFrame(rows).to_csv(FD+"F28_personhood_over_time.csv",index=False)
both(F28)
# ---------- C15 reference network
CANON=[("EU AI Act",r"\bAI Act\b|2024/1689|Artificial Intelligence Act"),("GDPR",r"GDPR|General Data Protection"),("UNESCO Recommendation on the Ethics of AI",r"UNESCO"),("OECD AI Principles",r"OECD"),("EU Civil Law Rules on Robotics 2017",r"Civil Law Rules|2015/2103|electronic person"),
("ISO 13482",r"13482"),("ISO 10218",r"10218"),("ISO/TS 15066",r"15066"),("ISO/IEC 42001",r"42001"),("ISO/IEC 23894",r"23894"),("ISO/IEC 22989",r"22989"),("IEEE 7000 series",r"IEEE"),("ANSI/A3 R15.06",r"R15\.06|ANSI"),("Asimov's Laws of Robotics",r"Asimov|Three Laws"),
("NIST AI RMF",r"NIST"),("Council of Europe Framework Convention on AI",r"Council of Europe"),("EU Machinery Regulation",r"Machinery"),("EU Product Liability Directive",r"Product Liability"),("EU AI Liability Directive (proposal)",r"AI Liability"),("Korea Intelligent Robots Act",r"Intelligent Robots? Act"),("Korea AI Basic Act",r"AI Basic Act|Basic Act on"),("Japan AI Promotion Act",r"Japan AI Promotion|Promotion of Research and Development"),("China Generative AI Measures",r"Generative AI Measures|Interim Measures"),("US Executive Order 14110",r"14110"),("Colorado AI Act",r"Colorado"),("Bletchley Declaration",r"Bletchley"),("Hiroshima Process",r"Hiroshima"),("UN LAWS/CCW GGE",r"\bCCW\b|LAWS|GGE|Certain Conventional"),("Bill of Rights (US AI Blueprint)",r"Bill of Rights")]
def canon(v):
    out=set()
    for x in v.split("; "):
        if not x: continue
        for name,pat in CANON:
            if re.search(pat,x,re.I): out.add(name); break
    return out
U=U.copy(); U["inst_canon"]=U.named_instruments_referenced.map(canon); emb=U[U.embodied_set]; gen=U[U.general_set]
cnt_e={n:int(emb.inst_canon.map(lambda s:n in s).sum()) for n,_ in CANON}; cnt_g={n:int(gen.inst_canon.map(lambda s:n in s).sum()) for n,_ in CANON}
t13=pd.DataFrame([dict(instrument=n,embodied_docs=cnt_e[n],embodied_pct=round(cnt_e[n]/len(emb)*100,1),general_docs=cnt_g[n],general_pct=round(cnt_g[n]/len(gen)*100,1)) for n,_ in CANON]).sort_values("embodied_docs",ascending=False)
write_table("T13_instruments_cited",t13,"Named instruments cited, by set (canonicalised from the annotated reference lists)"); R("instruments_cited",t13.to_dict("records"))
R("any_instrument_cited_pct",{"embodied":float(emb.inst_canon.map(len).gt(0).mean()),"general":float(gen.inst_canon.map(len).gt(0).mean())})
def F29(th):
    t=fs.setup(th); d=t13[(t13.embodied_docs+t13.general_docs)>=5].head(16); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,4.4))
    ax.barh(y-0.2,d.embodied_pct,height=0.38,color=t["cat"][0],label=f"Embodied-AI set (n={len(emb)})"); ax.barh(y+0.2,d.general_pct,height=0.38,color=t["cat"][1],label=f"General-AI set (n={len(gen)})")
    ax.set_yticks(y); ax.set_yticklabels(d.instrument,fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents citing the instrument (%)"); ax.legend(loc="lower right",fontsize=7)
    ax.set_title("Most cited governance instruments",loc="left"); fs.save(fig,"F29_instruments_cited",th); d.to_csv(FD+"F29_instruments_cited.csv",index=False)
both(F29)
TOPI=list(t13.head(12).instrument)
def F30(th):
    t=fs.setup(th); regs=[r for r in REGIONS if (U.study_region==r).sum()>=20]; mat=np.array([[U[U.study_region==r].inst_canon.map(lambda s:n in s).mean()*100 for r in regs] for n in TOPI])
    fig,ax=plt.subplots(figsize=(7.2,4.6)); heatmap(ax,mat,TOPI,[f"{RSHORT[r]} (n={(U.study_region==r).sum()})" for r in regs],t,fmt="{:.0f}",cbar_label="% of region's documents citing")
    ax.set_title("Instrument citation by jurisdiction region (all usable documents)",loc="left"); fs.save(fig,"F30_instruments_by_region",th)
    pd.DataFrame(mat,index=TOPI,columns=regs).round(1).reset_index().rename(columns={"index":"instrument"}).to_csv(FD+"F30_instruments_by_region.csv",index=False)
both(F30)
# ---------- D16 region profiles and distances
TOPS=list(RESULTS["topic_any_embodied"].keys())
def vec(g):
    v=[(g["pr_"+p]>=1).mean() for p in PR]+[has(g.governance_topics,k).mean() for k in TOPS]+[has(g.governance_mechanisms,m).mean() for m in MECH]
    return np.array(v)
PREG=[r for r in REGIONS if (emb.study_region==r).sum()>=30]   # v4: same region set as the bootstrap tables (T23) and noise floors
V=np.array([vec(emb[emb.study_region==r]) for r in PREG]); D=squareform(pdist(V,metric="cosine")); Z=linkage(pdist(V,metric="cosine"),method="average")
pd.DataFrame(D,index=PREG,columns=PREG).round(3).reset_index().rename(columns={"index":"region"}).to_csv(FD+"F31_region_distances.csv",index=False)
R("region_distance",{"regions":PREG,"matrix":D.round(3).tolist()})
def F31(th):
    t=fs.setup(th); fig,axes=plt.subplots(1,2,figsize=(7.4,3.6),gridspec_kw={"width_ratios":[1,1.25],"wspace":0.08})
    dn=dendrogram(Z,labels=[RSHORT[r] for r in PREG],ax=axes[0],orientation="left",color_threshold=0,above_threshold_color=t["cat"][0],no_labels=True); order=dn["leaves"][::-1]
    axes[0].set_xlabel("Cosine distance"); axes[0].xaxis.grid(True); axes[0].yaxis.grid(False); axes[0].set_yticks([])
    for s_ in axes[0].spines.values(): s_.set_visible(False)
    Do=D[np.ix_(order,order)]; labs=[RSHORT[PREG[i]] for i in order]
    heatmap(axes[1],Do,labs,labs,t,fmt="{:.2f}",cbar_label="cosine distance"); axes[1].yaxis.tick_left()
    fig.suptitle("Regional similarity in how embodied AI is governed (principles, topics, mechanisms)",x=0.02,ha="left",fontsize=10,fontweight="semibold"); fs.save(fig,"F31_region_similarity",th)
both(F31)
rows=[]
for r in REGIONS:
    g=emb[emb.study_region==r]; ga=U[U.study_region==r]
    if not len(ga): continue
    topc=sorted([(c,has(g.embodied_categories,c).mean()) for c in EMB],key=lambda x:-x[1])[:3]; topp=sorted([(p,(g["pr_"+p]>=1).mean()) for p in PR],key=lambda x:-x[1])[:3]; topm=sorted([(m,has(g.governance_mechanisms,m).mean()) for m in MECH],key=lambda x:-x[1])[:3]
    rows.append(dict(region=r,documents=len(ga),embodied_documents=len(g),embodied_share_pct=round(len(g)/len(ga)*100,1),governance_documents=int(ga.gov.sum()),embodied_governance_documents=int(g.gov.sum()),binding_embodied=int(g.binding.sum()),research_share_embodied_pct=round((g.doc_class=="research_output").mean()*100,1) if len(g) else None,
                     median_year=int(g.year.median()) if g.year.notna().any() else None,top_categories="; ".join(f"{nice(c)} {v*100:.0f}%" for c,v in topc),top_principles="; ".join(f"{PRL[p]} {v*100:.0f}%" for p,v in topp),top_mechanisms="; ".join(f"{nice(m)} {v*100:.0f}%" for m,v in topm),
                     top_languages="; ".join(f"{k} {v}" for k,v in ga.language.value_counts().head(3).items()),countries=int(ga[~ga.jurisdiction_country.isin(["EU","INT","XX"])].jurisdiction_country.nunique())))
t14=pd.DataFrame(rows); write_table("T14_region_profiles",t14,"Regional profiles (embodied-AI documents unless stated)"); R("region_profiles",t14.to_dict("records"))
# ---------- D17 divergence tests
rows=[]
for p in PR:
    tab=pd.crosstab(emb[emb.study_region.isin(PREG)].study_region,emb[emb.study_region.isin(PREG)]["pr_"+p]>=1)
    if tab.shape[1]<2: continue
    test,pv=chi2_or_fisher(tab.values); rows.append(dict(item="principle:"+p,label=PRL[p],cramers_v=round(cramers_v(tab.values),3),p=pv,min_region_pct=round(tab[True].div(tab.sum(1)).min()*100,1),max_region_pct=round(tab[True].div(tab.sum(1)).max()*100,1)))
for m in MECH:
    sub=G[G.study_region.isin(GR)]; tab=pd.crosstab(sub.study_region,has(sub.governance_mechanisms,m))
    if tab.shape[1]<2: continue
    test,pv=chi2_or_fisher(tab.values); rows.append(dict(item="mechanism:"+m,label=nice(m),cramers_v=round(cramers_v(tab.values),3),p=pv,min_region_pct=round(tab[True].div(tab.sum(1)).min()*100,1),max_region_pct=round(tab[True].div(tab.sum(1)).max()*100,1)))
t15=pd.DataFrame(rows); t15["p_holm"]=holm(t15.p); t15=t15.sort_values("cramers_v",ascending=False); write_table("T15_regional_divergence",t15.round(4),"Regional divergence: association between region and principle presence (embodied-AI documents) or mechanism presence (governance documents); Cramer's V with Holm-corrected chi-square p")
R("regional_divergence",t15.head(10).to_dict("records"))
# ---------- E18 recency
TERMS=[("lex_embodied_ai_term_pk","'Embodied AI' / 'physical AI'"),("lex_humanoid_pk","Humanoid"),("lex_cobot_pk","Cobot"),("lex_autonomous_vehicle_pk","Autonomous vehicle"),("lex_drone_pk","Drone / UAS"),("lex_military_laws_pk","Autonomous weapons"),("lex_surgical_robot_pk","Surgical robot"),("lex_care_robot_pk","Care robot"),("lex_social_robot_pk","Social robot")]
Yt=U[U.year.notna()&(U.year>=2018)&(U.year<=2026)].copy(); Yt["year"]=Yt.year.astype(int); yrs=list(range(2018,2027))
def F33(th):
    t=fs.setup(th); fig,axes=plt.subplots(3,3,figsize=(7.4,5.4),sharex=True); rows=[]
    for ax,(col,lab) in zip(axes.flat,TERMS):
        vals=[Yt[Yt.year==y][col].mean() for y in yrs]; share=[(Yt[Yt.year==y][col]>0).mean()*100 for y in yrs]
        ax.plot(yrs,share,color=t["cat"][0],marker="o",ms=3); ax.set_title(lab,loc="left",fontsize=8); ax.set_ylim(0,max(5,max(share)*1.15)); ax.xaxis.grid(False); ax.set_xticks([2018,2020,2022,2024,2026]); ax.tick_params(labelsize=7)
        for y,s,v in zip(yrs,share,vals): rows.append(dict(term=lab,year=y,share_docs_pct=round(s,1),mean_density_per_1000w=round(v,3),n=int((Yt.year==y).sum())))
    fig.supylabel("% of documents using the term",fontsize=8); fig.suptitle("Term usage over time across all usable documents (full-text lexicon)",x=0.02,ha="left",fontsize=10,fontweight="semibold")
    fs.save(fig,"F33_term_trends",th); pd.DataFrame(rows).to_csv(FD+"F33_term_trends.csv",index=False)
both(F33)
ALLTOPICS=sorted(set(labels_of(emb.governance_topics)))
old=emb[emb.year.between(2020,2024)]; new=emb[emb.year.between(2025,2026)]
rows=[]
for k in ALLTOPICS:
    o=has(old.governance_topics,k).mean()*100; n=has(new.governance_topics,k).mean()*100; tab=np.array([[has(new.governance_topics,k).sum(),(~has(new.governance_topics,k)).sum()],[has(old.governance_topics,k).sum(),(~has(old.governance_topics,k)).sum()]])
    rows.append(dict(topic=k,pct_2020_2024=round(o,1),pct_2025_2026=round(n,1),change_pp=round(n-o,1),p=chi2_or_fisher(tab)[1]))
t16=pd.DataFrame(rows); t16["p_holm"]=holm(t16.p); t16=t16.sort_values("change_pp",ascending=False); write_table("T16_topic_change",t16.round(4),f"Governance topics in embodied-AI documents: 2025-2026 (n={len(new)}) vs 2020-2024 (n={len(old)})")
R("topic_change",t16.to_dict("records")); R("recency_n",{"old":len(old),"new":len(new)})
def F34(th):
    t=fs.setup(th); d=t16[(t16.pct_2020_2024+t16.pct_2025_2026)>=6]; y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,4.6))
    for yi,(o,n) in enumerate(zip(d.pct_2020_2024,d.pct_2025_2026)): ax.plot([o,n],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.pct_2020_2024,y,color=t["cat"][1],s=36,zorder=2,label=f"2020-2024 (n={len(old)})"); ax.scatter(d.pct_2025_2026,y,color=t["cat"][0],s=36,zorder=3,label=f"2025-2026 (n={len(new)})")
    ax.set_yticks(y); ax.set_yticklabels([f"{nice(k)}{' *' if h<0.05 else ''}" for k,h in zip(d.topic,d.p_holm)],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of embodied-AI documents addressing the topic (%)"); ax.legend(loc="lower right",fontsize=7)
    ax.set_title("Governance topics: recent documents vs 2020-2024 (* = Holm-significant)",loc="left"); fs.save(fig,"F34_topic_change",th); d.to_csv(FD+"F34_topic_change.csv",index=False)
both(F34)
# ---------- E19 trend models
M=emb[emb.year.between(2015,2026)&emb.study_region.isin(PREG)].copy(); M["yc"]=M.year-2022
Xb=pd.get_dummies(M[["study_region","doc_class"]],drop_first=False).astype(float)
Xb=Xb.drop(columns=[c for c in Xb.columns if c.endswith("Europe") or c.endswith("research_output")],errors="ignore")
Xd=pd.concat([M[["yc"]].astype(float),Xb],axis=1); Xd=sm.add_constant(Xd)
rows=[]
for p in PR_EMB+["risk_based_tiering_mech","conformity_assessment_certification_mech"]:
    if p.endswith("_mech"): yv=has(M.governance_mechanisms,p[:-5]).astype(int); lab="mechanism: "+nice(p[:-5])
    else: yv=(M["pr_"+p]>=1).astype(int); lab="principle: "+PRL[p]
    try:
        fit=sm.Logit(yv,Xd).fit(disp=0,maxiter=200); ci=fit.conf_int().loc["yc"]
        rows.append(dict(outcome=lab,n=len(M),events=int(yv.sum()),odds_ratio_per_year=round(float(np.exp(fit.params["yc"])),3),ci_low=round(float(np.exp(ci[0])),3),ci_high=round(float(np.exp(ci[1])),3),p=float(fit.pvalues["yc"])))
    except Exception as e: rows.append(dict(outcome=lab,n=len(M),events=int(yv.sum()),odds_ratio_per_year=None,ci_low=None,ci_high=None,p=None))
t17=pd.DataFrame(rows); t17["p_holm"]=holm(t17.p.fillna(1)); write_table("T17_trend_models",t17.round(4),"Logistic regressions: presence of embodied-specific principles (level >= 1) and two mechanisms on publication year, adjusting for region and document class (embodied-AI documents, 2015-2026)")
R("trend_models",t17.to_dict("records"))
dump_results(); print("Part B done:",len(RESULTS),"result keys")
