#!/usr/bin/env python3
"""Stage 1 checkpoint: taxonomies with counts, corpus/coverage statistics, reliability, QA flags.
Outputs report/stage1_checkpoint.md, codebook/taxonomies.md, data/qa_flags.csv."""
import json, re, os, pandas as pd, numpy as np
B="/home/user/embodied-ai-governance-v4/"
m=pd.read_csv(B+"data/master_table.csv"); a=m[m.annotated].copy()
reg=pd.read_csv(B+"data/registry.csv"); files=pd.read_csv(B+"data/files.csv")
cov=pd.read_csv(B+"data/collector_coverage.csv"); nc=pd.read_csv(B+"data/not_captured.csv"); gaps=pd.read_csv(B+"data/download_gaps.csv")
rel=pd.read_csv(B+"data/reliability_fields.csv") if os.path.exists(B+"data/reliability_fields.csv") else None
xc=pd.read_csv(B+"data/reliability_team_crosscheck.csv") if os.path.exists(B+"data/reliability_team_crosscheck.csv") else None
cost=sum((json.loads(l).get("cost_usd") or 0) for f in ["annotations/main/_log.jsonl","annotations/reliability_opus/_log.jsonl"] if os.path.exists(B+f) for l in open(B+f))
def vc(col,top=None):
    s=a[col].value_counts(dropna=False); s=s.head(top) if top else s
    return "\n".join(f"| {k} | {v} | {100*v/len(a):.1f}% |" for k,v in s.items())
def multi(col):
    c={}
    for v in a[col].dropna():
        for x in str(v).split("; "):
            if x: c[x]=c.get(x,0)+1
    return sorted(c.items(),key=lambda x:-x[1])
def ex(col,val,n=3):
    s=a[(a[col]==val)]
    if not len(s): return ""
    s=s.sort_values("confidence",ascending=False).head(n)
    return "; ".join(f"{r.doc_id} {str(r.title_en)[:70]}" for _,r in s.iterrows())
def exm(col,val,n=3):
    s=a[a[col].astype(str).str.contains(r"(?:^|; )"+re.escape(val)+r"(?:;|$)",regex=True)]
    if not len(s): return ""
    s=s[s.relevance_to_embodied_ai_governance>=2] if (s.relevance_to_embodied_ai_governance>=2).any() else s
    # prefer documents whose primary category/topic is this value, then governance instruments, then confidence
    pref=(s.get("primary_embodied_category" if col=="embodied_categories" else "primary_topic")==val).astype(int)
    s=s.assign(_p=pref,_g=s.is_governance_document.astype(int)).sort_values(["_p","_g","confidence"],ascending=[False,False,False]).head(n)
    return "; ".join(f"{r.doc_id} {str(r.title_en)[:70]}" for _,r in s.iterrows())
# ---------- taxonomies.md
EMB_DEF={"industrial_manipulators":"Fixed industrial arms and caged robots in manufacturing","collaborative_robots":"Cobots that share a workspace with humans","mobile_industrial_logistics":"AMRs, AGVs, warehouse and forklift robots, industrial trucks","delivery_robots":"Sidewalk and last-mile delivery robots",
"professional_service_robots":"Cleaning, security, hospitality, retail, inspection and rescue robots","domestic_household_robots":"Vacuum, lawn and home-assistant robots","social_companion_robots":"Companionship and emotional-interaction robots, robotic pets","educational_robots":"Robots used in teaching and learning",
"care_assistive_robots":"Elder care, disability support and nursing assistance","toys_entertainment_robots":"Toys and entertainment robots","sex_robots":"Sexual and intimate-companion robots","surgical_medical_robots":"Surgical and clinical robots","rehabilitation_exoskeleton_prosthetic":"Exoskeletons, prostheses, wearable robots, BCI-driven actuators","biohybrid_or_cyborg":"Biohybrid systems and human augmentation",
"humanoid_general_purpose":"Humanoids, androids, general-purpose embodied agents and embodied foundation models","autonomous_road_vehicles":"Cars, trucks, buses and shuttles","drones_uas":"Aerial drones and unmanned aircraft systems","autonomous_maritime_or_rail":"Autonomous ships, vessels and trains","agricultural_robots":"Field, harvesting and livestock robots","space_or_extreme_environment":"Space, underwater, nuclear and mining robots",
"military_autonomous_weapons":"Lethal autonomous weapons, armed drones, military robots","security_policing_robots":"Police, border and surveillance robots","other_embodied":"Other physical AI systems"}
L1={"Industrial & logistics":["industrial_manipulators","collaborative_robots","mobile_industrial_logistics","delivery_robots"],"Service & social":["professional_service_robots","domestic_household_robots","social_companion_robots","educational_robots","care_assistive_robots","toys_entertainment_robots","sex_robots"],
"Medical & body-integrated":["surgical_medical_robots","rehabilitation_exoskeleton_prosthetic","biohybrid_or_cyborg"],"Humanoid & general-purpose":["humanoid_general_purpose"],"Vehicles & field":["autonomous_road_vehicles","drones_uas","autonomous_maritime_or_rail","agricultural_robots","space_or_extreme_environment"],"Security & military":["military_autonomous_weapons","security_policing_robots"],"Other":["other_embodied"]}
embc=dict(multi("embodied_categories")); prim=a.primary_embodied_category.value_counts()
out=["# Taxonomies (with corpus counts)\n",f"Counts are over the {len(a)} annotated documents. 'Any mention' counts documents carrying the label in `embodied_categories`; 'Primary' counts documents whose single most central category it is.\n",
"## 1. Robotics and embodied-AI taxonomy\n","Two cross-cutting axes precede the categories: **embodiment status** (physical system vs software agent called a robot) and **AI scope** (general AI only / general AI with embodied provisions / embodied AI as a class / a specific embodied category).\n",
"| Embodiment status | Documents | Share |","|---|---|---|",vc("embodiment_status"),"","| AI scope | Documents | Share |","|---|---|---|",vc("ai_scope"),"",
"| Level 1 | Level 2 category | Definition | Any mention | Primary | Example documents |","|---|---|---|---|---|---|"]
for l1,cats in L1.items():
    for c in cats: out.append(f"| {l1} | `{c}` | {EMB_DEF[c]} | {embc.get(c,0)} | {prim.get(c,0)} | {exm('embodied_categories',c)} |")
