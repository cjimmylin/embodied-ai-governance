"""Apply documented manual corrections (data/manual_overrides.csv) to the master table.
Rows with field == duplicate_of are removed from the master table (recorded in data/duplicates_removed.csv);
other rows set a single field. The original v1 table is kept as data/master_table_v1.csv on first run."""
import pandas as pd, numpy as np, os, shutil, json
B="/home/user/embodied-ai-governance-v5/"
SRC=B+"data/master_table_raw.csv" if os.path.exists(B+"data/master_table_raw.csv") else B+"data/master_table_v1.csv"
if not os.path.exists(B+"data/master_table_v1.csv"): shutil.copy(B+"data/master_table.csv",B+"data/master_table_v1.csv")
m=pd.read_csv(SRC,low_memory=False); print("overrides applied to",SRC)
ov=pd.read_csv(B+"data/manual_overrides.csv")
dups=ov[ov.field=="duplicate_of"]
removed=m[m.doc_id.isin(dups.doc_id)][["doc_id","title_en","jurisdiction_country","year_final","doc_class"]].merge(dups[["doc_id","new_value","reason"]],on="doc_id").rename(columns={"new_value":"duplicate_of"})
removed.to_csv(B+"data/duplicates_removed.csv",index=False)
m=m[~m.doc_id.isin(dups.doc_id)].copy()
log=[]
for _,r in ov[ov.field!="duplicate_of"].iterrows():
    if r.doc_id not in set(m.doc_id): continue
    old=m.loc[m.doc_id==r.doc_id,r.field].iloc[0]
    val=r.new_value
    if r.field=="is_governance_document": val=(str(val).lower()=="true")
    if r.field=="year_final": val=(float(val) if isinstance(val,str) and val.strip() else (val if isinstance(val,(int,float)) and not pd.isna(val) else np.nan))
    m.loc[m.doc_id==r.doc_id,r.field]=val
    log.append({"doc_id":r.doc_id,"field":r.field,"old":old,"new":val,"reason":r.reason,"source":r.source})
pd.DataFrame(log).to_csv(B+"data/overrides_applied.csv",index=False)
# second deduplication pass: identical normalised title within the same jurisdiction (years within one) -> keep the fullest capture
import re as _re
def norm(t):
    t=str(t).lower(); t=_re.sub(r"[^a-z0-9\u00c0-\u024f\u0400-\u04ff\u0600-\u06ff\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af ]+"," ",t); t=_re.sub(r"\s+"," ",t).strip()
    return _re.sub(r"^(the|a|an) ","",t)
m["_nt"]=m.title_en.fillna(m.title_clean).fillna("").map(norm)
cand=m[m.annotated&(m._nt.str.len()>=18)].copy()
drop=[]
for (nt,jc),g in cand.groupby(["_nt","jurisdiction_country"]):
    if len(g)<2: continue
    g=g.sort_values(["words"],ascending=False)
    kept=[]
    for _,r in g.iterrows():
        same=[k for k in kept if (pd.isna(r.year_final) or pd.isna(k.year_final) or abs(r.year_final-k.year_final)<=1)]
        if same: drop.append({"doc_id":r.doc_id,"title_en":r.title_en,"jurisdiction_country":jc,"year_final":r.year_final,"doc_class":r.doc_class,"duplicate_of":same[0].doc_id,"reason":"identical normalised title and jurisdiction (second pass); fuller capture kept"})
        else: kept.append(r)
if drop:
    d2=pd.DataFrame(drop); m=m[~m.doc_id.isin(d2.doc_id)].copy()
    removed=pd.concat([removed,d2],ignore_index=True); removed.to_csv(B+"data/duplicates_removed.csv",index=False)
    print("second-pass duplicates removed",len(d2))
