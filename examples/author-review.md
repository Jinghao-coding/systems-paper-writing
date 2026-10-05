# Author draft review: GateQueue

**Task:** review the active first draft without edits. Materials: `paper/main.tex`, five included sections, `PROJECT.md`, and inactive `history/v0-abstract.tex`. No source execution or rendered-page inspection. All data are synthetic teaching data.

## Overall assessment and actual argument

The useful contribution is the explicit coupling of admission control with queue ordering for a shared, non-preemptive inference worker. Its operations and queue bound are understandable. The principal problem is the equal-service performance claim: the actual algorithm rejects work, and the current table covers different completed populations. The result can support a narrower admission/latency trade-off, not the abstract's unchanged-work claim.

| Author claim | Design/evidence | Supported interpretation |
| --- | --- | --- |
| Accept all requests | Design, arrival step: reject at capacity 8 | Bounded queue with explicit rejection |
| 40% lower end-to-end P99 without changing completed work | Evaluation table: 100 to 80 ms, 100 to 80 completions; Eq. 1 excludes rejected requests | 20% lower completed-request P99 with 20% fewer completions in this synthetic trace |
| Equal service coverage | Introduction vs. evaluation admission counts | Not established under these policies |
| Non-preemptive execution avoids discarded partial work | Introduction and design dispatch step | Consistent; preserve the clear paragraph |

The paper does not claim starvation freedom. Do not invent that guarantee or treat its absence as a contradiction. The actual update schedule of the estimator remains unclear.

## Located findings

**P1 — Service population changes.** Locations: abstract “accepts all” and “without changing completed work”; introduction's equal-coverage sentence; design step 1; Fig. 1 caption; Table 1 caption and rows. Nature: evidence and cross-location facts. Status: confirmed contradiction in the text, not evidence of an implementation bug. Rejection at capacity contradicts all-arrivals execution; 80 versus 100 completions makes the latency populations unequal. Minimum repair: describe admission and completed-request P99 consistently and remove equal-coverage claims. To claim a scheduling benefit under equal coverage, compare the ordering rules under a common admission/service condition. Completion: every claim/caption uses the correct population and any equal-service benefit has a corresponding controlled comparison.

**P1 — Stale magnitude.** Locations: abstract 40%; Table 1 P99 100/80; inactive historical abstract 100/60. Nature: research fact. Status: confirmed numerical mismatch. The current reduction is `(100-80)/100=20%`. The old record explains the likely origin without making it current evidence. Repair: replace 40% and synchronize the abstract against the active table. Completion: all current numerical claims use current data and the completed-request qualification.

**P2 — Estimator lifecycle unclear.** Location: design paragraph after the algorithm. Nature: explanation with an evidence-backed generalization risk. Status: clarification needed. Updates occur after completion, but initialization and schedule are unspecified; readers cannot reproduce decision inputs or evaluate whether evaluation fitting used future observations. This does not establish leakage or a wrong algorithm. Repair: specify when initial estimates were fitted and updates applied, using actual project records. Completion: each dispatch input is available at its stated decision time, or the evaluation is clearly labeled offline/oracle.

**P3 — Visual inspection pending.** The figure source's caption contradicts rejection, but no rendered page was supplied. Correct the caption from source evidence; do not claim that layout, font size, or arrow placement has been inspected. This is an inspection limit, not a defect in the paper's rendering.

## Priority route

1. **Existing material:** correct the numerical claim and admission descriptions in abstract, introduction, Fig. 1, and Table 1. Preserve the equation, labels, non-preemption paragraph, and low-load no-gain result. Obtain the documented estimator initialization/update details; do not write invented ones.
2. **Reanalysis:** if existing request logs are available, separate admission, completion, timeout, and latency distributions using the same interval and clarify coverage. The package contains no logs, so do not claim this reanalysis has been performed. Aggregate rows cannot recover missing quantiles or uncertainty.
3. **New evidence:** if retaining an equal-service scheduling claim, compare FIFO and shortest-estimate ordering with the same admission policy and service constraints. Measure coverage and latency jointly. This is the decisive control, not a demand for an arbitrary number of GPUs or baselines.
4. **Positioning:** with present material, describe a bounded-queue admission trade-off illustrated by synthetic data. Retaining a general tail-latency improvement claim requires evidence beyond this illustration.

## After an explicit request to revise

The [patch](author-revision.diff) changes only supported claims/captions; it does not fill estimator details or fabricate experiments. Apply it to a copy of `paper/`. Its revised abstract reads:

> Shared inference services face queue growth during bursts. GateQueue rejects requests when its waiting queue reaches a fixed capacity and orders admitted requests by predicted service time. In a synthetic burst trace, GateQueue completes 80 of 100 requests with a completed-request P99 latency of 80 ms; FIFO completes all 100 with a P99 of 100 ms. These observations illustrate a trade-off between service coverage and tail latency under the respective admission policies.

This is usable English replacement text for the teaching manuscript. It narrows the claim to the supplied evidence and leaves the correct non-preemption explanation unchanged.
