"""Build data/registry.csv and data/text_features.csv for the round-2 annotation run (same columns the v2 annotator reads)."""
import pandas as pd, os, re
B="/home/user/collection-round-3/"; os.makedirs(B+"data",exist_ok=True)
m=pd.read_csv(B+"candidates_merged.csv",dtype=str,keep_default_na=False); st=pd.read_csv(B+"fetch_status.csv",dtype=str,keep_default_na=False).set_index("doc_id")
try:
    from fast_langdetect import detect
    def lang(t):
        try: return detect(t[:3000].replace("\n"," "))["lang"]
        except Exception: return ""
except Exception:
    def lang(t): return ""
rows=[]; feats=[]
for _,r in m.iterrows():
    tp=B+"texts/"+r.doc_id+".txt"; ok=os.path.exists(tp); how="fetched"
    ap=B+"texts_agent/"+r.candidate_id+".txt"
    if not ok and os.path.exists(ap) and os.path.getsize(ap)>300:   # fallback: scope/abstract text collected by the standards agent for blocked catalogue pages
        import shutil; shutil.copy(ap,tp); ok=True; how="agent_abstract"
    elif ok and os.path.exists(ap) and open(tp,encoding="utf8",errors="replace").read(400)==open(ap,encoding="utf8",errors="replace").read(400): how="agent_abstract"
    txt=open(tp,encoding="utf8",errors="replace").read() if ok else ""
    rows.append(dict(doc_id=r.doc_id,file_rel=r.doc_id+".txt",region=r.jurisdiction,filename=r.doc_id+".txt",title_best=(r.title_en or r.title_original),meta_url=r.url_primary,text_status=("ok" if how=="fetched" else how) if ok else "missing",text_usable=ok,text_path=tp if ok else "",text_chars=len(txt),
                     set_primary="round3",meta_tier="",meta_how=(how if ok else ""),meta_points="",meta_country=r.jurisdiction,meta_robot_focus="",meta_type=r.instrument_type,ext="txt",n_files=1,regions_listed=r.jurisdiction,sets_listed="round3"))
    feats.append(dict(file_rel=r.doc_id+".txt",lang=lang(txt) if ok else r.language,words=len(re.findall(r"\w+",re.sub(r"\s+"," ",txt))),doi_first="",year_mode_head="",pdf_creation=""))
pd.DataFrame(rows).to_csv(B+"data/registry.csv",index=False); pd.DataFrame(feats).to_csv(B+"data/text_features.csv",index=False)
print("registry",len(rows),"with text",sum(r["text_usable"] for r in rows))