out+=["","## 2. Document topic taxonomy\n","Documents carry one `primary_topic` and any number of `governance_topics`.\n","| Topic | Primary | Any mention | Example documents |","|---|---|---|---|"]
tp=dict(multi("governance_topics")); pt=a.primary_topic.value_counts()
for t,n in sorted(tp.items(),key=lambda x:-x[1]): out.append(f"| `{t}` | {pt.get(t,0)} | {n} | {exm('governance_topics',t)} |")
out+=["","## 3. Document type taxonomy\n","| Class | Fine type | Documents | Governance instruments | Example documents |","|---|---|---|---|---|"]
for (dc,dt),g in a.groupby(["doc_class","doc_type"]):
    out.append(f"| {dc} | `{dt}` | {len(g)} | {int(g.is_governance_document.sum())} | {ex('doc_type',dt)} |")
out+=["","## 4. Instrument lifecycle status (governance documents only)\n","| Status | Documents |","|---|---|"]
gd=a[a.is_governance_document==True]
for k,v in gd.instrument_status.value_counts().items(): out.append(f"| `{k}` | {v} |")
out+=["","| Binding nature | Documents |","|---|---|"]+[f"| `{k}` | {v} |" for k,v in gd.binding_nature.value_counts().items()]
out+=["","## 5. Principles framework\n","Core principles follow Jobin et al. (2019) and the OECD AI Principles; six embodied-specific extensions were added. Salience: 0 absent, 1 mentioned, 2 substantive.\n","| Principle | Mentioned (1) | Substantive (2) | Any |","|---|---|---|---|"]
PR=[c[3:] for c in a.columns if c.startswith("pr_")]
for p in PR: out.append(f"| `{p}` | {int((a['pr_'+p]==1).sum())} | {int((a['pr_'+p]==2).sum())} | {int((a['pr_'+p]>0).sum())} |")
out+=["","## 6. Governance mechanisms\n","| Mechanism | Documents |","|---|---|"]+[f"| `{k}` | {v} |" for k,v in multi("governance_mechanisms")]
open(B+"codebook/taxonomies.md","w").write("\n".join(out))
# ---------- QA flags
flags=[]
for _,r in a.iterrows():
    f=[]
    if pd.notna(r.year_final) and r.year_final<1990: f.append("year<1990")
    if pd.notna(r.get("pub_year")) and pd.notna(r.get("oa_year")) and abs(r.pub_year-r.oa_year)>1: f.append("annotation_year_vs_openalex>1")
    if r.jurisdiction_country=="XX": f.append("jurisdiction_unknown")
    if isinstance(r.lang_detected,str) and isinstance(r.language,str) and r.lang_detected and r.lang_detected!=r.language and r.words>300: f.append("language_disagreement")
    if r.is_governance_document and r.doc_class in ("communication_or_news","research_output"): f.append("governance_doc_in_news_or_research_class")
    if r.confidence<0.5 and r.text_usable: f.append("low_confidence_with_text")
    if r.collection_set=="sprint" and r.relevance_to_embodied_ai_governance==0 and r.text_usable: f.append("sprint_doc_rated_irrelevant")
    if r.ai_scope in ("embodied_ai_robotics_general","embodied_ai_specific_category") and r.embodiment_status=="none": f.append("embodied_scope_but_no_embodiment")
    if f: flags.append(dict(doc_id=r.doc_id,title=str(r.title_en)[:90],flags="; ".join(f),year=r.year_final,oa_year=r.get('oa_year'),lang=r.language,lang_detected=r.lang_detected,confidence=r.confidence))
