"""Merge the supplementary v5 annotations (bound parties, dates, legal effect of standards, robot-provision year)
into the master table as new columns and write their summary tables (T70, T71). Run after 07c."""
import os, json, glob, re, pandas as pd, numpy as np
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
M=pd.read_csv(B+"data/master_table.csv",low_memory=False)
rows=[]
for p in glob.glob(B+"annotations/supplement_v5/*.json"):
    j=json.load(open(p)); a=j["annotation"]
    rows.append(dict(doc_id=j["doc_id"],bound_parties="; ".join(a.get("bound_parties") or []),bound_parties_text=a.get("bound_parties_text",""),
                     entry_into_force_date=a.get("entry_into_force_date"),applicability_date=a.get("applicability_date"),repeal_or_expiry_date=a.get("repeal_or_expiry_date"),
                     legal_effect_of_standard=a.get("legal_effect_of_standard"),robot_provision_year=a.get("robot_provision_year"),robot_provision_basis=a.get("robot_provision_basis"),
                     supp_confidence=a.get("confidence"),supp_model=j.get("model"),supp_prompt_hash=j.get("prompt_hash")))
S=pd.DataFrame(rows)
if not len(S): print("no supplementary annotations"); raise SystemExit
for c in S.columns:
    if c!="doc_id" and c in M.columns: M=M.drop(columns=[c])
M=M.merge(S,on="doc_id",how="left")
M.to_csv(B+"data/master_table.csv",index=False)
print("supplementary fields merged for",len(S),"documents")
# ---- summary tables
def write_table(name,df,caption):
    os.makedirs(B+"tables",exist_ok=True); df.to_csv(B+f"tables/{name}.csv",index=False)
    with open(B+f"tables/{name}.md","w") as f: f.write(f"**{name}. {caption}**\n\n"+df.to_markdown(index=False)+"\n")
import sys; sys.path.insert(0,B+"scripts")
from analysis_common import load
a=load(); P=a[a.embodied_set & a.instrument]; Bn=P[P.binding]
def yr(s):
    try: return int(str(s)[:4])
    except Exception: return np.nan
def cov(df):
    return dict(n=len(df),
        bound_parties_stated=int((~df.bound_parties.fillna("").isin(["","none_stated","not_applicable"])).sum()),
        entry_into_force_date=int(df.entry_into_force_date.notna().sum()),applicability_date=int(df.applicability_date.notna().sum()),
        repeal_or_expiry_date=int(df.repeal_or_expiry_date.notna().sum()),
        robot_provision_year=int(df.robot_provision_year.notna().sum()),
        provision_year_later_than_document_year=int(((df.robot_provision_year.notna())&(df.robot_provision_year>df.year_final+0)).sum()))
t=pd.DataFrame([dict(population="principal embodied instruments",**cov(P)),dict(population="principal binding embodied instruments",**cov(Bn)),dict(population="principal binding, dated before 2010",**cov(Bn[Bn.year_final<2010]))])
write_table("T70_supplement_v5_coverage",t,"Supplementary fields (v5) stated in the text: counts of principal instruments for which the model found each field in the document, and the number whose robot-relevant provision is dated later than the document's own year")
# bound parties among binding instruments
bp=Bn.bound_parties.fillna("").str.split("; ").explode(); bp=bp[bp!=""]
t2=bp.value_counts().rename_axis("party").reset_index(name="binding_instruments"); t2["share_pct"]=(100*t2.binding_instruments/len(Bn)).round(1)
write_table("T71_bound_parties_binding",t2,f"Whom the {len(Bn)} principal binding embodied instruments bind, as stated in their text (a document may bind several parties)")
# legal effect of standards among soft principal instruments that are standards
st=P[P.doc_type.eq("technical_standard")]
t3=st.legal_effect_of_standard.fillna("unknown").value_counts().rename_axis("legal_effect").reset_index(name="standards"); t3["share_pct"]=(100*t3.standards/max(len(st),1)).round(1)
write_table("T72_legal_effect_of_standards",t3,f"Legal effect of the {len(st)} principal instruments annotated as technical standards, as stated on the captured text")
# provision dating: binding instruments whose robot provision is dated later than the document year
d=Bn[Bn.robot_provision_year.notna()&(Bn.robot_provision_year>Bn.year_final)][["doc_id","title_en","jurisdiction_country","year_final","robot_provision_year","robot_provision_basis"]].sort_values("year_final")
write_table("T73_provision_dating",d,"Principal binding embodied instruments whose robot-relevant provision was added later than the document's recorded year, according to the amendment history in the text (the dates to use for provision-level trend analyses)")
print("T70-T73 written; provision later than document year:",len(d))
