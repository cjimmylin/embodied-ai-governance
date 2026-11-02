"""Append the round-2 collection to the v3 project before re-assembly.

Round-2 candidates with a usable text (fetched, or a scope/abstract text collected for blocked catalogue pages) become
registry rows (set_primary = "round2") so that they are annotated, assembled and analysed exactly like the original
collection. Every candidate, with or without text, is written to data/round2_inventory.csv so that the collection
report can separate the discovered inventory from the content-analysed subset.
"""
import pandas as pd, shutil, glob, os, sys
V3="/home/user/embodied-ai-governance-v5/"; R2="/home/user/collection-round-2/"
sys.path.insert(0,V3+"scripts"); from regions import lookup

reg=pd.read_csv(V3+"data/registry.csv",dtype=str,keep_default_na=False)
reg=reg[~reg.doc_id.str.startswith("R2-")]
r2=pd.read_csv(R2+"data/registry.csv",dtype=str,keep_default_na=False)
cand=pd.read_csv(R2+"candidates_merged.csv",dtype=str,keep_default_na=False)
fs=pd.read_csv(R2+"fetch_status.csv",dtype=str,keep_default_na=False).drop_duplicates("doc_id",keep="last").set_index("doc_id")

# --- inventory: every candidate, its fetch outcome and whether it is content-analysed
ann_ids=set(os.path.basename(p)[:-5] for p in glob.glob(R2+"annotations/round2/R2-*.json"))
inv=cand.copy()
inv["fetch_status"]=inv.doc_id.map(fs.status).fillna("not_attempted")
inv["fetch_url"]=inv.doc_id.map(fs.url).fillna("")
inv["text_status"]=inv.doc_id.map(r2.set_index("doc_id").text_status).fillna("missing")
inv["has_text"]=inv.text_status.isin(["ok","agent_abstract"])
inv["content_analysed"]=inv.doc_id.isin(ann_ids)
inv["study_region"]=inv.jurisdiction.map(lambda c: lookup(c)["study_region"])
inv.to_csv(V3+"data/round2_inventory.csv",index=False)

# --- registry rows for texted candidates only
r2=r2[r2.text_usable.astype(str)=="True"].copy()
r2["region"]=r2.meta_country.map(lambda c: lookup(c)["study_region"])
for c in reg.columns:
    if c not in r2.columns: r2[c]=""
r2=r2[reg.columns]
pd.concat([reg,r2],ignore_index=True).to_csv(V3+"data/registry.csv",index=False)

tf=pd.read_csv(V3+"data/text_features.csv",dtype=str,keep_default_na=False); t2=pd.read_csv(R2+"data/text_features.csv",dtype=str,keep_default_na=False)
tf=tf[~tf.file_rel.str.startswith("R2-")]; t2=t2[t2.file_rel.str[:-4].isin(set(r2.doc_id))]
for c in tf.columns:
    if c not in t2.columns: t2[c]=""
pd.concat([tf,t2[tf.columns]],ignore_index=True).to_csv(V3+"data/text_features.csv",index=False)

os.makedirs(V3+"annotations/round2",exist_ok=True)
for p in glob.glob(V3+"annotations/round2/R2-*.json"): os.remove(p)
n=0
for p in glob.glob(R2+"annotations/round2/R2-*.json"): shutil.copy(p,V3+"annotations/round2/"); n+=1
print(f"inventory {len(inv)} candidates; with text {int(inv.has_text.sum())}; content-analysed {int(inv.content_analysed.sum())}")
print(f"registry rows {len(reg)+len(r2)} (round-2 rows {len(r2)}); annotations copied {n}")
