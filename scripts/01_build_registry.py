#!/usr/bin/env python3
"""Build the document registry: one row per captured file, joined to collector metadata,
then deduplicated into canonical documents. Outputs data/files.csv, data/registry.csv, data/coverage.csv."""
import os, re, csv, json, hashlib, collections, unicodedata
import pandas as pd, openpyxl
try:
    from rapidfuzz import fuzz
    def sim(a,b): return fuzz.ratio(a,b)/100
except ImportError:
    import difflib
    def sim(a,b): return difflib.SequenceMatcher(None,a,b).ratio()

SRC="/home/user/drive-src/AI Robotics (Filtered Sources)/Filtered Sources"
MD="/home/user/drive-md-out/AI Robotics (Filtered Sources-md)/Filtered Sources"
REPORT="/home/user/drive-md-out/AI Robotics (Filtered Sources-md)/_conversion_report.csv"
OUT="/home/user/embodied-ai-governance-v5/data"
REGION_CODE={"1. Africa":"AF","2a. North America - USA":"US","2b. North America - Canada, Greenland":"CA",
 "3. Latin America - Caribbean":"LA","4. Asia":"AS","5. Middle East":"ME","6. Europe/Oct 15 - Version 1":"EU1",
 "6. Europe/Oct 29 - Version 2":"EU2","7. Oceania":"OC"}
REGION_NAME={"AF":"Africa","US":"North America (USA)","CA":"North America (Canada, Greenland)","LA":"Latin America & Caribbean",
 "AS":"Asia","ME":"Middle East","EU1":"Europe","EU2":"Europe","OC":"Oceania"}

# conversion statuses
conv={}
for r in csv.DictReader(open(REPORT)):
    conv[r["source"].split("/",1)[1]] = (r["status"], r["output"].split("/",1)[1] if r["output"] else "", int(r["output_bytes"] or 0))

def slug_to_title(name):
    base=os.path.splitext(name)[0]
    base=re.sub(r"^D?\d{3}_","",base)
    base=re.sub(r"\s*\[C\d+\]$","",base)
    return base.replace("-"," ").strip()

def norm_title(t):
    t=unicodedata.normalize("NFKD",str(t or "")).encode("ascii","ignore").decode().lower()
    t=re.sub(r"^\[?pdf\]?\s*","",t)
    t=re.sub(r"[^a-z0-9 ]+"," ",t); t=re.sub(r"\s+"," ",t).strip()
    return t

rows=[]
for dp,dn,fn in os.walk(SRC):
    for f in sorted(fn):
        if f.lower()==".ds_store" or f.endswith(".xlsx") or f=="README.md": continue
        p=os.path.join(dp,f); rel=os.path.relpath(p,SRC)
        parts=rel.split(os.sep)
        region=parts[0] if not parts[0].startswith("6. Europe") else parts[0]+"/"+parts[1]
        rc=REGION_CODE[region]
        setname="database" if ("Database (non-sprint)" in rel or "/Non-sprint/" in rel) else "sprint"
        m=re.match(r"^(D?\d{3})_",f); num=m.group(1) if m else ""
        mc=re.search(r"\[(C\d+)\]",f); ccode=mc.group(1) if mc else ""
        sub=""
        if rc=="EU2":
            # Europe/Sprint/1_Official_documents/<Country>/file
            sub="/".join(parts[3:-1])
        st,mdrel,mdbytes=conv.get(rel,("missing","",0))
        with open(p,"rb") as fh: md5=hashlib.md5(fh.read()).hexdigest()
        rows.append(dict(file_rel=rel, region_code=rc, region=REGION_NAME[rc], set=setname, number=num, ccode=ccode,
            eu2_subpath=sub, filename=f, ext=os.path.splitext(f)[1].lower(), bytes=os.path.getsize(p), md5=md5,
            text_status=st, text_path=(os.path.join(MD,mdrel) if mdrel else ""), text_chars=0, title_from_filename=slug_to_title(f)))
files=pd.DataFrame(rows)
# text length in chars
def tlen(p):
    try: return len(open(p,encoding="utf8",errors="replace").read())
    except Exception: return 0
files["text_chars"]=files["text_path"].map(lambda p: tlen(p) if p else 0)

# ---- collector metadata: 4-region manifest
man=openpyxl.load_workbook(os.path.join(SRC,"Filtered-Sources_Manifest_2026-10-13.xlsx"),read_only=True,data_only=True)
sheet_region={"Asia":"AS","North America - Canada, Greenla":"CA","Middle East":"ME","Oceania":"OC"}
meta=[]  # all manifest rows incl. not captured
for ws in man.worksheets:
    rc=sheet_region[ws.title]; it=ws.iter_rows(values_only=True); hdr=[str(h) for h in next(it)]
    for r in it:
        if not any(r): continue
        d=dict(zip(hdr,r)); d["region_code"]=rc; meta.append(d)
