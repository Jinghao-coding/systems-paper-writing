# Journal-paper analysis notes

Snapshot: 2026-09-28. The ten [journal records](journal-corpus.md) preserve version-specific organization, key-passage, and representative-page observations. Page numbers refer to each reviewed PDF. Conference/TOCS comparisons below are limited to the stated sections and extension statements.

## 1. SANL — TPDS 2017

Contention and NUMA locality change the costs of in-place versus delegated execution. The design explains mode switching, delegated requests, and server placement. Earlier lock comparisons motivate Section 3's local contention signals, voting, thresholds, and service limits; evaluation progresses from controlled contention to applications. Table 6 explains workload suitability through lock behavior and critical-section fractions.

Section 3.1 (p5) defines a signal and its computation, then explains global averaging cost and threshold oscillation before introducing voting and buffered counts. Low-contention measurement costs remain visible. Fig. 2 (p4) shows modes; Algorithm 1 and Fig. 3 (p5) provide precision and a dynamic example; Fig. 19 (p13) shows server reselection. Explain update frequency, hysteresis, and reserved-core accounting rather than copying thresholds or sampling rates.

## 2. FCP — TPDS 2016

Shared reader-side state limits scaling, while writers need timely knowledge of reader progress. The protocol exploits common propagation behavior and actively handles delayed readers; sleeping readers require explicit transitions and counts. Section 3 develops the protocol, Section 4 instantiates a read–write lock, and Section 8 evaluates kernel and user contexts.

Sections 3.1–3.2 (pp4–5) distinguish typically fast visibility from synchronization required for correctness. Happens-before relationships explain progress and additional handling for migration, inactivity, and sleep. Section 8.2 (p12) distinguishes memory-access evidence from a proposed bus-contention explanation. Fig. 2 (p5) uses reader/writer lanes and numbered dependencies; Figs. 12–13 (p12) use markers and line styles for scalable comparisons. Cheap common paths and correctness for all allowed executions require separate arguments.

## 3. VarCatcher — TPDS 2017

Identical inputs can produce different parallel execution patterns, confounding cross-design comparisons. Section 2 establishes the measurement problem; Section 3 motivates PCV and grouping; Section 5 demonstrates analysis uses.

The paired examples on pp4–5 isolate what per-core concatenation and global aggregation omit: relative progress and individual core paths. Section 5.1 (p9) separates shared pattern sets, pattern frequency, and one-to-one matched-run fractions. Fig. 2 (p4) shows the measurement pipeline; Figs. 3–6 compare representations through common runs; Figs. 14–16 (p9) answer distinct questions about sets, distributions, and sample counts. Validate the representation before its applications. Matched comparisons are not automatically unbiased workload averages.

## 4. Prophet — TPDS 2017

Section 2 locates cycle-oriented simulation costs in host instructions, cache misses, and branch mispredictions. Section 3 changes the organizing unit to instructions, successively adding pipeline, dependence, resource, branch, and cache constraints; Section 3.5 reunites them in an example. Section 4 handles multicore speculation and communication, followed by implementation and accuracy/speed/use-case evaluation.

Section 4.2 (p6) identifies a new global-adjustment bottleneck before introducing Bloom-filter reduction. Fig. 4 (p5) integrates stages, dependencies, corrections, and branch flushing on a common cycle grid. Fig. 15 (p11) distinguishes physical host cores from simulated cores; Fig. 16 (p12) explains a shifted bottleneck.

Section 6.4.2 and Tables 5–6 (pp11–12) connect error and runtime to actual architecture choices. Full-system and user-mode scale limits differ. Recorded internal discrepancies include 9.8% versus Table 6's 9.58%, and about 107 minutes described as 1.6 hours instead of about 1.79. Preserve the measurement scope and check numbers independently of publication status.

## 5. DrTM+B — TPDS 2022

