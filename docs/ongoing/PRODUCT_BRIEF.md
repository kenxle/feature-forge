# Product brief

## Charter

**What belongs:** What the product is, who it is for, and why. Sections, in this order: Charter, What it is, Who it is for, The problem, The jobs to be done, What it does, What it is not, The principles for choosing methods, Commitments, How we know it works. The principles and commitments that hold for every feature.

**What does not:** How anything works (ARCHITECTURE.md and diagrams). How it looks (STYLE_GUIDE.md). A feature's own reasoning (its folder under docs/features/).

**Level of detail:** A reader finishes knowing what the product is for. That guides every other doc.

**Sources:** [package overview](../../README.md), [orchestrator](../../skills/feature-forge/SKILL.md), [Whetstone](../../skills/whetstone/SKILL.md), [research credits](../inspirations.md). No product validation report is present; see How we know it works.
## What it is

Feature Forge is a portable skills package that improves agentic software engineering. It connects product thinking, feature documents, implementation, verification, shipping, and compounding knowledge.

## Who it is for

People using coding agents to develop software, and the agents carrying out that work. It was developed mainly with Claude Code. Other hosts must supply compatible skill discovery and tool access; installation outside Claude Code is unverified.

## The problem

One-shot prototypes aren't so difficult to build, but working on the same codebase over extended periods of time remains quite difficult.

## The jobs to be done

- Build great software that is reliable, secure, and that users love.

- Increase development velocity.

- Maintain software over time.

- Reduce bugs in production.

- Preserve decisions, alternatives, review findings, and observed proof.

- Carry lessons into later work.

## What it does

Feature Forge provides a series of skills and reference documentation for creating great documentation, and building great software. It creates documentation dossiers that may include a Brief, Architecture, Plan, and Progress. It relies on test driven development (TDD) and verification to create software that always works reliably.

## What it is not

It is not a hosted agent runtime, deployment service, telemetry system, or application framework. It does not bundle Lahe, Pandoc, a browser driver, a research service, or the separate cleanup skill.

## The principles for choosing methods

- Ship as often as possible while maintaining software quality and reliability. Increase development velocity.

- Leave agents room to exercise judgment.

- Support multiple routes/runbooks depending on the use case.

- Provide robust verification so that agents can know that they are shipping good work.

- Give humans the complete record and agents the context relevant to their work.

- Keep each PR coherent and independently verifiable.

## Commitments

- Follow the consuming project's instructions, verification commands, and approval policy.
- Keep the Plan's verification table authoritative for acceptance and evidence.
- Preserve local installed edits. The installer refuses existing destinations.
- Keep durable documentation and lessons current when closing work.

## How we know it works

[Testing](TESTING.md) explains the package checks and their limits. Passing them establishes installer and helper behavior, not the quality of a real agent-led feature. Evaluate process changes in consuming projects against their approved acceptance and observed evidence. No measured productivity or quality improvement is claimed here.

The [research credits](../inspirations.md) identify influences, not a product validation study. If a refactor changes the audience, problem, or claims, run `research-report` and retain its sources before rewriting those commitments.
