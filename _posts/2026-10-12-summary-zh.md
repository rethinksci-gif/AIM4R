---
layout: "default"
title: "AIM4R 研究雷达 · 2026-10-12"
date: "2026-10-12"
lang: "zh"
edition: "research-radar"
issue_status: "published_degraded"
description: "本期精选 1 条，来自 21 条新内容（本轮共采集 45 条）。其中 1 条列入探索栏目。"
picks_count: 1
failed_sources: ["npj Computational Materials", "Nature Communications · Materials science", "Nature Machine Intelligence", "npj Materials Degradation"]
picks: [{"anchor": "pick-1", "title": "钙钛矿光伏ML评估改用来源分组划分", "why": "如果你用随机划分评估钙钛矿电池的机器学习模型，这份摘要给出了一个警示：高分可能只反映模型记住了历史配方，而不是学到了物理规律。", "topic": "data-trust", "topic_name": "数据上下文、验证与可信决策", "track": "explore", "source_kind": "preprint", "access": "abstract_or_summary", "url": "https://arxiv.org/abs/2610.12766v1"}]
---

<p class="issue-lede">本期精选 1 条，来自 21 条新内容（本轮共采集 45 条）。其中 1 条列入探索栏目。</p>

<nav class="reading-guide" aria-labelledby="reading-guide-title"><h2 id="reading-guide-title">本期阅读指南</h2><p>按研发问题选择原文；先看证据边界，再决定是否验证。</p><ol><li><a href="#pick-1">钙钛矿光伏ML评估改用来源分组划分</a><span class="guide-context">数据上下文、验证与可信决策 · 仅读到摘要 · 探索栏目</span><p>如果你用随机划分评估钙钛矿电池的机器学习模型，这份摘要给出了一个警示：高分可能只反映模型记住了历史配方，而不是学到了物理规律。</p></li></ol></nav>

<p class="issue-warning" role="note">注意：本次有 4 个来源采集失败（npj Computational Materials, Nature Communications · Materials science, Nature Machine Intelligence, npj Materials Degradation），覆盖可能不完整。</p>

<h2 id="explore">探索栏目</h2>

<p class="track-note">研究价值较高、但离工业应用尚远的内容。</p>

