#!/usr/bin/env python3
"""Stage 2 part A: the document landscape (analyses 1-5) and what is governed (6-9)."""
from analysis_common import *
import os
if os.path.exists(B+'data/results.json'): RESULTS.update(json.load(open(B+'data/results.json')))
a=load(); emb=a[a.embodied_set&a.usable]; gen=a[a.general_set&a.usable]; U=a[a.usable]
R("n_annotated",len(a)); R("n_usable",len(U)); R("n_embodied",len(emb)); R("n_general",len(gen))
def both(fn):
    for th in ("light","dark"): fn(th)
# ---------- A1 composition
def F01(th):
    t=fs.setup(th); sets=[("Embodied-AI set",emb),("General-AI set",gen)]
    fig,ax=plt.subplots(figsize=(7.2,2.4)); rows=[]
    for i,(name,g) in enumerate(sets):
        left=0
        for j,k in enumerate(DCO):
            v=(g.doc_class==k).mean()*100; col=t["cat"][j] if j<7 else t["muted"]
            ax.barh(name,v,left=left,color=col,height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=6: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7.5,color="#0b0b0b" if j==3 else "#ffffff")
            rows.append(dict(set=name,doc_class=k,share_pct=round(v,1),n=int((g.doc_class==k).sum()),n_total=len(g))); left+=v
    ax.set_xlim(0,100); ax.set_xlabel("Share of documents (%)"); ax.invert_yaxis(); ax.yaxis.grid(False)
    ax.set_title(f"Document classes: embodied-AI set (n={len(emb)}) vs general-AI set (n={len(gen)})",loc="left")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j] if j<7 else t["muted"]) for j in range(len(DCO))],[DCL[k] for k in DCO],ncol=4,loc="upper center",bbox_to_anchor=(0.5,-0.38),frameon=False)
    fs.save(fig,"F01_composition_by_set",th); pd.DataFrame(rows).to_csv(FD+"F01_composition_by_set.csv",index=False)
both(F01)
comp=pd.crosstab(U.doc_class,U.setname); R("class_by_set",comp.to_dict())
def F03(th):
    t=fs.setup(th); its=U.issuer_type.value_counts().index[:12]
    e=[(emb.issuer_type==i).mean()*100 for i in its]; g=[(gen.issuer_type==i).mean()*100 for i in its]
    fig,ax=plt.subplots(figsize=(7.2,3.6)); y=np.arange(len(its))
    for yi,(ev,gv) in enumerate(zip(e,g)): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(g,y,color=t["cat"][1],s=38,zorder=2,label="General-AI set"); ax.scatter(e,y,color=t["cat"][0],s=38,zorder=3,label="Embodied-AI set")
    ax.set_yticks(y); ax.set_yticklabels([nice(i) for i in its]); ax.invert_yaxis(); ax.set_xlabel("Share of documents (%)"); ax.yaxis.grid(False); ax.legend(loc="lower right")
    ax.set_title("Issuer types by set",loc="left"); fs.save(fig,"F03_issuer_types",th)
    pd.DataFrame({"issuer_type":its,"embodied_pct":np.round(e,1),"general_pct":np.round(g,1)}).to_csv(FD+"F03_issuer_types.csv",index=False)
