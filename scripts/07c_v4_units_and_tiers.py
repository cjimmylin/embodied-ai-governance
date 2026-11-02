#!/usr/bin/env python3
"""v4: two review-driven refinements of the counting unit and the construct, added to the master table after the override step.

1. instrument_unit (title-based, documented rules): principal | amendment | ancillary | incorporation | language_copy.
   Headline instrument counts in v4 use principal + amendment ("principal instruments"); ancillary paperwork (commencement orders,
   levy and fee instruments, individual exemptions/directions/approvals/permits, definitions-only parts, tables of contents),
   EEA incorporation decisions and language-version corrigenda are reported separately.
2. AI-content tiers from the full text (cached): ai_explicit (artificial intelligence, machine learning, AI system, algorithm, neural network,
   or their Chinese/Japanese/Korean/French/German/Spanish equivalents) and autonomy_terms (autonomous/automated operation, self-driving,
   remotely piloted, autonomy, automation of driving/flight). Headline counts are reported under the machine-class construct (v3) and under
   the two text-based constructs.
"""
import re, os, json, pandas as pd, numpy as np
B="/home/user/embodied-ai-governance-v5/"
m=pd.read_csv(B+"data/master_table.csv",low_memory=False)
t=m.title_en.fillna("").astype(str)
ANC=re.compile(r"commencement|bringing into force|\blevy\b|\bfees?\b|charges? (regulations|order)|exemption\b|direction\b|area approval|approval for operation|\bpermit\b|authori[sz]ation (for|of) (operation|flights?)|definitions of terms|definitions and abbreviations|table of contents|chapter index|^part \d+[:—-]?\s*(definitions|general provisions)$",re.I)
AMD=re.compile(r"\bamend|amending|amendment|modif(y|ying|ication)|supplementing|repeal(ing)? (and replacing)?|varying",re.I)
INC=re.compile(r"EEA Joint Committee",re.I)
LANG=re.compile(r"corrigend|language version|rectification",re.I)
def unit(row):
    ti=row["t"]
    if LANG.search(ti): return "language_copy"
    if INC.search(ti): return "incorporation"
    if ANC.search(ti): return "ancillary"
    if AMD.search(ti): return "amendment"
    return "principal"
reg=pd.read_csv(B+"data/registry.csv",low_memory=False)[["doc_id","text_path","text_chars"]].drop_duplicates("doc_id").set_index("doc_id")
m["instrument_unit"]=pd.DataFrame({"t":t}).apply(unit,axis=1)
# landing/index pages counted as instruments are not instruments as units
m.loc[m.page_quality.eq("landing_or_index_page")&m.instrument_unit.eq("principal"),"instrument_unit"]="catalogue_page"
# metadata stubs: captures under 150 words cannot carry provisions (the v2 Taiwan-stub rule, now applied to every round)
INST=m.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])
m.loc[INST&m.instrument_unit.isin(["principal","amendment"])&(m.words.fillna(0)<150)&m.page_quality.ne("substantive_document"),"instrument_unit"]="stub"
# status and class rules that the v3 annotation got wrong at scale (governance-expert audit of v3)
# 1. standards still in development (AWI, PWI, WD, CD, DIS, FDIS, DTS, DTR, PRF) are not published instruments
dev=t.str.contains(r"\b(AWI|PWI|WD|CD|DIS|FDIS|DTS|DTR|PRF)\b",regex=True)&m.doc_type.eq("technical_standard")
m.loc[dev,"instrument_status"]="under_development"; m.loc[dev&m.doc_class.isin(["governance_instrument_soft","governance_instrument_binding"]),"doc_class"]="governance_proposal_or_draft"
# 2. mandatory Chinese national standards (GB nnnn, not GB/T or GB/Z) are binding
gbm=(t.str.contains(r"^GB\s?\d",regex=True)|t.str.contains(r"(?<![/A-Za-z])GB\s?\d{4,5}(?:\.\d+)?-\d{4}",regex=True))&~t.str.contains(r"GB/[TZ]",regex=True)   # v4.1: number anywhere in the title (e.g. "... (GB 11291.1-2011)")
m.loc[gbm,"doc_class"]="governance_instrument_binding"; m.loc[gbm,"binding_nature"]="technical_standard_mandated"
# 3. CCW working papers, chair's summaries and rolling texts are formal positions and process documents, not instruments
ccw=t.str.contains(r"working paper|chair'?s summary|rolling text|draft articles on autonomous weapon|CRP\.\d",case=False,regex=True)&m.jurisdiction_country.isin(["INT","XX"])
m.loc[ccw&INST,"doc_class"]="government_report_or_parliamentary"
# 4. proposals whose adopted act is in the collection (same EU act lineage) are superseded
import re as _re
act_titles=set(m[m.doc_class.eq("governance_instrument_binding")].title_en.fillna("").str.lower())
prop=m.doc_class.eq("governance_proposal_or_draft")&t.str.contains(r"^proposal for|^draft |amendments adopted by the european parliament",case=False,regex=True)
def enacted(ti):
    k=_re.sub(r"^(proposal for a |draft )","",ti.lower()); k=_re.sub(r"amendments adopted by the european parliament on .*? on the proposal for a ","",k)
    core=_re.sub(r"\(.*?\)","",k); core=_re.sub(r"\s+"," ",core).strip()
    return any(core[:60] in a for a in act_titles) if len(core)>=25 else False
