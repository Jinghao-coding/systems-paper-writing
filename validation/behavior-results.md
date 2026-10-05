# Actual behavioral executions

Date: 2026-10-05. Each run used a fresh subagent context and only a prepared task bundle. Full output bytes are retained as plain-text transcripts; the original file was named output.md. Manifests retain its hash. Access logs are agent-reported; material preservation and the edit patch replay were checked by the parent. Assessment JSON identifies the parent assessor explicitly.

All three primary tasks ran with current, previous (786fec6b / 1.2.0), and no-skill variants. Raw material hashes match across each three-arm comparison. No model override was used; the exact serving model identifier and sampler settings were not exposed, and are recorded as unknown/host defaults. Run order was current, previous, then none, with three tasks concurrent within each group. These are task-level observations, not a calibrated model comparison.

Acceptance criteria were held outside the bundles. Skill resources copied into a run excluded examples, tests, validation outputs and repository history. The host enforced fresh conversation context; directory confinement was instructed and checked against reported access, not implemented as a separate filesystem sandbox.

Pass means the inspected criterion was satisfied in that output. Partial means a useful output omitted a requested distinction. Not observed marks editing behavior in a review-only task. There is no aggregate score.

| Run / full output | Detection | False positives | Meaning preservation | Over-editing | Scope | Actionability |
| --- | --- | --- | --- | --- | --- | --- |
| [author-current](runs/author-current/output.txt) | pass | pass | pass | not observed | pass | pass |
| [author-previous](runs/author-previous/output.txt) | pass | pass | pass | not observed | pass | partial |
| [author-none](runs/author-none/output.txt) | pass | pass | pass | not observed | pass | partial |
| [other-current](runs/other-current/output.txt) | pass | pass | pass | not observed | pass | pass |
| [other-previous](runs/other-previous/output.txt) | pass | pass | pass | not observed | pass | pass |
| [other-none](runs/other-none/output.txt) | pass | pass | pass | not observed | pass | pass |
| [venue-current](runs/venue-current/output.txt) | pass | pass | pass | not observed | pass | pass |
| [venue-previous](runs/venue-previous/output.txt) | pass | pass | pass | not observed | pass | pass |
| [venue-none](runs/venue-none/output.txt) | pass | pass | pass | not observed | pass | pass |
| [local-current](runs/local-current/output.txt) | pass | pass | pass | pass | pass | pass |
| [journal-current](runs/journal-current/output.txt) | pass | pass | pass | pass | pass | pass |
| [entrusted-current](runs/entrusted-current/output.txt) | pass | pass | pass | not observed | pass | pass |
| [edit-current](runs/edit-current/output.txt) | pass | pass | pass | pass | pass | pass |

## Observed differences

- All nine primary-task runs detected the core numerical and admission-population conflicts. The old and no-skill variants also handled the simulated policy states correctly; these fixtures did not establish a general gain in defect detection.
- The current author output explicitly separated existing-material fixes, conditional reanalysis, new evidence, and research positioning. Previous/no-skill author outputs provided useful priorities but did not clearly distinguish existing-data reanalysis as its own layer; their actionability dimension is partial on that rubric.
- Current venue analysis read SKILL plus venue-guide; previous venue analysis also loaded submission-preparation and style-analysis. Current local polishing read only SKILL, style-analysis, and its target inputs, retaining the already-clear paragraph exactly. These are observed routing behaviors, not prose-quality scores.
- The journal task recognized explanation of an existing epoch rule and supplied a corrected English sentence. The entrusted task did not read the present sealed manuscript according to its access log and produced no substantive review.
- The edit task changed only the requested abstract, introduction and captions. Independent patch replay reproduced the complete edited tree; labels, equation/definitions, inactive history and the clear non-preemption paragraph were preserved.

For each row, sibling `manifest.json`, `assessment.json`, and `access-log.txt` files record fingerprints, six dimension-specific judgments and evidence. The edit row also has `engineering-checks.json` and `revision.patch`. Full prepared bundles, including actual skill resources and materials before/after, were archived locally with this task.
