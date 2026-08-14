---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 49 条内容中筛选出 23 条重要资讯。

---

**科技新闻**
1. [GLM-5.3：前沿编码与新兴网络能力](#item-tech-news-1) ⭐️ 9.0/10
2. [Spaghettifying DRAM：新型内存特权访问攻击](#item-tech-news-2) ⭐️ 9.0/10
3. [谷歌发布 Gemini 3.7 Flash，定价与性能引发社区热议](#item-tech-news-3) ⭐️ 8.0/10
4. [Cerebras 与 OpenAI 推出 GPT-5.6 Sol Ultrafast，宣称近 7 倍加速](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek Harness 开发者预览：可追溯 AI Agent 框架](#item-tech-news-5) ⭐️ 8.0/10
6. [理解是新的瓶颈](#item-tech-news-6) ⭐️ 8.0/10
7. [选择无聊技术：用创新代币管理技术风险](#item-tech-news-7) ⭐️ 8.0/10
8. [systemd-journald 单行日志造成 49KB 以上磁盘写入](#item-tech-news-8) ⭐️ 8.0/10
9. [AI 机器人实验室年测 300 万人体组织，有望淘汰动物测试](#item-tech-news-9) ⭐️ 8.0/10
10. [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](#item-tech-news-10) ⭐️ 8.0/10
11. [Bluesky 发布协议服务，Jetstream 简化 Firehose 接入](#item-tech-news-11) ⭐️ 7.0/10
12. [Pi 上下文压缩机制解析](#item-tech-news-12) ⭐️ 7.0/10
13. [657607 条链接追踪：旧网页为何消失](#item-tech-news-13) ⭐️ 7.0/10
14. [City2Graph：面向城市系统的异构图神经网络 Python 库](#item-tech-news-14) ⭐️ 7.0/10
15. [worldproof：像素指标无法排名世界模型](#item-tech-news-15) ⭐️ 7.0/10
16. [X 扩大算法开源，推出排名透明度工具](#item-tech-news-16) ⭐️ 7.0/10
17. [苹果提交美国 App Store 外部购买抽成方案：最高 15%](#item-tech-news-17) ⭐️ 7.0/10
18. [美国法官责令谷歌取消第三方应用商店安装障碍](#item-tech-news-18) ⭐️ 7.0/10

**财经新闻**
1. [标普 500 成分股第二季度净利润率创新高至 16.9%](#item-finance-news-1) ⭐️ 8.0/10
2. [美国宣布对部分进口无人机加征最高 100%关税](#item-finance-news-2) ⭐️ 8.0/10
3. [盘前个股异动：Reddit 涨 12%、应用材料跌超 5%、Workday 传收购谈判](#item-finance-news-3) ⭐️ 7.0/10
4. [比尔·阿克曼再度建仓 Netflix，称其赢得流媒体战争](#item-finance-news-4) ⭐️ 7.0/10
5. [《大空头》投资者史蒂夫·艾斯曼指出 AI 热潮的致命弱点](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.3：前沿编码与新兴网络能力](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.AI 发布了前沿编码模型 GLM-5.3，并宣称其具备新兴的网络能力，包括大规模漏洞发现。这一能力使模型能够自动扫描并可能披露广泛软件中的安全漏洞，引发了对 AI 在网络安全领域应用的广泛讨论。社区对模型的实际性能、漏洞披露流程以及中国与美国在 AI 监管上的差异展开了激烈辩论。目前模型的具体技术细节、发布时间和基准数据尚未公布，仍需进一步验证。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**「背景」** GLM-5.3 是由中国 AI 公司 Z.ai 推出的开源大语言模型，聚焦编码与智能体能力，并宣称在网络安全方面具备更强能力。根据官方介绍，该模型主要依靠扩展后训练（post-training scaling）以及真实世界专家工作流来提升性能，而不是单纯扩大预训练规模；它相对于前代 GLM-5.2 在内部 Code Bench 编码基准上的成绩提升了约 50%。这波进展属于开源大模型在编码和自主智能体方向上的持续竞争，而模型具备的大规模漏洞发现与扫描能力也引起了社区对 AI 安全影响的关注。

**「影响」** 据社区反馈，GLM-5.3 基于与 GLM-5.2 相同的基础模型、仅通过后训练获得增强，已用于大规模扫描开源和流行软件并披露漏洞，可能让维护者收到更多高危 CVE 报告，同时降低漏洞发现的成本；不过这些披露尚未获得官方完全证实，具体影响取决于正式发布后的实际部署。

**「社区讨论」** 社区评论中，有用户指出 GLM-5.3 似乎正在大规模扫描开源和流行软件，并通过 cvd.z.ai 披露大量仍处于 embargo 期的 CVE，其中很多被评为严重或高危，这引发了关于漏洞披露成本和 Anthropic Project Glasswing 的讨论；也有用户认为其性能仍略逊于 Sol、Fable 和 Mythos 5 等模型，但差距很小，还有人赞赏 Z.AI 的博客写作风格接近研究者而非营销文案。另有评论讨论了中美在 AI 网络能力监管上的差异及其地缘政治影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=2uEunHawjIU">GLM - 5 . 3 : Frontier Coding with Emergent Cyber Capabilities</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM - 5 . 3 - Overview - Z . AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://theunum.io/en/news/read/chinese-startup-z-ai-has-introduced-the-glm-53-language-model-for-programming">Chinese startup Z ai has introduced the GLM - 5 . 3 language model for...</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM - 5 . 3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#Cybersecurity`, `#Software Engineering`, `#LLM`

---

<a id="item-tech-news-2"></a>
### [Spaghettifying DRAM：新型内存特权访问攻击](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

该 GitHub 仓库介绍了一种被称为“Spaghettifying”的新型 DRAM 寻址技术，通过操纵 DRAM 寻址可获得特权级访问。README 展示了对 AMD Jaguar 架构的证明，并提到 Zen 3 的内存控制器寄存器基地址不同。这项研究来自知名硬件安全研究者，对游戏主机和服务器安全具有潜在影响。目前公开信息有限，尚未说明是否影响其他较新的处理器家族。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**「背景」** 这项研究针对的是 DRAM 控制器的地址转换逻辑，现代 CPU 依靠该逻辑在物理 DRAM 地址与控制器实际访问之间进行加扰和重映射。操作系统内核通常看不到某些保留内存区域（carveouts），其中存放着固件、管理引擎等敏感数据。研究者 Christopher Domas 展示了通过修改 DRAM 地址翻译，可以让受控地址落到任意物理内存位置，从而解锁这些隐藏区域；该技术已在 AMD Jaguar（约 2013 年的架构）上验证，并给出了 Zen 3 上内存控制器寄存器基地址不同的说明。

**「影响」** 在受影响的 AMD Family 16h（Jaguar）CPU 上，拥有 ring 0 权限的攻击者可以利用该技术访问通常隐藏在“负环”层级中的硬件功能，把系统控制权扩展到几乎全部 CPU 内部机制。由于 AMD 17h 及之后的处理器数据手册不再公开或确认 DRAM 控制器的翻译寄存器是否可锁定，该攻击在较新平台上的影响范围仍属未知。

**「社区讨论」** 社区评论对即将到来的 Black Hat 演讲表示期待，认为作者 Christopher Domas 的讲解非常出色；也有用户感叹现代 DRAM 复杂性和庞大攻击面，并质疑该攻击除 AMD Jaguar 外是否影响 Zen 3 或其他较新 CPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>
<li><a href="https://cybersecuritynews.com/dram-scrambling-attack/">New DRAM Scrambling Attack Exposes CPU’s Most Protected ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#hardware security`, `#exploit`, `#memory attack`, `#reverse engineering`

---

<a id="item-tech-news-3"></a>
### [谷歌发布 Gemini 3.7 Flash，定价与性能引发社区热议](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌推出新一代模型 Gemini 3.7 Flash，但发布信息仅指向 API 文档，未包含详细基准或规格。该模型的“介绍性定价”引发热议：价格计划在 2026 年 12 月 31 日翻倍，而距离上一代 3.6 Flash 发布仅三周。开发者实测显示，Gemini 3.7 Flash 在图像转 HTML 等视觉任务上表现良好，但仍逊于 Opus 5；同时社区要求与 Luna、Terra 等模型进行基准对比，认为定价和性能优势尚不明确。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**「背景信息」** Gemini 3.7 Flash 是 Google 于 2026 年 8 月 13 日发布的 Flash 系列最新模型，定位为面向编码和智能体（agent）工作流的“最强工作马”模型，距上一代 Gemini 3.6 Flash 发布仅三周。该模型上下文窗口为 100 万 token，定价为每百万输入 token 0.375 美元、每百万输出 token 1.875 美元。此次发布源于开发者反馈和算法创新，是 Flash 系列持续快速迭代的一部分。

**「影响」** 对 Gemini API 开发者而言，Gemini 3.7 Flash 已开始替换三周前发布的 3.6 Flash，因此调用旧版模型的请求会迁移到新版本，需重新验证推理输出和成本。官方基准表中，3.7 Flash 的表现随所选对比模型（Gemini 3.6 Flash、Claude Sonnet 5、GPT-5.6 Terra、Muse Spark 1.2）和指标行而异，而 OpenAI 的 GPT-5.6 Luna 定价仅 0.20/1.20 美元/百万 token，这让 Gemini 3.7 Flash 的性价比优势并不稳固。

**「社区讨论」** 社区主要争议集中在定价策略和竞品对比：有开发者认为 Luna 价格更低且性能更强，削弱了 Flash 系列的低成本定位；也有开发者分享图像转 HTML 等实测，认为 Gemini 3.7 Flash 在性价比上具备竞争力。同时，对“介绍性定价”三个月后翻倍的做法，多数评论表示难以理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/google/gemini-3.7-flash">Gemini 3.7 Flash - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://www.digitalapplied.com/blog/gemini-3-7-flash-vs-sonnet-5-gpt-5-6-terra-benchmarks">Gemini 3 . 7 Flash vs Sonnet 5 vs GPT - 5 . 6 Terra: Real Wins</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/google-announces-gemini-3-7-flash-just-three-weeks-after-previous-release/">Google announces Gemini 3 . 7 Flash just three weeks... - Ars Technica</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#AI model`, `#LLM`, `#pricing`

---

<a id="item-tech-news-4"></a>
### [Cerebras 与 OpenAI 推出 GPT-5.6 Sol Ultrafast，宣称近 7 倍加速](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras 与 OpenAI 宣布为 GPT-5.6 Sol 推出 Ultrafast 推理模式。其评估显示，Ultrafast 模式在 11 小时 11 分钟内答完 2500 道 HLE 问题，而 Claude Fable 5 需要 78 小时 27 分钟，即达到相近准确率的速度约为后者的 7 倍。该数据来自供应商，尚无第三方独立验证；官方尚未公布定价和面向普通用户的可用性，且未明确该模式与常规 GPT-5.6 Sol 在性能上是否完全一致。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**「背景」** OpenAI 与 Cerebras 于 2026 年 8 月联合预览“Ultrafast”服务层级，由 Cerebras 硬件驱动 GPT-5.6 Sol，生成速度最高可达每秒 750 个输出 token，较 Standard 处理快最多 14 倍，率先在 OpenAI API 中面向少量客户开放。此次发布标志着两家公司合作的实际进展，并引发外界对定价、可用性以及与常规版本是否完全一致等问题的关注。

**「影响」** 如果厂商声明经独立验证，Ultrafast 将大幅缩短前沿推理和长时间研究任务的等待时间，并让依赖反复迭代的推理工作流受益；但定价、开放范围与精度一致性仍未公开，实际影响尚待确认。

**「社区讨论」** 社区反响积极，部分评论认为更快推理能带来更多迭代修正，从而提升输出质量；但也有用户指出自己的 Pro 账户仅看到 Standard 和 Fast 档位、怀疑 UltraFast 短期内只面向企业用户，同时质疑官方未说明 Ultrafast 是否与常规 GPT-5.6 Sol 精度完全一致，且缺少定价信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>
<li><a href="https://explainx.ai/blog/openai-gpt-5-6-sol-ultrafast-cerebras-august-2026">GPT-5.6 Sol Ultrafast: 750 TPS on Cerebras, No Price Yet | explainx.ai ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM inference`, `#OpenAI`, `#Cerebras`, `#performance`

---

<a id="item-tech-news-5"></a>
### [DeepSeek Harness 开发者预览：可追溯 AI Agent 框架](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek Harness 的早期开发者预览版，这是一个采用 MIT 许可证的开源 AI 代理框架，核心特性是完整可追溯性和动态插件系统。该框架基于 Cordis v4，采用“一切皆插件”的架构，支持热加载、动态启用/禁用以及卸载时清理相关状态和副作用。模型看到的所有内容都会记录在仅追加的会话日志中，开发者可在轨迹视图中按来源检查系统提示、推理、工具调用、子代理调度和上下文注入，并支持恢复、分叉、搜索和重放。作者提醒当前只是早期预览，会存在许多粗糙之处和破坏兼容性的变更。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**「背景」** DeepSeek Harness（dsh）是 DeepSeek AI 推出的开源智能体（agent）运行时框架，目前以 MIT 许可证发布 v0.1 开发者预览版，旨在把 DeepSeek V4 系列模型变成能执行多步工作流和使用工具的自主编码智能体。它采用 Cordis v4 插件系统，支持插件热加载/卸载并在卸载时回滚状态和副作用；同时所有模型输入（系统提示、推理、工具调用等）都写入追加式会话日志，提供完整可追溯性。该项目仍处于早期阶段，官方明确表示会有兼容性破坏性变更。

**「影响」** 对希望构建可审计 AI 代理的开发者而言，现在可以在 MIT 许可下体验具备端到端可追溯会话和运行时插件动态管理能力的框架，但需要接受不稳定的接口和持续的破坏性变更。

**「社区讨论」** 社区反应积极而审慎：作者本人强调这仍是早期预览，欢迎反馈；有评论认为完整运行轨迹记录是“杀手级功能”，也有评论解释了 Cordis v4 与已在 Koishi 中使用的 Cordis v3 的关系，另有人对“一切皆插件”表达了插件疲劳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview : Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://cryptobriefing.com/deepseek-harness-open-source-developer-preview/">DeepSeek Harness v0.1 enters developer preview with open - source ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open source`, `#developer tools`, `#DeepSeek`, `#traceability`

---

<a id="item-tech-news-6"></a>
### [理解是新的瓶颈](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) ⭐️ 8.0/10

Geoffrey Litt 于 2026 年 7 月 2 日发表文章《Understanding is the new bottleneck》，提出理解代码已成为软件开发的新瓶颈，尤其是在大语言模型生成代码日益普及的背景下。文章认为，随着生成代码变得容易，程序员的主要挑战从编写代码转向理解现有代码的意图、行为和系统影响。这一观点引发了对程序理解工具和方法的广泛讨论，包括时间旅行调试、拉取请求描述生成等思路。文章获得了较高的社区参与度和实质性讨论，说明该主题在软件工程师和 AI 从业者中引起了强烈共鸣。

hackernews · sebg · 8月13日 18:47 · [社区讨论](https://news.ycombinator.com/item?id=49290299)

**「背景」** 随着大语言模型（LLM）越来越多地参与代码生成，软件开发的瓶颈正在从“编写代码”转向“理解代码”。Geoffrey Litt 在 2026 年 7 月的 AI Engineer 会议上发表了相关演讲，并撰写了同名文章。他提出，人类仍然需要理解智能体所编写的代码，这不仅是为了验证正确性，更是为了进行创造性协作。为此，他介绍了一些结合认知科学与现代智能体能力的技巧，包括生成个性化解释文档、以“文字化代码差异”的方式呈现变更，以及利用交互式“微世界”来帮助开发者深入理解复杂系统。

**「影响」** 这一观点促使软件工程师和 AI 辅助开发实践者重新聚焦于程序理解能力，而不仅仅是代码生成能力。实际经验显示，开发者仍然需要亲自理解代码以核实 LLM 生成的描述或代码是否正确，因此改进代码理解工具（如时间旅行调试）可能成为提升开发效率的关键方向。

**「社区讨论」** 评论区多数人认同理解代码是瓶颈，但对其“新”程度有分歧：有评论指出这在工程管理和程序管理中早已存在，并非新问题。同时，实际经验表明 LLM 生成的拉取请求描述普遍不受欢迎，因为它们过于机械且缺乏动机说明，而开发者仍需亲自理解代码以确认 LLM 没有出错。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html">Understanding is the new bottleneck - geoffreylitt.com</a></li>
<li><a href="https://aidotengineer.podhood.com/48d7e61f-305d-4bf8-9ac6-b7dcb1d9c5d6">Understanding is the new bottleneck — Geoffrey Litt, Notion</a></li>
<li><a href="https://www.youtube.com/watch?v=WkBPX-oDMnA">Understanding is the new bottleneck — Geoffrey Litt, Notion Understanding is the new bottleneck — Geoffrey Litt, Notion Understanding is the New Bottleneck in AI - startuphub.ai Understanding is the new bottleneck • Buttondown Understanding is the new bottleneck — Geoffrey Litt, Notion</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#code understanding`, `#LLMs`, `#developer tools`, `#program comprehension`

---

<a id="item-tech-news-7"></a>
### [选择无聊技术：用创新代币管理技术风险](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

丹·麦金利 2015 年的文章《选择无聊技术》提出，每家公司的创新能力就像数量固定的“创新代币”，大约只有三枚，应该把它们花在真正重要的地方，而其余大部分问题应优先采用成熟、可预测的“无聊技术”。文章认为，新技术虽然诱人，但其隐含的调试、运维和生态成本往往很高，而成熟技术能降低整体风险并释放出宝贵的创新空间。该文后来成为技术选型领域的经典，常被工程管理者用来向同事和上级解释取舍。在当前的 AI 代理时代，读者将其进一步延伸为“把创新代币集中在代理本身，而让代理周围的技术栈保持无聊”。

hackernews · tosh · 8月13日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49289512)

**「背景」** 丹·麦金利（Dan McKinley）在 2015 年发表的经典文章《选择无聊的技术》（Choose Boring Technology）提出，每个团队可用的“创新代币”（innovation tokens）数量有限，应当将这些代币花在真正的产品创新上，而不是用热门新数据库替换成熟的 PostgreSQL 之类的基础组件。所谓“无聊的技术”指成熟、可预测、已被广泛验证的解决方案，选择它们可以降低风险并节省创新预算，用于真正需要差异化的环节。这篇文章后来成为技术选型讨论中的经典参考。

**「影响」** 对于软件工程师和技术管理者而言，这篇文章提供了一个可操作的决策框架：通过限制同时引入的新技术数量、优先采用成熟方案，可以更清晰地权衡技术债与创新投入，并更容易向团队内外解释这些决策。在 AI 代理开发场景中，这一原则被进一步解读为应使用代理更擅长、更主流的技术栈，以降低整体不确定性。

**「社区讨论」** Hacker News 评论中，多数人表示“创新代币”概念对产品经理和工程领导非常有用，能帮助说明技术取舍；也有评论提出反驳，认为“创新代币”的设定显得随意且不够严谨，“新颖”或“新”只是薄弱的代理指标，工程师应根据需求、风险、权衡和潜在收益来做具体判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Dan McKinley :: Choose Boring Technology</a></li>
<li><a href="https://boringtechnology.club/">Choose Boring Technology</a></li>
<li><a href="https://jonathannen.com/choose-boring-technology/">Dan McKinley &#x27;s classic advice on &quot; choosing boring technology &quot; is....</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#technology strategy`, `#innovation tokens`, `#engineering culture`

---

<a id="item-tech-news-8"></a>
### [systemd-journald 单行日志造成 49KB 以上磁盘写入](https://github.com/systemd/systemd/issues/40262) ⭐️ 8.0/10

systemd 的 GitHub issue \#40262 指出，journald 基于 mmap 的日志写入设计导致单条日志行在 ext4 上产生 49KB 以上、在 btrfs 上产生 110KB 以上的磁盘写入。该性能问题源于日志数据通过在内存映射文件中追加并把元数据写入头部的机制，而不是使用顺序追加写入。社区讨论认为这种设计是错误的，pwrite 或直接以 append-only 顺序文件方式写日志会好得多。此问题对运行 systemd 的系统会造成不必要的磁盘 I/O 和 SSD 磨损。

hackernews · ValdikSS · 8月13日 18:41 · [社区讨论](https://news.ycombinator.com/item?id=49290215)

**「背景」** systemd-journald 使用内存映射（mmap）方式读写日志文件，把日志文件直接映射到内存；这种设计虽减少系统调用，但为使新条目在崩溃时可靠持久化，每次追加日志都要更新文件头等元数据，并通过页面缓存将改动落盘。GitHub issue \#40262 报告在 systemd 257.9、Debian 13、内核 6.12.57+deb13-amd64 上，每秒仅写 2 条日志也让虚拟机保持约 50 IOPS，ext4 上单条日志触发 49KB+ 磁盘写入、btrfs 上超过 110KB，远高于 syslog 的开销。相关分析也将此性能问题归因于 mmap 导致的日志文件碎片化。

**「影响」** 对于 systemd 用户和开发者，这可能意味着在高日志量环境里产生大量额外磁盘 I/O 与存储磨损；有经验的社区成员建议只把 journald 当作日志路由而不在其中存储日志。

**「社区讨论」** 评论普遍认为 journald 的 mmap 写日志设计是根本性错误，并推荐使用 pwrite 或追加式顺序文件；还有人抱怨系统组件（如 KIO）会写入成千上万条无意义日志，且 journald 缺乏对单一标识符日志截断的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/systemd/systemd/issues/40262">Excessive IO caused by systemd-journald · Issue #40262 - GitHub</a></li>
<li><a href="https://devops-geek.net/devops-lab/the-unexpected-performance-killer-how-memory-mapped-files-in-systemd-journal-are-fragmenting-your-pr/">The Unexpected Performance Killer: How Memory-Mapped Files in Systemd ...</a></li>
<li><a href="https://zeli.app/en/story/49290215">systemd-journald writes 49KB+ per log line on ext4, 110KB+ on btrfs</a></li>

</ul>
</details>

**标签**: `#systemd`, `#journald`, `#logging`, `#disk-io`, `#performance`

---

<a id="item-tech-news-9"></a>
### [AI 机器人实验室年测 300 万人体组织，有望淘汰动物测试](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

Vivodyne 公司在旧金山南部运营着一套由衣柜大小的机器人实验室组成的系统，利用 AI 设计实验并培养人体组织，以更准确地预测新药的疗效和安全性。该系统目前包含 12 个“蜂巢”机器人实验室，每年可对 300 多万个人体组织开展受控试验，其容量是美国全部临床试验总和的两倍。当前约 90%的临床试验在通过动物测试后仍告失败，该技术有望减少甚至替代动物测试，从而加速药物研发并提高成功率。

telegram · zaihuapd · 8月14日 01:48

**「背景」** 新药研发的传统路径是先做动物实验，再进入人体临床试验，但动物模型常无法准确预测人体反应，大量候选药在临床阶段失败。Vivodyne 是一家总部位于费城的生物科技公司，2025 年 5 月宣布获得 4000 万美元资金，用于扩建其结合自动化机器人平台与 AI 的人体组织测试系统，并在旧金山开设全机器人实验室。其做法是在体外培养多种功能性人体组织，再由 AI 设计并执行大量受控实验，以更接近人体真实情况的方式筛选药物。

**「影响」** 如果该系统的性能得到验证，药物研发企业将能以更低成本和更快速度筛选候选药物，同时减少对动物测试的依赖，并可能提高临床试验通过率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businesswire.com/news/home/20250528498236/en/Vivodyne-to-Replace-Animal-Testing-With-$40-Million-Funding-to-Reverse-95-Clinical-Trial-Failure-Rate">Vivodyne to Replace Animal Testing With $40 Million Funding ...</a></li>
<li><a href="https://firstwordpharma.com/story/5967233">Vivodyne raises $40M to replace animal testing with AI and ...</a></li>

</ul>
</details>

**标签**: `#AI-driven drug discovery`, `#robotic lab automation`, `#human tissue engineering`, `#animal testing alternatives`, `#biotech`

---

<a id="item-tech-news-10"></a>
### [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室开源了 dots3-note preview，这是 dots3 系列首个开放权重模型。该模型总参数 280B，每次激活仅 16B，支持 512K 上下文，可处理文字、图片、视频和音频等多模态输入。模型引入 TEMPO 强化学习方法，以自批判和测试时价值估计训练长程智能体，权重已在 Hugging Face 开放，并同步发布 VibeSearchBench、VibeLifeBench 两个真实场景智能体基准。此次开源为 AI/ML 社区提供了大参数 MoE 在多模态与长程智能体任务上的可复现实验基础，不过仍属预览版本，有待基准验证。

telegram · zaihuapd · 8月14日 08:27

**「背景」** 小红书（Xiaohongshu）dots 实验室此前主要面向内部研究，dots3 系列是其在长程智能体任务上的新模型家族。MoE（混合专家）模型通常将总参数量与每次激活的参数量分离，从而使推理成本接近激活参数量而非总参数量，因此 280B 总参数、16B 激活参数的设置意味着较低的每次推理开销。本次开源的 dots3-note preview 是 dots3 系列首个开放权重模型，配合 TEMPO 这一新的强化学习方法，强调通过自批判和测试时价值估计来训练长程智能体。

**「影响」** 开发者现可在 Hugging Face 获取 preview 权重并在 512K 上下文下开展多模态和长程智能体实验，但作为预览版本，其实际性能仍需 VibeSearchBench、VibeLifeBench 等基准确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3938759517896072">Xiaohongshu Open -Sourced Dots 3 - Note : The Same-Series Model ...</a></li>
<li><a href="https://github.com/studio-dots-ai/dots3-note-prev">GitHub - studio- dots -ai/ dots 3 - note -prev: dots 3 note preview · GitHub</a></li>

</ul>
</details>

**标签**: `#open source`, `#MoE`, `#multimodal`, `#reinforcement learning`, `#AI models`

---

<a id="item-tech-news-11"></a>
### [Bluesky 发布协议服务，Jetstream 简化 Firehose 接入](https://atproto.com/blog/introducing-bluesky-protocol-services) ⭐️ 7.0/10

Bluesky 官方宣布推出新的 Bluesky Protocol Services，为开发者提供更便捷的协议基础设施，其中最受关注的是 Jetstream。Jetstream 使消费 Bluesky 实时数据流（firehose）变得非常容易，开发者甚至无需运行服务器，直接在浏览器中即可连接并查看事件流。这一举措被视为 Bluesky 将服务范围从官方 App 扩展到更广泛协议生态的例证。不过，评论中也有人指出这类由 VC 支持的底层基础设施尚未找到可持续的盈利路径，且 Bluesky 活跃用户数在收缩。

hackernews · danabramov · 8月14日 00:14 · [社区讨论](https://news.ycombinator.com/item?id=49293324)

**「背景」** Bluesky Protocol Services 是 Bluesky 为其在 AT Protocol 开放网络上运行的公共基础设施推出的新品牌和网站，取代了原先的 docs.bsky.app 域名。Jetstream 是 AT Protocol 的流式 API，开发者可以用它轻松消费 Bluesky 的全量火线（firehose），甚至无需服务器即可在浏览器中直接连接。此次发布的核心是 Jetstream v2，它新增了 Network Replay 功能，允许开发者先通过压缩归档包回填历史数据，再无缝切换到实时 WebSocket 流，从而更方便地获取完整网络数据。

**「影响」** 对开发者而言，Jetstream 降低了实时接入 Bluesky 数据流的门槛，浏览器端即可体验，无需自建服务端。但仍需注意其长期资金可持续性存在不确定性。

**「社区讨论」** 开发者普遍称赞 Jetstream 的易用性，并有人提出基于 Bluesky 火线重构 DNS 的设想；同时也有评论质疑 VC 资金难以为继，并关联 Bluesky 活跃用户缩小的消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atproto.com/blog/introducing-bluesky-protocol-services">Introducing Bluesky Protocol Services - AT Protocol</a></li>
<li><a href="https://zeli.app/en/story/49293324">Bluesky launches Protocol Services with Jetstream v2 network replay</a></li>
<li><a href="https://news.linxi.com.au/news/bluesky-unveils-protocol-services-and-jetstream-v2-with-network-replay">Bluesky Unveils Protocol Services and Jetstream v2 with Network Replay</a></li>

</ul>
</details>

**标签**: `#bluesky`, `#atproto`, `#decentralized protocols`, `#open source`, `#jetstream`

---

<a id="item-tech-news-12"></a>
### [Pi 上下文压缩机制解析](https://earendil.com/posts/compaction-in-pi/) ⭐️ 7.0/10

一篇题为《How Compaction Works in Pi》的技术文章深入解析了 Pi AI 系统中的上下文压缩（context compaction）机制，说明它如何处理长对话中的上下文窗口限制。这类压缩通常依赖另一个模型生成对话摘要，而用户能控制的只有触发时机，因此长任务最好从一开始拆分为可单独审查的小块，再在适当时机压缩。该主题对构建 LLM agent 的工程师具有直接参考价值，因为上下文窗口管理直接影响智能体的长期行为与回答质量。文章引发了关于修剪、双 KV 缓存、保持低上下文占用等替代策略的讨论，整体被看作一次务实的工程改进而非颠覆性突破。

hackernews · tosh · 8月13日 17:57 · [社区讨论](https://news.ycombinator.com/item?id=49289654)

**「背景」** Pi 是一个 AI 编程助手，其上下文压缩（compaction）功能会在对话接近模型上下文窗口上限时，通过单独的压缩请求生成摘要。该请求使用专门的系统提示词，例如将模型设定为“上下文摘要助手”，而非常规的“编程助手”，从而对已有对话进行总结。压缩条目会保留先前未被清除的消息，并基于重建后的会话上下文重新计算 token 数，以确保计数准确。

**「影响」** 对正在开发 LLM agent 的工程师来说，上下文压缩不是万能方案；社区经验表明，提前规划分支、修剪低价值消息或维护双 KV 缓存，可能比事后压缩更有效地保持对话质量。

**「社区讨论」** 评论者 kierangill 更倾向于修剪而不是压缩，认为摘要容易丢失原始意图；errantmind 建议将上下文占用保持在 30%以下，并用分支方式处理旁支任务；novaRom 介绍了双 KV 缓存的实现，让一个缓存产出 token 时另一个缓存趁机生成摘要；imgyuri 认为压缩依赖另一个模型，需提前规划可审查的阶段性工作；skeledrew 则指出提示词缓存机制会抑制更创新的压缩方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://earendil.com/posts/compaction-in-pi/">How Compaction Works in Pi | EARENDIL</a></li>
<li><a href="https://pi.dev/docs/latest/compaction">Compaction &amp; Branch Summarization · Documentation · Pi</a></li>

</ul>
</details>

**标签**: `#LLM`, `#context-window`, `#compaction`, `#AI-agents`, `#infrastructure`

---

<a id="item-tech-news-13"></a>
### [657607 条链接追踪：旧网页为何消失](https://0.mk/blog/link-rot) ⭐️ 7.0/10

一项大规模分析追踪了 657,607 条链接，试图回答“旧网页去了哪里”，将链接失效（link rot）与互联网文化变迁作为主要线索。该研究受到 Hacker News 社区广泛讨论，共获得 193 分和 182 条评论，反映出开发者与网络史爱好者对这一现象的浓厚兴趣。虽然源内容未提供具体发现细节，但标题与讨论表明，旧网络内容的消失并非单一时间事件，而是持续性的文化和技术过程。

hackernews · tdx · 8月13日 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49289532)

**「背景」** 链接腐烂（link rot）指的是网页中的超链接随着时间推移逐渐失效的现象，是旧互联网内容消失的主要原因之一。一项大规模分析追踪了 657,607 个链接，去重后得到 494,781 个不同 URL，其中 492,620 个可被爬取，结果显示 76.7%的旧网页链接已经失效。这项研究通过数据揭示了早期网络文化的消逝，并提到了一些有趣的发现，例如第一个被缩短的链接和指向 localhost 的链接。

**「影响」** 对关注网页存档与链接维护的开发者、研究者而言，这项分析把“旧网消失”从模糊怀旧变成可量化的数据问题，提示需要更重视链接持久性和档案保存。

**「社区讨论」** 评论者就“旧网”何时结束分歧明显：有人认为是 Facebook 真正崛起前的博客时代，有人认为是谷歌搜索公开前的 1997 年以前，也有人认为 2009-2014 年已不算“旧网”。还有评论指出，人们怀念“旧网”更多是一种文化现象，取决于个人接触网络的年龄段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://0.mk/blog/link-rot">Where did the old web go ? We followed 657 , 607 links to find out .</a></li>
<li><a href="https://zeli.app/en/story/49289532">76.7% of old web links are dead: a 657 , 607 - link autopsy — Where ...</a></li>

</ul>
</details>

**标签**: `#link rot`, `#web history`, `#data analysis`, `#internet culture`

---

<a id="item-tech-news-14"></a>
### [City2Graph：面向城市系统的异构图神经网络 Python 库](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph 是一个新发布的 Python 开源库，可将城市地理空间数据转换为适用于空间分析、网络分析和图神经网络（GeoAI）的异构图。其配套论文已发表于《Computers, Environment and Urban Systems》第 130 卷，文章编号 102492（2026 年），作者为 Sato、Pietrostefani、Mahabir 和 Arribas-Bel。该库覆盖形态学（建筑、街道、镶嵌城市肌理）、交通（GTFS/GBFS 通过 DuckDB 加载）、流动性（OD 矩阵和流量数据）以及邻近性（KNN、Delaunay、Gilbert、Waxman、皇后/车相邻，支持欧氏、曼哈顿或网络距离），并支持通过元路径构建异构图关系。它还能在 GeoDataFrames、NetworkX、rustworkx 和 PyTorch Geometric（Data/HeteroData）之间往返转换，同时保留几何与属性信息。

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · 8月13日 11:59

**「背景」** 城市系统包含建筑、街道、交通线路、人口流动等多类实体及其相互关系，传统上常被表示为扁平化的特征表格，丢失了这些实体间的结构联系。异构图允许在同一图中包含多种节点和边类型，并通过元路径表达跨类型关系，能够更自然地建模城市数据的复杂依赖。City2Graph 正是提供了一条从原始地理数据到这种异构图的自动化转换路径。

**「影响」** 对于从事 GeoAI、城市计算和空间分析的研究者与开发者，City2Graph 提供了可直接使用的工具，降低了将 OpenStreetMap、Overture Maps、GTFS、GBFS 等数据构建为异构图并接入 PyTorch Geometric 等图学习框架的门槛。

**标签**: `#python`, `#graph-neural-networks`, `#geospatial`, `#urban-systems`, `#open-source`

---

<a id="item-tech-news-15"></a>
### [worldproof：像素指标无法排名世界模型](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

作者发布了开源诊断工具 worldproof（Apache-2.0，pip install worldproof），用于对比世界模型 rollout 与真实轨迹及物理不变量，定位预测在何处失效。验证工具时发现，在真实机器人视频上像素指标常常无法区分模型：以 SO-101 机械臂 30fps、三相机、64 次 rollout、6 步 horizon、仅动态区域评分为例，&quot;最后一帧复制&quot;基线达到 0.983 SSIM 和 53.9 dB PSNR，且 SSIM 随 horizon 不下降而在 0.89–0.97 间波动。在 DROID 15fps 的 48 步实验中，SSIM@dynamic 从第 1 步的 0.873 单调降至第 24 步的 0.260，第 28 步后约在 0.20 SSIM、10.3 dB 触底并震荡，说明该数据上可评估区间约为 8–24 步，两端都会使模型排名失效。作者还指出把第 0 步计入会抬高标量指标（30fps 下第 0 步达 119.8 dB，把 horizon 平均从约 32 拉到 53.9 dB），因此更应报告曲线而非标量。工具核心仅依赖 numpy、torch、pillow，可在无 GPU 笔记本上运行，并可直接读取 LeRobotDataset v3.0 的 parquet/mp4。

reddit · r/MachineLearning · /u/georgia\_bucea · 8月13日 19:58

**「背景」** 世界模型指根据起始上下文和动作序列预测未来帧的模型，评估时常用 SSIM、PSNR 等像素相似度指标。作者原本只想验证自己的诊断工具，却发现此前被认为在 curated data 上能通过排序测试的指标，在真实机器人视频中可能因为场景变化缓慢而失去区分度。

**「影响」** 对评估世界模型的研究者和工程师而言，最直接的后果是不能直接沿用论文默认的 horizon 或标量指标：应在自己的帧率与任务速度下测量&quot;基线可分离区间&quot;，并避免把第 0 步纳入汇总分数。

**标签**: `#world models`, `#evaluation metrics`, `#SSIM`, `#PSNR`, `#robotics`

---

<a id="item-tech-news-16"></a>
### [X 扩大算法开源，推出排名透明度工具](https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/) ⭐️ 7.0/10

X 宣布将“为你推荐”时间线及核心排名引擎代码发布到 GitHub，采用 Apache 2 许可证，代码规模约为此前的 10 至 15 倍。X 还在设置中推出透明度工具，近一个月发帖 10 次或以上的用户可下载 JSON 文件，查看账号或帖子是否被排名系统标记。该工具先向账号注册满一年的测试用户开放，部分用于判断违规内容的 Grok 系统未公开。此次扩大开源范围让外部开发者能更深入地审查排名机制，也使用户对算法影响有了更直接的可见性。

telegram · zaihuapd · 8月14日 01:03

**「背景」** 排名算法决定了用户能在“为你推荐”时间线中看到哪些内容，此前用户无法直接得知自己的账号或帖子是否被系统标记。X 本次将更多排名引擎代码开源，并推出透明度工具，使外部审查和用户自查成为可能。

**「影响」** 频繁发帖且账号注册满一年的 X 用户可借此直接查看自己的排名标记，开发者和研究者也能审查更完整的时间线排名代码；不过工具仍处于测试阶段且 Grok 违规判断逻辑未公开。

**标签**: `#open source`, `#algorithms`, `#transparency`, `#social media`, `#AI`

---

<a id="item-tech-news-17"></a>
### [苹果提交美国 App Store 外部购买抽成方案：最高 15%](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 7.0/10

苹果已向美国法院提交 App Store 外部购买抽成方案：标准应用抽成 15%，视频、新闻等合作项目及订阅续费抽成 10%，小型企业计划应用抽成 5%。此前美国最高法院驳回了苹果暂停下级法院审理相关费率的请求，Epic 将有机会作出回应，苹果预计需在 9 月 14 日前向最高法院提交书面意见。该方案是 Epic 反垄断诉讼后续进程中关于 App Store 支付规则的重要提案，直接影响外部购买场景下苹果向开发者收取的佣金比例。

telegram · zaihuapd · 8月14日 02:33

**「背景」** Epic Games 自 2020 年起起诉苹果，指控其 App Store 限制应用内支付方式并收取高额抽成，这一案件被称为 Epic Games v. Apple。2021 年法官 Yvonne Gonzalez Rogers 裁定苹果必须允许应用提供外部支付链接，但苹果随后以收取抽成的形式规避合规。2025 年 4 月，同一法院认定苹果“故意”未遵守原判决，此后苹果向法院提交了对外部购买收取抽成的具体方案。据 The Verge 和 AppleInsider 报道，苹果提议对标准应用收取 15% 佣金、对小企业计划应用收取 5% 佣金，而 Epic 则认为这些费用仍不合理。

**「影响」** 若该方案获法院批准，美国 App Store 开发者通过应用外购买产生的销售额将被苹果抽取最高 15% 的佣金，订阅续费和符合条件的小型企业应用可适用更低档位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Apple">Epic Games v. Apple - Wikipedia</a></li>
<li><a href="https://www.theverge.com/tech/979967/apple-epic-games-external-links-fees-filing">Apple and Epic argue over how much Apple should get from purchases made outside the App Store | The Verge</a></li>
<li><a href="https://appleinsider.com/articles/26/08/13/apples-latest-commission-rates-for-external-app-store-purchases-havent-satisfied-epic">Apple&#x27;s latest commission rates for external App Store purchases haven&#x27;t satisfied Epic</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#Epic Games`, `#commissions`, `#developers`

---

<a id="item-tech-news-18"></a>
### [美国法官责令谷歌取消第三方应用商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

美国地区法官 James Donato 在 Epic 诉谷歌反垄断案中下令谷歌简化第三方安卓应用商店的安装流程，删除 Play Store 中“查看”后才出现“安装”的多余步骤与警告弹窗。法院认定这些步骤是蓄意制造的反竞争摩擦，用于吓退普通用户。谷歌须在一周内完成修改，使安装第三方市场像安装普通安卓应用一样直接。此前的陪审团裁定谷歌在安卓应用分发上构成非法垄断。

telegram · zaihuapd · 8月14日 09:55

**「背景」** Epic Games v. Google 是美国法院审理的反垄断案件，此案中陪审团裁定谷歌在安卓应用分发市场上构成非法垄断。作为该案的后续裁决，法官 James Donato 已命令谷歌开放 Google Play 商店以允许第三方应用商店竞争，并要求其取消阻碍用户安装第三方应用商店的多余步骤和警告弹窗。

**「影响」** 该裁决将直接改变 Android 平台上第三方应用商店的分发方式，降低用户安装竞品商店的阻力，并为 Epic 与谷歌之间反垄断判决的具体执行迈出关键一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Google">Epic Games v . Google - Wikipedia</a></li>
<li><a href="https://www.theverge.com/policy/2024/10/7/24243316/epic-google-permanent-injunction-ruling-third-party-stores">Google must crack open Android for third - party stores , rules Epic ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#Antitrust`, `#Google`, `#App Stores`, `#Legal`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [标普 500 成分股第二季度净利润率创新高至 16.9%](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 8.0/10

根据 FactSet 高级盈利分析师 John Butters 的数据，标普 500 指数成分股第二季度综合净利润率达到 16.9%，高于第一季度的 14.8%和去年同期的 12.9%，也高于五年均值 12.4%。若该数字最终成立，将是 FactSet 自 2009 年开始统计以来的最高纪录。

rss · CNBC Finance · 8月13日 20:21

**「背景」** 净利润率是企业每 1 美元收入在扣除所有费用后真正留下的利润占比；Alphabet 和亚马逊是最大贡献者，但即使剔除这两家公司，15%的利润率也同样是 2009 年以来最高纪录。

**标签**: `#profit margins`, `#S&amp;P 500`, `#earnings`, `#stock market`, `#corporate profitability`

---

<a id="item-finance-news-2"></a>
### [美国宣布对部分进口无人机加征最高 100%关税](https://www.whitehouse.gov/presidential-actions/2026/08/adjusting-imports-of-unmanned-aircraft-systems-and-unmanned-aircraft-systems-components-into-the-united-states/) ⭐️ 8.0/10

美国总统 8 月 13 日签署公告，自 2026 年 9 月 3 日起对最大起飞重量超过 25 公斤的进口无人机、搭载热成像仪的无人机、无人机基站及部分关键部件加征 100%关税；25 公斤及以下无人机加征 25%。另一部分无人机部件的 25%关税将于 2027 年 2 月 9 日生效，公告并授权商务部长将更多部件纳入征税范围。

telegram · zaihuapd · 8月14日 01:24

**「背景」** 据彭博社报道，该公告旨在降低美国对外国无人机供应的依赖，并减少对中国无人机产业的依赖。

**「影响」** 这项关税将直接提高进口无人机及部件的采购成本，尤其会影响依赖中国供应链的大型或热成像无人机用户，如公共安全、农业和物流等行业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-13/trump-imposes-100-tariffs-on-certain-drones-countering-china">Trump Imposes 100 % Tariffs on Some Drones ... - Bloomberg</a></li>
<li><a href="https://www.datamintelligence.com/news/trump-drone-tariffs-2026-impact-on-global-drone-market-us-china-uav-supply-chain">Trump Drone Tariffs 2026: 100 % Duty on Chinese UAV Imports...</a></li>

</ul>
</details>

**标签**: `#无人机关税`, `#美国贸易政策`, `#进口限制`, `#白宫公告`, `#无人机行业`

---

<a id="item-finance-news-3"></a>
### [盘前个股异动：Reddit 涨 12%、应用材料跌超 5%、Workday 传收购谈判](https://www.cnbc.com/2026/08/14/stocks-making-the-biggest-moves-premarket-rddt-amat-sndk-w.html) ⭐️ 7.0/10

Reddit 因将于 8 月 18 日被纳入标普 500 指数，盘前上涨 12%。应用材料第二季度调整后每股收益 3.50 美元、营收 91.2 亿美元，但半导体系统部门营收仅略高于 FactSet 预期，盘前下跌超 5%；Workday 因 Silver Lake 洽谈收购的报道上涨约 2%。

rss · CNBC Finance · 8月14日 10:46

**「背景」** 标普 500 指数调整将使 Reddit 取代 AvalonBay Communities；Workday 周四已大涨近 18%，为 10 年来最佳单日表现。

**标签**: `#premarket`, `#S&amp;P 500`, `#earnings`, `#M&amp;A`, `#analyst upgrades`

---

<a id="item-finance-news-4"></a>
### [比尔·阿克曼再度建仓 Netflix，称其赢得流媒体战争](https://www.cnbc.com/2026/08/13/ackman-buys-netflix-again-four-years-later-says-it-won-streaming-wars.html) ⭐️ 7.0/10

比尔·阿克曼旗下 Pershing Square 在半年报告中披露已重新建仓 Netflix，认为其以逾 3.25 亿订阅用户赢得流媒体战争，且估值已从 2025 年 6 月高点下跌约 50%至约 21 倍预期市盈率。消息公布后，Netflix 股价周四上涨近 4%。

rss · CNBC Finance · 8月13日 18:04

**「背景」** 阿克曼曾在 2022 年初买入 Netflix，但在该公司报告十多年来首次订阅用户下降后约三个月内清仓，当时他表示商业模式变化使前景难以预测。

**标签**: `#Bill Ackman`, `#Netflix`, `#Pershing Square`, `#streaming`, `#investment`

---

<a id="item-finance-news-5"></a>
### [《大空头》投资者史蒂夫·艾斯曼指出 AI 热潮的致命弱点](https://www.cnbc.com/2026/08/13/big-short-investor-steve-eisman-sees-an-achilles-heel-in-the-ai-boom.html) ⭐️ 7.0/10

以做空楼市闻名的投资者史蒂夫·艾斯曼警告，当前 AI 热潮的回报越来越依赖 OpenAI 和 Anthropic 两家公司。他估计，这两家 AI 初创公司约占微软、亚马逊、谷歌母公司 Alphabet 和甲骨文 AI 相关收入的 70%，并占其云收入的 25%至 35%。这是艾斯曼的个人估计，并非已证实的数据。

rss · CNBC Finance · 8月13日 15:16

**「背景」** 艾斯曼因金融危机前做空楼市而广为人知。他的警告加入了一场关于 AI 巨额支出能否带来足够回报的辩论；另一知名投资者迈克尔·伯里已对英伟达等 AI 受益公司持看空立场。

**「影响」** 按艾斯曼的推演，如果中国开源 AI 模型真的抢走市场份额并触发价格战，大型云厂商及其投资者的收入可能承压。

**标签**: `#AI boom`, `#Big Tech`, `#OpenAI`, `#Anthropic`, `#China AI`

---