m.loc[prop&m.instrument_status.isin(["draft_or_bill_under_consideration","consultation_open","proposal_or_concept"])&m.title_en.fillna("").map(enacted),"instrument_status"]="superseded_or_repealed"
# 5. byte-identical texts are one capture
import hashlib
def thash(d):
    tp=reg.text_path.get(d) if d in reg.index else None
    try: return hashlib.md5(open(tp,"rb").read()).hexdigest() if isinstance(tp,str) and os.path.exists(tp) else None
    except Exception: return None
m["text_hash"]=m.doc_id.map(thash)
dup=m[m.text_hash.notna()&INST].sort_values(["text_hash","words"],ascending=[True,False]).duplicated("text_hash",keep="first")
m.loc[dup[dup].index,"instrument_unit"]="duplicate_text"
# documented doc-level corrections from the governance-expert audit of v3 (data/manual_overrides_v4.csv), applied last
ovp=B+"data/manual_overrides_v4.csv"
if os.path.exists(ovp):
    ov=pd.read_csv(ovp,dtype=str,keep_default_na=False); n=0
    for _,r in ov.iterrows():
        if r.doc_id in set(m.doc_id) and r.field in m.columns:
            v=r.new_value
            if pd.api.types.is_numeric_dtype(m[r.field]):
                try: v=float(v) if v!="" else np.nan
                except Exception: continue
            elif v=="": v=np.nan
            m.loc[m.doc_id==r.doc_id,r.field]=v; n+=1
    print("v4 doc-level overrides applied:",n)
INST=m.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])
# ---- AI-content tiers from full text (cached by doc_id + text_chars)
AI=re.compile(r"artificial intelligence|machine learning|\bAI system|\bAI\b|algorithm|neural network|deep learning|intelligent system|人工智能|机器学习|算法|人工知能|機械学習|アルゴリズム|인공지능|머신러닝|알고리즘|intelligence artificielle|künstliche intelligenz|inteligencia artificial|inteligência artificial|intelligenza artificiale",re.I)
AUTO=re.compile(r"autonom|automated (driving|vehicle|operation|flight|system|lane|function)|self-driving|driverless|remotely piloted|unmanned|automated driving system|\bADS\b|automation|自動運転|自律|無人|自动驾驶|自主|无人|자율|자동|autonome|automatisiert|autónom|autônom",re.I)
cache_p=B+"data/ai_content_flags.csv"
cache=pd.read_csv(cache_p).set_index("doc_id") if os.path.exists(cache_p) else pd.DataFrame(columns=["text_chars","ai_explicit_n","autonomy_n"]).set_index(pd.Index([],name="doc_id"))
rows=[]
for d in m.doc_id:
    tc=reg.text_chars.get(d) if d in reg.index else None; tp=reg.text_path.get(d) if d in reg.index else None
    if d in cache.index and cache.loc[d,"text_chars"]==tc: rows.append(dict(doc_id=d,text_chars=tc,ai_explicit_n=cache.loc[d,"ai_explicit_n"],autonomy_n=cache.loc[d,"autonomy_n"])); continue
    n1=n2=np.nan
    if isinstance(tp,str) and os.path.exists(tp):
        txt=open(tp,encoding="utf8",errors="replace").read(); n1=len(AI.findall(txt)); n2=len(AUTO.findall(txt))
    rows.append(dict(doc_id=d,text_chars=tc,ai_explicit_n=n1,autonomy_n=n2))
