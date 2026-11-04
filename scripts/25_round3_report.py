"""Round-3 companion report: what the third round changed (recovered instruments, new harvest, full-text re-reads,
supplementary fields, second precision audit, source-split gap). Writes report/src/collection_round3.md with table placeholders."""
import os, json, glob, pandas as pd, numpy as np, sys
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
sys.path.insert(0,B+"scripts"); from analysis_common import load
R3="/home/user/collection-round-3/"
a=load(); U=a[a.usable]; E=U[U.embodied_set]
def n(x): return f"{int(x):,}"
# --- round-3 documents
r3=a[a.collection_set=="round3"]; r3u=r3[r3.usable]
rec=r3u[r3u.doc_id.str.startswith("R2-")]; new=r3u[r3u.doc_id.str.startswith("R3-")]
_cm=pd.read_csv(R3+"candidates_merged.csv",dtype=str,keep_default_na=False); ref_ids=set(_cm[_cm.candidate_id.str.startswith("REF-")].doc_id)
P=E[E.instrument]; Bn=P[P.binding]
P3=P[P.collection_set=="round3"]; B3=Bn[Bn.collection_set=="round3"]
# --- collector outcomes
outs=[]
for p in glob.glob(R3+"status/agent_*.csv"):
    try: outs.append(pd.read_csv(p,dtype=str,keep_default_na=False))
    except Exception: pass
st=pd.concat(outs,ignore_index=True) if outs else pd.DataFrame(columns=["candidate_id","outcome","source_url","method","note"])
tg=pd.read_csv(R3+"targets.csv",dtype=str,keep_default_na=False)
oc=st.outcome.value_counts().to_dict() if len(st) else {}
blocked=st[st.outcome=="blocked"] if len(st) else st
t80=pd.DataFrame([dict(outcome=k,targets=v) for k,v in oc.items()]+[dict(outcome="not attempted",targets=len(tg)-len(st))])
def write_table(name,df,caption):
    df.to_csv(B+f"tables/{name}.csv",index=False)
    with open(B+f"tables/{name}.md","w") as f: f.write(f"**{name}. {caption}**\n\n"+df.to_markdown(index=False)+"\n")
write_table("T80_round3_collector_outcomes",t80,f"Round-3 collector outcomes for the {len(tg)} targets (189 verified-but-unread binding candidates from round 2 and 17 reference-list instruments missing on the strict test)")
if len(blocked):
    bl=blocked.merge(tg[["candidate_id","title_en","jurisdiction"]],on="candidate_id",how="left")[["candidate_id","title_en","jurisdiction","source_url","note"]]
    write_table("T81_round3_blocked",bl,"Targets whose official hosts refuse the identified research crawler: the list for manual download")
# --- harvest
inv=pd.read_csv(B+"data/round3_inventory.csv",dtype=str,keep_default_na=False) if os.path.exists(B+"data/round3_inventory.csv") else pd.DataFrame()
harv=inv[inv.doc_id.str.startswith("R3-")] if len(inv) else inv
# --- precision audit v5
pa={}
try:
    res=pd.read_csv(B+"review/v5_audit/precision_audit_v5_results.csv",dtype=str)
    y=lambda c:(res[c].str.upper()=="Y")
    from math import sqrt
    def wilson(k,n,z=1.96):
        p=k/n; d=1+z*z/n; c=p+z*z/(2*n); h=z*sqrt(p*(1-p)/n+z*z/(4*n*n)); return (c-h)/d,(c+h)/d
    joint=int((y("a")&y("b")&y("c")).sum()); lo,hi=wilson(joint,len(res))
    pa=dict(n=len(res),a=int(y("a").sum()),b=int(y("b").sum()),c=int(y("c").sum()),d=int(y("d").sum()),e=int(y("e").sum()),joint=joint,lo=lo,hi=hi,N=195,N5=len(Bn))   # sampled from the v4 set of 195 (SAMPLING.txt)
