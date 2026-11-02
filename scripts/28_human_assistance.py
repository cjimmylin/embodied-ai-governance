"""Write HUMAN_ASSISTANCE.md: the round-3 items that need a person (access, judgement, paid sources, validation),
with the concrete lists drawn from the project data. Run after 25_round3_report.py."""
import os, glob, pandas as pd, numpy as np, sys
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
sys.path.insert(0,B+"scripts"); from analysis_common import load
R3="/home/user/collection-round-3/"
a=load(); U=a[a.usable]; E=U[U.embodied_set]; P=E[E.instrument]; Bn=P[P.binding]
tg=pd.read_csv(R3+"targets.csv",dtype=str,keep_default_na=False)
outs=[pd.read_csv(p,dtype=str,keep_default_na=False) for p in glob.glob(R3+"status/agent_*.csv")]
st=pd.concat(outs,ignore_index=True) if outs else pd.DataFrame(columns=["candidate_id","outcome","source_url","method","note"])
st=st.drop_duplicates("candidate_id",keep="last")
tgi=tg.set_index("candidate_id")
def row_md(df,cols): return df[cols].to_markdown(index=False) if len(df) else "_none_"
L=[]
L.append("# What a person is needed for\n")
L.append("Round 3 ran everything an agent can run alone (see report/src/collection_round3.md). The items below need a person: a browser with ordinary access, a subscription, a judgement the model should not make, or a second pair of eyes. They are ordered by how much they would change the results.\n")
# 1 blocked
bl=st[st.outcome=="blocked"].copy()
if len(bl):
    bl["title"]=bl.candidate_id.map(tgi.title_en); bl["jurisdiction"]=bl.candidate_id.map(tgi.jurisdiction); bl["year"]=bl.candidate_id.map(tgi.year)
    bl["official_url"]=bl.candidate_id.map(tgi.url_primary)
hosts=bl.official_url.str.extract(r"https?://([^/]+)")[0].value_counts() if len(bl) else pd.Series(dtype=int)
L.append(f"## 1. Download {len(bl)} instruments whose official hosts refuse the research crawler\n")
L.append("The collectors identify themselves honestly (`CEI-AI-Robotics-collector/1.0`) and do not imitate a browser or bypass bot checks, so some official legal databases return nothing to them. A person with an ordinary browser can save each document (the HTML page or the PDF) into `/home/user/collection-round-3/texts/<candidate_id>.txt` (plain text) or `raw/<candidate_id>.pdf`; the fetch and annotation scripts then pick them up (`scripts/fetch_texts_r3.py` skips ids that already have a text). Each file needs the source URL on its first line as `SOURCE_URL: ...`.\n")
if len(hosts): L.append("Hosts, by number of blocked targets:\n\n"+hosts.rename_axis("host").reset_index(name="targets").to_markdown(index=False)+"\n")
L.append(row_md(bl.sort_values(["jurisdiction","year"]),["candidate_id","title","jurisdiction","year","official_url","note"])+"\n")
# 2 not found
nf=st[st.outcome.isin(["not_found"])].copy()
if len(nf):
    nf["title"]=nf.candidate_id.map(tgi.title_en); nf["jurisdiction"]=nf.candidate_id.map(tgi.jurisdiction); nf["year"]=nf.candidate_id.map(tgi.year); nf["recorded_url"]=nf.candidate_id.map(tgi.url_primary)
L.append(f"## 2. Locate {len(nf)} instruments the collectors could not find\n")
L.append("These are round-2 candidates whose recorded URL is dead and for which no official alternative turned up by search. A person who knows the jurisdiction (or has access to a national gazette archive, Westlaw, Lexis, Beck-online, 北大法宝 or 法律図書館) can usually resolve them in minutes. Save them as in item 1.\n")
L.append(row_md(nf.sort_values(["jurisdiction","year"]),["candidate_id","title","jurisdiction","year","recorded_url","note"])+"\n")
# 3 not attempted
done=set(st.candidate_id); na=tg[~tg.candidate_id.isin(done)]
if len(na):
    L.append(f"## 3. Finish the {len(na)} targets the collectors did not reach\n")
    L.append("The collectors ran with a time budget. These targets were not attempted in round 3 and should be fetched first by the scripts (`python3 scripts/r3fetch.py --ids ...`) and, where that fails, by a person.\n")
    L.append(row_md(na,["candidate_id","title_en","jurisdiction","year","url_primary"])+"\n")
