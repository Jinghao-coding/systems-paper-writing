<div align="center">

# Systems Paper Writing

**把问题、机制与证据写清楚。**

面向 CCF A 类会议与期刊的英文计算机系统论文写作技能。

[English](README.md) · **简体中文**

</div>

## 能做什么

覆盖调度、GPU 共享、集群管理、AI 基础设施和 Agent 系统，支持论文组织、起草、精修、审阅和期刊扩展。

| 任务 | 处理重点 |
| :--- | :--- |
| 组织论证 | 明确研究问题、章节作用及问题—设计—证据对应 |
| 解释机制 | 写清对象、状态、触发条件、决策和执行后果 |
| 精修英文 | 改善句间衔接、具体动作与术语一致性，保留技术含义 |
| 分析实验 | 区分指标、比较口径、总体效果、机制贡献和开销 |
| 期刊扩展 | 对照版本，区分新增机制、解释增强和新增证据 |
| 整理引用 | 生成检索入口、查询元数据、获取 BibTeX、逐字段核对 |

技能指令和参考指南使用英文，交流语言遵循用户要求。CCF A 是目标场所与选材偏好；章节数量、句数、篇幅和图表按研究与当届要求确定。中文博士论文整合与学校规范适配可使用独立的 `cs-phd-writing`。

## 推荐会议与写作资料

以 **OSDI、SOSP、ASPLOS、EuroSys、ATC** 为常见起点，按研究问题扩展：网络系统参考 **NSDI / SIGCOMM**，存储参考 **FAST**，体系结构参考 **ISCA / MICRO / HPCA**，并行执行与系统软件参考 **PPoPP / PLDI / SC**，性能评价参考 **SIGMETRICS**，数据系统参考 **SIGMOD / VLDB / ICDE**，机器学习基础设施参考 **MLSys**。

[会议推荐指南](references/venue-guide.md)覆盖 11 个研究方向，并补充专业会议和 workshop。阅读选材与投稿候选分别判断；实际投稿按当届范围、文章类型及适用的 CCF 目录筛选。

[写作方法](references/writing-playbook.md)已将资料内容提炼为可直接执行的论证方法、语言诊断、实验解释、审稿回应和 artifact 准备步骤，并附有上下文明确的修改示例。日常写作和润色直接应用技能中的方法；[来源记录](references/writing-sources.md)单独保存署名和链接。查询新文献、核验引用或确认当届投稿规定时，再按任务需要联网。

## 安装与调用

Codex 新安装示例：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-paper-writing.git ~/.agents/skills/systems-paper-writing
```

Claude Code 使用 `~/.claude/skills/systems-paper-writing`。已有 `~/.codex/skills` 安装时沿用现有位置，避免重复副本。安装后开启新任务或刷新技能列表。

```text
使用 $systems-paper-writing 精修设计部分。
先读相邻段落、算法和符号定义，保留技术含义，改善执行过程与段落衔接。
先给可用替换文本；科学内容的更正单独说明依据。
```

Claude Code 使用 `/systems-paper-writing`。

## 内容导航

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

Git 安装在处理好本地修改后执行 `git pull --ff-only`。正文材料、学校规定与个人资料保存在论文项目中。

采用 [Apache-2.0](LICENSE)，保留已整合部分的 [MIT 许可](licenses/system-paper-skill-MIT.txt)；完整署名见 [NOTICE](NOTICE.md)。