Section 2.3 (p4) frames migration as sustained interference, including on-demand reads and contention. Section 3 explains pre-copy's remaining costs before using replicas and forwarded logs. Sections 4–6 develop structures, replication, commit, hybrid copying, placement, and recovery.

Section 4.3 (pp7–8) states existing guarantees and remaining commit conditions before identifying replay-induced pauses and introducing exchange mode. Prepare, Collect, Suspend, and Resume consistently refer to nodes, offsets, and partition states. Figs. 9–10 compare commit protocols with common lanes and downtime intervals; Fig. 17 (p12) zooms to milliseconds; Fig. 19 links gradual service benefit to migration completion.

Sections 7.4–7.5 distinguish copying speed, foreground interference, and longer total reconfiguration. In Section 7.6, a reported 44 ms starts at suspicion while failure appears at −17 ms; define whether recovery includes detection. Separate benefit onset, foreground pause, and background completion.

## 6. Wukong+G — TPDS 2022

Sections 2–3 connect light/heavy queries to CPU/GPU execution, then identify memory, PCIe, communication, and utilization costs. Section 4 organizes mechanisms around one query's needs: fitting data, timely transfer, distributed movement, and suitable execution granularity.

Section 4.1 (pp5–6) progresses from graph size to query predicates, triple patterns, overlapped preparation, block exchange, and reuse. Each step addresses a remaining cost. Section 4.4 (p8) explains why multiple CUDA streams alone are insufficient before introducing multi-query combining.

Figs. 4–6 separate deployment, numbered operations, and changing timelines. Figs. 14–16 (p13) separate throughput contributions, utilization over time, and thresholds. Section 6.5 (p11) distinguishes aggregate-memory capacity gains from later parallelism gains. Section 6.10 and Table 8 cover a benefiting query subset; do not treat its aggregate as all queries. SM-efficiency measured by nvprof is not a FLOPS-utilization ratio.

## 7. Pragh — TPDS 2024

Section II contrasts irrelevant movement under coarse partitioning with metadata cost under fine partitioning. Section III keeps keys fixed while moving values. Section IV extends basic migration with location caching, concurrent updates, and monitoring; Section V revisits the protocol without RDMA.

Sections IV-A–B (pp5–6) begin with read-only traversal, then address stale addresses, reclamation, and remote key access. Section IV-C adds Put under the store's existing update semantics. “No metadata” concerns additional full location mappings, not all address fields or caches.

Figs. 4–5 explain key/value paths, migration, and invalidation; Fig. 10 (p8) carries the same objects into message passing. Fig. 16 (p13) aligns strategies and throughput/latency/remote-access metrics. Section VII-C compares when eager/deferred benefits appear, not just the final steady state. Sections V and VII-F explain why value migration alone may not reduce message round trips without location caching. Platform transfer requires revisiting actual access paths.

## 8. REEF — TOCS, DOI 10.1145/3768622

The 42-page journal version extends recovery and kernel selection. The conference version already supported NVIDIA by waiting for running kernels; journal Section 4.6 (pp15–16) adds trap/EXIT and binary instrumentation. Conference Section 4.3 (p8) and journal Section 4.4 (pp13–15) use different restart-location mechanisms. Conference Section 8 (p15) identifies non-idempotent kernels and selection limitations later addressed in journal Sections 4.4 and 5.3.

Section 4.4 explains when restarting one kernel is unsafe, defines group re-execution semantics, and uses K0–K3 read/write sets to derive restartable groups. Section 5.3 (pp20–22) shows that the fastest isolated kernel may not be best for padding, then handles the enlarged search space with offline dominance pruning.

Section 6.2 (p24) defines latency and per-client throughput denominators. Section 6.5 (pp29–30) connects CU usage and kernel/block duration to RT/BE pairs. DKP-MV benefits require comparison with DKP. Section 6.6 disables source-transforming padding for engine comparisons. Section 6.7's LLM example has a specific configuration and output length. Section 7 retains determinism, side-effect, dynamic-behavior, and capacity assumptions.

