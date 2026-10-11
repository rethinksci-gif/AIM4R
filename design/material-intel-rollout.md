# AIM4R → Material Intelligence 研究雷达：本轮改造说明（2026-10-11）

分支：`feat/material-intelligence-radar`。未合并、未部署、未触发生产任务、未调用付费模型 API。

## 1. 核实出的根因

| 现象 | 核实结果 | 证据 |
| --- | --- | --- |
| 首页写“机器人/具身智能/材料”，内容却是通用 AI/财经 | **属实**。Actions 执行 `cp data/config.github.json data/config.json`，用的是 HN、Reddit、Telegram、CNBC、vLLM、LWN 等源 + `tech-news`/`finance-news` profile。仓库里偏材料的 `data/config.json`（168h、arXiv 材料类）从未被线上使用 | `.github/workflows/daily-summary.yml`；gh-pages 上 09-21/09-28/10-05 三期全部为通用科技/财经条目 |
| 评分面向软件/AI 读者 | **属实**。`profiles/tech-news/analysis.md` 的评估目标是 software engineering / AI / industry | — |
| RSS 优先 summary | **属实**。`_extract_content` 先取 `summary`，`content:encoded` 排最后；且保存的是 HTML | `src/scrapers/rss.py` |
| 分析只看前 1000 字 | **属实**。`tech-news` 未配置 `content`，默认 `analysis_max_chars=1000`、`prefix` 截断 | `src/processing/profiles.py` |
| 搜索补充只返回摘要 | **属实**。`web_search` 是 DDG 片段（3 条），被当作“参考链接”展示 | `src/processing/tools.py` |
| 每周跑一次只抓 24 小时 | **属实**。cron `0 23 * * 0` + `--hours 24`，约 6/7 的时间窗口从未采集；无任何跨期记录（`seen.json` 在 .gitignore 里但代码从未使用） | workflow、`src/storage/manager.py` |
| 重复/异常引用、`&\#x27;`、中英混杂 | **属实**。`html.escape(quote=True)` 把 `'` 变成 `&#x27;`，随后 Markdown 转义把 `#` 变成 `\#`；引用不按 URL 去重、不清洗标题、无 URL 的条目也保留；标签直接输出英文分析标签；中英文两次独立生成，没有共享事实 | 10-05 期 “Why don&\#x27;t…”、重复的 nonobench 链接、“Multiagent Systems - arXiv” |
| 无跨条目判断/跨期跟踪 | 属实（本轮只做跨期去重，跟踪列入下一阶段） | — |
| 另：来源故障与“无内容”无法区分 | **新发现**。单个 RSS 源失败被吞掉，表现为“0 条”；空日页面建议“降低阈值” | `RSSScraper._fetch_feed` |
| 另：arXiv HTML 中的数字丢失 | **新发现**。正文数字在 MathML 中，trafilatura 抽取时丢弃（“accuracy ( versus macro-)”） | 本轮实测 2610.06973 |

配置区分：仓库默认 `data/config.example.json`（未改）；Actions 原用 `data/config.github.json`（未改，保留为旧版通用简报配置）；本地 `data/config.json`（私人配置，**未改动**）。新版使用新增的 `data/config.material-intel.json`。工作区里未跟踪的 `projects/` 目录未触碰。

## 2. 实际修改

**引擎（通用能力，不含材料业务逻辑）**

