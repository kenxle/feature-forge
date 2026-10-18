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

Agents can start building before the problem, scope and acceptance are clear. Decisions then scatter across chat and code. A working test suite alone cannot establish that a feature meets its user's needs.

## The jobs to be done

- Define the problem, scope and acceptance before implementation.
- Give each implementation owner the relevant source and a clear outcome.
- Preserve decisions, alternatives, review findings and observed proof.
- Obtain required human approvals and carry lessons into later work.

## What it does

The installer copies the packaged skills into a consuming project. Feature Forge coordinates the full route. Brief, Architecture and Plan provide document guidance. Whetstone covers small changes. The optional renderer turns trusted Markdown feature records into offline HTML. The evidence helper records actual verification output and command status.

## What it is not

It is not a hosted agent runtime, deployment service, telemetry system or application framework. It does not bundle Lahe, Pandoc, a browser driver, a research service or the separate cleanup skill. The fixture dossier is test data.

## The principles for choosing methods

- Keep instructions plain and leave agents room to exercise judgment.
- Preserve both the full route and Whetstone.
- Give humans the complete record and agents the context relevant to their work.
- Choose reviews for concrete risks. Keep reviewers independent of builders.
- Keep each PR coherent and independently verifiable.

## Commitments

- Follow the consuming project's instructions, verification commands and approval policy.
- Record explicit document approval before building through the full route.
- Keep the Plan's verification table authoritative for acceptance and evidence.
- Require independent checks of integrated work before PR.
- Preserve local installed edits. The installer refuses existing destinations.
- Keep durable documentation and lessons current when closing work.

## How we know it works

[Testing](TESTING.md) explains the package checks and their limits. Passing them establishes installer and helper behavior, not the quality of a real agent-led feature. Evaluate process changes in consuming projects against their approved acceptance and observed evidence. No measured productivity or quality improvement is claimed here.

The [research credits](../inspirations.md) identify influences, not a product validation study. If a refactor changes the audience, problem or claims, run `research-report` and retain its sources before rewriting those commitments.
