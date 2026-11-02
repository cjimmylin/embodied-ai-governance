"""Map the texts the round-3 collectors saved (texts/<target candidate_id>.txt) to registry ids and append them to candidates_merged.csv.
Targets that were round-2 candidates keep their R2- doc_id (data/round2_inventory.csv); reference-list targets (REF-nn) get R3- ids.
The collector header lines (SOURCE_URL ... WORDS) are stripped from the copied text. Run after merge_candidates_r3.py, before fetch_texts_r3.py."""
import pandas as pd, os, re, hashlib, csv, glob, unicodedata
B="/home/user/collection-round-3/"
V4="/home/user/embodied-ai-governance-v4/"
tg=pd.read_csv(B+"targets.csv",dtype=str,keep_default_na=False).set_index("candidate_id")
inv=pd.read_csv(V4+"data/round2_inventory.csv",dtype=str,keep_default_na=False).set_index("candidate_id")
outs=[pd.read_csv(p,dtype=str,keep_default_na=False) for p in glob.glob(B+"status/agent_*.csv")]
st=pd.concat(outs,ignore_index=True).drop_duplicates("candidate_id",keep="last").set_index("candidate_id") if outs else pd.DataFrame()
cm=pd.read_csv(B+"candidates_merged.csv",dtype=str,keep_default_na=False) if os.path.exists(B+"candidates_merged.csv") else pd.DataFrame()
def norm(t):
    t=unicodedata.normalize("NFKC",str(t or "")).lower(); t=re.sub(r"\(.*?\)","",t); t=re.sub(r"[^\w\s]"," ",t); t=re.sub(r"\s+"," ",t).strip()
    return re.sub(r"^(the|a|an|an act|a bill) ","",t)
def normurl(u):
    u=str(u or "").strip().lower(); u=re.sub(r"^https?://(www\.)?","",u); u=u.split("#")[0].rstrip("/"); return u
HDR=re.compile(r"^(SOURCE_URL|REQUESTED_URL|FETCHED|METHOD|CRAWLER|WORDS|NOTE|TITLE):")
rows=[]; n_r2=n_ref=0
for p in sorted(glob.glob(B+"texts/*.txt")):
    cid=os.path.basename(p)[:-4]
    if cid.startswith(("R2-","R3-")) or cid not in tg.index: continue
    lines=open(p,encoding="utf8",errors="replace").read().split("\n")
    src=""
    for l in lines[:10]:
        if l.startswith("SOURCE_URL:"): src=l.split(":",1)[1].strip()
    body="\n".join(l for i,l in enumerate(lines) if not (i<10 and HDR.match(l))).strip()
    if len(re.findall(r"\w+",body))<150 and len(re.sub(r"\s+","",body))<1000: continue   # the pipeline word rule; Chinese and Japanese texts have few space-separated tokens
    t=tg.loc[cid]
    if cid in inv.index:
        did=inv.loc[cid,"doc_id"]; did=did.iloc[0] if hasattr(did,"iloc") else did; n_r2+=1
    else: did="R3-"+hashlib.md5(normurl(src or t.url_primary).encode()).hexdigest()[:8]; n_ref+=1
    open(B+"texts/"+did+".txt","w",encoding="utf8").write(body)
    r={c:t.get(c,"") for c in ["candidate_id","title_original","title_en","jurisdiction","subnational","issuer","year","instrument_type","binding_nature","status","robot_types","language","url_primary","url_secondary","source_database","confidence","notes"]}
    r["candidate_id"]=cid; r["url_primary"]=src or t.url_primary; r["source_file"]="RECOVERED_round3"; r["title_key"]=norm(t.title_en or t.title_original); r["url_key"]=normurl(r["url_primary"])
    r["dup_of_v2"]=""; r["dup_of_r2"]=""; r["doc_id"]=did; r["recovery_outcome"]=st.loc[cid,"outcome"] if len(st) and cid in st.index else "saved"
    rows.append(r)
new=pd.DataFrame(rows)
if len(cm):
    cm=cm[~cm.doc_id.isin(set(new.doc_id))]
    for c in cm.columns:
        if c not in new.columns: new[c]=""
    out=pd.concat([cm,new[cm.columns.tolist()+[c for c in new.columns if c not in cm.columns]]],ignore_index=True)
else: out=new
out.to_csv(B+"candidates_merged.csv",index=False,quoting=csv.QUOTE_ALL)
print(f"recovered texts ingested: {len(new)} (round-2 ids {n_r2}, reference-list R3 ids {n_ref}); candidates_merged now {len(out)} rows")
