"""Fetch each candidate's primary URL (secondary as fallback), convert to text, write texts/<doc_id>.txt and fetch_status.csv."""
import pandas as pd, requests, os, re, subprocess, time, sys, csv, html
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
B="/home/user/collection-round-3/"; T=B+"texts/"; R=B+"raw/"; os.makedirs(T,exist_ok=True); os.makedirs(R,exist_ok=True)
UA={"User-Agent":"CEI-AI-Robotics-collector/1.0 (academic research crawler; mailto:mail@drjimmylin.com)","Accept-Language":"en"}
BLOCKED=("www.iso.org","iso.org","www.ncsl.org","unece.org","www.unece.org","www.legifrance.gouv.fr","sso.agc.gov.sg","docs-library.unoda.org","www.icao.int","store.icao.int","www.osha.gov","www.loc.gov","www.bcn.cl","openstd.samr.gov.cn","flk.npc.gov.cn","www.law.go.kr","law.moj.gov.tw","www.esd.whs.mil","leginfo.legislature.ca.gov","www.a3automate.org","egazette.gov.in")
import urllib.parse
def blocked(u):
    try: return urllib.parse.urlparse(u).netloc.lower() in BLOCKED
    except Exception: return False
def un_symbol(u):
    """Derive a UN document symbol from undocs.org or UNODA docs-library URLs and return the ODS access URL."""
    try:
        pr=urllib.parse.urlparse(u); path=urllib.parse.unquote(pr.path)
    except Exception: return None
    if pr.netloc.endswith("undocs.org"): sym=path.strip("/")
    elif "docs-library.unoda.org" in pr.netloc:
        fn=path.rsplit("/",1)[-1]; mm=re.match(r"^(CCW)-([A-Z]+(?:\.\d+)?)-(\d{4})-((?:WP|CRP|INF|L|MISC)?\.?\d+(?:[-/]Rev\.?\d+)?)",fn,re.I)
        if not mm: return None
        sym="/".join(mm.groups()).replace("WP.","WP.").replace("-Rev","/Rev")
    else: return None
    if not re.match(r"^[A-Z]+/",sym): return None
    return "https://documents.un.org/api/symbol/access?s="+urllib.parse.quote(sym,safe="/.")+"&l=E"
def html_to_text(b):
    soup=BeautifulSoup(b,"lxml")
    for t in soup(["script","style","nav","header","footer","noscript","svg","form","aside"]): t.decompose()
    main=soup.select_one("#UCAP-CONTENT") or soup.select_one(".pages_content") or soup.find("main") or soup.find("article") or soup.find(id=re.compile("content|main",re.I)) or soup.body or soup
    txt=main.get_text("\n",strip=True)
    txt=re.sub(r"\n{3,}","\n\n",txt)
    return txt
