#!/bin/bash
cd /home/user/embodied-ai-governance-v5
rm -f /home/user/embodied-ai-governance-v5.zip
zip -qr /home/user/embodied-ai-governance-v5.zip README.md LICENSE requirements.txt \
  report/brief.md report/brief.pdf report/analysis_report.md report/analysis_report.pdf report/analysis_report.html report/paper.md report/paper.pdf report/supplement.md report/supplement.pdf report/results_digest.md report/stage1_checkpoint.md report/src \
  review figures tables codebook dashboard/index.html dashboard/artifact.html \
  data/master_table.csv data/master_table.xlsx data/master_table_raw.csv data/data_dictionary.csv data/registry.csv data/files.csv data/results.json data/manual_overrides.csv data/overrides_applied.csv data/duplicates_removed.csv data/reference_instruments.csv \
  data/reliability_fields.csv data/reliability_fields_retest.csv data/reliability_fields_fulltext.csv data/reliability_fields_blind.csv data/reliability_fields_govext.csv data/reliability_team_crosscheck.csv \
  data/collector_coverage.csv data/not_captured.csv data/download_gaps.csv data/qa_flags.csv data/openalex_summary.csv data/text_features.csv data/lexicon_features.csv data/recovered_docs.csv \
  annotations scripts -x "scripts/__pycache__/*" "annotations/test/*"
ls -la /home/user/embodied-ai-governance-v5.zip
