# Venue recommendations by research question

Reviewed: 2026-10-05. Use this map to select relevant readers and paper examples. It is an expandable recommendation set; the manuscript's contribution determines which venues to investigate. The writing priorities below are this skill's synthesis, not official acceptance criteria or a ranking table.

## Select an audience

| Research focus | Recommended starting points | What to make understandable |
| --- | --- | --- |
| Operating systems, distributed infrastructure, cloud platforms | OSDI, SOSP, EuroSys, ATC; SoCC, Middleware, ICDCS for closely aligned work | The abstraction or mechanism, execution semantics, practical constraints, and system-level evidence |
| Storage, persistence, caching, file systems | FAST; relevant OSDI, SOSP, EuroSys, ATC and SYSTOR papers | Data lifecycle, consistency/durability semantics, recovery, and the workload causing the bottleneck |
| Networked systems and communication | NSDI, SIGCOMM; CoNEXT, IMC and INFOCOM according to the contribution | Protocol behavior, deployment assumptions, traffic conditions, and measurement validity |
| Architecture and hardware/software interaction | ASPLOS, ISCA, MICRO, HPCA | The relevant hardware behavior, software interface, implementation or model, and costs across the boundary |
| Parallel execution, compilers, and runtimes | PPoPP, PLDI; CGO, PACT and OOPSLA where appropriate | Execution or language semantics, transformations, synchronization, and end-to-end effects |
| High-performance and distributed computing | SC, HPDC, IPDPS, ICS | Scaling limits, communication, placement, workload size, and resource-normalized comparisons |
| Performance modeling and measurement | SIGMETRICS, PERFORMANCE, IMC, ICPE | The model's assumptions, validation, estimand, workload selection, and uncertainty |
| Data-intensive systems | SIGMOD, VLDB/PVLDB, ICDE; CIDR for suitable exploratory work | Query or transaction semantics, data distribution, consistency, and processing costs |
| Machine-learning infrastructure | MLSys and relevant systems, architecture, networking, and database venues above | Training/serving behavior, quality constraints, workload distributions, and resource costs |
| Reliability, security, and predictable execution | DSN; USENIX Security, IEEE S&P, CCS, NDSS for security contributions; RTSS and RTAS for timing contributions | Fault/threat/timing models, guarantees, failure cases, and evidence appropriate to the guarantee |
| Mobile, edge, and sensing systems | MobiSys, MobiCom, SenSys | Device and network conditions, deployment observations, energy, and user-visible effects |

For early ideas and position papers, also inspect HotOS, HotNets, HotStorage, and APSys. Their article types and evidence expectations differ from full research papers; choose examples accordingly.

Preserve the user's CCF A preference when producing a submission shortlist. Verify the applicable edition of the [official CCF directory](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml) and any institutional rules before assigning categories. The wider reading map intentionally includes specialist and workshop sources. A useful example does not automatically become a recommended submission destination.

## Official entry points and dated scope examples

