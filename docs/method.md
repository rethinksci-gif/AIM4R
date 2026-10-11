---
layout: default
title: 选题标准与信息源 · Method & Sources
lang: zh
---

<div class="method-page" markdown="1">

## 这个雷达为谁服务

面向有材料化学、实验放大、质量工程与工业研发背景的材料工程师。当前重点是聚合物与再生塑料，长期方向是 Material Intelligence：用数据和 AI 让研发决策更快、更可靠。每期帮助读者判断四件事：**什么值得读、证据支持到哪里、与我的问题有什么关系、下一步验证什么。**

长期选源的大致比例（不是每期配额）：

| 方向 | 长期占比 |
| --- | --- |
| AI × 材料与聚合物研发 | 35% |
| AI × 实验自动化与制造闭环 | 30% |
| 数据上下文、验证、不确定性与可信决策 | 20% |
| 可迁移方法、开源工具及相关机器人技术 | 15% |

## 两步筛选

**第一步：入选条件**（任一不满足即排除）

1. 有明确的领域关联，或可以讲清楚机制的方法迁移价值。
2. 有新增事实、方法、结果或有实质内容的分析。
3. 核心信息可追溯到原始来源；纯宣传、重复报道和无法追溯的内容不入选。

通用模型发布、排行榜、融资、财经和前端开发新闻默认排除。机器人内容只有在关联实验操作、检测、分选、制造，或有明确方法迁移价值时才入选。

**第二步：多维评价**（每个维度都附理由）

| 维度 | 权重 | 说明 |
| --- | --- | --- |
| 相关性 | 30% | 低于 5 分直接排除，不能被其他维度补偿 |
| 证据质量 | 25% | 按内容类型使用不同标准；仅有摘要时有上限 |
| 方法可迁移性 | 20% | 迁移条件是否清楚 |
| 工业适用性 | 15% | 只看来源报告的规模、过程数据和约束，不推算成本或碳排 |
| 新增信息量 | 10% | 相对已知工作的增量 |

加权分只用于内部排序。研究价值高但工业适用性低的内容进入**探索栏目**。每日主刊最多 3 条、探索最多 1 条，可以为零；没有合格内容时不发布当日期次，并在首页“最近运行状态”中显示“无合格内容”，与“采集失败”“处理失败”明确区分。

## 证据标注

每条精选都保留一份结构化证据记录，中英文版本由同一份记录生成：

- **实际访问级别**：已读全文 / 仅读到摘要 / 仅片段 / 仅标题，由程序根据实际获取路径判定，不由模型自报。论文类来源只有在读到正文章节时才算全文。
- **来源性质**：预印本、期刊论文、研究机构/企业研究博客、行业媒体、开源代码等；以及它是原始证据、发现线索还是评论分析。
- **同行评审状态、验证环境（仿真/实验室/中试/生产）与独立复现**分开记录：同行评审不等于工业验证，多家转载不等于独立证据。
- **材料体系、数据规模、批次、条件、比较基线、验证方法、结果与局限**：来源没写的标为“未报告”，不推算 TRL、成本或碳排。
- **发布日期、事件日期与收录日期**分开显示，旧材料被重新发现不会被当作新闻时间。

**自动检查只是引用一致性检查**：核对原文摘录能否在已读文本中逐字找到，以及正文里的数字是否都出现在证据记录中。它不是事实核验。搜索引擎结果只作为线索，不会被标为已核验原文。

## 运行节奏

- 每天运行一次（UTC 22:00，北京时间次日 06:00），全局回看 48 小时，arXiv 等存在公告延迟的来源单独回看 96–120 小时。
- 跨期去重由历史账本完成：已发布或已筛查的条目不再重复出现；arXiv 不同版本视为同一篇。
- 运行失败不写入账本，重跑会重新处理；同一天已发布后重跑不会覆盖当期内容。

## 信息源

以下来源均于 2026-10-11 用 `scripts/check_sources.py` 实测（HTTP、解析、日期、正文长度、关键词过滤后的数量、原文可读性）。“过滤后/周”为最近 7 天通过主题关键词预筛的条目数。

