# Veytrix public documentation

**Discover. Connect. Understand.** A curated, public introduction to the Veytrix OT Asset & Security Intelligence platform.

Read the [published site](https://veytrixot.github.io/veytrix-docs-public/) or preview locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Run `mkdocs build --strict` before a PR. Merges to `main` build and deploy through [the GitHub Pages workflow](.github/workflows/pages.yml). Enable Pages with **GitHub Actions** as its source in repository settings. This repo contains only externally reviewed content; detailed architecture, security, decisions, and agent definitions live in the private `veytrix-docs` repository. Do not copy internal source material into this public tree wholesale.

Brand colors and the geometric-V artwork derive from the Veytrix brand kit. The editable vector is an approximation of the approved visual reference; review production artwork and brand clearance before broader use.