def fetch_one(doc_id,url,alt):
    out={"doc_id":doc_id,"url":url,"status":"","bytes":0,"words":0,"content_type":"","note":""}
    if blocked(url) and not (alt and not blocked(alt)) and not un_symbol(url):
        out["status"]="blocked_host"; return out
    def fix(u):
        if "legislation.gov.uk" in u and "/data." not in u: u=u.rstrip("/")+"/data.xml"
        return u
    tried=[fix(u) for u in ([url,alt] if alt else [url]) if u]
    if "publications.europa.eu/resource/celex" in (alt or "") and tried and "eur-lex.europa.eu" in tried[0]: tried=[tried[1],tried[0]]
    # eur-lex CELEX links map to CELLAR; undocs/UNODA links map to the UN ODS symbol API
    extra=[]
    for u in list(tried):
        mm=re.search(r"uri=CELEX[:%3A]+([0-9A-Z()]+)",u)
        if "eur-lex.europa.eu" in u and mm and not any("resource/celex/"+mm.group(1) in t for t in tried): extra.append("https://publications.europa.eu/resource/celex/"+mm.group(1))
        us=un_symbol(u)
        if us and us not in tried: extra.append(us)
    tried=[t for t in extra if "documents.un.org" in t]+[t for t in tried if not blocked(t)]+[t for t in extra if "documents.un.org" not in t]
    for u in tried:
        if blocked(u): continue
        try:
            hdr=dict(UA)
            if "publications.europa.eu/resource/celex" in u: hdr["Accept"]="application/xhtml+xml"
            r=requests.get(u,headers=hdr,timeout=90,allow_redirects=True)
            if "publications.europa.eu/resource/celex" in u and r.status_code==404:
                for acc in ("application/pdf","text/html"):
                    r=requests.get(u,headers={**UA,"Accept":acc},timeout=120,allow_redirects=True)
                    if r.status_code==200 and len(r.content)>500: break
        except Exception as e:
            out["note"]=str(e)[:100]; continue
        out["status"]=str(r.status_code); ct=r.headers.get("content-type","").lower(); out["content_type"]=ct[:60]; out["bytes"]=len(r.content)
        if r.status_code==300 and "publications.europa.eu" in u:
            links=re.findall(r'href="(https?://publications\.europa\.eu/resource/[^"]+)"',r.text)
            links=[l for l in links if "ENG" in l.upper() or ".eng" in l.lower()] or links
            if links:
                try:
                    r=requests.get(links[0],headers={**UA,"Accept":"application/xhtml+xml"},timeout=90); out["status"]=str(r.status_code); ct=r.headers.get("content-type","").lower(); out["content_type"]=ct[:60]; out["bytes"]=len(r.content)
                except Exception as e: out["note"]=str(e)[:80]; continue
        if r.status_code!=200 or len(r.content)<500: continue
        try:
            if "pdf" in ct or u.lower().endswith(".pdf") or r.content[:5]==b"%PDF-":
                p=R+doc_id+".pdf"; open(p,"wb").write(r.content)
                txt=subprocess.run(["pdftotext","-layout","-enc","UTF-8",p,"-"],capture_output=True,text=True,timeout=120).stdout
            elif "json" in ct and "e-gov.go.jp" in u:
                import json; j=r.json(); txt=json.dumps(j,ensure_ascii=False)
                txt=re.sub(r"<[^>]+>"," ",txt); txt=html.unescape(txt)
            elif "xml" in ct and "e-gov.go.jp" in u:
                txt=re.sub(r"<[^>]+>","\n",r.text); txt=re.sub(r"\n{2,}","\n",txt)
            elif "xml" in ct and "legislation.gov.uk" in u:
                txt=re.sub(r"<[^>]+>","\n",r.text); txt=re.sub(r"\n{2,}","\n",txt)
            elif "html" in ct or "xml" in ct or b"<html" in r.content[:2000].lower():
                txt=html_to_text(r.content)
            else:
                txt=r.text
        except Exception as e:
            out["note"]="convert: "+str(e)[:80]; continue
        txt=txt.replace("\x00","")
        w=len(txt.split()); out["words"]=w
        cjk=len(re.findall(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]",txt))
        if w>=80 or cjk>=400:
            open(T+doc_id+".txt","w",encoding="utf8").write(txt); out["url"]=u; out["status"]="ok"; return out
        out["note"]="thin text"
    if out["status"]=="": out["status"]="fail"
    return out
if __name__=="__main__":
    m=pd.read_csv(B+"candidates_merged.csv",dtype=str,keep_default_na=False)
    done=set()
    if os.path.exists(B+"fetch_status.csv"): done=set(pd.read_csv(B+"fetch_status.csv",dtype=str).doc_id)
    rows=[]; t0=time.time()
    for _,r in m.iterrows():   # texts recovered by the round-3 collectors are already on disk: record them, do not re-fetch
        if r.doc_id not in done and os.path.exists(T+r.doc_id+".txt") and r.get("source_file","")=="RECOVERED_round3":
            rows.append({"doc_id":r.doc_id,"url":r.url_primary,"status":"ok","bytes":os.path.getsize(T+r.doc_id+".txt"),"words":len(open(T+r.doc_id+".txt",encoding="utf8",errors="replace").read().split()),"content_type":"recovered","note":"recovered by collector ("+r.get("recovery_outcome","")+")"}); done.add(r.doc_id)
    todo=[r for _,r in m.iterrows() if r.doc_id not in done]
    print("to fetch",len(todo),"recovered on disk",len(rows),flush=True)
    with ThreadPoolExecutor(6) as ex:
        futs=[ex.submit(fetch_one,r.doc_id,r.url_primary,r.url_secondary) for r in todo]
        for i,f in enumerate(as_completed(futs),1):
            rows.append(f.result())
            if i%25==0:
                pd.DataFrame(rows).to_csv(B+"fetch_status_partial.csv",index=False); print(f"[{i}/{len(todo)}] ok={sum(1 for x in rows if x['status']=='ok')} {time.time()-t0:.0f}s",flush=True)
    new=pd.DataFrame(rows)
    allr=pd.concat([pd.read_csv(B+"fetch_status.csv",dtype=str),new]) if os.path.exists(B+"fetch_status.csv") else new
    allr.to_csv(B+"fetch_status.csv",index=False); print(new.status.value_counts().to_string())