- `src/processing/profiles.py`：profile 可声明 `rubric`（入选门槛、加权维度、不可补偿的维度下限、探索栏目规则）、`topics`（读者可见的主题导航）、`evidence`（证据抽取阶段）。
- `src/processing/rubric.py`：模型只给出各门槛/维度的判断与理由，加权分、下限、轨道（main/explore/rejected）由代码计算。
- `src/ai/prompting/analysis.py`、`src/ai/analyzer.py`：rubric 输出契约；向模型说明来源性质与实际访问级别。
- `src/scrapers/rss.py`：取 `content` 与 `summary` 中更完整者并转为纯文本；实体解码；页面抽取只有更长时才替换；关键词组预筛（零成本）；单源回看窗口；单源失败上报；HTML 反爬页视为失败；arXiv API 请求间隔 3 秒。
- `src/extractors/trafilatura.py`：抽取前用 MathML `alttext` 还原公式中的数字。
- `src/processing/evidence.py`：访问级别由代码判定（论文类需看到正文章节才算全文）；arXiv 全文入口；跨期 URL 键（去版本号、去追踪参数）；摘录逐字定位、数字溯源、中文夹杂英文从句检测、跨块重复句删除、引用去重与标题清洗。
- `src/ai/evidence.py`：入围条目读取原文（仅在提升访问级别时采用）；一次性抽取语言中立的证据记录；访问级别、来源性质、评审状态、日期由代码填写，模型不能覆盖；无法定位的摘录、含原文没有的数字的字段/结果被删除并记录。
- `src/ai/enricher.py`：写作校验（数字须在证据记录中、禁用空话、中文不得夹带英文整句），不通过则带错误信息重写一次，仍不通过则该条不发布。
- `src/ai/research_renderer.py`：新版期次渲染（HTML 卡片、全部转义）。
- `src/storage/history.py`：跨期账本与运行状态。
- `src/orchestrator.py`：`digest.renderer: "research"` 时走新流程；单源失败汇总；`track_limits`（上限而非配额）；入围候选读原文后再评；明确的运行状态。
- `src/ai/summarizer.py`：修复 `&\#x27;`（旧版渲染同样受益）。

**内容与配置**：`profiles/material-intel/`（match/analysis/evidence/enrichment 提示词与 rubric）；`data/config.material-intel.json`；`.github/workflows/daily-summary.yml`（每日、历史账本恢复与回传、失败也发布状态但任务仍标红）；`scripts/daily-run.sh`。

**网站**：`docs/index.md`（新定位、最新一期精选与理由、主题浏览、运行状态、旧期标注）、`docs/method.md`（选题标准、证据标注、信息源与候选）、`docs/_layouts/default.html`（导航、预览横幅）、CSS/JS。旧期 URL（`/YYYY/MM/DD/summary-{lang}.html`）、`feed-zh.xml`/`feed-en.xml` 不变。

**工具与测试**：`scripts/check_sources.py`、`scripts/preview_site.py`、`scripts/build_preview_edition.py`、`tests/test_material_intel.py`（34 项）、`tests/fixtures/material_intel/`（均为 MOCK）。

## 3. 前后对比：历史三期 18 条

历史生成文本不作事实依据，以下只判断“是否值得进入新雷达”。

| 期次 | 条目 | 旧分 | 新判定 | 理由 |
| --- | --- | --- | --- | --- |
| 10-05 | 开发者为何不用“平台”（Web 框架之争） | 7.0 | 排除 | 无领域关联、无方法迁移；前端讨论 |
| 10-05 | Nonobench：49 个 LLM 数织基准 | 7.0 | 排除 | 通用模型排行榜，Reddit 自述，无研发关联 |
| 10-05 | VeriHarness 长程任务验证 | 7.0 | 排除（边缘） | “用证据核对智能体输出”对未来自主实验有启发，但条目未给出可说明的迁移机制；来源是 Telegram 转述 |
| 09-28 | 澳参议院传唤 OpenAI/Anthropic CEO | 8.0 | 排除 | 政策新闻 |
| 09-28 | SemiAnalysis 中国数据中心容量 | 8.0 | 排除 | 算力/资本新闻 |
| 09-28 | Simon Willison 回顾 LLM 进展 | 7.0 | 排除 | 通用模型综述 |
| 09-28 | ClashRoyaleAi 强化学习模拟器 | 7.0 | 排除 | 游戏 RL，无迁移路径 |
| 09-28 | 波音 737 MAX 自动导航缺陷 | 7.0 | 排除 | 航空软件新闻，转载来源 |
| 09-28 | 美债收益率与 AI 基础设施借债 | 8.0 | 排除 | 财经 |
| 09-21 | AI 编造情报险致美军拦截 | 8.0 | 排除 | 安全/政策新闻 |
| 09-21 | 三星 HBM4 产能翻倍 | 7.0 | 排除 | 半导体产能新闻 |
| 09-21 | Qwen Image 2.1 发布 | 7.0 | 排除 | 普通模型发布 |
| 09-21 | Pirate Face 用 BT 保存模型 | 7.0 | 排除 | 无关 |
| 09-21 | 西班牙屏蔽 Archive.today | 7.0 | 排除 | 无关 |
| 09-21 | 去污染报告无法修复基准污染 | 7.0 | 排除（边缘） | 训练/测试泄漏问题与材料数据划分相通，但为 Reddit 讨论，不可追溯到原始研究 |
| 09-21 | 长鑫 DRAM 量产 | 7.0 | 排除 | 产业新闻 |
| 09-21 | 关税、燃料与利率挤压企业 | 7.0 | 排除 | 财经 |
| 09-21 | 迪士尼+ 插广告 | 7.0 | 排除 | 无关 |