qa=pd.DataFrame(flags); qa.to_csv(B+"data/qa_flags.csv",index=False)
# ---------- checkpoint report
regcount=reg.groupby(["region","set_primary"]).size().unstack(fill_value=0)
rp=["# Stage 1 checkpoint: corpus, taxonomies, dashboard\n",f"Generated from {len(m)} canonical documents ({len(a)} annotated). Annotation spend so far: ${cost:.2f}.\n",
"## 1. Corpus construction\n",f"- Files downloaded from Drive: {len(files)} (plus {int((files.text_status=='reader').sum())} recovered through the Drive text reader).",
f"- Unique documents after deduplication by content hash, URL, title and prose similarity: {len(reg)}.",f"- Documents listed in more than one regional folder: {int(reg.regions_listed.str.contains(';').sum())}.",
f"- Documents with usable text: {int(reg.text_usable.sum())}; bot-walled or empty captures kept as metadata-only rows: {int((~reg.text_usable).sum())}.","",
"| Collection region | Sprint | Database |","|---|---|---|"]+[f"| {i} | {r.get('sprint',0)} | {r.get('database',0)} |" for i,r in regcount.iterrows()]
rp+=["","### Coverage against the collectors' own manifests\n","| Region | Set | Rows in sheet | Captured by collectors | Not captured |","|---|---|---|---|---|"]+[f"| {r.region} | {r.set} | {r.rows} | {r.captured} | {r.rows-r.captured} |" for _,r in cov.iterrows()]
rp+=["",f"The collectors list {len(nc)} sprint sources they could not capture (bot walls, dead hosts); these are in `data/not_captured.csv`. A further {len(gaps)} captured files exceeded the Drive download cap or were permission-denied; {int(gaps.status.str.contains('recovered').sum())} were recovered as text, the rest are listed in `data/download_gaps.csv`.","",
"## 2. Annotation results at a glance\n","| Document class | Documents | Share |","|---|---|---|",vc("doc_class"),"","| AI scope | Documents | Share |","|---|---|---|",vc("ai_scope"),"",
"| Jurisdiction region (from jurisdiction, not folder) | Documents | Share |","|---|---|---|",vc("study_region"),"","| Language | Documents | Share |","|---|---|---|",vc("language",12),"",
"| Page quality | Documents | Share |","|---|---|---|",vc("page_quality"),"",
f"Year known for {int(a.year_final.notna().sum())} of {len(a)} annotated documents (annotation {int((a.year_source=='annotation').sum())}, OpenAlex {int((a.year_source=='openalex').sum())}, PDF metadata {int((a.year_source=='pdf_metadata').sum())}). Median year {int(a.year_final.median()) if a.year_final.notna().any() else 'n/a'}.","",
"Governance instruments by status:","","| Status | Documents |","|---|---|"]+[f"| {k} | {v} |" for k,v in gd.instrument_status.value_counts().items()]
if rel is not None:
    rp+=["","## 3. Reliability (main model vs independent second model, 10% sample)\n",f"Overlap documents: {int(rel.n.max())}. Cohen's kappa (quadratic-weighted for ordinal fields; mean per-label kappa for multi-label fields).\n","| Field | Agreement | Kappa |","|---|---|---|"]
    for _,r in rel.iterrows(): rp.append(f"| {r.field} | {r.percent_agreement:.2f} | {'' if pd.isna(r.kappa) else f'{r.kappa:.2f}'} |")
if xc is not None:
    rp+=["","### Cross-check against the collectors' labels\n","| Check | n | Agreement | Kappa |","|---|---|---|---|"]+[f"| {r.check} | {r.n} | {r.agreement:.2f} | {'' if pd.isna(r.kappa) else f'{r.kappa:.2f}'} |" for _,r in xc.iterrows()]
rp+=["","## 4. Quality flags for review\n",f"{len(qa)} documents carry at least one flag (`data/qa_flags.csv`). Counts by flag:",""]
fc={}
for v in (qa["flags"] if len(qa) else []):
    for x in v.split("; "): fc[x]=fc.get(x,0)+1
rp+=[f"- {k}: {v}" for k,v in sorted(fc.items(),key=lambda x:-x[1])]
rp+=["","## 5. Deliverables in this stage\n","- `data/master_table.csv` and `data/master_table.xlsx` (sheet `documents` plus `data_dictionary`): one row per document, 160+ columns.","- `dashboard/index.html`: interactive dashboard (filters, four charts with table views, document table with detail drawer).",
"- `codebook/codebook.md`, `codebook/schema.json`, `codebook/lexicons.json`: the annotation scheme.","- `codebook/taxonomies.md`: the three taxonomies with definitions, counts and example documents.",
"- `data/registry.csv`, `data/files.csv`: document registry and file-to-document mapping.","- `data/reliability_fields.csv`, `data/reliability_team_crosscheck.csv`: reliability results.","- `data/collector_coverage.csv`, `data/not_captured.csv`, `data/download_gaps.csv`: coverage accounting.","- `annotations/main/*.json`: raw per-document annotations with model, prompt hash and cost."]
open(B+"report/stage1_checkpoint.md","w").write("\n".join(rp))
print("report written; qa flags:",len(qa)); print(pd.Series(fc).sort_values(ascending=False).to_string() if fc else "no flags")
