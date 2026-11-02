#!/bin/bash
# v5 pipeline: round-3 merge, assembly, overrides, then the post-assembly chain (run_v5_post.sh) and the reports.
cd /home/user/embodied-ai-governance-v5
set -e
mkdir -p logs
python3 /home/user/collection-round-3/scripts/merge_round3.py /home/user/embodied-ai-governance-v5/ > logs/v5_merge.log 2>&1
python3 scripts/07_assemble.py > logs/v5_07.log 2>&1
python3 scripts/07b_apply_overrides.py > logs/v5_07b.log 2>&1
bash scripts/run_v5_post.sh
python3 scripts/16_build_reports.py > logs/v5_16.log 2>&1
echo V5_ALL_DONE
