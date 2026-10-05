# OpenQueue: a fictional related-work report

Original constructed material under Apache-2.0. Publication identity: fictional technical report, edition 1. Reading version: this complete text, 2026-10-05. No DOI or real authors are asserted.

## 1. Scope

One worker serves a fixed inference model. The scheduler has estimated service times at arrival. It admits every request, including during overload. It supplies no tail-latency guarantee and no bounded-memory guarantee.

## 2. Mechanism

At worker idle time, choose the queued request with shortest estimated service time; break ties by arrival order. Run it to completion. The mechanism is non-preemptive and can starve long requests under continuous short arrivals.

## 3. Evidence

This report defines the algorithm only; it reports no measured speedup. It does not evaluate an admission budget. An implementation of the same ordering rule with a budget changes service coverage and must account for rejections separately.
