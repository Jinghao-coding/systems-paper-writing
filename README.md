<div align="center">

# Systems Paper Writing

**Explain the problem. Make the mechanism clear. Let evidence support the claim.**

An English writing skill for computer-systems research targeting CCF A conferences and journals.

[![Version](https://img.shields.io/badge/skill-1.1.0-2563eb?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b?style=flat-square)](LICENSE)
[![Checks](https://github.com/Jinghao-coding/systems-paper-writing/actions/workflows/check.yml/badge.svg)](https://github.com/Jinghao-coding/systems-paper-writing/actions/workflows/check.yml)

**English** · [简体中文](README.zh-CN.md)

[Quick start](#quick-start) · [What it does](#what-it-does) · [Guides](#guides) · [Reference tools](#reference-tools)

</div>

## What it does

Turn research materials into a focused argument, explain consequential design choices, refine technical prose, and connect experiments to claims. The skill covers scheduling, GPU sharing, cluster management, AI infrastructure, and agent systems, including journal extensions.

| Task | Result |
| :--- | :--- |
| Organize a paper | A problem-driven outline with clear section roles and evidence dependencies |
| Draft or refine a mechanism | Concrete objects, states, decisions, execution effects, and necessary conditions |
| Review an argument | Located issues with evidence, consequences, and completion criteria |
| Explain experiments | Accurate comparisons and interpretations that add understanding beyond plotted numbers |
| Extend a conference paper | Consistent motivation, design, implementation, and evaluation for the added contribution |
| Find and check references | Search entry points, candidate metadata, DOI lookup, retrieved BibTeX, and field-level checks |

Instructions and reference guides are in English. Communicate in the user's requested language; provide manuscript text in the requested language. CCF A is the target audience and venue preference, not a mandatory paper template. Current venue rules are checked for submission tasks.

## Recommended research communities

Start with **OSDI, SOSP, ASPLOS, EuroSys, and ATC**, then expand according to the contribution: **NSDI / SIGCOMM** for networked systems, **FAST** for storage, **ISCA / MICRO / HPCA** for architecture, **PPoPP / PLDI / SC** for parallel execution and systems software, **SIGMETRICS** for performance, **SIGMOD / VLDB / ICDE** for data systems, and **MLSys** for ML infrastructure. Specialist communities and workshops are included in the [11-area venue guide](references/venue-guide.md).

The guide separates reading recommendations from submission selection and records official entry points. The [writing-resource guide](references/writing-resources.md) connects classic advice, researcher blogs, current author guidance, and artifact experience to concrete revision actions.

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
Use $systems-paper-writing to refine the design section.
Read the adjacent paragraphs and algorithm first. Preserve technical meaning,
explain the state and decision flow, and return replacement prose.
Separate any scientific correction from optional language changes.
```

In Claude Code, invoke `/systems-paper-writing`.

Other useful requests:

- “Review whether the introduction's claims are supported by the design and evaluation. Do not edit files.”
- “Reorganize this evaluation around its research questions, retaining all metric definitions and comparison conditions.”
- “Compare the conference and journal drafts. Identify new mechanisms, explanation, and evidence, then revise the contribution statements.”
- “Check the references supporting this paragraph, including the version and author order.”

## Guides

[SKILL.md](SKILL.md) routes each task to the relevant material.

| Topic | Guides |
| :--- | :--- |
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

For a Git installation, review local changes, then run `git pull --ff-only` in the skill repository. Keep institution-specific rules, manuscript facts, and private source material in the user's project.

## License and attribution

Distributed under [Apache-2.0](LICENSE), with the predecessor's [MIT notice](licenses/system-paper-skill-MIT.txt) retained for adapted portions. [NOTICE](NOTICE.md) and [provenance](references/provenance.md) identify sources. Full papers and private manuscript revisions are outside this package.
