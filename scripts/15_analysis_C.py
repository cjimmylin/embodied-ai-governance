#!/usr/bin/env python3
"""Stage 2 part C: robustness and validation (20-23) and the results digest for the narrative."""
from analysis_common import *
from sklearn.metrics import cohen_kappa_score
RESULTS.update(json.load(open(B+"data/results.json")))
a=load(); U=a[a.usable]; emb=U[U.embodied_set]; gen=U[U.general_set]; G=U[U.gov]
def both(fn):
    for th in ("light","dark"): fn(th)
# ---------- F20 reliability figure
r1=pd.read_csv(B+"data/reliability_fields.csv"); r2=pd.read_csv(B+"data/reliability_fields_retest.csv")
rr=r1.merge(r2[["field","kappa","percent_agreement"]],on="field",suffixes=("_model","_retest")); rr=rr[rr.kappa_model.notna()]
def F35(th):
    t=fs.setup(th); d=rr.copy(); d["lab"]=d.field.str.replace("principle:","P: ").map(lambda s: nice(s) if not s.startswith("P: ") else "P: "+PRL.get(s[3:],s[3:])); d=d.sort_values("kappa_model"); y=np.arange(len(d))
    fig,ax=plt.subplots(figsize=(7.2,7.6)); ax.axvspan(0.8,1.0,color=t["grid"],alpha=0.35,lw=0)
    for yi,(k1,k2) in enumerate(zip(d.kappa_model,d.kappa_retest)): ax.plot([k1,k2],[yi,yi],color=t["grid"],lw=2,zorder=1)
    ax.scatter(d.kappa_retest,y,color=t["cat"][1],s=26,zorder=2,label="Same model, test-retest"); ax.scatter(d.kappa_model,y,color=t["cat"][0],s=26,zorder=3,label="Independent second model")
    ax.set_yticks(y); ax.set_yticklabels(d.lab,fontsize=6.8); ax.yaxis.grid(False); ax.set_xlim(0.4,1.0); ax.set_xlabel("Cohen's kappa (weighted for ordinal; mean per-label for multi-label)"); ax.legend(loc="lower left",fontsize=7)
    ax.set_title("Annotation reliability on the 160-document sample (shaded: kappa >= 0.8)",loc="left"); fs.save(fig,"F35_reliability",th); d.to_csv(FD+"F35_reliability.csv",index=False)
both(F35)
R("reliability_summary",{"n_fields":len(rr),"median_kappa_model":float(rr.kappa_model.median()),"min_kappa_model":float(rr.kappa_model.min()),"min_field_model":rr.loc[rr.kappa_model.idxmin(),"field"],"fields_below_0_8_model":rr[rr.kappa_model<0.8].field.tolist(),"median_kappa_retest":float(rr.kappa_retest.median()),"min_kappa_retest":float(rr.kappa_retest.min())})
# ---------- F21 lexicon validation
LEXP={"transparency":"lex_p_transparency_pk","justice_fairness":"lex_p_fairness_pk","non_maleficence":"lex_p_safety_pk","responsibility_accountability":"lex_p_accountability_pk","privacy":"lex_p_privacy_pk","beneficence":"lex_p_beneficence_pk","freedom_autonomy":"lex_p_autonomy_pk","trust":"lex_p_trust_pk","sustainability":"lex_p_sustainability_pk","dignity":"lex_p_dignity_pk","solidarity":"lex_p_solidarity_pk","human_oversight":"lex_p_human_oversight_pk","robustness_security":"lex_p_robustness_pk","inclusive_growth":"lex_p_inclusive_growth_pk","physical_safety":"lex_p_physical_safety_pk","human_robot_proximity":"lex_p_proximity_pk","liability_for_physical_damage":"lex_p_liability_physical_pk","autonomy_level_control":"lex_p_autonomy_level_pk","conformity_assessment_certification":"lex_p_certification_pk","dual_use_military":"lex_p_dual_use_pk"}
LEXC={"humanoid_general_purpose":"lex_humanoid_pk","collaborative_robots":"lex_cobot_pk","industrial_manipulators":"lex_industrial_robot_pk","mobile_industrial_logistics":"lex_logistics_mobile_pk","delivery_robots":"lex_delivery_robot_pk","professional_service_robots":"lex_service_robot_pk","domestic_household_robots":"lex_domestic_robot_pk","social_companion_robots":"lex_social_robot_pk","care_assistive_robots":"lex_care_robot_pk","educational_robots":"lex_educational_robot_pk","sex_robots":"lex_sex_robot_pk","surgical_medical_robots":"lex_surgical_robot_pk","rehabilitation_exoskeleton_prosthetic":"lex_exoskeleton_pk","autonomous_road_vehicles":"lex_autonomous_vehicle_pk","drones_uas":"lex_drone_pk","autonomous_maritime_or_rail":"lex_maritime_rail_pk","agricultural_robots":"lex_agri_robot_pk","space_or_extreme_environment":"lex_space_extreme_pk","military_autonomous_weapons":"lex_military_laws_pk","security_policing_robots":"lex_police_security_pk"}
W=U[U.words>=300]
rows=[]
for p,lc in LEXP.items():
    ann=(W["pr_"+p]>=1).astype(int); lex=(W[lc].fillna(0)>0).astype(int); lex2=(W[lc].fillna(0)>=0.5).astype(int)
    rows.append(dict(item="principle:"+p,label=PRL[p],n=len(W),annotated_pct=round(ann.mean()*100,1),lexicon_any_pct=round(lex.mean()*100,1),agreement_any=round((ann==lex).mean(),3),kappa_any=round(cohen_kappa_score(ann,lex),3),agreement_density05=round((ann==lex2).mean(),3),kappa_density05=round(cohen_kappa_score(ann,lex2),3)))
