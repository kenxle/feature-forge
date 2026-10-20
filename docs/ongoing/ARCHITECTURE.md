# Architecture

## Charter

**What belongs:** The shape of the system at a level a person can hold in their head. The stack and the folder structure. The surfaces people and agents touch, and the outside services behind them. The main models and how they relate, in outline.

**What does not:** How one feature works. That goes in a diagram or its own ongoing doc. How a feature got built. That stays in docs/features/.

**Level of detail:** A paragraph or a short table per area. Link out when a section passes three paragraphs.

**Describes:** `skills/`, `scripts/`

**Sources:** [installer](../../scripts/install.py), [renderer](../../skills/feature-forge/scripts/build_feature_docs.py), [evidence helper](../../skills/feature-forge/scripts/forge_support.py), [Feature Forge](../../skills/feature-forge/SKILL.md).
## System shape

This repository publishes instructions and local command-line helpers. It has no application server, database, or hosted state. A consuming project's agent interprets the skills and supplies its own tools, models, and approval rules.

| Area | Responsibility | Source |
|---|---|---|
| Installation | Copy a fixed skill set into a project's skill folder; refuse conflicts before copying | [installer](../../scripts/install.py) |
| Route selection | Default to prototype-first features, retain full dossier review by explicit choice, and use Whetstone for small changes | [Feature Forge](../../skills/feature-forge/SKILL.md), [runbooks](../../skills/feature-forge/references/runbooks/) |
| Document guidance | Define the content of each feature document | [Brief](../../skills/brief/SKILL.md), [Architecture](../../skills/architecture/SKILL.md), [Plan](../../skills/plan/SKILL.md) |
| Short route | Keep small changes compact while retaining independent verification and cleanup | [Whetstone](../../skills/whetstone/SKILL.md) |
| Shared guidance | Templates, reviewer perspectives, work contracts, and build loop | [references](../../skills/feature-forge/references/) |
| Engineering principles | Load applicable pstack leaves with upstream provenance and license | [index](../../skills/feature-forge/references/principles.md), [source record](../../skills/feature-forge/vendor/pstack/UPSTREAM.md) |
| Writing and comments | Use vendored prose guidance and the unchanged Comment Sicko prompt through local host adapters | [writing](../../skills/feature-forge/references/writing.md), [comment review](../../skills/feature-forge/references/comment-review.md) |
| Dossier rendering | Expand Markdown sources, invoke Pandoc and write local HTML | [renderer](../../skills/feature-forge/scripts/build_feature_docs.py), [header](../../skills/feature-forge/assets/header.html) |
| Verification capture | Run a supplied command and record its output, status, and revision | [evidence helper](../../skills/feature-forge/scripts/forge_support.py) |

## Installation boundary

The Python installer requires an existing project directory. It checks all destinations and rejects symlinked installation directories. It then copies the packaged skills, excluding Python cache files. It does not edit project instructions, manage upgrades, or merge installed local changes. An interrupted copy attempts to remove only destinations created by that invocation.

Installed copies do not track this checkout. Fix package problems here, compare installed copies before updating them, and preserve consumer changes. Sibling skills link relatively to the shared Feature Forge references.

## Feature records and approval

The default route uses a short brief, prototype decision, PRD, architecture, Plan, and Progress. The prototype precedes detailed requirements. The full review route retains the established brief/architecture/Plan/Progress organization. Optional leaves preserve details and review history. The renderer accepts filenames starting with a numeric prefix of at least two digits and an underscore, including the longer new route. Historical records need no renaming.

The Plan owns acceptance evidence and the throughput checkpoint. Whetstone uses its compact spec's table. Default document production does not add an approval gate. The explicit full review route retains consolidated human approval before build. Shared verification and release guidance covers independent review, evidence, confidence, and existing project authority. These are instruction contracts rather than runtime enforcement.

## Renderer flow

The renderer selects numbered dossier Markdown at the feature folder's top level. It expands `forge-include` directives relative to their containing file, rejects paths outside the folder, and detects cycles. It appends review siblings, rewrites links between selected documents, and adds shared navigation. With a house style found (`FORGE_DOC_STYLE_DIR`, then Lahe through the `lahe` command), it inlines the style and lays each page out as the style expects, and copies the font files the style names beside the pages. Without one, it uses the bundled plain stylesheet and prints one line to stderr. Pandoc renders each source. The helper renders all sources before writing output files; it does not provide an atomic filesystem transaction.

Markdown remains authoritative. Generated HTML is a review artifact. Raw HTML is supported for trusted authors, so the renderer is unsuitable for untrusted input. The bundled output has no CDN or browser-script dependency.

## Evidence flow

The evidence helper runs an argument list in the specified repository. It saves combined output to `output.log` and command metadata to `result.json`. It refuses existing evidence files and returns the actual command status. The recorded revision does not identify dirty files or external state. Evidence is an observation from that invocation, not a reusable completion verdict.

## Outside tools

Python runs the helpers and tests. Pandoc is optional for HTML and rendering tests. Git supplies revision metadata. Lahe is an optional separately installed review tool; the package does not contain its state or lifecycle implementation. Browser automation and deployment tools come from the consuming project.

## Refactor boundaries

Preserve installer conflict refusal, relative skill links, Markdown authority, include containment, review history, truthful command status, and project authority. Preserve Whetstone and the full review route alongside the default feature flow. The bundled principles are reference material; the full pstack plugin and its architect skill are not runtime dependencies. The [board](../BOARD.md) records future work, including cloud board runners and further pstack integrations.
