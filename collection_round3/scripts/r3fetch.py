#!/usr/bin/env python3
"""Round-3 fetch helper. Usage:
  r3fetch.py <candidate_id> <url> [--render] [--note "text"]
Fetches the URL with the project's identified research crawler (no browser impersonation, no bot-check
circumvention), converts HTML or PDF to text, writes texts/<candidate_id>.txt with a metadata header, and
appends a row to status/fetch_log.csv. --render loads the page in headless Chromium (same identification)
for sites whose content is built by JavaScript. Exit code 0 = text saved (>= 150 words), 1 = failed.
"""
import sys, os, re, csv, subprocess, time, datetime, argparse
import requests
from bs4 import BeautifulSoup
B = "/home/user/collection-round-3/"
UA = "CEI-AI-Robotics-collector/1.0 (academic research crawler; mailto:mail@drjimmylin.com)"
H = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8", "Accept-Language": "en,zh;q=0.8,ja;q=0.7,ko;q=0.7,fr;q=0.7,de;q=0.7"}

def html_to_text(b):
    soup = BeautifulSoup(b, "lxml")
    for t in soup(["script", "style", "nav", "header", "footer", "noscript", "svg", "form", "aside", "iframe"]):
        t.decompose()
    main = (soup.select_one("#UCAP-CONTENT") or soup.select_one(".pages_content") or soup.find("main") or soup.find("article")
            or soup.find(id=re.compile("content|main|law|text", re.I)) or soup.body or soup)
    # round-3 (agent A): if the selected element is nearly empty (e.g. an empty <a id="...Text">
    # matched the id regex), fall back to the whole body instead of returning nothing
    if soup.body is not None and len(main.get_text(" ", strip=True)) < 200 and len(soup.body.get_text(" ", strip=True)) > len(main.get_text(" ", strip=True)):
        main = soup.body
    txt = main.get_text("\n", strip=True)
    return re.sub(r"\n{3,}", "\n\n", txt)

def pdf_to_text(path):
    r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", path, "-"], capture_output=True, text=True, timeout=180)
    return r.stdout

def render(url):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        ctx = b.new_context(user_agent=UA, locale="en-US")
        pg = ctx.new_page(); pg.set_default_timeout(45000)
        pg.goto(url, wait_until="networkidle")
        time.sleep(1.5)
        html = pg.content(); final = pg.url
        b.close()
    return html, final

def save(cid, url, final_url, method, txt, note):
    # round-3 (agent A): CJK text has no spaces, so count CJK characters too (1 word ~ 2 CJK chars)
    words = max(len(txt.split()), len(re.findall(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af\uf900-\ufaff]", txt)) // 2)
    ok = words >= 150
    if ok:
        os.makedirs(B + "texts", exist_ok=True)
        hdr = (f"SOURCE_URL: {final_url}\nREQUESTED_URL: {url}\nFETCHED: {datetime.datetime.utcnow().isoformat()}Z\n"
               f"METHOD: {method}\nCRAWLER: {UA}\nWORDS: {words}\n\n")
        open(B + f"texts/{cid}.txt", "w", encoding="utf8").write(hdr + txt)
    os.makedirs(B + "status", exist_ok=True)
    new = not os.path.exists(B + "status/fetch_log.csv")
    with open(B + "status/fetch_log.csv", "a", newline="", encoding="utf8") as f:
        w = csv.writer(f)
        if new: w.writerow(["candidate_id", "requested_url", "final_url", "method", "outcome", "words", "note", "time"])
        w.writerow([cid, url, final_url, method, "ok" if ok else "too_short", words, note, datetime.datetime.utcnow().isoformat()])
    print(("SAVED" if ok else "TOO_SHORT"), cid, words, "words", method, final_url)
    return ok

def log_fail(cid, url, method, outcome, note):
    os.makedirs(B + "status", exist_ok=True)
    new = not os.path.exists(B + "status/fetch_log.csv")
    with open(B + "status/fetch_log.csv", "a", newline="", encoding="utf8") as f:
        w = csv.writer(f)
        if new: w.writerow(["candidate_id", "requested_url", "final_url", "method", "outcome", "words", "note", "time"])
        w.writerow([cid, url, "", method, outcome, 0, note, datetime.datetime.utcnow().isoformat()])
    print("FAIL", cid, outcome, note[:120])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cid"); ap.add_argument("url"); ap.add_argument("--render", action="store_true"); ap.add_argument("--note", default="")
    a = ap.parse_args()
    cid, url = a.cid, a.url
    if not re.match(r"^[A-Za-z0-9_-]{1,40}$", cid): print("bad id"); sys.exit(1)
    try:
        if a.render:
            html, final = render(url)
            txt = html_to_text(html)
            sys.exit(0 if save(cid, url, final, "playwright", txt, a.note) else 1)
        r = requests.get(url, headers=H, timeout=60, allow_redirects=True)
        ct = r.headers.get("content-type", "")
        if r.status_code != 200:
            log_fail(cid, url, "requests", f"http_{r.status_code}", a.note); sys.exit(1)
        if "pdf" in ct or url.lower().endswith(".pdf") or r.content[:5] == b"%PDF-":
            os.makedirs(B + "raw", exist_ok=True); p = B + f"raw/{cid}.pdf"; open(p, "wb").write(r.content)
            txt = pdf_to_text(p); method = "requests+pdftotext"
        elif "xml" in ct and "html" not in ct:
            txt = BeautifulSoup(r.content, "lxml-xml").get_text("\n", strip=True); method = "requests+xml"
        else:
            txt = html_to_text(r.content); method = "requests+html"
        sys.exit(0 if save(cid, url, r.url, method, txt, a.note) else 1)
    except SystemExit: raise
    except Exception as e:
        log_fail(cid, url, "requests", "error", repr(e)[:200]); sys.exit(1)

if __name__ == "__main__": main()
