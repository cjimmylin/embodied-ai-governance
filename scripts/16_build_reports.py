"""Assemble report/analysis_report.md, report/supplement.md and report/paper.md
from the templates in report/src/, inlining figure embeds ({{Fxx}}) and tables ({{Txx}}),
then export HTML (self-contained) and PDF (Chromium) for each."""
import re, os, subprocess, json, sys
ROOT="/home/user/embodied-ai-governance-v4"
SRC=f"{ROOT}/report/src"; OUT=f"{ROOT}/report"; FIG=f"{ROOT}/figures"; TAB=f"{ROOT}/tables"

CAPTIONS={
"F01":"Document classes in the embodied-AI set and the general-AI set, usable documents only (n in the axis labels).",
"F02":"Documents per publication year by set, 2010 to 2026 (2026 is partial).",
"F03":"Issuer types by set.",
"F04":"Governance documents: lifecycle status (left) and binding nature (right), embodied-AI set vs general-AI set (n in the axis labels).",
"F05":"Share of each year's documents that fall in the embodied-AI set, with 95% Wilson intervals.",
"F06":"Cumulative embodied-AI governance documents by binding nature.",
"F07":"Documents by jurisdiction region and set (left) and the embodied share within each region (right).",
"F08":"Top 20 national jurisdictions by embodied-AI documents.",
"F10":"Document language by jurisdiction region.",
"F11":"Embodied-AI categories addressed: any mention and primary category (embodied-AI set).",
"F12":"Embodied categories by jurisdiction region, as a share of the region's embodied-AI documents.",
"F13":"Embodied categories by document class (share of each class's embodied-AI documents).",
"F14":"Embodied categories by publication period (share of the period's embodied-AI documents).",
"F16":"Co-occurrence of embodied categories within documents (counts of documents carrying both labels).",
"F17":"Co-occurrence of governance topics in embodied-AI documents.",
"F18":"Research attention versus governance attention by embodied category (share of research outputs vs share of principal governance instruments).",
"F19":"Application sectors by set.",
"F20":"Principle salience by set; asterisks mark differences that remain significant after Holm correction.",
"F21":"Principle presence by jurisdiction region among embodied-AI documents (core principles above the line, embodied-specific below).",
"F22":"Substantive treatment (level 2) of principles by document class among embodied-AI documents.",
"F23":"Embodied-specific considerations by document type, content-analysed captures of at least 150 words only (catalogue and landing pages excluded): share mentioning (light) and treating in depth (dark); counts shown where n is below 30.",
"F24":"Governance mechanisms by set: principal governance instruments only (left, the fair comparison) and all documents (right, genre-confounded).",
"F25":"Governance mechanisms by jurisdiction region (all governance documents).",
"F26":"Dominant governance framing by region (embodied-AI documents with a framing).",
"F27":"Stance toward regulation by document class (embodied-AI documents).",
"F28":"Positions on robot legal personhood over time (documents that discuss the question).",
"F29":"Most cited named governance instruments, embodied-AI set vs general-AI set.",
"F30":"Instrument citation by jurisdiction region (share of all usable documents in the region).",
"F31":"Cosine distance between regional principle, topic and mechanism profiles (embodied documents; regions with at least 30), ordered by average-linkage clustering with n per region; distances below the split-half noise floor (T31b) are within sampling noise.",
"F33":"Full-text term usage within the embodied-AI set by year (composition-free), with 95% Wilson bands and documents per year.",
"F34":"Governance topics in 2025 to 2026 embodied documents compared with 2020 to 2024: * crude difference Holm-significant; † significant after adjusting for document class and region.",
"F35":"Annotation reliability on the 160-document sample, computed against the final annotations: inter-model kappa and same-model test-retest kappa per field (shaded band marks kappa at or above 0.8).",
"F36":"Lexicon-based measures from full text versus model annotation of the excerpt: agreement and kappa per principle and category.",
"F37":"Collection coverage by region: sources captured versus listed, by collector set.",
"F38":"Crude and covariate-adjusted odds ratios (embodied vs general) for principles and mechanisms, adjusting for document class, region and year.",
"F39":"Embodied vs general principle presence within research outputs and within governance instruments (genre-stratified).",
"F40":"Governance-gap index with 95% bootstrap intervals (research share minus principal-instrument share by robot type); the title names the categories whose interval excludes zero.",
"F41":"Coverage audit: documents citing each reference instrument, coloured by whether the instrument itself was captured as a principal instrument with a content-analysed capture.",
"F42":"Robot-type shares within the embodied-AI set by year, with 95% Wilson bands (composition-free trends).",
"F43":"Per-field kappa for three comparisons: different model on the same excerpt, same model re-run, and same model reading the full text instead of the excerpt.",
"F44":"Per-field kappa for the metadata-blind, header-stripped re-annotation versus the original annotation (leakage check).",
"F50":"Round-2 funnel: from de-duplicated candidates to texts obtained, content-analysed documents, usable captures and the instruments the blind annotation found among them.",
"F51":"Embodied-AI governance instruments by jurisdiction region, v2 (original collection) versus v3 (with round 2).",
"F52":"Round-2 additions by annotated document class, split into the embodied-AI set and the rest.",
}
FIGFILES={f[:3]:f for f in sorted(os.listdir(FIG)) if f.endswith(".png") and "_dark" not in f}

def fig_embed(key):
    f=FIGFILES[key]; cap=CAPTIONS[key]
    return f'![Figure {key[1:]}. {cap}](../figures/{f})\n\n<em class="cap">Figure {key[1:]}. {cap}</em>'

