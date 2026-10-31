# Brief for v3 narrative updates (round 2 added to the collection)

You are updating one narrative document of a content-analysis study so that every number, claim and figure/table reference matches the v3 data (original collection plus collection round 2). The v2 text is your starting point; keep its structure, voice, hedges and section order. Do not invent numbers: every figure you write must come from one of the files below, and if a v2 claim can no longer be verified from them, rewrite it to what the files support or drop it.

## Files (read these first)
- v2 source text to update: given in your task.
- v3 numbers: /home/user/embodied-ai-governance-v3/report/results_digest.md (auto-generated digest), /home/user/embodied-ai-governance-v3/data/results.json (full results), /home/user/embodied-ai-governance-v3/tables/*.md (every table with caption; T50-T60 are the round-2 tables, T53 is the before/after table), /home/user/embodied-ai-governance-v3/report/src/collection_round2.md (the round-2 companion report with its numbers already filled in).
- v2 numbers for comparison: /home/user/embodied-ai-governance-v2/report/results_digest.md.
- Collector reports and limitations of round 2: /home/user/collection-round-2/COLLECTOR_REPORTS.md.
- Figure captions available to embed: the CAPTIONS dict in /home/user/embodied-ai-governance-v3/scripts/16_build_reports.py (use {{Fxx}} and {{Txx}} placeholders exactly as the v2 text does; F50-F52 and T50-T60 are new).

## What changed between v2 and v3 (read T53 for the exact counts)
- A second collection round searched legal databases, treaty archives, standards catalogues and regulator sites with nine collector agents and seven scripted harvests. Candidates were de-duplicated against round 1, fetched from the issuing source, and annotated with the same metadata-blind extended-excerpt policy. Documents without text stay in an inventory and are not counted anywhere.
- Headline consequence: binding instruments that reach robots are no longer rare in the collection. The v2 finding "five binding instruments" becomes a much larger set dominated by vehicle, aviation, workplace and product-safety law and by national drone and automated-driving statutes. Keep the v2 insight that most binding rules reach robots through sector law rather than robotics statutes only if the v3 tables support it (check T59/T60 and the category tables).
- The research-versus-governance gap analysis, principle salience, mechanisms, regional profiles and trends were all re-run on v3; use their new values and significance markers. Where a v2 effect disappeared or reversed, say so plainly.
- The coverage audit against the 38 reference instruments changed (see T25 and the round-2 report).
- The embodied set is larger and its composition shifted toward governance instruments; the general-AI set barely changed. Research outputs are unchanged in number because round 2 targeted instruments.

## Rules
- Every number in the text must be traceable to the digest, results.json or a table. Round percentages as v2 did. Give n for every percentage.
- Keep "within this collection" framing and the limitations (model-labelled, excerpt-based, uneven capture, blocked hosts, exhausted search budget in round 2, standards annotated on scope text only).
- Mention round 2 where the method is described and add one short paragraph in the results on what round 2 changed, pointing to the companion report; do not duplicate the companion report.
- Figures/tables: keep the same {{Fxx}}/{{Txx}} embeds where the figure still exists; the figure titles and captions now carry v3 numbers, so adjust surrounding prose to match them.
- Do not change the document's YAML header except version labels (v2 -> v3) and the document count in titles/subtitles.
- Write the updated document to the path given in your task. Then write a short change log (bullet list of claims that changed, with old -> new numbers) to the path given in your task.
