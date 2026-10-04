# Edits organized by problem

These examples are constructed for instruction. Apply an edit only when the source has the same technical meaning and conditions.

| Problem and original | Revision or action | Meaning to preserve |
| --- | --- | --- |
| “The predictor performs the estimation of execution time for the comparison of candidate placements by the scheduler.” | “The predictor estimates execution time. The scheduler uses these estimates to compare candidate placements.” | Distinct actors and actions; no new decision criterion. |
| “The scheduler intelligently coordinates jobs to improve resource efficiency.” | Verify the rule first. If supported: “The scheduler selects the configuration with the shortest predicted completion time.” | The more specific rule requires evidence; specificity cannot justify inventing an algorithm. |
| “The controller updates the queue to reflect newly arrived jobs. This update keeps the queue up to date with new arrivals.” | “The controller adds newly arrived jobs to the queue.” | This assumes updating means enqueueing only. Preserve reordering if it also occurs. |
| “Our system is not merely a static allocator; instead, it selects placements using predicted execution times.” | “Our system selects placements using predicted execution times.” | Describe a static baseline separately if its behavior is a relevant comparison. |
| “Suspending a queue stops new commands from launching; it does not cancel commands already running.” | Keep. | The negative clause defines operation semantics. |
| “The system significantly improves performance, demonstrating the effectiveness of our sophisticated design.” | Replace the vague result with the supplied metric, baseline, and conditions; remove the self-evaluation. | Do not invent numbers or causal explanations. |
| “The scheduler resumes the highest-priority ready queue.” | Keep. | Avoid nominalizing a clear action or adding irrelevant deployment qualifications. |

## Additional context-sensitive examples

- If only a cost model compares A and B, discuss the modeled trade-off. Do not write that the authors implemented and rejected B.
- If an ablation removes ordering guarantees, explain that both mechanism and semantics change. Do not label the entire performance difference as component overhead.
- A proof of linearizability under a stated failure model supports that guarantee. It does not establish higher throughput.
- A worker can be a process or a node. Use the project's definition when translating or refining the term.

Alternative wording is acceptable when it resolves the same issue and preserves meaning. A valid unchanged sentence is also a successful outcome.
