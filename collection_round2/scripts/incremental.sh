#!/bin/bash
# Incremental round-2 pipeline: merge new candidates, fetch texts for new ids, annotate newly texted documents.
cd /home/user/collection-round-2
TAG=${1:-inc}
while pgrep -f "^python3 scripts/fetch_texts.py" >/dev/null; do sleep 15; done
python3 scripts/merge_candidates.py > logs/merge_$TAG.log 2>&1
python3 scripts/fetch_texts.py > logs/fetch_$TAG.log 2>&1
python3 scripts/build_registry.py >> logs/fetch_$TAG.log 2>&1
python3 - <<'PY'
import os, pandas as pd, glob
B="/home/user/collection-round-2/"
m=pd.read_csv(B+"candidates_merged.csv",dtype=str,keep_default_na=False)
done=set(os.path.basename(p)[:-5] for p in glob.glob(B+"annotations/round2/R2-*.json"))
queued=set()
for f in glob.glob(B+"data/ids_with_text*.txt"): queued|=set(open(f).read().split())
ids=[d for d in m.doc_id if os.path.exists(B+f"texts/{d}.txt") and d not in done and d not in queued]
import time; name=B+f"data/ids_with_text_{int(time.time())}.txt"; open(name,"w").write("\n".join(ids)); print(name,len(ids))
open(B+"data/_last_ids_file.txt","w").write(name)
PY
IDS=$(cat data/_last_ids_file.txt)
N=$(wc -l < "$IDS")
if [ "$N" -gt 0 ]; then nohup python3 scripts/04_annotate_r2.py --ids "$IDS" --out annotations/round2 --workers 3 --head 100000 --mid 6000 --tail 4000 --blind --policy v2 > logs/annotate_$TAG.log 2>&1 & fi
echo "INCREMENTAL_DONE $TAG new_ids=$N"
