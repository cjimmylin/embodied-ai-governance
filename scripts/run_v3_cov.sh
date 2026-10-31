#!/bin/bash
cd /home/user/embodied-ai-governance-v4
set -e
python3 scripts/18_analysis_D.py > logs/v3_18.log 2>&1
python3 scripts/21_round2_report.py > logs/v3_21.log 2>&1
python3 scripts/17_supp_tables.py > logs/v3_17.log 2>&1
echo COV_DONE