结论：0/18 保留，2 条边缘。这些条目的来源均不在新配置中，且无法通过新配置的关键词预筛。旧版问题不在单条判断，而在选源。对照：编辑预览期（同一周的真实来源）中，3 条中有 2 条进入主刊、1 条进入探索。

## 4. 本地预览

- 编辑预览期：`docs/_previews/2026-10-11-summary-{zh,en}.md`。由编辑（Claude）依据实际读到的原文手写，`preview: true`，页面顶部有“编辑预览 · 非正式发布”横幅。`docs/_previews/` 被 Jekyll 排除，合并后也不会发布。三条均为真实来源：arXiv 2610.06973（全文）、npj Comput. Mater. 10.1038/s41524-026-02357-7（仅摘要）、arXiv 2610.04134（全文，仿真）。
- 生成方式：`scripts/build_preview_edition.py --fetch` 重新读取原文，并用生产代码重算访问级别、证据记录与写作校验：10 条摘录全部逐字定位，数字全部溯源，任何一项失败都会中止构建。
- 站点预览（近似 Jekyll，非 GitHub Pages 实际构建）：

```bash
uv run --with "python-liquid<2" --with pyyaml python scripts/preview_site.py \
  --out /tmp/aim4r-site --gh-pages-posts --extra-posts docs/_previews \
  --data docs/_previews/aim4r_history.preview.json
python -m http.server -d /tmp/aim4r-site 8000   # http://localhost:8000/AIM4R/
```

无头 Chromium 检查了首页、预览期（中/英）、旧期、方法页，宽度 1440 与 390：均无横向溢出、无脚本错误；语言切换与中英对应链接正常。运行状态条用 `tests/fixtures/material_intel/history_states.mock.json`（MOCK）检查了 7 种状态的区分显示。

## 5. 测试

`pytest`：**524 passed**（原有 490 项 + 新增 34 项），在按 `uv.lock` 构建的环境中运行（本地 `.venv` 与锁文件不一致：mcp 2.x、anthropic 新版，原有测试在该环境下本来就有 4 项失败或无法收集，与本次改动无关）。

新增测试覆盖：通用热门新闻被门槛或关键词预筛排除；低相关性不能被高分补偿；材料研究进入主刊；跨领域方法进入探索栏目且有独立门槛；只有摘要时不标为全文（包括长落地页）；缺失数字/字段不补写，模型自报的访问级别与评审状态被忽略；无法定位的摘录被删除；中英文由同一证据记录生成，各自数字都在记录内，编造数字触发重写，持续编造则不发布；重复链接、无效标题、无 URL 引用被清理；arXiv 版本与追踪参数的跨期去重；同日重跑不覆盖；无合格内容、来源全部失败、部分来源失败、AI 故障四种状态分别记录；轨道上限不是配额；渲染转义与 `&#x27;` 回归。

