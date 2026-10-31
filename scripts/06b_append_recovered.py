#!/usr/bin/env python3
"""Append reader-recovered documents to files.csv / registry.csv as new canonical docs (ids continue from the max),
deduplicating among themselves (MinHash on prose) and attaching to existing docs when a title/content twin exists."""
import os, re, json, collections, unicodedata, pandas as pd
from datasketch import MinHash, MinHashLSH
B="/home/user/embodied-ai-governance-v4/data/"
files=pd.read_csv(B+"files.csv"); reg=pd.read_csv(B+"registry.csv"); rec=pd.read_csv(B+"data/recovered_docs.csv".replace("data/data/","data/")) if False else pd.read_csv(B+"recovered_docs.csv")
REGION_NAME={"AF":"Africa","US":"North America (USA)","CA":"North America (Canada, Greenland)","LA":"Latin America & Caribbean","AS":"Asia","ME":"Middle East","EU1":"Europe","EU2":"Europe","OC":"Oceania"}
def norm(t):
    t=unicodedata.normalize("NFKD",str(t or "")).encode("ascii","ignore").decode().lower()
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]+"," ",t)).strip()
def shingles(text):
    lines=[l.strip() for l in text[:200000].splitlines() if len(l.split())>=8 and not l.strip().startswith(("- ","* ","|","[","#","> "))]
    w=re.findall(r"\w+"," ".join(lines).lower())[:4000]; return {" ".join(w[k:k+5]) for k in range(max(0,len(w)-4))}
def mh(sh):
    m=MinHash(num_perm=128)
    for x in sh: m.update(x.encode()); 
    return m
# index existing usable docs
lsh=MinHashLSH(threshold=0.65,num_perm=128)
for _,d in reg.iterrows():
    if d.text_usable and isinstance(d.text_path,str) and os.path.exists(d.text_path):
        sh=shingles(open(d.text_path,encoding="utf8",errors="replace").read())
        if len(sh)>=120: lsh.insert(d.doc_id,mh(sh))
titles={norm(t):d for d,t in zip(reg.doc_id,reg.title_best) if isinstance(t,str) and len(norm(t))>=25}
rec["title_norm"]=rec.title_from_filename.map(norm)
# group recovered among themselves
parent=list(range(len(rec)))
def find(i):
    while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
    return i
def union(i,j):
    a,b=find(i),find(j)
    if a!=b: parent[max(a,b)]=min(a,b)
rmh={}
for i,r in rec.iterrows():
    if r.text_status!="reader": continue
    sh=shingles(open(r.text_path,encoding="utf8",errors="replace").read())
    if len(sh)>=120: rmh[i]=mh(sh)
for i in rmh:
    for j in rmh:
        if j>i and rmh[i].jaccard(rmh[j])>=0.65: union(i,j)
rec["grp"]=[find(i) for i in range(len(rec))]
# attach to existing docs
attach={}
for i,r in rec.iterrows():
    hit=None
    if i in rmh:
        q=lsh.query(rmh[i]); hit=q[0] if q else None
    if hit is None and r.title_norm in titles: hit=titles[r.title_norm]
    if hit: attach[r.grp]=hit
next_id=int(reg.doc_id.str[1:].astype(int).max())+1
newfiles=[]; newdocs=[]
for g,grp in rec.groupby("grp"):
    if g in attach: did=attach[g]
    else: did=f"D{next_id:04d}"; next_id+=1
    best=grp.sort_values("text_chars",ascending=False).iloc[0]
    for _,r in grp.iterrows():
        newfiles.append(dict(file_rel=r.file_rel,region_code=r.region_code,region=REGION_NAME[r.region_code],set=r.set,number=r.number,ccode=r.ccode,eu2_subpath="",filename=r.filename,ext=r.ext,bytes=0,md5=r.md5,
            text_status=r.text_status,text_path=r.text_path,text_chars=r.text_chars,title_from_filename=r.title_from_filename,join_key="",meta_source="none (filename only)",
            title_best=r.title_from_filename,title_norm=r.title_norm,title_is_truncated_slug=True,url_norm="",is_primary=False,doc_id=did))
    if g in attach:
        # upgrade existing doc text if it had none
        ex=reg[reg.doc_id==did].iloc[0]
        if not ex.text_usable and best.text_status=="reader":
            reg.loc[reg.doc_id==did,["text_status","text_path","text_chars","text_usable"]]=["reader",best.text_path,best.text_chars,True]
        reg.loc[reg.doc_id==did,"n_files"]+=len(grp)
        print("attached",list(grp.filename)[:2],"->",did,ex.title_best[:60])
    else:
        newdocs.append(dict(doc_id=did,file_rel=best.file_rel,region_code=best.region_code,region=REGION_NAME[best.region_code],set=best.set,number=best.number,ccode=best.ccode,filename=best.filename,ext=best.ext,bytes=0,md5=best.md5,
            text_status=best.text_status,text_path=best.text_path,text_chars=best.text_chars,title_from_filename=best.title_from_filename,meta_source="none (filename only)",title_best=best.title_from_filename,
            title_norm=best.title_norm,title_is_truncated_slug=True,is_primary=True,n_files=len(grp),regions_listed="; ".join(sorted({REGION_NAME[x] for x in grp.region_code})),
            sets_listed="; ".join(sorted(set(grp.set))),all_files=" || ".join(grp.file_rel),any_ok_text=best.text_status=="reader",set_primary=("sprint" if "sprint" in set(grp.set) else "database"),
            text_usable=(best.text_status=="reader" and best.text_chars>=400)))
        print("new",did,"<-",list(grp.filename))
nf=pd.DataFrame(newfiles); nd=pd.DataFrame(newdocs)
if len(nf):
    # mark primary among new files for new docs
    for d in nd.doc_id: nf.loc[(nf.doc_id==d)&(nf.file_rel==nd[nd.doc_id==d].file_rel.iloc[0]),"is_primary"]=True
files=pd.concat([files[~files.file_rel.isin(nf.file_rel)],nf],ignore_index=True); reg=pd.concat([reg[~reg.doc_id.isin(nd.doc_id)],nd],ignore_index=True).sort_values("doc_id")
files.to_csv(B+"files.csv",index=False); reg.to_csv(B+"registry.csv",index=False)
open(B+"recovered_doc_ids.txt","w").write("\n".join(nd.doc_id))
print("new docs:",len(nd)," registry now:",len(reg))
