# Feature Forge

A feature development process for coding agents: short brief, prototype, PRD,
architecture, Plan, TDD, verification, ship, and land. Small understood changes
use Whetstone. The comprehensive pre-build dossier review remains available.

The process is model agnostic, but designed mostly on Claude Code, with some
Codex as well. No hosted service or telemetry is included.

Knows how to use the Lahe editor for documentation review.

## What the Feature Forge brings together

The Feature Forge carries a feature from product thinking through specification,
implementation, independent verification, and compounding knowledge. A short
brief guides the prototype; the PRD captures the agreed behavior; architecture
preserves choices and alternatives; the Plan connects requirements to implementation
and testing. Agents write and maintain these documents without routine human
reading or approval gates.
A clean-up process feeds lessons back into durable project guidance for the next feature.

The process is built around:

- **One accountable feature record:** decisions, questions, acceptance, evidence,
  and lessons stay connected from the initial premise through release.
- **Two reading surfaces:** Agents read MD. Humans read HTML.
  The Lahe editor or the orchestrator coordinates between the two so that each
  stakeholder has the optimal surface and context.
- **Plan for agent implementation:** break a feature into slices that an agent
  or subagent can own, test, and ship. Make each slice's outcome, dependencies,
  and integration with the rest of the feature clear before building.
- **Persona-based reviews:** optional subagents bring product, architecture,
  security, testing, and other perspectives to a review. Choose the personas
  that can catch problems in the feature rather than running every reviewer.
- **Compounding knowledge:** cleanup records useful findings and proposes updates
  to project guidance so later work can use what the feature taught.
- **Engineering principles:** the package includes selected pstack principles
  with their license and source revision. Agents load applicable leaves through
  the [principles index](skills/feature-forge/references/principles.md).

## Inspirations

