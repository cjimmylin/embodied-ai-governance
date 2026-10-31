"""Merge all candidate CSVs, normalise, deduplicate within round 2 and against the v2 collection, assign R2 ids."""
import pandas as pd, glob, re, os, unicodedata, csv
B="/home/user/collection-round-2/"
COLS=["candidate_id","title_original","title_en","jurisdiction","subnational","issuer","year","instrument_type","binding_nature","status","robot_types","language","url_primary","url_secondary","source_database","confidence","notes"]
def norm(t):
    t=unicodedata.normalize("NFKC",str(t or "")).lower(); t=re.sub(r"\(.*?\)","",t); t=re.sub(r"[^\w\s]"," ",t); t=re.sub(r"\s+"," ",t).strip()
    return re.sub(r"^(the|a|an|an act|a bill) ","",t)
def normurl(u):
    u=str(u or "").strip().lower(); u=re.sub(r"^https?://(www\.)?","",u); u=u.split("#")[0].rstrip("/")
    return u
frames=[]
for f in sorted(glob.glob(B+"candidates/*.csv")):
    try: d=pd.read_csv(f,dtype=str,keep_default_na=False,on_bad_lines="skip",engine="python")
    except Exception as e: print("skip",f,e); continue
    if "title_original" not in d.columns and "title_en" not in d.columns: print("no title cols",f); continue
    for c in COLS:
        if c not in d.columns: d[c]=""
    d=d[COLS].copy(); d["source_file"]=os.path.basename(f); frames.append(d)
m=pd.concat(frames,ignore_index=True)
m=m[(m.title_original.str.strip()!="")|(m.title_en.str.strip()!="")]
m=m[m.url_primary.str.strip()!=""]
m=m[~m.source_file.eq("API_fedlex.csv")]   # Fedlex hits are Federal Gazette items behind a JS app; Switzerland is covered by the national collector
m=m[~m.url_primary.str.contains(r"CELEX:\d{5}[A-Z]\d{4}R\(\d\d\)",regex=True)]   # corrigenda are not instruments
# relevance filter for scripted (API_) sources: keep titles with embodied-AI terms, drop obvious noise
INC=re.compile(r"robot|humanoid|unmanned|drone|remotely piloted|automated (driving|vehicle|lane|valet)|autonomous (vehicle|driving|car|ship|vessel|weapon|system|mobile|machine)|driver assistance|self-driving|driverless|lane keeping|emergency braking|machinery|surgical|exoskeleton|lethal autonomous|toy safety|product liability|medical device|cyber resilience|general product safety|u-space|type-approval|automatic lane|vehicle automation|automated system|machine safety|industrial truck|lift|ロボット|自動運転|特定自動運行|無人航空機|遠隔操作型小型車|自動運行|機器人|具身智能|自动驾驶|智能网联|无人驾驶|无人机|低空|로봇|자율주행|드론|무인항공기|robô|robótic|drone|aeronave|exoesquelet|humanoide|autônom|Roboter|Drohne|automatisiert|unbemannt|Fahrzeugautomat|selbstfahrend",re.I)
EXC=re.compile(r"anti-dumping|countervailing|concentration|merger|written question|customs|tariff|import|export licence|state aid|appointment|data exchange with regard to vehicle registration|vehicle registration data|fisheries|Automated Information Exchange|Autonomous Community|autonomous region|autonomous province|Autonomous Republic",re.I)
api=m.source_file.isin(["API_eurlex.csv","API_uk.csv","API_fedlex.csv","API_australia.csv"])   # title-searched sources need a title relevance check; full-text-searched sources (Japan, gov.cn, eCFR, Brazil) are kept and judged by annotation
keep=(~api)|(m.apply(lambda r:bool(INC.search(r.title_en+" "+r.title_original)) and not EXC.search(r.title_en+" "+r.title_original),axis=1))
keep=keep&(~m.apply(lambda r:bool(EXC.search(r.title_en+" "+r.title_original)),axis=1))
print("relevance filter on API rows:",int(api.sum()),"->",int((api&keep).sum()))
m=m[keep].copy()
m["title_key"]=m.apply(lambda r:norm(r.title_en if r.title_en.strip() else r.title_original),axis=1)
m["url_key"]=m.url_primary.map(normurl)
# within-round dedupe: same url, or same title_key + jurisdiction
before=len(m)
m=m.drop_duplicates("url_key")
m=m.drop_duplicates(["title_key","jurisdiction"])
print("within-round dedupe",before,"->",len(m))
# against existing v2 collection
ex=pd.read_csv(B+"existing_documents.csv",dtype=str,keep_default_na=False)
ex_t=set(ex.title_en.map(norm))|set(ex.title_clean.map(norm)); ex_u=set(ex.source_url.map(normurl))
def dup(r):
    if r.url_key and r.url_key in ex_u: return "url"
    if r.title_key and len(r.title_key)>=20 and r.title_key in ex_t: return "title"
    return ""
m["dup_of_v2"]=m.apply(dup,axis=1)
print("duplicates of v2:",(m.dup_of_v2!="").sum())
m=m[m.dup_of_v2==""].copy()
import hashlib
m=m.reset_index(drop=True); m["doc_id"]=["R2-"+hashlib.md5(u.encode()).hexdigest()[:8] for u in m.url_key]
m.to_csv(B+"candidates_merged.csv",index=False,quoting=csv.QUOTE_ALL)
print("merged candidates",len(m)); print(m.source_file.value_counts().to_string()); print(m.jurisdiction.value_counts().head(25).to_string())
