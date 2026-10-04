---
name: systems-paper-writing
description: Draft, organize, review, and refine English computer-systems research papers targeting CCF A conferences and journals. Covers scheduling, GPU sharing, cluster management, AI infrastructure, and agent systems, including journal extensions. Use for mechanism explanations, technical arguments, evaluation narratives, and submission preparation; verify current venue requirements when needed.
license: Apache-2.0
metadata:
  version: "1.0.0"
  language: en
---

# Systems Paper Writing

Explain the problem, design, and results through concrete facts and execution behavior. Preserve scientific meaning, experimental scope, and claim strength. Keep prose that already works.

## Select the task and reading scope

- **Review:** report located problems without editing files. Distinguish required corrections, optional simplification, and technical questions. Combine repeated issues and give a concrete completion criterion.
- **Refine:** resolve ambiguity and broken reasoning before removing repetition and correcting grammar. Preserve formulas, terminology, baselines, units, and aggregation.
- **Draft or extend:** determine each passage's role from available research materials. Obtain missing evidence rather than inventing facts. Ask only when missing information changes the substantive decision.
- Deliver usable manuscript text first when requested. Keep editorial explanations outside the manuscript. For bilingual output, provide a complete translation rather than a summary.
- Follow the user's requested communication language; English is the default manuscript language. Chinese dissertation integration and university-specific thesis rules belong to `cs-phd-writing` when that skill is available.

Read the relevant parts of [writing guidance](references/style-analysis.md). For examples, use the [edit catalog](references/edit-catalog.md). For paper organization, mechanisms, or evaluation, use [systems-paper patterns](references/systems-paper-patterns.md); for figures, use [figure and table guidance](references/figure-and-table-style.md). Read [conference](references/paper-analyses-conferences.md), [agent](references/paper-analyses-agents.md), or [journal](references/paper-analyses-journals.md) notes only when a concrete example helps. Use [submission preparation](references/submission-preparation.md) for submission tasks and [provenance](references/provenance.md) for source tracing.

For related-work discovery, DOI metadata, or BibTeX import, use the optional [reference workflow](references/reference-workflow.md). Ordinary prose edits do not require network lookup.

## Core decisions

1. **Establish the concrete problem.** Identify the workload, resource or execution stage, constraint, and consequence. Background should locate the problem.
2. **Let observations explain design.** Show which property makes an operation possible or useful. Avoid restating the same component list as challenges, insights, and contributions.
3. **Describe mechanisms as actions.** Explain who reads which state, under what conditions, makes what decision, and changes which execution behavior. Define objects and semantics before implementation details.
4. **Advance one argument per paragraph.** Connect sentences through causal, conditional, sequential, or comparative relationships. Split overloaded sentences without creating disconnected fragments.
5. **Explain differences in results.** Identify important trends and conditions. Separate local metrics from end-to-end effects and measurements from proposed explanations.
6. **Keep terms precise.** Use concrete subjects and verbs. Do not rotate job, task, request, model, instance, latency, and throughput as stylistic synonyms.
7. **Match confidence to evidence.** State supported results directly. Preserve uncertainty where evidence warrants it; do not turn an untested explanation into causality.
8. **Remove unnecessary defensive prose.** Keep real assumptions, semantic boundaries, and relevant conditions where they matter. Omit imagined objections and editing history from the manuscript.
9. **Diagnose meaning, not an “AI vocabulary.”** Evaluate whether wording contributes facts, mechanisms, relationships, or evidence. Preserve terms with technical or statistical meanings.
10. **Respect editing scope.** Language refinement does not authorize new experiments or research claims. Investigate contradictions in existing materials and identify unresolved factual questions separately.

## Organize around the research

Use state, choice, and execution for scheduling; blocking stages and state lifecycles for elasticity and recovery; repeated work and reuse decisions for caching; operation semantics for protocols; and validated observations for measurement papers. Combine these as needed rather than imposing a universal outline.

For a whole-paper review, connect the problem and its conditions to consequential design decisions, evidence locations, and supported scope. This relationship can be many-to-many. A contribution may concern performance, correctness, interfaces, or measurement; it need not claim universal superiority.

Explain credible alternatives when they reveal an important trade-off. Distinguish evidence-based retrospective reasoning from actual development history. Never invent experiments with rejected alternatives. Check whether an ablation preserves semantics and resource conditions before attributing its performance difference to a component.

Separate offline preparation, online decisions, updates, and their costs. Choose evaluation order according to evidence dependencies. Explain how local effects influence system objectives and where benefits diminish or costs increase.

For a journal extension, identify added mechanisms, operating conditions, implementation, evaluation, or explanation by comparing the relevant versions. Update motivation, design, implementation, experiments, and contributions consistently.

## Use the paper corpus

The [corpus](references/paper-corpus.md) contains 28 dated version records: 12 conference papers, 10 journal papers, and six explicitly identified agent preprints. Related conference and journal versions form one research family. Prefer relevant formally published CCF A work when expanding the corpus; user-specified sources may be included with their publication status recorded. Verify classification and publication metadata when they affect selection.

Record source version and section or figure locations. Inspect PDF pages before inferring visual style. Analyze organization, reasoning, language, evaluation, and text–figure relationships. Do not transfer a sample's mechanisms, numbers, assumptions, or hardware into the target paper as facts.

## Consistency and delivery

- Keep contributions, design, and evaluation aligned with the same question. Introduce concepts before substantive use and preserve terminology afterward.
- Distinguish useful recurrence from repetition: the abstract summarizes, the introduction motivates, the design explains execution, the evaluation tests and interprets, and the conclusion extracts supported lessons.
- Centralize shared configurations and assumptions; repeat them when a local comparison requires them.
- Let research determine paragraph length, contribution count, voice, and figures. Verify current official requirements for page limits, anonymity, templates, and disclosure.
- Write the revised paper for a first-time reader and the response letter for the actual reviewer question. Keep their facts consistent and their voices distinct.
- Before delivery, check numbers, units, conditions, baselines, aggregation, causality, and claim strength. Preserve or consistently update LaTeX macros, labels, citation keys, and cross-references. Run the project's relevant checks when editing structure or formatting.
