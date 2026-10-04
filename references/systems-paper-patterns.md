# Systems-paper patterns: from evidence to prose

These patterns synthesize the dated [conference](paper-analyses-conferences.md), [agent](paper-analyses-agents.md), and [journal](paper-analyses-journals.md) notes. Related publication versions form one research family. Choose a structure that explains the actual contribution.

## 1. Determine what the work changes

Explain where execution incurs a cost, what observation enables another approach, how the new decision or mechanism changes execution, and what evidence supports the effect.

| Research type | Useful argument | Examples |
| --- | --- | --- |
| Scheduling and sharing | Workload behavior and constraints → decision state → selection and execution → service or resource effects | XSched, REEF, Jiagu, CPS, SMetric, SANL |
| Elasticity and state movement | Blocking stages → reusable state or overlap → lifecycle/protocol → stage costs | BlitzScale, MITOSIS, PhoenixOS, DeltaBox, DrTM+B, Pragh |
| Caching and reuse | Repeated content and availability → placement/retrieval/invalidation → avoided work → application effects | UGache, KVCache, RhymeRL, MobiAgent, MOBIMEM |
| Interfaces and concurrency | Use case → objects and operation semantics → dependencies → implementation → costs and applications | Copier, FCP, CoAgent |
| Measurement | Missing distinctions → discriminating examples → representation and validation → analysis uses | VarCatcher, KVCache |

A paper may combine types. They identify explanatory needs rather than mandatory section titles.

## 2. Allocate information by purpose

**Abstract.** Locate the problem, identify the central mechanism and changed execution behavior, and report representative supported results. Component names help only when readers can attach meaning to them.

**Introduction.** Establish why a specific behavior incurs a cost, which assumption or decision in prior approaches is unsuitable under the stated conditions, and what opportunity the observation reveals. Contributions describe technical substance rather than an architecture inventory.

**Background and motivation.** Introduce only the objects, semantics, and behavior needed later. Use evidence or a concrete example to establish the problem. REEF's shared timeline and VarCatcher's paired counterexamples isolate differences more effectively than adjectives such as complex, dynamic, or heterogeneous.

**Design.** Establish overall execution relationships, then explain consequential decisions: state, triggers, operations, outputs, and semantics. A common path can precede exceptional paths, but correctness-critical cases remain part of the explanation.

**Implementation.** Explain how abstractions map to the environment and which engineering decisions affect feasibility, semantics, or cost. Centralize routine versions and configuration. State lifecycle, concurrency, and ownership are not automatically disposable detail.

**Evaluation.** Order evidence by dependency. A complete system may begin with end-to-end effects; a primitive such as Copier may establish its isolated behavior first. Measurement papers may devote substantial space to observations. Do not require equal-sized sections for ablation, sensitivity, overhead, and scalability.

**Related work and conclusion.** Organize comparisons by problem or mechanism, with explicit goals, assumptions, and operations. Conclusions identify supported lessons and effects rather than new results or an inflated application scope.

## 3. Make a design followable

For an important decision, identify the current state, trigger, reader of that state, selection or execution rule, and effect on the next step. These are semantic questions rather than a four-sentence template.

“Uses predictions” is insufficient when readers need to know whether the estimate concerns execution time, interference, or resource demand, and whether it filters, ranks, or allocates candidates. Explain the connection to the system objective at the level the contribution requires.

For protocols, explain visibility, ownership, prerequisites, and recovery after retry or rollback. Performance regularities do not replace guarantees. PhoenixOS connects time points to copying; CoAgent distinguishes framework notifications from agent repair.

A running example can connect mechanisms by showing the cost each removes and what remains. Wukong+G progresses from a graph to queries, patterns, and blocks; Pragh extends basic read-only migration with caching, updates, and reclamation. State whether a simplifying assumption is later removed or retained.

Separate offline sampling or training, online prediction, decisions, and updates. Report when and how often costs occur. A new model dimension needs an explanation of where the information comes from, how it affects a decision, and how computation or maintenance grows. UGache's per-GPU hotness also needs a dispatch policy; REEF's version selection introduces a search cost.

## 4. Write precise sentences and paragraphs

| Problem | Revision principle | Constructed example |
| --- | --- | --- |
| Abstract actor | Name the actor and decision | “The scheduler ranks candidate placements by predicted completion time.” |
| Nested nominalization | Restore actions and their relationship | “The predictor estimates execution time. The scheduler uses the estimates to compare placements.” |
| Vague coordination | Identify avoided or reused work | “The worker reuses the cached prefix and generates the remaining tokens.” |
| Mixed timing boundaries | Separate stages while retaining dependency | “The transfer continues in the background. Requests can start after the required layers arrive.” |
| Unexplained result | Explain the condition and supported cause | “The gain decreases as the cache grows, because more requests hit in both configurations.” |
| Rotating terminology | Keep distinct objects distinct | Session, request, and turn retain their defined meanings. |

