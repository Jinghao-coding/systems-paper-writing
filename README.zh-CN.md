<div align="center">

# Systems Paper Writing

**把问题、机制与证据写清楚。**

面向英文计算机系统论文的初稿审阅、他稿评审与投稿匹配技能。

[English](README.md) · **简体中文**

</div>

## 三项主能力

| 任务 | 核心交付 |
| --- | --- |
| **作者初稿审阅** | 整体判断、可定位的实质问题、主张与设计和证据的对应关系、优先修改路线，按请求提供英文替换正文 |
| **其他论文评审** | 中立贡献复述、有依据的优点与问题、可回答的作者问题，区分确定错误、证据不足和解释不清 |
| **投稿匹配与准备度分析** | 少量有来源的会议及年份/track 候选，分别判断研究适配、当前证据风险与投稿安排 |

局部英文润色、机制重写、实验分析、相关工作核查、期刊扩展、配图和格式检查仍可独立调用。润色保持局部范围；论文审阅检查研究实质。机制、抽象、协议、测量、部署经验、跨层设计与优化使用相应证据，不统一要求新算法或性能提升。

操作指南使用英文，交流和正文语言遵循用户要求。实际推荐核对当届官方政策与用户要求的目录分类。[会议指南](references/venue-guide.md)按贡献选择社区，分别判断适配与成熟度。

## 安装与调用

Codex 新安装示例：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-paper-writing.git ~/.agents/skills/systems-paper-writing
```

Claude Code 使用 `~/.claude/skills/systems-paper-writing`。已有 `~/.codex/skills` 安装时沿用现有位置，避免重复副本。安装后开启新任务或刷新技能列表。

```text
使用 $systems-paper-writing 审阅当前初版论文，
先判断研究贡献、设计与实验是否相互支持。
按位置指出问题，区分研究缺口与表达问题，给出优先修改路线。
本次不修改文件。
```

```text
使用 $systems-paper-writing 对这篇公开论文做模拟评审。
准确总结贡献，给出有依据的优点、主要问题和作者需要澄清的问题。
区分确定错误与材料不足，不预设拒稿结论。
```

```text
使用 $systems-paper-writing，根据当前论文的研究问题、贡献类型和已有证据，
推荐匹配的顶级会议及具体 track。
核查当前官方要求，说明适配理由、主要风险和投稿前改进建议，
不要仅按会议名气排序。
```

短任务也可直接调用：“只润色这一段，保留正确内容”；“根据算法重写机制解释”；“比较会议稿与期刊稿的实质增量”；“核对引用元数据及原文支持”。Claude Code 使用 `/systems-paper-writing`。

## 实际交付示例

> **已确认的证据冲突——摘要、算法第 1 步、表 1。** 摘要声称接纳全部请求，算法却在队列满时拒绝请求；结果表中 GateQueue 完成 80 个请求，FIFO 完成 100 个。两项 P99 对应不同样本群体。先同步接纳语义，并同时报告覆盖率和已完成请求的延迟；若保留同等服务条件下的收益主张，需要采用一致接纳条件进行对照。完成条件：所有正文和图注使用正确统计范围，同等服务收益有对应证据。

[完整初稿示例](examples/author-review.md)包含可分发的最小论文工程、旧版本与实际补丁；另有[模拟评审](examples/other-review.md)和[投稿匹配](examples/venue-match.md)。数据和政策均明确标为构造材料。

## 内容导航

- [审阅流程](review-workflows.md)：作者诊断、他稿证据判断与正式受托审稿政策入口。
- [写作指导](references/style-analysis.md)与[修改示例](references/edit-catalog.md)：语言、信息组织、语义保持。
- [系统论文组织](references/systems-paper-patterns.md)：设计选择、证据对应、评价与期刊扩展。
- [图表指导](references/figure-and-table-style.md)与[投稿准备](references/submission-preparation.md)。
- [论文样本目录](references/paper-corpus.md)：12 个会议版本、10 个期刊版本、6 篇标明身份的 Agent 预印本；同项工作的不同版本按研究关系理解。
- [文献工具](references/reference-workflow.md)：检索、DOI、BibTeX 与元数据核验。
- [来源记录](references/provenance.md)与[旧仓库整合说明](references/repository-migration.md)。

## 可选文献工具

在仓库目录运行，依赖 Python 3.10+ 标准库：

```bash
python3 scripts/reference_tools.py links --topic "GPU preemption" --venue OSDI
python3 scripts/reference_tools.py search --query "GPU preemption scheduling" --limit 5
python3 scripts/reference_tools.py lookup --doi 10.1145/945445.945450
python3 scripts/reference_tools.py bibtex --doi 10.1145/945445.945450
python3 scripts/reference_tools.py verify --input papers.json
```

工具输出 JSON，保留输入文件。联网功能只提交所需题名、查询词或 DOI；无需上传论文正文。核验区分字段匹配、冲突、缺项和访问失败，文献对正文论点的支持仍需阅读原文。输入格式见[工具指南](references/reference-workflow.md)。

旧 `system-paper-skill` 的适用功能已选择性整合：保留检索入口、元数据查询和引用获取/核对，移除固定会议排名、猜测式 BibTeX 生成、缓存文件和旧输出。

## 检查与更新

```bash
python3 scripts/check_package.py
python3 -m unittest discover -s tests
```

行为评测使用[隔离输入与验收答案](tests/behavior/README.md)，支持无技能、旧版本与当前版本的准备和实际输出记录；本轮结果见[验证记录](validation/2026-10-05.md)。

Git 安装在处理好本地修改后执行 `git pull --ff-only`。正文材料、学校规定与个人资料保存在论文项目中。

采用 [Apache-2.0](LICENSE)，保留已整合部分的 [MIT 许可](licenses/system-paper-skill-MIT.txt)；完整署名见 [NOTICE](NOTICE.md)。
