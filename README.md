# Feature Forge

A feature development process for coding agents: clarify, brief, plan, build,
verify, ship, and learn. Small understood changes use the Whetstone short route.

Claude Code is the supported installation target. The process is model agnostic.
No hosted service or telemetry is included.

## What Forge brings together

Forge carries a feature from product thinking through specification,
implementation, independent verification, and compounding knowledge. The brief
states what matters; the architecture preserves choices and alternatives; the
plan connects requirements to implementation slices and proof. Release findings
and lessons feed back into durable project guidance for the next feature.

Its emphasis is the continuity between those stages:

- **One accountable feature record:** decisions, questions, acceptance, evidence,
  and lessons stay connected from the initial premise through release.
- **Two reading surfaces:** agents receive relevant authoritative source sections;
  the human reviews a comprehensive dossier composed from those same sources.
- **Coherent implementation slices:** dependencies, ownership, integration, and
  safe landings are explicit without equating agents, tasks, and PRs.
- **Independent completion:** someone other than the builder or orchestrator
  checks the integrated implementation against the specification.
- **Compounding knowledge:** cleanup records useful findings and proposes updates
  to project guidance so later work can use what the feature taught.

## Inspirations

This process has been shaped by studying and using other agent workflows,
including [gstack](https://github.com/garrytan/gstack),
[pstack](https://cursor.com/marketplace/cursor/pstack), and
[Superpowers](https://github.com/obra/superpowers), alongside practical iteration
on real features. Forge's emphasis above describes the process assembled here;
it does not claim those ideas are exclusive to this project. See
[provenance](NOTICE.md) for the distinction between process influences and
material shipped in this repository.

## Install in a project

Requires Python 3.10 or later. From this clone:

```sh
python3 scripts/install.py /absolute/path/to/your-project --dry-run
python3 scripts/install.py /absolute/path/to/your-project
```

The installer checks every destination before copying five skills into the
project's `.claude/skills/`. It refuses existing destinations and never edits
project instructions. Review and move old copies yourself before updating.
Start Claude Code in that project and invoke `/feature-forge`, `/brief`,
`/architecture`, `/plan` or `/whetstone`. Commit installed skills for team use.
Read the consuming project's instructions and use its actual verification
commands, branch conventions and approval policy.

## Process

1. Establish scope and an isolated branch/worktree; clarify uncertainties.
2. Brief context, solution, requirements, analytics and rollout.
3. Design from reconnaissance and preserve alternatives. Select architecture/security perspectives by need.
4. Plan coherent slices, dependencies, contracts and one verification table. Retain an independent testing checkpoint.
5. Present the complete dossier for consolidated human document approval.
6. Build with targeted tests; integrate and check seams, then run one final independent walk of changed user flows before PR.
7. Before PR, an independent reviewer verifies integrated implementation against requirements and acceptance using evidence. Resolve gaps.
8. Prepare PR, follow human merge/deployment approval policy, verify release and record lessons.

Choose delegation, models, reuse and reviewer grouping judiciously. One independent
owner per check; agents, workstreams and PRs need not map one to one. Do not
repeat the documentation pipeline per slice. Browser automation is an option
for browser apps, not a requirement for other projects.

[Available reviewer perspectives](skills/feature-forge/references/reviewers.md)
include product management, architecture, security, testing, code quality,
completion evaluation, cross-model review, and design judgment. Select the
perspectives the feature needs rather than dispatching the entire roster.

Behavior changes follow red/green/refactor using project tools, with practical
verification choices for reconnaissance, UI exploration and vendor material.

## Example and optional HTML

[The non-Rails CSV example](examples/csv-export/README.md) demonstrates sources,
slices and an explicitly illustrative completion review. No application is
claimed to have been shipped.

Markdown needs no renderer dependencies. Optional HTML requires separately
installed [Pandoc](https://pandoc.org/installing.html):

```sh
python3 skills/feature-forge/scripts/build_feature_docs.py examples/csv-export
python3 -m unittest discover -s tests -v
```

The renderer bundles CSS, expands modular includes and review siblings, rewrites
local document links and adds navigation. It uses no CDN or browser scripts.
Mermaid remains readable code, not rendered diagrams. Raw HTML is supported for
trusted local authoring; do not render untrusted documents. Edit Markdown and rebuild.

Capture a project's real verification command without caching or overwriting
prior evidence (choose a new evidence directory per run):

```sh
python3 skills/feature-forge/scripts/forge_support.py --repo /path/to/project --evidence /path/to/new-evidence -- python3 -m unittest discover
```

The helper records actual output, exit status, command, time and Git revision.
It does not fingerprint uncommitted/external state or establish spec completion.
Progress remains directly authored Markdown; automatic progress mutation and
evidence reuse are intentionally outside this portable package.

[LAHE pairing](docs/lahe.md) uses the separate
[Live Agentic HTML Editor](https://github.com/kenxle/live-agentic-html-editor).
Human gates also work by sharing Markdown or local HTML and recording approval.

See [verification](docs/verification.md), [provenance](NOTICE.md) and [MIT license](LICENSE).