These examples require corresponding evidence in the target work. A paragraph may start with a conclusion or an execution step depending on what the reader needs. Avoid repeated generic transitions when a specific unresolved cost or dependency can connect the paragraphs.

## 5. Add understanding beyond plotted numbers

Select trends that answer the research question. Separate measured behavior, causes supported by additional analysis, and plausible explanations. Do not turn an untested account into “because.”

Keep these distinctions explicit:

- Cache hit rate, reuse rate, and prediction quality are local metrics; connect them to transfer, model calls, placement, or completion time.
- Scaling time, application pause, checkpoint completion, and request latency have different timing boundaries.
- Mean latency, P99, and SLO-constrained throughput answer different questions.
- Reserved resources, actual occupancy, total resource-time, and peak capacity are different quantities.
- Agent action accuracy, partial completion, full success, and shared-state consistency are not interchangeable.

Explain a gain that shrinks, a stage that slows, or a curve that turns using relevant conditions and evidence. DrTM+B's hybrid copy can improve service during migration while extending total reconfiguration; Pragh's eager and deferred strategies can reach similar steady states at different times.

Specify time origins, sampling intervals, and key events. An average over a long interval can hide a short pause. Scaling can change memory capacity before exposing compute parallelism, as in Wukong+G; do not attribute all gains to core count.

For prediction, simulation, and approximation, relate local errors to actual choices when evidence permits. Average or extreme error alone does not show every decision is preserved. Separate host resources, target size, and execution mode.

Ensure implementation configurations support attribution. REEF's engine comparisons disable padding where source transformation is unavailable; UGache holds extraction constant when comparing placement. Small synthetic instances do not establish full-scale optimality bounds. A configuration called OPT is not automatically a global optimum.

Moving work off the critical path does not eliminate resource interference. Explain triggers, frequency, completion, and foreground impact. Whether preparation pays off depends on the reuse duration or count.

## 6. Coordinate figures and prose

Give each figure an explanatory role before choosing a form: architecture for responsibilities, timelines for execution, states for transitions, examples for decisions, and result plots for evaluation questions.

Captions identify objects, conditions, units, normalization, and necessary decoding information. Prose explains why the comparison matters and what the observations mean. See [figure guidance](figure-and-table-style.md).

## 7. Integrate journal extensions

Read both versions and the authors' extension statement. Identify whether an addition changes assumptions, mechanisms, implementation, evaluation, or explanation. Insert it where it is needed: motivation establishes the newly addressed problem, design changes the operation, implementation explains support, and evaluation tests the claim.

REEF extends recovery and kernel selection; UGache adds affinity-aware decisions and elaborates an existing refresh lifecycle; Jiagu connects GPU batching to scaling. These are different extension patterns, not a common page template.

A platform extension needs interface and execution-path differences. A new scenario may transfer only a policy rather than the entire system. Similar performance to a simple baseline can explain behavior, as in UGache's image-cache example.

Recheck abstracts, contribution counts, notation, captions, pseudocode, and evaluation scope. A more detailed description does not make a conference mechanism newly invented. Separate architectural applicability, implementation, and measured support.

## 8. Connect claims, choices, and evidence

Identify applications, workloads, environment, objective, and contribution. Performance papers specify metrics and baselines; protocol papers specify semantics and failure models; measurement papers specify observations and validation.

For a substantial review, use a compact mapping when helpful:

**Problem and conditions → consequential decision → evidence location → supported scope.**

Allow many-to-many relationships. Identify missing evidence without inventing experiments or expanding a polish into new research.

For important choices, discuss credible alternatives, comparison dimensions, benefits, costs, and applicability. Retrospective rationale must not become fictional development history. A cost model can justify a choice without implying that rejected alternatives were implemented or measured.

End-to-end comparisons establish overall effects; mechanism experiments explain decisions and conditions. An ablation that changes ordering guarantees, recovery, resource quotas, or interfaces needs a comparability check. Use a semantics-preserving alternative or controlled microbenchmark when appropriate. Interacting components' ablation differences are not additive contribution percentages.

Extract lessons about execution properties, assumptions, or trade-offs that determine applicability. Preserve the conditions of a single-case observation. Review novelty, actual implementation status, lessons, choices, context, focus, and presentation using the evidence appropriate to theoretical, prototype, measurement, or deployed work.

## 9. Practical refinement order

1. Read the abstract, introduction, design overview, and main evaluation to identify claims and evidence.
2. Identify each section's unique contribution and repeated challenge/component/contribution lists.
3. Follow key state and execution paths to locate explanatory gaps.
4. Check terms, metrics, comparisons, assumptions, and text–figure correspondence before sentence polishing.
5. Recheck the abstract, conclusion, captions, algorithms, formulas, and cross-references after edits.

Borrow reasoning methods from samples rather than their hardware, thresholds, guarantees, visual density, or editorial mistakes.