Recorded visual pages: 13, 14, 21, 29. Fig. 9 uses read/write sets and group boundaries; Fig. 14 compares device/operator points by kernel time, block time, and occupancy; Figs. 23–24 align service metrics and CU usage. A p14 comparison calls a four-kernel group smaller than a three-kernel group, contrary to the figure and derivation; treat it as a referent error, not a writing pattern. Finite pair tests do not establish universal starvation freedom.

## 9. UGache — TOCS, DOI 10.1145/3767725

The 32-page journal version connects placement and extraction costs: higher global hit rate can reduce locality, and remote access can contend for links. Section 5 explains factored extraction; Section 6 defines access locations, storage/capacity constraints, hotness-weighted path times, overlap, and tractable grouping.

The extension adds affinity-aware decisions, baselines, application examples, and refresh detail. Section 6.4 (pp15–16) introduces per-GPU hotness; Section 7.3 (p17) explains dispatch that creates those distributions. Conference Section 7.2 already had background refresh. Journal Section 7.2 and Algorithm 1 (pp16–17) expand index removal, in-flight batches, space reuse, local filling, and remote-address installation. Section 8.8 (p26) adds evidence about restoration after hot/cold-ID swaps. Do not label the existing refresh mechanism as new.

Section 8.5 (pp23–24) holds extraction constant across placement policies. Fig. 17's average 1.9% gap uses reduced synthetic instances on a particular server, not a universal approximation bound. Section 8.7 reports both extraction gains and slower solving, with explicit exclusions. Section 8.9 (pp27–28) transfers placement to historical images; similar behavior to partitioning explains the cost structure rather than proving every original mechanism generalizes.

Recorded visual pages: 11, 17, 23, 26. Figs. 8–9 connect congestion, grouping, and execution. Figs. 15–16 separate access fractions and path times, including estimated local times. Fig. 20 pairs extraction benefit with solving cost; Fig. 21 marks workload change, refresh start, and completion. Preserve read-only versus mutable-data update costs from Section 7.4.

## 10. Jiagu — TOCS, DOI 10.1145/3788863

The 38-page extension connects GPU batching to utilization and scaling: batch size affects efficiency, waiting, and per-instance saturated load. New material spans motivation (Section 2.2.3), overview (Fig. 6), configuration (Section 6), implementation (Section 7), and evaluation (Section 8.4), retaining the original fast/slow-path argument.

Sections 4.2–4.5 (pp14–18) progress from Boolean deployment capacity through neighbor protection to numerical capacity, then combine events in one example. Sections 6.1–6.2 turn utilization and latency profiles into batch choices, saturated RPS, and timeout handling. Section 7 (p22) distinguishes implemented CPU prediction from proposed GPU predictor use. GPU tests use a particular four-V100 machine; do not transfer CPU measurements into GPU implementation claims.

Section 8.2 distinguishes cost per scheduling event, per cold start, and across cold starts. Section 8.4 combines violation rates, instance counts, density, and cold-start behavior. A larger batch can use fewer instances while violating QoS. OPT names a selected configuration rather than proving global optimality.

Recorded visual pages: 12, 20, 21, 29. Fig. 6 locates fast/slow paths and GPU decisions; Fig. 12 pairs utilization and latency against batch size; Figs. 19–20 use truncated count/density axes. Recorded issues include outdated two-insight counts, a memory-correlation label for mainly SM measurements, and an inequality that becomes equality when timeout does not exceed execution time. Similar errors on two test halves alone do not establish absence of overfitting. Keep these scientific questions separate from stylistic preferences.

## Scope of the synthesis

Journal depth is useful when it explains remaining mechanism questions, operating conditions, and evidence differences. It is not a requirement to lengthen background or add a fixed number of challenges. For Prophet, DrTM+B, Wukong+G, and Pragh, the notes analyze the journal itself; claims of newly added journal contributions require a separate predecessor comparison. REEF, UGache, and Jiagu comparisons use the stated conference/journal sections and extension statements.
