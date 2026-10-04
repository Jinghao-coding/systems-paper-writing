# Systems-writing resources and how to apply them

Reviewed: 2026-10-05. These are independently summarized recommendations from original author pages, official conference material, and first-person community articles. Read the relevant item for the current writing problem. Personal advice informs judgment; the target edition's official instructions govern submission requirements.

## Core writing and language

### 1. Levin and Redell: How (and How Not) to Write a Good Systems Paper

[USENIX text](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html), originally published in Operating Systems Review, July 1983; based on the ninth SOSP submissions. Read the originality, reality, lessons, and presentation discussions.

Apply: identify the new knowledge, its relationship to earlier work, implementation evidence, and what readers can reuse. Make the significant design choice and its consequence explicit. Use the classic questions to diagnose the argument; use current venue instructions for policies.

### 2. Irene Zhang: Hints on how to write an SOSP paper

[Author blog](https://irenezhang.net/blog/2021/06/05/hints.html), 2021-06-05.

Apply: explain why the work matters to systems readers and what they should understand before each technical step. Use the contribution to select detail and organize the story. Keep the user's actual research central; do not manufacture a dramatic motivation or enforce a universal paragraph count.

### 3. Gernot Heiser: Tips and Guidance for Students and ECRs Writing Papers and Reports

[Author guide](https://gernot-heiser.org/style-guide.html), especially General Advice, About Paper Writing, and Some Things People Frequently Get Wrong.

Apply: maintain reader context, use a coherent purpose at sentence/paragraph/section scale, and align the introduction with the completed paper. During language edits, inspect unclear references, overloaded noun phrases, and inconsistent technical names. Preserve natural sentence variation. Adapt the author's stylistic preferences to the project rather than enforcing fixed paragraph lengths or one voice throughout.

### 4. Simon Peyton Jones: How to write a great research paper

[Microsoft Research resource](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) and [slides](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/02/simon-peyton-jones_paper.pdf).

Apply: use early writing to expose gaps in the idea, explain the central insight before excessive detail, and use a concrete example to help the reader understand it. A draft may reveal an unanswered scientific question; language polishing must preserve that distinction instead of filling the gap with invented evidence.

## Introductions and contribution types

### 5. ATC 2026: Extended Abstract Guidelines for Authors

[Official guidelines](https://sigops.org/s/conferences/atc/2026/abstract.html), Extended Abstract Guidelines section.

Apply: check whether the introduction makes the problem's importance, relevant prior limitations, technical insight, and supported results recoverable. The explicit format applies to that edition's extended abstract; elsewhere use these as content questions and let the research determine their order and length.

### 6. OSDI 2026 and ASPLOS 2026 calls for papers

[OSDI CFP](https://www.usenix.org/conference/osdi26/call-for-papers), Submitting a Paper and Submission Tracks; [ASPLOS CFP](https://www.asplos-conference.org/asplos2026/cfp/), scope and contribution discussion.

Apply: identify whether the paper contributes a new mechanism, operational experience, or a validated insight. Explain the actual contribution and evaluate it on appropriate evidence. For example, assess an operational report through its concrete experience and lessons rather than inventing a novel algorithm to make it resemble another paper type.

### 7. The journey of real-life industry work behind an OSDI paper

[SIGOPS first-person account](https://www.sigops.org/2024/the-journey-of-real-life-industry-work-behind-an-osdi-paper-global-capacity-management-for-millions-of-servers/), 2024-02-05; the Flux capacity-management project. Read the problem decomposition and Preparing for landing sections.

Apply: distinguish the broader engineering effort from the paper's chosen contribution. Explain the operational constraints that motivated decomposition and identify which decisions the paper addresses. Preserve evidence from deployment and iteration when it teaches a reusable lesson. Present supported design rationale without inventing development history.

## Evaluation, artifacts, and reviewing

### 8. Gernot Heiser: Systems Benchmarking Crimes

[Author guide](https://gernot-heiser.org/benchmarking-crimes.html), benchmarking categories and best practice. Also recommended by the [EuroSys 2026 CFP](https://2026.eurosys.org/cfp.html).

Apply: check workload selection, baseline configuration, absolute quantities, aggregation, and resource costs. Separate component measurements from application performance; evaluate relevant regressions and overheads. Keep calibration and evaluation data appropriately separated. Choose uncertainty analysis for the measurement design, not a universal threshold or statistical test. Describe a concrete flaw and its effect without copying the source's accusatory tone.

### 9. Timothy Roscoe: Writing reviews for systems conferences

[Author-hosted notes](https://people.inf.ethz.ch/troscoe/pubs/review-writing.pdf), March 2007, for the SOSP shadow PC; especially Structure of a review.

Apply: summarize the contribution neutrally before judging it, explain concerns through specific evidence, and distinguish uncertainty from a demonstrated error. For an author response, answer the actual concern with the relevant evidence and planned or completed correction; keep review dialogue out of the manuscript.

### 10. EuroSys AE chairs: Lessons from Five Years of Artifact Evaluation at EuroSys

[SIGOPS article](https://www.sigops.org/2025/lessons-from-five-years-of-artifact-evaluation-at-eurosys/), 2025-08-05, drawing on 2021–2025 experience; How Artifact Evaluation Works and Six Persistent Challenges.

Apply: connect the paper's main claims to runnable experiments and clear documentation. State hardware requirements early and plan artifact preparation alongside the paper. Distinguish availability, functionality, and reproduced results. The article's proposed future policies remain proposals; consult the actual year's artifact call.

### 11. Dong Du and Jiayi Meng: Lessons Learned from Chairing the Artifact Evaluation at SOSP 2023

[SIGOPS article](https://www.sigops.org/2024/lessons-learned-from-chairing-the-artifact-evaluation-at-sosp-2023/), 2024-01-26; Challenges We Did Not Expect.

Apply: specify special hardware, execution access, expected outputs, and meaningful result tolerances. Separate a functionality demonstration on substitute hardware from reproduction of a hardware-dependent performance claim. Use the article to anticipate practical documentation needs.

## Turn sources into revisions

| Observed manuscript issue | Revision action | Useful resources |
| --- | --- | --- |
| The introduction lists modules but leaves the idea unclear | State the observation, changed decision, and resulting effect; retain only necessary module names | 1, 2, 4, 5 |
| A sentence is grammatical but hard to follow | Identify its actor/action/object and ambiguous referents; reconnect it to the paragraph's purpose | 3 |
| A paper resembles an engineering diary | Select the technically meaningful constraints, decisions, and lessons supported by the project | 1, 6, 7 |
| A speedup claim conceals costs or a narrow workload | Inspect metric definitions, baseline conditions, absolute results, overheads, and supported scope | 8 |
| Review feedback is vague or combative | Locate the problem, identify its consequence, and propose an actionable correction | 9 |
| The artifact instructions cannot be matched to figures | Map the supported claims to commands, inputs, outputs, and relevant hardware | 10, 11 |

For a prose-edit request, apply the relevant revision directly and list any unresolved scientific question separately. For an evaluation-design request, turn that question into a proposed experiment before execution. Preserve the user's scope and resource budget.

When adding a resource, record its author or responsible body, URL, date when available, relevant section, and the decision it improves. Summarize in original language, retain attribution, and reconcile advice with the current task. Add new guidance only when it changes the skill's behavior; avoid accumulating duplicate maxims or copying complete articles.
