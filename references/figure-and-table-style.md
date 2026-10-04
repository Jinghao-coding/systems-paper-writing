# Figures and tables: semantics, layout, and prose

Use the corpus notes' recorded page and figure locations to inspect concrete examples. Related conference and journal figures belong to the same research family. Choose visual encoding for the explanatory task, not an author-specific palette or font.

## Architecture: responsibilities and relationships

Choose a primary abstraction level: software components, deployment nodes, or interface boundaries. Use labeled containers when combining levels. A process, GPU, and algorithm step are not equivalent boxes.

Show where inputs originate, where decisions occur, and where data or commands go. Give data, control, and dependency arrows distinct documented meanings. Use a small number of emphasis colors to distinguish new work from existing infrastructure. Numbers should correspond to an actual order.

Examples: UGache Fig. 5 separates offline and online work; CPS Fig. 3 distinguishes guest and host; RhymeRL Fig. 9 distinguishes relationship types; Jiagu Fig. 4 highlights fast and slow paths. MOBIMEM Fig. 2 locates responsibilities but does not by itself explain a task's execution.

## Timelines and states: changed execution

Keep inputs, arrivals, names, and colors consistent across alternatives. Change the decision being compared. REEF Fig. 4 and CoAgent Fig. 6 make such changes visible.

Define axes and lane objects. Distinguish waiting, computation, copying, synchronization, and rollback. Colors and textures can jointly support grayscale reading. Mark total latency, blocking, preemption, and background work separately; identify omitted activity or schematic timing.

State diagrams should show relevant state content and transition triggers. Protocol arrows may represent happens-before rather than duration; FCP Fig. 2 uses this distinction.

Useful examples include:

- DeltaBox Fig. 2: changed state and rollback deltas.
- VarCatcher Figs. 3–6: shared runs explaining representation differences.
- MobiAgent Fig. 3: state-tree merging.
- Wukong+G Figs. 4–6: deployment, operations, and progressively changed execution.
- Pragh Figs. 4, 5, and 10: consistent key/value symbols across access paths and protocols.
- DrTM+B Figs. 9–10 and 17: commit protocols and a millisecond-scale pause; preserve event origins and units.
- REEF TOCS Fig. 9: read/write sets and restartable groups.
- UGache TOCS Figs. 8–9: congestion, grouping, core allocation, and execution time linked by shared source-location symbols.

## Results: match layout to comparison

Use lines for change over load or scale, CDFs for distributions, grouped bars for categories, stacks for additive parts, heatmaps for two-dimensional structure, and scatterplots for relationships between costs.

Keep method colors, markers, and ordering stable. Share legends where helpful. Align axes only when comparisons warrant it, and make differing ranges visible. Pair local and end-to-end metrics: XSched/REEF latency and throughput, KVCache hit rate and QTTFT, or MOBIMEM reuse and final latency. Aligned panels can be clearer than dual axes.

State normalization denominators and direction, including per-workload normalization. Include absolute values when scale matters. SMetric's separately P99-normalized heatmaps support within-policy balance analysis, not cross-policy absolute load comparison.

Identify log scales, broken or truncated axes, percentages, and percentage points. Error bars require actual observations and a defined statistical procedure.

Additional examples:

- Pragh Fig. 16: columns for strategies and rows for throughput, latency, and remote access.
- Prophet Fig. 15: logarithmic speed comparison; distinguish host cores from simulated cores.
- REEF TOCS Fig. 14: device/operator panels separate shortest kernel time from shortest block time.
- UGache TOCS Figs. 15–16: access fractions versus path times, including estimated quantities and common extraction conditions.
- UGache TOCS Fig. 20: extraction benefit and solving cost; Fig. 21: workload change, refresh start, and completion.
- Jiagu TOCS Fig. 12: shared batch-size axis for utilization and latency constraints. Figs. 19–20 use truncated count/density axes, so inspect numerical scales rather than inferring ratios from bar height.

## Tables and pseudocode

Use tables for precise configurations, conditions, symbols, categories, and results. SANL's workload table explains suitability; BeeHive's native-call classification connects cases to handling; KVCache connects observations to policies.

Put units in headers and keep precision consistent with data. Highlight meaningful comparisons rather than every maximum. Expose baseline conditions and inapplicable entries. Binary capability matrices require clearly defined, source-supported dimensions and visible qualifications.

Pseudocode should retain decision-relevant state, conditions, and updates while omitting incidental implementation boilerplate. Synchronize algorithm lines with prose, examples, and figures after edits.

## Captions and publication-size inspection

An experiment's opening states its question and comparison. The body explains findings and supported causes. Captions provide the objects, conditions, units, normalization, and necessary takeaway for reading the figure. Do not force identical conclusions or numbers into three locations or presuppose superiority.

Inspect text and legends at the actual single- or double-column size. Dense examples may need splitting; do not copy visual density as a style rule. Choose vector, raster, or mixed sources according to the user's editing needs and venue requirements. Do not infer an author's drawing software from the PDF.

Use identifying icons or screenshots when they help recognize objects; omit decoration that adds no meaning. Check abstraction levels, arrows, colors, units, normalization, terminology, references, grayscale, and reduced-size readability. Add a first-page figure only when it serves the argument and layout.
