# Workshop Revival

The source for the Workshop Revival website: a practical record of repairing,
reusing, and repurposing discarded materials.

> “Where old stuff gets a new life and earns its keep.”

This is a dependency-free static website built with HTML, CSS, and a small
amount of vanilla JavaScript. It is intended for GitHub Pages at both:

- `https://chipswoodshop.github.io/workshop-revival/`
- `https://workshoprevival.com/`

All internal URLs are relative so either hosting path works. Hosting requires
no additional subscription: GitHub Pages provides the static hosting. The
domain is registered through Squarespace, which also manages its DNS.

## Preview locally

From the repository root, run:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000/`. Opening the HTML files directly also works,
but a local server more closely matches GitHub Pages.

## Validate

```sh
python3 scripts/validate_site.py
```

The validator uses only the Python standard library. It confirms that required
files exist and checks local page, stylesheet, script, and image references.

See [PROJECT.md](PROJECT.md) for scope, [TODO.md](TODO.md) for planned work,
and [AGENTS.md](AGENTS.md) for contributor guidance.
