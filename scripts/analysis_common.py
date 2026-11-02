"""Shared loaders, label maps, statistics and plotting helpers for the Stage 2 analysis."""
import sys, os, json, numpy as np, pandas as pd
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts"); import figstyle as fs
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multitest import multipletests
B="/home/user/embodied-ai-governance-v5/"; FD=B+"figures/data/"; TD=B+"tables/"
RESULTS={}
def R(key,val): RESULTS[key]=val
def dump_results():
    def conv(o):
        if isinstance(o,(np.integer,)): return int(o)
        if isinstance(o,(np.floating,)): return None if np.isnan(o) else float(o)
        if isinstance(o,(np.ndarray,list,tuple)): return [conv(x) for x in o]
        if isinstance(o,dict): return {str(k):conv(v) for k,v in o.items()}
        if isinstance(o,float) and np.isnan(o): return None
        return o
    json.dump(conv(RESULTS),open(B+"data/results.json","w"),indent=1,ensure_ascii=False)
PR=["transparency","justice_fairness","non_maleficence","responsibility_accountability","privacy","beneficence","freedom_autonomy","trust","sustainability","dignity","solidarity","human_oversight","robustness_security","inclusive_growth","physical_safety","human_robot_proximity","liability_for_physical_damage","autonomy_level_control","conformity_assessment_certification","dual_use_military"]
PR_CORE=PR[:14]; PR_EMB=PR[14:]
PRL={"transparency":"Transparency","justice_fairness":"Justice & fairness","non_maleficence":"Non-maleficence","responsibility_accountability":"Responsibility & accountability","privacy":"Privacy","beneficence":"Beneficence","freedom_autonomy":"Freedom & autonomy","trust":"Trust","sustainability":"Sustainability","dignity":"Dignity","solidarity":"Solidarity","human_oversight":"Human oversight","robustness_security":"Robustness & security","inclusive_growth":"Inclusive growth","physical_safety":"Physical safety","human_robot_proximity":"Human-robot proximity","liability_for_physical_damage":"Liability for physical damage","autonomy_level_control":"Autonomy level & control","conformity_assessment_certification":"Conformity assessment","dual_use_military":"Dual use & military"}
DCL={"governance_instrument_binding":"Binding instrument","governance_instrument_soft":"Soft-law instrument","governance_proposal_or_draft":"Proposal or draft","government_report_or_parliamentary":"Gov. report / parliamentary","research_output":"Research output","grey_literature":"Grey literature","communication_or_news":"Communication / news","unusable":"Unusable capture"}
DCO=list(DCL)
EMB=["industrial_manipulators","collaborative_robots","mobile_industrial_logistics","delivery_robots","professional_service_robots","domestic_household_robots","social_companion_robots","educational_robots","care_assistive_robots","toys_entertainment_robots","sex_robots","surgical_medical_robots","rehabilitation_exoskeleton_prosthetic","biohybrid_or_cyborg","humanoid_general_purpose","autonomous_road_vehicles","drones_uas","autonomous_maritime_or_rail","agricultural_robots","space_or_extreme_environment","military_autonomous_weapons","security_policing_robots","other_embodied"]
L1={"industrial_manipulators":"Industrial & logistics","collaborative_robots":"Industrial & logistics","mobile_industrial_logistics":"Industrial & logistics","delivery_robots":"Industrial & logistics","professional_service_robots":"Service & social","domestic_household_robots":"Service & social","social_companion_robots":"Service & social","educational_robots":"Service & social","care_assistive_robots":"Service & social","toys_entertainment_robots":"Service & social","sex_robots":"Service & social","surgical_medical_robots":"Medical & body-integrated","rehabilitation_exoskeleton_prosthetic":"Medical & body-integrated","biohybrid_or_cyborg":"Medical & body-integrated","humanoid_general_purpose":"Humanoid & general-purpose","autonomous_road_vehicles":"Vehicles & field","drones_uas":"Vehicles & field","autonomous_maritime_or_rail":"Vehicles & field","agricultural_robots":"Vehicles & field","space_or_extreme_environment":"Vehicles & field","military_autonomous_weapons":"Security & military","security_policing_robots":"Security & military","other_embodied":"Other embodied"}
REGIONS=["Europe","Asia","North America","Latin America & Caribbean","Middle East","Africa","Oceania","International"]
RSHORT={"Europe":"Europe","Asia":"Asia","North America":"North America","Latin America & Caribbean":"Latin America","Middle East":"Middle East","Africa":"Africa","Oceania":"Oceania","International":"International"}
TOPL={"ethics_principles":"Ethics principles","civil_liability":"Civil liability","criminal_liability":"Criminal liability","legal_personhood_robot_rights":"Legal personhood & robot rights","safety_physical_harm":"Safety & physical harm","cybersecurity":"Cybersecurity","privacy_data_protection":"Privacy & data protection","human_oversight_control":"Human oversight & control","transparency_explainability":"Transparency & explainability","fairness_bias_discrimination":"Fairness, bias & discrimination","labor_employment":"Labour & employment","human_dignity_autonomy":"Human dignity & autonomy","human_robot_interaction_social_effects":"Human-robot interaction & social effects","military_use_ihl":"Military use & IHL","certification_conformity_assessment":"Certification & conformity assessment","standards_interoperability":"Standards & interoperability","risk_management_risk_tiers":"Risk management & risk tiers","intellectual_property":"Intellectual property","consumer_protection":"Consumer protection","industrial_policy_innovation":"Industrial policy & innovation","research_ethics":"Research ethics","sustainability_environment":"Sustainability & environment","children_vulnerable_groups":"Children & vulnerable groups","trust_acceptance":"Trust & acceptance","education_training":"Education & training","taxation_economic_policy":"Taxation & economic policy","other":"Other"}
MECHL={"risk_based_tiering":"Risk-based tiering","conformity_assessment_certification":"Conformity assessment & certification","audits_impact_assessment":"Audits & impact assessment","transparency_disclosure_labelling":"Transparency, disclosure & labelling","human_oversight_requirement":"Human-oversight requirement","liability_regime":"Liability regime","insurance_requirement":"Insurance requirement","licensing_registration":"Licensing & registration","prohibitions_bans":"Prohibitions & bans","testing_sandboxes":"Testing & sandboxes","technical_standards_reference":"Reference to technical standards","oversight_body_creation":"Creation of an oversight body","funding_or_incentives":"Funding & incentives","education_training_programs":"Education & training programmes","international_cooperation":"International cooperation","self_regulation_codes":"Self-regulation & codes","data_governance_requirements":"Data-governance requirements","incident_reporting":"Incident reporting","procurement_rules":"Procurement rules","other":"Other"}
SECL={"healthcare":"Healthcare","elder_care_social_care":"Elder & social care","manufacturing":"Manufacturing","logistics_transport":"Logistics & transport","agriculture_food":"Agriculture & food","defense_security":"Defence & security","public_administration_justice":"Public administration & justice","education":"Education","finance":"Finance","retail_hospitality":"Retail & hospitality","construction":"Construction","energy_environment":"Energy & environment","domestic_consumer":"Domestic & consumer","research_science":"Research & science","cross_sector":"Cross-sector","other":"Other"}
ISSL={"academic_or_research":"Academic or research","intergovernmental_org":"Intergovernmental organisation","national_government_executive":"National executive","standards_body":"Standards body","legislature":"Legislature","news_media":"News media","regulator_or_agency":"Regulator or agency","subnational_government":"Subnational government","ngo_or_civil_society":"NGO or civil society","industry_association":"Industry association","industry_company":"Company","think_tank":"Think tank","court":"Court","other":"Other"}
def lab(s):
    for d in (PRL,TOPL,MECHL,SECL,ISSL,DCL):
        if s in d: return d[s]
    return nice(s)
