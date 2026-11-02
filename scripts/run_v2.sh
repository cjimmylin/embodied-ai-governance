#!/bin/bash
# Full v2 pipeline from stored annotations to reports. Waits for the two blind annotation runs first.
cd /home/user/embodied-ai-governance-v5
until grep -q "^finished" logs/annotate_gov_extended.log && grep -q "^finished" logs/annotate_blind160.log; do sleep 20; done
set -e
python3 scripts/07_assemble.py > logs/v2_07.log 2>&1
python3 scripts/07b_apply_overrides.py > logs/v2_07b.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_opus > logs/v2_09a.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_sonnet_rerun _retest > logs/v2_09b.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_fulltext _fulltext > logs/v2_09c.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_blind _blind > logs/v2_09d.log 2>&1
python3 scripts/09_reliability.py annotations/gov_extended _govext > logs/v2_09e.log 2>&1
python3 scripts/13_analysis_A.py > logs/v2_13.log 2>&1
python3 scripts/14_analysis_B.py > logs/v2_14.log 2>&1
python3 scripts/15_analysis_C.py > logs/v2_15.log 2>&1
python3 scripts/18_analysis_D.py > logs/v2_18.log 2>&1
python3 scripts/19_fulltext_validation.py > logs/v2_19.log 2>&1
python3 scripts/17_supp_tables.py > logs/v2_17.log 2>&1
python3 scripts/20_figures_v2.py > logs/v2_20.log 2>&1
python3 scripts/10_dashboard.py > logs/v2_10.log 2>&1
python3 scripts/11_stage1_report.py > logs/v2_11.log 2>&1 || echo "stage1 report failed (non-fatal)"
echo V2_PIPELINE_DONE
