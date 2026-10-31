#!/bin/bash
# Package Stage 1 deliverables into a single zip for download.
cd /home/user/embodied-ai-governance-v4
rm -f /home/user/embodied-ai-governance-v4-stage1.zip
zip -qr /home/user/embodied-ai-governance-v4-stage1.zip data/master_table.csv data/master_table.xlsx data/data_dictionary.csv data/registry.csv data/files.csv \
  data/reliability_fields.csv data/reliability_fields_retest.csv data/reliability_team_crosscheck.csv data/collector_coverage.csv data/not_captured.csv data/download_gaps.csv data/qa_flags.csv \
  data/openalex_summary.csv data/text_features.csv data/lexicon_features.csv codebook dashboard/index.html report/stage1_checkpoint.md report/stage2_analysis_plan.md annotations scripts -x "scripts/__pycache__/*" "dashboard/shot-*"
ls -la /home/user/embodied-ai-governance-v4-stage1.zip
