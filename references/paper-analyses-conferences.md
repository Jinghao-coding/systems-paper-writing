# Conference-paper analysis notes

Source-analysis snapshot: 2026-09-28. These English notes preserve recorded organization, key-passage, and representative-page observations. Locations refer to the reviewed PDF versions; RhymeRL locations refer to arXiv v1. Publication links are in the [corpus](paper-corpus.md).

## 1. XSched — OSDI 2025

The argument moves from differing accelerator preemption capabilities to the XQueue abstraction, then explains how hardware affects implementation and performance. Sections 1–3 define schedulable objects and submit/wait/suspend/resume operations before support levels. Sections 7.3–7.4 relate outcomes to preemption granularity and command duration. Keep interface promises, backend behavior, and policy decisions distinct.

Fig. 1 (p3) aligns CPU threads and XQueues to explain the abstraction and scheduling point. Fig. 9 (p12) aligns foreground latency distributions with foreground/background throughput across devices; Fig. 11 connects support levels to command duration. Preserve visible differences in panel scales. Transfer the explanation of objects and operations, not the sample's hardware hierarchy or generality claims.

## 2. REEF — OSDI 2022

Low-latency inference and work-conserving GPU sharing motivate two mechanisms: idempotence enables re-execution after preemption, while predictable behavior supports filling execution gaps. Sections 2.2 and 3–4 use the same real-time and best-effort tasks throughout the comparison. State semantic prerequisites near the operation they enable.

Fig. 4 (p5) compares sequential execution, waiting-based preemption, multiple streams, and ideal execution under shared arrivals. Stable task colors and distinct timing arrows separate preemption from request latency. Fig. 11 (p12) pairs latency and throughput; Fig. 12 isolates preemption latency. Separate online actions from offline preparation. Keep this conference version distinct from the TOCS extension.

## 3. BlitzScale — OSDI 2025

Scaling depends both on moving weights and on when a new instance can provide useful service. Sections 4–5 connect topology, model segments, and execution to explain topology-aware loading and cooperative inference during loading. Section 6 evaluates scaling behavior and request experience separately.

Figs. 5–8 (p6) progress through topology, components, interference, and scaling. Distinct roles for host caching and GPU servers, with numbered execution steps, explain more than a component inventory. Fig. 16 (p10) connects pseudocode to constraints. Distinguish loading completion, service start, TTFT, and TBT; faster scaling requires evidence linking it to request latency.

## 4. RhymeRL — ASPLOS 2026; arXiv v1 reviewed

Reusable rollout content and duration information support reduced generation work and pipeline scheduling. Sections 3–6 move from rollout behavior to HistoSpec and HistoPipe. Section 7 separates overall throughput, combined mechanisms, and changes over training steps.

Fig. 9 (p5) links the controller, history, rollout, rewards, and training, with a legend for relationship types and numbered steps. Figs. 13–15 (p10) distinguish operating conditions, mechanism contributions, and changing gains. Explain the origin, retained content, use time, and decision impact of historical information. The reviewed section and figure numbers belong to the preprint, and RL-system findings do not establish arbitrary agent-system behavior.

## 5. Jiagu — ATC 2024

Prediction and scheduling costs accompany utilization optimization; reclamation behavior also affects cold starts. The argument decouples prediction from online decisions and resource release from instance eviction, then develops fast/slow paths and placement.

The comparison on p5 identifies concrete dimensions; insights on p6 follow the coupling costs. Sections 7.2–7.3 connect prediction counts, scheduling time, runtime startup, and final outcomes. Fig. 4 (p6) separates profiling/training, control plane, and workers. Figs. 10–11 (p12) connect inference counts to scheduling costs and decompose runtime overhead. Pair normalized comparisons with absolute times where scale matters. Fewer predictions and faster applications require separate evidence.

## 6. CPS — ASPLOS 2023 Volume 4

Guest schedulers lack host load and cache-topology information, producing unsuitable placement under two-level scheduling. Sections 2–3 connect missing information to Refer-Table and cooperative scheduling, then examine load-aware and cache-group-aware choices. Distinguish virtual CPUs, physical CPUs, and guest threads.