# 4 paid standards
stds=P[P.doc_type.eq("technical_standard")].copy()
scope=stds[stds.page_quality.ne("substantive_document")]
L.append(f"## 4. Obtain the full text of {len(scope)} technical standards read only from their scope pages\n")
L.append("ISO, IEC, CEN, UL, JIS, GB and similar standards are sold, not published. The study reads them from the public scope and preview pages, so every label for these documents describes the preview, and the supplementary 'legal effect of the standard' field could only be answered from the preview. A person with an institutional subscription (ISO OBP, IEEE Xplore, Techstreet, a university library) can download the PDFs into `data/texts_private/` (ignored by git and never redistributed) and re-run the annotation for these ids with `scripts/04_annotate.py --ids data/ids_standards.txt --out annotations/standards_full`. The list, with the issuer and the public page used:\n")
scope=scope.assign(issuer=scope.authors_or_issuer.fillna("").str.slice(0,60))
L.append(row_md(scope.sort_values(["issuer","year_final"]),["doc_id","title_en","issuer","year_final","words","source_url"])+"\n")
open(B+"data/ids_standards.txt","w").write("\n".join(scope.doc_id)+"\n")
# 5 human validation
L.append("## 5. Hand-label the 200-document validation sample (about two working days)\n")
L.append("No person has yet labelled a document in this study; the precision audits are model-on-model. The kit in `data/human_validation/` has a stratified sample of 200 documents (40 per stratum), a coding sheet with drop-downs (`coding_sheet.xlsx`), instructions, and an answer key of the model's labels kept separate so the coder is blind to them. A coder with legal or policy training fills the sheet from the stored text (`texts/<doc_id>.txt`) or the source URL; `scripts/22_human_agreement.py` (to be written against the returned sheet, following `21_precision_audit.py`) then reports agreement per field and recalibrates the three headline counts. Languages in the sample: English 157, Japanese 12, Chinese 8, Portuguese 6, Spanish 4, French 4; a second coder for the non-English documents is useful.\n")
# 6 legal-basis checks
chk=[]
if "legal_effect_of_standard" in Bn.columns or "supp_confidence" in P.columns:
    lo=P[pd.to_numeric(P.get("supp_confidence",pd.Series(index=P.index,dtype=float)),errors="coerce")<0.6]
    nd=Bn[Bn.get("robot_provision_basis",pd.Series(index=Bn.index,dtype=object)).fillna("not_determinable").eq("not_determinable")]
    unk=stds[stds.get("legal_effect_of_standard",pd.Series(index=stds.index,dtype=object)).isin(["unknown"])]
    later=Bn[Bn.get("robot_provision_year",pd.Series(index=Bn.index,dtype=float)).notna() & (Bn.get("robot_provision_year",pd.Series(index=Bn.index,dtype=float))>Bn.year_final)]
    L.append("## 6. Check the model's legal readings where it was unsure\n")
    L.append(f"The supplementary pass (whom the rule binds, dates, legal effect, provision dating) rated its own confidence. A lawyer should check the {len(lo)} principal instruments where the model's confidence is below 0.6, the {len(unk)} standards whose legal effect could not be determined from the preview, the {len(later)} binding instruments whose robot provision the model dated later than the document year (Table 73), and above all the {len(nd)} binding instruments (including {int((nd.year_final<2010).sum())} consolidated statutes dated before 2010) for which the captured text carries no amendment history, so the year the robot provision arrived could not be read: these dates drive the provision-level trend and a wrong amendment year moves a document between periods. The ids are in `data/ids_legal_check.txt`; the quotes the model relied on are in `annotations/supplement_v5/<doc_id>.json`.\n")
    open(B+"data/ids_legal_check.txt","w").write("\n".join(sorted(set(lo.doc_id)|set(unk.doc_id)|set(later.doc_id)|set(nd.doc_id)))+"\n")
