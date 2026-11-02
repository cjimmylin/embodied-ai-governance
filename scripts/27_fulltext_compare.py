"""Compare the full-text re-reads (annotations/fulltext_v5) with the excerpt-based labels they replace, for the truncated
principal instruments. Writes T74 (field-level agreement) and T75 (documents whose set membership or binding label changed)."""
import os, json, glob, pandas as pd, numpy as np
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
def load_folder(folder):
    out={}
    for p in glob.glob(B+folder+"/*.json"):
        j=json.load(open(p)); out[j["doc_id"]]=j["annotation"]
    return out
full=load_folder("annotations/fulltext_v5")
if not full: print("no full-text annotations"); raise SystemExit
# the excerpt-based label is the latest earlier overlay for the same id
earlier={}
for folder in ["annotations/main","annotations/main_clean","annotations/gov_extended","annotations/round2","annotations/cjk_fix"]:
    for did,a in load_folder(folder).items():
        if did in full: earlier[did]=a
ids=[d for d in full if d in earlier]
single=["doc_class","binding_nature","instrument_status","ai_scope","embodiment_status","relevance_to_embodied_ai_governance","page_quality","primary_embodied_category","risk_framing"]
rows=[]
for f in single:
    agree=sum(1 for d in ids if earlier[d].get(f)==full[d].get(f)); rows.append(dict(field=f,n=len(ids),agree=agree,agree_pct=round(100*agree/len(ids),1)))
for f in ["embodied_categories","governance_topics","governance_mechanisms","application_sectors"]:
    j=[]
    for d in ids:
        A=set(earlier[d].get(f) or []); Bs=set(full[d].get(f) or []); j.append(len(A&Bs)/len(A|Bs) if (A|Bs) else 1.0)
    rows.append(dict(field=f+" (mean Jaccard)",n=len(ids),agree=round(float(np.mean(j))*len(ids),1),agree_pct=round(100*float(np.mean(j)),1)))
pr=[]
for d in ids:
    pa=earlier[d].get("principles") or {}; pb=full[d].get("principles") or {}
    for k in set(pa)|set(pb):
        va=pa.get(k); vb=pb.get(k)
        va=va.get("level") if isinstance(va,dict) else va; vb=vb.get("level") if isinstance(vb,dict) else vb
        pr.append((va==vb, (vb or 0)-(va or 0) if isinstance(va,(int,float)) and isinstance(vb,(int,float)) else 0))
rows.append(dict(field="principles (exact level, all 20)",n=len(pr),agree=sum(1 for x,_ in pr if x),agree_pct=round(100*sum(1 for x,_ in pr if x)/max(len(pr),1),1)))
up=sum(1 for _,dlt in pr if dlt>0); down=sum(1 for _,dlt in pr if dlt<0)
rows.append(dict(field="principle levels raised by the full text",n=len(pr),agree=up,agree_pct=round(100*up/max(len(pr),1),1)))
rows.append(dict(field="principle levels lowered by the full text",n=len(pr),agree=down,agree_pct=round(100*down/max(len(pr),1),1)))
t=pd.DataFrame(rows)
def write_table(name,df,caption):
    df.to_csv(B+f"tables/{name}.csv",index=False)
    with open(B+f"tables/{name}.md","w") as f: f.write(f"**{name}. {caption}**\n\n"+df.to_markdown(index=False)+"\n")
write_table("T74_fulltext_vs_excerpt",t,f"Full-text re-read (up to 400,000 characters) against the excerpt-based label (110,000 characters) for the {len(ids)} principal instruments whose text exceeded the excerpt: agreement per field")
ch=[]
M=pd.read_csv(B+"data/master_table.csv",low_memory=False).set_index("doc_id")
for d in ids:
    e,f=earlier[d],full[d]
    changed=[k for k in ["doc_class","binding_nature","relevance_to_embodied_ai_governance","ai_scope"] if e.get(k)!=f.get(k)]
    if changed: ch.append(dict(doc_id=d,title=M.title_en.get(d,"") if d in M.index else "",changed_fields="; ".join(changed),excerpt_class=e.get("doc_class"),fulltext_class=f.get("doc_class"),excerpt_relevance=e.get("relevance_to_embodied_ai_governance"),fulltext_relevance=f.get("relevance_to_embodied_ai_governance")))
write_table("T75_fulltext_changes",pd.DataFrame(ch) if ch else pd.DataFrame([dict(doc_id="",title="no set-defining field changed",changed_fields="",excerpt_class="",fulltext_class="",excerpt_relevance="",fulltext_relevance="")]),"Truncated principal instruments whose set-defining labels changed when the full text was read")
print("compared",len(ids),"documents; set-defining changes:",len(ch))
