"""v2 figures: redraw F01-F37 from the data twins written by 13-15 (and the master table where n is needed),
with the review fixes: titles that state the finding, n shown, small-n groups hatched or dropped (threshold stated),
no label collisions, monotone sequential ramps in dark mode, label dictionaries, consistent region names/order,
embodied = blue and general = orange throughout, dark ink on low-contrast fills."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts")
from analysis_common import *
from analysis_common import _lum
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
m=load(); u=m[m.usable]; emb=u[u.embodied_set]; gen=u[u.general_set]; U=u
MIN_N=30
INK_DARK={2,3,4}  # aqua, yellow, magenta need dark ink
def ink(j): return "#0b0b0b" if j in INK_DARK else "#ffffff"
def rd(name): return pd.read_csv(FD+name+".csv")
def both(fn):
    for th in ["light","dark"]: fn(th)
import textwrap
EMBL={"drones_uas":"drones and UAS","autonomous_road_vehicles":"automated road vehicles","industrial_manipulators":"industrial robot arms","collaborative_robots":"collaborative robots","mobile_industrial_logistics":"mobile and logistics robots","delivery_robots":"delivery robots","professional_service_robots":"professional service robots","domestic_household_robots":"domestic robots","social_companion_robots":"social and companion robots","educational_robots":"educational robots","care_assistive_robots":"care and assistive robots","toys_entertainment_robots":"toy and entertainment robots","sex_robots":"sex robots","surgical_medical_robots":"surgical and medical robots","rehabilitation_exoskeleton_prosthetic":"exoskeletons and prosthetics","biohybrid_or_cyborg":"biohybrid and cyborg systems","humanoid_general_purpose":"humanoid and general-purpose robots","autonomous_maritime_or_rail":"autonomous maritime and rail","agricultural_robots":"agricultural robots","space_or_extreme_environment":"space and extreme-environment robots","military_autonomous_weapons":"military autonomous weapons","security_policing_robots":"security and policing robots","other_embodied":"other embodied systems"}
def cl(c): return EMBL.get(c, lower1(nice(c)))
PLUR={"Binding law":"binding laws","Voluntary guidance / standard":"voluntary guidance documents and standards","Proposal or bill":"proposals and bills","Government report":"government reports","Research paper":"research papers","NGO / industry report":"NGO and industry reports","News / web page":"news and web pages"}
def title(ax_or_fig,main,sub,fs_main=10):
    main=main[:1].upper()+main[1:]
    w=int(118*9/fs_main) if fs_main>=9 else 118
    main="\n".join(textwrap.wrap(main,w)[:3]); sub="\n".join(textwrap.wrap(sub,int(w*1.15))[:2]); fs_main=min(fs_main,9.5)
    if hasattr(ax_or_fig,"set_title"): ax_or_fig.set_title(main+"\n"+sub,loc="left",fontsize=fs_main,fontweight="semibold")
    else: ax_or_fig.suptitle(main+"\n"+sub,x=0.02,ha="left",fontsize=fs_main,fontweight="semibold")
SETC=lambda t:(t["cat"][0],t["cat"][1])  # embodied blue, general orange
INSTC=["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"]
def joinl(xs):
    xs=list(xs); return xs[0] if len(xs)==1 else ", ".join(xs[:-1])+" and "+xs[-1]
def lower1(x): return x[:1].lower()+x[1:] if x[:2]!="AI" and x[:2]!="UN" and x[:2]!="EU" else x
DCO7=[k for k in DCO if k!="unusable"]
DCS={"governance_instrument_binding":"Binding law","governance_instrument_soft":"Voluntary guidance / standard","governance_proposal_or_draft":"Proposal or bill","government_report_or_parliamentary":"Government report","research_output":"Research paper","grey_literature":"NGO / industry report","communication_or_news":"News / web page"}
# slot order by class frequency: research (blue), news (orange), soft (aqua), gov report (yellow), proposals (magenta), binding (green), grey (violet)
CLASS_SLOT={"research_output":0,"communication_or_news":1,"governance_instrument_soft":2,"government_report_or_parliamentary":3,"governance_proposal_or_draft":4,"governance_instrument_binding":5,"grey_literature":6}

# ---------- F01
def F01(th):
    t=fs.setup(th); d=rd("F01_composition_by_set"); fig,ax=plt.subplots(figsize=(7.2,2.1)); sets=["Embodied-AI set","General-AI set"]
    for i,s in enumerate(sets):
        left=0; dd=d[d.set==s].set_index("doc_class")
        for k in DCO7:
            v=float(dd.loc[k,"share_pct"]) if k in dd.index else 0; j=CLASS_SLOT[k]
            ax.barh(i,v,left=left,color=t["cat"][j],height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=6: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7.5,color=ink(j))
            left+=v
    n_e=int(d[d.set=="Embodied-AI set"].n_total.iloc[0]); n_g=int(d[d.set=="General-AI set"].n_total.iloc[0])
    ax.set_yticks([0,1]); ax.set_yticklabels([f"Embodied-AI set (n={n_e})",f"General-AI set (n={n_g})"]); ax.set_xlim(0,100); ax.set_xlabel("Share of documents (%)"); ax.invert_yaxis(); ax.yaxis.grid(False)
    re_=float(d[(d.set=="Embodied-AI set")&(d.doc_class=="research_output")].share_pct.iloc[0]); rg=float(d[(d.set=="General-AI set")&(d.doc_class=="research_output")].share_pct.iloc[0])
    ie=float(d[(d.set=="Embodied-AI set")&d.doc_class.isin(INSTC)].share_pct.sum()); ig=float(d[(d.set=="General-AI set")&d.doc_class.isin(INSTC)].share_pct.sum()); ng_news=float(d[(d.set=="General-AI set")&(d.doc_class=="communication_or_news")].share_pct.sum())
    title(ax,f"Governance instruments are {ie:.0f}% of the embodied-AI set and research papers {re_:.0f}%; the general-AI set is {ig:.0f}% instruments and {ng_news:.0f}% news and web pages",f"Document class by analysis set (research: {re_:.0f}% vs {rg:.0f}%). Round 1 mirrored how the collection was built (robot sprint vs AI database); round 2 added instruments.",9.2)
    ax.legend([Patch(color=t["cat"][CLASS_SLOT[k]]) for k in DCO7],[DCS[k] for k in DCO7],ncol=4,loc="upper center",bbox_to_anchor=(0.5,-0.45),frameon=False,fontsize=7)
    fs.save(fig,"F01_composition_by_set",th)
both(F01)
# ---------- F02
def F02(th):
    t=fs.setup(th); Y=u[u.year.between(2014,2026)]; yrs=list(range(2014,2027)); e=[int((Y[Y.year==y].embodied_set).sum()) for y in yrs]; g=[int((Y[Y.year==y].general_set).sum()) for y in yrs]
    fig,ax=plt.subplots(figsize=(7.2,3)); ax.bar(yrs,e,color=t["cat"][0],width=0.5,label=f"Embodied-AI set (n={sum(e)})"); ax.bar(yrs,g,bottom=e,color=t["cat"][1],width=0.5,label=f"General-AI set (n={sum(g)})",edgecolor=t["surface"],linewidth=1)
    ax.set_xticks(yrs); ax.set_xticklabels([str(y) if y!=2026 else "2026*" for y in yrs],fontsize=8); ax.xaxis.grid(False); ax.set_ylabel("Documents"); ax.legend(loc="upper left")
    s23=100*(Y.year>=2023).mean(); pk=yrs[int(np.argmax(np.array(e)+np.array(g)))]
    title(ax,f"The collection is recent: {s23:.0f}% of dated documents are from 2023 or later, and {pk} is the largest year",f"Documents per publication year by set, 2014 to 2026 (* 2026 runs to October). Off-topic documents excluded.",9.5)
    fs.save(fig,"F02_timeline",th); pd.DataFrame({"year":yrs,"embodied":e,"general":g}).to_csv(FD+"F02_timeline.csv",index=False)
both(F02)
# ---------- F03
def F03(th):
    t=fs.setup(th); d=rd("F03_issuer_types"); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,3.6))
    for yi,(ev,gv) in enumerate(zip(d.embodied_pct,d.general_pct)): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.general_pct,y,color=t["cat"][1],s=38,zorder=2,label=f"General-AI set (n={len(gen)})"); ax.scatter(d.embodied_pct,y,color=t["cat"][0],s=38,zorder=3,label=f"Embodied-AI set (n={len(emb)})")
    ax.set_yticks(y); ax.set_yticklabels([lab(i) for i in d.issuer_type]); ax.invert_yaxis(); ax.set_xlabel("Share of documents (%)"); ax.yaxis.grid(False); ax.legend(loc="lower right")
    te=d.sort_values("embodied_pct",ascending=False).head(2); tg=d.sort_values("general_pct",ascending=False).head(2)
    title(ax,f"{joinl(lower1(lab(i)) for i in te.issuer_type)} issue {te.embodied_pct.sum():.0f}% of embodied-AI documents; {joinl(lower1(lab(i)) for i in tg.issuer_type)} issue {tg.general_pct.sum():.0f}% of general-AI ones",
          "Issuer type by analysis set",9.2); fs.save(fig,"F03_issuer_types",th)
both(F03)
# ---------- F04
def F04(th):
    t=fs.setup(th); d=rd("F04_lifecycle_binding"); fig,axes=plt.subplots(1,2,figsize=(7.4,3.4),gridspec_kw={"width_ratios":[1.3,1]})
    ST=["proposal_or_concept","draft_or_bill_under_consideration","consultation_open","adopted_not_yet_in_force","in_force","published_current","under_development","superseded_or_repealed","unknown"]
    STL={"proposal_or_concept":"Proposal","draft_or_bill_under_consideration":"Bill / draft","consultation_open":"Consultation","adopted_not_yet_in_force":"Adopted, not in force","in_force":"In force","published_current":"Published, current","under_development":"Under development","superseded_or_repealed":"Superseded / repealed","unknown":"Unknown"}
    ramp=[fs.SEQ[i] for i in (1,2,3,5,7,9,11)]; cols={s:(ramp[i] if i<7 else t["muted"]) for i,s in enumerate(ST)}; cols["unknown"]=t["axis"]
    ax=axes[0]; ns={}
    for i,s_ in enumerate(["Embodied-AI set","General-AI set"]):
        dd=d[(d.set==s_)&(~d.status.str.startswith("binding:"))].set_index("status"); left=0; ns[s_]=int(dd.n.sum())
        for st in ST:
            v=float(dd.loc[st,"pct"]) if st in dd.index else 0; nn=int(dd.loc[st,"n"]) if st in dd.index else 0
            ax.barh(i,v,left=left,color=cols[st],height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=9: ax.text(left+v/2,i,f"{v:.0f}% ({nn})",ha="center",va="center",fontsize=6.5,color="#ffffff" if _lum(cols[st]) <0.18 else "#0b0b0b")
            left+=v
    ax.set_yticks([0,1]); ax.set_yticklabels([f"Embodied (n={ns['Embodied-AI set']})",f"General (n={ns['General-AI set']})"]); ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of governance documents (%)"); ax.set_title("Lifecycle status (ordered, light to dark)",loc="left",fontsize=8.5)
    ax.legend([Patch(color=cols[s]) for s in ST],[STL[s] for s in ST],ncol=3,loc="upper left",bbox_to_anchor=(0,-0.36),frameon=False,fontsize=6.3,title="Lifecycle status",title_fontsize=6.5); ax.set_xlim(0,105)
    ax=axes[1]; BN=["legally_binding","voluntary_soft_law","technical_standard_voluntary","not_applicable"]; bc=[t["cat"][5],t["cat"][2],t["cat"][6],t["muted"]]; BNL=["Legally binding","Voluntary soft law","Technical standard","Not applicable (drafts)"]
    for i,s_ in enumerate(["Embodied-AI set","General-AI set"]):
        dd=d[(d.set==s_)&(d.status.str.startswith("binding:"))].copy(); dd["b"]=dd.status.str.replace("binding:",""); dd=dd.set_index("b"); left=0
        for j,b in enumerate(BN):
            v=float(dd.loc[b,"pct"]) if b in dd.index else 0; nn=int(dd.loc[b,"n"]) if b in dd.index else 0
            ax.barh(i,v,left=left,color=bc[j],height=0.55,edgecolor=t["surface"],linewidth=1.5)
            if v>=9: ax.text(left+v/2,i,f"{v:.0f}% ({nn})",ha="center",va="center",fontsize=6.5,color="#0b0b0b" if j==1 else "#ffffff")
            left+=v
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_yticks([0,1]); ax.set_yticklabels([]); ax.set_xlabel("Share (%)"); ax.set_title("Binding nature",loc="left",fontsize=8.5)
    ax.legend([Patch(color=c) for c in bc],BNL,ncol=1,loc="upper left",bbox_to_anchor=(0,-0.36),frameon=False,fontsize=6.3,title="Binding nature",title_fontsize=6.5); ax.set_xlim(0,105)
    def bshare(s_,b): 
        dd=d[(d.set==s_)&(d.status=="binding:"+b)]; return float(dd.pct.iloc[0]) if len(dd) else 0.0
    def lshare(s_,sts):
        dd=d[(d.set==s_)&d.status.isin(sts)]; return float(dd.pct.sum())
    title(fig,f"{bshare('Embodied-AI set','legally_binding'):.0f}% of embodied-AI governance documents are legally binding and {bshare('Embodied-AI set','technical_standard_voluntary'):.0f}% are technical standards; general-AI governance is {bshare('General-AI set','voluntary_soft_law'):.0f}% voluntary soft law and {lshare('General-AI set',['proposal_or_concept','draft_or_bill_under_consideration','consultation_open']):.0f}% still at proposal, bill or consultation stage",
          "Governance documents by lifecycle status and binding nature; segment labels show share (count)",9)
    fig.subplots_adjust(top=0.76,bottom=0.42,wspace=0.12)
    fs.save(fig,"F04_lifecycle_binding",th)
both(F04)
# ---------- F05
def F05(th):
    t=fs.setup(th); d=rd("F05_embodied_share_by_year"); fig,ax=plt.subplots(figsize=(7.2,3.1))
    ax.fill_between(d.year,d.ci_low,d.ci_high,color=t["cat"][0],alpha=0.15,linewidth=0); ax.plot(d.year,d.share_pct,color=t["cat"][0],lw=1.8)
    big=d.n>=MIN_N; ax.scatter(d.year[big],d.share_pct[big],color=t["cat"][0],s=28,zorder=3,label=f"year with at least {MIN_N} documents"); ax.scatter(d.year[~big],d.share_pct[~big],facecolors=t["surface"],edgecolors=t["cat"][0],s=28,zorder=3,label=f"fewer than {MIN_N} documents")
    ax.set_ylim(0,100); ax.set_ylabel("Embodied-AI share of the year's documents (%)"); ax.xaxis.grid(False); ax.set_xticks(d.year); ax.set_xticklabels([str(y) if y!=2026 else "2026*" for y in d.year],fontsize=8)
    for y,nn in zip(d.year,d.n): ax.text(y,3,f"{nn}",ha="center",fontsize=6.5,color=t["ink2"])
    ax.text(d.year.iloc[0]-0.4,3,"n:",ha="right",fontsize=6.5,color=t["ink2"]); ax.legend(loc="upper right",fontsize=7)
    dd=d[d.n>=MIN_N]; y0,y1=int(dd.year.iloc[0]),int(dd.year.iloc[-1]); s0,s1=float(dd.share_pct.iloc[0]),float(dd.share_pct.iloc[-1]); smin=dd.loc[dd.share_pct.idxmin()]
    title(ax,f"The embodied share of each year's documents is {s0:.0f}% in {y0} and {s1:.0f}% in {y1}, with its low point in {int(smin.year)} ({smin.share_pct:.0f}%) when general-AI material peaked",f"Share with 95% Wilson band; absolute embodied counts by year are in F02. * 2026 to October.",9)
    fs.save(fig,"F05_embodied_share_by_year",th)
both(F05)
# ---------- F06
def F06(th):
    t=fs.setup(th); d=rd("F06_cumulative_instruments"); d=d[d.year>=2014]; fig,ax=plt.subplots(figsize=(7.2,3.2))
    cols={"Legally binding":t["cat"][5],"Voluntary soft law":t["cat"][2],"Technical standards":t["cat"][6],"Drafts and proposals":t["muted"]}
    order=sorted(cols,key=lambda c:-d[c].iloc[-1]); ymax=max(d[c].iloc[-1] for c in cols); step=max(1.6,ymax*0.06); ypos={}; last=None
    for c in sorted(cols,key=lambda c:d[c].iloc[-1]):
        yv=float(d[c].iloc[-1]); yv=yv if last is None else max(yv,last+step); ypos[c]=yv; last=yv
    for c in order:
        ax.step(d.year,d[c],where="post",color=cols[c],lw=1.8); ax.text(d.year.iloc[-1]+0.3,ypos[c],f"{c} ({int(d[c].iloc[-1])})",va="center",fontsize=7,color=t["ink"])
        if abs(ypos[c]-d[c].iloc[-1])>0.3: ax.plot([d.year.iloc[-1],d.year.iloc[-1]+0.28],[d[c].iloc[-1],ypos[c]],color=t["axis"],lw=0.6)
    ax.set_xlim(2014,2029.5); ax.set_ylabel("Cumulative documents (dated)"); ax.xaxis.grid(False); ax.set_xticks(list(range(2014,2027))); ax.set_xticklabels([str(y) if y%2==0 else "" for y in range(2014,2027)],fontsize=8)
    nb=int(d["Legally binding"].iloc[-1]); nsft=int(d["Voluntary soft law"].iloc[-1]); nt=int(d["Technical standards"].iloc[-1]); half=d[d["Legally binding"]>=nb/2].year.iloc[0]
    title(ax,f"Binding law reaching robots accumulates steadily: {nb} dated binding instruments by 2026, half of them since {int(half)}; voluntary guidance ({nsft}) and standards ({nt}) accumulate alongside","Cumulative embodied-AI governance documents by binding nature (documents without a recoverable year are not plotted)",9)
    fs.save(fig,"F06_cumulative_instruments",th)
both(F06)
# ---------- F07
def F07(th):
    t=fs.setup(th); d=rd("F07_region_counts"); regs=list(d.region); y=np.arange(len(regs)); fig,axes=plt.subplots(1,2,figsize=(7.4,3.4),gridspec_kw={"width_ratios":[1.4,1]})
    ax=axes[0]; ax.barh(y-0.2,d.embodied,height=0.38,color=t["cat"][0],label="Embodied-AI set"); ax.barh(y+0.2,d.general,height=0.38,color=t["cat"][1],label="General-AI set")
    ax.set_yticks(y); ax.set_yticklabels([f"{RSHORT[r]} (n={n})" for r,n in zip(regs,d.n_usable)],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Documents"); ax.legend(loc="lower right",fontsize=7)
    ax=axes[1]; ci=[wilson(e,n) for e,n in zip(d.embodied,d.n_usable)]
    ax.barh(y,d.embodied_share_pct,height=0.55,color=t["cat"][0]); ax.errorbar(d.embodied_share_pct,y,xerr=[[s-c[0]*100 for s,c in zip(d.embodied_share_pct,ci)],[c[1]*100-s for s,c in zip(d.embodied_share_pct,ci)]],fmt="none",ecolor=t["ink2"],elinewidth=0.8,capsize=2)
    ax.set_yticks(y); ax.set_yticklabels([]); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Embodied share (%), 95% Wilson interval")
    hi=d.loc[d.embodied_share_pct.idxmax()]; lo=d.loc[d.embodied_share_pct.idxmin()]
    title(fig,f"Europe supplies {d.n_usable.iloc[0]/d.n_usable.sum()*100:.0f}% of the documents; the embodied share is highest in {RSHORT.get(hi.region,hi.region)} ({hi.embodied_share_pct:.0f}%) and lowest in {RSHORT.get(lo.region,lo.region)} ({lo.embodied_share_pct:.0f}%)",f"Documents by jurisdiction region (n={int(d.n_usable.sum())} usable documents with a known region)",9)
    fs.save(fig,"F07_region_counts",th)
both(F07)
# ---------- F08
def F08(th):
    t=fs.setup(th); d=pd.read_csv(TD+"T04_countries.csv").sort_values("embodied",ascending=False).head(20); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,5.2))
    ax.barh(y,d.embodied,color=t["cat"][0],height=0.66)
    for yi,(_,r) in enumerate(d.iterrows()): ax.text(r.embodied+1,yi,f"{int(r.embodied)}  ·  {int(r.embodied_instruments_principal)} principal embodied instrument{'s' if r.embodied_instruments_principal!=1 else ''}, {int(r.binding_embodied)} binding",va="center",fontsize=6.8,color=t["ink2"])
    ax.set_yticks(y); ax.set_yticklabels([f"{c}  " for c in d.country_name],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Embodied-AI documents (any type)"); ax.set_xlim(0,d.embodied.max()*1.9)
    for yi,r in enumerate(d.region): ax.text(-1,yi,RSHORT.get(r,r),ha="right",va="center",fontsize=6,color=t["muted"],transform=ax.get_yaxis_transform(),clip_on=False) if False else None
    tp=d.sort_values("embodied_instruments_principal",ascending=False).iloc[0]
    title(ax,f"{tp.country_name} has the most principal embodied instruments ({int(tp.embodied_instruments_principal)}); document counts still measure the collectors' and databases' reach as much as national activity","Top 20 national jurisdictions by embodied-AI documents (any document type), with principal instruments in the embodied set and the binding ones among them",8.8)
    fs.save(fig,"F08_top_countries",th); d.to_csv(FD+"F08_top_countries.csv",index=False)
both(F08)
# ---------- F10
def F10(th):
    t=fs.setup(th); d=rd("F10_language_by_region"); regs=[r for r in REGIONS if r in set(d.region)]; groups=list(dict.fromkeys(d.language_group)); fig,ax=plt.subplots(figsize=(7.2,3.4))
    for i,r in enumerate(regs):
        dd=d[d.region==r].set_index("language_group"); left=0; n=int(dd.n.sum())
        for j,g in enumerate(groups):
            v=float(dd.loc[g,"pct"]) if g in dd.index else 0; col=t["cat"][j] if j<5 else t["muted"]
            ax.barh(i,v,left=left,color=col,height=0.6,edgecolor=t["surface"],linewidth=1.2)
            if v>=10: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color=ink(j))
            left+=v
    ax.set_yticks(range(len(regs))); ax.set_yticklabels([f"{RSHORT[r]} (n={int(d[d.region==r].n.sum())})" for r in regs],fontsize=7.5)
    ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents (%)")
    ax.legend([Patch(color=t["cat"][j] if j<5 else t["muted"]) for j in range(len(groups))],groups,ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.22),frameon=False,fontsize=7)
    en={r:float(d[(d.region==r)&(d.language_group=="English")].pct.sum()) for r in regs}; local=[RSHORT[r] for r in regs if en[r]<50]; cjk=float(d[d.language_group.str.contains("Chinese|Japanese|Korean",regex=True)].n.sum())
    title(ax,f"Local-language documents dominate in {joinl(local) if local else 'no region'}; English dominates elsewhere",f"Document language by jurisdiction region (international bodies excluded); {int(cjk)} documents are in Chinese, Japanese or Korean",9)
    fs.save(fig,"F10_language_by_region",th)
both(F10)
# ---------- F11
def F11(th):
    t=fs.setup(th); d=rd("F11_categories"); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,5.2))
    ax.barh(y-0.2,d.any_mention,height=0.38,color=t["cat"][0],label="Mentioned (any)"); ax.barh(y+0.2,d.primary,height=0.38,color=t["cat"][1],label="Main category of the document")
    ax.set_yticks(y); ax.set_yticklabels([f"{nice(c)}  ·  {l1}" for c,l1 in zip(d.category,d.level1)],fontsize=7.2); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel(f"Embodied-AI documents (n={len(emb)})"); ax.legend(loc="lower right")
    for yi,v in enumerate(d.any_mention): ax.text(v+1.5,yi-0.2,str(int(v)),va="center",fontsize=6.5,color=t["ink2"])
    top=d.sort_values("any_mention",ascending=False); 
    title(ax,f"{joinl(cl(c) for c in top.category.head(3))} are the most-addressed robot types; {joinl(cl(c) for c in top.category.tail(3))} barely appear","Robot types addressed by embodied-AI documents (a document can mention several types)",9)
    fs.save(fig,"F11_categories",th)
both(F11)
# ---------- F12-F14 heatmaps with shared scale and small-n hatching
TOPCAT=list(rd("F12_categories_by_region").category)
def cat_heat(th,name,groups,gsel,glabel,main,sub,vmax=50,figsize=(7.2,5.4)):
    t=fs.setup(th); mats=[]; cols=[]; small=[]
    for gi,g in enumerate(groups):
        d=gsel(g); n=len(d)
        if n<10: continue
        mats.append([has(d.embodied_categories,c).mean()*100 for c in TOPCAT]); cols.append(f"{glabel(g)}\n(n={n})")
        if n<MIN_N: small.append(len(cols)-1)
    mat=np.array(mats).T; fig,ax=plt.subplots(figsize=figsize)
    heatmap(ax,mat,[nice(c) for c in TOPCAT],cols,t,fmt="{:.0f}",vmin=0,vmax=vmax,cbar_label="% of group's embodied documents",small_cols=small)
    ax.tick_params(axis="x",labelsize=7)
    title(ax,main,sub+(f"; hatched columns have fewer than {MIN_N} documents" if small else ""),8.8); fs.save(fig,name,th)
    return mat,cols
def F12(th):
    regs=[r for r in REGIONS if (emb.study_region==r).sum()>=10]
    cat_heat(th,"F12_categories_by_region",regs,lambda r:emb[emb.study_region==r],lambda r:RSHORT[r],
             "; ".join(f"{cl(c)} peak in {RSHORT[max(regs,key=lambda r: has(emb[emb.study_region==r].embodied_categories,c).mean())]}" for c in TOPCAT[:4]),"Robot types by jurisdiction region, as a share of the region's embodied-AI documents (shared 0-50% scale with F13 and F14)")
both(F12)
def F13(th):
    cls=[c for c in DCO7 if (emb.doc_class==c).sum()>=10]
    cat_heat(th,"F13_categories_by_class",cls,lambda c:emb[emb.doc_class==c],lambda c:DCS[c],
             "; ".join(f"{PLUR[DCS[c]]} are mostly about {cl(max(TOPCAT,key=lambda k: has(emb[emb.doc_class==c].embodied_categories,k).mean()))}" for c in ["research_output","governance_instrument_binding","governance_instrument_soft"] if c in cls),"Robot types by document class, as a share of the class's embodied-AI documents (classes with fewer than 10 documents omitted)")
both(F13)
def F14(th):
    pers=["2015-2019","2020-2022","2023-2024","2025-2026"]
    cat_heat(th,"F14_categories_by_period",pers,lambda p:emb[emb.period==p],lambda p:p if p!="2025-2026" else "2025-2026*",
             (lambda ch: f"Within the embodied set, {joinl(cl(c) for c,_ in ch[:2])} rise most after 2024 while {joinl(cl(c) for c,_ in ch[-2:])} recede")(sorted(((c,has(emb[emb.period=="2025-2026"].embodied_categories,c).mean()-has(emb[emb.period=="2020-2022"].embodied_categories,c).mean()) for c in TOPCAT),key=lambda z:-z[1])),"Robot types by publication period, as a share of the period's embodied-AI documents (* 2026 to October)",figsize=(6.4,5.4))
both(F14)
# ---------- F16 / F17 co-occurrence (lower triangle, diagonal n in muted ink)
def cooc_fig(th,name,csv,keycol,labf,main,sub,cbar):
    t=fs.setup(th); d=pd.read_csv(FD+csv).set_index(keycol); keys=list(d.index); M=d.values.astype(float); diag=np.diag(M).copy()
    L=M.copy(); L[np.triu_indices_from(L,0)]=np.nan
    fig,ax=plt.subplots(figsize=(7.4,6.2)); heatmap(ax,L[1:,:-1],[labf(k) for k in keys[1:]],[labf(k) for k in keys[:-1]],t,fmt="{:.0f}",vmin=0,cbar_label=cbar)
    for i,k in enumerate(keys[1:]): ax.text(i+0.5,i,f"n={int(diag[i+1])}",fontsize=6,color=t["muted"],va="center",ha="left")
    ax.tick_params(axis="x",labelsize=7); ax.tick_params(axis="y",labelsize=7)
    title(ax,main,sub,8.8); fs.save(fig,name,th)
def top_pairs(csv,keycol,labf,k=2):
    d=pd.read_csv(FD+csv).set_index(keycol); M=d.values.astype(float); keys=list(d.index); out=[]
    for i in range(len(keys)):
        for j in range(i): out.append((M[i,j],keys[i],keys[j]))
    out.sort(reverse=True); return joinl(f"{lower1(labf(a))} with {lower1(labf(b))} ({int(n)})" for n,a,b in out[:k])
def F16(th): cooc_fig(th,"F16_category_cooccurrence","F16_category_cooccurrence.csv","category",nice,f"The robot types most often addressed together: {top_pairs('F16_category_cooccurrence.csv','category',nice)}","Documents mentioning both robot types (lower triangle; n = documents mentioning the row type)","documents mentioning both")
def F17(th): cooc_fig(th,"F17_topic_cooccurrence","F17_topic_cooccurrence.csv","topic",lab,f"The topics most often addressed together: {top_pairs('F17_topic_cooccurrence.csv','topic',lab)}","Embodied-AI documents addressing both topics (lower triangle)","documents addressing both")
both(F16); both(F17)
# ---------- F18 dumbbell with counts, small-n greyed
def F18(th):
    t=fs.setup(th); d=rd("F18_governance_gap"); d=d[(d.n_research+d.n_instruments)>=8].sort_values("research_pct",ascending=False); y=np.arange(len(d)); n_r=int(pd.read_csv(TD+"T07_governance_gap.csv").n_research.max()*0+len(emb[emb.doc_class=="research_output"])); n_i=int(emb.instrument.sum())
    fig,ax=plt.subplots(figsize=(7.4,4.8))
    for yi,(_,r) in enumerate(d.iterrows()):
        ax.plot([r.instrument_pct,r.research_pct],[yi,yi],color=t["grid"],lw=2,zorder=1)
        small=r.n_instruments<5
        ax.scatter([r.instrument_pct],[yi],facecolors=t["surface"] if small else t["cat"][1],edgecolors=t["cat"][1],s=40,zorder=3)
        ax.scatter([r.research_pct],[yi],color=t["cat"][0],s=40,zorder=2)
        ax.text(max(r.instrument_pct,r.research_pct)+1.5,yi,f"{int(r.n_research)} papers · {int(r.n_instruments)} instruments",va="center",fontsize=6.3,color=t["muted"])
    ax.set_yticks(y); ax.set_yticklabels([nice(c) for c in d.category],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents mentioning the robot type (%)"); ax.set_xlim(0,max(d.research_pct.max(),d.instrument_pct.max())+28)
    ax.legend(handles=[Line2D([],[],marker="o",color=t["cat"][0],lw=0,label=f"Research papers (n={n_r})"),Line2D([],[],marker="o",color=t["cat"][1],lw=0,label=f"Governance instruments (n={n_i})"),Line2D([],[],marker="o",markerfacecolor=t["surface"],markeredgecolor=t["cat"][1],lw=0,label="fewer than 5 instruments")],loc="lower right",fontsize=7)
    tr=d.sort_values("research_pct",ascending=False).iloc[0]; ti=d.sort_values("instrument_pct",ascending=False).head(2)
    title(ax,f"Researchers study {cl(tr.category)} ({tr.research_pct:.0f}% of papers); principal instruments address {joinl(cl(c) for c in ti.category)} ({ti.instrument_pct.iloc[0]:.0f}% and {ti.instrument_pct.iloc[1]:.0f}%)","Share of embodied research papers vs share of principal embodied governance instruments mentioning each robot type (see F40 for intervals)",9)
    fs.save(fig,"F18_governance_gap",th)
both(F18)
# ---------- F19
def F19(th):
    t=fs.setup(th); d=rd("F19_sectors"); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,3.9))
    for yi,(ev,gv) in enumerate(zip(d.embodied_pct,d.general_pct)): ax.plot([gv,ev],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.general_pct,y,color=t["cat"][1],s=38,zorder=2,label=f"General-AI set (n={len(gen)})"); ax.scatter(d.embodied_pct,y,color=t["cat"][0],s=38,zorder=3,label=f"Embodied-AI set (n={len(emb)})")
    ax.set_yticks(y); ax.set_yticklabels([lab(s) for s in d.sector]); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents addressing the sector (%)"); ax.legend(loc="lower right")
    te=d.sort_values("embodied_pct",ascending=False).head(3); tg=d.sort_values("general_pct",ascending=False).head(2)
    title(ax,f"Embodied documents are about {joinl(lower1(lab(x)) for x in te.sector)}; general-AI documents are about {joinl(lower1(lab(x)) for x in tg.sector)}","Application sectors by analysis set",9); fs.save(fig,"F19_sectors",th)
both(F19)
# ---------- F20
def F20(th):
    t=fs.setup(th); d=rd("F20_principles_by_set"); d=d.sort_values("embodied_any_pct",ascending=False); y=np.arange(len(d)); fig,axes=plt.subplots(1,2,figsize=(8.6,5.2),sharey=True)
    for ax,(ec,gc,ttl,xmax) in zip(axes,[("embodied_any_pct","general_any_pct","Mentioned at all (level 1 or 2)",100),("embodied_substantive_pct","general_substantive_pct","Treated in depth (level 2)",50)]):
        for yi,(e,g) in enumerate(zip(d[ec],d[gc])): ax.plot([g,e],[yi,yi],color=t["grid"],lw=2,zorder=1)
        ax.scatter(d[gc],y,color=t["cat"][1],s=30,zorder=2,label=f"General-AI set (n={len(gen)})"); ax.scatter(d[ec],y,color=t["cat"][0],s=30,zorder=3,label=f"Embodied-AI set (n={len(emb)})")
        ax.set_xlim(0,xmax); ax.set_xlabel("Share of documents (%)"); ax.set_title(ttl,loc="left",fontsize=9); ax.yaxis.grid(False)
    axes[0].set_yticks(y); axes[0].set_yticklabels([f"{l}{'' if s else ' (n.s.)'}" for l,s in zip(d.label,d.significant_holm_05)],fontsize=7.5); axes[0].invert_yaxis(); axes[0].legend(loc="lower right",fontsize=7)
    ns=[l for l,s in zip(d.label,d.significant_holm_05) if not s]
    dd=d.assign(diff=d.embodied_any_pct-d.general_any_pct).sort_values("diff")
    title(fig,f"Embodied-AI documents lean toward {joinl(lower1(x) for x in dd.label.tail(3)[::-1])}; general-AI documents toward {joinl(lower1(x) for x in dd.label.head(3))}",f"Principle salience by set; all differences are Holm-significant except: {', '.join(ns) if ns else 'none'}. Pooled comparison: see F39 for the within-genre version.",9)
    fs.save(fig,"F20_principles_by_set",th)
both(F20)
# ---------- F21 / F22 heatmaps
def pr_heat(th,name,groups,gsel,glabel,main,sub,level=1,figsize=(7.4,6.4)):
    t=fs.setup(th); mats=[]; cols=[]; small=[]
    for g in groups:
        d=gsel(g); n=len(d)
        if n<10: continue
        mats.append([(d["pr_"+p]>=level).mean()*100 for p in PR]); cols.append(f"{glabel(g)}\n(n={n})")
        if n<MIN_N: small.append(len(cols)-1)
    mat=np.array(mats).T; fig,ax=plt.subplots(figsize=figsize)
    heatmap(ax,mat,[PRL[p] for p in PR],cols,t,fmt="{:.0f}",vmin=0,vmax=100 if level==1 else 60,cbar_label="% of group's embodied documents",small_cols=small)
    ax.axhline(13.5,color=t["ink"],lw=0.8); ax.tick_params(axis="x",labelsize=7); ax.tick_params(axis="y",labelsize=7)
    title(ax,main,sub+(f"; hatched: fewer than {MIN_N} documents" if small else ""),8.6); fs.save(fig,name,th)
def F21(th):
    regs=[r for r in REGIONS if (emb.study_region==r).sum()>=10]
    pr_heat(th,"F21_principles_by_region",regs,lambda r:emb[emb.study_region==r],lambda r:RSHORT[r],(lambda rng: f"{joinl(lower1(PRL[p]) for p,_ in rng[:2])} look alike across regions; {joinl(lower1(PRL[p]) for p,_ in rng[-3:])} vary most")(sorted(((p,max((emb[emb.study_region==r]["pr_"+p]>=1).mean() for r in regs)-min((emb[emb.study_region==r]["pr_"+p]>=1).mean() for r in regs)) for p in PR),key=lambda z:z[1])).capitalize(),"Principle presence (level 1 or 2) by jurisdiction region, embodied-AI documents; core principles above the line, embodied-specific below")
def F22(th):
    cls=[c for c in DCO7 if (emb.doc_class==c).sum()>=10]
    pr_heat(th,"F22_principles_by_class",cls,lambda c:emb[emb.doc_class==c],lambda c:DCS[c],"In-depth treatment follows genre: "+"; ".join(f"{PLUR[DCS[c]]} treat {lower1(PRL[max(PR,key=lambda p:(emb[emb.doc_class==c]['pr_'+p]>=2).mean())])} most" for c in ["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft","research_output"] if c in cls),"Substantive treatment (level 2) by document class, embodied-AI documents (classes with fewer than 10 documents omitted)",level=2)
both(F21); both(F22)
# ---------- F23: embodied-specific considerations by instrument type (content-analysed captures only)
def F23(th):
    t=fs.setup(th); content=emb[emb.content_capture&emb.words_ok]
    groups=[("Binding law",content[content.doc_class=="governance_instrument_binding"]),("Voluntary guidance",content[(content.doc_class=="governance_instrument_soft")&(content.doc_type!="technical_standard")]),("Technical standards",content[content.doc_type=="technical_standard"]),("Proposals / drafts",content[content.doc_class=="governance_proposal_or_draft"]),("Government reports",content[content.doc_class=="government_report_or_parliamentary"]),("Research papers",content[content.doc_class=="research_output"])]
    groups=[(g,d) for g,d in groups if len(d)>=3]
    fig,axes=plt.subplots(2,3,figsize=(11.5,6),sharex=True); fig.subplots_adjust(wspace=0.85,hspace=0.45,top=0.85,left=0.14,right=0.98); rows=[]
    for ax,p in zip(axes.flat,PR_EMB):
        y=np.arange(len(groups))
        for yi,(g,d) in enumerate(groups):
            a=(d["pr_"+p]>=1).mean()*100; s2=(d["pr_"+p]>=2).mean()*100; n=len(d)
            ax.barh(yi,a,color=t["cat"][0],alpha=0.35,height=0.7); ax.barh(yi,s2,color=t["cat"][0],height=0.7)
            ax.text(min(a,100)+2,yi,f"{int(round(a*n/100))}/{n}" if n<MIN_N else f"{a:.0f}%",va="center",fontsize=6.3,color=t["ink2"],clip_on=False)
            rows.append(dict(principle=p,group=g,n=n,any_pct=round(a,1),substantive_pct=round(s2,1),n_any=int(round(a*n/100)),n_substantive=int(round(s2*n/100))))
        ax.set_yticks(y); ax.set_yticklabels([f"{g} (n={len(d)})" for g,d in groups],fontsize=7); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlim(0,100); ax.set_xticks([0,25,50,75,100]); ax.set_title(PRL[p],loc="left",fontsize=8.5)
    for ax in axes[1]: ax.set_xlabel("% of documents (light: mentioned; dark: treated in depth)",fontsize=7.5)
    R=pd.DataFrame(rows); ps=R[R.principle=="physical_safety"].sort_values("substantive_pct",ascending=False); dep=R.groupby("principle").substantive_pct.mean().sort_values(); gap=(R.groupby("principle").any_pct.mean()-R.groupby("principle").substantive_pct.mean()).sort_values()
    title(fig,f"Physical safety is specified in depth most often ({joinl(g.lower() for g in ps.group.head(2))} lead); {lower1(PRL[dep.index[0]])} is specified in depth least often, and {lower1(PRL[gap.index[-1]])} shows the widest gap between mention and depth","Embodied-specific considerations by document type, content-analysed captures with at least 150 words (catalogue and landing pages excluded); counts shown where n < 30",8.8)
    fs.save(fig,"F23_embodied_principles_by_type",th); pd.DataFrame(rows).to_csv(FD+"F23_embodied_principles_by_type.csv",index=False)
both(F23)
# ---------- F24 two panels
def F24(th):
    t=fs.setup(th); d=rd("F24_mechanisms_by_set"); d=d.sort_values("embodied_instruments_pct",ascending=False); y=np.arange(len(d)); fig,axes=plt.subplots(1,2,figsize=(9.2,5.4),sharey=True)
    gi_e=int(emb.instrument.sum()); gi_g=int(gen.instrument.sum())
    for ax,(ec,gc,ttl,ne,ng) in zip(axes,[("embodied_instruments_pct","general_instruments_pct","Governance instruments only",gi_e,gi_g),("embodied_pct","general_pct","All documents (genre-confounded)",len(emb),len(gen))]):
        for yi,(e,g) in enumerate(zip(d[ec],d[gc])): ax.plot([g,e],[yi,yi],color=t["grid"],lw=2,zorder=1)
        ax.scatter(d[gc],y,color=t["cat"][1],s=30,zorder=2,label=f"General-AI (n={ng})"); ax.scatter(d[ec],y,color=t["cat"][0],s=30,zorder=3,label=f"Embodied-AI (n={ne})")
        ax.set_xlabel("Share using the mechanism (%)"); ax.set_title(ttl,loc="left",fontsize=9); ax.yaxis.grid(False); ax.legend(loc="lower right",fontsize=7); ax.set_xlim(0,100)
    axes[0].set_yticks(y); axes[0].set_yticklabels([lab(x) for x in d.mechanism],fontsize=7.5); axes[0].invert_yaxis()
    dd=d.assign(diff=d.embodied_instruments_pct-d.general_instruments_pct).sort_values("diff")
    title(fig,f"Robot rules lean on {joinl(lower1(lab(x)) for x in dd.mechanism.tail(3)[::-1])}; AI rules lean on {joinl(lower1(lab(x)) for x in dd.mechanism.head(3))}","Governance mechanisms by set; the instrument-only panel is the fair comparison (significance: see T21)",9)
    fs.save(fig,"F24_mechanisms_by_set",th)
both(F24)
# ---------- F25 mechanisms by region among governance documents
def F25(th):
    t=fs.setup(th); G=u[u.gov]; regs=[r for r in REGIONS if (G.study_region==r).sum()>=10]; regs=sorted(regs,key=lambda r:-(G.study_region==r).sum())
    mech=[x for x,_ in sorted({x:int(has(G.governance_mechanisms,x).sum()) for x in set(labels_of(G.governance_mechanisms))}.items(),key=lambda z:-z[1])]
    mat=np.array([[has(G[G.study_region==r].governance_mechanisms,x).mean()*100 for r in regs] for x in mech]); small=[i for i,r in enumerate(regs) if (G.study_region==r).sum()<MIN_N]
    fig,ax=plt.subplots(figsize=(7.6,6)); heatmap(ax,mat,[lab(x) for x in mech],[f"{RSHORT[r]}\n(n={(G.study_region==r).sum()})" for r in regs],t,fmt="{:.0f}",vmin=0,vmax=100,cbar_label="% of region's governance documents",small_cols=small)
    ax.tick_params(axis="x",labelsize=7); ax.tick_params(axis="y",labelsize=7)
    big=[i for i,r in enumerate(regs) if (G.study_region==r).sum()>=MIN_N]
    title(ax,"Where each tool is used most: "+"; ".join(f"{lower1(lab(mech[k]))} in {RSHORT[regs[big[int(np.argmax(mat[k,big]))]]]}" for k in range(min(4,len(mech)))),f"Governance mechanisms by region, all governance documents; columns ordered by n; hatched: fewer than {MIN_N} documents",8.4)
    fs.save(fig,"F25_mechanisms_by_region",th); pd.DataFrame(mat,index=mech,columns=regs).round(1).reset_index().rename(columns={"index":"mechanism"}).to_csv(FD+"F25_mechanisms_by_region.csv",index=False)
both(F25)
# ---------- F26 framing by region
def F26(th):
    t=fs.setup(th); d=rd("F26_framing_by_region"); regs=[r for r in REGIONS if r in set(d.region)]; frs=list(dict.fromkeys(d.framing)); FRL={"risk_based":"Risk-based","rights_based":"Rights-based","principle_or_ethics_based":"Principle / ethics-based","innovation_promotion":"Innovation promotion","liability_or_accountability_based":"Liability / accountability","mixed":"Mixed"}
    fig,ax=plt.subplots(figsize=(7.2,3.4))
    for i,r in enumerate(regs):
        dd=d[d.region==r].set_index("framing"); n=int(dd.n.iloc[0]); left=0; alpha=1 if n>=MIN_N else 0.45
        for j,f in enumerate(frs):
            v=float(dd.loc[f,"pct"]) if f in dd.index else 0; col=t["cat"][j] if j<5 else t["muted"]
            ax.barh(i,v,left=left,color=col,height=0.6,edgecolor=t["surface"],linewidth=1.2,alpha=alpha)
            if v>=10: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color=ink(j))
            left+=v
    ax.set_yticks(range(len(regs))); ax.set_yticklabels([f"{RSHORT[r]} (n={int(d[d.region==r].n.iloc[0])})" for r in regs],fontsize=7.5); ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of embodied-AI documents with a framing (%)")
    ax.legend([Patch(color=t["cat"][j] if j<5 else t["muted"]) for j in range(len(frs))],[FRL.get(f,f) for f in frs],ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.22),frameon=False,fontsize=7)
    dom={}
    for r in regs:
        dd=d[d.region==r]; 
        if int(dd.n.iloc[0])>=MIN_N: dom.setdefault(FRL.get(dd.sort_values("pct",ascending=False).framing.iloc[0]),[]).append(RSHORT[r])
    title(ax,"Dominant framing: "+"; ".join(f"{joinl(v)} through {k.lower()}" for k,v in dom.items()),f"Dominant framing by region (regions with fewer than 20 embodied documents omitted; faded rows have fewer than {MIN_N})",8.8)
    fs.save(fig,"F26_framing_by_region",th)
both(F26)
# ---------- F27 stance by class (n>=10 after filter), ordinal colours, neutral muted
def F27(th):
    t=fs.setup(th); d=rd("F27_stance_by_class"); d=d[d.n>=10]; cls=[c for c in DCO7 if c in set(d.doc_class)]; STN=["calls_for_new_regulation","self_regulation_or_standards_preferred","existing_law_sufficient_or_adapt","descriptive_or_neutral"]; STL={"calls_for_new_regulation":"Calls for new regulation","self_regulation_or_standards_preferred":"Prefers self-regulation / standards","existing_law_sufficient_or_adapt":"Existing law suffices or can adapt","descriptive_or_neutral":"No position"}
    cols=[fs.SEQ[9],fs.SEQ[6],fs.SEQ[3],t["muted"]]; fig,ax=plt.subplots(figsize=(7.2,2.6))
    for i,c in enumerate(cls):
        dd=d[d.doc_class==c].set_index("stance"); left=0
        for j,s_ in enumerate(STN):
            v=float(dd.loc[s_,"pct"]) if s_ in dd.index else 0
            ax.barh(i,v,left=left,color=cols[j],height=0.6,edgecolor=t["surface"],linewidth=1.2)
            if v>=8: ax.text(left+v/2,i,f"{v:.0f}%",ha="center",va="center",fontsize=7,color="#ffffff" if j==0 else "#0b0b0b")
            left+=v
    ax.set_yticks(range(len(cls))); ax.set_yticklabels([f"{DCS[c]} (n={int(d[d.doc_class==c].n.iloc[0])})" for c in cls],fontsize=7.5); ax.set_xlim(0,100); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of embodied-AI documents with a classifiable stance (%)")
    ax.legend([Patch(color=c) for c in cols],[STL[s] for s in STN],ncol=2,loc="upper center",bbox_to_anchor=(0.5,-0.3),frameon=False,fontsize=7)
    rr=d[d.doc_class=="research_output"].set_index("stance").pct
    title(ax,f"{rr.get('descriptive_or_neutral',0):.0f}% of embodied-AI research papers take no regulatory position; {rr.get('calls_for_new_regulation',0):.0f}% call for new rules and {rr.get('existing_law_sufficient_or_adapt',0):.0f}% argue existing law suffices","Stance toward regulation by document class (classes with fewer than 10 classifiable documents omitted)",8.8)
    fs.save(fig,"F27_stance_by_class",th)
both(F27)
# ---------- F28 personhood: shares per period with n
def F28(th):
    t=fs.setup(th); d=rd("F28_personhood_over_time"); pers=[p for p in ["2015-2019","2020-2022","2023-2024","2025-2026"]]; pos=["supports","discusses_neutral","opposes"]; PL={"supports":"Supports some personhood","discusses_neutral":"Discusses without a position","opposes":"Opposes"}
    cols={"supports":fs.STATUS["good"] if hasattr(fs,"STATUS") else t["cat"][2],"discusses_neutral":t["muted"],"opposes":t["cat"][7]}
    d=d[d.period.isin(pers)]; fig,ax=plt.subplots(figsize=(7.2,3)); x=np.arange(len(pers)); tot=[int(d[d.period==p].n.sum()) for p in pers]
    for j,po in enumerate(pos):
        vals=[float(d[(d.period==p)&(d.position==po)].n.sum())/tot[i]*100 if tot[i] else 0 for i,p in enumerate(pers)]
        ax.bar(x+(j-1)*0.26,vals,width=0.24,color=cols[po],label=PL[po])
    ax.set_xticks(x); ax.set_xticklabels([f"{p}{'*' if p=='2025-2026' else ''}\n(n={n})" for p,n in zip(pers,tot)],fontsize=8); ax.set_ylabel("% of documents discussing personhood"); ax.xaxis.grid(False); ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.25),ncol=3,frameon=False,fontsize=7)
    T=sum(tot); sh={po:100*float(d[d.position==po].n.sum())/T for po in pos}
    title(ax,f"The robot-personhood debate is mostly agnostic: {sh['discusses_neutral']:.0f}% of discussing documents take no position, {sh['opposes']:.0f}% oppose and {sh['supports']:.0f}% support some personhood","Positions among documents that discuss legal personhood for robots, as a share of the period's discussing documents (* 2026 to October)",8.8)
    fs.save(fig,"F28_personhood_over_time",th)
both(F28)
# ---------- F29
def F29(th):
    t=fs.setup(th); d=rd("F29_instruments_cited"); d=d[d.instrument!="Asimov's Laws of Robotics"].sort_values("embodied_pct",ascending=False); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,4.4))
    ax.barh(y-0.2,d.embodied_pct,height=0.38,color=t["cat"][0],label=f"Embodied-AI set (n={len(emb)})"); ax.barh(y+0.2,d.general_pct,height=0.38,color=t["cat"][1],label=f"General-AI set (n={len(gen)})")
    ax.set_yticks(y); ax.set_yticklabels(d.instrument,fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of documents citing the instrument (%)"); ax.legend(loc="lower right")
    te=d.sort_values("embodied_pct",ascending=False).head(2); tg=d.sort_values("general_pct",ascending=False).head(2)
    title(ax,f"General-AI documents cite {joinl(tg.instrument)} most; embodied documents cite {joinl(te.instrument)} most","Named instruments cited, by set (Asimov's fictional laws are omitted from this chart)",8.8)
    fs.save(fig,"F29_instruments_cited",th)
both(F29)
# ---------- F30
def F30(th):
    t=fs.setup(th); d=rd("F30_instruments_by_region").set_index("instrument"); regs=[r for r in REGIONS if r in d.columns]; n={r:int((u.study_region==r).sum()) for r in regs}; small=[i for i,r in enumerate(regs) if n[r]<MIN_N]
    fig,ax=plt.subplots(figsize=(7.6,4.8)); heatmap(ax,d[regs].values,list(d.index),[f"{RSHORT[r]}\n(n={n[r]})" for r in regs],t,fmt="{:.0f}",vmin=0,vmax=30,cbar_label="% of region's documents citing",small_cols=small)
    ax.tick_params(axis="x",labelsize=7); ax.tick_params(axis="y",labelsize=7)
    top={}
    for r in regs:
        if n[r]>=MIN_N: top.setdefault(d[r].idxmax(),[]).append(RSHORT[r])
    title(ax,"Most-cited instrument by region: "+"; ".join(f"{k} in {joinl(v)}" for k,v in top.items()),"Instrument citation by jurisdiction region (all usable documents)",8.6); fs.save(fig,"F30_instruments_by_region",th)
both(F30)
# ---------- F31 lower-triangle distance matrix with dendrogram, labels in the gap
def F31(th):
    t=fs.setup(th); d=rd("F31_region_distances").set_index("region"); regs=list(d.index); D=d.values.astype(float)
    from scipy.cluster.hierarchy import linkage, dendrogram
    from scipy.spatial.distance import squareform
    Z=linkage(squareform(D,checks=False),method="average"); fig=plt.figure(figsize=(7.6,4.2)); gs=fig.add_gridspec(1,2,width_ratios=[1,1.6],wspace=0.55)
    ax0=fig.add_subplot(gs[0]); dn=dendrogram(Z,labels=[RSHORT[r] for r in regs],orientation="left",ax=ax0,color_threshold=0,above_threshold_color=t["ink2"],leaf_font_size=7.5)
    ax0.set_xlabel("Cosine distance (average linkage)",fontsize=7.5); ax0.grid(False); [s.set_visible(False) for s in ax0.spines.values()]; ax0.tick_params(axis="x",labelsize=7)
    order=[regs[i] for i in dn["leaves"]][::-1]; M=d.loc[order,order].values.astype(float); L=M.copy(); L[np.triu_indices_from(L,0)]=np.nan
    nreg={r:int((emb.study_region==r).sum()) for r in regs}
    ax1=fig.add_subplot(gs[1]); heatmap(ax1,L[1:,:-1],[f"{RSHORT[r]} (n={nreg[r]})" for r in order[1:]],[RSHORT[r] for r in order[:-1]],ax1 and t,fmt="{:.2f}",vmin=0,vmax=0.25,cbar_label="cosine distance (0 = identical profile)")
    ax1.yaxis.tick_right(); ax1.tick_params(axis="x",labelsize=7); ax1.tick_params(axis="y",labelsize=7)
    pairs=sorted((D[i,j],regs[i],regs[j]) for i in range(len(regs)) for j in range(i)); far=regs[int(np.argmax(D.sum(1)))]
    title(fig,f"{RSHORT[pairs[0][1]]} and {RSHORT[pairs[0][2]]} have the closest regional profiles (distance {pairs[0][0]:.2f}); {RSHORT[far]} stands furthest apart (mean distance {D[regs.index(far)].sum()/(len(regs)-1):.2f})","Cosine distance between regional principle, topic and mechanism profiles (embodied documents; regions with at least 15); distances under 0.05 are within sampling noise (T31b)",8.6)
    fs.save(fig,"F31_region_similarity",th); pd.DataFrame(M,index=order,columns=order).round(3).reset_index().rename(columns={"index":"region"}).to_csv(FD+"F31_region_similarity.csv",index=False)
both(F31)
# ---------- F33 within-embodied term usage (composition-free) with n per year
def F33(th):
    t=fs.setup(th); lex=pd.read_csv(B+"data/lexicon_features.csv"); keycol="doc_id" if "doc_id" in lex.columns else lex.columns[0]
    E=emb.merge(lex[[keycol]+[c for c in lex.columns if c.endswith("_pk")]],left_on="doc_id",right_on=keycol,how="left",suffixes=("","_lx")) if keycol!="doc_id" else emb
    terms=[("lex_embodied_ai_term_pk","'Embodied AI' / 'physical AI'"),("lex_humanoid_pk","Humanoid"),("lex_cobot_pk","Cobot"),("lex_autonomous_vehicle_pk","Autonomous vehicle"),("lex_military_laws_pk","Autonomous weapons (repaired lexicon)"),("lex_social_robot_pk","Social robot")]
    yrs=list(range(2018,2027)); fig,axes=plt.subplots(2,3,figsize=(9.6,5),sharex=True,sharey=True); rows=[]
    for ax,(col,name) in zip(axes.flat,terms):
        sh=[]; lo=[]; hi=[]
        for y in yrs:
            d=E[E.year==y]; n=len(d); k=int((d[col].fillna(0)>0).sum()) if col in d else 0; sh.append(100*k/n if n else np.nan); l,h=wilson(k,n); lo.append(100*l); hi.append(100*h); rows.append(dict(term=name,year=y,n=n,docs_using=k,share_pct=round(100*k/n,1) if n else np.nan))
        ax.fill_between(yrs,lo,hi,color=t["cat"][0],alpha=0.15,lw=0); ax.plot(yrs,sh,color=t["cat"][0],marker="o",ms=3); ax.set_title(name,loc="left",fontsize=8); ax.xaxis.grid(False); ax.set_xticks([2018,2020,2022,2024,2026]); ax.tick_params(labelsize=7)
    axes[0][0].set_ylim(0,70); fig.supylabel("% of the year's embodied-AI documents using the term (95% Wilson band)",fontsize=8)
    ns=", ".join(f"{y}: {int((E.year==y).sum())}" for y in yrs)
    R=pd.DataFrame(rows); ch=R.groupby("term").apply(lambda g: g[g.year>=2025].share_pct.mean()-g[g.year<=2020].share_pct.mean()).sort_values()
    title(fig,f"{ch.index[-1]} vocabulary rises most from 2018-2020 to 2025-2026 ({ch.iloc[-1]:+.0f} points); {ch.index[0]} vocabulary falls most ({ch.iloc[0]:+.0f})",f"Full-text term usage within the embodied-AI set (composition-free). Embodied documents per year: {ns} (* 2026 to October)",8.6)
    fs.save(fig,"F33_term_trends",th); pd.DataFrame(rows).to_csv(FD+"F33_term_trends.csv",index=False)
both(F33)
# ---------- F34 topic change with adjusted marker, legend outside
def F34(th):
    t=fs.setup(th); d=rd("F34_topic_change"); adj=pd.read_csv(TD+"T28_topic_change_adjusted.csv") if os.path.exists(TD+"T28_topic_change_adjusted.csv") else None
    d=d[(d.pct_2020_2024>=8)|(d.pct_2025_2026>=8)].sort_values("change_pp",ascending=False); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.4,5.6))
    for yi,(o,n_) in enumerate(zip(d.pct_2020_2024,d.pct_2025_2026)): ax.plot([o,n_],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.pct_2020_2024,y,color=t["cat"][1],s=30,zorder=2); ax.scatter(d.pct_2025_2026,y,color=t["cat"][0],s=30,zorder=3)
    labs=[]
    for tp,ph in zip(d.topic,d.p_holm):
        mark=" *" if ph<0.05 else ""
        if adj is not None:
            a=adj[adj.topic==lab(tp)]
            if len(a) and float(a.p_holm.iloc[0])<0.05: mark+="†"
        labs.append(lab(tp)+mark)
    ax.set_yticks(y); ax.set_yticklabels(labs,fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Share of embodied-AI documents addressing the topic (%)")
    ax.legend(handles=[Line2D([],[],marker="o",color=t["cat"][1],lw=0,label="2020 to 2024"),Line2D([],[],marker="o",color=t["cat"][0],lw=0,label="2025 to 2026 (to October)")],loc="upper center",bbox_to_anchor=(0.5,-0.08),ncol=2,frameon=False,fontsize=7.5)
    sig=d[d.p_holm<0.05]; ups=[lab(x) for x in sig[sig.change_pp>0].topic]; downs=[lab(x) for x in sig[sig.change_pp<0].topic]; nadj=sum(1 for l in labs if "†" in l)
    title(ax,(f"Since 2025 the robot debate has shifted toward {joinl(lower1(x) for x in ups[:3])}" if ups else "Since 2025 no topic has risen significantly")+(f" and away from {joinl(lower1(x) for x in downs[:3])}" if downs else "")+f"; {nadj} shift{'s' if nadj!=1 else ''} survive{'' if nadj!=1 else 's'} genre adjustment","* crude difference Holm-significant; † significant after adjusting for document class and region (T28)",8.6)
    fs.save(fig,"F34_topic_change",th)
both(F34)
# ---------- F35 reliability, legend outside; F36; F37
def F35(th):
    t=fs.setup(th); d=rd("F35_reliability").sort_values("kappa_model"); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.4,9.2)); ax.axvspan(0.8,1.0,color=t["grid"],alpha=0.5,lw=0)
    ax.scatter(d.kappa_model,y,color=t["cat"][0],s=22,zorder=3); ax.scatter(d.kappa_retest,y,color=t["cat"][2],s=22,marker="s",zorder=3)
    ax.set_yticks(y); ax.set_yticklabels(d.lab,fontsize=6.8); ax.yaxis.grid(False); ax.set_xlim(0.4,1.0); ax.set_xlabel("Cohen's kappa (shaded: 0.8 and above)")
    ax.legend(handles=[Line2D([],[],marker="o",color=t["cat"][0],lw=0,label="Sonnet vs Opus (different model, same excerpt)"),Line2D([],[],marker="s",color=t["cat"][2],lw=0,label="Sonnet re-run (same model, same excerpt)")],loc="upper center",bbox_to_anchor=(0.5,-0.035),ncol=1,frameon=False,fontsize=7.5)
    weak=d.sort_values("kappa_model").head(4)
    title(ax,f"Two models agree on most fields (median kappa {d.kappa_model.median():.2f}); the weak spots are {joinl(lower1(x) for x in weak.lab)}","Agreement on the 160-document sample, computed against the final annotations (see F43 for the full-text and blind comparisons)",8.8)
    fs.save(fig,"F35_reliability",th)
def F36(th):
    t=fs.setup(th); d=rd("F36_lexicon_validation"); d=d.sort_values("kappa_any",ascending=False); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.4,8.6))
    cols=[t["cat"][0] if i.startswith("principle") else t["cat"][1] for i in d.item]
    ax.barh(y,d.kappa_any,color=cols,height=0.7); ax.axvline(0.4,color=t["ink"],lw=0.8); ax.text(0.41,len(d)-0.5,"0.4 = moderate agreement",fontsize=7,color=t["ink2"],va="bottom")
    ax.set_yticks(y); ax.set_yticklabels(d.label,fontsize=6.8); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel(f"Cohen's kappa, lexicon presence (full text) vs model annotation (excerpt); n={int(d.n.iloc[0])} documents with at least 300 words")
    ax.legend(handles=[Patch(color=t["cat"][0],label="Principle"),Patch(color=t["cat"][1],label="Robot type")],loc="lower right",fontsize=7.5)
    title(ax,f"Keyword lexicons agree with the model's reading best for {joinl(lower1(x) for x in d.label.head(2))} and worst for {joinl(lower1(x) for x in d.label.tail(2))}","A model-free check on the annotations after repairing the lexicon bugs found in review",8.8)
    fs.save(fig,"F36_lexicon_validation",th)
def F37(th):
    t=fs.setup(th); d=rd("F37_coverage"); RM={"Latin America - Caribbean":"Latin America & Caribbean","Middle East":"Middle East","Oceania":"Oceania","Africa":"Africa","Asia":"Asia","North America - USA":"North America","North America - Canada, Greenland":"North America","Europe":"Europe"}
    d["r"]=d.region.map(lambda x:RM.get(x,x)); regs=[r for r in REGIONS if r in set(d.r)]; y=np.arange(len(regs)); fig,ax=plt.subplots(figsize=(7.2,3.6))
    for j,(st,off) in enumerate([("sprint",-0.2),("database",0.2)]):
        cap=[int(d[(d.r==r)&(d.set==st)].captured.sum()) for r in regs]; nc=[int(d[(d.r==r)&(d.set==st)].not_captured.sum()) for r in regs]
        ax.barh(y+off,cap,height=0.38,color=t["cat"][j]); ax.barh(y+off,nc,left=cap,height=0.38,color=t["cat"][j],alpha=0.35)
        for yi,(c,n_) in enumerate(zip(cap,nc)): ax.text(c+n_+4,yi+off,f"{c}/{c+n_}",va="center",fontsize=6.5,color=t["ink2"])
    ax.set_yticks(y); ax.set_yticklabels([RSHORT[r] for r in regs],fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Sources listed by the collectors (captured / listed)"); ax.set_xlim(0,d.groupby(["r","set"]).sum(numeric_only=True).sum(axis=1).max()*1.18)
    ax.legend([Patch(color=t["cat"][0]),Patch(color=t["cat"][0],alpha=0.35),Patch(color=t["cat"][1]),Patch(color=t["cat"][1],alpha=0.35)],["Robot sprint, captured","Robot sprint, not captured","General-AI database, captured","General-AI database, not captured"],ncol=2,loc="upper center",bbox_to_anchor=(0.5,-0.2),frameon=False,fontsize=7)
    title(ax,"Round-1 collection coverage: one in five European robot-sprint sources could not be captured and Oceania lost a third of its list","Collection coverage by region and collector set (round 1 lists only; round 2 is described in the companion report)",9)
    fs.save(fig,"F37_coverage",th)
both(F35); both(F36); both(F37)
print("figures v2 done")
