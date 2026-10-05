# Three version-bound reading cases

This supplement deepens three existing corpus entries; it does not add new papers. Read only the relevant case. The 2026-10-05 pass re-read selected extracted passages from the archived reading versions. Earlier visual observations remain attributed to the 2026-09-28 notes; this pass makes no new layout judgments. [Version fingerprints](reading-versions.json) identify PDF bytes and the extracted text used. PDF page numbering can include a proceedings cover; section names and passage landmarks are the primary locators.

## Mechanism: REEF conference version

Family: REEF. Publication/read edition: OSDI 2022 conference PDF, [official paper page](https://www.usenix.org/conference/osdi22/presentation/han). The TOCS extension is a separate publication; its recovery changes must not be read into the conference design.

**Reader question.** If best-effort kernels are killed, how can execution safely continue, and what happens to work already buffered outside the device? This is a semantic prerequisite for understanding the latency claim.

**Located progression.** Section 3.2, “An Illustrative Example,” follows the same best-effort and real-time requests through normal mode, arrival, preemption, padding, and return to normal mode. Section 4, “Reset-based Preemption,” then connects idempotent kernels to re-execution without saving a GPU context. The following paragraph identifies launched kernels buffered in runtime queues, motivating the kernel-lifecycle explanation accompanying Fig. 7. The source's claim depends on DNN-kernel properties; it is not a guarantee for arbitrary stateful GPU code.

**Why an example before lower-level detail.** The request timeline supplies an event and a purpose for the subsequent queue-reset actions. Without it, the reader would have to infer why host queues, device queues, and running kernels all matter from an architecture inventory. The next layer answers an unresolved execution question instead of listing another component.

**Use in review.** Clue: a target paper says “instant preemption” without recovery semantics. Locate the kill/restart rule and buffered-work lifecycle. Judge only whether the supplied semantics justify the target operation; request the missing state and restart conditions. Transfer the explanation sequence, not REEF's idempotence, timing, hardware support, or measured benefits.

## Protocol and correctness: FCP journal version

Family: FCP. Publication/read edition: TPDS 27(12), 2016; [DOI](https://doi.org/10.1109/TPDS.2016.2539953). Exact reading bytes appear in the fingerprint record, distinct from any other downloaded PDF.

**Reader question.** Why can a cheap reader path coexist with safe writer progress when visibility is delayed, readers migrate, or readers sleep?

**Located progression.** Section 3.1 describes the synchronization issue; Section 3.2, “Basic Design,” explains the version/status relationship and the numbered happens-before dependencies associated with Fig. 2. It then identifies readers that do not re-enter or migrate, introduces messages/IPIs for stragglers, and addresses sleeping readers through passive/active transitions and a shared counter. The text explicitly discusses TSO conditions. Typical propagation behavior motivates the fast path; it is not the entire correctness argument.

**Why the dependencies and exceptional paths matter.** An empirical propagation time cannot prove safety across permitted executions. Version/status observations show what each party can infer; the subsequent cases explain how progress is recovered when ordinary observation stalls. The new state is introduced only after the reader sees the case that needs it.

**Use in review.** Clue: a target protocol uses a common-case timing argument as a universal guarantee. Locate the invariant, memory model, transition order, and exceptional-path handling. Ask for the missing guarantee argument if absent; do not call the protocol wrong solely because the exposition omits it. Transfer the progression from common case to required exceptional paths. Do not transfer TSO assumptions, IPI semantics, or cost measurements to another platform.

## Measurement and operational insight: KVCache Cache in the Wild

Family: KVCache characterization/policy study. Publication/read edition: ATC 2025 conference PDF, [official paper page](https://www.usenix.org/conference/atc25/presentation/wang-jiahao).

**Reader question.** Which observed reuse differences justify changing a cache policy, and why are familiar frequency/recency policies insufficient for these traces?

**Located progression.** Section 3 separates request categories and their reuse patterns. Section 4.1, “An overview of the design space,” first explains the existing cache mechanism and the two policy choices, then uses a same-time-since-access example with different turn counts to expose the limitation. Table 2 maps measured workload properties to policy choices. Section 4.2 contrasts the GDFS priority terms with the newly characterized reuse information and introduces the replacement priority calculation.

**Why a table and formula after the observations.** The mapping makes each policy decision traceable to a particular observation. The formula then defines how that information changes priority, rather than leaving “workload aware” as a label. This organization lets a reviewer distinguish an observed property, a design inference, and evaluation of the resulting policy. The mechanism discussion explicitly retains existing asynchronous swapping/loading; elaborating that mechanism is not a new contribution by itself.

**Use in review.** Clue: a target deployment paper generalizes one trace or attributes all benefit to a new policy. Locate sample definitions, category distributions, observation windows, and the evidence linking policy outputs to service metrics. Bound claims to observed categories; separate hit-rate changes from latency and consider alternative explanations. Transfer the observation-to-decision mapping, not production distributions, capacity recommendations, or causal claims across deployments.
