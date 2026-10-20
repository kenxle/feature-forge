# Style guide

## Charter

**What belongs:** How the product looks: color, type, spacing, and the reusable components. Tokens and the rules for using them. Each component and when to use it.

**What does not:** Voice and word choice (BRAND.md). How a screen works.

**Level of detail:** Rules a builder can apply without asking, with the reason for each.

**Describes:** `skills/feature-forge/assets/`, `skills/feature-forge/scripts/build_feature_docs.py`, `doc_style.py` and `doc_layout.py` beside it

**Sources:** [header asset](../../skills/feature-forge/assets/header.html), [house header asset](../../skills/feature-forge/assets/house_header.html), [renderer](../../skills/feature-forge/scripts/build_feature_docs.py), [style lookup](../../skills/feature-forge/scripts/doc_style.py), [page layout](../../skills/feature-forge/scripts/doc_layout.py), [Lahe pairing](../lahe.md).
First draft by Seneschal.

## Scope

This describes Feature Forge's document review styles and bundled dossier output. It does not establish a new visual system for a consuming project or replace a review tool's own styles. The projects that the Forge creates feature for should have their own style guides.

## Source and layout

Use Lahe's default styles for human document review. The built dossier carries them: the [renderer](../../skills/feature-forge/scripts/build_feature_docs.py) finds the style, inlines it in a `data-lahe-doc-style` block so Lahe's style switcher can restyle the page, and [lays the page out](../../skills/feature-forge/scripts/doc_layout.py) the way the style expects (title block, links row, folded contents, numbered sections, callouts as insight panels, review verdicts as status dots). The [style lookup](../../skills/feature-forge/scripts/doc_style.py) checks `FORGE_DOC_STYLE_DIR`, then Lahe through the `lahe` command on PATH. When neither is found, the [header asset](../../skills/feature-forge/assets/header.html) supplies a small plain stylesheet and the build prints one line to stderr. The [house header asset](../../skills/feature-forge/assets/house_header.html) adds only the review-history rules the style lacks. Pandoc supplies document structure. Use semantic headings, paragraphs, lists, and tables in Markdown. Keep source leaves readable for agents.

Preserve existing document conventions when changing rendering. Repair compatibility in the renderer rather than rewriting source documents merely to suit a tool.

## Default review styles

Feature Forge defaults to using [Lahe](https://github.com/kenxle/live-agentic-html-editor) and its default styles. Other styles may be used if those are not present, or at the user's request.

## Review surfaces

Bundled HTML works offline, with or without the house style. The style lookup reads local files only. Mermaid blocks render at build time through the separately installed local Mermaid CLI. The [diagram helper](../../skills/feature-forge/scripts/doc_diagrams.py) embeds self-contained SVG images and retains source in a disclosure. Descriptions come from the diagram's accessible title and description where supplied. There is no CDN or browser-script dependency. Missing tooling or invalid diagrams fail the build instead of silently displaying code in place of the diagram. Lahe is a separate optional review surface; follow its installed instructions and preserve the source-to-render relationship described in [Lahe pairing](../lahe.md).

## Change discipline

Diagrams retain their intrinsic size so labels stay readable. Wide diagrams use
a keyboard-focusable horizontal scroll region inside the figure on narrow pages.
The page itself should not overflow. Captions name the diagram and explain the
scroll affordance. Do not shrink a large graph until its labels become illegible.

Treat the current stylesheet as implementation, not as an approved new brand. Check representative dossiers and navigation after style changes. Keep include leaves and review siblings visible in the composed human record. The package has no token or component library of its own. The house style comes from Lahe or from the folder the user names. Tests use a made-up style under `tests/fixtures/house-style/` and never a real one.
