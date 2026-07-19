# Decisions

## 001 — Dependency-free static architecture

**Status:** Accepted

Use semantic HTML, a shared CSS file, and minimal vanilla JavaScript. This keeps
the site durable, inexpensive, easy to audit, and directly compatible with
GitHub Pages without a build step.

## 002 — Relative internal URLs

**Status:** Accepted

Use document-relative paths rather than root-relative paths. The same files can
then run under the `/workshop-revival/` project path and at the custom-domain
root.

## 003 — Honest placeholders

**Status:** Accepted

Use styled, text-labeled placeholders for missing photography, publication
links, and project details. Placeholder links are not made clickable, avoiding
misleading or broken destinations.

## 004 — Workshop visual language

**Status:** Superseded by decision 005

Use warm beige surfaces, near-black charcoal, muted steel gray, and restrained
oxide red. Strong borders, practical typography, and subtle grid/measurement
details evoke a working shop without sacrificing readability.

## 005 — Authoritative brand snapshot

**Status:** Accepted

Use `docs/brand/` as the repository's working snapshot while the listed
Obsidian notes remain authoritative. Use the supplied logo, the approved color
tokens, and the helpful, hands-on, optimistic voice. Do not retain the earlier
provisional palette or infer typography and asset rules that the sources do not
define. Use the darker olive text token where the standard olive would not
provide enough contrast on a light background.

## 006 — SVG used as an image resource

**Status:** Accepted

Embed the approved logo through `<img>` elements instead of inlining it. This
keeps the Inkscape-generated SVG inert, prevents its internal IDs or editor
namespaces from affecting the document, and lets each placement provide an
appropriate HTML alternative text. The authoritative artwork remains unchanged.

## 007 — Publisher-neutral project cards

**Status:** Accepted

Keep project cards structurally independent of any one publishing platform.
Use a `data-project-host` value and explicit publication copy for builds hosted
elsewhere. This supports the current verified Instructables builds while
leaving future cards free to link to project pages hosted directly on Workshop
Revival.

## 008 — Thumbnail-only supplied project images

**Status:** Accepted

Use supplied project images only inside cards and cap the card grid at the
smallest thumbnail's native width. Include intrinsic image dimensions to avoid
layout shift. Do not reuse these files as hero, background, or full-width
images.
