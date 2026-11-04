#!/usr/bin/env python3
"""v2 interactive dashboard. Writes dashboard/index.html (standalone, with doctype/meta, CSV export) and
dashboard/artifact.html (fragment for publishing as a claude.ai artifact). Definitions match the analysis
(analysis_common.load): usable set, embodied set, governance documents."""
import json, math, sys, pandas as pd, numpy as np
sys.path.insert(0,"/home/user/embodied-ai-governance-v5/scripts")
from analysis_common import load, PR, PRL, L1
B="/home/user/embodied-ai-governance-v5/"
m=load()
def s(v): return "" if (v is None or (isinstance(v,float) and math.isnan(v))) else str(v)
def i(v):
    try: return None if pd.isna(v) else int(v)
    except Exception: return None
rows=[]
for _,r in m.iterrows():
    cats=[c for c in s(r.embodied_categories).split("; ") if c]
    rows.append({"id":r.doc_id,"t":s(r.title_en)[:220],"to":s(r.title_clean)[:220],"y":i(r.year_final),"ys":s(r.year_source),"c":s(r.jurisdiction_country),"cn":s(r.jurisdiction_country_name),
        "reg":s(r.study_region),"col":s(r.collection_region),"set":s(r.collection_set),"tier":s(r.collection_tier),"dt":s(r.doc_type),"dc":s(r.doc_class),"gov":bool(r.gov),
        "st":s(r.instrument_status),"bn":s(r.binding_nature),"sc":s(r.ai_scope),"emb":s(r.embodiment_status),"l1":sorted(set(L1.get(c,"Other embodied") for c in cats)),"pe":s(r.primary_embodied_category),"ec":cats,
        "pt":s(r.primary_topic),"tp":s(r.governance_topics),"mech":s(r.governance_mechanisms),"inst":s(r.named_instruments_referenced),"sec":s(r.application_sectors),"iss":s(r.issuer_type),
        "au":s(r.authors_or_issuer)[:300],"lang":s(r.language),"rel":i(r.relevance_to_embodied_ai_governance),"conf":(None if pd.isna(r.confidence) else round(float(r.confidence),2)),
        "pq":s(r.page_quality),"sum":s(r.summary_en),"kp":s(r.key_provisions_or_claims),"url":s(r.source_url),"ven":s(r.venue),"doi":s(r.doi),"rf":s(r.risk_framing),"str":s(r.stance_toward_regulation),
        "meth":s(r.methodology),"rlp":s(r.robot_legal_personhood_position),"words":i(r.words),"txt":s(r.text_status),"cit":i(r.get("oa_cited_by")),
        "pr":[i(r.get("pr_"+p)) or 0 for p in PR],"us":bool(r.usable),"es":bool(r.embodied_set),"gs":bool(r.general_set),
        "r2":bool(r.round2),"r3":s(r.collection_set)=="round3","bp":s(r.get("bound_parties")),"eif":s(r.get("entry_into_force_date")),"app":s(r.get("applicability_date")),"rep":s(r.get("repeal_or_expiry_date")),"les":s(r.get("legal_effect_of_standard")),"rpy":i(r.get("robot_provision_year")),"rpb":s(r.get("robot_provision_basis")),"ft":s(r.get("_fulltext_v5"))=="True","unit":s(r.get("instrument_unit")),"pi":bool(r.instrument),"fam":i(r.get("family_size")) or 1,"ai":bool(r.ai_explicit),"auto":bool(r.autonomy_terms),"na":s(r.ai_scope)=="not_ai"})
data=json.dumps(rows,ensure_ascii=False,separators=(",",":"))
u=m[m.usable]; N=len(m); NU=len(u); NE=int(u.embodied_set.sum()); NG=int(u.instrument.sum()); NB=int((u.binding&u.instrument).sum()); NBE=int((u.binding&u.instrument&u.embodied_set).sum()); NGE=int((u.instrument&u.embodied_set).sum())
NBE_ALL=int((u.binding&u.embodied_set).sum()); NR2=int(u.round2.sum()); NR3=int((u.collection_set=="round3").sum()); NR2I=int((u.round2&u.instrument&u.embodied_set).sum()); NNA=int((u.ai_scope=="not_ai").sum())
NAIE=int((u.binding&u.instrument&u.embodied_set&u.ai_explicit).sum()); NAUE=int((u.binding&u.instrument&u.embodied_set&u.autonomy_terms).sum())
# reliability medians for the methods panel (whatever files exist)
import os
def kmed(path):
    try:
        d=pd.read_csv(path); d=d[d.type.isin(["single","ordinal"])] if "type" in d.columns else d; return f"{d.kappa.median():.2f}"
    except Exception: return "n/a"
