---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 49 items, 23 important content pieces were selected

---

**Technology News**
1. [GLM-5.3 brings frontier coding and cyber capabilities](#item-tech-news-1) ⭐️ 9.0/10
2. [Spaghettifying DRAM: Novel Addressing Attack Grants Privileged Access](#item-tech-news-2) ⭐️ 9.0/10
3. [Gemini 3.7 Flash Launches Amid Pricing Debate](#item-tech-news-3) ⭐️ 8.0/10
4. [OpenAI and Cerebras Claim ~7x Faster GPT-5.6 Sol Inference](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek Harness Developer Preview: Traceable Open-Source Agent Harness](#item-tech-news-5) ⭐️ 8.0/10
6. [Understanding is the new bottleneck](#item-tech-news-6) ⭐️ 8.0/10
7. [Why &\#x27;Boring&\#x27; Technology Wins: The Innovation Tokens Framework](#item-tech-news-7) ⭐️ 8.0/10
8. [systemd-journald: single log line can cause 49-110KB disk writes](#item-tech-news-8) ⭐️ 8.0/10
9. [AI Robotic Labs Scale Human Tissue Testing to 3 Million Samples a Year](#item-tech-news-9) ⭐️ 8.0/10
10. [Xiaohongshu Open-Sources 280B MoE Model with 16B Active Parameters](#item-tech-news-10) ⭐️ 8.0/10
11. [Bluesky Launches Protocol Services with Easy Firehose Access](#item-tech-news-11) ⭐️ 7.0/10
12. [Pi&\#x27;s Context Compaction: How It Works and Its Limits](#item-tech-news-12) ⭐️ 7.0/10
13. [657,607 Links Show Where the Old Web Went](#item-tech-news-13) ⭐️ 7.0/10
14. [City2Graph turns urban geospatial data into graph-ready Python library](#item-tech-news-14) ⭐️ 7.0/10
15. [Pixel metrics often can&\#x27;t rank world models on real robot video](#item-tech-news-15) ⭐️ 7.0/10
16. [X Open-Sources More Ranking Algorithm Code, Adds Transparency Tool](#item-tech-news-16) ⭐️ 7.0/10
17. [Apple Proposes Up to 15% Commission for External Purchases in US](#item-tech-news-17) ⭐️ 7.0/10
18. [Judge orders Google to remove Play Store barriers for rival app stores](#item-tech-news-18) ⭐️ 7.0/10

**Financial News**
1. [S&amp;P 500 net profit margins reach record high in Q2](#item-finance-news-1) ⭐️ 8.0/10
2. [U.S. Imposes Tariffs Up to 100% on Some Imported Drones](#item-finance-news-2) ⭐️ 8.0/10
3. [Premarket movers: Reddit jumps on S&amp;P 500 inclusion; Applied Materials slides on earnings](#item-finance-news-3) ⭐️ 7.0/10
4. [Ackman&\#x27;s Pershing Square takes new Netflix stake after four-year break](#item-finance-news-4) ⭐️ 7.0/10
5. [Eisman warns AI boom depends on OpenAI and Anthropic](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [GLM-5.3 brings frontier coding and cyber capabilities](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.ai announced GLM-5.3, a frontier coding model with emergent cyber capabilities, including large-scale vulnerability discovery. The release positions the model for advanced code reasoning and security work, and community members point to the companion disclosure site cvd.z.ai, where vulnerabilities in open-source and popular software are being reported, many under embargo and rated critical or high. Commenters describe the results as close to but not yet surpassing models like Sol and Fable, and view the release as an incremental post-training advance over GLM 5.2. The announcement has generated significant discussion about AI-driven vulnerability discovery and the geopolitical and economic implications of releasing such capabilities broadly.

hackernews · pella · Aug 14, 05:19 · [Discussion](https://news.ycombinator.com/item?id=49294997)

**「Background」** GLM-5.3 is the latest model in Z.AI&\#x27;s GLM series and is positioned as the \#1 open-source model for coding and agent tasks, with Z.AI describing the release as the result of post-training scaling through real-world expert workflows. The company says it improves on its predecessor by about 50% on its internal Code Bench benchmark and introduces stronger cybersecurity capabilities. The release follows GLM-5.2, and the announcement has drawn attention partly because Z.AI is publishing vulnerability findings from large-scale scans of open-source software via cvd.z.ai.

**「Impact」** By making a frontier coding model with large-scale vulnerability-discovery capabilities broadly available, Z.ai is likely to push open-source maintainers and security teams to triage and patch a growing flow of automated CVEs faster.

**「Community Discussion」** Commenters acknowledged the scale of the vulnerability scanning effort, with one linking cvd.z.ai and noting a wide range of critical and high-severity CVEs under embargo, while another questioned whether such scans provide unique value as costs fall and Anthropic&\#x27;s Project Glasswing does similar work. Others compared GLM-5.3 unfavorably to Sol, Fable, and Mythos 5 on benchmarks, considered local quantization potential, and appreciated a less marketing-driven tone from the Chinese lab, though one commenter raised geopolitical concerns about unrestricted access to cyber capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM - 5 . 3 - Overview - Z . AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://theunum.io/en/news/read/chinese-startup-z-ai-has-introduced-the-glm-53-language-model-for-programming">Chinese startup Z ai has introduced the GLM - 5 . 3 language model for...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Cybersecurity`, `#Software Engineering`, `#LLM`

---

<a id="item-tech-news-2"></a>
### [Spaghettifying DRAM: Novel Addressing Attack Grants Privileged Access](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

A newly published GitHub repository describes a novel DRAM addressing technique called &quot;spaghettifying&quot; that manipulates memory controller behavior to gain privileged access on affected systems. The proof of concept targets AMD Jaguar, an older low-power architecture from 2013, with additional notes indicating that Zen 3 uses a different base address for memory controller registers. The technique has potentially serious implications for hardware security, particularly for game consoles and servers that rely on DRAM address scrambling to protect privileged regions. The repository is accompanied by expectations of a Black Hat talk explaining the research in more depth. It remains unclear from the available material which newer processor families beyond AMD Jaguar are actually vulnerable.

hackernews · matt\_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**「Background」** Modern DRAM controllers add proprietary address-translation and scrambling logic between the CPU and physical memory, partly as a defense against side-channel and Rowhammer attacks. Christopher Domas&\#x27;s &\#x27;skitter-creek-bath-salts&\#x27; project demonstrates that this translation layer can itself be manipulated: by reprogramming the DRAM controller&\#x27;s registers, an attacker can remap physical addresses to expose specialized memory carveouts that are normally hidden even from the kernel. The proof-of-concept targets AMD&\#x27;s Jaguar \(16h\) microarchitecture, with additional notes indicating that newer Zen 3 chips use a different memory-controller register base.

**「Impact」** On AMD Family 16h \(Jaguar\) systems, the attack gives ring-0 code access to hidden negative-ring CPU features because that family&\#x27;s DRAM controller translation registers are documented as unlockable, while newer CPUs&\#x27; exposure remains uncertain since 17h and later omit that documentation and Zen 3 at least differs in memory controller register base address.

**「Community Discussion」** Commenters praised Christopher Domas&\#x27;s previous reverse engineering and hardware security talks, and several noted that the growing complexity and proprietary nature of DRAM controllers make such attack surfaces unsurprising. Others questioned which modern CPUs are actually affected beyond the AMD Jaguar example and speculated that Xbox and PlayStation security teams would be concerned about post-ring-0 access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>
<li><a href="https://cybersecuritynews.com/dram-scrambling-attack/">New DRAM Scrambling Attack Exposes CPU’s Most Protected ...</a></li>
<li><a href="https://github.com/xoreaxeaxeax">xoreaxeaxeax (domas) · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#hardware security`, `#exploit`, `#memory attack`, `#reverse engineering`

---

<a id="item-tech-news-3"></a>
### [Gemini 3.7 Flash Launches Amid Pricing Debate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google introduced Gemini 3.7 Flash, a new AI model in the Gemini API, only about three weeks after releasing 3.6 Flash. The posting links to model documentation, but community discussion centered on its unusual introductory pricing, which is scheduled to double on December 31, 2026, with input and output costs rising to $1.50 and $7.50 per million tokens starting January 1, 2027. Early hands-on tests showed strong image-to-HTML results, although commenters noted that Anthropic&\#x27;s Opus 5 remains best in class for that task and that competing models such as GPT-5.6 Luna are considered cheaper and stronger on benchmarks like DeepSWE 1.1. The release generated 442 comments debating whether Flash still fills its intended low-cost, high-volume role.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**「Background」** Gemini 3.7 Flash is Google&\#x27;s latest addition to its Flash family of AI models, which are designed as cost-efficient &\#x27;workhorse&\#x27; models for coding, agentic workflows, and high-volume text tasks. It was released on August 13, 2026, just three weeks after Gemini 3.6 Flash, continuing a rapid iteration cycle driven by developer feedback and algorithmic improvements. The model offers a 1,048,576-token context window and up to 65,536 output tokens, with initial API pricing of $0.375 per million input tokens and $1.875 per million output tokens.

**「Impact」** Gemini 3.7 Flash is rolling out as the replacement for 3.6 Flash in Google&\#x27;s API, just three weeks after the previous release, while its introductory pricing is scheduled to double on December 31, 2026. Developers comparing it against alternatives must account for inconsistent benchmark tables across sources, and OpenAI&\#x27;s cheaper GPT-5.6 Luna pricing \($0.20/1M input, $1.20/1M output\) undercuts Flash&\#x27;s positioning for low-cost, high-volume text workloads.

**「Community Discussion」** Commenters were divided: one tester found Gemini 3.7 Flash&\#x27;s vision-to-HTML output strong for its price class but still below Opus 5, while another called the introductory pricing &\#x27;really weird&\#x27; because it doubles at the end of 2026 just months after 3.6 Flash shipped. Others argued Google should benchmark against cheaper rivals like Luna and Terra, claiming GPT-5.6 Luna outperforms it on DeepSWE 1.1 and undercuts the Flash tier&\#x27;s cost advantage.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/google/gemini-3.7-flash">Gemini 3.7 Flash - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://www.digitalapplied.com/blog/gemini-3-7-flash-vs-sonnet-5-gpt-5-6-terra-benchmarks">Gemini 3 . 7 Flash vs Sonnet 5 vs GPT - 5 . 6 Terra: Real Wins</a></li>
<li><a href="https://arstechnica.com/ai/2026/08/google-announces-gemini-3-7-flash-just-three-weeks-after-previous-release/">Google announces Gemini 3 . 7 Flash just three weeks... - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#Google`, `#Gemini`, `#AI model`, `#LLM`, `#pricing`

---

<a id="item-tech-news-4"></a>
### [OpenAI and Cerebras Claim ~7x Faster GPT-5.6 Sol Inference](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

OpenAI and Cerebras have announced GPT-5.6 Sol Ultrafast, a new inference mode for OpenAI&\#x27;s frontier model running on Cerebras hardware, claiming roughly 7x faster inference on frontier benchmarks with comparable accuracy. In their evaluations, Ultrafast answered all 2,500 Humanity&\#x27;s Last Exam questions in 11 hours and 11 minutes, while Claude Fable 5 needed 78 hours and 27 minutes, a nearly 7x speedup. The claims come from the vendors, and neither company has yet disclosed pricing, general availability, or a definitive statement that Ultrafast matches the standard GPT-5.6 Sol&\#x27;s performance exactly.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**「Background」** GPT-5.6 Sol is OpenAI&\#x27;s frontier model, and UltraFast is a new Cerebras-powered service tier that runs it at up to 750 output tokens per second—about 14× faster than standard processing—while aiming for no quality compromise. Cerebras specializes in wafer-scale AI accelerators designed for high-speed inference, and this collaboration brings that hardware to OpenAI&\#x27;s API for latency-sensitive workloads.

**「Impact」** Affected users are likely enterprise OpenAI/Cerebras customers rather than ordinary Pro subscribers, since Pro users report having only Standard and Fast tiers and pricing or availability for Ultrafast is undisclosed.

**「Community Discussion」** Commenters are intrigued by the speedup but cautious: some see faster inference as enabling more iterative thinking, while others note the lack of pricing, doubts about identical performance to standard GPT-5.6 Sol, and likely enterprise-only access.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM inference`, `#OpenAI`, `#Cerebras`, `#performance`

---

<a id="item-tech-news-5"></a>
### [DeepSeek Harness Developer Preview: Traceable Open-Source Agent Harness](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek released an early developer preview of DeepSeek Harness, an open-source AI agent harness under the MIT license. It records every model input in an append-only session log—system prompts, reasoning, tool calls and results, subagent scheduling, and context injections—and provides a Trajectory view for inspecting, resuming, forking, searching, and replaying runs. The framework uses a plugin architecture built on Cordis v4, supporting hot reload and dynamic enable/disable of plugins, including UI components, with state and side-effect cleanup on unload. The authors warn that this is an early version with rough edges and compatibility-breaking changes.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**「Background」** DeepSeek Harness \(dsh\) is an open-source agent runtime framework from DeepSeek AI, currently in developer preview as v0.1 under the MIT license; it is designed to turn DeepSeek&\#x27;s V4 series models into autonomous coding agents capable of multi-step workflows and tool use. The project advertises full traceability through append-only session logs and an architecture in which everything is a plugin. The plugin system builds on Cordis v4, a hot-reload plugin framework that can roll back side effects when unloading, which has been used for years in the Koishi project; the preview is expected to have rough edges and compatibility-breaking changes.

**「Impact」** Developers building auditable agent workflows can now inspect and replay every context injection and tool call, which stands out against encrypted or obfuscated traces offered by some US models. Because the preview is explicitly unstable, adopters should expect breaking changes and avoid relying on it in production yet.

**「Community discussion」** Commenters praised the full traceability feature as a differentiator, contrasting it with encrypted or obfuscated traces in US models, while others noted that Cordis v4&\#x27;s hot-reloading plugin system has prior use in Koishi. Skeptics worried about &quot;plugin fatigue&quot; from an everything-is-a-plugin architecture, and one reader found the accompanying paper useful but not dramatically so; the authors welcomed feedback at this early stage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview : Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://cryptobriefing.com/deepseek-harness-open-source-developer-preview/">DeepSeek Harness v0.1 enters developer preview with open - source ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open source`, `#developer tools`, `#DeepSeek`, `#traceability`

---

<a id="item-tech-news-6"></a>
### [Understanding is the new bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) ⭐️ 8.0/10

The article argues that understanding code, not writing it, has become the main bottleneck in software development, a shift reinforced by the rise of LLM-generated code. It calls for developer tools and workflows that prioritize program comprehension rather than just generation. The piece points to practical directions such as time-travel debugging, which would let engineers step through pull requests and inspect program state for specific test executions. Commenters add that LLM-written PR descriptions often lack motivation and warn that letting an LLM generate the understanding defeats the purpose of verifying code. Overall, the article reframes comprehension as a core engineering challenge.

hackernews · sebg · Aug 13, 18:47 · [Discussion](https://news.ycombinator.com/item?id=49290299)

**「Background」** Geoffrey Litt, a researcher at Notion, presented this argument at the AI Engineer conference in July 2026, warning that even as AI agents generate more code, human understanding of that code remains essential for creative collaboration and trustworthy oversight. He proposes techniques such as AI-generated personalized “explain diff” documents, literate code diffs, and interactive “micro worlds” to help developers efficiently comprehend AI-written changes rather than passively accepting them.

**「Impact」** For software engineers and teams working with LLM-assisted code, this framing elevates comprehension and verification from an afterthought to the central constraint, creating pressure for tools that expose execution state and for processes that keep humans in the loop.

**「Community discussion」** Commenters largely agree that understanding is the bottleneck, but diverge on remedies: one advocates time-travel debugging to inspect state during review, while another reports that LLM-generated PR descriptions are universally disliked and warns that using LLMs to build understanding can undermine human verification. Another notes the problem predates LLMs, arising when working code breaks the underlying model.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html">Understanding is the new bottleneck - geoffreylitt.com</a></li>
<li><a href="https://aidotengineer.podhood.com/48d7e61f-305d-4bf8-9ac6-b7dcb1d9c5d6">Understanding is the new bottleneck — Geoffrey Litt, Notion</a></li>
<li><a href="https://www.youtube.com/watch?v=WkBPX-oDMnA">Understanding is the new bottleneck — Geoffrey Litt, Notion Understanding is the new bottleneck — Geoffrey Litt, Notion Understanding is the New Bottleneck in AI - startuphub.ai Understanding is the new bottleneck • Buttondown Understanding is the new bottleneck — Geoffrey Litt, Notion</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#code understanding`, `#LLMs`, `#developer tools`, `#program comprehension`

---

<a id="item-tech-news-7"></a>
### [Why &\#x27;Boring&\#x27; Technology Wins: The Innovation Tokens Framework](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley&\#x27;s widely shared 2015 essay argues that organizations have a fixed budget for innovation—roughly three &\#x27;innovation tokens&\#x27;—and should spend them only on problems where novel technology offers a real competitive edge. For everything else, teams should choose mature, predictable, well-understood technologies, because the cost of debugging unfamiliar or unstable systems quickly exhausts the innovation budget. The essay has become a touchstone for engineering strategy and is now being applied to the age of AI agents, where the recommendation is to push all innovation tokens into agents and keep the surrounding stack as boring as possible.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**「Background」** Dan McKinley&\#x27;s essay &quot;Choose Boring Technology&quot; \(2015\) argues that every engineering organization has a limited budget for adopting new, unproven technology, which he metaphorically calls &quot;innovation tokens.&quot; He advises spending these tokens only where they create product differentiation, and otherwise choosing mature, predictable, and well-understood technologies for infrastructure and non-core problems. The essay grew out of McKinley&\#x27;s experience at companies like Etsy and has become a widely referenced framework for pragmatic technology decision-making.

**「Impact」** The &\#x27;innovation tokens&\#x27; framework gives engineering leaders and project managers a concrete way to evaluate new technology requests and communicate why most of a system should rely on proven components rather than chasing hype.

**「Community Discussion」** Commenters largely praise the essay as one of their favorites, with one reader calling it &\#x27;one of the most useful concepts&\#x27; for making and explaining tradeoffs. Others push back on the arbitrary nature of the token concept, arguing that engineers should weigh requirements, risks, and potential gains directly, with &\#x27;novel&\#x27; or &\#x27;new&\#x27; being weak proxies for the right decision.

<details><summary>References</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Dan McKinley :: Choose Boring Technology</a></li>
<li><a href="https://boringtechnology.club/">Choose Boring Technology</a></li>
<li><a href="https://jonathannen.com/choose-boring-technology/">Dan McKinley &#x27;s classic advice on &quot; choosing boring technology &quot; is....</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#technology strategy`, `#innovation tokens`, `#engineering culture`

---

<a id="item-tech-news-8"></a>
### [systemd-journald: single log line can cause 49-110KB disk writes](https://github.com/systemd/systemd/issues/40262) ⭐️ 8.0/10

A systemd GitHub issue \(systemd/systemd\#40262\) reports that a single journald log line can generate 49KB or more of disk writes on ext4 and over 110KB on btrfs, due to journald&\#x27;s mmap-based journal file design. The issue has triggered discussion about whether the design is fundamentally flawed, with some arguing that using pwrite or append-only sequential writes would be far better for logging. The high write amplification is particularly concerning for systems with high-volume logging or storage devices sensitive to write wear, such as flash and SSD storage. The availability of specific filesystem-dependent numbers highlights the concrete performance impact of journald&\#x27;s current implementation.

hackernews · ValdikSS · Aug 13, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49290215)

**「Background」** systemd-journald stores logs in a binary journal format that uses memory-mapped files \(mmap\) to append entries, a design inspired by classic log files and git that tries to ensure robustness and atomicity. On filesystems such as ext4 and btrfs, this mmap-based approach can produce much larger disk write amplification than expected: the reported GitHub issue \#40262 shows a single log line consuming 49KB+ of writes on ext4 and 110KB+ on btrfs, with roughly 50 IOPS at only 2 lines per second. This is a long-standing concern, as the issue references earlier report \#15292, and contrasts sharply with traditional syslog-style append-only logging, which performs writes in the same order of magnitude as the log line itself.

**「Impact」** Users running systemd-based systems on ext4 or btrfs may experience significantly more disk I/O than expected from their log volume, which can exacerbate storage performance issues and wear on flash-based media.

**「Community Discussion」** Commenters broadly agree that journald&\#x27;s mmap-based design was a mistake, with some suggesting append-only I/O as a simpler and more efficient approach. Others criticize journald&\#x27;s indexing and per-identifier log management, while noting that chatty applications can flood the journal with huge numbers of low-value entries.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/systemd/systemd/issues/40262">Excessive IO caused by systemd-journald · Issue #40262 - GitHub</a></li>
<li><a href="https://devops-geek.net/devops-lab/the-unexpected-performance-killer-how-memory-mapped-files-in-systemd-journal-are-fragmenting-your-pr/">The Unexpected Performance Killer: How Memory-Mapped Files in Systemd ...</a></li>
<li><a href="https://zeli.app/en/story/49290215">systemd-journald writes 49KB+ per log line on ext4, 110KB+ on btrfs</a></li>

</ul>
</details>

**Tags**: `#systemd`, `#journald`, `#logging`, `#disk-io`, `#performance`

---

<a id="item-tech-news-9"></a>
### [AI Robotic Labs Scale Human Tissue Testing to 3 Million Samples a Year](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

Vivodyne has deployed 12 “hive” robotic laboratories south of San Francisco that grow human tissue in closet-sized machines and use AI-designed experiments to test drug efficacy and safety. The system can run controlled experiments on more than 3 million human tissue samples per year, a capacity roughly double the total volume of all U.S. clinical trials combined. Vivodyne positions this as a way to better predict clinical outcomes at a time when approximately 90% of clinical trials still fail after passing animal tests. The scale-up is aimed at making animal testing obsolete by replacing some of those preclinical screens with human-relevant tissue assays.

telegram · zaihuapd · Aug 14, 01:48

**「Background」** Animal testing has long been the standard for preclinical drug safety and efficacy checks, but it often fails to predict human responses, with about 90% of clinical trials failing after passing animal tests. Vivodyne is a biotech company developing automated robotic platforms and AI to grow and analyze thousands of functional human tissues outside the body, aiming to replace animal testing and improve clinical trial success rates. In May 2025, the company announced $40 million in funding to expand this approach and open a fully robotic lab in San Francisco.

**「Impact」** For drug developers, the system offers a high-throughput human-tissue screening option that could identify ineffective or unsafe drug candidates earlier and reduce reliance on animal testing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businesswire.com/news/home/20250528498236/en/Vivodyne-to-Replace-Animal-Testing-With-$40-Million-Funding-to-Reverse-95-Clinical-Trial-Failure-Rate">Vivodyne to Replace Animal Testing With $40 Million Funding ...</a></li>
<li><a href="https://firstwordpharma.com/story/5967233">Vivodyne raises $40M to replace animal testing with AI and ...</a></li>

</ul>
</details>

**Tags**: `#AI-driven drug discovery`, `#robotic lab automation`, `#human tissue engineering`, `#animal testing alternatives`, `#biotech`

---

<a id="item-tech-news-10"></a>
### [Xiaohongshu Open-Sources 280B MoE Model with 16B Active Parameters](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

Xiaohongshu&\#x27;s dots lab has open-sourced dots3-note preview, the first open-weight model in the dots3 series, with 280B total parameters and only 16B active parameters per inference. The model supports a 512K context window and handles text, images, video, and audio inputs. It introduces TEMPO, a new reinforcement learning method that trains long-horizon agents using self-criticism and test-time value estimation. The weights are available on Hugging Face, and the release also includes two new real-world agent benchmarks, VibeSearchBench and VibeLifeBench.

telegram · zaihuapd · Aug 14, 08:27

**「Background」** Xiaohongshu&\#x27;s Dots Model Lab announced the open-sourcing of dots3-note-preview, the first open-weight model in its dots3 series, targeting long-horizon tasks. It is a Mixture-of-Experts \(MoE\) model with 280B total parameters and only 16B activated parameters, supporting a context length of up to 512K tokens. In an MoE architecture, all 280B weights are stored but only 16B are used per token, which reduces inference cost. The model introduces the TEMPO reinforcement learning method, which trains agents using self-critique and test-time value estimation, and is accompanied by two real-world agent benchmarks, VibeSearchBench and VibeLifeBench.

**「Impact」** AI/ML developers and researchers can now experiment with and fine-tune a large multimodal MoE model at a relatively low inference cost due to its 16B active parameters, while evaluating long-horizon agent behavior with the newly released benchmark suites. The new TEMPO reinforcement learning method offers a concrete, testable approach for improving agentic reasoning through self-criticism, though the model is only a preview release and not yet fully proven for production use.

<details><summary>References</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3938759517896072">Xiaohongshu Open -Sourced Dots 3 - Note : The Same-Series Model ...</a></li>
<li><a href="https://github.com/studio-dots-ai/dots3-note-prev">GitHub - studio- dots -ai/ dots 3 - note -prev: dots 3 note preview · GitHub</a></li>
<li><a href="https://www.remio.ai/post/xiaohongshu-dots-model-claims-an-imo-2026-perfect-score-but-verification-is-the">Xiaohongshu dots Model Claims an IMO 2026 Perfect Score, but...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#MoE`, `#multimodal`, `#reinforcement learning`, `#AI models`

---

<a id="item-tech-news-11"></a>
### [Bluesky Launches Protocol Services with Easy Firehose Access](https://atproto.com/blog/introducing-bluesky-protocol-services) ⭐️ 7.0/10

Bluesky announced Bluesky Protocol Services, a set of hosted infrastructure offerings built around AT Protocol, including Jetstream, a lightweight firehose endpoint that can be consumed directly in the browser without running a server. The launch reflects Bluesky&\#x27;s push to expand its protocol beyond the Bluesky app, giving developers simpler access to real-time firehose data. The announcement drew practical developer interest, with community members immediately updating demos to use Jetstream, though others noted concerns about Bluesky&\#x27;s VC-backed funding sustainability and a shrinking active user base as the company expands beyond the app.

hackernews · danabramov · Aug 14, 00:14 · [Discussion](https://news.ycombinator.com/item?id=49293324)

**「Background」** Bluesky Protocol Services is a rebranded hub for the public infrastructure Bluesky runs on the AT Protocol, replacing the previous docs.bsky.app domain and introducing Jetstream v2 with Network Replay, which lets developers backfill historical network data from compressed archives and then seamlessly switch to a live WebSocket stream. Jetstream is a lightweight way to consume Bluesky&\#x27;s firehose of public posts, and it can be used directly in a browser without running a server. This expansion reflects Bluesky&\#x27;s move to support open-network developers beyond its main app.

**「Impact」** Developers can now start consuming the Bluesky firehose much more easily via Jetstream, including directly from the browser, lowering the barrier for building real-time AT Protocol tools and demos.

**「Community Discussion」** Commenters praised Jetstream for being incredibly easy to use, with Simon Willison updating his browser-based firehose demo to use it immediately. Others floated broader ideas like rebuilding DNS on Bluesky, while expressing skepticism about the project&\#x27;s VC funding and a shrinking active user base.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.com/blog/introducing-bluesky-protocol-services">Introducing Bluesky Protocol Services - AT Protocol</a></li>
<li><a href="https://zeli.app/en/story/49293324">Bluesky launches Protocol Services with Jetstream v2 network replay</a></li>
<li><a href="https://news.linxi.com.au/news/bluesky-unveils-protocol-services-and-jetstream-v2-with-network-replay">Bluesky Unveils Protocol Services and Jetstream v2 with Network Replay</a></li>

</ul>
</details>

**Tags**: `#bluesky`, `#atproto`, `#decentralized protocols`, `#open source`, `#jetstream`

---

<a id="item-tech-news-12"></a>
### [Pi&\#x27;s Context Compaction: How It Works and Its Limits](https://earendil.com/posts/compaction-in-pi/) ⭐️ 7.0/10

A technical post on earendil.com, authored by tosh, explains how context compaction works in Pi, an AI system, detailing the approach to condensing conversation history as context windows fill. The topic matters for engineers building LLM agents because effective context-window management determines how long agentic workflows can run before losing fidelity. The surrounding Hacker News discussion treats compaction as a lossy but often necessary operation and explores alternative strategies. Since the original article body was not included in the supplied item, this summary relies on the item&\#x27;s analysis summary and the supplied comments.

hackernews · tosh · Aug 13, 17:57 · [Discussion](https://news.ycombinator.com/item?id=49289654)

**「Background」** In AI chat systems, context compaction condenses conversation history into a shorter summary to fit within a model&\#x27;s fixed context window. The Pi assistant performs compaction separately from regular conversation: it sends a standalone request with a distinct system prompt that instructs the model to act as a context summarization assistant. Pi&\#x27;s auto-compaction operates around the model&\#x27;s full context window using generic summarization instructions, and it recalculates token counts from the rebuilt session context, preserving messages that survived earlier compaction so they are included in the next summarization pass.

**「Community Discussion」** Commenters generally agree that compaction can be painful and may lose conversational intent; some prefer pruning low-value messages or avoiding compaction entirely by keeping context utilization below about 30% and using tree/branch summaries for asides. Implementation suggestions include running two KV caches so one model compacts while another generates tokens, while another commenter notes that prompt caching discourages more creative compaction techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://earendil.com/posts/compaction-in-pi/">How Compaction Works in Pi | EARENDIL</a></li>
<li><a href="https://pi.dev/docs/latest/compaction">Compaction &amp; Branch Summarization · Documentation · Pi</a></li>
<li><a href="https://github.com/easiest-ai/pi-compaction-manager">GitHub - easiest-ai/pi-compaction-manager: Makes pi&#x27;s auto ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#context-window`, `#compaction`, `#AI-agents`, `#infrastructure`

---

<a id="item-tech-news-13"></a>
### [657,607 Links Show Where the Old Web Went](https://0.mk/blog/link-rot) ⭐️ 7.0/10

A data-driven blog investigation followed 657,607 links to explore link rot and the disappearance of the old web. The analysis addresses how dead hyperlinks and shifting internet culture have removed much of the early web from view. Specific findings were not available in the supplied context, but the scale of the dataset is notable. The work touches on debates among web developers and historians about what the old web was and when it ended.

hackernews · tdx · Aug 13, 17:49 · [Discussion](https://news.ycombinator.com/item?id=49289532)

**「Background」** The study analyzed 657,607 links gathered from the old web, of which 162,826 were duplicates pointing to the same destination, leaving 494,781 distinct URLs and 492,620 crawlable ones. It found that roughly 76.7% of those old links were dead, and also uncovered oddities such as the first shortened link and a link to localhost. Link rot is the process by which web links become inaccessible over time as pages are removed or domains expire, a key concern in web preservation and digital history.

**「Impact」** For web developers and digital archivists, the study illustrates that link rot is measurable at a large scale and reinforces the importance of link-preservation efforts.

**「Community Discussion」** Commenters largely disagreed about when the &\#x27;old web&\#x27; ended, with suggestions ranging from before Google&\#x27;s public search \(pre-1997\), Facebook&\#x27;s rise, and the 2009-2014 era to as late as 2023 with AI. Several argued that the nostalgia for the old web is itself a cultural phenomenon tied to when each person discovered online communities.

<details><summary>References</summary>
<ul>
<li><a href="https://0.mk/blog/link-rot">Where did the old web go ? We followed 657 , 607 links to find out .</a></li>
<li><a href="https://zeli.app/en/story/49289532">76.7% of old web links are dead: a 657 , 607 - link autopsy — Where ...</a></li>

</ul>
</details>

**Tags**: `#link rot`, `#web history`, `#data analysis`, `#internet culture`

---

<a id="item-tech-news-14"></a>
### [City2Graph turns urban geospatial data into graph-ready Python library](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph is a newly published open-source Python library that converts urban geospatial data into analysis-ready heterogeneous graphs for spatial analysis, network analysis, and Graph Neural Networks \(GeoAI\). It supports morphological graphs from OpenStreetMap and Overture Maps, transportation graphs from GTFS and GBFS feeds via DuckDB, mobility and flow graphs from OD matrices, and proximity/contiguity graphs using KNN, Delaunay, Gilbert, Waxman, and queen/rook contiguity. It provides round-trip conversions between GeoDataFrames, NetworkX, rustworkx, and PyTorch Geometric Data/HeteroData, preserving geometries and attributes. The companion paper by Sato, Pietrostefani, Mahabir, and Arribas-Bel was published in Computers, Environment and Urban Systems, volume 130, article 102492 \(2026\). The library is available at https://github.com/c2g-dev/city2graph.

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · Aug 13, 11:59

**「Background」** Urban analytics increasingly models cities as graphs, where entities such as buildings, streets, transit stops, and neighborhoods are nodes and their relationships are edges. Heterogeneous graphs extend this by allowing multiple node and edge types, which suits the multi-layered structure of cities. City2Graph aims to automate the often laborious step of turning raw geospatial data into such graphs for Graph Neural Networks \(GNNs\).

**「Impact」** Urban researchers and GeoAI practitioners can now use City2Graph to go directly from OpenStreetMap, Overture Maps, GTFS/GBFS, and OD flow data to PyTorch Geometric graph objects, reducing the engineering overhead in GNN-based urban studies.

**Tags**: `#python`, `#graph-neural-networks`, `#geospatial`, `#urban-systems`, `#open-source`

---

<a id="item-tech-news-15"></a>
### [Pixel metrics often can&\#x27;t rank world models on real robot video](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

A researcher released worldproof, an open-source tool for diagnosing world-model failures, and used it to show that pixel metrics can fail to rank world models on real robot video. A last-frame baseline \(“predict nothing changes”\) achieved 0.983 SSIM and 53.9 dB PSNR on a 30fps SO-101 arm recording with a 6-step horizon, and the error did not grow with horizon. On DROID footage at 15fps, the same baseline separated models only between roughly steps 8 and 24, tying at both ends; step 0 inflation also skewed horizon-averaged scalars. The tool is Apache-2.0, pip-installable, runs without a GPU, and reads LeRobotDataset v3.0 directly.

reddit · r/MachineLearning · /u/georgia\_bucea · Aug 13, 19:58

**「Background」** World models are neural networks that predict future frames from context and actions; evaluating them usually relies on pixel metrics such as SSIM and PSNR that compare generated frames to ground truth. This post demonstrates an evaluation pitfall: a trivial copy-last-frame baseline can produce high pixel scores and flat error curves on real robot video, giving an evaluation setup that cannot discriminate between models.

**「Impact」** Practitioners evaluating world models on real robot video should measure horizon curves and run naive baselines before trusting pixel-metric rankings, since both ends of the horizon often produce ties.

**Tags**: `#world models`, `#evaluation metrics`, `#SSIM`, `#PSNR`, `#robotics`

---

<a id="item-tech-news-16"></a>
### [X Open-Sources More Ranking Algorithm Code, Adds Transparency Tool](https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/) ⭐️ 7.0/10

X expanded its open-source release by publishing its “For You” timeline and core ranking engine code on GitHub under the Apache 2 license, with the codebase now roughly 10 to 15 times larger than the previous release. The company also introduced a transparency tool in Settings that lets users who posted at least 10 times in the past month download a JSON file to see whether their account or posts were flagged by the ranking system. The tool is initially available only to test users whose accounts have been registered for at least one year. Some Grok-based systems used to determine rule violations were not included in the public release. The move gives developers and users greater visibility into how X’s ranking system treats content.

telegram · zaihuapd · Aug 14, 01:03

**「Background」** Social platforms use ranking algorithms to decide which posts appear prominently, and concerns about hidden visibility restrictions, often called shadowbanning, have driven demand for algorithmic transparency. X had previously open-sourced some of its recommendation code, and this release significantly expands the available code while adding a direct way for eligible users to inspect ranking flags applied to their own accounts and posts.

**「Impact」** Active X users who meet the posting and account-age requirements can download a JSON file to check if the ranking system flagged their account or posts, while developers gain a substantially larger Apache-2.0-licensed codebase to analyze and build upon.

**Tags**: `#open source`, `#algorithms`, `#transparency`, `#social media`, `#AI`

---

<a id="item-tech-news-17"></a>
### [Apple Proposes Up to 15% Commission for External Purchases in US](https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/) ⭐️ 7.0/10

Apple has submitted a proposal to the court outlining commissions for external purchases made outside the US App Store, with rates capped at 15%. Standard apps would pay 15%, video and news partnership programs and subscription renewals would pay 10%, and apps enrolled in the Small Business Program would pay 5%. The filing follows the Supreme Court&\#x27;s denial of Apple&\#x27;s request to pause lower court proceedings on the rates. Epic Games will have an opportunity to respond, and Apple is expected to submit written arguments to the Supreme Court by September 14. These proposed rates are part of the ongoing Epic Games antitrust case and would apply to purchases made through external links in the United States.

telegram · zaihuapd · Aug 14, 02:33

**「Background」** Apple and Epic Games have been in litigation since August 2020 over App Store rules, including whether developers may steer users to external payment systems. A California district judge found Apple had &quot;willfully&quot; failed to comply with an earlier injunction and ruled in April 2025 that Apple cannot currently take a commission on external purchases. This dispute concerns the commission rates Apple may charge for purchases made through linkouts outside the App Store, including its proposed 15% standard rate, 10% for certain subscriptions, and 5% for small business program apps.

**「Impact」** Developers selling digital goods through the US App Store would face commission fees of up to 15% on external purchases, with lower rates for subscription renewals and small business program members, depending on court approval.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Apple">Epic Games v. Apple - Wikipedia</a></li>
<li><a href="https://www.theverge.com/tech/979967/apple-epic-games-external-links-fees-filing">Apple and Epic argue over how much Apple should get from purchases made outside the App Store | The Verge</a></li>
<li><a href="https://appleinsider.com/articles/26/08/13/apples-latest-commission-rates-for-external-app-store-purchases-havent-satisfied-epic">Apple&#x27;s latest commission rates for external App Store purchases haven&#x27;t satisfied Epic</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Store`, `#Epic Games`, `#commissions`, `#developers`

---

<a id="item-tech-news-18"></a>
### [Judge orders Google to remove Play Store barriers for rival app stores](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

U.S. District Judge James Donato ordered Google to remove what the court called deliberately created “anti-competitive friction” in the Play Store that blocks competing Android app stores. Google must make installing third-party stores as direct as installing ordinary Android apps and has one week to eliminate extra steps and warning pop-ups. The order stems from Epic v. Google, after a jury found Google held an illegal monopoly in Android app distribution. The changes are intended to stop scare tactics that deter average users from installing alternative marketplaces.

telegram · zaihuapd · Aug 14, 09:55

**「Background」** The order stems from Epic Games v. Google, an antitrust case in which a jury found that Google illegally monopolized Android app distribution through the Play Store. In October 2024, U.S. District Judge James Donato issued a permanent injunction requiring Google to open the Play Store to third-party app stores for three years. The current ruling follows that injunction, specifically targeting the extra warning dialogs and multi-step install flows that Google used to deter users from installing competing app stores.

**「Impact」** Third-party Android app store operators and users should soon encounter a more direct installation flow for competing marketplaces, reducing the warning screens and extra steps Google previously imposed. The practical effect depends on Google’s compliance within the one-week deadline.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Google">Epic Games v . Google - Wikipedia</a></li>
<li><a href="https://www.theverge.com/policy/2024/10/7/24243316/epic-google-permanent-injunction-ruling-third-party-stores">Google must crack open Android for third - party stores , rules Epic ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Antitrust`, `#Google`, `#App Stores`, `#Legal`

---

## Financial News

<a id="item-finance-news-1"></a>
### [S&amp;P 500 net profit margins reach record high in Q2](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 8.0/10

S&amp;P 500 companies are on track for a record net profit margin of 16.9% in the second quarter, according to FactSet data cited by CNBC, up from 14.8% in the first quarter and 12.9% a year earlier.

rss · CNBC Finance · Aug 13, 20:21

**「Background」** Net profit margin is the share of revenue left after all expenses; strong demand and operating leverage have helped companies convert more sales into profit, with gains broad across most sectors.

**Tags**: `#profit margins`, `#S&amp;P 500`, `#earnings`, `#stock market`, `#corporate profitability`

---

<a id="item-finance-news-2"></a>
### [U.S. Imposes Tariffs Up to 100% on Some Imported Drones](https://www.whitehouse.gov/presidential-actions/2026/08/adjusting-imports-of-unmanned-aircraft-systems-and-unmanned-aircraft-systems-components-into-the-united-states/) ⭐️ 8.0/10

President signed a proclamation on August 13 imposing a 100% tariff, effective September 3, 2026, on imported drones with maximum takeoff weight above 25 kg, drones equipped with thermal imagers, drone base stations, and certain key components, and a 25% tariff on drones weighing 25 kg or less. Another 25% tariff on certain drone components will take effect on February 9, 2027, and the proclamation authorizes the Commerce Secretary to include more components in the tariff scope.

telegram · zaihuapd · Aug 14, 01:24

**「Background」** The U.S. drone market relies heavily on imported aircraft and components, and the administration has framed these tariffs as a way to cut that dependence and counter China&\#x27;s leading role in drone manufacturing.

**「Impact」** U.S. businesses and agencies that buy imported drones—especially larger models over 25 kg and thermal-imaging versions—will see their costs rise sharply when the 100% tariff takes effect in September 2026, with smaller drones and components facing a 25% duty, a move aimed at reducing reliance on Chinese suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-13/trump-imposes-100-tariffs-on-certain-drones-countering-china">Trump Imposes 100 % Tariffs on Some Drones ... - Bloomberg</a></li>
<li><a href="https://www.datamintelligence.com/news/trump-drone-tariffs-2026-impact-on-global-drone-market-us-china-uav-supply-chain">Trump Drone Tariffs 2026: 100 % Duty on Chinese UAV Imports...</a></li>
<li><a href="https://www.newsy-today.com/trump-imposes-new-tariffs-of-up-to-100/">Trump Imposes New Tariffs of Up to 100 % - Newsy Today</a></li>
<li><a href="https://www.thevideshi.com/articles/trump-imposes-100-percent-tariff-drones-counter-china">Trump Imposes Up to 100 % Tariffs on Drone Imports... — The Videshi</a></li>

</ul>
</details>

**Tags**: `#无人机关税`, `#美国贸易政策`, `#进口限制`, `#白宫公告`, `#无人机行业`

---

<a id="item-finance-news-3"></a>
### [Premarket movers: Reddit jumps on S&amp;P 500 inclusion; Applied Materials slides on earnings](https://www.cnbc.com/2026/08/14/stocks-making-the-biggest-moves-premarket-rddt-amat-sndk-w.html) ⭐️ 7.0/10

In premarket trading, Reddit surged 12% after S&amp;P Dow Jones Indices said it will join the S&amp;P 500 starting Aug. 18, and Applied Materials lost more than 5% after reporting adjusted earnings of $3.50 per share on revenue of $9.12 billion. Wayfair, Fox, Sandisk, and Workday also moved on analyst upgrades or a reported buyout approach.

rss · CNBC Finance · Aug 14, 10:46

**「Background」** Premarket moves reflect investor reactions to news before the regular U.S. session; joining the S&amp;P 500 typically triggers buying by index funds.

**Tags**: `#premarket`, `#S&amp;P 500`, `#earnings`, `#M&amp;A`, `#analyst upgrades`

---

<a id="item-finance-news-4"></a>
### [Ackman&\#x27;s Pershing Square takes new Netflix stake after four-year break](https://www.cnbc.com/2026/08/13/ackman-buys-netflix-again-four-years-later-says-it-won-streaming-wars.html) ⭐️ 7.0/10

Bill Ackman&\#x27;s Pershing Square disclosed a new Netflix position, saying the streaming platform has &quot;effectively won the streaming wars&quot; and that its valuation is attractive after shares fell about 50% from their June 2025 high; Pershing put the stock at roughly 21 times forward earnings, down from more than 40 times.

rss · CNBC Finance · Aug 13, 18:04

**「Background」** Ackman had built a large Netflix stake in early 2022 but sold it about three months later after the company reported its first subscriber decline in more than a decade and he said its business-model changes made future prospects too hard to predict.

**Tags**: `#Bill Ackman`, `#Netflix`, `#Pershing Square`, `#streaming`, `#investment`

---

<a id="item-finance-news-5"></a>
### [Eisman warns AI boom depends on OpenAI and Anthropic](https://www.cnbc.com/2026/08/13/big-short-investor-steve-eisman-sees-an-achilles-heel-in-the-ai-boom.html) ⭐️ 7.0/10

Investor Steve Eisman warned that the AI boom is increasingly dependent on OpenAI and Anthropic, saying the two startups account for roughly 70% of AI-related revenue at Microsoft, Amazon, Alphabet’s Google and Oracle, and as much as 25% to 35% of those companies’ cloud revenue. He said cheaper Chinese open-source AI models could gain market share and trigger a price war if OpenAI or Anthropic stumble.

rss · CNBC Finance · Aug 13, 15:16

**「Background」** Eisman, known for betting against mortgages before the 2008 financial crisis, is adding to a debate over whether heavy AI spending will generate sufficient returns.

**Tags**: `#AI boom`, `#Big Tech`, `#OpenAI`, `#Anthropic`, `#China AI`

---