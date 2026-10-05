# Systems-paper writing playbook

Use this guide directly with the manuscript and supplied research materials. It contains the extracted methods and their context-sensitive application; no external reading is required to apply them. Source attribution is kept separately in [writing sources](writing-sources.md). The procedures and examples below are this skill's synthesis, not quotations or mandatory conference templates.

## 1. Establish the editing scope

Confirm the target, adopted version, active files, current contents, and requested output before editing. Read only the context affecting the passage. For substantial restructuring, recover the argument using the [review workflow](../review-workflows.md#recover-the-actual-argument), and select contribution-specific criteria in [systems research](systems-paper-patterns.md). Review-only requests use that workflow without modifying files.

Draft from established facts. Re-read the affected files before writing and reconcile intervening edits. Reuse the project's existing source/version and terminology records where useful; keep editorial questions outside manuscript prose.

## 2. Make motivation lead to the technical idea

Give the reader enough concrete context to understand why the existing execution path causes a problem. Identify the affected work, the limiting condition, and its consequence. Then explain the observation that enables the proposed change. Use related work to compare the relevant behavior and assumptions.

Check whether the reader can recover the problem's importance, the relevant limitation, the technical idea, and the supported outcome. These are content needs, not four compulsory paragraphs. Keep background only when it prepares a later claim. Replace a component inventory with an explanation of the consequential decision.

For an abstract, make the main action understandable without concepts defined later. Select results that represent the contribution and include the comparison needed to interpret them. After revising the body, reconcile the abstract and introduction with what the paper actually establishes.

**Constructed example.** Supplied facts: a queue lets a long job delay short jobs; the new policy uses supplied duration estimates; no performance results are available.

Weak: “We introduce a sophisticated prediction, scheduling, and execution framework.”

Revision: “When a long job occupies the head of the queue, short jobs wait behind it. The scheduler uses estimated job durations to order the queued work.”

The revision exposes the action without asserting a measured latency benefit, starvation protection, or preemption behavior that the supplied facts do not establish.

## 3. Explain design through decisions and execution

Define the managed object and the operations available on it. Follow one relevant event through the state it reads, the choice it makes, and the state or execution it changes. Describe ordering, ownership, failure handling, or concurrency where the operation's meaning depends on them. Put an unfamiliar concept into use before introducing several variants.

For a consequential design choice, explain the feasible alternatives, the constraint distinguishing them, and the cost of the chosen option. A comparison based on analysis must remain an analytical comparison; only recorded implementation experience supports a claim that an alternative was tried and rejected.

Separate a general design from the prototype that exercises it. State an implementation restriction where it affects a claim. Use an architecture figure for relationships and an execution example for state changes; explain the decision that the visual helps the reader understand.

In an industrial project, isolate the paper's technical contribution from the surrounding engineering effort. Describe project history only when the sequence itself supplies evidence for a lesson.

**Constructed example.** Evidence shows a controller computes placements, while workers apply them on their next poll.

Ambiguous: “The controller updates workers immediately.”

Revision: “The controller records the new placements. Each worker applies its assigned placement at its next poll.”

This resolves the control/execution boundary without inventing an immediate notification mechanism.

## 4. Revise language in context

Apply the [English expression guide](style-analysis.md) to the target paragraph. It owns sentence structure, referents, information flow, compression, and preservation decisions. Use the [edit catalog](edit-catalog.md) only when an example clarifies a concrete revision. Resolve ambiguity without inventing the missing mechanism.

## 5. Turn evidence into evaluation prose

Locate the research question, comparison, metric, and result before writing. State the relevant observation and explain its implications within the supported conditions. [Systems research](systems-paper-patterns.md#5-add-understanding-beyond-plotted-numbers) owns metric boundaries, ablation comparability, and local versus end-to-end effects.

**Constructed arithmetic example.** A service processes 100 requests/s at 50% CPU utilization in one configuration and 90 requests/s at 60% in another. Throughput falls by 10%. With the same CPU capacity and interval, CPU time per request rises by `(0.60 / 90) / (0.50 / 100) - 1`, about 33.3%. Calling this “10% CPU overhead” confuses metrics. State the measured quantities and label any derivation.

## 6. Respond to an actual reviewer concern

Reviews use the [dedicated workflows](../review-workflows.md). For a response, state the concern, evidence answering it, and resulting manuscript change. Distinguish proposed from completed experiments and keep reviewer dialogue outside the manuscript.

For example, if a reviewer believes placement omits transfer cost, locate the actual cost term and clarify it if present. If absent, assess the consequence and describe the correction or unresolved question. Do not invent a term to answer the concern.

## 7. Connect artifacts to claims

When artifact preparation is requested, identify which important claim each experiment reproduces and record its input, command, environment, expected output, and supported variation. State special hardware requirements and distinguish a quick functionality check from the full measurement. Prepare these mappings while the experiments are still understood.

For example, an inference demonstration on a single GPU can show that a program executes; reproducing a multi-node scaling figure requires the corresponding configuration and measurement. Describe the actual supported experiment rather than treating any successful run as reproduction of the paper.

Use a released artifact identifier when available and keep the link between code revision, configuration, outputs, and paper figures traceable. Current artifact submission rules are a separate, year-specific lookup.

## 8. Finish within the requested scope

Return usable replacement text for an edit. Provide located findings for a review. Keep unresolved facts and proposed research outside manuscript prose. Check that the revision preserves terminology, evidence strength, conditions, references, and technical semantics.

Apply this playbook directly. External source pages are not prerequisites for writing or polishing. Network lookup is appropriate for requested new literature, citation verification, actual current venue rules, or an explicit source update. If the user requests an offline task, keep it offline and identify any dynamic fact that remains to be verified.
