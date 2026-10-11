# AIM4R maintainer notes

AIM4R is a Horizon fork that publishes a materials R&D research radar to GitHub Pages.

- Production config: `data/config.material-intel.json` (profile `profiles/material-intel/`, renderer `research`).
  `data/config.json` is a private local config — do not overwrite it. `data/config.github.json` is the legacy general digest.
- Workflow: `.github/workflows/daily-summary.yml` (weekly, one-week window). Run history ledger lives at `docs/_data/aim4r_history.json`
  on gh-pages; it is restored before and published after every run. Never commit it to main.
- Tests: `uv sync --extra dev && uv run pytest`. Tests use scripted fake AI clients; never call paid APIs in tests.
- Sources: verify with `uv run python scripts/check_sources.py --probe-pages` before adding a feed. Do not add
  unverified feed URLs; list them as candidates in `docs/method.md`.
- Previews: `scripts/build_preview_edition.py` and `scripts/preview_site.py`; previews go in `docs/_previews/`
  (excluded from Jekyll) and must be marked `preview: true`. Mock data lives only in `tests/fixtures/` and must say MOCK.
- Rollout notes, root causes and unverified parts: `design/material-intel-rollout.md`.