for c,lc in LEXC.items():
    ann=has(W.embodied_categories,c).astype(int); lex=(W[lc].fillna(0)>0).astype(int); lex2=(W[lc].fillna(0)>=0.5).astype(int)
    rows.append(dict(item="category:"+c,label=nice(c),n=len(W),annotated_pct=round(ann.mean()*100,1),lexicon_any_pct=round(lex.mean()*100,1),agreement_any=round((ann==lex).mean(),3),kappa_any=round(cohen_kappa_score(ann,lex),3),agreement_density05=round((ann==lex2).mean(),3),kappa_density05=round(cohen_kappa_score(ann,lex2),3)))
t18=pd.DataFrame(rows); write_table("T18_lexicon_validation",t18,f"Agreement between full-text lexicon presence and excerpt-based annotation (documents with >= 300 words, n={len(W)}); 'density05' = at least 0.5 hits per 1,000 words")
R("lexicon_validation",{"median_kappa_categories_density05":float(t18[t18.item.str.startswith("category")].kappa_density05.median()),"median_kappa_principles_density05":float(t18[t18.item.str.startswith("principle")].kappa_density05.median()),"median_kappa_principles_any":float(t18[t18.item.str.startswith("principle")].kappa_any.median())})
# sensitivity: embodied-vs-general principle differences under lexicon measure vs annotation
emW=W[W.embodied_set]; geW=W[W.general_set]
diff_ann=[(emW["pr_"+p]>=1).mean()-(geW["pr_"+p]>=1).mean() for p in PR]; diff_lex=[(emW[LEXP[p]].fillna(0)>=0.5).mean()-(geW[LEXP[p]].fillna(0)>=0.5).mean() for p in PR]
from scipy.stats import spearmanr; rho,pv=spearmanr(diff_ann,diff_lex); R("lexicon_sensitivity_spearman",{"rho":float(rho),"p":float(pv)})
def F36(th):
    t=fs.setup(th); d=t18.sort_values("kappa_density05"); y=np.arange(len(d)); fig,ax=plt.subplots(figsize=(7.2,7.2))
    cols=[t["cat"][0] if i.startswith("category") else t["cat"][2] for i in d.item]
    ax.barh(y,d.kappa_density05,height=0.6,color=cols); ax.set_yticks(y); ax.set_yticklabels(d.label,fontsize=7); ax.yaxis.grid(False); ax.set_xlabel("Cohen's kappa: lexicon (>= 0.5 hits per 1,000 words) vs annotation"); ax.axvline(0.4,color=t["ink2"],lw=0.8,ls="-")
    ax.legend([plt.Rectangle((0,0),1,1,color=t["cat"][0]),plt.Rectangle((0,0),1,1,color=t["cat"][2])],["Embodied category","Principle"],loc="lower right",fontsize=7)
    ax.set_title("Lexicon-based measures vs model annotation (full text vs excerpt)",loc="left"); fs.save(fig,"F36_lexicon_validation",th); d.to_csv(FD+"F36_lexicon_validation.csv",index=False)