except Exception: pass
# --- tables already produced by other scripts
def has(name): return os.path.exists(B+f"tables/{name}.md")
t70=pd.read_csv(B+"tables/T70_supplement_v5_coverage.csv") if has("T70_supplement_v5_coverage") else None
t72=pd.read_csv(B+"tables/T72_legal_effect_of_standards.csv") if has("T72_legal_effect_of_standards") else None
t74=pd.read_csv(B+"tables/T74_fulltext_vs_excerpt.csv") if has("T74_fulltext_vs_excerpt") else None
t75=pd.read_csv(B+"tables/T75_fulltext_changes.csv") if has("T75_fulltext_changes") else None
t7b=pd.read_csv(B+"tables/T07b_governance_gap_by_source.csv") if has("T07b_governance_gap_by_source") else None
# --- narrative
md=[]
md.append("← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)\n")
md.append("*Companion to the analysis report. Round 3 executed the items of the round-3 plan that an agent can do alone: re-fetching blocked and missing instruments by official alternative routes, a harvest with service-robot terms, a full-text re-read of truncated statutes, a supplementary schema (whom an instrument binds, dates, legal effect of standards, provision dating), a second precision audit, and a source split of the governance-gap index. Items that need a person are listed in HUMAN_ASSISTANCE.md.*\n")
md.append("## Summary\n")
md.append(f"Round 3 added {n(len(r3u))} usable documents to the collection: {n(len(rec))} round-2 candidates whose text could now be read ({n(int(rec.doc_id.isin(Bn.doc_id).sum()))} of them principal binding embodied instruments) and {n(len(new))} new documents, {n(int(new.doc_id.isin(ref_ids).sum()))} of them reference-list instruments fetched from their titles and the rest from the harvest with service-robot, care, exoskeleton, humanoid and collaborative-robot terms and EuroVoc concepts. The harvest itself added little: of its {n(int((~new.doc_id.isin(ref_ids)).sum()))} usable documents only {n(int((new.embodied_set&~new.doc_id.isin(ref_ids)).sum()))} fall in the embodied set and {n(int((new.embodied_set&new.instrument&~new.doc_id.isin(ref_ids)).sum()))} are principal instruments, so the open legal databases hold few service-robot instruments that rounds 1 and 2 had not already found, and the gains of round 3 come from reading texts that were already known. Of the reference-list instruments, {n(int((new.embodied_set&new.instrument&new.doc_id.isin(ref_ids)).sum()))} are now principal embodied instruments in the collection. The collection now holds {n(len(U))} usable documents, {n(len(E))} in the embodied set, {n(len(P))} principal embodied instruments and {n(len(Bn))} principal binding ones (v4: 3,165 / 1,603 / 505 / 195). "
          + (f"Of the {len(tg)} round-3 targets, the collectors saved a text for {oc.get('saved',0)+oc.get('saved_partial',0)}, found {oc.get('blocked',0)} blocked at official hosts, judged {oc.get('irrelevant',0)} irrelevant and could not locate {oc.get('not_found',0)} (Table 80)." if oc else "Collector outcomes are in Table 80.") + "\n")
