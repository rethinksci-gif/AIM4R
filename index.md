---
layout: default
page_kind: home
lang: zh-CN
title: AIM4R · 材料研发研究雷达
description: AI for Materials R&D & Manufacturing — 面向材料研发工程师的研究雷达：值得读什么、证据到哪里、下一步验证什么。
---

{% assign languages = 'zh,en' | split: ',' %}
{% assign radar_runs = site.data.aim4r_history.runs %}
{% for language in languages %}
{% assign posts = site.posts | where: 'lang', language %}
{% assign editions = posts | where: 'edition', 'research-radar' %}
{% assign latest = editions | first %}
<div class="digest-language" id="lang-{{ language }}" lang="{{ language }}">
  <section class="research-hero">
    <div class="hero-intro">
      <p class="eyebrow"><span class="live-dot"></span> AIM4R / AI FOR MATERIALS R&amp;D &amp; MANUFACTURING</p>
      {% if language == 'zh' %}
      <h1>材料研发的 AI 研究雷达。<br><span>先看证据，再谈意义。</span></h1>
      <p class="hero-copy">每天从论文、预印本、研究机构和工业来源中筛选最多三条值得读的原文，说明它新增了什么、证据成立在什么材料和条件上、哪里还没有被证明，以及下一步可以验证什么。没有合格内容的日子不凑数。</p>
      {% else %}
      <h1>An AI research radar for materials R&amp;D.<br><span>Evidence first, significance second.</span></h1>
      <p class="hero-copy">Each day, at most three originals worth reading — from papers, preprints, research labs and industry — with what is new, which materials and conditions the evidence covers, what is not yet shown, and what to verify next. Quiet days stay empty.</p>
      {% endif %}
      <ul class="topic-strip" aria-label="{% if language == 'zh' %}关注方向{% else %}Coverage{% endif %}">
        {% if language == 'zh' %}
        <li><a href="#topics-{{ language }}-ai-materials">AI × 材料与聚合物研发</a></li>
        <li><a href="#topics-{{ language }}-lab-automation">实验自动化与制造闭环</a></li>
        <li><a href="#topics-{{ language }}-data-trust">数据上下文、验证与可信决策</a></li>
        <li><a href="#topics-{{ language }}-transferable-methods">可迁移方法与开源工具</a></li>
        {% else %}
        <li><a href="#topics-{{ language }}-ai-materials">AI × Materials &amp; Polymer R&amp;D</a></li>
        <li><a href="#topics-{{ language }}-lab-automation">Lab Automation &amp; Manufacturing Loops</a></li>
        <li><a href="#topics-{{ language }}-data-trust">Data Context, Validation &amp; Trust</a></li>
        <li><a href="#topics-{{ language }}-transferable-methods">Transferable Methods &amp; Open Tools</a></li>
        {% endif %}
      </ul>
    </div>
    <aside class="latest-card">
      <p class="eyebrow">{% if language == 'zh' %}最新一期{% else %}LATEST EDITION{% endif %} <span aria-hidden="true">↗</span></p>
      {% if latest %}
      <time class="latest-date" datetime="{{ latest.date | date_to_xmlschema }}">{{ latest.date | date: '%m.%d' }}<small>{{ latest.date | date: '%Y' }} / {{ language | upcase }}</small></time>
      <ol class="latest-picks">
        {% for pick in latest.picks %}
        <li><a href="{{ latest.url | relative_url }}#{{ pick.anchor }}"><strong>{{ pick.title | escape }}</strong>{% if pick.why %}<span>{{ pick.why | escape }}</span>{% endif %}</a></li>
        {% endfor %}
      </ol>
      <a class="primary-action" href="{{ latest.url | relative_url }}">{% if language == 'zh' %}阅读本期{% else %}Read this edition{% endif %}<span aria-hidden="true">→</span></a>
      {% else %}
      <h2>{% if language == 'zh' %}第一期研究雷达即将发布{% else %}The first radar edition is coming{% endif %}</h2>
      <p>{% if language == 'zh' %}新定位的首期发布后会显示在这里；往期通用科技简报仍保留在下方归档中。{% else %}The first edition under the new focus will appear here; earlier general tech digests remain in the archive below.{% endif %}</p>
      {% endif %}
    </aside>
  </section>

  {% if radar_runs %}
  <section class="run-status" aria-labelledby="status-{{ language }}">
    <h2 class="section-number" id="status-{{ language }}">{% if language == 'zh' %}最近运行状态{% else %}RECENT RUNS{% endif %}</h2>
    <ol class="run-list">
      {% for run in radar_runs limit: 7 %}
      <li data-status="{{ run.status }}"><time>{{ run.date }}</time>
        <span class="run-label">{% case run.status %}
          {% when 'published' %}{% if language == 'zh' %}已发布 {{ run.selected }} 条{% else %}{{ run.selected }} published{% endif %}
          {% when 'published_degraded' %}{% if language == 'zh' %}已发布 {{ run.selected }} 条 · 部分来源失败{% else %}{{ run.selected }} published · some sources failed{% endif %}
          {% when 'no_qualified' %}{% if language == 'zh' %}无合格内容（筛查 {{ run.screened }} 条）{% else %}Nothing qualified ({{ run.screened }} screened){% endif %}
          {% when 'no_new_items' %}{% if language == 'zh' %}无新内容{% else %}No new items{% endif %}
          {% when 'source_failure' %}{% if language == 'zh' %}采集失败{% else %}Collection failed{% endif %}
          {% when 'processing_failure' %}{% if language == 'zh' %}处理失败{% else %}Processing failed{% endif %}
          {% when 'editorial_preview' %}{% if language == 'zh' %}编辑预览（非正式发布）{% else %}Editorial preview (not published){% endif %}
          {% when 'already_published' %}{% if language == 'zh' %}重跑：当日已发布{% else %}Rerun: already published{% endif %}
          {% else %}{{ run.status }}
        {% endcase %}</span>{% if run.failed_sources.size > 0 %}<span class="run-failed">{% if language == 'zh' %}失败来源{% else %}Failed{% endif %}: {{ run.failed_sources | join: ', ' | escape }}</span>{% endif %}</li>
      {% endfor %}
    </ol>
  </section>
  {% endif %}

  <section class="topic-browse" aria-labelledby="topics-heading-{{ language }}">
    <div class="archive-heading"><div><p class="section-number">{% if language == 'zh' %}按主题浏览{% else %}BROWSE BY TOPIC{% endif %}</p><h2 id="topics-heading-{{ language }}">{% if language == 'zh' %}近期精选{% else %}Recent picks{% endif %}</h2></div></div>
    <div class="topic-grid">
      {% assign topic_ids = 'ai-materials,lab-automation,data-trust,transferable-methods' | split: ',' %}
      {% for topic_id in topic_ids %}
      <article class="topic-column" id="topics-{{ language }}-{{ topic_id }}">
        <h3>{% case topic_id %}
          {% when 'ai-materials' %}{% if language == 'zh' %}AI × 材料与聚合物研发{% else %}AI × Materials &amp; Polymer R&amp;D{% endif %}
          {% when 'lab-automation' %}{% if language == 'zh' %}实验自动化与制造闭环{% else %}Lab Automation &amp; Manufacturing Loops{% endif %}
          {% when 'data-trust' %}{% if language == 'zh' %}数据上下文、验证与可信决策{% else %}Data Context, Validation &amp; Trust{% endif %}
          {% else %}{% if language == 'zh' %}可迁移方法与开源工具{% else %}Transferable Methods &amp; Open Tools{% endif %}
        {% endcase %}</h3>
        <ul>
          {% assign shown = 0 %}
          {% for edition in editions %}{% for pick in edition.picks %}{% if pick.topic == topic_id and shown < 5 %}
          <li><a href="{{ edition.url | relative_url }}#{{ pick.anchor }}">{{ pick.title | escape }}</a><span class="topic-meta">{{ edition.date | date: '%m-%d' }}{% if pick.track == 'explore' %} · {% if language == 'zh' %}探索{% else %}explore{% endif %}{% endif %}</span></li>
          {% assign shown = shown | plus: 1 %}
          {% endif %}{% endfor %}{% endfor %}
          {% if shown == 0 %}<li class="topic-empty">{% if language == 'zh' %}暂无精选{% else %}No picks yet{% endif %}</li>{% endif %}
        </ul>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="archive-section" id="archive-{{ language }}">
    <div class="archive-heading"><div><p class="section-number">{% if language == 'zh' %}归档 / {{ posts.size }} 期{% else %}THE ARCHIVE / {{ posts.size }} EDITIONS{% endif %}</p><h2>{% if language == 'zh' %}全部期次{% else %}All editions{% endif %}</h2></div><a href="{{ '/feed-' | append: language | append: '.xml' | relative_url }}">{% if language == 'zh' %}订阅中文 RSS{% else %}Subscribe via RSS{% endif %} ↗</a></div>
    <div class="archive-tools"><label for="search-{{ language }}">{% if language == 'zh' %}查找期次{% else %}Find an edition{% endif %}</label><input id="search-{{ language }}" type="search" placeholder="{% if language == 'zh' %}输入日期或标题，如 2026-10{% else %}Date or title, e.g. 2026-10{% endif %}" aria-controls="list-{{ language }}"><span class="search-count" role="status" aria-live="polite"></span></div>
    <div class="issue-list" id="list-{{ language }}">
      {% for post in posts %}<a class="issue-row" href="{{ post.url | relative_url }}"><time class="issue-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y-%m-%d' }}</time><span class="issue-title">{% if post.edition == 'research-radar' %}{{ post.title | escape }}<small>{% if language == 'zh' %}{{ post.picks_count }} 条精选{% else %}{{ post.picks_count }} picks{% endif %}{% for pick in post.picks limit: 2 %} · {{ pick.title | escape }}{% endfor %}</small>{% else %}{% if language == 'zh' %}{{ post.title | replace: 'Horizon Summary:', 'AIM4R 日报 ·' | remove: '(ZH)' | escape }}<small>旧版通用科技简报</small>{% else %}{{ post.title | replace: 'Horizon Summary:', 'AIM4R Digest ·' | remove: '(EN)' | escape }}<small>Earlier general tech digest</small>{% endif %}{% endif %}</span><span class="issue-arrow" aria-hidden="true">↗</span></a>{% else %}<p>{% if language == 'zh' %}暂无期次。{% else %}No editions yet.{% endif %}</p>{% endfor %}
    </div>
    <p class="search-empty" hidden>{% if language == 'zh' %}没有匹配的期次，请尝试其他日期或关键词。{% else %}No matching editions. Try another date or keyword.{% endif %}</p>
  </section>
  <section class="research-note"><span class="section-number">{% if language == 'zh' %}如何阅读{% else %}READ WITH CONTEXT{% endif %}</span><p>{% if language == 'zh' %}每条都标明来源类型、实际读到的范围（全文或仅摘要）和评审状态。摘要是线索，原文是依据；“自动检查”只核对摘录和数字能否在原文中找到，不等于事实核验。{% else %}Each pick shows its source type, how much of the original was actually read (full text or abstract only) and review status. Summaries are leads; the original is the evidence. Automatic checks only confirm that excerpts and numbers can be found in the source — they are not fact-checking.{% endif %}</p><a href="{{ '/method.html' | relative_url }}">{% if language == 'zh' %}选题标准与信息源{% else %}Selection method &amp; sources{% endif %} ↗</a></section>
</div>
{% endfor %}
