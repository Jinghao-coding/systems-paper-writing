# Paper corpus

Bibliographic and analysis snapshot: 2026-09-28. The corpus has 28 version records: 12 conference papers, 10 journal papers, and six separately identified agent preprints. Related conference and journal versions form one research family. Publication status here describes the reviewed snapshot; verify current metadata when citing.

The corpus supports writing analysis, not a mandatory citation list. Expand it according to the target problem and venue. The historical selection emphasizes systems research; it does not restrict future sources to an author group.

## Conference records

| Paper | Publication | Public source | Reviewed version |
| --- | --- | --- | --- |
| XSched: Preemptive Scheduling for Diverse XPUs | OSDI 2025 | [Source](https://www.usenix.org/conference/osdi25/presentation/shen-weihang) | Conference PDF |
| Microsecond-scale Preemption for Concurrent GPU-accelerated DNN Inferences (REEF) | OSDI 2022 | [Source](https://www.usenix.org/conference/osdi22/presentation/han) | Conference PDF |
| BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching | OSDI 2025 | [Source](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan) | Conference PDF |
| History Doesn't Repeat Itself but Rollouts Rhyme: Accelerating Reinforcement Learning with RhymeRL | ASPLOS 2026 | [Source](https://doi.org/10.1145/3779212.3790172) | arXiv v1 |
| Harmonizing Efficiency and Practicability: Optimizing Resource Utilization in Serverless Computing with Jiagu | ATC 2024 | [Source](https://www.usenix.org/conference/atc24/presentation/liu-qingyuan) | Conference PDF |
| CPS: A Cooperative Para-virtualized Scheduling Framework for Manycore Machines | ASPLOS 2023 Volume 4 | [Source](https://ipads.se.sjtu.edu.cn/zh/publications/LiuASPLOS23.pdf) | Conference PDF |
| BeeHive: Sub-second Elasticity for Web Services with Semi-FaaS Execution | ASPLOS 2023 | [Source](https://ipads.se.sjtu.edu.cn/zh/publications/ZhaoASPLOS23.pdf) | Conference PDF |
| No Provisioned Concurrency: Fast RDMA-codesigned Remote Fork for Serverless Computing (MITOSIS) | OSDI 2023 | [Source](https://www.usenix.org/conference/osdi23/presentation/wei-rdma) | Conference PDF |
| UGACHE: A Unified GPU Cache for Embedding-based Deep Learning | SOSP 2023 | [Source](https://github.com/SJTU-IPADS/ugache) | Conference PDF |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | SOSP 2025 | [Source](https://github.com/SJTU-IPADS/PhoenixOS) | Conference PDF |
| KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider | ATC 2025 | [Source](https://www.usenix.org/conference/atc25/presentation/wang-jiahao) | Conference PDF |
| How to Copy Memory? Coordinated Asynchronous Copy as a First-Class OS Service | SOSP 2025 | [Source](https://sigops.org/s/conferences/sosp/2025/accepted.html) | Conference PDF |

See [conference notes](paper-analyses-conferences.md) for section and figure locations.

## Agent preprints

| Paper | Reviewed version |
| --- | --- |
| [SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565) | arXiv v1 |
| [DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback](https://arxiv.org/abs/2605.22781) | arXiv v1 |
| [CoAgent: Concurrency Control for Multi-Agent Systems](https://arxiv.org/abs/2606.15376) | arXiv v1 |
| [MobiAgent: A Systematic Framework for Customizable Mobile Agents](https://arxiv.org/abs/2509.00531) | arXiv v1 |
| [Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM](https://arxiv.org/abs/2512.15784) | arXiv v1 |
| [Get Experience from Practice: LLM Agents with Record & Replay (AgentRR)](https://arxiv.org/abs/2505.17716) | arXiv v1 |

These six preprints were deliberately included for session scheduling, environment state, concurrency, mobile execution, and experience reuse. See [agent notes](paper-analyses-agents.md).

## Journal records

Seven TPDS and three TOCS records are listed in the [journal corpus](journal-corpus.md), with [analysis notes](paper-analyses-journals.md).

## How to extend the corpus

Record the original publication or author source, DOI or version identifier, relevant sections, and inspected figures. Analyze the research question, section roles, technical reasoning, sentence/paragraph progression, evaluation, visual encoding, and text–figure division. Distinguish reading an abstract, reading passages, and inspecting rendered pages. Derive guidance from concrete observations before generalizing; do not copy a sample's unsupported rhetoric or editorial errors. PDFs and private reading artifacts remain outside this repository.

## Stable reading-version records

The [three deeper cases](case-study-depth.md) cover mechanism, protocol/correctness, and measurement reasoning. Their [fingerprints](reading-versions.json) separate research family, publication edition, exact reading bytes, extracted text, and passage locators. Existing notes retain their historical reading scope; a publication DOI identifies an edition, not necessarily identical PDF bytes. When adding or refreshing a case, record both identities and any change in pagination.
