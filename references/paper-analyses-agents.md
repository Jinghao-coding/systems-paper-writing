# Agent-system analysis notes

Snapshot: 2026-09-28. The six [corpus](paper-corpus.md) entries are explicitly identified preprints, using the archived arXiv v1 versions. The notes preserve recorded organization, key-passage, and representative-figure analysis. Page numbers refer to those PDFs.

## 1. SMetric

The argument makes multi-turn sessions the scheduling unit: balance the first turn, reuse KVCache for subsequent requests, and define when to relax stickiness. Pages 7–8 compare balancing and reuse before presenting branch conditions. Keep session, turn, and request distinct. Page 10 separates SLO-constrained throughput from latency distributions; improvements need not hold for every tail metric.

Figs. 12–13 (p8) place stickiness measurements next to pseudocode. Figs. 15–17 (p10) combine throughput, tokens, local/global hits, and latency CDFs. Each strategy's heatmap uses its own P99 normalization, so cross-panel colors do not establish absolute load. Synchronize prose with pseudocode line numbers when revising. Explain behavioral changes between low and high load.

## 2. DeltaBox

Branching, retries, and rollback require restoring both filesystem and process-memory state. The design follows incremental state, coordination, and fast/slow restoration paths. Page 6 makes checkpoint/restore actors and stages explicit; p8 explains template hits; p13 separates operation blocking, fork resources, and trajectory time.

Figs. 2–3 (p6) connect state deltas to filesystem, process checkpoint, and coordinator roles. Figs. 6–7 and Tables 2–3 (p13) distinguish distributions, end-to-end overhead, event averages, and fan-out costs. Preserve the LLM-only baseline and absolute times. O(1) or hidden overhead claims apply to specific stages, not all execution. Consistency needs the actual freeze/copy/restore order.

## 3. CoAgent

A shared-environment conflict shows why locally executable actions need not compose correctly. The exposition defines order, access footprints, conflict handling, reads, reversible writes, and notifications, then reuses the example in evaluation. Section 5's properties have premises; Section 6 distinguishes the protocol from agent repair after notification.

Fig. 4 (p9) illustrates ToolSmith generation and invocation; Fig. 5 (p11) separates correctness, speed, and cost. Fig. 6 compares timelines for the same canary scenario using read/write, waiting, deadlock, notification, and repair markers. Borrow the conflict → semantics → protocol → matched-example organization. Do not turn conditional protocol guarantees into unconditional LLM repair success.

## 4. MobiAgent

Model capability, experience reuse, and evaluation serve mobile task execution. Section 4 defines ActTree nodes and edges through states, actions, and past tasks, then explains prefix merging, tracking, reuse, and model calls after misses. Section 6 separates task capability from acceleration; p13 distinguishes difficulty and request distributions.

Fig. 3 (p7) links tree merging to a small set of interface screenshots. Fig. 5 (p13) preserves application ordering across overall, easy, and hard conditions. Distinguish average completion score, complete success, and action reuse. Fewer calls, correct reuse decisions, and final success need separate evidence. Check dense legends at publication size.

## 5. MOBIMEM

Profile, Experience, and Action Memory handle personalization, execution knowledge, and action reuse, supported by OS services. Section 4 separates fixed control flow from variable parameters and explains templates, retrieval, and slot filling. Action caching distinguishes prefix from prefix/suffix reuse. Section 6 evaluates personalization, capability, efficiency, and scheduling separately.

Fig. 2 (p4) locates agent, memory, and OS responsibilities; an execution example is still needed to explain order. Fig. 5 (p6) contrasts ActTree and ActChain using a hotel task. Figs. 9–10 (p10) pair reuse with latency. Graph traversal is only part of retrieval cost; no LLM call does not mean zero cost. Keep memory objects and dependencies explicit without repeating a rigid challenge/insight/design template.

## 6. AgentRR

Recording, generalization, and replay form an experience lifecycle. Section 3.4 (p12) defines states, actions, transitions, and traces before explaining constrained action selection. Sections 4–5 connect traces, experience templates, check functions, and runtime execution. Page 16's high/low-level fallback helps explain semantic levels.

Fig. 4 (p15) connects the interface, two recordings, derived experience, and replay. Its full-page code/text density may require splitting for a two-column article. The reviewed version is primarily a proposal and case demonstration. Use it for state modeling and artifact flow rather than as evidence of general performance, reliability, or security. Conceptual definitions and executable guarantees remain distinct.
