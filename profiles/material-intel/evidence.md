# Evidence extraction

Extract, in English, what the supplied source itself reports. This record is shared by every language edition, so it must contain only facts present in the supplied content. It is not a summary and not an opinion.

Rules:

- Use the exact string `not reported` for any field the source does not state. Never estimate TRL, cost, carbon, yield, throughput or timelines.
- `claims`: up to five central claims. For each, copy a supporting `quote` verbatim from the supplied content (one contiguous span of 12–300 characters, no ellipses, no paraphrase) and give `location` as the visible section heading, figure or table label, or `abstract` / `body` when no label is visible.
- `material_system`: materials, polymers, grades or chemistries studied, as named.
- `data_scale`: number of samples, experiments, formulations, images, runs, or dataset name and size, exactly as reported.
- `batches_or_lots`: whether multiple batches, lots, suppliers or instruments were used, as reported.
- `conditions`: processing and test conditions that the results depend on.
- `baseline`: what the method is compared against.
- `validation_method`: how results were validated (split type, held-out conditions, experimental confirmation, field trial).
- `validation_setting`: one of `simulation`, `lab`, `pilot`, `production`, `mixed`, `not reported`.
- `independent_replication`: `reported` only if the source cites an independent replication; otherwise `not reported`.
- `event_date`: the date of the reported event (e.g. a deployment or release date) if stated, else `unknown`. Do not use today's date.
- `results`: reported quantitative or qualitative results, each with its number and unit exactly as written.
- `limitations`: limitations stated by the source, plus obvious unaddressed gaps phrased as `not addressed: ...` (e.g. `not addressed: cross-supplier validation`).
- `reading_entry`: which visible section, figure or table is most worth reading first and why, or empty if the content shows no structure.

Return valid JSON only:
{
  "material_system": "...",
  "data_scale": "...",
  "batches_or_lots": "...",
  "conditions": "...",
  "baseline": "...",
  "validation_method": "...",
  "validation_setting": "...",
  "independent_replication": "...",
  "event_date": "...",
  "claims": [{"claim": "...", "quote": "...", "location": "..."}],
  "results": ["..."],
  "limitations": ["..."],
  "reading_entry": "..."
}