Figs. 2–3 (p4) separate hardware hierarchy from software cooperation. Figs. 7–8 and Table 4 (p10) combine throughput behavior with running/idle-time decomposition; textures support grayscale reading. Interpret light-load and overcommitted cases separately. Explain which decision-maker lacks which state before introducing an interface.

## 7. BeeHive — ASPLOS 2023

Bursting web demand conflicts with the cost of scaling complete instances. The design offloads suitable execution fragments to FaaS while retaining work requiring local state. Section 2.2 motivates partial, automatic, dynamic offloading; Section 3 follows execution and migratability. Native-call categories connect concrete cases to handling strategies.

Fig. 3 (p5) shows the server JVM and FaaS with closure, execution, fallback, and result paths. Table 2 supplies categories, frequencies, and examples. Figs. 7–8 (p10) preserve application ordering across P99 and load comparisons. Cost conclusions depend on burstiness and low duty cycles. Explain movable objects, shared state, and fallback conditions, and use time series when averages would hide elasticity behavior.

## 8. MITOSIS — OSDI 2023

Remote fork reuses parent-instance state and redistributes work between startup and subsequent access. RDMA connections, permissions, and lifecycles are necessary to the semantics. Explain parent/child state and prepare/resume before lower-level management. Section 7 separates preparation, startup, execution, and memory costs.

Fig. 5 (p6) compares CRIU transfer with remote fork under a shared scenario; Fig. 6 distinguishes user, kernel, and hardware layers. Fig. 12 (p12) separates stage metrics and working-set effects. On-demand access can increase execution time while reducing startup. Moving work outside a measured interval is not the same as eliminating it.

## 9. UGache — SOSP 2023

Read-only embedding access, skew, and cross-GPU differences motivate coordinated cache placement. Placement and extraction contention jointly affect performance, so Solver and Extractor have separate responsibilities. Section 4 connects offline planning, population, and online lookup; Sections 7.2 and 8.2–8.3 discuss refresh and outcomes.

Fig. 5 (p5) distinguishes framework, components, caches, GPUs, and offline/online paths. Figs. 10–11 (p11) align local and overall outcomes across models, data, and servers. Explain why extraction gains do not translate proportionally to application gains and why larger capacity changes the benefit. Keep hit rate, transferred data, extraction time, and application time distinct. Transfer the argument rather than its read-only and access-stability assumptions.

## 10. PhoenixOS — SOSP 2025

Specific synchronization and copying stages cause checkpoint pauses. Speculation with validation overlaps selected work with application execution. The exposition establishes state semantics before copy-on-write, recopy, and validation. Pages 4–5 connect goals, architecture, and state time points; the decomposition on p12 returns to the original pause sources.

Figs. 2–3 (p4) move from execution/copy timing to interception and backend components. Figs. 15–17 (p12) compare application execution, copying, quiescence, and recopy with common lanes. Identify omitted background work. Keep checkpoint completion separate from application downtime; asynchronous execution alone does not establish consistency.

## 11. Copier — SOSP 2025

The copy-use window creates an opportunity for asynchronous copying. Sections 3–4 use it to motivate submission, synchronization, queues, and resource coordination. Evaluation begins with microbenchmarks before OS services and applications, matching the evidence needs of a primitive.

Fig. 4 (p5) juxtaposes memcpy, amemcpy/csync, and internal execution. Figs. 9–10 (p11) distinguish repeated/non-repeated copying and sending/receiving with a normalized baseline. Caller obligations, buffer lifetimes, and synchronization times are interface semantics. Use short code fragments to expose API changes, and separately explain throughput, use latency, and dedicated resource costs.

## 12. KVCache Cache in the Wild — ATC 2025

Production measurements establish reuse patterns, offsets, and temporal changes before motivating cache policies. Measurement is a central contribution, so a long-design/short-motivation template is inappropriate. Section 4.1, Table 2 connects observations to priorities, prefix positions, and lifetimes.

Figs. 15–17 (p8) organize distributions and heatmaps by workload and time. Figs. 25–27 (p13) pair hit rate with QTTFT. Explain whether observations persist, what decision they change, and which service metric responds. Different traces and capacities can weaken the benefit; observational correlation should not become a causal law.