- [OSDI 2026 CFP](https://www.usenix.org/conference/osdi26/call-for-papers): research and operational-systems tracks have distinct expectations. Select the actual track before applying a novelty checklist.
- [SIGOPS conference directory](https://www.sigops.org/conferences/): entry point for SOSP, EuroSys, SoCC, ASPLOS, and related series. Follow the relevant edition's CFP for submission decisions.
- [EuroSys 2026 CFP](https://2026.eurosys.org/cfp.html): broad systems scope and explicit attention to rigorous evaluation.
- [ASPLOS 2026 CFP](https://www.asplos-conference.org/asplos2026/cfp/): architecture, languages, operating systems, and emerging hardware; also discusses experience and insight-oriented contributions. The acronym is ASPLOS.
- [ATC 2026](https://sigops.org/s/conferences/atc/2026/index.html): ACM SIGOPS Annual Technical Conference. USENIX concluded its ATC series after 2025 ([announcement](https://www.usenix.org/blog/usenix-atc-announcement)); search historical USENIX ATC papers as well as the current series.
- [NSDI 2026 CFP](https://www.usenix.org/conference/nsdi26/call-for-papers) and [FAST 2026 CFP](https://www.usenix.org/conference/fast26/call-for-papers): networked systems and storage-specific entry points.
- [SIGCOMM](https://www.sigcomm.org/events/sigcomm-conference), [CoNEXT](https://www.sigcomm.org/events/conext-conference), and [IMC](https://www.sigcomm.org/events/imc-conference/): distinguish communication mechanisms from measurement contributions.
- [SIGPLAN conferences](https://www.sigplan.org/Conferences/) and [SIGARCH calls](https://www.sigarch.org/call-contributions/): find the appropriate runtime, programming, or architecture audience.
- [SC26 paper guidance](https://sc26.supercomputing.org/program/papers/) and [SIGMETRICS conference history](https://www.sigmetrics.org/history_conferences.shtml): HPC and performance-evaluation entry points.
- [SIGMOD](https://sigmod.org/) and [VLDB](https://www.vldb.org/): check the actual publication route, including proceedings journals, instead of assuming every conference uses the same submission model.
- [RTSS 2026](https://2026.rtss.org/): entry point for time-predictable systems work.

These dated links document the material consulted. For an actual submission, retrieve the requested year and track rather than treating 2026 rules as permanent.

## Matching workflow

1. Recover the manuscript's research question, contribution type, actual mechanism/semantics or finding, evidence scope, and user constraints. Respect named targets and requested classification; do not automatically substitute journals or lower targets to fill a list.
2. Identify a few communities whose readers need this contribution. Topic overlap, contribution form, evidence readiness, and schedule feasibility are separate judgments. Do not recommend an identical list for every GPU or Agent paper. Protocol guarantees, measurements, operational lessons, runtimes, and hardware/software co-design imply different audiences.
3. For each plausible candidate, find the actual edition and track from current official sources. Record retrieval date and URL for the series/year/name, paper type, CFP scope and review criteria, page limit and counting convention, anonymity, AI use/disclosure, submission and supplement rules. If timing matters, record the exact deadline, official time zone and date, and a justified conversion to the user's time zone. Check reviewer-specific AI policy separately for entrusted reviews.
4. Use explicit states: **verified for this edition**, **historical/closed**, **next rules unpublished**, **inaccessible**, or **conflicting official sources**. Never project a future deadline from past years. Search/tool failure leaves a field unverified; it does not inherit an older value. If an entire candidate cannot be verified, present it only as a provisional community fit, not an actionable submission plan. Do not claim that a rule is unpublished merely because one page failed.
5. If the user requests CCF A or another category, verify the applicable official edition and classify each candidate separately. Community influence, directory category, fit, and maturity are different attributes. A reading-map venue is not automatically in the requested class.
6. When needed, inspect nearby accepted papers by research object, contribution form, assumptions, and evidence, using stable full-text locations. Shared keywords alone are insufficient. Explain why an exemplar helps assess the contribution; do not turn observed paper traits into official requirements.
7. Assess readiness from the paper's claim–evidence mapping. Attribute explicit requirements to the CFP; label your methodological judgment as your analysis. A suitable community can still require substantial evidence repair. An otherwise complete study can be unsuitable for a track.

### Delivery

Lead with the strongest fit and decisive risk. Use this compact table:

| Candidate year/track | Why the contribution fits | Current manuscript risks | Highest-value preparation | Sources and verification state |
| --- | --- | --- | --- | --- |
| Verified edition, or provisional series only | Object, audience, contribution form | Claim-specific evidence/communication gaps | Concrete repair and closure criterion | Official links, date, field-specific unknowns |

Separate **current first choice**, **candidate after specified improvements**, and **directions not currently recommended**. Fewer justified candidates are better than an arbitrary fixed count. Do not mix prestige, deadline, implementation size, and research strength into one score, promise acceptance, or invent acceptance probabilities.

For example: “The contribution concerns execution semantics and resource sharing, which matches a systems audience. The immediate preparation is to explain the invariant and make admission policies comparable; broader background would not resolve that evidence gap.” Only make this statement when supported by the actual manuscript.

Use [submission preparation](submission-preparation.md) for applying the verified rules to files. The [worked matching example](../examples/venue-match.md) uses explicitly simulated policies; it is not a live CFP source.
