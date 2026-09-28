# AIM4R UI refresh — 2026-09-28

## Reference projects

- https://github.com/withastro/starlight — checked this session, latest commit 2026-09-28. Reference for reading controls and content navigation.
- https://github.com/just-the-docs/just-the-docs — checked this session, latest commit 2026-09-23. Reviewed responsive sidebar and bounded reading layout.

Continues the Plastic Signal UI work with a distinct blue/orange research-desk design. No external project source was copied or new runtime dependencies added.

## Behavior

- Bilingual latest-edition card with real date and excerpt, followed by the complete language-specific archive.
- Date/title search, clear no-results state and live result count.
- Persistent language preference; article language links only appear when a matching published counterpart exists.
- Light/dark/system theme and standard/large text preferences.
- Article table of contents, bounded reading width, source metadata and existing score badges.
- Native keyboard controls, skip link, focus indicators, reduced-motion support.
- Existing content generation, RSS and deployment workflow preserved. Published posts live on gh-pages; main contains an older sample.

## Validation

JavaScript syntax and Git whitespace checks passed. Liquid previews used 16 actual gh-pages posts, latest 2026-09-28, with temporary Python Liquid/Markdown rendering (not Jekyll).

Headless Chrome checked home and both article languages at 1440/390/320px: no horizontal overflow or runtime exceptions. Language switching, search empty/reset, preference persistence and generated contents navigation passed. Desktop/mobile screenshots visually reviewed. Full Jekyll validation is performed by the GitHub Pages deployment.
