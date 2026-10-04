# Systems-paper writing playbook

Use this guide directly with the manuscript and supplied research materials. It contains the extracted methods and their context-sensitive application; no external reading is required to apply them. Source attribution is kept separately in [writing sources](writing-sources.md). The procedures and examples below are this skill's synthesis, not quotations or mandatory conference templates.

## 1. Recover the argument before editing

Identify the application, execution environment, problem, changed decision or mechanism, and available evidence. Use the manuscript's terms. For a paragraph edit, recover only the context that affects that paragraph; a whole-paper assessment needs the broader argument.

Write a private one-sentence statement of what the work establishes. If it reduces to a system name or a list of modules, identify what the reader learns from the modules' behavior. If an element is missing, inspect adjacent text, algorithms, figures, or project evidence. Keep an unresolved scientific question outside the replacement prose.

Choose the contribution type before judging adequacy:

| Contribution | Explain | Relevant support |
| --- | --- | --- |
| Mechanism or abstraction | The changed operation, semantics, and reason it addresses the problem | Implementation, correctness argument, and experiments appropriate to the claim |
| Measurement or analytical insight | The question, sampling/model assumptions, observation, and interpretation | Traceable data, validation, uncertainty, and competing explanations |
| Operational experience | The real constraints, consequential decisions, and lessons transferable to other settings | Deployment observations and clearly delimited experience |
| Cross-layer design | What information or control crosses the boundary and why it matters | Interface behavior and costs on each affected side |

A language revision preserves the established contribution. It does not add a novel algorithm to an experience paper or turn a local measurement into a general guarantee.

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

## 4. Revise language with its technical context

Use the paragraph's role to determine what each sentence must contribute. Resolve meaning before shortening. A clear sentence identifies an actor or topic, its main action, and necessary conditions. Keep the subject near the verb when intervening detail obscures the action.

| Symptom | Contextual diagnosis and revision |
| --- | --- |
| “This reduces its cost.” | Resolve both referents from nearby text. Name the relevant operation and measured cost if multiple candidates exist. |
| A chain of abstract nouns | Recover the actual actor and verb; preserve distinct actions instead of replacing them with an invented umbrella term. |
| “Therefore” after two observations | Check the inference. Explain the missing causal/conditional link if supported; otherwise report the observations without claiming causality. |
| Parallel items mix mechanisms, goals, and outcomes | Reorganize by the relationship the sentence intends to express; do not rename items merely to make their grammar match. |
| A modifier changes the guarantee | Determine which noun or action it qualifies. Preserve “all,” “only,” “at most,” and failure conditions according to the source semantics. |
| Several spellings or synonyms for one object | Use the defined technical name, even when it repeats. Different names may signify different objects. |
| Each sentence is short but the paragraph feels disconnected | Restore the relevant cause, contrast, or execution sequence rather than adding generic transition words. |

**Constructed example.** “The worker sends the request to the coordinator after it releases the lock.” The referent of “it” affects synchronization. If the worker releases the lock first, write: “After releasing the lock, the worker sends the request to the coordinator.” If the source does not identify the lock owner, raise that technical question before choosing the sentence.

Do not impose active voice everywhere, a vocabulary blacklist, a fixed sentence length, or one opening pattern. Preserve correct passages; the completion criterion is resolved ambiguity or improved reasoning, not the number of changed words.

## 5. Explain what experiments establish

Locate the research question, comparison, metric, and result before drafting an evaluation paragraph. State the observation that matters, then relate it to the question. Use a mechanism explanation only when the evidence supports it; distinguish a plausible cause from a measured cause.

For an evaluation review, inspect whether workloads cover the claimed operating conditions, baselines receive comparable configuration effort, and resource accounting includes the relevant costs. Keep component effects distinct from application effects. Check whether removing a component also changes semantics or the available resources. Separate calibration from evaluation when judging predictive generalization.

Use the actual metric and denominator. Report absolute quantities when ratios hide practical meaning. Choose aggregation and uncertainty methods according to what is estimated and how observations were collected. Preserve adverse results and conditions where a benefit disappears. These are questions for evaluating evidence, not permission to fabricate missing experiments during prose editing.

**Constructed arithmetic example.** A CPU-bound service processes 100 requests/s at 50% CPU utilization in one configuration and 90 requests/s at 60% in another. Throughput falls by 10%. Assuming the same CPU capacity and accounting interval, CPU time per request rises by `(0.60 / 90) / (0.50 / 100) - 1`, approximately 33.3%. Calling this “10% CPU overhead” confuses two metrics. In a manuscript, use the measured quantities and disclose the derivation if needed.

A useful result paragraph adds an interpretation, a relevant condition, or an explanation beyond the plotted values. Its opening, closing, and caption need not repeat the same conclusion verbatim.

## 6. Produce actionable reviews and responses

For a review, first reconstruct the author's claim neutrally. Locate the passage or evidence causing the concern. Distinguish an established error, an unclear explanation, and an unanswered scientific question. State the consequence and the smallest useful correction. Do not infer that unfamiliar design choices are wrong.

For a response, address the actual reviewer concern using available evidence and identify the resulting revision. Keep proposed experiments distinct from completed ones. Preserve this factual distinction in both the response and manuscript, while removing reviewer dialogue from the manuscript itself.

**Constructed example.** Concern: the placement decision seems to omit transfer cost. If the model already includes it, point to the actual term and clarify its definition in the text. If it is absent, determine the consequence and describe the correction or open question. Do not answer by asserting that the design is “comprehensive.”

## 7. Connect artifacts to claims

When artifact preparation is requested, identify which important claim each experiment reproduces and record its input, command, environment, expected output, and supported variation. State special hardware requirements and distinguish a quick functionality check from the full measurement. Prepare these mappings while the experiments are still understood.

For example, an inference demonstration on a single GPU can show that a program executes; reproducing a multi-node scaling figure requires the corresponding configuration and measurement. Describe the actual supported experiment rather than treating any successful run as reproduction of the paper.

Use a released artifact identifier when available and keep the link between code revision, configuration, outputs, and paper figures traceable. Current artifact submission rules are a separate, year-specific lookup.

## 8. Finish within the requested scope

Return usable replacement text for an edit. Provide located findings for a review. Keep unresolved facts and proposed research outside manuscript prose. Check that the revision preserves terminology, evidence strength, conditions, references, and technical semantics.

Apply this playbook directly. External source pages are not prerequisites for writing or polishing. Network lookup is appropriate for requested new literature, citation verification, actual current venue rules, or an explicit source update. If the user requests an offline task, keep it offline and identify any dynamic fact that remains to be verified.
