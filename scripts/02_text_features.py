#!/usr/bin/env python3
"""File-level deterministic text features over converted Markdown: language, script, word count,
DOI, year mentions, PDF metadata date. Output data/text_features.csv keyed by file_rel."""
import os, re, csv, subprocess, collections
import pandas as pd
from fast_langdetect import detect
SRC="/home/user/drive-src/AI Robotics (Filtered Sources)/Filtered Sources"
files=pd.read_csv("data/files.csv")
def script_of(s):
    for name,rng in [("CJK","一-鿿"),("Arabic","؀-ۿ"),("Hebrew","֐-׿"),("Cyrillic","Ѐ-ӿ"),
                     ("Hangul","가-힯"),("Kana","぀-ヿ"),("Thai","฀-๿"),("Greek","Ͱ-Ͽ")]:
        if len(re.findall(f"[{rng}]",s))>40: return name
    return "Latin"
def pdf_dates(p):
    try: out=subprocess.run(["pdfinfo",p],capture_output=True,text=True,timeout=30).stdout
    except Exception: return "",""
    c=re.search(r"CreationDate:\s+(.*)",out); m=re.search(r"ModDate:\s+(.*)",out)
    return (c.group(1).strip() if c else ""),(m.group(1).strip() if m else "")
rows=[]
for _,f in files.iterrows():
    d=dict(file_rel=f["file_rel"])
    txt=""
    if isinstance(f["text_path"],str) and f["text_path"] and f["text_status"] in ("ok","copied"):
        txt=open(f["text_path"],encoding="utf8",errors="replace").read()
    body=re.sub(r"\s+"," ",txt)
    d["words"]=len(re.findall(r"\w+",body))
    d["script"]=script_of(body[:8000]) if body else ""
    lang,score="",0.0
    if len(body)>200:
        try:
            r=detect(body[:4000].replace("\n"," "),low_memory=False) if False else detect(body[:4000].replace("\n"," "))
            if isinstance(r,list): r=r[0]
            lang,score=r["lang"],float(r["score"])
        except Exception: pass
    d["lang"],d["lang_score"]=lang,round(score,3)
    dois=re.findall(r"\b(10\.\d{4,9}/[^\s\"'<>\\)\]]+)",txt)
    dois=[re.sub(r"[.,;:]+$","",x) for x in dois]
    d["doi_first"]=dois[0] if dois else ""
    d["doi_count"]=len(set(dois))
    yrs=[int(y) for y in re.findall(r"\b(19[89]\d|20[0-2]\d)\b",txt[:30000])]
    d["year_mode_head"]=collections.Counter(yrs).most_common(1)[0][0] if yrs else ""
    d["year_max_head"]=max(yrs) if yrs else ""
    if f["ext"]==".pdf":
        d["pdf_creation"],d["pdf_mod"]=pdf_dates(os.path.join(SRC,f["file_rel"]))
    else: d["pdf_creation"]=d["pdf_mod"]=""
    rows.append(d)
out=pd.DataFrame(rows); out.to_csv("data/text_features.csv",index=False)
print(len(out),"files;  lang top:",out["lang"].value_counts().head(15).to_dict())
print("script:",out["script"].value_counts().to_dict())
print("words median:",out["words"].median()," with DOI:",(out["doi_first"]!="").sum())