This process has been shaped by studying and using other agent workflows,
including [gstack](https://github.com/garrytan/gstack),
[pstack](https://cursor.com/marketplace/cursor/pstack),
[Superpowers](https://github.com/obra/superpowers),
[Paweł Huryn's PM Skills](https://github.com/phuryn/pm-skills),
[GitHub Spec Kit](https://github.com/github/spec-kit),
[BMAD](https://github.com/bmad-code-org/BMAD-METHOD),
[Agent OS](https://github.com/buildermethods/agent-os),
[SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework),
[claude-flow](https://github.com/ruvnet/ruflo), and
[Anthropic's Claude Code best practices](https://code.claude.com/docs/en/best-practices),
alongside practical iteration in a number of projects since February 2026. Ideas are not exclusive to this project,
merely assembled in a different way.

The wider research also includes a Fable 5 system prompt architecture teardown,
agent orchestration frameworks like LangGraph, and work by
Jason Liu, Daniel Hnyk, Shrivu Shankar, Addy Osmani, Harper Reed, Simon Willison,
Kieran Klaassen, and other practitioners. See the
[full research and inspirations list](docs/inspirations.md).

## Maintainer documents

Read the [project document index](docs/README.md) for the current product brief,
architecture, testing guidance, and public writing conventions before changing
the package. The [board](docs/BOARD.md) tracks future work.

## Install in a project

Requires Python 3.10 or later. Clone this repository first:

```sh
git clone https://github.com/kenxle/feature-forge.git
```

From the cloned repository:

```sh
python3 scripts/install.py /absolute/path/to/your-project --dry-run
python3 scripts/install.py /absolute/path/to/your-project
```

The installer checks every destination before copying five skills into the
project's `.claude/skills/`. It refuses existing destinations and never edits
project instructions. Review and move old copies yourself before updating.

Start Claude Code in that project and invoke `/feature-forge` or `/whetstone`. Commit installed skills for team use.
Read the consuming project's instructions and use its actual verification
commands, branch conventions, and approval policy.

## Process

Read the project's instructions, fetch before choosing a base, and work in an
isolated branch/worktree. The default route for a new user experience is:

1. **Short brief.** Target users, context, problem, desired outcome, and constraints.
2. **Prototype.** Build a clickable high-fidelity experience, let the human explore it, and record the chosen behavior. Keep or discard the code deliberately.
3. **PRD.** Derive detailed requirements, failures, scope, analytics, and rollout from the agreed experience.
4. **Architecture.** Investigate the codebase, choose data shapes, and preserve design alternatives and risks.
5. **Plan.** Define coherent slices, the throughput checkpoint, and the authoritative verification table.
6. **TDD.** Build changed behavior with focused failing tests, implementation, and refactoring.
7. **Verify.** Check the integrated result against acceptance with independent review and a real walk of changed flows. Resolve required gaps.
8. **Ship.** Prepare coherent PRs with proof and rollout, then follow checks and review findings through readiness.
9. **Land.** Merge and deploy when evidence and existing authority permit. Verify the actual release, update durable documentation and lessons, and close the record.

Before the short brief, use lightweight
[product thinking](skills/feature-forge/references/product-thinking.md) to clarify
the user job, evidence, priority, and credible alternatives. Focused references
restore [setup](skills/feature-forge/references/environment-readiness.md),
[progress and handoffs](skills/feature-forge/references/progress-and-handoffs.md),
[UI fidelity and style checks](skills/feature-forge/references/ui-quality.md),
[automated post-launch proof](skills/feature-forge/references/post-launch.md), and
[closeout](skills/feature-forge/references/closeout.md). Load them when relevant.

For nonvisual work, use a concrete interface example or spike when useful rather
than manufacturing a UI. [Whetstone](skills/whetstone/SKILL.md) retains a compact
spec for small changes. Choose the [full dossier route](skills/feature-forge/references/runbooks/full-dossier.md)
when a comprehensive human document review before build is explicitly wanted.

The default route releases on evidence-based confidence under the project's
standing authority. Forge adds no routine document or per-release human approval
request. Project restrictions and new material product decisions still matter.
Shipping requires a passing full project test suite with no failures or errors.
Pre-existing, unrelated, and environment/setup failures still block release.
See [verification and release](skills/feature-forge/references/verification-and-release.md).

Agents can adapt or combine routes for the task while preserving explicit user
choices and verification. Delegated agents receive the same principles index.
[Writing](skills/feature-forge/references/writing.md) and
[comment review](skills/feature-forge/references/comment-review.md) guidance load
when useful. The package does not depend on the complete pstack plugin or arena.

Specialist reviewers cover product management, architecture, security, testing,
code quality, completion, cross-model review, and design judgment. The project's
existing voice-of-customer persona judges are also retained for prototypes and
user-facing changes. Use their actual persona definitions and research to judge
the experience from the intended users' perspective. The orchestrator selects
relevant perspectives; independent code review, acceptance review, and changed-flow
proof remain required. See the [reviewer guidance](skills/feature-forge/references/reviewers.md).

## HTML for human review

The included renderer combines a feature's Markdown documents into an HTML
dossier for human review. Markdown remains the source for agents and edits.
You can use this renderer or let the Lahe skills invoke the renderer. The bundled
renderer requires separately installed [Pandoc](https://pandoc.org/installing.html):

```sh
python3 skills/feature-forge/scripts/build_feature_docs.py /absolute/path/to/your-project/docs/features/your-feature
python3 -m unittest discover -s tests -v
```

The renderer expands modular includes and review siblings, rewrites local
document links and adds navigation. It uses no CDN or browser scripts.
Mermaid fences render locally as embedded SVG images, with their source available
in a disclosure. Dossiers containing Mermaid require separately installed
[Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) and its compatible Node
and browser dependencies. Put `mmdc` on PATH or set `FORGE_MERMAID_CLI` to its
executable. The renderer does not install dependencies automatically. A missing
renderer or invalid diagram fails the build before replacing existing pages.

It builds in the house document style when it can find one: first the folder
named by `FORGE_DOC_STYLE_DIR` (a folder holding `system-tokens.css`,
`document.css` and `lahe-markdown.css`), then the style that ships with
[Lahe](https://github.com/kenxle/live-agentic-html-editor), found through the
`lahe` command on PATH. The style is inlined in the page, and the page uses its
title block, links row, folded contents, numbered sections and components. When
no style is found, the build writes a plain page with a small bundled
stylesheet and prints one line to stderr.
Raw HTML is supported for
trusted local authoring; do not render untrusted documents. Edit Markdown and rebuild.
See [modular authoring](skills/feature-forge/references/document-authoring.md) for
source leaves, components, and composed review. The
[evidence helper](skills/feature-forge/references/tested-code-evidence.md) records
tested working files and described setup alongside each run's original output.

[Lahe pairing](docs/lahe.md) uses the separate
[Live Agentic HTML Editor](https://github.com/kenxle/live-agentic-html-editor).
The optional full dossier review also works by sharing Markdown or local HTML
and recording the requested approval.

See [verification](docs/verification.md), [research and inspirations](docs/inspirations.md), and [MIT license](LICENSE).
