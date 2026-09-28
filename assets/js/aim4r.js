(function () {
  'use strict';
  var root = document.documentElement;
  var theme = document.getElementById('theme-setting');
  var size = document.getElementById('size-setting');
  function preference(key, fallback) {
    try { return localStorage.getItem('aim4r-' + key) || fallback; }
    catch (_) { return fallback; }
  }
  function apply(control, key, allowed, fallback) {
    var value = preference(key, fallback);
    if (allowed.indexOf(value) === -1) value = fallback;
    control.value = value;
    root.setAttribute('data-' + key, value);
    control.addEventListener('change', function () {
      root.setAttribute('data-' + key, control.value);
      try { localStorage.setItem('aim4r-' + key, control.value); } catch (_) { /* Optional persistence. */ }
    });
  }
  apply(theme, 'theme', ['system', 'light', 'dark'], 'system');
  apply(size, 'size', ['standard', 'large'], 'standard');
  var settings = document.querySelector('.reading-settings');
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && settings.open) {
      settings.open = false;
      settings.querySelector('summary').focus();
    }
  });
  document.addEventListener('click', function (event) {
    if (!settings.contains(event.target)) settings.open = false;
  });
  var languageButtons = document.querySelectorAll('button[data-lang]');
  var languageSections = document.querySelectorAll('.digest-language');
  function setLanguage(lang) {
    languageSections.forEach(function (section) { section.hidden = section.lang !== lang; });
    languageButtons.forEach(function (button) { button.setAttribute('aria-pressed', String(button.dataset.lang === lang)); });
    root.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelector('.site-masthead nav a').href = '#archive-' + lang;
    document.querySelector('.site-masthead nav a:nth-child(2)').href = 'feed-' + lang + '.xml';
    try { localStorage.setItem('aim4r-lang', lang); } catch (_) {}
  }
  if (languageSections.length) {
    setLanguage(preference('lang', 'zh') === 'en' ? 'en' : 'zh');
    languageButtons.forEach(function (button) { button.addEventListener('click', function () { setLanguage(button.dataset.lang); }); });
    if (location.hash === '#archive') document.querySelector('.digest-language:not([hidden]) .archive-section').scrollIntoView();
  }
  languageSections.forEach(function (section) {
    var input = section.querySelector('input[type="search"]');
    var rows = section.querySelectorAll('.issue-row');
    input.addEventListener('input', function () {
      var query = input.value.trim().toLocaleLowerCase();
      var count = 0;
      rows.forEach(function (row) { row.hidden = !row.textContent.toLocaleLowerCase().includes(query); if (!row.hidden) count++; });
      section.querySelector('.search-count').textContent = section.lang === 'zh' ? count + ' 期匹配' : count + ' matching editions';
      section.querySelector('.search-empty').hidden = count > 0;
    });
  });
  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn|telegram)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  processScoreBadges();
  markSemanticElements();
  var toc = document.querySelector('.article-toc');
  if (!toc) return;
  var headings = document.querySelectorAll('.article-content h2');
  headings.forEach(function (heading, index) {
    if (!heading.id) heading.id = 'section-' + (index + 1);
    var item = document.createElement('li');
    var link = document.createElement('a');
    link.href = '#' + heading.id;
    link.textContent = heading.textContent;
    item.appendChild(link);
    toc.querySelector('ol').appendChild(item);
  });
  toc.hidden = !headings.length;
})();