def nice(s): 
    s=str(s).replace("_"," "); s=s[:1].upper()+s[1:]
    return s.replace(" ai "," AI ").replace(" ai"," AI").replace("Ai ","AI ").replace("ihl","IHL").replace(" uas"," UAS").replace("Uas","UAS")
def load():
    m=pd.read_csv(B+"data/master_table.csv"); a=m[m.annotated].copy()
    a["embodied_set"]=((a.relevance_to_embodied_ai_governance>=2)|(a.embodied_categories.fillna("")!=""))&(a.ai_scope!="not_ai")
    a["general_set"]=(~a.embodied_set)&a.ai_scope.isin(["general_ai_only","general_ai_with_embodied_provisions"])
    a["usable"]=a.text_usable&(a.page_quality!="error_or_blocked_page")&(a.doc_class!="unusable")
    a["gov"]=a.is_governance_document.astype(bool)
    a["binding_text"]=a.doc_class=="governance_instrument_binding"          # every binding-class text
    a["binding"]=a.doc_class=="governance_instrument_binding"               # redefined below as principal binding instruments once the unit flags are known
    a["legal_text"]=a.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])   # every text of instrument class (v3's 808 embodied)
    if "principal_instrument" in a.columns: a["instrument"]=a.principal_instrument.astype(bool)   # v4 headline unit: principal instruments and amendments; ancillary paperwork, incorporation decisions, language copies and catalogue pages excluded
    else: a["instrument"]=a.legal_text
    for c in ["family_rep","ai_explicit","autonomy_terms","words_ok"]:
        if c not in a.columns: a[c]=True
    a["family_rep"]=a.family_rep.astype(bool); a["ai_explicit"]=a.ai_explicit.astype(bool); a["autonomy_terms"]=a.autonomy_terms.astype(bool); a["words_ok"]=a.words_ok.astype(bool)
    a["binding"]=a.binding_text&a.instrument                                 # v4 headline unit for binding counts: principal binding instruments
    a["content_capture"]=a.page_quality.isin(["substantive_document","partial_or_excerpt"])
    a["round2"]=a.collection_set.isin(["round2","round3"])   # v5: database-harvested rounds (2 and 3) versus the web-collected round 1
    a["round3"]=(a.collection_set=="round3")
    a["year"]=a.year_final
    a["period"]=pd.cut(a.year,[0,2014,2019,2022,2024,2026],labels=["to 2014","2015-2019","2020-2022","2023-2024","2025-2026"])
    a["setname"]=np.where(a.embodied_set,"Embodied-AI set",np.where(a.general_set,"General-AI set","Other"))
    for c in ["embodied_categories","governance_topics","governance_mechanisms","application_sectors","named_instruments_referenced","countries_discussed"]: a[c]=a[c].fillna("")
    return a
