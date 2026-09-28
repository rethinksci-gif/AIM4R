---
layout: default
page_kind: home
lang: zh-CN
title: AIM4R · 每日研究情报
---

{% assign languages = 'zh,en' | split: ',' %}
{% for language in languages %}
{% assign posts = site.posts | where: 'lang', language %}
{% assign latest = posts | first %}
<div class="digest-language" id="lang-{{ language }}" lang="{{ language }}">
  <section class="research-hero">
    <div class="hero-intro">
      <p class="eyebrow"><span class="live-dot"></span> AIM4R / DAILY RESEARCH RADAR</p>
      <h1>{% if language == 'zh' %}追踪智能前沿。<br><span>连接研究与现实。</span>{% else %}Follow the frontier.<br><span>Connect the dots.</span>{% endif %}</h1>
      <p class="hero-copy">{% if language == 'zh' %}机器人、具身智能与材料研究的每日信息入口。汇集论文、技术动态与开源项目，从摘要出发，回到原始证据。{% else %}A daily entry point to robotics, embodied AI and materials research. Explore papers, technology news and open-source projects, then follow the evidence.{% endif %}</p>
      <div class="topic-strip"><span>01 / ROBOTICS</span><span>02 / EMBODIED AI</span><span>03 / MATERIALS</span></div>
    </div>
    <aside class="latest-card">
      <p class="eyebrow">{% if language == 'zh' %}最新日报{% else %}LATEST DIGEST{% endif %} <span aria-hidden="true">↗</span></p>
      {% if latest %}
      <time class="latest-date" datetime="{{ latest.date | date_to_xmlschema }}">{{ latest.date | date: '%m.%d' }}<small>{{ latest.date | date: '%Y' }} / {{ language | upcase }}</small></time>
      <h2>{% if language == 'zh' %}今天，值得关注什么？{% else %}What deserves your attention?{% endif %}</h2>
      <p>{{ latest.excerpt | strip_html | truncate: 100 }}</p>
      <a class="primary-action" href="{{ latest.url | relative_url }}">{% if language == 'zh' %}阅读最新一期{% else %}Read the latest digest{% endif %}<span aria-hidden="true">→</span></a>
      {% else %}<h2>{% if language == 'zh' %}日报即将更新{% else %}Your next briefing awaits{% endif %}</h2><p>{% if language == 'zh' %}新内容发布后将在这里显示。{% else %}New editions will appear here when published.{% endif %}</p>{% endif %}
    </aside>
  </section>
  <section class="archive-section" id="archive-{{ language }}">
    <div class="archive-heading"><div><p class="section-number">THE ARCHIVE / {{ posts.size }} {% if language == 'zh' %}期日报{% else %}EDITIONS{% endif %}</p><h2>{% if language == 'zh' %}每日速递{% else %}The daily archive{% endif %}</h2></div><a href="{{ '/feed-' | append: language | append: '.xml' | relative_url }}">{% if language == 'zh' %}订阅中文 RSS{% else %}Subscribe via RSS{% endif %} ↗</a></div>
    <div class="archive-tools"><label for="search-{{ language }}">{% if language == 'zh' %}查找日报{% else %}Find a digest{% endif %}</label><input id="search-{{ language }}" type="search" placeholder="{% if language == 'zh' %}输入日期或标题，如 2026-09{% else %}Date or title, e.g. 2026-09{% endif %}" aria-controls="list-{{ language }}"><span class="search-count" role="status" aria-live="polite"></span></div>
    <div class="issue-list" id="list-{{ language }}">
      {% for post in posts %}<a class="issue-row" href="{{ post.url | relative_url }}"><time class="issue-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y-%m-%d' }}</time><span class="issue-title">{% if language == 'zh' %}{{ post.title | replace: 'Horizon Summary:', 'AIM4R 日报 ·' | remove: '(ZH)' | escape }}{% else %}{{ post.title | replace: 'Horizon Summary:', 'AIM4R Digest ·' | remove: '(EN)' | escape }}{% endif %}</span><span class="issue-arrow" aria-hidden="true">↗</span></a>{% else %}<p>{% if language == 'zh' %}暂无日报。{% else %}No digests yet.{% endif %}</p>{% endfor %}
    </div>
    <p class="search-empty" hidden>{% if language == 'zh' %}没有匹配的日报，请尝试其他日期或关键词。{% else %}No matching digests. Try another date or keyword.{% endif %}</p>
  </section>
  <section class="research-note"><span class="section-number">READ WITH CONTEXT</span><p>{% if language == 'zh' %}摘要是线索，原文是依据。评分帮助安排阅读顺序；具体结论请结合原始来源判断。{% else %}Summaries are a starting point. Scores help prioritize reading; consult the original sources before drawing conclusions.{% endif %}</p><a href="{{ '/scoring.html' | relative_url }}">{% if language == 'zh' %}了解评分方式{% else %}How scoring works{% endif %} ↗</a></section>
</div>
{% endfor %}
