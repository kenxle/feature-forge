# Feature Forge

A feature development process for coding agents: clarify, brief, plan, build,
verify, ship, and learn. Small understood changes use the Whetstone short route.

The process is model agnostic, but designed mostly on Claude Code, with some
Codex as well. No hosted service or telemetry is included.

Knows how to use the Lahe editor for documentation review.

## What the Feature Forge brings together

The Feature Forge carries a feature from product thinking through specification,
implementation, independent verification, and compounding knowledge. The brief
states what matters; the architecture preserves choices and alternatives; the
plan connects requirements to agent-aware implementation planning and testing.
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

## Inspirations

This process has been shaped by studying and using other agent workflows,
including [gstack](https://github.com/garrytan/gstack),
[pstack](https://cursor.com/marketplace/cursor/pstack),
[Superpowers](https://github.com/obra/superpowers), and
[Paweł Huryn's PM Skills](https://github.com/phuryn/pm-skills), alongside practical iteration
in a number of projects over N months. Ideas are not exclusive to this project,
merely assembled in a new way.

The wider research also includes Jason Liu, Daniel Hnyk, Shrivu Shankar,
Addy Osmani, Harper Reed, Simon Willison, Kieran Klaassen, and other practitioners.
See the [full research and inspirations list](docs/inspirations.md), including
the earlier subagent coding research, system prompt architecture teardown,
code orchestration alternatives, and other workflows compared.
See [provenance](NOTICE.md) for the distinction between process influences and
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

Start Claude Code in that project and invoke `/feature-forge` or `/whetstone`. Commit installed skills for team use.
Read the consuming project's instructions and use its actual verification
commands, branch conventions and approval policy.

## Process

1. **Dev hygiene.** Set up an isolated branch/worktree and the feature's working files.
2. **Product thinking.** Think through the product problem, establish scope and clarify uncertainties. Push back on whether you should be spending your limited time and resources on this.
3. **Brief.** Context, user, requirements, analytics, and rollout.
4. **Architecture.** Explore the codebase. Explore the internet. Explore alternatives. Write a thorough architecture without any code, and spawn optional reviewers for security and architecture.
5. **Plan.** Create coherent slices of work that consider the needs of implementation agents.
6. **Review.** Present the complete dossier for consolidated human document approval.
7. **Implement.** Build with TDD, unit tests, playwright tests, and an agent browser walkthrough before PR.
8. **Verify.** Before PR, an independent reviewer verifies integrated implementation against requirements and acceptance using evidence. Resolve gaps.
9. **Ship and land.** Prepare PR, follow human merge/deployment approval policy, verify release in prod.
10. **Cleanup.** Update durable project documentation, record lessons and propose improvements to project guidance. Close out the feature record and remove owned temporary resources with authorization.

Multiple reviewer personas are available for subagent review. To preserve tokens and prevent context poisoning, the orchestrator is given the judgment to choose which reviewers are invoked during the documentation process. Implementation always gets code review, completion review, and browser walkthrough. [Available reviewer perspectives](skills/feature-forge/references/reviewers.md) include product management, architecture, security, testing, code quality, completion evaluation, cross-model review, and design judgment.

## Example feature documents

[The non-Rails CSV example](examples/csv-export/README.md) demonstrates sources,
slices and an explicitly illustrative completion review. No application is
claimed to have been shipped.

## HTML for human review

The included renderer combines a feature's Markdown documents into an HTML
dossier for human review. Markdown remains the source for agents and edits.
You can use this renderer or let LAHE render Markdown directly; the bundled
renderer requires separately installed [Pandoc](https://pandoc.org/installing.html):

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