<article class="pick" id="pick-1" data-track="explore">
<p class="pick-badges"><span class="badge" data-kind="kind" data-value="preprint">预印本</span><span class="badge" data-kind="access" data-value="abstract_or_summary">仅读到摘要</span><span class="badge" data-kind="review" data-value="preprint">未经同行评审</span></p>
<h3>钙钛矿光伏ML评估改用来源分组划分</h3>
<p class="pick-why"><span class="label">为什么值得读</span>如果你用随机划分评估钙钛矿电池的机器学习模型，这份摘要给出了一个警示：高分可能只反映模型记住了历史配方，而不是学到了物理规律。</p>
<p class="pick-actions"><a class="read-original" href="https://arxiv.org/abs/2610.12766v1">阅读原文 ↗</a><span class="pick-meta">arXiv · Uncertainty, shift &amp; provenance in materials/process data · 发布 10月8日 · 收录 10月12日</span></p>
<div class="pick-body">
<h4 data-block="advance">新增进展</h4>
<p>相对常规的随机数据划分，作者提出按机构来源分组的划分层级，依次隔离重复器件、同一出版物与同一机构。其目标是以此替代随机划分——摘要称随机划分主要在奖励对历史配方的记忆；具体指标、模型结构与实现细节未在摘要中给出。</p>
<h4 data-block="evidence">关键证据</h4>
<p>材料体系为钙钛矿太阳能电池（含吸收层化学），数据来自 Perovskite Database（规模未报告），共基准测试13个模型，对照为随机划分。摘要报告的关键结果有三点：近三分之二的已整理器件与另一器件共享完全相同的配方；树集成模型在随机划分上占优，但在真正未见的机构和未来发现上排名崩塌，此时成分感知的神经网络架构表现更好；特征重要性显示器件结构与制备方法对最终效率的影响与吸收层化学相当。该记录仅读到摘要，属预印本，未经同行评审，验证为计算基准测试，实验或现场验证未报告。</p>
<h4 data-block="significance">研发意义</h4>
<p>对依赖历史配方库筛选新配方的团队，这份摘要提示随机划分下的高排名可能只说明模型复现了库内已知配方。编辑推断：在把模型用于候选配方排序前，先按机构或批次分组留出验证集，是成本较低的一道检查；该做法迁移到其他材料体系前，需要先为自己的数据集补上来源标注。</p>
<h4 data-block="boundaries">适用边界</h4>
<p>摘要未报告任何定量性能指标、误差或不确定性，也未给出数据库规模、模型架构与特征集，且无独立复现、无批次或供应商层面的验证、无实验验证。由于只读到摘要，无法判断这些测试是没有做，还是仅未在摘要中报告；分组划分能否在其他材料数据库上成立，取决于该库是否具备可追溯的机构来源字段。</p>
<h4 data-block="next_step">下一步</h4>
<p>可向作者索取各划分下13个模型的逐项指标，并确认“重复配方”的判定标准。编辑建议：在自己的数据集上按机构分组留出一组做对比，看随机划分与分组划分的排名差异是否同样出现。</p>
</div>
<details class="pick-evidence"><summary>证据记录</summary><p class="evidence-hint">字段与摘录保留原文语言，按来源报告填写。</p><dl><dt>材料体系</dt><dd lang="en">perovskite solar cells; absorber chemistry</dd><dt>数据规模</dt><dd lang="en">Perovskite Database (size not reported); thirteen models benchmarked</dd><dt>批次/批号</dt><dd class="missing">未报告</dd><dt>条件</dt><dd lang="en">Evaluation depends on random data splits versus grouped splits that progressively isolate duplicate devices, publications, and institutions; results are reported for random splits, genuinely unseen institutions, and future discoveries.</dd><dt>比较基线</dt><dd lang="en">Random data splits (typical evaluation); tree ensembles on random splits as comparison point for composition-aware neural architectures.</dd><dt>验证方法</dt><dd lang="en">Benchmarking against random splits and a hierarchy of grouped splits that progressively isolate duplicate devices, publications, and institutions, including genuinely unseen institutions and future discoveries.</dd><dt>验证环境</dt><dd class="missing">未报告</dd><dt>独立复现</dt><dd class="missing">未报告</dd><dt>事件日期</dt><dd class="missing">未知</dd></dl><p class="evidence-sub">原文摘录</p><ol class="quotes"><li><q lang="en">Machine-learning models for perovskite solar cells are typically evaluated using random data splits, which we show systematically leak information through massive internal duplication.</q> <span class="quote-loc" lang="en">— abstract</span></li><li><q lang="en">Because nearly two-thirds of curated devices share their exact recipe with another, random splits primarily reward the mere recall of historical data rather than testing true physical generalisation.</q> <span class="quote-loc" lang="en">— abstract</span></li><li><q lang="en">To solve this, we mapped the institutional provenance of the Perovskite Database and established a rigorous hierarchy of grouped splits that progressively isolate duplicate devices, publications, and institutions.</q> <span class="quote-loc" lang="en">— abstract</span></li><li><q lang="en">while tree ensembles dominate random splits by recognising familiar recipes, their ranking collapses on genuinely unseen institutions and future discoveries, where composition-aware neural architectures excel.</q> <span class="quote-loc" lang="en">— abstract</span></li><li><q lang="en">Furthermore, feature importance demonstrates that the device architecture and fabrication methodology dictate final efficiency just as strongly as the absorber chemistry.</q> <span class="quote-loc" lang="en">— abstract</span></li></ol><p class="check-note">自动检查（引用一致性，不是事实核验）：5 条摘录可在已读文本中定位。</p></details>
</article>
