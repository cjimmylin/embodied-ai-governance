# Human validation of the model labels: instructions for coders

← Back to the **[project hub](https://github.com/cjimmylin/embodied-ai-governance/blob/main/docs/index.html)** (all deliverables) · [live hub page on claude.ai](https://claude.ai/artifact/QRA3FAoGPUDJeNAg4QUQoA)

Purpose: the study's labels were produced by a language model and checked only against other model runs. This exercise produces the first human-coded labels, so that human-versus-model agreement can be reported per field and the headline counts corrected for measurement error.

## Materials in this folder

- `sample.csv`: 200 documents in five strata of 40 (embodied principal binding instruments; embodied principal soft or draft instruments; embodied research outputs; embodied reports, news and grey literature; general-AI governance documents), drawn with seed 2028 from the usable documents of version 4. 112 are from the database-harvested round 2 and 88 from the web-collected round 1; 157 are in English, 12 Japanese, 8 Chinese, 6 Portuguese, 4 Spanish, 4 French. Each row gives the document's title, jurisdiction, year, language, source URL and the path of its text in the project package.
- `coding_sheet.xlsx`: one row per document with drop-down lists for the six single-choice fields, a free-text column for robot types, twelve principle columns scored 0, 1 or 2, and a notes column. The `Codes` tab lists the allowed values. Do not open `answer_key_model_labels.csv` before coding.
- The codebook (`codebook/codebook.md`) and the taxonomies (`codebook/taxonomies.md`) in the package define every field and value.

## Procedure

1. Two coders, each coding every document independently. Coders should read the document text (at least the first 6,000 characters and the end; the whole text when it is short) and may open the source URL. Chinese and Japanese documents should go to coders who read those languages; machine translation is acceptable only as an aid, and should be noted.
2. Code the six single-choice fields, the robot types (semicolon-separated codes from the taxonomy; leave empty if none), and the twelve principles at 0 (absent), 1 (mentioned) or 2 (specified in depth: an operative requirement, a defined procedure or a quantified threshold).
3. Record initials and minutes per document. Expect 8 to 15 minutes per document; about 30 hours per coder for the full sample.
4. After both coders finish, disagreements are adjudicated jointly, and the adjudicated set becomes the gold standard.
5. Return the two completed sheets and the adjudicated sheet. The analysis script will compute Cohen's kappa (quadratic-weighted for relevance and the principles) between the coders and between the gold standard and the model labels, per field, and the measurement-error correction of the headline shares.

## What the result settles

With this sample, the study can say whether the model's labels for the fields that define its analysis sets (document class, binding nature, status, AI scope, relevance) agree with domain experts, and by how much the counts of binding and robot-relevant instruments should be adjusted. Without it, every reliability figure in the study remains a consistency check between machines.