KAP={"opus":kmed(B+"data/reliability_fields.csv"),"rerun":kmed(B+"data/reliability_fields_retest.csv"),"full":kmed(B+"data/reliability_fields_fulltext.csv"),"blind":kmed(B+"data/reliability_fields_blind.csv"),"r2opus":kmed(B+"data/reliability_fields_r2opus.csv"),"r2rerun":kmed(B+"data/reliability_fields_r2rerun.csv")}
PEU=round(100*(u.study_region=="Europe").mean()); PEN=round(100*(u.language=="en").mean()); NZH=int(u.language.isin(["zh","zh-cn","zh-tw"]).sum()); NJA=int((u.language=="ja").sum())
SOC=["social_companion_robots","care_assistive_robots","humanoid_general_purpose"]; _soc=u[u.embodied_set&u.embodied_categories.fillna("").map(lambda s: any(c in s for c in SOC))]; NESOC=len(_soc); NBSOC=int((_soc.binding&_soc.instrument).sum())
NC=u[~u.jurisdiction_country.isin(["EU","INT","XX"])].jurisdiction_country.nunique(); YMIN=int(u.year_final.min()); YMAX=int(u.year_final.max())
body=r'''<title>Embodied AI Governance Corpus</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&display=swap">
<style>
:root{--bg:#f9f9f7;--surface:#fcfcfb;--fg:#0b0b0b;--fg2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;--ring:rgba(11,11,11,.10);--accent:#2a78d6;--accent-ink:#1c5cab;--wash:#eef4fc;
--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#e87ba4;--s6:#008300;--s7:#6250d6;--s8:#e34948;--seq2:#86b6ef;--seq5:#1c5cab;--ui:"Public Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d0d0d;--surface:#1a1a19;--fg:#f0efec;--fg2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);--accent:#3987e5;--accent-ink:#86b6ef;--wash:#16233a;
--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;--seq2:#184f95;--seq5:#86b6ef;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0d0d0d;--surface:#1a1a19;--fg:#f0efec;--fg2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);--accent:#3987e5;--accent-ink:#86b6ef;--wash:#16233a;
--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;--seq2:#184f95;--seq5:#86b6ef;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--ui);font-size:15px;line-height:1.5}
.wrap{max-width:1360px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1{font-size:28px;font-weight:700;margin:0 0 6px;letter-spacing:-.01em;text-wrap:balance}h2{font-size:16px;font-weight:600;margin:0 0 2px}h3{font-size:15px;margin:14px 0 6px}
.sub{color:var(--fg2);max-width:78ch;margin:0 0 14px}.eyebrow{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}
.story{background:var(--wash);border:1px solid var(--ring);border-radius:6px;padding:12px 14px;margin:0 0 16px;max-width:100ch}.story b{font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:14px}
.tile{background:var(--surface);border:1px solid var(--ring);border-radius:6px;padding:12px 14px}.tile .v{font-size:28px;font-weight:600;line-height:1.1;margin-top:2px}.tile .l{color:var(--fg2);font-size:13px}.tile .n{color:var(--muted);font-size:12px}
.start{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 16px}.start .lbl{color:var(--fg2);font-size:13px;margin-right:4px}
.start button{border-radius:16px;padding:5px 12px}.start button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.filters{display:flex;flex-wrap:wrap;gap:8px 10px;align-items:end;background:var(--surface);border:1px solid var(--ring);border-radius:6px;padding:10px 12px;margin-bottom:8px;position:sticky;top:env(safe-area-inset-top,0px);z-index:5}
.filters label{display:flex;flex-direction:column;gap:3px;font-size:12px;color:var(--fg2);min-width:0}.filters label.chk{flex-direction:row;align-items:center;gap:6px;align-self:center;padding-bottom:4px}
.filters select,.filters input{font:inherit;font-size:14px;color:var(--fg);background:var(--bg);border:1px solid var(--axis);border-radius:4px;padding:5px 7px;min-width:140px;max-width:260px}
.filters input[type=number]{min-width:90px;width:90px}.filters input[type=search]{min-width:220px}.filters .cnt{font-weight:600;color:var(--fg);align-self:center;padding-bottom:4px;white-space:nowrap}
button{font:inherit;font-size:14px;color:var(--fg);background:var(--surface);border:1px solid var(--axis);border-radius:4px;padding:6px 10px;cursor:pointer}button:hover{border-color:var(--accent)}button:focus-visible,select:focus-visible,input:focus-visible,tr:focus-visible,.cardrow:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.charts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:14px 0 22px}@media (max-width:860px){.charts{grid-template-columns:1fr}}
.card{background:var(--surface);border:1px solid var(--ring);border-radius:6px;padding:12px 14px;min-width:0}.card .hd{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;margin-bottom:4px}
.card .hd small{display:block;color:var(--muted);font-size:12px;font-weight:400}.tbl-toggle{font-size:12px;padding:3px 8px;white-space:nowrap}
svg{display:block;width:100%;height:auto;font-family:var(--ui)}svg text{fill:var(--fg2);font-size:12px}svg .ax{stroke:var(--axis);stroke-width:1}svg .gr{stroke:var(--grid);stroke-width:1}svg .lab{fill:var(--fg)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:var(--fg2);margin-top:6px}.legend span{display:inline-flex;align-items:center;gap:5px}.legend i{width:10px;height:10px;border-radius:2px;display:inline-block}
.mini{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}.mini td,.mini th{padding:3px 6px;border-bottom:1px solid var(--grid);text-align:right;font-variant-numeric:tabular-nums}.mini td:first-child,.mini th:first-child{text-align:left}
#tip{position:fixed;pointer-events:none;background:var(--fg);color:var(--bg);padding:6px 8px;border-radius:4px;font-size:13px;max-width:300px;z-index:20;opacity:0;transition:opacity .08s}
.views{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin:0 0 8px}.views button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.tablewrap{overflow-x:auto;background:var(--surface);border:1px solid var(--ring);border-radius:6px}
table.docs{border-collapse:collapse;width:100%;min-width:980px;font-size:13.5px}table.docs th{position:sticky;top:0;background:var(--surface);text-align:left;font-weight:600;padding:8px 8px;border-bottom:1px solid var(--axis);cursor:pointer;white-space:nowrap;color:var(--fg2)}
table.docs th.on{color:var(--accent-ink)}table.docs th .sortbtn{all:unset;cursor:pointer;font:inherit;color:inherit}table.docs th .sortbtn:focus-visible{outline:2px solid var(--accent)}table.docs td{padding:6px 8px;border-bottom:1px solid var(--grid);vertical-align:top;max-width:420px}table.docs tr{cursor:pointer}table.docs tr:hover td{background:color-mix(in srgb,var(--accent) 8%,var(--surface))}
.num{font-variant-numeric:tabular-nums;text-align:right}.chip{display:inline-block;font-size:12px;padding:1px 7px;border-radius:10px;border:1px solid var(--ring);color:var(--fg2);white-space:nowrap}
.chip.bind{border-color:var(--s6);color:var(--s6);font-weight:600}.chip.soft{border-color:var(--s3)}.chip.prop{border-color:var(--s4)}.chip.res{border-color:var(--s7)}.chip.x{border-color:var(--s8);color:var(--s8)}
.cards{display:none}.cardrow{background:var(--surface);border:1px solid var(--ring);border-radius:6px;padding:10px 12px;margin-bottom:8px;cursor:pointer}.cardrow .t{font-weight:600}.cardrow .m{color:var(--fg2);font-size:13px;margin-top:2px}
@media (max-width:640px){.tablewrap{display:none}.cards{display:block}.filters{position:static;max-height:none}.filters.collapsed label,.filters.collapsed .cnt{display:none}.filters.collapsed{padding:8px 12px}.tile .v{font-size:22px}}
.ftoggle{display:none}@media (max-width:640px){.ftoggle{display:inline-block}}
.pager{display:flex;gap:8px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin:10px 0;color:var(--fg2);font-size:13px}
#drawer{position:fixed;top:0;right:0;bottom:0;width:min(600px,100%);background:var(--surface);border-left:1px solid var(--ring);box-shadow:-8px 0 24px rgba(0,0,0,.12);transform:translateX(102%);transition:transform .18s;z-index:30;overflow:auto;padding-block:16px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
#drawer.open{transform:none}#drawer h3{margin:4px 0 2px;font-size:17px;text-wrap:balance}#drawer .meta{display:grid;grid-template-columns:140px 1fr;gap:4px 10px;font-size:13.5px;margin:10px 0}#drawer .meta dt{color:var(--muted)}#drawer .meta dd{margin:0;min-width:0;overflow-wrap:anywhere}
#drawer .close{position:sticky;top:0;float:right}#drawer ul{padding-left:18px;margin:4px 0}.prbars{display:grid;grid-template-columns:1fr 1fr;gap:3px 14px;font-size:13px}.prbars div{display:flex;justify-content:space-between;gap:6px}.prbars b{font-weight:500}
.disc{font-size:12.5px;color:var(--muted);border-top:1px solid var(--grid);margin-top:12px;padding-top:8px}
details{background:var(--surface);border:1px solid var(--ring);border-radius:6px;padding:10px 14px;margin:14px 0}summary{cursor:pointer;font-weight:600}details dl{display:grid;grid-template-columns:200px 1fr;gap:4px 12px;font-size:14px}details dt{font-weight:600}details dd{margin:0}
@media (max-width:640px){details dl{grid-template-columns:1fr}#drawer .meta{grid-template-columns:1fr}}
.foot{color:var(--muted);font-size:13px;margin-top:20px;max-width:90ch}
@media (prefers-reduced-motion:reduce){#drawer,#tip{transition:none}}
</style>
<div class="wrap">
<div class="eyebrow">Who governs the robots? · document explorer</div>
<h1>Embodied AI Governance Corpus</h1>
<p class="sub"><a href="https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html">← Project hub: all deliverables of the study</a></p>
<p class="sub"><b>Embodied AI</b> means AI in a body: robots, self-driving vehicles, drones, surgical and factory machines. This explorer holds __N__ documents collected by eight regional teams and by a second round of searches of official legal databases, treaty archives, standards catalogues and regulator sites (laws, bills, strategies, standards, guidelines, government reports, research papers and news), each labelled by an AI model against a fixed codebook and checked against a second model on a sample. No human read every document; treat labels as consistent, not certified.</p>
<div class="story"><b>The story in one line:</b> the binding rules that reach robots are mostly aviation, road-vehicle, machinery and product law written for drones, self-driving cars and factory equipment (__NBE__ principal binding instruments in the embodied set, of which only __NAIE__ mention artificial intelligence explicitly and __NAUE__ contain autonomy or automation provisions); the robots people live with (companions, carers, humanoids) have __NBSOC__ binding rules among __NESOC__ documents about them. Counts are principal instruments: amendments count, but commencement orders, levies, individual exemptions, incorporation decisions and catalogue pages do not.</div>
<div class="story" style="margin-top:-8px"><b>What the second and third collection rounds changed:</b> __NR2__ usable documents were added from legal databases, standards catalogues and treaty archives (round 2) and by recovering the texts of round-2 candidates that could not be read before (round 3, __NR3__ documents), __NR2I__ of them principal instruments in the embodied set. Round 3 also re-read the 104 longest instruments in full and added, for every principal instrument, whom the rule binds, its dates, the legal effect of a standard and the year the robot provision arrived (shown in each record). The rise from a handful of binding robot rules to hundreds reflects where the first teams searched, not a change in the world; filter "Collected as" to compare rounds.</div>
<div class="tiles" id="tiles"></div>
<div class="start"><span class="lbl">Start here:</span>
 <button data-view="binding" type="button">The __NBE__ principal binding instruments that reach robots</button><button data-view="robot-rules" type="button">All __NGE__ principal robot rules and policies</button><button data-view="round2" type="button">Added in round 2</button><button data-view="round3" type="button">Added in round 3</button><button data-view="humanoids" type="button">Humanoid robots</button><button data-view="companions" type="button">Companion and social robots</button><button data-view="standards" type="button">Technical standards</button><button data-view="all" type="button">Everything</button></div>
<div class="filters" id="filters">
 <button class="ftoggle" id="ftoggle" type="button" aria-expanded="true">Filters</button>
 <label>Collected as<select id="f_set"><option value="">All</option><option value="sprint">Round 1: robot-specific sources</option><option value="database">Round 1: general-AI sources</option><option value="round2">Round 2: legal databases and repositories</option><option value="round3">Round 3: recovered and harvested instruments</option></select></label>
 <label>Region (by jurisdiction)<select id="f_reg"></select></label>
 <label>Document type<select id="f_dc"></select></label>
 <label>Robot focus<select id="f_es"><option value="">About AI (embodied or general)</option><option value="e">About robots or embodied AI</option><option value="g">General AI only</option><option value="n">Rated not about AI</option><option value="all">All documents incl. not about AI</option></select></label>
 <label>Robot group (any mention)<select id="f_l1"></select></label>
 <label>Robot type (any mention)<select id="f_ec"></select></label>
 <label>Instrument kind<select id="f_dt"></select></label>
 <label>Counting unit<select id="f_unit"><option value="">All documents</option><option value="pi">Principal instruments only</option><option value="anc">Ancillary, incorporation and catalogue items</option></select></label>
 <label>Rules and policies<select id="f_gov"><option value="">All</option><option value="1">Rules and policies only</option><option value="0">Everything else</option></select></label>
 <label>Year from<input id="f_y0" type="number" min="1990" max="2026" placeholder="min"></label>
 <label>Year to<input id="f_y1" type="number" min="1990" max="2026" placeholder="max"></label>
 <label>Search title, issuer, summary<input id="f_q" type="search" placeholder="e.g. surgical, ISO 13482, Korea"></label>
 <label class="chk"><input id="f_x" type="checkbox"> include excluded captures</label>
 <span class="cnt" id="count"></span><button id="f_reset" type="button">Reset</button>__EXPORT__
</div>
<div class="charts">
 <div class="card"><div class="hd"><h2>Where do the documents come from?<small>Region of the issuing body or first author; bars split by what the document is</small></h2><button class="tbl-toggle" data-t="c1" type="button">Table</button></div><div id="c1"></div></div>
 <div class="card"><div class="hd"><h2>When were they published?<small>Documents per year (2026 runs to October); earlier years grouped</small></h2><button class="tbl-toggle" data-t="c2" type="button">Table</button></div><div id="c2"></div></div>
 <div class="card"><div class="hd"><h2>Which robots do they discuss?<small>Documents mentioning each robot type (a document can mention several)</small></h2><button class="tbl-toggle" data-t="c3" type="button">Table</button></div><div id="c3"></div></div>
 <div class="card"><div class="hd"><h2>Which values do they discuss?<small>Documents that treat each principle in depth or mention it in passing</small></h2><button class="tbl-toggle" data-t="c4" type="button">Table</button></div><div id="c4"></div></div>
</div>
<div class="views"><span class="lbl" style="color:var(--fg2);font-size:13px">Columns:</span><button data-cols="docs" class="on" type="button">All documents</button><button data-cols="rules" type="button">Rules and policies</button><button data-cols="research" type="button">Research</button></div>
<div class="pager"><span id="count2"></span><span><button id="prev" type="button">Previous</button> <span id="page"></span> <button id="next" type="button">Next</button></span></div>
<div class="tablewrap"><table class="docs" id="docs"><thead><tr id="thead"></tr></thead><tbody></tbody></table></div>
<div class="cards" id="cards"></div>
<div class="pager"><span></span><span><button id="prev2" type="button">Previous</button> <span id="page2"></span> <button id="next2" type="button">Next</button></span></div>
<details><summary>What the labels mean (glossary)</summary><dl>
<dt>Embodied AI, physical AI</dt><dd>AI that controls a machine with a body: robots, self-driving vehicles, drones, surgical and factory machines, as opposed to AI that only produces text, images or decisions on a screen.</dd>
<dt>About robots or embodied AI</dt><dd>Documents the model rated at least moderately relevant to governing embodied AI, or that name a specific robot type. This is the "embodied-AI set" used in the report (__NE__ documents).</dd>
<dt>Rules and policies</dt><dd>Governance instruments: laws, regulations, decrees, bills, strategies, guidelines, codes of conduct, standards and resolutions. Research papers and news are not instruments.</dd>
<dt>Binding law</dt><dd>A statute, regulation, decree or order whose breach has legal consequences. "Voluntary guidance" (soft law) and technical standards cannot be enforced on their own, though laws often point to standards.</dd>
<dt>Technical standard</dt><dd>A detailed voluntary engineering specification (for example ISO 10218 for factory robots, ISO 13482 for care robots) that says how to make a machine safe.</dd>
<dt>Status</dt><dd>Where an instrument is in its life: proposal, bill under consideration, consultation open, adopted but not yet in force, in force, published and current, superseded or repealed.</dd>
<dt>In depth vs in passing</dt><dd>A principle is "in depth" when the document says what must be done, by whom and how it is checked; "in passing" when it is only named.</dd>
<dt>Relevance</dt><dd>The model's 0 to 3 rating of how central embodied-AI governance is to the document (3 = the document is about it).</dd>
<dt>Confidence</dt><dd>The model's own 0 to 1 confidence in its labels; lower for partial captures and landing pages.</dd>
<dt>Excluded captures</dt><dd>Files that were bot-walls, empty pages, wrong documents or off-topic; hidden by default and listed when the box is ticked.</dd>
</dl></details>
<details><summary>How the data were made, and what to be careful about</summary>
<p>Eight regional teams collected sources in two exercises (round 1): a sprint for robot-specific material and a database of general AI-governance instruments. A second collection round then searched official legal databases (EUR-Lex, legislation.gov.uk, the Japanese e-Gov law API, the Chinese State Council policy library, the Australian Federal Register, the US eCFR), treaty-body archives, standards catalogues and regulator sites for instruments the teams had missed; candidates were de-duplicated against round 1 and their texts fetched directly from the issuing source. Files were converted to text, duplicates merged, and every document was labelled by Claude Sonnet 5.5 under a fixed codebook (39 fields). A second model (Claude Opus 5.5) re-labelled a 160-document round-1 sample (median kappa __KOPUS__); the main model was re-run on the same sample (__KRERUN__) and on the full text instead of an excerpt (__KFULL__); a 160-document round-2 sample was re-labelled by the second model (__KR2OPUS__) and re-run (__KR2RERUN__). Keyword searches over the full text were used as an independent check. Years are the dates stated in the documents, inferred from content where unstated.</p>
<p>Generated __DATE__ from data/master_table.csv (__N__ captured documents; __NU__ usable). Figure data and tables are in the project package.</p>
<p>Be careful with: Europe is __PEU__% of the usable documents and English __PEN__%; __NZH__ usable documents are in Chinese and __NJA__ in Japanese, nearly all from round 2; the first round sought research on robots and official texts on AI in general and the second sought instruments, so the ratio of research to rules is by design; counts of instruments are lower bounds (the collection is not a census) and are reported as principal instruments (__NBE__ binding in the embodied set; __NBE_ALL__ if every legal text is counted); __NNA__ usable documents rated "not about AI" (mostly harvested statutes in which the technology terms are incidental) are hidden unless the robot-focus filter includes them; the agreement checks are median kappa __KOPUS__ (second model), __KRERUN__ (re-run), __KFULL__ (full text) and __KBLIND__ (metadata-blind) on round-1 samples and __KR2OPUS__ (second model) and __KR2RERUN__ (re-run) on a round-2 sample; the round-2 collectors were AI agents working from legal databases; 2026 runs to October; percentages over small groups (fewer than 30 documents) are shown as counts.</p>
</details>
<p class="foot">Region follows the issuing jurisdiction or first author's affiliation, so it can differ from the folder a document was collected under. "Year" is the annotated publication or adoption date, falling back to OpenAlex for DOI-matched papers and then to PDF metadata. Summaries in the record panel were written by the AI model from the document text.</p>
</div>
<div id="tip"></div>
<aside id="drawer" role="dialog" aria-modal="true" aria-label="Document details" tabindex="-1"><button class="close" type="button" id="dclose">Close</button><div id="dbody"></div></aside>
<script>
const DATA=__DATA__;
const PR=__PR__;
const PRL={transparency:"Transparency",justice_fairness:"Justice & fairness",non_maleficence:"Avoiding harm",responsibility_accountability:"Accountability",privacy:"Privacy",beneficence:"Benefit & well-being",freedom_autonomy:"Human freedom & autonomy",trust:"Trust",sustainability:"Sustainability",dignity:"Dignity",solidarity:"Solidarity",human_oversight:"Human oversight",robustness_security:"Robustness & security",inclusive_growth:"Inclusive growth",physical_safety:"Physical safety",human_robot_proximity:"Human-robot proximity",liability_for_physical_damage:"Liability for physical damage",autonomy_level_control:"Autonomy level & control",conformity_assessment_certification:"Conformity assessment",dual_use_military:"Dual use & military"};
const DCL={governance_instrument_binding:"Binding law",governance_instrument_soft:"Voluntary guidance or standard",governance_proposal_or_draft:"Proposal or bill",government_report_or_parliamentary:"Government or parliamentary report",research_output:"Research paper",grey_literature:"NGO, industry or think-tank report",communication_or_news:"News, press release or web page",unusable:"Excluded capture"};
const DCO=Object.keys(DCL);
const SCL={general_ai_only:"General AI only",general_ai_with_embodied_provisions:"General AI with robot provisions",embodied_ai_robotics_general:"Robots or embodied AI in general",embodied_ai_specific_category:"A specific robot type",not_ai:"Not about AI"};
const STL={proposal_or_concept:"Proposal",draft_or_bill_under_consideration:"Bill under consideration",consultation_open:"Consultation open",adopted_not_yet_in_force:"Adopted, not yet in force",in_force:"In force",published_current:"Published, current",under_development:"Under development",superseded_or_repealed:"Superseded or repealed",withdrawn_or_lapsed:"Withdrawn",unknown:"Status unknown",not_applicable:""};
const BNL={legally_binding:"Binding",voluntary_soft_law:"Voluntary",technical_standard_voluntary:"Standard (voluntary)",technical_standard_mandated:"Standard (mandated)",not_applicable:""};
const RELL=["not relevant","marginal","relevant","central"];
const CLR=["var(--s1)","var(--s2)","var(--s3)","var(--s4)","var(--s5)","var(--s6)","var(--s7)","var(--muted)"];
const nice=s=>s?s.replace(/_/g," ").replace(/^./,c=>c.toUpperCase()).replace(/\bai\b/gi,"AI").replace(/\bihl\b/gi,"IHL").replace(/\buas\b/gi,"UAS").replace(/\bUsa\b/,"USA"):"";
const short=s=>s==="Latin America & Caribbean"?"Latin America":s;
const $=id=>document.getElementById(id);
const esc=v=>String(v==null?"":v).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
let CW=640;function measure(){const c=document.getElementById("c1");CW=Math.max(320,Math.min(760,(c?c.clientWidth:640)-4));}
const USABLE=DATA.filter(d=>d.us);
function opts(id,vals,labeler,counter){const sel=$(id);sel.innerHTML='<option value="">All</option>'+vals.map(v=>`<option value="${v}">${labeler?labeler(v):nice(v)}${counter?` (${counter(v)})`:""}</option>`).join("");}
const uniq=(k,src)=>[...new Set(src.map(d=>d[k]).filter(Boolean))].sort();
opts("f_reg",uniq("reg",USABLE),v=>v,v=>USABLE.filter(d=>d.reg===v).length);
opts("f_dc",DCO.filter(k=>USABLE.some(d=>d.dc===k)),v=>DCL[v],v=>USABLE.filter(d=>d.dc===v).length);
const ECS=[...new Set(USABLE.flatMap(d=>d.ec))].sort();opts("f_ec",ECS,v=>nice(v),v=>USABLE.filter(d=>d.ec.includes(v)).length);
const DTS=[...new Set(USABLE.map(d=>d.dt).filter(Boolean))].sort();opts("f_dt",DTS,v=>nice(v),v=>USABLE.filter(d=>d.dt===v).length);
const L1S=[...new Set(USABLE.flatMap(d=>d.l1))].sort();opts("f_l1",L1S,v=>v,v=>USABLE.filter(d=>d.l1.includes(v)).length);
let sortK="_default",sortD=1,page=0,PAGE=50,cur=[],cols="docs",view="";
const F=()=>({set:$("f_set").value,reg:$("f_reg").value,dc:$("f_dc").value,es:$("f_es").value,l1:$("f_l1").value,ec:$("f_ec").value,dt:$("f_dt").value,unit:$("f_unit").value,gov:$("f_gov").value,y0:+$("f_y0").value||null,y1:+$("f_y1").value||null,q:$("f_q").value.trim().toLowerCase(),x:$("f_x").checked});
const focusOk=(d,es)=>es===""?(d.es||d.gs):es==="e"?d.es:es==="g"?d.gs:es==="n"?d.na:true;
function filt(){const f=F();
 return DATA.filter(d=>(f.x||d.us)&&(!f.set||d.set===f.set)&&(!f.reg||d.reg===f.reg)&&(!f.dc||d.dc===f.dc)&&focusOk(d,f.es)&&(!f.l1||d.l1.includes(f.l1))&&(!f.ec||d.ec.includes(f.ec))&&(!f.dt||d.dt===f.dt)&&(!f.unit||(f.unit==="pi"?d.pi:(d.gov&&!d.pi)))&&(f.gov===""||(f.gov==="1")===d.pi)&&(!f.y0||(d.y&&d.y>=f.y0))&&(!f.y1||(d.y&&d.y<=f.y1))&&(!f.q||(d.t+" "+d.to+" "+d.au+" "+d.sum+" "+d.inst+" "+d.cn+" "+d.id+" "+d.ec.join(" ")).toLowerCase().includes(f.q)));}
function tiles(rows){const gov=rows.filter(d=>d.pi).length,bind=rows.filter(d=>d.pi&&d.dc==="governance_instrument_binding").length,emb=rows.filter(d=>d.es).length,r2=rows.filter(d=>d.r2).length,cty=new Set(rows.map(d=>d.c).filter(c=>c&&!["EU","INT","XX"].includes(c))).size,ys=rows.map(d=>d.y).filter(y=>y&&y>=1990);
 const t=[["Documents",rows.length,`of ${DATA.length} captured`],["About robots or embodied AI",emb,"the embodied-AI set"],["Principal rules and policies",gov,"laws, strategies, guidance, standards; paperwork excluded"],["Principal binding laws",bind,`${rows.filter(d=>d.pi&&d.es&&d.dc==="governance_instrument_binding").length} reach robots`],["Added in rounds 2 and 3",r2,"legal databases, catalogues and recovered texts"],["Countries",cty,"plus EU and international bodies"],["Years",ys.length?Math.min(...ys)+" to "+Math.max(...ys):"n/a","2026 to October"]];
 $("tiles").innerHTML=t.map(([l,v,n])=>`<div class="tile"><div class="l">${l}</div><div class="v">${v}</div><div class="n">${n}</div></div>`).join("");}
const tip=$("tip");function showTip(e,html){tip.innerHTML=html;tip.style.opacity=1;const x=Math.min(e.clientX+12,window.innerWidth-310),y=e.clientY+14;tip.style.left=x+"px";tip.style.top=y+"px";}function hideTip(){tip.style.opacity=0;}
const tableMode={};
function hbars(el,rows,series,o){const W=CW,lw=Math.min(o.lw||190,Math.round(W*0.34)),bh=20,gap=6,top=6,H=top+rows.length*(bh+gap)+24;const max=Math.max(1,...rows.map(r=>r.vals.reduce((a,b)=>a+b,0)));const pw=W-lw-56;
 let svg=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.aria||''}">`;
 for(let i=0;i<=4;i++){const x=lw+pw*i/4;svg+=`<line class="gr" x1="${x}" x2="${x}" y1="${top}" y2="${H-22}"/><text x="${x}" y="${H-6}" text-anchor="middle">${Math.round(max*i/4)}</text>`;}
 rows.forEach((r,ri)=>{const y=top+ri*(bh+gap);let x=lw;const lab=r.label.length>30?r.label.slice(0,29)+"…":r.label;svg+=`<text class="lab" x="${lw-8}" y="${y+bh*0.72}" text-anchor="end"><title>${r.label}</title>${lab}</text>`;
  r.vals.forEach((v,si)=>{if(!v)return;const w=pw*v/max;const last=r.vals.slice(si+1).every(z=>!z);svg+=`<rect x="${x}" y="${y}" width="${Math.max(0,w-2)}" height="${bh}" fill="${series[si].color}" rx="${last?4:0}" data-l="${r.label}" data-s="${series[si].name}" data-v="${v}"/>`;x+=w;});
  svg+=`<text x="${x+5}" y="${y+bh*0.72}">${r.vals.reduce((a,b)=>a+b,0)}</text>`;});
 svg+=`<line class="ax" x1="${lw}" x2="${lw}" y1="${top}" y2="${H-22}"/></svg>`;
 const leg=series.length>1?`<div class="legend">${series.map(s=>`<span><i style="background:${s.color}"></i>${s.name}</span>`).join("")}</div>`:"";
 const tser=o.tableSeries||series;const tbl=`<table class="mini"><tr><th>${o.rowName||""}</th>${tser.map(s=>`<th>${s.name}</th>`).join("")}<th>Total</th></tr>${rows.map(r=>{const tv=o.tableVals?o.tableVals(r):r.vals;return `<tr><td>${r.label}</td>${tv.map(v=>`<td>${v}</td>`).join("")}<td>${tv.reduce((a,b)=>a+b,0)}</td></tr>`;}).join("")}</table>`;
 el.innerHTML=tableMode[el.id]?tbl:svg+leg;
 el.querySelectorAll("rect").forEach(rc=>{rc.addEventListener("mousemove",e=>showTip(e,`<b>${rc.dataset.l}</b><br>${rc.dataset.s}: ${rc.dataset.v}`));rc.addEventListener("mouseleave",hideTip);});}
function vbars(el,rows,o){const W=CW,H=230,lw=40,bot=30,pw=W-lw-12,ph=H-bot-10;const max=Math.max(1,...rows.map(r=>r.v));const bw=pw/rows.length;const bwid=Math.min(24,bw-2);
 let svg=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.aria||''}">`;for(let i=0;i<=4;i++){const y=10+ph-ph*i/4;svg+=`<line class="gr" x1="${lw}" x2="${W-12}" y1="${y}" y2="${y}"/><text x="${lw-6}" y="${y+4}" text-anchor="end">${Math.round(max*i/4)}</text>`;}
 rows.forEach((r,i)=>{const h=ph*r.v/max,x=lw+i*bw+(bw-bwid)/2,y=10+ph-h;svg+=`<rect x="${x}" y="${y}" width="${Math.max(1,bwid)}" height="${h}" fill="var(--s1)" data-l="${esc(r.label)}" data-v="${r.v}"/>`;if(i%2===rows.length%2||rows.length<=12)svg+=`<text x="${x+bw/2}" y="${H-8}" text-anchor="middle">${r.label}</text>`;});
 svg+=`<line class="ax" x1="${lw}" x2="${W-12}" y1="${10+ph}" y2="${10+ph}"/></svg>`;
 const tbl=`<table class="mini"><tr><th>Year</th><th>Documents</th></tr>${rows.map(r=>`<tr><td>${r.label}</td><td>${r.v}</td></tr>`).join("")}</table>`;
 el.innerHTML=tableMode[el.id]?tbl:svg;el.querySelectorAll("rect").forEach(rc=>{rc.addEventListener("mousemove",e=>showTip(e,`<b>${rc.dataset.l}</b><br>${rc.dataset.v} documents`));rc.addEventListener("mouseleave",hideTip);});}
const GRP=[["Research",["research_output"],"var(--s1)"],["News, web pages, reports",["communication_or_news","grey_literature","unusable"],"var(--s2)"],["Voluntary guidance, standards, bills",["governance_instrument_soft","governance_proposal_or_draft"],"var(--s3)"],["Government reports",["government_report_or_parliamentary"],"var(--s4)"],["Binding laws",["governance_instrument_binding"],"var(--s6)"]];
function charts(rows){
 if(!rows.length){["c1","c2","c3","c4"].forEach(id=>$(id).innerHTML='<p style="color:var(--muted)">No documents match the current filters.</p>');return;}
 const regs=[...new Set(rows.map(d=>d.reg))].filter(Boolean);const r1=regs.map(g=>({label:short(g),vals:GRP.map(([n,ks])=>rows.filter(d=>d.reg===g&&ks.includes(d.dc)).length),full:DCO.map(k=>rows.filter(d=>d.reg===g&&d.dc===k).length)})).sort((a,b)=>b.vals.reduce((x,y)=>x+y,0)-a.vals.reduce((x,y)=>x+y,0));
 hbars($("c1"),r1,GRP.map(([n,ks,c])=>({name:n,color:c})),{rowName:"Region",aria:"Documents by region stacked by document type",lw:150,tableSeries:DCO.map(k=>({name:DCL[k]})),tableVals:r=>r.full});
 const ys={};rows.forEach(d=>{if(d.y){const k=d.y<2014?"pre-2014":String(d.y);ys[k]=(ys[k]||0)+1;}});const yk=Object.keys(ys).sort((a,b)=>(a==="pre-2014"?-1:b==="pre-2014"?1:a-b));
 vbars($("c2"),yk.map(k=>({label:k,v:ys[k]})),{aria:"Documents by year"});
 const ec={};rows.forEach(d=>d.ec.forEach(c=>ec[c]=(ec[c]||0)+1));const r3=Object.entries(ec).sort((a,b)=>b[1]-a[1]).slice(0,14).map(([k,v])=>({label:nice(k),vals:[v]}));
 hbars($("c3"),r3.length?r3:[{label:"No robot types in selection",vals:[0]}],[{name:"Documents",color:"var(--s1)"}],{rowName:"Robot type",aria:"Robot types mentioned",lw:210});
 const r4=PR.map((p,i)=>({label:PRL[p],vals:[rows.filter(d=>d.pr[i]===2).length,rows.filter(d=>d.pr[i]===1).length]})).sort((a,b)=>(b.vals[0]+b.vals[1])-(a.vals[0]+a.vals[1]));
 hbars($("c4"),r4,[{name:"Discussed in depth",color:"var(--seq5)"},{name:"Mentioned in passing",color:"var(--seq2)"}],{rowName:"Principle",aria:"Principles discussed",lw:210});}
const chipCls={governance_instrument_binding:"bind",governance_instrument_soft:"soft",governance_proposal_or_draft:"prop",research_output:"res",unusable:"x"};
const COLS={docs:[["id","ID"],["t","Title"],["y","Year"],["cn","Jurisdiction"],["reg","Region"],["dt","Document type"],["st","Status"],["pe","Main robot type"],["pt","Main topic"],["rel","Relevance"],["lang","Lang"]],
 rules:[["id","ID"],["t","Instrument"],["y","Year"],["cn","Jurisdiction"],["dt","Type"],["st","Status"],["bn","Binding?"],["ec","Robot types covered"],["mech","Mechanisms"],["iss","Issuer"]],
 research:[["id","ID"],["t","Title"],["y","Year"],["cn","Country"],["ven","Venue"],["meth","Method"],["pe","Main robot type"],["pt","Main topic"],["str","Stance on regulation"],["cit","Citations"]]};
const rank=d=>(d.dc==="governance_instrument_binding"?0:d.gov?1:d.dc==="government_report_or_parliamentary"?2:3);
function cell(d,k){switch(k){case "t":return `${esc(d.t||d.to)} <span class="chip ${chipCls[d.dc]||""}">${DCL[d.dc]||""}</span>`;case "y":return `<span class="num">${d.y||""}</span>`;case "st":return STL[d.st]||"";case "bn":return BNL[d.bn]||"";case "pe":return d.pe==="none"?"":nice(d.pe);case "ec":return d.ec.map(nice).join(", ");case "mech":return d.mech.split("; ").filter(Boolean).map(nice).join(", ");case "rel":return d.rel==null?"":`${d.rel}/3 ${RELL[d.rel]}`;case "cit":return d.cit==null?"":d.cit;default:return nice(d[k]==null?"":String(d[k]));}}
function renderTable(){const tb=$("docs").querySelector("tbody");const rows=cur.slice().sort((a,b)=>{if(sortK==="_default"){const r=rank(a)-rank(b);if(r)return r;const y=(b.y||0)-(a.y||0);if(y)return y;return (b.rel||0)-(a.rel||0);}const x=a[sortK],y=b[sortK];if(x==null&&y==null)return 0;if(x==null)return 1;if(y==null)return -1;return (x>y?1:x<y?-1:0)*sortD;});
 const pages=Math.max(1,Math.ceil(rows.length/PAGE));page=Math.min(page,pages-1);const sl=rows.slice(page*PAGE,(page+1)*PAGE);const C=COLS[cols];
 $("thead").innerHTML=C.map(([k,l])=>`<th data-k="${k}" class="${k===sortK?"on":""}" aria-sort="${k===sortK?(sortD>0?"ascending":"descending"):"none"}"><button type="button" class="sortbtn">${l}${k===sortK?(sortD>0?" ▲":" ▼"):""}</button></th>`).join("");
 tb.innerHTML=sl.map(d=>`<tr tabindex="0" data-id="${d.id}">${C.map(([k])=>`<td>${cell(d,k)}</td>`).join("")}</tr>`).join("");
 $("cards").innerHTML=sl.map(d=>`<div class="cardrow" tabindex="0" data-id="${d.id}"><div class="t">${esc(d.t||d.to)}</div><div class="m">${d.y||"n.d."} · ${d.cn||d.reg} · ${DCL[d.dc]||""}${d.pe&&d.pe!=="none"?" · "+nice(d.pe):""}</div></div>`).join("");
 $("count").textContent=`${rows.length} match`;$("count2").textContent=`${rows.length} documents (sorted: binding laws, then rules, then by year)`;$("page").textContent=`Page ${page+1} of ${pages}`;$("page2").textContent=`Page ${page+1} of ${pages}`;
 document.querySelectorAll("#thead th").forEach(th=>th.querySelector("button").addEventListener("click",()=>{if(sortK===th.dataset.k)sortD*=-1;else{sortK=th.dataset.k;sortD=(sortK==="y"||sortK==="rel"||sortK==="cit")?-1:1;}renderTable();}));}
function update(){measure();cur=filt();tiles(cur);charts(cur);renderTable();}
let rto;window.addEventListener("resize",()=>{clearTimeout(rto);rto=setTimeout(()=>{measure();charts(cur);},150);});
function drawer(d){const pr=PR.map((p,i)=>[PRL[p],d.pr[i]]).filter(x=>x[1]>0).sort((a,b)=>b[1]-a[1]);
 const li=s=>s?`<ul>${s.split("; ").map(x=>`<li>${x}</li>`).join("")}</ul>`:"<span style='color:var(--muted)'>none</span>";
 $("dbody").innerHTML=`<div class="eyebrow">${d.id} · ${DCL[d.dc]||""}${d.us?"":" · excluded from analysis"}</div><h3>${esc(d.t)}</h3>${d.to&&d.to!==d.t?`<div style="color:var(--fg2)">${esc(d.to)}</div>`:""}
 <p>${esc(d.sum)}</p>
 <dl class="meta"><dt>Authors / issuer</dt><dd>${esc(d.au)}</dd><dt>Issuer type</dt><dd>${nice(d.iss)}</dd><dt>Year</dt><dd>${d.y||"unknown"} <small style="color:var(--muted)">(${d.ys||"n/a"})</small></dd><dt>Jurisdiction</dt><dd>${d.cn} (${d.c}) · ${d.reg}</dd>
 <dt>Document type</dt><dd>${nice(d.dt)}</dd><dt>Rule or policy?</dt><dd>${d.gov?"yes · "+(STL[d.st]||nice(d.st))+(BNL[d.bn]?" · "+BNL[d.bn]:""):"no"}</dd><dt>Robot focus</dt><dd>${SCL[d.sc]||nice(d.sc)} · ${nice(d.emb)}</dd>
 <dt>Robot types</dt><dd>${d.ec.length?d.ec.map(nice).join(", "):"none"}</dd><dt>Sectors</dt><dd>${d.sec.split("; ").map(nice).join(", ")}</dd><dt>Topics</dt><dd>${d.tp.split("; ").map(nice).join(", ")}</dd>
 <dt>Mechanisms</dt><dd>${d.mech.split("; ").map(nice).join(", ")||"none"}</dd><dt>Instruments cited</dt><dd>${d.inst||"none"}</dd><dt>Framing</dt><dd>${nice(d.rf)}</dd><dt>Stance on regulation</dt><dd>${nice(d.str)}</dd><dt>Method</dt><dd>${nice(d.meth)}</dd><dt>Robot personhood</dt><dd>${nice(d.rlp)}</dd>
 <dt>Relevance / confidence</dt><dd>${d.rel==null?"":d.rel+" of 3 ("+RELL[d.rel]+")"} · ${d.conf==null?"":d.conf}</dd><dt>Capture quality</dt><dd>${nice(d.pq)} · ${d.txt} · ${d.words||0} words</dd><dt>Collected as</dt><dd>${d.set==="round3"?"round 3 · recovered or harvested instruments":d.set==="round2"?"round 2 · legal databases and repositories":d.set==="sprint"?"round 1 · robot-specific sources":"round 1 · general-AI sources"} · ${d.col}${d.tier?" · "+d.tier:""}</dd><dt>Counting unit</dt><dd>${d.gov?(d.pi?"principal instrument":"not counted as a principal instrument ("+nice(d.unit)+")")+(d.fam>1?" · one of "+d.fam+" versions/parts of one regime":""):"not an instrument"}</dd><dt>AI content in the text</dt><dd>${d.ai?"mentions AI explicitly":d.auto?"autonomy or automation provisions, no explicit AI":"neither AI nor autonomy terms found"}</dd>
 ${d.bp&&!["","none_stated","not_applicable"].includes(d.bp)?`<dt>Binds whom</dt><dd>${d.bp.split("; ").map(nice).join(", ")}</dd>`:""}${d.eif||d.app||d.rep?`<dt>Dates in the text</dt><dd>${d.eif?"in force "+d.eif:""}${d.app?" · applies "+d.app:""}${d.rep?" · repealed/expires "+d.rep:""}</dd>`:""}${d.les&&d.les!=="not_a_standard"&&d.les!=="unknown"?`<dt>Legal effect of standard</dt><dd>${nice(d.les)}</dd>`:""}${d.rpy?`<dt>Robot provision dated</dt><dd>${d.rpy}${d.rpb?" · "+nice(d.rpb):""}</dd>`:""}${d.ft?`<dt>Read in full</dt><dd>yes · full text re-read in round 3</dd>`:""} ${d.ven?`<dt>Venue</dt><dd>${d.ven}</dd>`:""}${d.cit!=null?`<dt>Citations (OpenAlex)</dt><dd>${d.cit}</dd>`:""}${d.doi?`<dt>DOI</dt><dd>${d.doi}</dd>`:""}${d.url?`<dt>Source</dt><dd><a href="${d.url}" target="_blank" rel="noopener">${d.url.slice(0,70)}${d.url.length>70?"…":""}</a></dd>`:""}</dl>
 <div class="eyebrow">Key provisions or claims</div>${li(esc(d.kp))}
 <div class="eyebrow" style="margin-top:10px">Principles discussed (2 = in depth, 1 = in passing)</div><div class="prbars">${pr.map(([l,v])=>`<div><span>${l}</span><b>${v}</b></div>`).join("")||"none"}</div>
 <div class="disc">Summary, labels and key provisions were written by an AI model (Claude Sonnet 5.5) from an excerpt of the document and have not been verified by a person. Check the source before relying on them.</div>`;
 lastFocus=document.activeElement;$("drawer").classList.add("open");$("dclose").focus();}
let lastFocus=null;function closeDrawer(){$("drawer").classList.remove("open");if(lastFocus&&lastFocus.focus)lastFocus.focus();}
$("drawer").addEventListener("keydown",e=>{if(e.key==="Tab"){const f=$("drawer").querySelectorAll("button,a,[tabindex]:not([tabindex='-1'])");if(!f.length)return;const first=f[0],last=f[f.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}});
const VIEWS={all:{},binding:{dc:"governance_instrument_binding",es:"e",unit:"pi"},"robot-rules":{gov:"1",es:"e"},humanoids:{ec:"humanoid_general_purpose"},companions:{ec:"social_companion_robots"},standards:{dt:"technical_standard"},round2:{set:"round2"},round3:{set:"round3"}};
function applyView(v){const p=VIEWS[v];if(!p)return;["f_set","f_reg","f_dc","f_es","f_l1","f_ec","f_dt","f_unit","f_gov"].forEach(id=>$(id).value="");["f_y0","f_y1","f_q"].forEach(id=>$(id).value="");$("f_x").checked=false;
 if(p.dc)$("f_dc").value=p.dc;if(p.es)$("f_es").value=p.es;if(p.gov)$("f_gov").value=p.gov;if(p.l1)$("f_l1").value=p.l1;if(p.ec)$("f_ec").value=p.ec;if(p.dt)$("f_dt").value=p.dt;if(p.unit)$("f_unit").value=p.unit;if(p.set)$("f_set").value=p.set;if(p.q)$("f_q").value=p.q;
 view=v;document.querySelectorAll(".start button").forEach(b=>b.classList.toggle("on",b.dataset.view===v));page=0;update();}
document.querySelectorAll(".start button").forEach(b=>b.addEventListener("click",()=>{applyView(b.dataset.view);try{history.replaceState(null,"","#"+b.dataset.view);}catch(e){}}));
document.querySelectorAll(".views button").forEach(b=>b.addEventListener("click",()=>{cols=b.dataset.cols;document.querySelectorAll(".views button").forEach(x=>x.classList.toggle("on",x===b));page=0;renderTable();}));
["docs","cards"].forEach(id=>{$(id).addEventListener("click",e=>{const tr=e.target.closest("[data-id]");if(tr)drawer(DATA.find(d=>d.id===tr.dataset.id));});$(id).addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){const tr=e.target.closest("[data-id]");if(tr){e.preventDefault();drawer(DATA.find(d=>d.id===tr.dataset.id));}}});});
$("dclose").addEventListener("click",closeDrawer);document.addEventListener("keydown",e=>{if(e.key==="Escape")closeDrawer();});
["f_set","f_reg","f_dc","f_es","f_l1","f_ec","f_dt","f_unit","f_gov","f_x"].forEach(id=>$(id).addEventListener("change",()=>{page=0;view="";document.querySelectorAll(".start button").forEach(b=>b.classList.remove("on"));update();}));["f_y0","f_y1","f_q"].forEach(id=>$(id).addEventListener("input",()=>{page=0;update();}));
$("f_reset").addEventListener("click",()=>applyView("all"));
[["prev",-1],["next",1],["prev2",-1],["next2",1]].forEach(([id,dir])=>$(id).addEventListener("click",()=>{if(dir<0&&page>0){page--;renderTable();}if(dir>0){page++;renderTable();window.scrollTo({top:$("docs").getBoundingClientRect().top+window.scrollY-120});}}));
document.querySelectorAll(".tbl-toggle").forEach(b=>b.addEventListener("click",()=>{tableMode[b.dataset.t]=!tableMode[b.dataset.t];b.textContent=tableMode[b.dataset.t]?"Chart":"Table";charts(cur);}));
const ex=$("f_export");if(ex)ex.addEventListener("click",()=>{const C=COLS[cols];const esc=v=>'"'+String(v==null?"":v).replace(/"/g,'""')+'"';const lines=[C.map(([k,l])=>esc(l)).join(",")].concat(cur.map(d=>C.map(([k])=>esc(k==="ec"?d.ec.join("; "):k==="st"?(STL[d.st]||""):k==="bn"?(BNL[d.bn]||""):d[k])).join(",")));const blob=new Blob([lines.join("\n")],{type:"text/csv"});const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="embodied_ai_governance_filtered.csv";a.click();});
$("ftoggle").addEventListener("click",()=>{const f=$("filters");f.classList.toggle("collapsed");$("ftoggle").setAttribute("aria-expanded",String(!f.classList.contains("collapsed")));});if(window.innerWidth<640){$("filters").classList.add("collapsed");$("ftoggle").setAttribute("aria-expanded","false");}
const h=(location.hash||"").replace("#","");if(VIEWS[h])applyView(h);else update();
window.addEventListener("hashchange",()=>{const v=(location.hash||"").replace("#","");if(VIEWS[v])applyView(v);});
</script>'''
import datetime
body=body.replace("__DATE__",datetime.date.today().isoformat()).replace("__NU__",f"{NU:,}").replace("__DATA__",data).replace("__PR__",json.dumps(PR)).replace("__N__",f"{N:,}").replace("__NBE__",str(NBE)).replace("__NBSOC__",str(NBSOC)).replace("__NESOC__",str(NESOC)).replace("__NGE__",str(NGE)).replace("__NE__",f"{NE:,}").replace("__NBE_ALL__",str(NBE_ALL)).replace("__NR2I__",str(NR2I)).replace("__NR3__",str(NR3)).replace("__NR2__",f"{NR2:,}").replace("__NNA__",str(NNA)).replace("__NAIE__",str(NAIE)).replace("__NAUE__",str(NAUE)).replace("__PEU__",str(PEU)).replace("__PEN__",str(PEN)).replace("__NZH__",str(NZH)).replace("__NJA__",str(NJA)).replace("__KOPUS__",KAP["opus"]).replace("__KRERUN__",KAP["rerun"]).replace("__KFULL__",KAP["full"]).replace("__KBLIND__",KAP["blind"]).replace("__KR2OPUS__",KAP["r2opus"]).replace("__KR2RERUN__",KAP["r2rerun"])
frag=body.replace("__EXPORT__","")
import re as _re
frag=_re.sub(r'const ex=\$\("f_export"\);if\(ex\)ex\.addEventListener\("click",\(\)=>\{.*?\}\);\n',"",frag,flags=_re.S)
stand=body.replace("__EXPORT__",'<button id="f_export" type="button">Download CSV</button>')
stand='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+stand.split("<div class=\"wrap\">",1)[0]+'</head>\n<body>\n<div class="wrap">'+stand.split("<div class=\"wrap\">",1)[1]+'\n</body>\n</html>\n'
open(B+"dashboard/index.html","w",encoding="utf8").write(stand)
open(B+"dashboard/artifact.html","w",encoding="utf8").write(frag)
print("rows",N,"usable",NU,"embodied",NE,"gov",NG,"binding",NB,"binding embodied",NBE,"gov embodied",NGE,"countries",NC,"years",YMIN,YMAX,"size MB",round(len(stand.encode())/1e6,2))
