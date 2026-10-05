<div align="center">

# Systems Paper Writing

**Explain the problem. Make the mechanism clear. Let evidence support the claim.**

Author draft review, fair paper assessment, and evidence-based submission matching for English computer-systems research.

[![Version](https://img.shields.io/badge/skill-1.3.0-2563eb?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b?style=flat-square)](LICENSE)
[![Checks](https://github.com/Jinghao-coding/systems-paper-writing/actions/workflows/check.yml/badge.svg)](https://github.com/Jinghao-coding/systems-paper-writing/actions/workflows/check.yml)

**English** · [简体中文](README.zh-CN.md)

[Quick start](#quick-start) · [What it does](#what-it-does) · [Guides](#guides) · [Reference tools](#reference-tools)

</div>

## What it does

Three first-class tasks for English computer-systems research:

| Task | What you receive |
| --- | --- |
| **Author draft review** | Overall contribution assessment, located substantive issues, claim–design–evidence mapping, prioritized revision route, and requested replacement prose |
| **Other-paper review** | Neutral contribution summary, evidenced strengths and concerns, answerable questions, and a distinction between errors, missing evidence, and unclear explanation |
| **Conference matching and readiness** | A small sourced shortlist by year/track, research-fit rationale, current evidence risks, policy verification, and concrete preparation priorities |

Local English polishing, mechanism rewriting, evaluation analysis, related-work verification, journal extensions, figure review, and submission formatting remain separately selectable. A polish stays local; a paper review examines the research. Mechanisms, abstractions, protocols, measurements, deployment experience, cross-layer designs, and optimizations need different evidence.

Guides are English; communication follows your language and manuscript prose follows your request. Real submission advice checks current official policies and requested classifications. OSDI, SOSP, ASPLOS, EuroSys, PPoPP, and ATC are possible starting communities, not a universal ranking or a promise of suitability. See the [contribution-based venue guide](references/venue-guide.md).

## Quick start

### Install

Clone into one skill directory supported by your agent. For a fresh Codex installation:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-paper-writing.git ~/.agents/skills/systems-paper-writing
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Jinghao-coding/systems-paper-writing.git ~/.claude/skills/systems-paper-writing
```

If you already maintain the skill under `~/.codex/skills`, update that existing copy instead of creating a duplicate. Keep `SKILL.md` directly inside the skill folder and preserve its references. Start a new task or refresh skill discovery after installation.

### Use it

```text
Use $systems-paper-writing to review my first draft.
Assess whether its contribution, design and experiments support each other.
Locate the problems, distinguish research gaps from expression issues,
and provide a prioritized revision route. Do not edit files.
```

```text
Use $systems-paper-writing for a simulated review of this public paper.
Summarize its contribution accurately, give evidenced strengths and major
concerns, and ask answerable questions. Distinguish established errors from
insufficient material; do not presuppose rejection.
```

```text
Use $systems-paper-writing to recommend matching top conferences and tracks
from this paper's question, contribution type and available evidence.
Verify current official requirements. Explain fit, risks and preparation
priorities rather than sorting by conference prestige.
```

In Claude Code, invoke `/systems-paper-writing`. Smaller requests:

- “Polish only this paragraph; read adjacent definitions and preserve correct text.”
- “Rewrite this mechanism using its actual state, trigger, decision and execution.”
- “Compare conference and journal versions; distinguish new mechanisms from added explanation.”
- “Check these references and the original passages supporting this claim.”

### Example review output

> **Confirmed evidence conflict — abstract, design step 1, Table 1.** The abstract says all requests are accepted, but the algorithm rejects arrivals at capacity and the table completes 80 requests versus FIFO's 100. The two P99 values describe different populations. Correct the admission descriptions and report coverage alongside completed-request latency. Retaining an equal-service improvement claim requires a comparison with matched admission conditions. Closure: all claims and captions use the correct population and any equal-service benefit has corresponding evidence.

This excerpt comes from the [complete original teaching example](examples/author-review.md), with a minimal multi-file paper, an inactive old version, and an applicable revision patch. Full [other-paper](examples/other-review.md) and [venue matching](examples/venue-match.md) examples use the same manuscript. All data/policies are explicitly constructed and distributable.

## Guides

[SKILL.md](SKILL.md) routes each task to the relevant material.

| Topic | Guides |
| :--- | :--- |
| Author and other-paper review | [Review workflows](review-workflows.md) |
| Drafting and responses | [Writing playbook](references/writing-playbook.md) |
| Language and reader understanding | [Writing guidance](references/style-analysis.md) · [Edit examples](references/edit-catalog.md) |
| Structure, design, and evaluation | [Systems-paper patterns](references/systems-paper-patterns.md) |
| Figures and submission | [Figures and tables](references/figure-and-table-style.md) · [Submission preparation](references/submission-preparation.md) |
| Paper-based examples | [12 conference records](references/paper-analyses-conferences.md) · [6 agent preprints](references/paper-analyses-agents.md) · [10 journal records](references/paper-analyses-journals.md) |
| Literature and citation metadata | [Reference workflow](references/reference-workflow.md) |
| Sources and consolidation | [Corpus](references/paper-corpus.md) · [Provenance](references/provenance.md) · [Repository migration](references/repository-migration.md) |

The 28 records identify publication versions and source locations. Related conference/journal editions are one research family. The preprints are explicitly labeled. Examples inform reasoning; they do not supply facts for the user's paper.

## Reference tools

Optional helpers use **Python 3.10+ and the standard library**. Run these commands from the repository root:

```bash
# Offline search entry points
python3 scripts/reference_tools.py links --topic "GPU preemption" --venue OSDI

# Candidate metadata and authoritative DOI lookup
python3 scripts/reference_tools.py search --query "GPU preemption scheduling" --limit 5
python3 scripts/reference_tools.py lookup --doi 10.1145/945445.945450

# Retrieve BibTeX or compare supplied metadata
python3 scripts/reference_tools.py bibtex --doi 10.1145/945445.945450
python3 scripts/reference_tools.py verify --input papers.json
```

The helper prints JSON and leaves input files unchanged. Network commands send bibliographic queries or identifiers to public metadata services. Verification distinguishes agreement, conflicts, missing fields, and request failures; reading the paper establishes support for a manuscript claim. See the [input schema and statuses](references/reference-workflow.md).

Selected tools from `system-paper-skill` were consolidated here. Venue-ranking heuristics, guessed BibTeX fallbacks, bytecode caches, and obsolete outputs were removed. See [migration decisions](references/repository-migration.md).

## Development and updates

```bash
python3 scripts/check_package.py
python3 -m unittest discover -s tests
```

Behavioral and engineering tasks have [separate blind inputs and assessor answers](tests/behavior/README.md). Use `scripts/behavior_eval.py` to prepare current, previous, or no-skill arms and capture actual outputs. See the [validation record](validation/2026-10-05.md) for this revision.

For a Git installation, review local changes, then run `git pull --ff-only` in the skill repository. Keep institution-specific rules, manuscript facts, and private source material in the user's project.

## License and attribution

Distributed under [Apache-2.0](LICENSE), with the predecessor's [MIT notice](licenses/system-paper-skill-MIT.txt) retained for adapted portions. [NOTICE](NOTICE.md) and [provenance](references/provenance.md) identify sources. Original constructed manuscript fixtures are included under this license. Third-party full papers and private manuscripts remain outside this package.
