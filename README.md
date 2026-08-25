# Feature Forge

**A full feature lifecycle for coding agents: crucible, brief, wireframe, architecture, plan, TDD build loop, adversarial review, ship. Docs are the source of truth, sub-agents do the work, and a human reviews at three gates.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status: cleaning up for release](https://img.shields.io/badge/status-cleaning%20up%20for%20release-orange.svg)](#status)
[![Agents: Claude Code](https://img.shields.io/badge/agents-Claude%20Code-8A7CFF.svg)](#status)

## Status

**Not published yet.** The Feature Forge has been running against real production work for months, but it is still wired to one person's machine: private repo paths, personal skill names, and a few habits that only make sense in my setup. This repo exists so the project has a home while I pull all of that out.

Watch it if you want to know when the code lands.

## Why

Agents are good at writing code and bad at deciding what to write. Handed a one-line feature request, an agent will start editing files inside of a minute, and you find out three hours later that it built the wrong thing, or built the right thing with no tests, or quietly rewrote a module nobody asked it to touch.

The Feature Forge puts the thinking before the typing. A feature moves through phases, and each phase produces a document that the next phase has to answer to. Different sub-agents read those documents from different angles: a PM challenges the brief, a security reviewer challenges the architecture, an engineering manager challenges the plan, and an adversary reads everyone else's findings and goes looking for what they all missed.

The human reads a compiled HTML page at three gates and comments in the browser. Everything else runs on its own.

## The lifecycle

0. **Setup.** Branch and worktree first, so no doc and no commit ever lands on the shared tree.
1. **Crucible.** Challenge the idea before writing anything down. Is this worth building?
2. **Brief.** What we're building and why. Problem, user, requirements, success criteria. No architecture.
3. **Wireframe.** Interactive wireframes for anything a person looks at. *Human gate.*
4. **Architecture.** The technical design, with alternatives considered. No step-by-step plan.
5. **Plan.** Ordered, dispatchable tasks with a test list and acceptance criteria. *Human gate.*
6. **Implement.** A loop: dispatch parallel builders into their own worktrees, merge, run the app, score against the acceptance criteria, repeat until green. Built with TDD.
7. **Review.** Code review, security, testing, a cross-model pass, then an adversary fed everyone else's findings. Anything red goes back to phase 6.
8. **Ship and land.** Readiness pass, open the PR, *human gate*, merge, watch the deploy, smoke test in production.
9. **Cleanup.** Update the docs, review the outcome, write down what the process should have caught.

## What's in the box

Once it's cleaned up, this repo will hold:

- The `feature-forge` orchestration skill and its phase skills: crucible, brief, architecture, plan.
- The reviewer sub-agents: PM, architect, security, engineering manager, code lead, testing, adversary, and a clarity reader that catches unreadable prose before a human has to.
- The reference material the agents actually read: document templates, a code review checklist, a doc review checklist, a TDD guide, a post-deploy checklist.
- The build script that compiles the markdown docs into the HTML pages a human reviews.

## Related

- [Live Agentic HTML Editor (Lahe)](https://github.com/kenxle/live-agentic-html-editor) — the review layer the human gates run on. Select a passage in the built page, comment on it, and the agent edits the underlying markdown.

## License

MIT