# third pass (v3): round-2 additions whose title closely matches a round-1 document in the same jurisdiction (token-set ratio >= 92, years within one)
# are near-duplicates (different URL or capture of the same instrument). The round-1 capture is kept when it is usable; otherwise the fuller round-2 text is kept.
from rapidfuzz import fuzz
r2=m[m.doc_id.str.startswith("R2-")&m.annotated&(m._nt.str.len()>=18)]; r1=m[~m.doc_id.str.startswith("R2-")&m.annotated&(m._nt.str.len()>=18)]
drop3=[]
if len(r2) and len(r1):
    r1g={jc:g for jc,g in r1.groupby("jurisdiction_country")}
    for _,r in r2.iterrows():
        g=r1g.get(r.jurisdiction_country)
        if g is None: continue
        g=g[(g.year_final.isna())|(pd.isna(r.year_final))|((g.year_final-r.year_final).abs()<=1)]
        if not len(g): continue
        # symmetric similarity (token-sort) with a length guard, so a short generic round-1 title cannot absorb longer distinct titles;
        # plus an identifier rule: the same EU act number at the head of both titles (the act itself, not amendments, opinions or guidance about it)
        ACT=_re.compile(r"\b((?:19|20)\d\d \d{1,4}|\d{1,4} (?:19|20)\d\d)\b"); ABOUT=_re.compile(r"amend|implement|delegat|opinion|guideline|annex|summary|impact assessment|position|corrigend|consult|report|statement|question|resolution of")
        def act_no(t):
            mm=ACT.search(t[:60]) if _re.match(r"^(proposal for a )?(regulation|directive|decision|council regulation|commission regulation|commission implementing|commission delegated)",t) else None
            return mm.group(1) if mm else None
        def score(t):
            if min(len(t),len(r._nt))<30 or min(len(t),len(r._nt))/max(len(t),len(r._nt))<0.6: return 0
            return fuzz.token_sort_ratio(t,r._nt)
        sc=g._nt.map(score); best=sc.idxmax()
        if sc[best]<90:
            a=act_no(r._nt)
            if a and not ABOUT.search(r._nt):
                hit=g[g._nt.map(lambda t: act_no(t)==a and not ABOUT.search(t))]
                if len(hit): best=hit.index[0]; sc[best]=100
        if sc[best]>=90:
            k=g.loc[best]; k_usable=bool(k.text_usable) and k.page_quality!="error_or_blocked_page" and k.doc_class!="unusable"
            if k_usable: drop3.append({"doc_id":r.doc_id,"title_en":r.title_en,"jurisdiction_country":r.jurisdiction_country,"year_final":r.year_final,"doc_class":r.doc_class,"duplicate_of":k.doc_id,"reason":f"round-2 near-duplicate of a round-1 document (title similarity {sc[best]:.0f}); round-1 capture kept"})
            else: drop3.append({"doc_id":k.doc_id,"title_en":k.title_en,"jurisdiction_country":k.jurisdiction_country,"year_final":k.year_final,"doc_class":k.doc_class,"duplicate_of":r.doc_id,"reason":f"round-1 capture unusable; replaced by round-2 near-duplicate (title similarity {sc[best]:.0f})"})
if drop3:
    d3=pd.DataFrame(drop3).drop_duplicates("doc_id"); m=m[~m.doc_id.isin(d3.doc_id)].copy()
    removed=pd.concat([removed,d3],ignore_index=True); removed.to_csv(B+"data/duplicates_removed.csv",index=False)
    print("third-pass cross-round near-duplicates removed",len(d3))
m=m.drop(columns=["_nt"])
# instruments still at proposal, bill or consultation stage cannot be binding instruments: move to the draft class
pre=m.instrument_status.isin(["draft_or_bill_under_consideration","proposal_or_concept","consultation_open"])&(m.doc_class=="governance_instrument_binding")
m.loc[pre,"doc_class"]="governance_proposal_or_draft"; print("binding->draft reclassified",int(pre.sum()))
# bills and proposals are not yet binding: record prospective binding nature separately
m["binding_nature_prospective"]=((m.doc_class=="governance_proposal_or_draft")&(m.binding_nature=="legally_binding"))
m.loc[m.binding_nature_prospective,"binding_nature"]="not_applicable"
# capture quality tier for instrument-level claims
m["capture_tier"]=np.where(m.page_quality=="substantive_document","substantive",np.where(m.page_quality=="partial_or_excerpt","partial","landing_or_other"))
# primary category must be among the categories (fixes F11 inconsistency)
def fixcats(r):
    pe=r.primary_embodied_category; ec=str(r.embodied_categories) if isinstance(r.embodied_categories,str) else ""
    if isinstance(pe,str) and pe not in ("none","") and pe not in ec.split("; "):
        return (ec+"; "+pe).strip("; ")
    return ec
m["embodied_categories"]=m.apply(fixcats,axis=1)
# derived flags that depend on overridden fields
m["is_governance_document"]=m["is_governance_document"].astype(bool)
m.to_csv(B+"data/master_table.csv",index=False)
try:
    dd=pd.read_csv(B+"data/data_dictionary.csv")
    with pd.ExcelWriter(B+"data/master_table.xlsx") as xw:
        m.to_excel(xw,sheet_name="documents",index=False); dd.to_excel(xw,sheet_name="data_dictionary",index=False)
except Exception as e: print("xlsx skipped",e)
print("rows",len(m),"removed",len(removed),"field overrides",len(log))