def labels_of(series): 
    out=[]
    for v in series: out.extend([x for x in str(v).split("; ") if x])
    return out
def has(series,label): return series.str.contains(r"(?:^|; )"+label.replace("(","\\(").replace(")","\\)")+r"(?:;|$)",regex=True)
def wilson(k,n,z=1.96):
    if n==0: return (np.nan,np.nan)
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return (max(0,c-h),min(1,c+h))
def chi2_or_fisher(table,n_mc=4000,seed=0):
    """2x2 with any expected count < 5 -> Fisher exact; r x k with >20% of expected counts < 5 -> Monte-Carlo chi-square; else chi-square."""
    table=np.asarray(table,dtype=float)
    if table.sum()==0 or min(table.shape)<2: return "none",np.nan
    chi,p,_,exp=stats.chi2_contingency(table)
    if table.shape==(2,2) and (exp<5).any():
        _,p=stats.fisher_exact(table.astype(int)); return "Fisher",p
    if (exp<5).mean()>0.2:
        rng=np.random.default_rng(seed); r=table.sum(1); c=table.sum(0); n=int(table.sum()); pr=np.outer(r,c).ravel()/n/n
        sims=rng.multinomial(n,pr,size=n_mc).reshape(n_mc,*table.shape); E=np.outer(r,c)/n
        with np.errstate(divide="ignore",invalid="ignore"): cs=np.nansum((sims-E)**2/E,axis=(1,2))
        return "chi-square (Monte Carlo)",float((np.sum(cs>=chi)+1)/(n_mc+1))
    return "chi-square",p