# 7 precision audit fails
try:
    res=pd.read_csv(B+"review/v5_audit/precision_audit_v5_results.csv",dtype=str)
    y=lambda c:(res[c].str.upper()=="Y"); fail=res[~(y("a")&y("b")&y("c"))]
    L.append(f"## 7. Decide the {len(fail)} audited documents the second audit would exclude\n")
    L.append("The second precision audit (review/v5_audit/precision_audit_v5.md) lists the sampled principal binding instruments that failed one of the three main criteria (distinct instrument, binding, substantive embodied provisions). Whether to exclude them, relabel them (for instance as amendments or as general-AI instruments) or change the criteria is an editorial decision. Accepting the audit's reading and extrapolating it is what the report does now; a person's ruling on each of the failing documents would let the counts be corrected directly rather than by a sample-based factor. Three of the failure types are also fixable by a person with a browser: the register, table-of-contents and bill-tracking captures (the Australian CASR 1998 and its Part 101 manual, the Kentucky and Utah bills, the Nigerian Part 21 entry) need the operative text saved as in item 1; the UK retained copies of EU drone regulations need a ruling on whether a retained copy is a distinct instrument; and the generic regimes rated relevant (the Digital Omnibus on AI, UN R155 and R156, the medical-device regulations) need a ruling on whether a regime that governs robots only through general product rules belongs in the count.\n")
    ft=fail.reason.str.extract(r"^\[(.*?)\]")[0].fillna("other").value_counts().rename_axis("failure type").reset_index(name="sampled documents")
    L.append(ft.to_markdown(index=False)+"\n")
    fl=fail.assign(reason=fail.reason.str.slice(0,160))[["doc_id","title","jurisdiction","year","reason"]]
    L.append(fl.to_markdown(index=False)+"\n")
except Exception: pass
# 8 boundary decisions
L.append("## 8. Boundary decisions only the authors can make\n")
L.append("- Whether consolidated statutes amended for robots (the Japanese Road Traffic Act and Road Transport Vehicle Act, the German Road Traffic Act, the US Federal Motor Vehicle Safety Standards) count as one instrument each or as one per amendment; the counts in the report treat them as one and date them by the provision year where the text gives it (Table 73).\n- Whether purely sectoral vehicle and drone rules belong in the 'embodied AI' set at all, or only those that mention automation, autonomy or AI. The report gives both (Table 53b counts principal instruments with and without autonomy or AI provisions); the headline needs one.\n- The reference list of 'instruments every collection should have' (17 titles) was compiled by the agent; an expert panel should settle it before recall is reported against it.\n- Which categories in the governance-gap index count as governed by general product-safety law rather than by a robot-specific instrument (the index treats both as instruments; a stricter reading changes the gap for care, delivery and humanoid robots most).\n")
# 9 accounts and infrastructure
L.append("## 9. Accounts and infrastructure\n")
L.append("- GitHub: the repository's history still contains the model-input excerpts under `annotations/**/_inputs/` in earlier commits. Either force-push the cleaned history (commands in README) or make the repository private; the agent cannot force-push.\n- A database or API account for the national legal databases that block crawlers (item 1) would make rounds 4 onward reproducible without a person in the loop: EUR-Lex and the Japanese e-Gov API are already used; the Korean law.go.kr Open API, the Chinese flk.npc.gov.cn and the Taiwanese law.moj.gov.tw open-data portal all require registration by a person.\n- Translations: the Japanese, Chinese, Korean and Portuguese texts were labelled from the original language; a native-speaking reviewer for the 24 non-English documents in the validation sample would also validate the cross-language labels.\n- The narrated video and the decks cite the v4 counts; once the v5 counts are accepted, the slides with numbers need updating (the agent can do this on request).\n")
import re as _re
_txt="\n".join(L); _n=[0]
def _renum(m): _n[0]+=1; return f"## {_n[0]}. "
_txt=_re.sub(r"^## \d+\. ",_renum,_txt,flags=_re.M)
_txt=_re.sub(r"item 6\b",lambda m:"the legal-check item",_txt)
open(B+"HUMAN_ASSISTANCE.md","w").write(_txt)
print("HUMAN_ASSISTANCE.md written: blocked",len(bl),"not found",len(nf),"not attempted",len(na),"standards from scope pages",len(scope))