c=pd.DataFrame(rows); c.to_csv(cache_p,index=False); c=c.set_index("doc_id")
m["ai_explicit_n"]=m.doc_id.map(c.ai_explicit_n); m["autonomy_n"]=m.doc_id.map(c.autonomy_n)
m["ai_explicit"]=m.ai_explicit_n.fillna(0)>=2          # at least two explicit AI mentions in the text
m["autonomy_terms"]=(m.autonomy_n.fillna(0)>=2)|m.ai_explicit
m["principal_instrument"]=m.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])&m.instrument_unit.isin(["principal","amendment"])
# ---- instrument families: the same instrument captured as yearly renewals, successive versions, parts or amendments within one jurisdiction
import unicodedata
def fam_key(ti):
    k=unicodedata.normalize("NFKC",str(ti)).lower()
    k=re.sub(r"\b(19|20)\d\d\b"," ",k)                                                      # years
    k=re.sub(r"\b\d{1,4}/\d{1,4}\b"," ",k)                                                  # act numbers 2019/947, 64/23
    k=re.sub(r"\b(no\.?|n°|nr\.?|ex|revision|rev\.?|version|edition|ed\.?|issue)\s*[a-z]?\d+[a-z]?\b"," ",k)   # version / instrument numbers
    k=re.sub(r"\b(amending|amendment|amendments|to amend|supplementing|modifying|as amended|consolidated|consolidation|correcting)\b"," ",k)
    k=re.sub(r"[^a-z0-9()\u00c0-\u024f\u0400-\u04ff\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af ]+"," ",k); k=re.sub(r"\s+"," ",k).strip()
    return k
m["family_key"]=m.title_en.fillna("").map(fam_key)+" | "+m.jurisdiction_country.fillna("XX").astype(str)
inst=m.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"])
fam=m[inst&(m.family_key.str.len()>8)].groupby("family_key").doc_id.transform("size")
m["family_size"]=1; m.loc[fam.index,"family_size"]=fam.values
# family representative: the longest usable capture in the family (used for family-level counts)
rep=m[inst].sort_values(["family_key","words"],ascending=[True,False]).drop_duplicates("family_key").doc_id
m["family_rep"]=m.doc_id.isin(set(rep))
m["words_ok"]=m.words.fillna(0)>=150                            # minimum text for depth (level-2) statistics
m.to_csv(B+"data/master_table.csv",index=False)
u=m[m.text_usable&(m.page_quality!="error_or_blocked_page")&(m.doc_class!="unusable")&m.annotated]
emb=((u.relevance_to_embodied_ai_governance>=2)|(u.embodied_categories.fillna("")!=""))&(u.ai_scope!="not_ai")
inst=u.doc_class.isin(["governance_instrument_binding","governance_instrument_soft","governance_proposal_or_draft"]); b=u.doc_class=="governance_instrument_binding"
print("instrument_unit among embodied instruments:",u[inst&emb].instrument_unit.value_counts().to_dict())
print("instrument_unit among binding embodied:",u[b&emb].instrument_unit.value_counts().to_dict())
for name,sel in [("embodied instruments",inst&emb),("principal embodied instruments",inst&emb&u.principal_instrument),("binding embodied",b&emb),("principal binding embodied",b&emb&u.principal_instrument)]:
    s=u[sel]; print(f"{name}: all={len(s)} families={s[s.family_rep].shape[0] if 'family_rep' in s else 'na'} ai_explicit={int(s.ai_explicit.sum())} autonomy_or_ai={int(s.autonomy_terms.sum())}")
big=u[inst&emb&(u.family_size>=3)].sort_values("family_key")[["family_key","family_size"]].drop_duplicates().head(12); print(big.to_string())