md.append("The collectors' own reports, with the alternative routes that worked (Publications Office CELEX resolver for EUR-Lex, state legislatures' PDF endpoints, Riigi Teataja and legislation.govt.nz rendered pages, the Kremlin acts bank, Gazzetta Ufficiale issue PDFs) and the metadata corrections they noticed (act numbers, repeal dates, mislabelled gazette copies), are in collection_round3/status/report_*.md.\n\n{{T80}}\n")
if len(blocked): md.append("The blocked targets are the manual-download list for a person with ordinary browser access (Table 81).\n\n{{T81}}\n")
md.append("## Full-text re-reads of truncated instruments\n")
if t74 is not None:
    row=lambda f: t74[t74.field==f].iloc[0] if (t74.field==f).any() else None
    dc=row("doc_class"); rl=row("relevance_to_embodied_ai_governance"); pr=row("principles (exact level, all 20)"); up=row("principle levels raised by the full text")
    md.append(f"The excerpt policy stops at 110,000 characters; {int(dc['n'])} principal embodied instruments exceeded it. Re-reading them with up to 400,000 characters under the same prompt left the document class unchanged in {dc['agree_pct']}% and the relevance rating in {rl['agree_pct']}%; principle levels agreed exactly in {pr['agree_pct']}% of field-document pairs, and the full text raised a level in {up['agree_pct']}% of pairs (Table 74). The full-text labels replace the excerpt labels for these documents. The documents whose set-defining labels changed are listed in Table 75.\n")
    md.append("{{T74}}\n\n{{T75}}\n")
md.append("## Supplementary fields: whom a rule binds, when it applies, what a standard's legal effect is, when the robot provision arrived\n")
if t70 is not None:
    b=t70[t70.population=="principal binding embodied instruments"].iloc[0]; o=t70[t70.population=="principal binding, dated before 2010"].iloc[0]
    basis=Bn.robot_provision_basis.fillna("not_determinable").value_counts()
    nd_old=int((o["n"]))-int(o["robot_provision_year"])
    md.append(f"A second, smaller annotation pass asked five questions the codebook had not asked, of every principal embodied instrument, with a quote required for every answer. Among the {int(b['n'])} principal binding instruments the text names whom the rule binds in {int(b['bound_parties_stated'])} cases (operators or deployers and public bodies most often; Table 71), an entry-into-force date in {int(b['entry_into_force_date'])}, a later application date in {int(b['applicability_date'])} and a repeal or expiry date in {int(b['repeal_or_expiry_date'])} (Table 70). The year the robot-relevant provision arrived could be given for {int(b['robot_provision_year'])} binding instruments, but mostly because the whole instrument is about such systems ({int(basis.get('whole_instrument_is_about_such_systems',0))} cases), so the provision year is the document year; an amendment history in the text dated the provision in {int(basis.get('amendment_history_in_text',0))} cases and the provision itself stated its date in {int(basis.get('stated_in_provision',0))}; in {int(basis.get('not_determinable',0))} the year could not be determined from the captured text. Only {int(b['provision_year_later_than_document_year'])} binding instruments carry a provision year later than the document's recorded year (Table 73). The consolidated statutes dated before 2010 are the case that matters for trend analyses, and for {nd_old} of the {int(o['n'])} the captured consolidation carries no amendment history, so the model could not date their automated-driving or drone articles: these need a person with the amendment record (HUMAN_ASSISTANCE.md, the legal-check item). Among the technical standards, {int(t72.standards[t72.legal_effect=='voluntary'].sum()) if t72 is not None and (t72.legal_effect=='voluntary').any() else 0} state on their public page that they are voluntary and {int(t72.standards[t72.legal_effect=='harmonised_or_designated'].sum()) if t72 is not None and (t72.legal_effect=='harmonised_or_designated').any() else 0} that they are harmonised or designated under a law (Table 72).\n")
    md.append("{{T70}}\n\n{{T71}}\n\n{{T72}}\n\n{{T73}}\n")
