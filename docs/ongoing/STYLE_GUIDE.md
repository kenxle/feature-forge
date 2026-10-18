# Style guide

## Charter

**What belongs:** How the product looks: color, type, spacing and the reusable components. Tokens and the rules for using them. Each component and when to use it.

**What does not:** Voice and word choice (BRAND.md). How a screen works.

**Level of detail:** Rules a builder can apply without asking, with the reason for each.

**Describes:** `skills/feature-forge/assets/`, `skills/feature-forge/scripts/build_feature_docs.py`

**Sources:** [header asset](../../skills/feature-forge/assets/header.html), [renderer](../../skills/feature-forge/scripts/build_feature_docs.py), [LAHE pairing](../lahe.md).
First draft by Seneschal.

## Scope

This describes the package's bundled dossier output. It does not establish a new visual system for a consuming project or replace a review tool's own styles.

## Source and layout

The [header asset](../../skills/feature-forge/assets/header.html) is the visual source of truth. Pandoc supplies document structure. The [renderer](../../skills/feature-forge/scripts/build_feature_docs.py) inserts shared dossier navigation. Use semantic headings, paragraphs, lists and tables in Markdown. Keep source leaves readable for agents.

Preserve existing document conventions when changing rendering. Repair compatibility in the renderer rather than rewriting source documents merely to suit a tool.

## Bundled visual rules

The stylesheet uses system sans-serif type, dark text on white, blue links and pale gray code blocks. It limits the reading width and lets navigation wrap. Tables span the reading column with thin gray borders. Requirement callouts, question callouts and cross-references share a blue left rule. Print output hides navigation and removes the reading-width limit. Consult the linked asset for exact CSS values.

## Review surfaces

Bundled HTML works offline. Do not add CDN assets or browser scripts without a deliberate contract change. LAHE is a separate optional review surface; follow its installed instructions and preserve the source-to-render relationship described in [LAHE pairing](../lahe.md).

## Change discipline

Treat the current stylesheet as implementation, not as an approved new brand. Check representative dossiers and navigation after style changes. Keep include leaves and review siblings visible in the composed human record. The package has no separate token or component library.
