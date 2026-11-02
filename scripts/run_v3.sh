#!/bin/bash
# Full v3 pipeline: merge round-2 collection into the v2 project copy, then re-run every analysis, the dashboard and the reports.
cd /home/user/embodied-ai-governance-v5
set -e
mkdir -p logs
python3 scripts/merge_round2.py > logs/v3_merge.log 2>&1
python3 scripts/05_lexicons.py > logs/v3_05.log 2>&1
python3 scripts/07_assemble.py > logs/v3_07.log 2>&1
python3 scripts/07b_apply_overrides.py > logs/v3_07b.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_opus > logs/v3_09a.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_sonnet_rerun _retest > logs/v3_09b.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_fulltext _fulltext > logs/v3_09c.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_blind _blind > logs/v3_09d.log 2>&1
python3 scripts/09_reliability.py annotations/gov_extended _govext > logs/v3_09e.log 2>&1
python3 scripts/13_analysis_A.py > logs/v3_13.log 2>&1
python3 scripts/14_analysis_B.py > logs/v3_14.log 2>&1
python3 scripts/15_analysis_C.py > logs/v3_15.log 2>&1
python3 scripts/18_analysis_D.py > logs/v3_18.log 2>&1
python3 scripts/19_fulltext_validation.py > logs/v3_19.log 2>&1
python3 scripts/17_supp_tables.py > logs/v3_17.log 2>&1
python3 scripts/20_figures_v2.py > logs/v3_20.log 2>&1
python3 scripts/21_round2_report.py > logs/v3_21.log 2>&1
python3 scripts/10_dashboard.py > logs/v3_10.log 2>&1
python3 scripts/11_stage1_report.py > logs/v3_11.log 2>&1 || echo "stage1 report failed (non-fatal)"
echo V3_PIPELINE_DONE