both(F36)
# ---------- F22 collector-bias sensitivity
def headline(df,name):
    g=df[df.gov]; e=df[df.embodied_set]
    return dict(subset=name,n=len(df),embodied_share_pct=round(df.embodied_set.mean()*100,1),governance_share_pct=round(df.gov.mean()*100,1),binding_share_of_gov_pct=round((g.binding_nature=="legally_binding").mean()*100,1) if len(g) else None,
                research_share_embodied_pct=round((e.doc_class=="research_output").mean()*100,1) if len(e) else None,accountability_any_embodied_pct=round((e.pr_responsibility_accountability>=1).mean()*100,1) if len(e) else None,
                physical_safety_any_embodied_pct=round((e.pr_physical_safety>=1).mean()*100,1) if len(e) else None,risk_tiering_gov_pct=round(has(g.governance_mechanisms,"risk_based_tiering").mean()*100,1) if len(g) else None,
                top_category=(max(EMB,key=lambda c:has(e.embodied_categories,c).sum()) if len(e) else None),median_year=int(df.year.median()) if df.year.notna().any() else None)
subs=[("All usable documents",U),("Collectors' sprint set only",U[U.collection_set=="sprint"]),("Collectors' database set only",U[U.collection_set=="database"]),("Substantive captures only",U[U.page_quality=="substantive_document"]),("Confidence >= 0.5 only",U[U.confidence>=0.5]),("Collector tier Core only",U[U.collection_tier=="Core"]),("Collector tier Supporting/Context only",U[U.collection_tier.isin(["Supporting","Context only"])]),("Excluding Europe",U[U.study_region!="Europe"]),("English only",U[U.language=="en"]),("Non-English only",U[U.language!="en"]),("All annotated incl. unusable captures",a)]
t19=pd.DataFrame([headline(d,n) for n,d in subs]); write_table("T19_sensitivity",t19,"Headline statistics under alternative document subsets")
R("sensitivity",t19.to_dict("records"))
# ---------- F23 coverage
cov=pd.read_csv(B+"data/collector_coverage.csv"); gaps=pd.read_csv(B+"data/download_gaps.csv")
def F37(th):
    t=fs.setup(th); cov["region_short"]=cov.region.str.replace(r"^\d[ab]?\. ","",regex=True); regs=list(dict.fromkeys(cov.region_short)); fig,ax=plt.subplots(figsize=(7.2,3.2)); y=np.arange(len(regs)); rows=[]
    for i,s in enumerate(["sprint","database"]):
        c=[int(cov[(cov.region_short==r)&(cov.set==s)].captured.sum()) for r in regs]; nc=[int((cov[(cov.region_short==r)&(cov.set==s)].rows-cov[(cov.region_short==r)&(cov.set==s)].captured).sum()) for r in regs]
        off=-0.2 if s=="sprint" else 0.2; ax.barh(y+off,c,height=0.38,color=t["cat"][i],label=f"{s}: captured"); ax.barh(y+off,nc,left=c,height=0.38,color=t["cat"][i],alpha=0.35,label=f"{s}: not captured")
        for r,cc,nn in zip(regs,c,nc): rows.append(dict(region=r,set=s,captured=cc,not_captured=nn))
    ax.set_yticks(y); ax.set_yticklabels(regs,fontsize=7.5); ax.invert_yaxis(); ax.yaxis.grid(False); ax.set_xlabel("Sources in collectors' sheets"); ax.legend(fontsize=7,loc="lower right")
    ax.set_title("Collection coverage by region: captured vs not captured sources",loc="left"); fs.save(fig,"F37_coverage",th); pd.DataFrame(rows).to_csv(FD+"F37_coverage.csv",index=False)