man_df=pd.DataFrame(meta)
man_df["set"]=man_df["Set"].map(lambda s:"sprint" if "sprint" in str(s).lower() and "non" not in str(s).lower() else "database")
man_df["join_key"]=man_df["region_code"]+"|"+man_df["set"]+"|"+man_df["File"].astype(str)
files["join_key"]=files["region_code"]+"|"+files["set"]+"|"+files["filename"]
mj=man_df.set_index("join_key")
for col,src in [("meta_title","Title"),("meta_tier","Tier"),("meta_country","Country"),("meta_url","URL"),("meta_how","How obtained"),("meta_number","#")]:
    files[col]=files["join_key"].map(mj[src].to_dict())
# ---- Europe V2 index
wb=openpyxl.load_workbook(os.path.join(SRC,"6. Europe/Oct 29 - Version 2/Europe/INDEX.xlsx"),read_only=True,data_only=True)
it=wb["Index"].iter_rows(values_only=True); hdr=[str(h) for h in next(it)]
eu=pd.DataFrame([dict(zip(hdr,r)) for r in it if any(r)])
eu_by_id=eu.set_index("ID")
mask=files["region_code"]=="EU2"
for col,src in [("meta_title","Title"),("meta_tier","Dr. K tier"),("meta_country","Issuer / country"),("meta_url","Source URL"),
                ("meta_points","Points"),("meta_robot_focus","Robot focus"),("meta_type","Type"),("meta_saved_as","Saved as")]:
    files.loc[mask,col]=files.loc[mask,"ccode"].map(eu_by_id[src].to_dict())
files["meta_source"]=files["region_code"].map(lambda r: "Europe INDEX.xlsx" if r=="EU2" else ("Filtered-Sources manifest" if r in ("AS","CA","ME","OC") else "none (filename only)"))
files["title_best"]=files["meta_title"].where(files["meta_title"].notna() & (files["meta_title"].astype(str).str.len()>3), files["title_from_filename"])
files["title_norm"]=files["title_best"].map(norm_title)
files["title_is_truncated_slug"]=files["meta_source"].str.startswith("none")
files["url_norm"]=files["meta_url"].map(lambda u: re.sub(r"^https?://(www\.)?","",str(u).strip().lower().rstrip("/")) if pd.notna(u) and str(u).strip() else "")

# ---- deduplication: union-find over md5, url, near-identical normalized title
parent=list(range(len(files)))
def find(i):
    while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
    return i
def union(i,j):
    a,b=find(i),find(j)
    if a!=b: parent[max(a,b)]=min(a,b)
for key in ["md5","url_norm"]:
    groups=collections.defaultdict(list)
    for i,v in enumerate(files[key]):
        if v: groups[v].append(i)
    for g in groups.values():
        for j in g[1:]: union(g[0],j)
# title-based: exact normalized title (len>=25 chars) across any region; fuzzy >=0.93 within Europe V1<->V2 and across regions
tgroups=collections.defaultdict(list)
for i,t in enumerate(files["title_norm"]):
    if len(t)>=25: tgroups[t].append(i)
for g in tgroups.values():
    for j in g[1:]: union(g[0],j)
# fuzzy pass, blocked by first 12 chars to keep it cheap
block=collections.defaultdict(list)
for i,t in enumerate(files["title_norm"]):
    if len(t)>=25: block[t[:12]].append(i)
fuzzy_links=0
for g in block.values():
    for a in range(len(g)):
        for b in range(a+1,len(g)):
            i,j=g[a],g[b]
            if find(i)==find(j): continue
            if sim(files.at[i,"title_norm"],files.at[j,"title_norm"])>=0.93:
                union(i,j); fuzzy_links+=1
# prefix pass: truncated slug titles (no collector metadata) vs full titles
prefix_links=0
slug_idx=[i for i in range(len(files)) if files.at[i,"meta_source"].startswith("none") and len(files.at[i,"title_norm"])>=30]
full_idx=[i for i in range(len(files)) if not files.at[i,"meta_source"].startswith("none") and len(files.at[i,"title_norm"])>=30]
by_prefix=collections.defaultdict(list)
for j in full_idx: by_prefix[files.at[j,"title_norm"][:15]].append(j)
for i in slug_idx:
    t=files.at[i,"title_norm"]; cands=by_prefix.get(t[:15],[])
    best=None;bs=0
    for j in cands:
        if find(i)==find(j): best=None; break
        u=files.at[j,"title_norm"][:len(t)]
        sc=sim(t,u)
        if sc>bs: bs,best=sc,j
    if best is not None and bs>=0.90:
        union(i,best); prefix_links+=1
print("prefix links:",prefix_links)
# content pass: MinHash LSH over word 5-shingles of the first 30k chars of usable text
from datasketch import MinHash, MinHashLSH
def shingles(text):
    # prose-only shingles: drop nav/menu/link-heavy/short lines so site boilerplate cannot drive similarity
    lines=[]
    for ln in text[:200000].splitlines():
        l=ln.strip()
        if len(l.split())<8: continue
        if l.startswith(("- ","* ","|","[","#","> ")): continue
        if l.count("](")>1 or l.count("http")>1: continue
        lines.append(l)
    w=re.findall(r"\w+"," ".join(lines).lower())[:4000]
    return {" ".join(w[k:k+5]) for k in range(max(0,len(w)-4))}
