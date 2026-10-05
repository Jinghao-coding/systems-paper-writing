# English expression and local revision

Use the target passage and directly relevant context. For whole-paper diagnosis, use [review workflows](../review-workflows.md); for structure and research evidence, use [systems research](systems-paper-patterns.md). A local polish does not load the corpus or require network access.

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

For substantive findings and priority, use [review delivery](../review-workflows.md#make-important-findings-actionable). Keep editorial explanations outside replacement prose.

## Apply a source-informed language pass

Diagnose the sentence in its actual paragraph before rewriting:

- Identify what is already established and what the sentence adds. Replace a vague reference such as “this improves efficiency” with its actual antecedent and the supported effect; obtain the missing fact instead of guessing it.
- Separate a measured quantity from an interpretation. A throughput loss is not automatically the same percentage of CPU overhead. State the measured metric and report resource cost only when it was measured or validly derived.
- Preserve comparisons with a clear denominator. For an illustrative change from 100 ms to 80 ms, write “20% lower latency” or “1.25x speedup” according to the intended metric, not “25% lower latency.” These are arithmetic examples, not experimental results.
- Keep the scope of quantifiers, modifiers, and guarantees clear. In “the controller always selects a feasible placement,” establish the feasible-set and failure conditions before retaining “always.” Language refinement must not silently strengthen or weaken the guarantee.

Revise only the defects present in the passage. Keep established terms, correct clauses, and necessary conditions even when another source recommends a different stylistic preference.
