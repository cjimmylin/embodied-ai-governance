#!/usr/bin/env python3
"""Structured annotation of every registry document with a fixed codebook prompt via the Claude Code CLI.
Usage: python3 04_annotate.py [--model claude-sonnet-5-5] [--out annotations/main] [--ids file] [--workers 8] [--limit N]"""
import os, re, json, sys, time, hashlib, argparse, subprocess, random
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
B="/home/user/embodied-ai-governance-v5/"
ap=argparse.ArgumentParser(); ap.add_argument("--model",default="claude-sonnet-5-5"); ap.add_argument("--out",default="annotations/main")
ap.add_argument("--ids",default=""); ap.add_argument("--workers",type=int,default=8); ap.add_argument("--limit",type=int,default=0); ap.add_argument("--effort",default=""); ap.add_argument("--head",type=int,default=10000); ap.add_argument("--mid",type=int,default=2500); ap.add_argument("--tail",type=int,default=1500); ap.add_argument("--blind",action="store_true",help="strip the CEI cover block and pass minimal metadata"); ap.add_argument("--policy",default="v1")
a=ap.parse_args()
OUT=os.path.join(B,a.out); os.makedirs(OUT,exist_ok=True)
codebook=open(B+"codebook/codebook.md").read(); schema=open(B+"codebook/schema.json").read()
SYSTEM=("You are an expert annotator for a research study on the global governance of embodied AI and robotics, combining AI-governance, legal, "
        "bibliometric and data-science expertise. Follow the codebook exactly. Output only the JSON object required by the schema.\n\n"+codebook)
prompt_hash=hashlib.sha256((SYSTEM+schema).encode()).hexdigest()[:12]
policy_tag=f"{a.policy}|head={a.head}|mid={a.mid}|tail={a.tail}|blind={a.blind}|cjk_clean=v4"
import gzip
INP=os.path.join(OUT,"_inputs"); os.makedirs(INP,exist_ok=True)
reg=pd.read_csv(B+"data/registry.csv"); feat=pd.read_csv(B+"data/text_features.csv").set_index("file_rel")
if a.ids:
    ids=set(open(a.ids).read().split()); reg=reg[reg.doc_id.isin(ids)]
if a.limit: reg=reg.head(a.limit)
HDR=re.compile(r"^\**\s*(Source URL|Issuer / country|Type|Dr\. K rubric tier|Saved|PDF downloaded from|Text)\s*\**\s*:",re.I)
def strip_cover(t):
    """Remove the CEI cover block (collector labels) that precedes many captures."""
    lines=t.splitlines(); cut=None
    for i,ln in enumerate(lines[:60]):
        if "Cover page added by CEI" in ln: cut=i
    if cut is not None: lines=lines[cut+1:]
    else:
        keep=[]; seen=False
        for i,ln in enumerate(lines):
            if i<60 and HDR.match(ln.strip()): seen=True; continue
            keep.append(ln)
        lines=keep
        if seen and lines and len(lines[0].split())<=20 and not lines[0].strip().endswith("."): pass
    return "\n".join(lines)
def clean_text(t):
    if a.blind or a.policy!="v1": t=strip_cover(t)
    t=re.sub(r"data:[a-z]+/[a-z0-9.+-]+;base64,[A-Za-z0-9+/=]+","",t)          # embedded images
    t=re.sub(r"!\[[^\]]*\]\([^)]*\)","",t)                                         # markdown images
    t=re.sub(r"\[([^\]]*)\]\([^)]*\)",r"\1",t)                                     # links -> link text
    t=re.sub(r"<[^>]{1,200}>","",t)                                                 # stray html tags
    out=[]
    for ln in t.splitlines():
        l=ln.strip()
        if not l: out.append(""); continue
        words=l.split()
        if a.policy=="v1":
            if len(words)<=4 and len(out)<400 and not re.search(r"[.:;]$",l) and not l.startswith("#"): continue   # short nav items near the top (v1 rule)
        else:
            # v2 rule: drop short navigation items near the top only when they carry no digits, are not all-caps headings and do not end a sentence
            # v4 rule: never apply the short-line rule to lines carrying CJK characters (Chinese and Japanese have no whitespace words), nor to lines ending in CJK punctuation
            if re.search(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]",l) or re.search(r"[。：；、」』）]$",l): out.append(l); continue
            if len(words)<=4 and len(out)<400 and not re.search(r"[.:;]$",l) and not l.startswith("#") and not re.search(r"\d",l) and not (l.isupper() and len(l)>5): continue
        out.append(l)
    t="\n".join(out)
    return re.sub(r"\n{3,}","\n\n",t)
