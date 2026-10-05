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

## 4. Express the mechanism precisely

The [English expression guide](style-analysis.md) owns sentence-level revision. Here, assess whether the described actor, timing, ownership, state transition, and guarantee correspond to the actual mechanism. A stylistically smooth change that alters any of these is a technical regression.

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

## 9. Use the appropriate workflow

Use [review workflows](../review-workflows.md) for diagnosis and [writing playbook](writing-playbook.md) for actual revisions. Borrow reasoning methods from samples, not their hardware, thresholds, guarantees, or measured effects.

## 10. Research-type review paths

Select paths activated by the paper's claims. Each example below is constructed; it illustrates an inspection sequence rather than reporting a real system result. Retain necessary conditions, negative outcomes, and benefit-disappearance cases. These paths do not prescribe experiment counts.

### Scheduling, sharing, and cluster resources

Inspect the scheduled object, available decision-time information, budget, queue/execution boundary, preemption/recovery cost, service constraints, and fairness. **Clue:** a scheduler uses actual completion time to rank waiting jobs. **Locate:** prediction inputs and timestamped trace fields, decision pseudocode, and evaluation replay configuration. **Support:** an oracle replay can bound achievable behavior but cannot establish an online scheduler's benefit. **Opinion:** identify the oracle explicitly or evaluate estimates available at dispatch; include recovery costs if preemption contributes to the claim. Close the issue when both the decision inputs and measured interval match the online claim.

### LLM training and inference

Inspect workload distribution, admission, failures, quality constraints, latency/throughput definitions, cache/warm-up state, and offline versus online costs. **Clue:** A has lower P99 than B. **Locate:** accepted/rejected counts, metric population, timeout handling, and arrival-to-completion boundaries. **Support:** A rejects 20% while B admits all, so completed-request P99 describes different populations. **Opinion:** report acceptance and failure rates with latency; compare under a shared service objective or narrow the claim. Do not silently impute finite latency to rejected requests. A low-load result with no benefit remains informative. For training, check convergence/quality and total training work before calling step-throughput gains a training speedup.

### Predictors and learned decisions

Inspect split unit/time, target-environment calibration, distribution changes, information leakage, inference/update costs, and the decision consequences of errors. **Clue:** random rows from the same execution appear in train and test. **Locate:** split keys, fitting timestamps, preprocessing state, ranking or placement code, and held-out outcomes. **Support:** row-level accuracy does not establish generalization to unseen jobs or machines. **Opinion:** re-split at the claimed generalization unit and connect errors to actual decisions/end-to-end cost. If the claim is only in-environment calibration, preserve that narrower result rather than inventing an unseen-device requirement.

### Protocols, storage, and concurrency

Inspect operation semantics, fault model, invariants, concurrent transitions, recovery, and whether guarantees come from proof, model checking, or finite tests. **Clue:** a crash test is described as proving exactly-once effects. **Locate:** commit/ack ordering, durable state, retry IDs, external side effects, and proof assumptions. **Support:** passing sampled failures does not establish all executions; missing explanation does not itself refute the protocol. **Opinion:** ask how atomicity and recovery preserve the invariant and distinguish the theorem's domain from test coverage. Preserve a correct single-writer design if the paper explicitly restricts its scope to one writer.

### Measurement and deployment experience

Inspect sample source, representativeness, observation window, missing samples, alternative explanations, correlation/causation, and transfer conditions. **Clue:** one region improves after a cache rollout. **Locate:** sampling, before/after workload mix, simultaneous changes, cache metrics, and latency distributions. **Support:** temporal association alone cannot identify the cache as the cause. **Opinion:** analyze matched periods/groups if available, or report a bounded observational result. A deployment lesson need not invent a new algorithm; explain which environmental condition makes the lesson transferable.

### Agent systems

Inspect boundaries among model inference, tool actions, environment state, task success, local action accuracy, retries/recovery, and cache/experience reuse validity. **Clue:** fewer model calls is called improved reliability. **Locate:** task-level success, tool errors, retry budgets, external state versions, invalidation and rollback semantics. **Support:** action accuracy or call reduction can coexist with worse task completion. **Opinion:** separate these outcomes, account for retry cost, and check reuse preconditions. If a cached plan is validated against an unchanged environment, do not demand universal validity after arbitrary state changes; require invalidation only within the claimed operating conditions.