both(F03)
t1=pd.crosstab(U.doc_type,U.setname).reindex(columns=["Embodied-AI set","General-AI set","Other"],fill_value=0); t1["total"]=t1.sum(1); t1=t1.sort_values("total",ascending=False).reset_index()
t1["doc_type"]=t1.doc_type.map(nice); write_table("T01_doc_types_by_set",t1,"Document types by analysis set (usable documents)")
# ---------- A2 lifecycle
G=U[U.gov]; Ge=G[G.embodied_set]; Gg=G[G.general_set]
R("n_gov",len(G)); R("n_gov_embodied",len(Ge)); R("n_gov_general",len(Gg))
bn=pd.crosstab(G.setname,G.binding_nature); R("binding_by_set",bn.to_dict())
tab=pd.crosstab(G[G.setname!="Other"].setname,G[G.setname!="Other"].binding_nature.replace({"technical_standard_mandated":"technical_standard_voluntary"}))
tab=tab[[c for c in ["legally_binding","voluntary_soft_law","technical_standard_voluntary"] if c in tab.columns]]
test,p=chi2_or_fisher(tab.values); R("binding_nature_test",{"test":test,"p":p,"cramers_v":cramers_v(tab.values),"table":tab.to_dict()})
def F04(th):
    t=fs.setup(th); fig,axes=plt.subplots(1,2,figsize=(7.2,3.2),gridspec_kw={"width_ratios":[1.3,1]})
    ST=["proposal_or_concept","draft_or_bill_under_consideration","consultation_open","adopted_not_yet_in_force","in_force","published_current","under_development","superseded_or_repealed","unknown"]
    ax=axes[0]; rows=[]
    for i,(name,g) in enumerate([("Embodied-AI set",Ge),("General-AI set",Gg)]):
        left=0
        for j,s in enumerate(ST):
            v=(g.instrument_status==s).mean()*100; col=t["cat"][j%7] if j<7 else t["muted"]
            ax.barh(name,v,left=left,color=col,height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=8: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#0b0b0b" if j==3 else "#ffffff")
            rows.append(dict(set=name,status=s,pct=round(v,1),n=int((g.instrument_status==s).sum()))); left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of governance documents (%)"); ax.set_title("Lifecycle status",loc="left",fontsize=9)
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j%7] if j<7 else t["muted"]) for j in range(len(ST))],[nice(s) for s in ST],ncol=2,loc="upper left",bbox_to_anchor=(0,-0.3),frameon=False,fontsize=6.5)
    ax=axes[1]; BN=["legally_binding","voluntary_soft_law","technical_standard_voluntary","not_applicable"]
    for i,(name,g) in enumerate([("Embodied-AI set",Ge),("General-AI set",Gg)]):
        left=0
        for j,s in enumerate(BN):
            v=(g.binding_nature==s).mean()*100; col=[t["cat"][0],t["cat"][1],t["cat"][2],t["muted"]][j]
            ax.barh(name,v,left=left,color=col,height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=8: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#ffffff")
            rows.append(dict(set=name,status="binding:"+s,pct=round(v,1),n=int((g.binding_nature==s).sum()))); left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_yticklabels([]); ax.set_xlabel("Share (%)"); ax.set_title("Binding nature",loc="left",fontsize=9)
    ax.legend([plt.Rectangle((0,0),1,1,color=c) for c in [t["cat"][0],t["cat"][1],t["cat"][2],t["muted"]]],["Legally binding","Voluntary soft law","Technical standard","Not applicable"],ncol=1,loc="upper left",bbox_to_anchor=(0,-0.3),frameon=False,fontsize=6.5)
    fig.suptitle(f"Governance documents: lifecycle status and binding nature (embodied n={len(Ge)}, general n={len(Gg)})",x=0.02,ha="left",fontsize=10,fontweight="semibold")
    fs.save(fig,"F04_lifecycle_binding",th); pd.DataFrame(rows).to_csv(FD+"F04_lifecycle_binding.csv",index=False)
both(F04)
t2=pd.crosstab([G.setname,G.instrument_status],G.binding_nature).reset_index(); write_table("T02_status_by_binding",t2,"Governance documents: lifecycle status by binding nature and set")
# ---------- A3 timeline
Y=U[U.year.notna()&(U.year>=2010)&(U.year<=2026)].copy(); Y["year"]=Y.year.astype(int)
def F02(th):
    t=fs.setup(th); yrs=list(range(2010,2027)); e=[int((Y[Y.year==y].embodied_set).sum()) for y in yrs]; o=[int((~Y[Y.year==y].embodied_set).sum()) for y in yrs]
    fig,ax=plt.subplots(figsize=(7.2,3)); ax.bar(yrs,e,color=t["cat"][0],width=0.72,label="Embodied-AI set"); ax.bar(yrs,o,bottom=e,color=t["cat"][1],width=0.72,label="Other AI governance",edgecolor=t["surface"],linewidth=1)
    ax.set_xticks(yrs); ax.set_xticklabels([str(y) if y%2==0 else "" for y in yrs]); ax.xaxis.grid(False); ax.set_ylabel("Documents"); ax.legend(loc="upper left")
    ax.set_title(f"Documents per publication year, 2010 to 2026 (n={len(Y)}; 2026 is partial)",loc="left"); fs.save(fig,"F02_timeline",th)
    pd.DataFrame({"year":yrs,"embodied":e,"other":o}).to_csv(FD+"F02_timeline.csv",index=False)
both(F02)
def F05(th):
    t=fs.setup(th); yrs=list(range(2015,2027)); k=[int(Y[Y.year==y].embodied_set.sum()) for y in yrs]; n=[int((Y.year==y).sum()) for y in yrs]
    p=[ki/ni*100 if ni else np.nan for ki,ni in zip(k,n)]; ci=[wilson(ki,ni) for ki,ni in zip(k,n)]
    fig,ax=plt.subplots(figsize=(7.2,2.8)); ax.fill_between(yrs,[c[0]*100 for c in ci],[c[1]*100 for c in ci],color=t["cat"][0],alpha=0.15,linewidth=0)
    ax.plot(yrs,p,color=t["cat"][0],marker="o",ms=4); ax.set_ylim(0,100); ax.set_ylabel("Embodied share of documents (%)"); ax.xaxis.grid(False)
    for y,pv,ni in zip(yrs,p,n): ax.text(y,pv+4,f"n={ni}",ha="center",fontsize=6.5,color=t["muted"])
    ax.set_title("Share of documents in the embodied-AI set by year, with 95% Wilson intervals",loc="left"); fs.save(fig,"F05_embodied_share_by_year",th)
    pd.DataFrame({"year":yrs,"embodied":k,"n":n,"share_pct":np.round(p,1),"ci_low":[round(c[0]*100,1) for c in ci],"ci_high":[round(c[1]*100,1) for c in ci]}).to_csv(FD+"F05_embodied_share_by_year.csv",index=False)
both(F05)
# trend test on embodied share 2015-2026 (Cochran-Armitage via logistic regression on year)
import statsmodels.api as sm
yy=Y[Y.year>=2015]; X=sm.add_constant((yy.year-2020).astype(float)); lg=sm.Logit(yy.embodied_set.astype(int),X).fit(disp=0)
R("embodied_share_trend",{"odds_ratio_per_year":float(np.exp(lg.params.iloc[1])),"ci":[float(np.exp(lg.conf_int().iloc[1,0])),float(np.exp(lg.conf_int().iloc[1,1]))],"p":float(lg.pvalues.iloc[1]),"n":len(yy)})
def F06(th):
    t=fs.setup(th); g=Y[Y.gov&Y.embodied_set]; yrs=list(range(2010,2027))
    series={"Legally binding":g[g.binding_nature=="legally_binding"],"Voluntary soft law":g[g.binding_nature=="voluntary_soft_law"],"Technical standards":g[g.binding_nature.str.startswith("technical")],"Drafts and proposals":g[g.instrument_status.isin(["proposal_or_concept","draft_or_bill_under_consideration","consultation_open"])]}
    fig,ax=plt.subplots(figsize=(7.2,3)); rows={"year":yrs}
    for i,(name,s) in enumerate(series.items()):
        c=np.cumsum([int((s.year==y).sum()) for y in yrs]); ax.step(yrs,c,where="post",color=t["cat"][i],label=f"{name} (n={len(s)})"); rows[name]=c
    ax.set_ylabel("Cumulative documents"); ax.xaxis.grid(False); ax.legend(loc="upper left"); ax.set_title("Cumulative embodied-AI governance documents by binding nature",loc="left")
    fs.save(fig,"F06_cumulative_instruments",th); pd.DataFrame(rows).to_csv(FD+"F06_cumulative_instruments.csv",index=False)
both(F06)
rows=[]
for c in EMB:
    s=U[has(U.embodied_categories,c)&U.year.notna()]
    gv=s[s.gov]; rs=s[s.doc_class=="research_output"]
    rows.append(dict(category=c,level1=L1[c],n_docs=len(s),first_year_any=int(s.year.min()) if len(s) else None,first_year_governance=int(gv.year.min()) if len(gv) else None,n_governance=len(gv),first_year_research=int(rs.year.min()) if len(rs) else None,n_research=len(rs),median_year=int(s.year.median()) if len(s) else None))
t3=pd.DataFrame(rows).sort_values("n_docs",ascending=False); write_table("T03_first_appearance",t3,"Embodied categories: document counts and first-appearance years (by document type)")
# ---------- A4 geography
Rg=U[U.study_region.isin(REGIONS)]
def F07(th):
    t=fs.setup(th); regs=[r for r in REGIONS]; e=[int((Rg[Rg.study_region==r].embodied_set).sum()) for r in regs]; g=[int((Rg[Rg.study_region==r].general_set).sum()) for r in regs]; n=[int((Rg.study_region==r).sum()) for r in regs]
    fig,axes=plt.subplots(1,2,figsize=(7.2,3.2),gridspec_kw={"width_ratios":[1.4,1]}); ax=axes[0]; y=np.arange(len(regs))
    ax.barh(y-0.2,e,height=0.38,color=t["cat"][0],label="Embodied-AI set"); ax.barh(y+0.2,g,height=0.38,color=t["cat"][1],label="General-AI set")
    ax.set_yticks(y); ax.set_yticklabels([RSHORT[r] for r in regs]); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Documents"); ax.legend(loc="lower right"); ax.set_title("Documents by jurisdiction region",loc="left",fontsize=9)
    ax=axes[1]; sh=[ei/ni*100 if ni else 0 for ei,ni in zip(e,n)]; ci=[wilson(ei,ni) for ei,ni in zip(e,n)]
    ax.barh(y,sh,height=0.55,color=t["cat"][0]); ax.errorbar(sh,y,xerr=[[s-c[0]*100 for s,c in zip(sh,ci)],[c[1]*100-s for s,c in zip(sh,ci)]],fmt="none",ecolor=t["ink2"],elinewidth=0.8,capsize=2)
    ax.set_yticks(y); ax.set_yticklabels([]); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Embodied share (%)"); ax.set_title("Embodied share within region",loc="left",fontsize=9)
    fs.save(fig,"F07_region_counts",th); pd.DataFrame({"region":regs,"embodied":e,"general":g,"n_usable":n,"embodied_share_pct":np.round(sh,1)}).to_csv(FD+"F07_region_counts.csv",index=False)
both(F07)
tab=pd.crosstab(Rg.study_region,Rg.embodied_set); R("embodied_share_by_region",{"table":tab.to_dict(),"cramers_v":cramers_v(tab.values),"p":chi2_or_fisher(tab.values)[1]})
cty=U[~U.jurisdiction_country.isin(["EU","INT","XX"])]
rows=[]
for c,g in cty.groupby("jurisdiction_country"):
    rows.append(dict(country=c,country_name=g.jurisdiction_country_name.iloc[0],region=g.study_region.iloc[0],docs=len(g),embodied=int(g.embodied_set.sum()),gov_instruments=int(g.instrument.sum()),embodied_instruments_principal=int((g.instrument&g.embodied_set).sum()),binding_embodied=int((g.binding&g.embodied_set&g.instrument).sum()),embodied_instruments=int((g.gov&g.embodied_set).sum()),binding=int(g.binding.sum()),research=int((g.doc_class=="research_output").sum()),median_year=(int(g.year.median()) if g.year.notna().any() else None)))
t4=pd.DataFrame(rows).sort_values(["embodied","docs"],ascending=False); write_table("T04_countries",t4,"Documents by jurisdiction country (national jurisdictions only; EU and international bodies excluded)")
R("n_countries",len(t4))
def F08(th):
    t=fs.setup(th); top=t4.head(20); y=np.arange(len(top))
    fig,ax=plt.subplots(figsize=(7.2,4.4)); ax.barh(y,top.embodied_instruments,height=0.6,color=t["cat"][0],label="Embodied governance instruments")
    ax.barh(y,top.embodied-top.embodied_instruments,left=top.embodied_instruments,height=0.6,color=t["cat"][2],label="Other embodied documents",edgecolor=t["surface"],linewidth=1)
    ax.set_yticks(y); ax.set_yticklabels([f"{n} ({r})" for n,r in zip(top.country_name,top.region.map(RSHORT))],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Embodied-AI documents"); ax.legend(loc="lower right")
    for yi,v in enumerate(top.embodied): ax.text(v+0.5,yi,str(v),va="center",fontsize=7,color=t["ink2"])
    ax.set_title("Top 20 national jurisdictions by embodied-AI documents",loc="left"); fs.save(fig,"F08_top_countries",th); top.to_csv(FD+"F08_top_countries.csv",index=False)
both(F08)
# ---------- A5 language and venue
LANGS=["en","es","pt","fr","zh","ja","ko","ar","ru","de"]
def F10(th):
    t=fs.setup(th); regs=[r for r in REGIONS if r!="International"]; fig,ax=plt.subplots(figsize=(7.2,3.2)); rows=[]
    groups=[("English",["en"]),("Spanish / Portuguese",["es","pt"]),("French / German / Italian",["fr","de","it"]),("Chinese / Japanese / Korean",["zh","ja","ko"]),("Arabic / Hebrew / Turkish",["ar","he","tr"]),("Russian / Polish / other",None)]
    for i,r in enumerate(regs):
        g=Rg[Rg.study_region==r]; left=0; used=set()
        for j,(name,ls) in enumerate(groups):
            if ls is None: m=~g.language.isin(used)
            else: m=g.language.isin(ls); used|=set(ls)
            v=m.mean()*100; col=t["cat"][j] if j<5 else t["muted"]
            ax.barh(RSHORT[r],v,left=left,color=col,height=0.6,edgecolor=t["surface"],linewidth=1.2)
            if v>=10: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#0b0b0b" if j==3 else "#ffffff")
            rows.append(dict(region=r,language_group=name,pct=round(v,1),n=int(m.sum()))); left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents (%)"); ax.set_title("Document language by jurisdiction region",loc="left")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][j] if j<5 else t["muted"]) for j in range(6)],[g[0] for g in groups],ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.2),frameon=False,fontsize=7)
    fs.save(fig,"F10_language_by_region",th); pd.DataFrame(rows).to_csv(FD+"F10_language_by_region.csv",index=False)
both(F10)
R("language_share",{"en":float((U.language=="en").mean()),"non_en":int((U.language!="en").sum())})
res=U[U.doc_class=="research_output"]
R("research",{"n":len(res),"peer_reviewed_share":float((res.publication_stage=="peer_reviewed").mean()),"with_openalex":int(res.oa_matched.fillna(False).astype(bool).sum()),"median_citations":float(res.oa_cited_by.dropna().median()) if res.oa_cited_by.notna().any() else None,"embodied_share":float(res.embodied_set.mean())})
ven=res[res.venue.notna()].groupby("venue").agg(n=("doc_id","size"),embodied=("embodied_set","sum"),median_citations=("oa_cited_by","median")).sort_values("n",ascending=False).head(25).reset_index()
write_table("T05_venues",ven,"Most frequent venues among research outputs (annotated venue field)")
# ---------- B6 category prevalence
cat_any={c:int(has(emb.embodied_categories,c).sum()) for c in EMB}; cat_prim=emb.primary_embodied_category.value_counts().to_dict()
R("category_any",cat_any); R("category_primary",cat_prim)
def F11(th):
    t=fs.setup(th); order=sorted(EMB,key=lambda c:-cat_any[c]); y=np.arange(len(order))
    fig,ax=plt.subplots(figsize=(7.2,5)); ax.barh(y-0.2,[cat_any[c] for c in order],height=0.38,color=t["cat"][0],label="Any mention")
    ax.barh(y+0.2,[cat_prim.get(c,0) for c in order],height=0.38,color=t["cat"][1],label="Primary category")
    ax.set_yticks(y); ax.set_yticklabels([f"{nice(c)}  [{L1[c].split(' ')[0]}]" for c in order],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel(f"Embodied-AI documents (n={len(emb)})"); ax.legend(loc="lower right")
    for yi,c in enumerate(order): ax.text(cat_any[c]+1,yi-0.2,str(cat_any[c]),va="center",fontsize=6.5,color=t["ink2"])
    ax.set_title("Embodied-AI categories addressed",loc="left"); fs.save(fig,"F11_categories",th)
    pd.DataFrame({"category":order,"level1":[L1[c] for c in order],"any_mention":[cat_any[c] for c in order],"primary":[cat_prim.get(c,0) for c in order]}).to_csv(FD+"F11_categories.csv",index=False)
both(F11)
TOPCAT=sorted(EMB,key=lambda c:-cat_any[c])[:16]
def F12(th):
    t=fs.setup(th); regs=[r for r in REGIONS if (emb.study_region==r).sum()>=15]
    mat=np.array([[has(emb[emb.study_region==r].embodied_categories,c).mean()*100 for r in regs] for c in TOPCAT])
    fig,ax=plt.subplots(figsize=(7.2,5.2)); heatmap(ax,mat,[nice(c) for c in TOPCAT],[f"{RSHORT[r]} (n={(emb.study_region==r).sum()})" for r in regs],t,fmt="{:.0f}",cbar_label="% of region's embodied documents")
    ax.set_title("Embodied categories by jurisdiction region (share of the region's embodied-AI documents)",loc="left"); fs.save(fig,"F12_categories_by_region",th)
    pd.DataFrame(mat,index=TOPCAT,columns=regs).round(1).reset_index().rename(columns={"index":"category"}).to_csv(FD+"F12_categories_by_region.csv",index=False)
both(F12)
def F13(th):
    t=fs.setup(th); cls=["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft","government_report_or_parliamentary","research_output","grey_literature","communication_or_news"]
    cls=[c for c in cls if (emb.doc_class==c).sum()>=10]
    mat=np.array([[has(emb[emb.doc_class==c].embodied_categories,k).mean()*100 for c in cls] for k in TOPCAT])
    fig,ax=plt.subplots(figsize=(7.2,5.2)); heatmap(ax,mat,[nice(c) for c in TOPCAT],[f"{DCL[c]} (n={(emb.doc_class==c).sum()})" for c in cls],t,cbar_label="% of class's embodied documents")
    ax.set_title("Embodied categories by document class",loc="left"); fs.save(fig,"F13_categories_by_class",th)
    pd.DataFrame(mat,index=TOPCAT,columns=cls).round(1).reset_index().rename(columns={"index":"category"}).to_csv(FD+"F13_categories_by_class.csv",index=False)
both(F13)
def F14(th):
    t=fs.setup(th); pers=["2015-2019","2020-2022","2023-2024","2025-2026"]; e=emb[emb.period.isin(pers)]
    mat=np.array([[has(e[e.period==p].embodied_categories,k).mean()*100 for p in pers] for k in TOPCAT])
    fig,ax=plt.subplots(figsize=(6.4,5.2)); heatmap(ax,mat,[nice(c) for c in TOPCAT],[f"{p} (n={(e.period==p).sum()})" for p in pers],t,cbar_label="% of period's embodied documents")
    ax.set_title("Embodied categories by publication period",loc="left"); fs.save(fig,"F14_categories_by_period",th)
    pd.DataFrame(mat,index=TOPCAT,columns=pers).round(1).reset_index().rename(columns={"index":"category"}).to_csv(FD+"F14_categories_by_period.csv",index=False)
both(F14)
# ---------- B7 co-occurrence
def cooc(df,col,labels):
    M=np.zeros((len(labels),len(labels)),dtype=int)
    for v in df[col]:
        s=[x for x in v.split("; ") if x in labels]
        for i in s:
            for j in s: M[labels.index(i),labels.index(j)]+=1
    return M
Mc=cooc(emb,"embodied_categories",TOPCAT)
def F16(th):
    t=fs.setup(th); M=Mc.astype(float).copy(); np.fill_diagonal(M,np.nan); M[np.triu_indices_from(M,1)]=np.nan
    fig,ax=plt.subplots(figsize=(7.2,6)); heatmap(ax,M,[nice(c) for c in TOPCAT],[nice(c) for c in TOPCAT],t,fmt="{:.0f}",cbar_label="documents mentioning both")
    ax.set_title("Co-occurrence of embodied categories within documents",loc="left"); fs.save(fig,"F16_category_cooccurrence",th)
    pd.DataFrame(Mc,index=TOPCAT,columns=TOPCAT).reset_index().rename(columns={"index":"category"}).to_csv(FD+"F16_category_cooccurrence.csv",index=False)
both(F16)
pairs=[]; N=len(emb)
for i in range(len(TOPCAT)):
    for j in range(i+1,len(TOPCAT)):
        n=Mc[i,j]; ni,nj=Mc[i,i],Mc[j,j]
        if n>=5: pairs.append(dict(category_a=TOPCAT[i],category_b=TOPCAT[j],together=int(n),lift=round(n*N/(ni*nj),2),jaccard=round(n/(ni+nj-n),2)))
t6=pd.DataFrame(pairs).sort_values("together",ascending=False).head(25); write_table("T06_category_pairs",t6,"Most frequent embodied-category pairs (lift = observed/expected under independence)")
TOPS=[k for k,_ in sorted({k:int(has(emb.governance_topics,k).sum()) for k in set(labels_of(emb.governance_topics))}.items(),key=lambda x:-x[1])[:16]]
Mt=cooc(emb,"governance_topics",TOPS)
def F17(th):
    t=fs.setup(th); M=Mt.astype(float).copy(); np.fill_diagonal(M,np.nan); M[np.triu_indices_from(M,1)]=np.nan
    fig,ax=plt.subplots(figsize=(7.2,6)); heatmap(ax,M,[nice(c) for c in TOPS],[nice(c) for c in TOPS],t,fmt="{:.0f}",cbar_label="documents addressing both")
    ax.set_title("Co-occurrence of governance topics in embodied-AI documents",loc="left"); fs.save(fig,"F17_topic_cooccurrence",th)
    pd.DataFrame(Mt,index=TOPS,columns=TOPS).reset_index().rename(columns={"index":"topic"}).to_csv(FD+"F17_topic_cooccurrence.csv",index=False)
both(F17)
R("topic_any_embodied",{k:int(has(emb.governance_topics,k).sum()) for k in TOPS})
# ---------- B8 governance gap
rs=emb[emb.doc_class=="research_output"]; gi=emb[emb.instrument]
rows=[]
for c in EMB:
    r_=has(rs.embodied_categories,c).mean()*100; g_=has(gi.embodied_categories,c).mean()*100
    rows.append(dict(category=c,level1=L1[c],research_pct=round(r_,1),n_research=int(has(rs.embodied_categories,c).sum()),instrument_pct=round(g_,1),n_instruments=int(has(gi.embodied_categories,c).sum()),binding_instruments=int(has(gi[gi.binding].embodied_categories,c).sum()),gap_index=round(r_-g_,1)))
t7=pd.DataFrame(rows).sort_values("gap_index",ascending=False); write_table("T07_governance_gap",t7,f"Governance-gap index per category: share among embodied research outputs (n={len(rs)}) minus share among embodied governance instruments (n={len(gi)})")
R("governance_gap",t7.to_dict("records"))
# v5: the same index with the instrument side split by collection source (round 1 web search vs round 2 database harvest), so that the round-2 search terms cannot masquerade as a gap
gi1=gi[~gi.round2]; gi2=gi[gi.round2]; rows=[]
for c in EMB:
    r_=has(rs.embodied_categories,c).mean()*100
    g1=has(gi1.embodied_categories,c).mean()*100 if len(gi1) else np.nan; g2=has(gi2.embodied_categories,c).mean()*100 if len(gi2) else np.nan
    rows.append(dict(category=c,level1=L1[c],research_pct=round(r_,1),n_research=int(has(rs.embodied_categories,c).sum()),
                     instrument_pct_round1=round(g1,1),n_instruments_round1=int(has(gi1.embodied_categories,c).sum()),gap_round1=round(r_-g1,1),
                     instrument_pct_round2=round(g2,1),n_instruments_round2=int(has(gi2.embodied_categories,c).sum()),gap_round2=round(r_-g2,1),
                     gap_all=round(r_-has(gi.embodied_categories,c).mean()*100,1)))
t7b=pd.DataFrame(rows).sort_values("gap_all",ascending=False)
write_table("T07b_governance_gap_by_source",t7b,f"Governance-gap index by collection source: research share (n={len(rs)}) minus the principal-instrument share among round-1 instruments (web search, n={len(gi1)}) and among round-2 instruments (database harvest, n={len(gi2)}); a gap present in both columns does not depend on the round-2 search terms")
R("governance_gap_by_source",t7b.to_dict("records"))
def F18(th):
    t=fs.setup(th); d=t7[(t7.n_research+t7.n_instruments)>=8].sort_values("research_pct",ascending=False); y=np.arange(len(d))
    fig,ax=plt.subplots(figsize=(7.2,4.6))
    for yi,(rp,gp) in enumerate(zip(d.research_pct,d.instrument_pct)): ax.plot([gp,rp],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.instrument_pct,y,color=t["cat"][1],s=40,zorder=3,label=f"Governance instruments (n={len(gi)})"); ax.scatter(d.research_pct,y,color=t["cat"][0],s=40,zorder=2,label=f"Research outputs (n={len(rs)})")
    ax.set_yticks(y); ax.set_yticklabels([nice(c) for c in d.category],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents mentioning the category (%)"); ax.legend(loc="lower right")
    ax.set_title("Research attention vs governance attention by embodied category",loc="left"); fs.save(fig,"F18_governance_gap",th); d.to_csv(FD+"F18_governance_gap.csv",index=False)
both(F18)
# ---------- B9 sectors
SEC=sorted(set(labels_of(U.application_sectors)),key=lambda s:-has(emb.application_sectors,s).sum())
def F19(th):
    t=fs.setup(th); e=[has(emb.application_sectors,s).mean()*100 for s in SEC]; g=[has(gen.application_sectors,s).mean()*100 for s in SEC]; y=np.arange(len(SEC))
    fig,ax=plt.subplots(figsize=(7.2,3.8))
    for yi,(ev,gv) in enumerate(zip(e,g)): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(g,y,color=t["cat"][1],s=38,zorder=2,label="General-AI set"); ax.scatter(e,y,color=t["cat"][0],s=38,zorder=3,label="Embodied-AI set")
    ax.set_yticks(y); ax.set_yticklabels([nice(s) for s in SEC]); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents addressing the sector (%)"); ax.legend(loc="lower right")
    ax.set_title("Application sectors by set",loc="left"); fs.save(fig,"F19_sectors",th)
    pd.DataFrame({"sector":SEC,"embodied_pct":np.round(e,1),"general_pct":np.round(g,1)}).to_csv(FD+"F19_sectors.csv",index=False)
both(F19)
R("sector_embodied",{s:float(has(emb.application_sectors,s).mean()) for s in SEC})
dump_results(); print("Part A done:",len(RESULTS),"result keys")