md.append("## Second precision audit\n")
if pa:
    md.append(f"An independent agent re-read a random sample of {pa['n']} of the {pa['N']} principal binding embodied instruments of v4 (seed 2027) against the five criteria of the v3 audit. Shares: distinct instrument {pa['a']}%, binding {pa['b']}%, substantive embodied provisions {pa['c']}%, autonomy or AI content {pa['d']}%, explicit AI {pa['e']}%; all three main criteria jointly {pa['joint']}% (Wilson {100*pa['lo']:.0f} to {100*pa['hi']:.0f}), implying about {round(pa['N']*pa['joint']/100)} genuine instruments ({round(pa['N']*pa['lo'])} to {round(pa['N']*pa['hi'])}) in the set of {pa['N']}. The v3 audit of the earlier set of 299 found 54% (44 to 63). The sample was drawn from the v4 set before round 3; applied to the v5 set of {pa['N5']} principal binding instruments the same share implies about {round(pa['N5']*pa['joint']/100)} ({round(pa['N5']*pa['lo'])} to {round(pa['N5']*pa['hi'])}). The failures are mostly binding instruments without a substantive embodied provision (a drone or robot named only in a list of functions or definitions), then register, tracking and catalogue pages and date-only amendments that the counting-unit rules let through. The audit report with the failing documents is review/v5_audit/precision_audit_v5.md.\n")
else: md.append("The audit report is review/v5_audit/precision_audit_v5.md.\n")
md.append("## The governance gap, split by collection source\n")
if t7b is not None:
    both_pos=t7b[(t7b.gap_round1>2)&(t7b.gap_round2>2)].sort_values("gap_all",ascending=False); both_neg=t7b[(t7b.gap_round1<-2)&(t7b.gap_round2<-2)].sort_values("gap_all"); flip=t7b[((t7b.gap_round1>2)&(t7b.gap_round2<-2))|((t7b.gap_round1<-2)&(t7b.gap_round2>2))]
    only1=t7b[(t7b.gap_round1.abs()<=2)&(t7b.gap_round2.abs()>10)|(t7b.gap_round2.abs()<=2)&(t7b.gap_round1.abs()>10)]
    nm=lambda c: c.replace("_"," ")
    md.append("Because round 2 searched legal databases for drones, vehicles and machinery, the instrument side of the governance-gap index could inherit the search terms. Table 7b computes the index separately against the round-1 instruments (web search of robot-specific and general-AI sources) and against the round-2 and round-3 instruments (database harvests and recovered texts). "
              + (f"The gap is positive against both sources for {', '.join(f'{nm(r.category)} ({r.gap_round1:+.0f} and {r.gap_round2:+.0f} points)' for r in both_pos.itertuples())}: research attention to these machine classes exceeds their share of instruments whichever way the instruments were found, so the headline gap for service, companion and humanoid robots is not an artefact of the round-2 terms. " if len(both_pos) else "")
              + (f"The instrument surplus is present against both sources for {', '.join(f'{nm(r.category)} ({r.gap_round1:+.0f} and {r.gap_round2:+.0f})' for r in both_neg.itertuples())}. " if len(both_neg) else "")
              + (f"The gap appears against only one source for {', '.join(f'{nm(r.category)} ({r.gap_round1:+.0f} against round-1 instruments, {r.gap_round2:+.0f} against harvested ones)' for r in only1.itertuples())}: for these classes the round-1 robot-specific sources supplied standards and guidance that the database harvests did not, so the size of the gap depends on how instruments were found. " if len(only1) else "")
              + (f"The sign flips for {', '.join(f'{nm(r.category)} ({r.gap_round1:+.0f} against round-1 instruments, {r.gap_round2:+.0f} against harvested ones)' for r in flip.itertuples())}: the round-1 instrument set, drawn from robot-specific sources, is rich in standards for these classes, and the harvested set is not, so for them the gap depends on the source and should not be read as a finding.\n" if len(flip) else "\n"))
    md.append("{{T07b}}\n")
md.append("## What round 3 did not do\n")
md.append("No person labelled any document (the human-validation kit is in data/human_validation/); hosts that refuse the identified crawler were not circumvented (Table 81 lists them for manual download); technical standards are still read from scope pages; and the labels of the new and recovered documents carry the same model limits as the rest.\n")
os.makedirs(B+"report/src",exist_ok=True)
open(B+"report/src/collection_round3.md","w").write("\n".join(md))
print("round-3 report written; round-3 usable docs",len(r3u),"recovered",len(rec),"new",len(new))
