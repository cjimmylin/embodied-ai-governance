#!/bin/bash
cd /home/user/embodied-ai-governance-v5
rm -f /home/user/embodied-ai-governance-v5.zip
rm -rf collection_round2 && python3 - <<'PY'
import shutil
shutil.copytree("/home/user/collection-round-2","/home/user/embodied-ai-governance-v5/collection_round2",ignore=shutil.ignore_patterns("texts","raw","texts_agent","logs","annotations","fetch_status_partial.csv","__pycache__","*.pdf"))
PY
zip -qr /home/user/embodied-ai-governance-v5.zip README.md LICENSE requirements.txt \
  report/collection_round2.md report/collection_round2.pdf report/collection_round2.html report/methods_document_discovery.md report/methods_document_discovery.pdf report/methods_document_discovery.html report/methods_review_and_revision.md report/methods_review_and_revision.pdf report/methods_review_and_revision.html report/brief.md report/brief.pdf report/analysis_report.md report/analysis_report.pdf report/analysis_report.html report/paper.md report/paper.pdf report/supplement.md report/supplement.pdf report/results_digest.md report/stage1_checkpoint.md report/v4_summary.md report/src \
  review figures tables codebook report/src_v3 report/src_v2 dashboard/index.html dashboard/artifact.html \
  data/master_table.csv data/master_table.xlsx data/master_table_raw.csv data/data_dictionary.csv data/registry.csv data/files.csv data/results.json data/manual_overrides.csv data/overrides_applied.csv data/duplicates_removed.csv data/reference_instruments.csv data/round2_inventory.csv data/lexicon_cache_key.json data/manual_overrides_v4.csv data/run_manifest.json data/ai_content_flags.csv data/reliability_variants.csv data/reliability_fields_r2opus.csv data/reliability_fields_r2rerun.csv \
  data/reliability_fields.csv data/reliability_fields_retest.csv data/reliability_fields_fulltext.csv data/reliability_fields_blind.csv data/reliability_fields_govext.csv data/reliability_team_crosscheck.csv \
  data/collector_coverage.csv data/not_captured.csv data/download_gaps.csv data/qa_flags.csv data/openalex_summary.csv data/text_features.csv data/lexicon_features.csv data/recovered_docs.csv \
  annotations scripts collection_round2 -x "scripts/__pycache__/*" "annotations/test/*" "collection_round2/texts/*" "collection_round2/raw/*" "collection_round2/texts_agent/*" "collection_round2/annotations/*/_inputs/*" "review/v3_reviews/shots/*"
ls -la /home/user/embodied-ai-governance-v5.zip