## 6. 信息源

已验证接入 15 个 RSS/Atom 源与 3 个 GitHub release 源，未接入的候选 8 个，详见 `docs/method.md`（含实测数据与限制）。`scripts/check_sources.py --probe-pages` 可随时复验。

## 7. 仍未验证的环节

1. **真实模型的判断质量**：没有调用 DeepSeek（或任何付费 API）。门槛/评分/证据抽取/写作的提示词只用脚本化的假模型测试了“引擎是否正确执行规则”，没有验证模型是否会给出合理的判断与文字。
2. **GitHub Pages 的真实 Jekyll 构建**：本地预览用 python-liquid 近似；kramdown 与 Python-Markdown 在个别 HTML/Markdown 混排处可能不同（`method.md` 用了 `markdown="1"`）。
3. **GitHub Actions 中的完整运行**：历史账本恢复、失败后仍发布状态、`hashFiles` 条件等，未在 Actions 上实跑。
4. **GitHub Actions 出口 IP 下的来源可达性**：本地可用的 Nature、Cell、arXiv 等在 Actions 上可能被限流；RSC 在本地 TLS 失败、Actions 上未测。
5. DeepSeek 对较长证据记录 + 中文写作约束的遵循程度、重写率与成本未测；关键词预筛后约每周 40 条进入分析，估算每日调用量很小，但未实测。

## 8. 正式启用步骤

1. 审阅 draft PR；必要时调整 `profiles/material-intel/*.md` 中的读者描述与门槛措辞。
2. 确认仓库 Secrets 中有 `DEEPSEEK_API_KEY`（新工作流只用它和内置的 `GITHUB_TOKEN`）。
3. 在本地用真实 key 做一次**不发布**的试跑并人工审读：
   ```bash
   export DEEPSEEK_API_KEY=...        # 不要提交
   uv run horizon --config data/config.material-intel.json --log-level INFO
   # 输出：docs/_posts/<今天>-summary-{zh,en}.md 与 docs/_data/aim4r_history.json（均被 .gitignore 忽略）
   uv run --with "python-liquid<2" --with pyyaml python scripts/preview_site.py --out /tmp/aim4r-site --gh-pages-posts --data docs/_data/aim4r_history.json
   ```
   检查：入选条目是否合理、访问级别是否诚实、数字是否与原文一致、中文是否通顺。试跑后删除本地 `docs/_data/aim4r_history.json`，避免把试跑标记为“已处理”。
4. 合并 PR。首次定时运行（UTC 22:00）会从空账本开始；如需立即验证，可在 Actions 页手动 `workflow_dispatch`。
5. 第一周每天看一眼首页“最近运行状态”和 Actions 结果，并用 `scripts/check_sources.py` 复验来源。
6. 旧版通用简报配置 `data/config.github.json` 保留，如需回退，把工作流的 `--config` 改回并恢复 `--hours`。

## 9. 下一阶段（最小实现建议）

- **跨期研究主题追踪**：在账本 `items` 中已有 `topic`/`track`/`issue` 字段的基础上，增加 `threads`（主题线索 → 相关条目键列表）。每周由一次模型调用把本周精选归入已有线索或新建线索；首页按线索展示时间线。
- **每周综合判断**：每周日从账本读取本周精选的证据记录（不读生成文本），生成一页“本周什么改变了判断、什么仍未被证明”，复用同一套数字溯源与禁用词校验。
- **读者反馈学习**：每条卡片加“有用/无关/证据不足”三个按钮（GitHub Issues 预填链接即可，无需后端），每月人工把反馈汇总进 `analysis.md` 的校准段落，而不是自动调权重。
- 来源：为 ScienceDirect 类无日期源实现“首次收录”日期策略；为 ChemRxiv 写专用 JSON 采集器；在 Actions 上复验 RSC。
