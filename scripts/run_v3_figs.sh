#!/bin/bash
cd /home/user/embodied-ai-governance-v4
set -e
python3 scripts/20_figures_v2.py > logs/v3_20.log 2>&1
python3 scripts/18_analysis_D.py > logs/v3_18.log 2>&1
python3 scripts/21_round2_report.py > logs/v3_21.log 2>&1
python3 scripts/10_dashboard.py > logs/v3_10.log 2>&1
echo FIGS_DONE
