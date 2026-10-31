#!/bin/bash
# Package all Stage 1 + Stage 2 deliverables into one zip.
cd /home/user/embodied-ai-governance-v4
rm -f /home/user/embodied-ai-governance-v4-full.zip
zip -qr /home/user/embodied-ai-governance-v4-full.zip \
  report/analysis_report.md report/analysis_report.pdf report/analysis_report.html \
  report/paper.md report/paper.pdf report/paper.html \
  report/supplement.md report/supplement.pdf report/supplement.html \
  report/stage1_checkpoint.md report/stage2_analysis_plan.md report/results_digest.md report/src \
  figures tables codebook dashboard/index.html \
  data/master_table.csv data/master_table.xlsx data/data_dictionary.csv data/registry.csv data/files.csv data/results.json \
  data/reliability_fields.csv data/reliability_fields_retest.csv data/reliability_team_crosscheck.csv \
  data/collector_coverage.csv data/not_captured.csv data/download_gaps.csv data/qa_flags.csv \
  data/openalex_summary.csv data/text_features.csv data/lexicon_features.csv data/recovered_docs.csv \
  annotations scripts -x "scripts/__pycache__/*" "annotations/test/*"
ls -la /home/user/embodied-ai-governance-v4-full.zip