def excerpt(path,head=10000,mid=2500,tail=1500):
    t=open(path,encoding="utf8",errors="replace").read().replace("\x00","")
    t=clean_text(t)
    if len(t)<=head+mid+tail+500: return t,len(t),False
    m=len(t)//2
    return t[:head]+"\n\n[... middle of document ...]\n\n"+t[m:m+mid]+"\n\n[... end of document ...]\n\n"+t[-tail:],len(t),True
def build_input(d):
    f=feat.loc[d.file_rel] if d.file_rel in feat.index else None
    if a.blind:
        meta={"doc_id":d.doc_id,"word_count_full_text":int(f["words"]) if f is not None else 0,"text_status":d.text_status}
    else:
        meta={"doc_id":d.doc_id,"region_folder":d.region,"filename":d.filename,"collector_title":d.title_best if isinstance(d.title_best,str) else "",
          "source_url":d.meta_url if isinstance(d.meta_url,str) else "","detected_language":(f["lang"] if f is not None and isinstance(f["lang"],str) else ""),
          "word_count_full_text":int(f["words"]) if f is not None else 0,"text_status":d.text_status}
    if d.text_usable and isinstance(d.text_path,str) and os.path.exists(d.text_path):
        ex,n,trunc=excerpt(d.text_path,a.head,a.mid,a.tail); meta["excerpt_is_truncated"]=trunc; meta["full_text_chars"]=n; text_available=True
    else:
        ex="(No usable text: the saved file is a bot-block/error page, a scanned PDF or is missing. Annotate from the metadata only.)"; text_available=False
    meta["text_available"]=text_available
    return "METADATA:\n"+json.dumps(meta,ensure_ascii=False,indent=1)+"\n\nDOCUMENT EXCERPT:\n"+ex
def call(doc_input):
    cmd=["claude","-p","--no-session-persistence","--model",a.model,"--tools","","--system-prompt",SYSTEM,"--json-schema",schema,"--output-format","json"]
    if a.effort: cmd+=["--effort",a.effort]
    r=subprocess.run(cmd,input=doc_input,capture_output=True,text=True,timeout=600)   # prompt via stdin (long inputs exceed the argv limit)
    try: j=json.loads(r.stdout)
    except Exception: return None,{"error":"non-json stdout","stdout":r.stdout[:500],"stderr":r.stderr[:500]}
    so=j.get("structured_output")
    if so is None and isinstance(j.get("result"),str):
        try: so=json.loads(j["result"])
        except Exception: so=None
    u=j.get("usage",{})
    log={"is_error":j.get("is_error"),"cost_usd":j.get("total_cost_usd"),"in":u.get("input_tokens"),"out":u.get("output_tokens"),
         "cache_read":u.get("cache_read_input_tokens"),"cache_create":u.get("cache_creation_input_tokens"),"api_ms":j.get("duration_api_ms"),"result_head":str(j.get("result"))[:200] if so is None else ""}
    return so,log
def work(row):
    d=row; path=os.path.join(OUT,d.doc_id+".json")
    if os.path.exists(path): return d.doc_id,"exists",None
    inp=build_input(d)
    for attempt in range(2):
        try: so,log=call(inp)
        except subprocess.TimeoutExpired: so,log=None,{"error":"timeout"}
        if so:
            rec={"doc_id":d.doc_id,"model":a.model,"prompt_hash":prompt_hash,"policy":policy_tag,"annotated_at":time.strftime("%Y-%m-%dT%H:%M:%S"),"usage":log,"annotation":so}
            json.dump(rec,open(path,"w"),ensure_ascii=False,indent=1)
            with gzip.open(os.path.join(INP,d.doc_id+".txt.gz"),"wt",encoding="utf8") as gz: gz.write(inp)
            with open(os.path.join(OUT,"_log.jsonl"),"a") as fh: fh.write(json.dumps({"doc_id":d.doc_id,**log})+"\n")
            return d.doc_id,"ok",log
        time.sleep(3)
    with open(os.path.join(OUT,"_failures.jsonl"),"a") as fh: fh.write(json.dumps({"doc_id":d.doc_id,**(log or {})})+"\n")
    return d.doc_id,"failed",log
rows=[r for _,r in reg.iterrows()]
print(f"model={a.model} prompt_hash={prompt_hash} docs={len(rows)} out={OUT}",flush=True)
done=0;cost=0.0;t0=time.time()
with ThreadPoolExecutor(a.workers) as ex:
    futs=[ex.submit(work,r) for r in rows]
    for f in as_completed(futs):
        did,st,log=f.result(); done+=1
        if log and log.get("cost_usd"): cost+=log["cost_usd"]
        if done%25==0 or st!="ok": print(f"[{done}/{len(rows)}] {did} {st} cost_so_far=${cost:.2f} elapsed={time.time()-t0:.0f}s",flush=True)
print(f"finished: {done} docs, cost=${cost:.2f}, {time.time()-t0:.0f}s")