| 来源 | 角色 | 主题 | 内容获取 | 过滤后/周 | 限制 |
| --- | --- | --- | --- | --- | --- |
| [arXiv API · AI for materials & polymers](https://export.arxiv.org/api/query) | 原始证据（预印本） | AI × 材料 | Atom 摘要；入围后读 arXiv HTML 全文 | 11 | 以机器学习势函数为主；部分论文无 HTML 版，仅摘要 |
| arXiv API · Autonomous experiments & experiment design | 原始证据（预印本） | 实验自动化 | 同上，叠加本地关键词组 | 4 | 检索词宽，依赖关键词组二次过滤 |
| arXiv API · Manufacturing process, inspection & sorting | 原始证据（预印本） | 制造闭环 | 同上 | 4 | 含少量控制理论等边缘内容，由入选条件排除 |
| arXiv API · Uncertainty, shift & provenance | 原始证据（预印本） | 数据可信 | 同上 | 6 | 同上 |
| [npj Computational Materials](https://www.nature.com/npjcompumats.rss) | 原始证据（期刊） | AI × 材料 | RSS 简介；原文页可得摘要 | 6 | 正文未在静态页面中提供，标为“仅摘要” |
| [Nature Communications · Materials science](https://www.nature.com/subjects/materials-science/ncomms.rss) | 原始证据（期刊） | AI × 材料 | RSS 仅标题；原文页可得摘要 | 2 | 同上；按机器学习关键词预筛 |
| [Nature Machine Intelligence](https://www.nature.com/natmachintell.rss) | 原始证据（期刊） | 可迁移方法 | RSS 摘要 | 0 | 产出低，仅保留材料/实验相关 |
| [Matter](https://www.cell.com/matter/inpress.rss) | 原始证据（期刊） | AI × 材料 | RSS 摘要 | 0 | 产出低 |
| [Patterns](https://www.cell.com/patterns/inpress.rss) | 原始证据（期刊） | 数据可信 | RSS 摘要 | 0 | 产出低 |
| [npj Materials Degradation](https://www.nature.com/npjmatdeg.rss) | 原始证据（期刊） | AI × 材料 | RSS 摘要 | 0 | 产出低，仅保留聚合物/预测相关 |
| [Microsoft Research Blog](https://www.microsoft.com/en-us/research/feed/) | 原始证据（企业研究博客） | 可迁移方法 | RSS 全文 | 0 | 企业内容，需对照论文 |
| [Google DeepMind Blog](https://deepmind.google/blog/rss.xml) | 原始证据（企业研究博客） | 可迁移方法 | RSS 仅标题；页面提取 | 0 | 企业内容，需对照论文 |
| [NIST News](https://www.nist.gov/news-events/news/rss.xml) | 原始证据（研究机构） | 数据可信 | RSS 简介 | 0 | 产出低 |
| [The Robot Report](https://www.therobotreport.com/feed/) | 发现线索（行业媒体） | 制造闭环 | RSS 全文 | 4 | 人形机器人等内容由入选条件排除 |
| [Plastics Today](https://www.plasticstoday.com/rss.xml) | 发现线索（行业媒体） | 制造闭环 | RSS 简介 | 3 | 原文页对程序访问返回 403，只有片段 |
| GitHub releases：[BayBE](https://github.com/emdgroup/baybe)、[BoTorch](https://github.com/meta-pytorch/botorch)、[Ax](https://github.com/facebook/Ax) | 原始证据（开源代码） | 可迁移方法 | Release notes | 低频 | 版本说明通常较短，只有重要版本可能入选 |

**候选来源（未接入，不冒充已接入）**

| 来源 | 未接入原因 |
| --- | --- |
| ACS 期刊 RSS（Chem. Mater.、Macromolecules 等） | 对程序访问返回 403 |
| RSC Digital Discovery RSS | 本环境 TLS 连接被重置，未能验证 |
| ChemRxiv 公共 API | 返回 403；且为 JSON 接口，需要专用采集器 |
| ScienceDirect 期刊 RSS（Polymer、J. Manufacturing Systems、Resources, Conservation & Recycling） | 条目没有发布日期，只有卷期日期；需要“首次收录”日期策略后再接入 |
| Springer J. Intelligent Manufacturing 检索 RSS | 返回 HTML 而非 RSS |
| Recycling Today RSS | 首次请求正常，随后返回反爬验证页 |
| Resource Recycling（塑料频道） | Feed 为空 |
| Google News 关键词检索 | 链接为跳转地址，难以获取原文，只适合作线索 |

**编辑参考（不作为素材库）**：Import AI、The Batch、Interconnects、SemiAnalysis、Asimov Press——参考其讲研究意义、机制、专业取舍、产业约束与替代方案的写法，不对其内容做二次摘要。

---

## In English (short)

AIM4R is a research radar for materials R&D engineers: at most three picks per day (plus one exploration pick), zero on quiet days. Items pass three admission gates (domain link or explainable transfer, new information, traceable to an original), then five weighted dimensions (relevance 30% with a non-compensable floor, evidence 25%, transferability 20%, industrial applicability 15%, novelty 10%). Each pick carries one evidence record shared by both languages, with access level determined by code (full text vs. abstract only), source type, peer-review status, validation setting and replication recorded separately, and "not reported" where the source is silent. Automatic checks are citation-consistency checks (excerpts and numbers traceable to the text that was read), not fact-checking. Sources and candidates are listed above with their verification results.

</div>