def cramers_v_bc(table):
    """Bias-corrected Cramer's V (Bergsma 2013)."""
    table=np.asarray(table,dtype=float); n=table.sum(); r,k=table.shape
    if n==0 or min(r,k)<2: return np.nan
    chi,_,_,_=stats.chi2_contingency(table); phi2=chi/n
    phi2c=max(0,phi2-(k-1)*(r-1)/(n-1)); rc=r-(r-1)**2/(n-1); kc=k-(k-1)**2/(n-1)
    d=min(rc-1,kc-1)
    return float(np.sqrt(phi2c/d)) if d>0 else np.nan
def v_bootstrap(groups,flags,B=500,seed=0):
    """Bias-corrected V for a binary outcome across groups, with a percentile bootstrap CI (resampling documents)."""
    rng=np.random.default_rng(seed); groups=np.asarray(groups); flags=np.asarray(flags).astype(int); G=sorted(set(groups))
    def tab(g,f): return np.array([[int(((g==x)&(f==1)).sum()),int(((g==x)&(f==0)).sum())] for x in G])
    v0=cramers_v_bc(tab(groups,flags)); vs=[]
    for b in range(B):
        idx=rng.integers(0,len(groups),len(groups)); vs.append(cramers_v_bc(tab(groups[idx],flags[idx])))
    vs=np.array([x for x in vs if not np.isnan(x)])
    return v0,(float(np.percentile(vs,2.5)) if len(vs) else np.nan),(float(np.percentile(vs,97.5)) if len(vs) else np.nan)
def cramers_v(table):
    table=np.asarray(table); chi,_,_,_=stats.chi2_contingency(table); n=table.sum(); r,k=table.shape
    return float(np.sqrt(chi/(n*(min(r,k)-1)))) if n and min(r,k)>1 else np.nan
def holm(pvals): return multipletests(pvals,method="holm")[1] if len(pvals) else []
def write_table(name,df,caption=""):
    df.to_csv(TD+name+".csv",index=False)
    with open(TD+name+".md","w") as fh:
        if caption: fh.write(f"**{name}. {caption}**\n\n")
        fh.write(df.to_markdown(index=False)+"\n")
def _lum(hexcol):
    h=hexcol.lstrip("#"); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def heatmap(ax,mat,rowlabels,collabels,t,fmt="{:.0f}",cmap_steps=None,vmin=0,vmax=None,annotate=True,cbar_label="",small_cols=None):
    """Sequential heatmap. Light theme: lightest step -> darkest; dark theme: darkest step -> lightest, so lightness is monotone in value on both surfaces.
    vmin defaults to 0 so the lightest step always means zero. small_cols: list of column indices with small n, hatched."""
    from matplotlib.colors import LinearSegmentedColormap
    steps=fs.SEQ[0:11] if t.get("name","light")=="light" else list(reversed(fs.SEQ[2:13]))
    cmap=LinearSegmentedColormap.from_list("seq",steps)
    im=ax.imshow(mat,cmap=cmap,aspect="auto",vmin=vmin,vmax=vmax)
    if small_cols:
        for j in small_cols: ax.add_patch(plt.Rectangle((j-0.5,-0.5),1,mat.shape[0],fill=False,hatch="///",edgecolor=t["muted"],lw=0,alpha=0.6))
    ax.set_xticks(range(len(collabels))); ax.set_xticklabels(collabels,rotation=35,ha="right"); ax.set_yticks(range(len(rowlabels))); ax.set_yticklabels(rowlabels)
    ax.grid(False); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    if annotate:
        mx=np.nanmax(mat) if vmax is None else vmax; mn=0 if vmin is None else vmin
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                v=mat[i,j]
                if np.isnan(v): continue
                rgba=cmap((v-mn)/max(1e-9,(mx-mn))); hexc="#%02x%02x%02x"%tuple(int(255*c) for c in rgba[:3])
                ax.text(j,i,fmt.format(v),ha="center",va="center",fontsize=7,color="#ffffff" if _lum(hexc)<0.18 else "#0b0b0b")
    cb=plt.colorbar(im,ax=ax,fraction=0.03,pad=0.02); cb.outline.set_visible(False); cb.ax.tick_params(length=0,labelsize=7)
    if cbar_label: cb.set_label(cbar_label,fontsize=7)
    return im
