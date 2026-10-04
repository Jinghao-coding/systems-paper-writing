# Writing guidance

## Abstract: make the problem and technical action recognizable

Provide enough context to locate the work, then identify the specific obstacle. Introduce what the system changes in a decision or execution path before listing component names. Give representative results with metrics, comparison targets, and necessary conditions. Avoid packing implementation, hardware, every result, and every qualification into one sentence.

Use the space the argument needs. There is no mandatory sentence count, three-component structure, or generic impact sentence. Expand unfamiliar abbreviations or use their full forms. Qualify a statement when its subject or quantifier exceeds the evidence, rather than attaching caution to every sentence.

## Introduction and motivation: explain why existing behavior causes a problem

Trace a concrete path: who submits work, how resources are allocated, when waiting occurs, which stage becomes a bottleneck, and which objective suffers. Support the important links with measurements, examples, or literature. Distinguish evidence of severity from evidence explaining the cause.

Compare specific operations and trade-offs under shared conditions. Waiting for execution to finish and reserving resources affect different objectives. Avoid saying that all existing systems fail.

Connect the observed property to an available operation and the bottleneck it addresses. Labels such as Observation or Insight are optional. The number of mechanisms and contributions follows the research.

## Design: explain an executable mechanism

- **Abstraction:** define managed objects, operations, and semantics. Distinguish policy and mechanism when that distinction helps explain the work.
- **Execution:** follow a request, job, or control event through its trigger, observed state, rule, output, and subsequent action. Explain concurrency, recovery, and dependencies where correctness depends on them.
- **Rationale:** identify the observation supporting the choice and where its cost occurs. Discuss alternatives when they clarify a real trade-off.
- **Examples:** use architecture diagrams for relationships and timelines for behavior. A running example can connect motivation and design without narrating every box.
- **Equations:** introduce variables and units, explain the resulting decision, and state how execution uses it. Do more than restate the notation verbally.

Prefer the actual actor: scheduler, controller, runtime, or worker. Passive voice is appropriate when the affected object matters more than the actor.

## Evaluation: answer questions with evidence

Identify the claim an experiment supports. Describe the configuration, baseline, and metric needed to interpret it, then explain the important trend or turning point using supported mechanisms.

When gains vary with load, scale, or granularity, examine competition, waiting, transfer, or scheduling costs. If the cause is uncertain, identify it as a possible explanation or report the observation alone. Avoid generic declarations that the design is effective.

Connect end-to-end effects, mechanism contributions, and overheads where evidence permits. Keep common setup in one place and local differences near the comparison. Preserve averages versus maxima, percentage reductions versus percentage points, and reductions versus speedups.

A language-editing task checks the expression of existing evidence. Additional baselines, sensitivity studies, and generalization experiments are research recommendations rather than prerequisites for completing a polish.

## Scheduling, clusters, and agents

Distinguish scheduling objects, resources, objectives, triggers, decision granularity, and execution granularity. Explain waiting, preemption, recovery, or colocation rather than relying on “adaptive” or “intelligent.”

Locate cluster costs in control, transfer, loading, or execution. Explain how a changed stage affects completion, resource use, or elasticity. A faster stage alone does not establish a faster application.

For agents, separate model inference, tool actions, environment state, and reusable records. Explain stored content, selection conditions, checkpoints, and failure handling from actual design evidence. Reliability, validation, and reduced calls require distinct support.

## Reader prerequisites and information flow

Ask what the reader already knows, what this paragraph adds, and what the next claim requires. Give a new concept enough meaning at first substantive use; a detailed definition may follow. Abstracts must be understandable without terminology defined later in the paper.

For section restructuring, reverse-outline each paragraph's claim, evidence, and role. Repair unexplained subject changes, variants introduced before basic behavior, and jumps from local observations to system conclusions. Do not use “therefore” to hide a missing inference.

Keep technical names stable. Continuity does not require identical sentence openings. Use a concrete completion criterion, such as making state ownership unambiguous. Stop once the issue is resolved; do not rotate accepted wording between iterations.

## Compression and natural sentences

Identify a paragraph's purpose before shortening it. Merge repeated claims, while preserving new evidence, conditions, and execution details. Remove transitions that merely announce an important mechanism.

Keep subjects, actions, and conditions clear. Reduce unnecessary nominalization and nested noun phrases. Ensure parallel items share a conceptual level and pronouns have recoverable referents. Causal connectors require causal support.

Do not mechanically delete academic words, replace technical terms with synonyms, split every long sentence, or convert all passive voice. Two adjectives may describe different properties. Determine correctness from execution and allocation semantics, not superficial patterns.

## Direct statements and review feedback

Remove imagined rebuttals, repeated scope disclaimers, and editing history. Retain contrasts that define an interface, guarantee, or research object. State conditions where they affect understanding rather than repeating them after every result.

Review categories:

- **Required correction:** grammar error, ambiguity, contradiction, wrong measurement scope, or a broken argument.
- **Optional refinement:** already clear prose that could be shorter or more connected.
- **Technical question:** a missing fact that existing materials cannot resolve.

For a substantial issue, provide its location, effect, evidence, and a practical correction or completion criterion. Keep editorial explanations outside the replacement text.

## Apply a source-informed language pass

Use the [writing resources](writing-playbook.md) for the reasoning behind these checks. Diagnose the sentence in its actual paragraph before rewriting:

- Identify what is already established and what the sentence adds. Replace a vague reference such as “this improves efficiency” with its actual antecedent and the supported effect; obtain the missing fact instead of guessing it.
- Separate a measured quantity from an interpretation. A throughput loss is not automatically the same percentage of CPU overhead. State the measured metric and report resource cost only when it was measured or validly derived.
- Preserve comparisons with a clear denominator. For an illustrative change from 100 ms to 80 ms, write “20% lower latency” or “1.25x speedup” according to the intended metric, not “25% lower latency.” These are arithmetic examples, not experimental results.
- Keep the scope of quantifiers, modifiers, and guarantees clear. In “the controller always selects a feasible placement,” establish the feasible-set and failure conditions before retaining “always.” Language refinement must not silently strengthen or weaken the guarantee.

Revise only the defects present in the passage. Keep established terms, correct clauses, and necessary conditions even when another source recommends a different stylistic preference.
