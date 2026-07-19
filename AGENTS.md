# Contributor instructions

These instructions apply to the entire repository.

- The authoritative Workshop Revival vault notes are
  `Workshop Revival/10_Brand/Brand Guidelines.md`,
  `Workshop Revival/10_Brand/Visual Assets.md`, and
  `Workshop Revival/10_Brand/Voice & Tone.md`.
- Treat `docs/brand/` as the repository's working brand snapshot; Obsidian
  remains authoritative.
- Never use vault copies under `Nextcloud`, `Nextcloud_old`, `Trash`, or
  `Archive` as current sources.
- Keep the site dependency-free: plain HTML, CSS, and minimal vanilla JavaScript.
- Use relative URLs for internal pages and assets; never assume a domain root.
- Do not invent project facts, photography, dates, testimonials, or publication
  links. Mark missing content clearly.
- Preserve accessible semantics, visible keyboard focus, strong color contrast,
  reduced-motion preferences, and useful alternative text.
- Do not add tracking, cookies, external fonts, third-party scripts, or paid
  services without explicit owner approval.
- Run `python3 scripts/validate_site.py` after changing pages or local links.
- Record meaningful architecture/content-policy decisions in `DECISIONS.md` and
  user-visible changes in `CHANGELOG.md`.
- Do not change GitHub Pages settings, DNS, or external accounts from repository
  work. Do not commit or push unless explicitly requested.
