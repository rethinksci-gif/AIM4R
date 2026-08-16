---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 32 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Anthropic 发布 Claude 官方系统提示词](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B 能力出色，但默认过度思考](#item-tech-news-2) ⭐️ 8.0/10
3. [PJM 建模失误浪费 120 亿美元且可能重蹈覆辙](#item-tech-news-3) ⭐️ 8.0/10
4. [AI 额度转售经济：Token 中介的灰色市场](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare 切换域名服务器后静默注入分析脚本](#item-tech-news-5) ⭐️ 7.0/10
6. [SSOG-Attention：亚二次复杂度的高效注意力替代方案](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [Anthropic 第二季初步营收超 115 亿美元，同比增逾 14 倍](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 发布 Claude 官方系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 发布了 Claude 模型的官方系统提示词，首次让外界看到这些模型被如何指示和约束。这些说明位于 Claude 平台文档的发布说明中，覆盖 Opus 4.8、Opus 5 等模型，并包含处理图片缺失、危机对话等场景的规则。对 AI 开发者与研究人员而言，这意味着可以逐版本对比提示词变化，例如 Simon Willison 已建立 git 提交历史来追踪差异。此举本身并非技术突破，但为理解领先 AI 系统的运行护栏提供了具体材料。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**「背景」** Anthropic 的 Claude 是一系列面向用户的大语言模型，此前其系统提示词（system prompts）通常只能通过社区逆向提取或泄露才可见。如今 Anthropic 在其官方文档中正式发布了这些系统提示词，并承诺随模型更新而更新，让开发者无需依赖第三方提取即可了解模型受哪些指令和约束。

**「影响」** 开发者与研究人员现在可以直接审查并追踪 Claude 系统提示词的版本变化，从而更精确地评估模型行为调整和透明度承诺。

**「社区讨论」** 评论中，Simon Willison 提供了可追踪提示词变化的 git 提交历史，方便查看 Opus 4.8 到 Opus 5 的差异；也有开发者质疑把“检查图片是否真的存在”这类常识写进系统提示词是否说明模型并未真正具备智能，另有人提醒系统提示词只是多层行为塑造的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beamstart.com/news/google-amazon-backed-openai-rival-17248365922191">Google, Amazon-Backed OpenAI-Rival Anthropic Releases &#x27; System ...</a></li>
<li><a href="https://simonwillison.net/tags/system-prompts/?page=2">Simon Willison on system - prompts</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/ system _ prompts _leaks: Extracted system prompts ...</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#claude`, `#system-prompts`, `#ai-transparency`, `#llm`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B 能力出色，但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 实验室发布了 Apache 2.0 许可的 27B 参数视觉语言模型 Qwen 3.8 27B。官方自报基准显示其性能超过前代 Qwen 3.6 27B，也超过闭源的 Qwen 3.7-Plus；Simon Willison 在 M5 Max MacBook Pro 和 NVIDIA DGX Spark 上运行了 17GB Q4\_K\_M 量化版本（LM Studio 和 llama-server）。模型默认使用 xhigh 推理档位，导致极其严重的过度思考：例如生成“pelican riding a bicycle”SVG 用了 21 分钟、22,276 个推理 token 和 3,223 个输出 token，而关闭推理后同一任务只用 137 秒和 3,715 token。LM Studio 默认 8,192 token 上下文限制会被思考内容迅速耗尽，需加载到 262,144 最大上下文。作者强烈建议忽略默认设置，先使用 low 或关闭推理模式。

rss · Simon Willison · 8月16日 22:00

**「背景」** Qwen 3.8 27B 是 Qwen 系列中的中端开源模型，27B 参数规模适合在配置较好的笔记本上本地运行，且具备视觉理解能力。Qwen 3.8 引入了官方的 reasoning\_effort 参数，可设置 xhigh、medium、low 来控制推理深度和成本，其中 xhigh 被设为默认值。

**「影响」** 对于在个人电脑或本地服务器上运行该模型的用户，默认 xhigh 会导致任务耗时数分钟到数十分钟，实用性大幅下降；用户应先设置 reasoning\_effort 为 low 或关闭推理，并在需要长输出时扩大上下文窗口。

**标签**: `#Qwen`, `#LLM`, `#open source`, `#benchmarks`, `#model release`

---

<a id="item-tech-news-3"></a>
### [PJM 建模失误浪费 120 亿美元且可能重蹈覆辙](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

据 SemiAnalysis 旗下通讯文章调查，美国最大电网运营商 PJM 因建模错误浪费了 120 亿美元的电费资金，并可能再次犯下同样错误。文章作者 Robert Boswall 指出，问题出在错误的模型上，但这些模型并非通常所说的人工智能模型。尽管 PJM 被称为“美国最伟大的电网”，其建模失误仍让缴费者面临风险。目前文章全文尚未完整公开，部分细节仍有待核实。

rss · Semianalysis · 8月16日 22:27

**「背景」** PJM 是美国最大的区域电网运营商，负责组织电力批发市场和容量拍卖，以确保未来供电充足。2024 年，PJM 在容量市场建模中采用了不恰当的供电假设，导致拍卖结果使费率纳税人多支付了约 120 亿美元。目前 PJM 提出的可靠性后备采购方案（backstop procurement）可能再次推高费率纳税人成本，相关投诉和州级监管质疑已经出现。

**「影响」** PJM 当前依赖静态长期预测的能力市场设计已导致数十亿美元的消费者支出由技术假设而非市场动态决定，且下一次容量拍卖（原定 2025 年 7 月）可能重演类似损失；若不能转向能源与辅助服务市场收入并配合远期合同，费率支付者将继续承受可避免的高额成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.rtoinsider.com/138882-maryland-fears-pjm-backstop-effort-could-raise-ratepayer-costs/">Maryland Ratepayers at Risk from PJM Backstop, Advocate Says</a></li>
<li><a href="https://www.pjm.com/-/media/DotCom/library/reports-notices/special-reports/2026/20260506-powering-reliability-through-market-design.pdf">Powering Reliability Through Market Design - pjm.com</a></li>
<li><a href="http://climatecabineteducation.org/wp-content/uploads/2025/12/PJMs-Capacity-Market-Report.pdf">PJM Capacity Market Report v3 - climatecabineteducation.org</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R48553/R48553.1.pdf">PJM’s Electric Capacity Market: Background and Current Issues</a></li>

</ul>
</details>

**标签**: `#energy`, `#machine-learning`, `#infrastructure`, `#modeling`, `#pjm`

---

<a id="item-tech-news-4"></a>
### [AI 额度转售经济：Token 中介的灰色市场](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

本文分析新兴的 AI 额度转售经济，重点观察所谓 token broker 如何撮合未使用 API 额度的交易，尽管这类转售通常违反 OpenAI 等平台的服务协议。文章提到有人试图转售 YC Startup School 获得的 2500 美元额度，还指出蒸馏等用途让这类灰色市场尤为独特。评论者认为，平台可通过识别中继 IP 地址、追溯来源来标记账号，因此卖家面临封号风险；也有人提醒，任何“给账号就送额度”的激励都会吸引批量注册、盗号转卖等几十年来常见的滥用模式。整体上，该市场缺乏可靠信用机制，买家需要信任几乎没有声誉的第三方，安全风险突出。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**「背景」** AI 信用转售经济指的是部分用户或组织将云服务商或 AI 平台免费赠送的 API 额度（如研究积分、初创企业积分）通过代理或中继服务转卖获利。这类做法通常违反服务条款，且技术上游常见于 one-api 类中继工具、蒸馏（distillation）以及滥用批量注册账号获取赠金的模式；同时，市场上也出现了跟踪 AI 内容工具 token 标价与实际 API 成本之间差价的独立指数，用于揭示这类套利空间。

**「影响」** 对参与转售的开发者而言，最直接的后果是账号可能因违反服务协议而被 AI 平台封禁，且向无信誉第三方提供 API 访问权会显著增加数据泄露和被盗用的风险。由于平台有能力通过 IP 和行为模式追溯中继来源，这种灰色交易的可持续性并不确定。

**「社区讨论」** 评论中既有对灰色市场必然性的认同——只要激励存在，批量注册、员工福利转卖和盗号转卖就会延续——也有强烈的不信任：多数人不愿以 99% 折扣信任几乎无声誉的中介。还有评论指出相关研究过浅，建议参考 linux.do、nodeseek 等平台，另有人发现某转售平台盗用 Chroma 的翻转 logo。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/ai-token-relay-market-resellers-fraud-july-2026">AI Token Relays — one-api, Pools, Distillation | explainx. ai</a></li>
<li><a href="https://draft2publish.ai/ai-token-markup-index/">The AI Token Markup Index — Draft2Publish</a></li>

</ul>
</details>

**标签**: `#AI`, `#token economy`, `#resale market`, `#security`, `#industry analysis`

---

<a id="item-tech-news-5"></a>
### [Cloudflare 切换域名服务器后静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

开发者 stagas 在 Hacker News 上报告，将域名服务器切换到 Cloudflare 以通过自有子域名启用 R2 桶服务后，Cloudflare 在其纯 HTML、无 JavaScript 的网站 textlog.cc 上静默注入了 JavaScript 分析代码。用户必须进入 Analytics 仪表盘，先添加网站，然后才能禁用该注入片段。stagas 认为这种默认注入并要求用户主动退出的做法具有侵入性。评论者指出 Cloudflare Web Analytics 的注入行为，并建议使用 Content-Security-Policy（CSP）来限制外部脚本加载。另有用户询问是否仅在 Cloudflare 作为代理而非仅 DNS 时才会注入，并提到 DNS-only 域名未观察到注入。

hackernews · stagas · 8月16日 17:49

**「背景」** Cloudflare Web Analytics 是一种基于 Real User Monitoring（RUM）的统计服务，其自动部署方式要求网站流量经过 Cloudflare 代理（橙色云）。当域名启用代理时，Cloudflare 会在返回的 HTML 中自动注入 beacon.min.js 探针；而仅使用 Cloudflare DNS（灰色云）的域名则不会自动注入，需要手动设置。用户切换 nameservers 后若恰好使用了代理，便可能无意中启用该脚本。

**「影响」** 对于使用 Cloudflare 代理的网站所有者，切换域名服务器后可能默认启用 Web Analytics 注入，需要前往分析仪表盘手动添加并关闭；评论显示仅使用 Cloudflare DNS（不开启代理）的域名可能不受影响。

**「社区讨论」** 评论中既有缓解建议（如通过 CSP 仅允许自托管脚本），也有人贴出 Cloudflare 官方博客关于 Web Analytics 的链接佐证行为。围绕注入条件的讨论显示，用户猜测该行为与 Cloudflare 代理（而非纯 DNS）有关，来自 DNS-only 域名的检查未发现分析被启用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/web-analytics/faq/">FAQs · Cloudflare Web Analytics docs</a></li>
<li><a href="https://burgeonlab.com/blog/cloudflare-web-analytics-rum-injected-tracking-beacon-script-into-my-sites/">Cloudflare Auto Injected Tracking Scripts To My Sites</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#privacy`, `#web-analytics`, `#security`, `#dns`

---

<a id="item-tech-news-6"></a>
### [SSOG-Attention：亚二次复杂度的高效注意力替代方案](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention 提出用可分离高斯和（Sum of Separable Gaussians）近似缩放点积注意力（SDPA），将复杂度从 O\(N²·d\) 降至 O\(N·√N·d\)。方法为每个注意力头学习少量高斯原子，并根据查询 token 进行几何引导，且原子可分解为可分离和，从而降低计算与内存开销。实验显示，该方法在 CIFAR-100 小数据集上明显优于 SDPA，在 ImageNet-1k 上取得相当精度且收敛更快，同时随规模增大更省显存和算力。项目已公开博客文章和代码仓库，作者还声明部分代码和文章由 AI 辅助完成。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**「背景」** 缩放点积注意力（SDPA）通过计算所有查询与所有键的相似度来生成注意力权重，复杂度随 token 数二次增长，成为长序列或高分辨率图像处理的瓶颈。SSOG 受高斯混合模型启发，用少量可分离高斯原子近似注意力分布，避免显式计算完整的 N×N 相似度矩阵。

**「影响」** 对处理高分辨率图像或长序列的计算机视觉开发者而言，SSOG-Attention 提供了一种在相近精度下显著减少计算量和显存占用的潜在方案；不过由于目前仅作者自行发布了实验结果，尚需更多独立复现来验证其在不同架构和任务上的泛化性。

**标签**: `#attention mechanisms`, `#efficient transformers`, `#sub-quadratic complexity`, `#computer vision`, `#machine learning`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 第二季初步营收超 115 亿美元，同比增逾 14 倍](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

据彭博社援引文件，Anthropic 2026 年第二季初步营收超过 115 亿美元，较上年同期的 7.87 亿美元增长逾 14 倍，调整后营业利润转正；公司正筹备可能在今秋启动的大型 IPO，数字仍可能调整。

telegram · zaihuapd · 8月16日 07:26

**「背景」** Anthropic 已于 2026 年 6 月 1 日秘密提交 IPO 申请，目标最早在 2026 年 10 月上市，并据称寻求约 9650 亿美元估值；截至 2026 年 5 月，公司年化营收运行率约为 470 亿美元。此次公布的 Q2 初步营收为最终财报前可能调整的数字，公司正在筹备大型 IPO。

**「影响」** 这加剧了 Anthropic 与 OpenAI 的 IPO 竞赛；分析师警告，SpaceX、OpenAI 和 Anthropic 合计的资本需求可能扰乱资本市场，并将投资者的关注从 OpenAI 转向 Anthropic。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fiscalzenith.com/anthropic-ipo-2026-965-billion-valuation-revenue-risks-and-what-investors-need-to-know/">Anthropic IPO 2026: $965 Billion Valuation, Revenue, Risks ...</a></li>
<li><a href="https://thebriefscript.com/anthropic-ipo-2026-s1-filing-valuation/">Anthropic IPO 2026: Everything You Need to Know About the ...</a></li>
<li><a href="https://www.reuters.com/business/ai-giant-anthropic-confidentially-files-us-ipo-2026-06-01/">Anthropic moves toward IPO, stepping up race with OpenAI | Reuters</a></li>
<li><a href="https://www.gurufocus.com/news/8996836/openai-faces-competition-from-anthropic-as-ipo-plans-shift">OpenAI Faces Competition from Anthropic as IPO Plans Shift</a></li>
<li><a href="https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html">Anthropic Files to Go Public, Setting Stage for Huge I.P.O. - The New York Times</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI`, `#revenue growth`, `#operating profit`, `#IPO`

---