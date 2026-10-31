#!/bin/bash
set -e
cd /home/user/embodied-ai-governance-v4
python3 scripts/07_assemble.py 2>&1 | grep -v "not found" | head -3
python3 scripts/09_reliability.py annotations/reliability_opus 2>&1 | grep -v "not found" | tail -3
python3 scripts/09_reliability.py annotations/reliability_sonnet_rerun _retest 2>&1 | grep -v "not found" | tail -3
python3 scripts/10_dashboard.py
python3 scripts/11_stage1_report.py 2>&1 | tail -8
