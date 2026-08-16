---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 32 items, 7 important content pieces were selected

---

**Technology News**
1. [Anthropic Publishes Official Claude System Prompts](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B shines but needs tuned-down reasoning](#item-tech-news-2) ⭐️ 8.0/10
3. [PJM Modeling Error Wasted $12B of Ratepayer Money](#item-tech-news-3) ⭐️ 8.0/10
4. [The AI Credit Resale Economy: Token Brokers and Risk](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare silently injects analytics after nameserver switch](#item-tech-news-5) ⭐️ 7.0/10
6. [SSOG-Attention: Sub-Quadratic Sum of Separable Gaussians Attention](#item-tech-news-6) ⭐️ 7.0/10

**Financial News**
1. [Anthropic preliminary Q2 revenue tops $11.5 billion, up 14x year over year](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Anthropic Publishes Official Claude System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has published the official system prompts used by Claude models in release notes, exposing the behind-the-scenes instructions and guardrails. The move gives developers and researchers a rare direct view into how a leading AI assistant is constrained, and allows tracking changes over time—Simon Willison has already compiled them into a git history. Notable content includes explicit guidance on image attachments, crisis response priorities, and model-specific additions such as references to Claude Fable 5 and Mythos 5. However, the release notes are a slice of a layered behavior-shaping system rather than the full mechanism.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**「Background」** System prompts are the hidden instructions given to an AI model to shape its behavior, covering safety rules, formatting guidelines, and other operational guardrails. Anthropic historically kept these prompts confidential, but in recent release notes began officially publishing them for its Claude models, making it easier for developers and researchers to understand how the model is instructed. Previously, such prompts were often extracted or leaked, and tools like Simon Willison&\#x27;s git repository track changes between Claude model versions.

**「Impact」** For AI developers and researchers, the official prompts provide auditable material for debugging, safety analysis, and cross-version comparison of Claude’s behavioral guardrails. The long-term practical effect will depend on how closely the documented prompts match the deployed configurations.

**「Community Discussion」** Commenters welcomed the transparency, but some questioned what transparent prompts reveal about model intelligence, noting that even powerful models need reminders to check for missing images; others viewed the prompts as just one layer of a larger behavior-shaping system. One user also raised concerns about platform moderation of critical AI stories.

<details><summary>References</summary>
<ul>
<li><a href="https://beamstart.com/news/google-amazon-backed-openai-rival-17248365922191">Google, Amazon-Backed OpenAI-Rival Anthropic Releases &#x27; System ...</a></li>
<li><a href="https://simonwillison.net/tags/system-prompts/?page=2">Simon Willison on system - prompts</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/ system _ prompts _leaks: Extracted system prompts ...</a></li>

</ul>
</details>

**Tags**: `#anthropic`, `#claude`, `#system-prompts`, `#ai-transparency`, `#llm`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B shines but needs tuned-down reasoning](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Alibaba&\#x27;s Qwen research lab released Qwen 3.8 27B, an Apache-2.0-licensed 27B parameter vision-capable LLM whose self-reported benchmarks show it beating Qwen 3.6 27B and even the larger closed-weight Qwen 3.7-Plus. Running the 17GB Q4\_K\_M quantized build with LM Studio on a 128GB M5 Max MacBook Pro and an NVIDIA DGX Spark, Simon Willison found it produces excellent local SVG outputs but defaults to an xhigh reasoning\_effort that consumes enormous context and time: one pelican SVG took 21 minutes, 22,276 reasoning tokens, and 3,223 output tokens, while the same prompt with reasoning off took 137 seconds and 3,715 tokens. He recommends overriding the default to low or no reasoning and reports the model is very good at bounding-box vision tasks. Independent benchmarks are still needed to confirm Qwen&\#x27;s performance claims.

rss · Simon Willison · Aug 16, 22:00

**「Background」** Qwen 3.8 27B is an open-weight, vision-capable model designed to run locally on reasonably powerful laptops and workstations. Its reasoning\_effort setting controls how much hidden chain-of-thought reasoning the model performs before answering, with options of xhigh, medium, and low; the xhigh default is meant for complex tasks but can exhaust typical context windows and cause very slow generation on consumer hardware.

**「Impact」** Users who load Qwen 3.8 27B with its default settings should expect multi-minute generations and potential context overflow even for simple prompts, so setting reasoning\_effort to low or off is the practical way to use the model for everyday tasks. The xhigh setting may still be worthwhile for complex requests where thorough analysis is more important than speed.

**Tags**: `#Qwen`, `#LLM`, `#open source`, `#benchmarks`, `#model release`

---

<a id="item-tech-news-3"></a>
### [PJM Modeling Error Wasted $12B of Ratepayer Money](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

A SemiAnalysis investigation by Robert Boswall reports that PJM, the US grid operator, wasted an estimated $12 billion of ratepayer money because of a modeling mistake. The article warns that PJM wants to repeat the flawed approach, putting ratepayers at further risk. The piece draws attention to how bad models in critical energy infrastructure can produce enormous financial consequences. Specific technical details of the modeling error are not included in the available excerpt.

rss · Semianalysis · Aug 16, 22:27

**「Background」** PJM Interconnection is the grid operator for a multi-state region in the eastern United States, responsible for ensuring reliable electricity supply and setting capacity market prices that ratepayers ultimately pay. In 2024, PJM&\#x27;s capacity market prices spiked by roughly $12 billion because its modeling relied on inappropriate assumptions about electricity supply, and PJM has proposed a &\#x27;reliability backstop&\#x27; procurement that critics, including state ratepayer advocates, warn could repeat the same costly mistake. Understanding this context is key to seeing why the modeling error is not just a technical oversight but a direct financial risk to millions of electricity customers.

**「Impact」** PJM ratepayers bear the $12B cost of the grid operator&\#x27;s modeling failure, and the upcoming July 2025 capacity auction risks repeating the same flawed approach, which may either keep consumer charges high or, if prices fall, discourage needed power plant investment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.rtoinsider.com/138882-maryland-fears-pjm-backstop-effort-could-raise-ratepayer-costs/">Maryland Ratepayers at Risk from PJM Backstop, Advocate Says</a></li>
<li><a href="http://climatecabineteducation.org/wp-content/uploads/2025/12/PJMs-Capacity-Market-Report.pdf">PJM Capacity Market Report v3 - climatecabineteducation.org</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R48553/R48553.1.pdf">PJM’s Electric Capacity Market: Background and Current Issues</a></li>

</ul>
</details>

**Tags**: `#energy`, `#machine-learning`, `#infrastructure`, `#modeling`, `#pjm`

---

<a id="item-tech-news-4"></a>
### [The AI Credit Resale Economy: Token Brokers and Risk](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

An analysis by vectoral.com examines the emerging AI credit resale economy, where token brokers facilitate trading of unused API credits even though such resale violates platform agreements. The article explores how relay services let users sell access to credits from accounts obtained through promotions, enterprise benefits, or compromised credentials, while providers can detect relays by IP address and flag originating accounts. Community discussion adds that the practice is an old abuse pattern also seen with loyalty accounts, and that credit resale can be used for model distillation. Commenters point to even larger gray markets on forums like linux.do and nodeseek, and a Y Combinator Startup School participant reportedly tried to resell $2,500 of credits. The analysis highlights trust and security problems for buyers, since brokers often have little reputation and accounts may be hacked.

hackernews · mlenhard · Aug 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**「Background」** AI API providers commonly distribute credits or free allowances as promotional incentives, and some users resell unused credits through brokers or relay services even though account agreements generally prohibit transfer. This credit-resale economy relies on technical mechanisms such as token relay pools, one-api gateways, and model distillation to route or repackage access. The practice echoes decades-old abuse patterns seen in online services and loyalty programs, and the ecosystem has spawned trackers that compare what AI content tools charge for tokens against published API rates.

**「Impact」** Buyers of resold AI credits risk account bans, credential theft, and data exposure, while AI providers such as OpenAI can identify relay usage by IP address and flag the originating accounts. This creates a fragile gray market that is likely to face escalating enforcement and security incidents.

**「Community discussion」** Commenters largely agree that credit resale violates platform terms and is risky for buyers, citing account bans, hacked credentials, and a lack of broker reputation. Some also note the practice follows the same abuse patterns as loyalty-program resale and point to deeper underground markets on forums like linux.do and nodeseek.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/ai-token-relay-market-resellers-fraud-july-2026">AI Token Relays — one-api, Pools, Distillation | explainx. ai</a></li>
<li><a href="https://draft2publish.ai/ai-token-markup-index/">The AI Token Markup Index — Draft2Publish</a></li>

</ul>
</details>

**Tags**: `#AI`, `#token economy`, `#resale market`, `#security`, `#industry analysis`

---

<a id="item-tech-news-5"></a>
### [Cloudflare silently injects analytics after nameserver switch](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

A developer reported on Hacker News that after switching nameservers to Cloudflare to enable R2 bucket serving through their own subdomain on textlog.cc, Cloudflare silently injected a JavaScript analytics snippet into their HTML-only, JS-free site. The snippet referenced static.cloudflareinsights.com/beacon.min.js and included an integrity hash and token, and the developer only discovered it after checking the Analytics dashboard, where they had to add the site and then disable the snippet. They described the behavior as invasive, arguing that such features should be opt-in rather than opt-out. The discussion notes that this injection appears tied to Cloudflare&\#x27;s proxy mode, since users with DNS-only setups did not observe it, and suggests using a Content-Security-Policy to block unwanted scripts.

hackernews · stagas · Aug 16, 17:49

**「Background」** Cloudflare Web Analytics can be enabled automatically by injecting a JavaScript beacon snippet into pages that are served through Cloudflare&\#x27;s proxy \(orange-clouded\). The original poster switched nameservers to Cloudflare to serve an R2 bucket on a subdomain, which meant the traffic was proxied, so Cloudflare auto-injected the analytics script even though the site was JavaScript-free HTML. Cloudflare&\#x27;s documentation confirms that automatic JS snippet injection only occurs for proxied domains; DNS-only domains require manual setup instead.

**「Impact」** Developers using Cloudflare in proxy mode may have Cloudflare Web Analytics injected into their sites without explicit consent, requiring them to manually opt out via the Analytics dashboard or implement a Content-Security-Policy to block the script.

**「Community discussion」** Commenters recommended using a Content-Security-Policy header to restrict script sources and shared the exact injected script tag as evidence. Others noted that the injection likely occurs only when Cloudflare terminates HTTPS as a proxy, not when domains are set to DNS-only mode.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/web-analytics/faq/">FAQs · Cloudflare Web Analytics docs</a></li>
<li><a href="https://burgeonlab.com/blog/cloudflare-web-analytics-rum-injected-tracking-beacon-script-into-my-sites/">Cloudflare Auto Injected Tracking Scripts To My Sites</a></li>

</ul>
</details>

**Tags**: `#cloudflare`, `#privacy`, `#web-analytics`, `#security`, `#dns`

---

<a id="item-tech-news-6"></a>
### [SSOG-Attention: Sub-Quadratic Sum of Separable Gaussians Attention](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention introduces a sum of separable Gaussians as a sub-quadratic alternative to scaled dot-product attention \(SDPA\), reducing complexity from O\(N²·d\) to O\(N·√N·d\). Instead of computing similarity scores between all image tokens and query tokens, each attention head learns a few Gaussian atoms that are geometrically steered by the query token, and because these atoms factorize into a separable sum, the computation becomes more efficient. Experiments reported by the author show that SSOG clearly outperforms SDPA on CIFAR-100 and delivers equivalent performance with much faster convergence on ImageNet \(IN1k\), while being increasingly faster and more memory-efficient as scale grows. The project includes a blog post and a GitHub repository with additional results and ablations. These findings are promising but lack external validation or wider adoption.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**「Background」** Scaled dot-product attention \(SDPA\) is the core mechanism in many transformer models, computing attention scores by comparing every query token with every key token, which leads to quadratic O\(N²·d\) complexity in the number of tokens. SSOG-Attention avoids this by learning a small number of Gaussian atoms per head and using the query token to steer them geometrically; since the Gaussians factorize, the attention computation becomes a separable sum with sub-quadratic complexity.

**「Impact」** For researchers and practitioners working with vision transformers, SSOG-Attention offers a concrete way to reduce the computational and memory cost of attention at scale while maintaining or improving accuracy on smaller datasets. However, the results are currently based on the author&\#x27;s own experiments and need independent replication before being widely adopted.

**Tags**: `#attention mechanisms`, `#efficient transformers`, `#sub-quadratic complexity`, `#computer vision`, `#machine learning`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic preliminary Q2 revenue tops $11.5 billion, up 14x year over year](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Bloomberg, citing documents, reported that Anthropic’s preliminary second-quarter revenue exceeded $11.5 billion, up more than 14 times from $787 million a year earlier and above the $4.73 billion seen in Q1 2026, while adjusted operating profit turned positive and the company prepares for a possible IPO this fall.

telegram · zaihuapd · Aug 16, 07:26

**「Background」** Anthropic reported preliminary second-quarter revenue above $11.5 billion, up more than 14x from $787 million a year earlier and up from $4.73 billion in Q1 2026; adjusted operating profit turned positive, though figures may be revised. The company filed confidentially for an IPO in June 2026 and is reportedly targeting a listing as early as October 2026.

**「Impact」** The preliminary results strengthen Anthropic&\#x27;s position as it races OpenAI toward the public markets, and analysts say combined capital demands from companies like Anthropic and OpenAI could disrupt capital markets; investors have also begun shifting focus to Anthropic amid concerns about OpenAI&\#x27;s cash burn and slowing user growth.

<details><summary>References</summary>
<ul>
<li><a href="https://fiscalzenith.com/anthropic-ipo-2026-965-billion-valuation-revenue-risks-and-what-investors-need-to-know/">Anthropic IPO 2026: $965 Billion Valuation, Revenue, Risks ...</a></li>
<li><a href="https://thebriefscript.com/anthropic-ipo-2026-s1-filing-valuation/">Anthropic IPO 2026: Everything You Need to Know About the ...</a></li>
<li><a href="https://www.reuters.com/business/ai-giant-anthropic-confidentially-files-us-ipo-2026-06-01/">Anthropic moves toward IPO, stepping up race with OpenAI | Reuters</a></li>
<li><a href="https://www.gurufocus.com/news/8996836/openai-faces-competition-from-anthropic-as-ipo-plans-shift">OpenAI Faces Competition from Anthropic as IPO Plans Shift</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI`, `#revenue growth`, `#operating profit`, `#IPO`

---