both(F37)
R("coverage",{"sheet_rows":int(cov.rows.sum()),"captured":int(cov.captured.sum()),"not_captured":int((cov.rows-cov.captured).sum()),"download_gaps":len(gaps),"recovered":int(gaps.status.str.contains("recovered").sum())})
# ---------- results digest
m=a
lines=["# Results digest (auto-generated numbers for the narrative)\n"]
def add(k,v): lines.append(f"- {k}: {v}")
add("annotated / usable / embodied set / general set",f"{len(a)} / {len(U)} / {len(emb)} / {len(gen)}")
add("governance documents (usable) / embodied gov / general gov",f"{len(G)} / {int(G.embodied_set.sum())} / {int(G.general_set.sum())}")
add("binding instruments (usable) / in embodied set",f"{int(U.binding.sum())} / {int((U.binding&U.embodied_set).sum())}")
add("doc_class counts (usable)",U.doc_class.value_counts().to_dict())
add("doc_class embodied",emb.doc_class.value_counts().to_dict()); add("doc_class general",gen.doc_class.value_counts().to_dict())
add("issuer_type embodied top",emb.issuer_type.value_counts().head(6).to_dict()); add("issuer_type general top",gen.issuer_type.value_counts().head(6).to_dict())
add("binding nature test",RESULTS["binding_nature_test"]); add("gov status embodied",G[G.embodied_set].instrument_status.value_counts().to_dict()); add("gov status general",G[G.general_set].instrument_status.value_counts().to_dict())
add("embodied binding nature",G[G.embodied_set].binding_nature.value_counts().to_dict()); add("general binding nature",G[G.general_set].binding_nature.value_counts().to_dict())
add("technical standards (doc_type) embodied / general",f"{int((emb.doc_type=='technical_standard').sum())} / {int((gen.doc_type=='technical_standard').sum())}")
add("embodied share trend logit",RESULTS["embodied_share_trend"]); 
Y=U[U.year.notna()]; add("year quantiles usable",Y.year.quantile([.1,.25,.5,.75,.9]).to_dict()); add("share of usable docs 2023+ / 2025+",f"{(Y.year>=2023).mean():.3f} / {(Y.year>=2025).mean():.3f}")
add("embodied by year 2015-2026",pd.read_csv(FD+"F05_embodied_share_by_year.csv").to_dict("records"))
add("cumulative instruments (final)",pd.read_csv(FD+"F06_cumulative_instruments.csv").iloc[-1].to_dict())
add("first appearance table",pd.read_csv(TD+"T03_first_appearance.csv").head(12).to_dict("records"))
add("region counts",pd.read_csv(FD+"F07_region_counts.csv").to_dict("records")); add("embodied share by region test",{k:v for k,v in RESULTS["embodied_share_by_region"].items() if k!="table"})
add("n countries",RESULTS["n_countries"]); add("top countries",pd.read_csv(FD+"F08_top_countries.csv")[["country_name","region","docs","embodied","embodied_instruments","binding"]].head(12).to_dict("records"))
add("language share",RESULTS["language_share"]); add("research summary",RESULTS["research"]); add("top venues",pd.read_csv(TD+"T05_venues.csv").head(8).to_dict("records"))
add("category any (embodied)",RESULTS["category_any"]); add("category primary",RESULTS["category_primary"])
add("categories by region (pct)",pd.read_csv(FD+"F12_categories_by_region.csv").to_dict("records"))
add("categories by class (pct)",pd.read_csv(FD+"F13_categories_by_class.csv").to_dict("records"))
add("categories by period (pct)",pd.read_csv(FD+"F14_categories_by_period.csv").to_dict("records"))
add("top category pairs",pd.read_csv(TD+"T06_category_pairs.csv").head(10).to_dict("records")); add("topic any embodied",RESULTS["topic_any_embodied"])
add("governance gap",pd.read_csv(TD+"T07_governance_gap.csv").to_dict("records")); add("sectors embodied",RESULTS["sector_embodied"]); add("sectors fig",pd.read_csv(FD+"F19_sectors.csv").to_dict("records"))
add("principles by set",pd.read_csv(TD+"T08_principles_by_set.csv").to_dict("records")); add("principles by region (pct any)",pd.read_csv(FD+"F21_principles_by_region.csv").to_dict("records"))
add("principles by class (pct substantive)",pd.read_csv(FD+"F22_principles_by_class.csv").to_dict("records")); add("embodied principles by instrument type",pd.read_csv(TD+"T09_embodied_principles_by_instrument_type.csv").to_dict("records"))
add("mechanisms by set",pd.read_csv(TD+"T10_mechanisms_by_set.csv").to_dict("records")); add("mechanisms by region",pd.read_csv(FD+"F25_mechanisms_by_region.csv").to_dict("records")); add("mechanism bundles",pd.read_csv(TD+"T11_mechanism_bundles.csv").to_dict("records")); add("cluster meta",RESULTS["mechanism_clusters"])
add("framing by region",pd.read_csv(FD+"F26_framing_by_region.csv").to_dict("records")); add("framing test",{k:v for k,v in RESULTS["framing_by_region_test"].items() if k!="table"}); add("stance by class",pd.read_csv(FD+"F27_stance_by_class.csv").to_dict("records")); add("stance research",RESULTS["stance_research"])
add("personhood",RESULTS["personhood"]); add("personhood by region",pd.read_csv(TD+"T12_personhood_by_region.csv").to_dict("records"))
add("instruments cited",pd.read_csv(TD+"T13_instruments_cited.csv").head(16).to_dict("records")); add("any instrument cited",RESULTS["any_instrument_cited_pct"]); add("instruments by region",pd.read_csv(FD+"F30_instruments_by_region.csv").to_dict("records"))
add("region profiles",pd.read_csv(TD+"T14_region_profiles.csv").to_dict("records")); add("region distances",RESULTS["region_distance"]); add("regional divergence top",pd.read_csv(TD+"T15_regional_divergence.csv").head(12).to_dict("records")); add("regional divergence bottom",pd.read_csv(TD+"T15_regional_divergence.csv").tail(6).to_dict("records"))
add("term trends",pd.read_csv(FD+"F33_term_trends.csv").to_dict("records")); add("topic change",pd.read_csv(TD+"T16_topic_change.csv").to_dict("records")); add("recency n",RESULTS["recency_n"]); add("trend models",pd.read_csv(TD+"T17_trend_models.csv").to_dict("records"))
add("reliability summary",RESULTS["reliability_summary"]); add("lexicon validation",RESULTS["lexicon_validation"]); add("lexicon sensitivity spearman",RESULTS["lexicon_sensitivity_spearman"]); add("lexicon table",pd.read_csv(TD+"T18_lexicon_validation.csv").to_dict("records"))
add("sensitivity",pd.read_csv(TD+"T19_sensitivity.csv").to_dict("records")); add("coverage",RESULTS["coverage"])
add("faith flag n",int(a.faith_or_religious_perspective.astype(bool).sum())); add("software robots n (usable)",int((U.embodiment_status=="software_agent_called_robot").sum())); add("not_ai n",int((a.ai_scope=="not_ai").sum()))
add("sprint set rated relevance>=2 share",float((a[a.collection_set=="sprint"].relevance_to_embodied_ai_governance>=2).mean())); add("embodied docs by scope",emb.ai_scope.value_counts().to_dict()); add("embodied docs by embodiment",emb.embodiment_status.value_counts().to_dict())
add("general_ai_with_embodied_provisions n and examples",[len(a[a.ai_scope=="general_ai_with_embodied_provisions"]),a[(a.ai_scope=="general_ai_with_embodied_provisions")&a.gov].sort_values("confidence",ascending=False).head(8)[["doc_id","title_en","jurisdiction_country","doc_type"]].to_dict("records")])
add("binding embodied instruments list",U[U.binding&U.embodied_set][["doc_id","title_en","jurisdiction_country","year","doc_type","embodied_categories"]].to_dict("records"))
add("embodied soft instruments sample",U[(U.doc_class=="governance_instrument_soft")&U.embodied_set].sort_values("confidence",ascending=False).head(20)[["doc_id","title_en","jurisdiction_country","year","doc_type","embodied_categories"]].to_dict("records"))
add("embodied technical standards list",U[(U.doc_type=="technical_standard")&U.embodied_set][["doc_id","title_en","jurisdiction_country","year","embodied_categories"]].to_dict("records"))
add("embodied drafts list",U[(U.doc_class=="governance_proposal_or_draft")&U.embodied_set][["doc_id","title_en","jurisdiction_country","year","doc_type","embodied_categories"]].to_dict("records"))
add("most cited embodied research (openalex)",U[U.embodied_set&(U.doc_class=="research_output")].sort_values("oa_cited_by",ascending=False).head(10)[["doc_id","title_en","year","oa_cited_by","venue"]].to_dict("records"))
open(B+"report/results_digest.md","w").write("\n".join(lines))
dump_results(); print("Part C done; digest chars:",sum(len(l) for l in lines))
