#!/bin/bash
cd /home/user/embodied-ai-governance-v4
set -e
python3 scripts/07c_v4_units_and_tiers.py > logs/v4_07c.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_opus > logs/v4_09a.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_sonnet_rerun _retest > logs/v4_09b.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_fulltext _fulltext > logs/v4_09c.log 2>&1
python3 scripts/09_reliability.py annotations/reliability_blind _blind > logs/v4_09d.log 2>&1
python3 scripts/09_reliability.py annotations/gov_extended _govext > logs/v4_09e.log 2>&1
python3 scripts/09b_reliability_round2.py annotations/reliability_round2_opus _r2opus > logs/v4_09f.log 2>&1 || echo "round-2 opus reliability skipped"
python3 scripts/09b_reliability_round2.py annotations/reliability_round2_rerun _r2rerun > logs/v4_09g.log 2>&1 || echo "round-2 rerun reliability skipped"
python3 scripts/09c_reliability_variants.py > logs/v4_09h.log 2>&1 || echo "variants skipped"
python3 scripts/13_analysis_A.py > logs/v4_13.log 2>&1
python3 scripts/14_analysis_B.py > logs/v4_14.log 2>&1
python3 scripts/15_analysis_C.py > logs/v4_15.log 2>&1
python3 scripts/18_analysis_D.py > logs/v4_18.log 2>&1
python3 scripts/19_fulltext_validation.py > logs/v4_19.log 2>&1
python3 scripts/17_supp_tables.py > logs/v4_17.log 2>&1
python3 scripts/20_figures_v2.py > logs/v4_20.log 2>&1
python3 scripts/21_round2_report.py > logs/v4_21.log 2>&1
python3 scripts/24_precision_vs_rules.py > logs/v4_24.log 2>&1 || echo "precision comparison skipped"
python3 scripts/23_run_manifest.py > logs/v4_23.log 2>&1 || echo "manifest skipped"
python3 scripts/10_dashboard.py > logs/v4_10.log 2>&1
python3 scripts/11_stage1_report.py > logs/v4_11.log 2>&1 || echo "stage1 report failed (non-fatal)"
echo V4_PIPELINE_DONE
