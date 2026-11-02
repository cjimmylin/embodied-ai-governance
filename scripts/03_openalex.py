#!/usr/bin/env python3
"""Resolve documents to OpenAlex works by DOI, else by title search (accepted only if title similarity >= 0.92).
Writes data/openalex.jsonl (one line per doc_id) and data/openalex_summary.csv."""
import json, time, re, os, sys, urllib.parse, urllib.request, unicodedata
import pandas as pd
from rapidfuzz import fuzz
B="/home/user/embodied-ai-governance-v5/data/"
MAILTO="mail@drjimmylin.com"
reg=pd.read_csv(B+"registry.csv"); feat=pd.read_csv(B+"text_features.csv")
files=pd.read_csv(B+"files.csv")
# DOI per doc: from any member file's extracted DOI (prefer primary)
doi_by_file=dict(zip(feat.file_rel,feat.doi_first.fillna("")))
docdoi={}
for _,f in files.sort_values("is_primary",ascending=False).iterrows():
    d=doi_by_file.get(f.file_rel,"")
    if d and f.doc_id not in docdoi: docdoi[f.doc_id]=d
def norm(t):
    t=unicodedata.normalize("NFKD",str(t or "")).encode("ascii","ignore").decode().lower()
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]+"," ",t)).strip()
SEARCH_OK=[True]
def get(url):
    for attempt in range(4):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":f"embodied-ai-governance-study (mailto:{MAILTO})"})
            with urllib.request.urlopen(req,timeout=40) as r: return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code==429:
                ra=e.headers.get("Retry-After")
                if ra and ra.isdigit() and int(ra)>120:
                    SEARCH_OK[0]=False; return None   # daily search budget exhausted: stop title searches
                time.sleep(float(ra) if ra and ra.isdigit() else 6*(attempt+1)); continue
            return None
        except Exception: time.sleep(2*(attempt+1))
    return None
def compact(w,match_type,score):
    auth=[]
    for a in (w.get("authorships") or [])[:12]:
        inst=(a.get("institutions") or [{}])[0] if a.get("institutions") else {}
        auth.append({"name":(a.get("author") or {}).get("display_name"),"country":(a.get("countries") or [None])[0] if a.get("countries") else inst.get("country_code"),
                     "institution":inst.get("display_name")})
    src=((w.get("primary_location") or {}).get("source") or {})
    return {"openalex_id":w.get("id"),"doi":w.get("doi"),"title":w.get("title") or w.get("display_name"),"publication_year":w.get("publication_year"),
            "publication_date":w.get("publication_date"),"type":w.get("type"),"language":w.get("language"),"cited_by_count":w.get("cited_by_count"),
            "venue":src.get("display_name"),"venue_type":src.get("type"),"publisher":src.get("host_organization_name"),"is_oa":(w.get("open_access") or {}).get("is_oa"),
            "authors":auth,"first_author_country":next((a["country"] for a in auth if a.get("country")),None),
            "topics":[t.get("display_name") for t in (w.get("topics") or [])[:3]],"match_type":match_type,"match_score":score}
out_path=B+"openalex.jsonl"
done=set()
if os.path.exists(out_path):
    for ln in open(out_path): done.add(json.loads(ln)["doc_id"])
fo=open(out_path,"a")
n_doi=n_title=n_none=0
from concurrent.futures import ThreadPoolExecutor
import threading
lock=threading.Lock()
todo=sorted([d for _,d in reg.iterrows() if d.doc_id not in done],key=lambda d: 0 if docdoi.get(d.doc_id) else 1)
def resolve(d):
    rec={"doc_id":d.doc_id,"work":None}
    doi=docdoi.get(d.doc_id,"")
    w=None
    if doi:
        w=get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi,safe='')}?mailto={MAILTO}")
        if w: rec["work"]=compact(w,"doi",1.0)
    if w is None and SEARCH_OK[0] and isinstance(d.title_best,str) and len(d.title_best)>=25 and not d.title_is_truncated_slug:
        q=urllib.parse.quote(d.title_best[:200])
        res=get(f"https://api.openalex.org/works?search={q}&per_page=3&mailto={MAILTO}")
        best=None;bs=0
        for cand in (res or {}).get("results",[]):
            s=fuzz.ratio(norm(d.title_best),norm(cand.get("title") or cand.get("display_name")))/100
            if s>bs: bs,best=s,cand
        if best and bs>=0.92: rec["work"]=compact(best,"title",round(bs,3))
    with lock:
        fo.write(json.dumps(rec,ensure_ascii=False)+"\n"); fo.flush()
    time.sleep(0.15)
    return rec
with ThreadPoolExecutor(3) as ex:
    for i,rec in enumerate(ex.map(resolve,todo)):
        if rec["work"]:
            if rec["work"]["match_type"]=="doi": n_doi+=1
            else: n_title+=1
        else: n_none+=1
        if (i+1)%100==0: print("progress",i+1,"/",len(todo),flush=True)
fo.close()
print("resolved by DOI:",n_doi," by title:",n_title," unresolved:",n_none)
# summary csv
rows=[]
for ln in open(out_path):
    j=json.loads(ln); w=j["work"] or {}
    rows.append({"doc_id":j["doc_id"],"oa_matched":bool(w),"oa_match_type":w.get("match_type"),"oa_match_score":w.get("match_score"),"oa_year":w.get("publication_year"),
                 "oa_date":w.get("publication_date"),"oa_type":w.get("type"),"oa_venue":w.get("venue"),"oa_cited_by":w.get("cited_by_count"),
                 "oa_first_author_country":w.get("first_author_country"),"oa_n_authors":len(w.get("authors") or []),
                 "oa_authors":"; ".join(a["name"] for a in (w.get("authors") or []) if a.get("name")),"oa_author_countries":"; ".join(sorted({a["country"] for a in (w.get("authors") or []) if a.get("country")})),
                 "oa_doi":w.get("doi"),"oa_id":w.get("openalex_id"),"oa_topics":"; ".join(w.get("topics") or [])})
pd.DataFrame(rows).to_csv(B+"openalex_summary.csv",index=False)
print("summary written", len(rows))
