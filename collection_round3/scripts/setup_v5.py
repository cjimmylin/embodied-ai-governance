"""Create /home/user/embodied-ai-governance-v5 from v4 and apply the v5 code changes.
Run after the full-text and supplementary annotation passes have finished in v4 (their folders are copied along).
"""
import os, re, shutil, sys, glob
V4="/home/user/embodied-ai-governance-v4/"; V5="/home/user/embodied-ai-governance-v5/"
if os.path.exists(V5): print("v5 exists; patching only")
else:
    shutil.copytree(V4,V5,ignore=shutil.ignore_patterns("__pycache__","*.zip","collection_round2","shot-*.png"))
    print("copied v4 -> v5")
# 1) repoint absolute paths in scripts
for p in glob.glob(V5+"scripts/*.py")+glob.glob(V5+"scripts/*.sh")+glob.glob(V5+"scripts/*.js"):
    s=open(p).read(); t=s.replace("/home/user/embodied-ai-governance-v4","/home/user/embodied-ai-governance-v5")
    if t!=s: open(p,"w").write(t)
# 2) assembly: round-3 annotations and the full-text re-reads override earlier labels
p=V5+"scripts/07_assemble.py"; s=open(p).read()
old='for folder in [ANN, ANN+"_clean", "annotations/gov_extended", "annotations/round2", "annotations/cjk_fix"]:'
new='for folder in [ANN, ANN+"_clean", "annotations/gov_extended", "annotations/round2", "annotations/cjk_fix", "annotations/round3", "annotations/fulltext_v5"]:   # v5: round-3 labels and full-text re-reads of truncated instruments override earlier labels'
assert old in s; s=s.replace(old,new)
s=s.replace('for p in sorted(glob.glob(B+folder+"/D*.json"))+sorted(glob.glob(B+folder+"/R2-*.json")):','for p in sorted(glob.glob(B+folder+"/D*.json"))+sorted(glob.glob(B+folder+"/R2-*.json"))+sorted(glob.glob(B+folder+"/R3-*.json")):')
s=s.replace('"_excerpt_extended":folder.endswith("gov_extended") or folder.endswith("round2") or folder.endswith("cjk_fix")','"_excerpt_extended":folder.endswith("gov_extended") or folder.endswith("round2") or folder.endswith("cjk_fix") or folder.endswith("round3") or folder.endswith("fulltext_v5"),"_fulltext_v5":folder.endswith("fulltext_v5")')
open(p,"w").write(s); print("07_assemble patched")
# 3) analysis_common: database-harvested rounds (2 and 3) versus the web-collected round 1; a separate round-3 flag
p=V5+"scripts/analysis_common.py"; s=open(p).read()
old='    a["round2"]=(a.collection_set=="round2")'
new='    a["round2"]=a.collection_set.isin(["round2","round3"])   # v5: database-harvested rounds (2 and 3) versus the web-collected round 1\n    a["round3"]=(a.collection_set=="round3")'
assert old in s; s=s.replace(old,new); open(p,"w").write(s); print("analysis_common patched")
# 4) collector code regex in 07_assemble already accepts 2-3 letters; registry builder untouched
# 5) the post-assembly runner gains the supplementary merge and the full-text comparison
p=V5+"scripts/run_v4_post.sh"; s=open(p).read()
s=s.replace("python3 scripts/07c_v4_units_and_tiers.py > logs/v4_07c.log 2>&1","python3 scripts/07c_v4_units_and_tiers.py > logs/v4_07c.log 2>&1\npython3 scripts/07d_supplement_v5.py > logs/v5_07d.log 2>&1\npython3 scripts/27_fulltext_compare.py > logs/v5_27.log 2>&1 || echo \"fulltext compare skipped\"")
s=s.replace("python3 scripts/24_precision_vs_rules.py > logs/v4_24.log 2>&1 || echo \"precision comparison skipped\"","python3 scripts/24_precision_vs_rules.py > logs/v4_24.log 2>&1 || echo \"precision comparison skipped\"\npython3 scripts/25_round3_report.py > logs/v5_25.log 2>&1 || echo \"round-3 report skipped\"")
s=s.replace("echo V4_PIPELINE_DONE","echo V5_PIPELINE_DONE")
open(V5+"scripts/run_v5_post.sh","w").write(s); os.chmod(V5+"scripts/run_v5_post.sh",0o755); print("run_v5_post.sh written")
for p in glob.glob(V5+"scripts/__pycache__/*"): os.remove(p)
print("done")
