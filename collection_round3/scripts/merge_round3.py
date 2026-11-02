"""Append the round-3 collection to the v5 project before re-assembly.

Round-3 documents are (a) round-2 candidates whose text was recovered by the round-3 collectors (they keep their R2- doc_id
and are marked set_primary = "round3" because their text and labels arrived in round 3), (b) reference-list instruments
fetched from the title (REF- rows, given R3- ids), and (c) new candidates from the round-3 harvest (R3- ids).
Every round-3 document with a usable text becomes a registry row with text features, and its annotation is copied to
annotations/round3/. data/round3_inventory.csv lists every round-3 target and candidate with its outcome.
"""
import pandas as pd, shutil, glob, os, sys
V5=sys.argv[1] if len(sys.argv)>1 else "/home/user/embodied-ai-governance-v5/"
R3="/home/user/collection-round-3/"
sys.path.insert(0,V5+"scripts"); from regions import lookup

reg=pd.read_csv(V5+"data/registry.csv",dtype=str,keep_default_na=False)
r3=pd.read_csv(R3+"data/registry.csv",dtype=str,keep_default_na=False)
cand=pd.read_csv(R3+"candidates_merged.csv",dtype=str,keep_default_na=False)
fs=pd.read_csv(R3+"fetch_status.csv",dtype=str,keep_default_na=False).drop_duplicates("doc_id",keep="last").set_index("doc_id") if os.path.exists(R3+"fetch_status.csv") else None

ann_ids=set(os.path.basename(p)[:-5] for p in glob.glob(R3+"annotations/round3/*.json"))
inv=cand.copy()
if fs is not None:
    inv["fetch_status"]=inv.doc_id.map(fs.status).fillna("not_attempted"); inv["fetch_url"]=inv.doc_id.map(fs.url).fillna("")
else:
    inv["fetch_status"]=""; inv["fetch_url"]=""
inv["text_status"]=inv.doc_id.map(r3.set_index("doc_id").text_status).fillna("missing")
inv["has_text"]=inv.text_status.isin(["ok","agent_abstract","recovered"])
inv["content_analysed"]=inv.doc_id.isin(ann_ids)
inv["study_region"]=inv.jurisdiction.map(lambda c: lookup(c)["study_region"])
inv.to_csv(V5+"data/round3_inventory.csv",index=False)

# recovered round-2 ids replace their textless round-2 registry rows; new ids are appended
r3=r3[r3.text_usable.astype(str)=="True"].copy()
r3["region"]=r3.meta_country.map(lambda c: lookup(c)["study_region"])
for c in reg.columns:
    if c not in r3.columns: r3[c]=""
r3=r3[reg.columns]
reg=reg[~reg.doc_id.isin(set(r3.doc_id))]
pd.concat([reg,r3],ignore_index=True).to_csv(V5+"data/registry.csv",index=False)

tf=pd.read_csv(V5+"data/text_features.csv",dtype=str,keep_default_na=False); t3=pd.read_csv(R3+"data/text_features.csv",dtype=str,keep_default_na=False)
t3=t3[t3.file_rel.str[:-4].isin(set(r3.doc_id))]
tf=tf[~tf.file_rel.isin(set(t3.file_rel))]
for c in tf.columns:
    if c not in t3.columns: t3[c]=""
pd.concat([tf,t3[tf.columns]],ignore_index=True).to_csv(V5+"data/text_features.csv",index=False)

os.makedirs(V5+"annotations/round3",exist_ok=True)
for p in glob.glob(V5+"annotations/round3/*.json"): os.remove(p)
n=0
for p in glob.glob(R3+"annotations/round3/*.json"): shutil.copy(p,V5+"annotations/round3/"); n+=1
print(f"round-3 inventory {len(inv)} rows; with text {int(inv.has_text.sum())}; content-analysed {int(inv.content_analysed.sum())}")
print(f"registry rows {len(reg)+len(r3)} (round-3 rows {len(r3)}: recovered R2 {int(r3.doc_id.str.startswith('R2-').sum())}, new R3 {int(r3.doc_id.str.startswith('R3-').sum())}); annotations copied {n}")
