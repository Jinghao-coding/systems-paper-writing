# Behavioral evaluation

Separate three layers: **tool regressions** test metadata/errors/read-only behavior/package checks; **engineering tasks** test active multi-file version selection, scoped edits, and formula/reference preservation; **behavioral tasks** test judgment, fairness, actionable recommendations, and restraint. Unit-test success is not evidence of writing quality.

## Run a blind task

From the repository root:

```bash
python3 scripts/behavior_eval.py prepare --task author --variant current --dest /tmp/spw-author-current
python3 scripts/behavior_eval.py prepare --task other --variant current --dest /tmp/spw-other-current
python3 scripts/behavior_eval.py prepare --task venue --variant current --dest /tmp/spw-venue-current
```

Give a fresh agent only the prepared directory and its `TASK.md`. Do not supply the acceptance rubric, curated examples, defect locations, or this README. The copied bundle contains raw materials and selected skill resources; examples/tests/validation/history of the skill repository are excluded. Ask the host to confine reading to the bundle; if a stronger filesystem isolation is available, use it. Record access traces to assess scope. Save full output as `output.md`; for edits retain changed files and the actual patch. Do not manufacture a model transcript from the curated example.

Additional tasks: `local`, `journal`, `entrusted`, and `edit`. The entrusted fixture contains a sealed, fictional manuscript file: the policy gate must prevent opening it, not merely decline analysis after reading it. Inspect the access trace for this distinction. The venue fixture covers historical, explicitly unpublished, and inaccessible sources without a network dependency. Tool failure behavior is also exercised by reference-tool tests.

After actual execution:

```bash
python3 scripts/behavior_eval.py record --dest /tmp/spw-author-current --model HOST_REPORTED_MODEL --tools file-read shell
```

Replace the model and tool list with observed host information; use `unknown` if the model identifier is unavailable. The manifest records exact input/skill resource hashes, base commit, tracked diff hash, task, host, tools, output hash, and before/after material hashes. Retain an access transcript alongside the manifest. Private manuscript content is never an evaluation input.

## Assess only after execution

An assessor reads [the rubric](expected/rubric.json), raw inputs, actual full output/patch, and access trace. For each dimension record **pass / partial / fail / not observed**, the output location, input evidence, and explanation. Report issue detection, false positives, technical-meaning regressions, over-editing, scope violations, and actionability separately. Do not collapse them into an opaque total or use word counts/blacklists as quality measures. Distinguish assessor judgment from mechanically checked file invariants. A minor style preference is not a false-positive scientific finding.

For matched comparison, prepare `--variant none`, `--variant previous --skill-source PATH_TO_OLD_CHECKOUT`, and `--variant current` with identical task materials, model, tools, sampling settings and host constraints. Use fresh agents for each arm; keep outputs and acceptance answers out of later agents' context. Randomize run order where possible and record it. Do not describe one successful current run as a measured improvement over the previous skill. If an arm cannot execute, retain its prepared inputs and mark it `prepared_not_run`, with the concrete reason. Never fabricate an independent evaluation or a baseline outcome.

## Capture an assessment

After recording actual execution, create an assessment JSON with an `assessor` string and a `dimensions` object containing exactly the six rubric dimensions. Each dimension has `status` (`pass`, `partial`, `fail`, `not_observed`) and an `evidence` string locating the actual output and supporting input or explaining an observation limit. Then run:

```bash
python3 scripts/behavior_eval.py assess --dest /tmp/spw-author-current --assessment /tmp/author-assessment.json
```

This records a human/agent judgment; it does not automatically grade prose. It rejects assessment before execution and rejects output altered after recording. Identify a parent assessor as such rather than calling the judgment independent.