lsh=MinHashLSH(threshold=0.65,num_perm=128); mh={}
for i in range(len(files)):
    if files.at[i,"text_status"] not in ("ok","copied") or files.at[i,"text_chars"]<800: continue
    sh=shingles(open(files.at[i,"text_path"],encoding="utf8",errors="replace").read())
    if len(sh)<120: continue
    m=MinHash(num_perm=128)
    for x in sh: m.update(x.encode("utf8"))
    mh[i]=m; lsh.insert(str(i),m)
content_links=0
for i,m in mh.items():
    for j in lsh.query(m):
        j=int(j)
        if j!=i and find(i)!=find(j): union(i,j); content_links+=1
print("content links:",content_links)
files["group"]=[find(i) for i in range(len(files))]

# ---- canonical document per group: choose best text member
def rank(r):
    st={"ok":0,"copied":0,"blocked-source":2,"stub":3,"missing":4}.get(r["text_status"],4)
    pref=0 if r["region_code"]=="EU2" else 1       # EU2 is the curated Europe version
    return (st, -r["text_chars"], pref)
files["rank_tuple"]=files.apply(rank,axis=1)
files=files.sort_values(["group","rank_tuple"]).reset_index(drop=True)
files["is_primary"]=~files.duplicated("group")
# doc ids
gid={g:i for i,g in enumerate(files["group"].unique(),1)}
files["doc_id"]=files["group"].map(lambda g: f"D{gid[g]:04d}")
files=files.drop(columns=["rank_tuple","group"])

prio={"Europe INDEX.xlsx":0,"Filtered-Sources manifest":1,"none (filename only)":2}
meta_cols=["meta_title","meta_tier","meta_country","meta_url","meta_how","meta_number","meta_points","meta_robot_focus","meta_type","meta_saved_as","meta_source","title_best","title_norm","title_is_truncated_slug"]
best_meta={}
for g,grp in files.groupby("doc_id"):
    grp=grp.assign(_p=grp["meta_source"].map(prio)).sort_values(["_p","text_chars"],ascending=[True,False])
    best_meta[g]=grp.iloc[0][meta_cols].to_dict()
    # tier/country/url may be missing on the best-source row but present on another member
    for c in ["meta_tier","meta_country","meta_url","meta_robot_focus","meta_type","meta_points"]:
        if pd.isna(best_meta[g][c]):
            vals=[v for v in grp[c] if pd.notna(v)]
            if vals: best_meta[g][c]=vals[0]
prim=files[files["is_primary"]].copy()
for c in meta_cols: prim[c]=prim["doc_id"].map(lambda d: best_meta[d][c])
agg=files.groupby("doc_id").agg(n_files=("file_rel","size"),
    regions_listed=("region",lambda s:"; ".join(sorted(set(s)))),
    sets_listed=("set",lambda s:"; ".join(sorted(set(s)))),
    all_files=("file_rel",lambda s:" || ".join(s)),
    any_ok_text=("text_status",lambda s: any(x in ("ok","copied") for x in s)))
reg=prim.merge(agg,on="doc_id")
reg["set_primary"]=reg["sets_listed"].map(lambda s: "sprint" if "sprint" in s else "database")
reg["text_usable"]=reg["text_status"].isin(["ok","copied"]) & (reg["text_chars"]>=400)
reg=reg.sort_values("doc_id")
files.to_csv(os.path.join(OUT,"files.csv"),index=False)
reg.to_csv(os.path.join(OUT,"registry.csv"),index=False)

# ---- coverage: manifest rows not captured (4 regions) + Europe INDEX rows w/o file
cov=[]
for _,r in man_df.iterrows():
    cov.append(dict(region_code=r["region_code"],set=r["set"],number=r["#"],tier=r["Tier"],country=r["Country"],title=r["Title"],
                    status=r["Status"],how=r["How obtained"],url=r["URL"]))
cov_df=pd.DataFrame(cov); cov_df.to_csv(os.path.join(OUT,"collector_manifest_rows.csv"),index=False)

print("files:",len(files)," unique docs:",len(reg)," fuzzy title links:",fuzzy_links)
print("docs by region (primary):"); print(reg["region"].value_counts().to_string())
print("docs by set_primary:"); print(reg["set_primary"].value_counts().to_string())
print("text_usable:",reg["text_usable"].sum()," not usable:",(~reg["text_usable"]).sum())
print("text_status of primaries:"); print(reg["text_status"].value_counts().to_string())
print("docs appearing in >1 region:",(reg["regions_listed"].str.contains(";")).sum())
print("meta_source:"); print(reg["meta_source"].value_counts().to_string())
print("tier known:",reg["meta_tier"].notna().sum()," country known:",reg["meta_country"].notna().sum())