def table_embed(key):
    base,_,suffix=key.partition("_")   # {{T29b_research}} selects tables/T29b_*_research.md
    cands=sorted(x for x in os.listdir(TAB) if x.startswith(base+"_") and x.endswith(".md") and (not suffix or x.endswith("_"+suffix+".md")))
    f=cands[0]; key=base
    txt=open(f"{TAB}/{f}",encoding="utf8").read().strip()
    # first line is the bold caption
    lines=txt.split("\n"); cap=lines[0].strip("* "); body="\n".join(lines[1:]).strip()
    cap=re.sub(r"^[TS]\d\d[a-z]?_[A-Za-z0-9_]+\.\s*","",cap)
    return f'*Table {key[1:]}. {cap}*\n\n{body}'

def expand(text):
    text=re.sub(r"\{\{(F\d\d)\}\}",lambda m:fig_embed(m.group(1)),text)
    text=re.sub(r"\{\{([TS]\d\d[a-z]?(?:_[a-z]+)?)\}\}",lambda m:table_embed(m.group(1)),text)
    text=text.replace("{{CODEBOOK}}",open(f"{ROOT}/codebook/codebook.md",encoding="utf8").read())
    text=text.replace("{{TAXONOMIES}}",open(f"{ROOT}/codebook/taxonomies.md",encoding="utf8").read())
    text=text.replace("{{STAGE1}}",open(f"{ROOT}/report/stage1_checkpoint.md",encoding="utf8").read())
    try:
        import pandas as pd
        t=pd.read_csv(f"{ROOT}/tables/T25_coverage_audit.csv"); cap=int(t.captured_as_document.sum()); cited=int(((~t.captured_as_document)&(t.n_documents_citing>0)).sum()); neither=len(t)-cap-cited
        text=text.replace("{{AUDIT}}",f"{cap} are captured as documents in the collection, {cited} are cited by documents in the corpus but were not captured, and {neither} are neither captured nor cited")
    except Exception as e: text=text.replace("{{AUDIT}}","see Table 25")
    return text

CSS="""
:root{--bg:#fcfcfb;--fg:#0b0b0b;--muted:#52514e;--rule:#e1e0d9;--accent:#2a78d6;--code:#f3f2ee}
body{background:var(--bg);color:var(--fg);font-family:"Public Sans","Segoe UI",system-ui,-apple-system,sans-serif;font-size:10.5pt;line-height:1.45;max-width:900px;margin:0 auto;padding:24px 32px}
h1{font-size:22pt;line-height:1.15;margin:0 0 6px;text-wrap:balance}
h2{font-size:15pt;margin:28px 0 8px;border-bottom:1px solid var(--rule);padding-bottom:4px;page-break-after:avoid}
h3{font-size:12pt;margin:20px 0 6px;page-break-after:avoid}
h4{font-size:10.5pt;margin:14px 0 4px}
p{margin:0 0 9px}
.author,.date{color:var(--muted);margin:0 0 4px}
table{border-collapse:collapse;font-size:8.2pt;margin:8px 0 14px;width:100%;page-break-inside:auto}
th,td{border-bottom:1px solid var(--rule);padding:3px 5px;text-align:left;vertical-align:top}
th{font-weight:600;background:var(--code)}
tr{page-break-inside:avoid}
img{max-width:100%;display:block;margin:14px auto 4px;page-break-inside:avoid}
figure{margin:0}
figcaption,em.cap{color:var(--muted);font-size:9pt}
em.cap{display:block;margin:-2px 0 16px}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:8.8pt;background:var(--code);padding:0 3px;border-radius:3px}
pre{background:var(--code);padding:8px;overflow-x:auto;font-size:8.5pt}
blockquote{border-left:3px solid var(--accent);margin:8px 0;padding:2px 12px;color:var(--muted)}
#TOC{font-size:9pt;columns:2;column-gap:28px;border:1px solid var(--rule);padding:10px 14px;margin:14px 0 20px}
#TOC ul{margin:0;padding-left:16px}
.abstract{border:1px solid var(--rule);padding:10px 14px;margin:12px 0 18px;background:var(--code)}
@page{size:A4;margin:16mm 14mm}
"""

def build(name,title,toc=True):
    src=open(f"{SRC}/{name}.md",encoding="utf8").read()
    md=expand(src)
    open(f"{OUT}/{name}.md","w",encoding="utf8").write(md)
    open(f"{OUT}/_style.css","w").write(CSS)
    cmd=["pandoc",f"{OUT}/{name}.md","-f","markdown+pipe_tables-implicit_figures","-t","html5","--standalone","--embed-resources",
         "--resource-path",f"{OUT}:{ROOT}","--css",f"{OUT}/_style.css","--metadata",f"title={title}","-o",f"{OUT}/{name}.html"]
    if toc: cmd+=["--toc","--toc-depth=2"]
    subprocess.run(cmd,check=True)
    subprocess.run(["node",f"{ROOT}/scripts/pdf.js",f"{OUT}/{name}.html",f"{OUT}/{name}.pdf"],check=True)
    print("built",name,os.path.getsize(f"{OUT}/{name}.pdf")//1024,"KB")

if __name__=="__main__":
    which=sys.argv[1:] or ["brief","analysis_report","supplement","paper","collection_round2","methods_document_discovery","methods_review_and_revision"]
    titles={"brief":"Who governs the robots? A short brief (v4)","analysis_report":"Governing machines that act in the world: analysis report (v4)",
            "supplement":"Supplementary material: codebook, reliability, coverage and extended tables",
            "paper":"Governing machines that act in the world: a content analysis of embodied-AI governance documents from eight world regions",
            "collection_round2":"Collection round 2: finding the instruments the first collection missed",
            "methods_document_discovery":"Document discovery and inclusion: methods",
            "methods_review_and_revision":"Adversarial review and revision: methods"}
    for w in which: build(w,titles[w],toc=(w!="brief"))
