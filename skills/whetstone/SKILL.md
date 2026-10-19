---
name: whetstone
description: A short spec, build and independent review route for small understood changes.
user-invocable: true
---

# Whetstone

Use for small understood behavior changes. Do trivial edits directly and route
uncertain features through [Feature Forge](../feature-forge/SKILL.md). Read project
conventions, fetch before choosing a base, establish an isolated branch/worktree,
and preserve unrelated work.

Write a compact spec with problem, behavior, scope, approach, questions, the
verification table, rollout, and review owners. Keep the document without adding
a routine human approval gate. Apply the relevant
[principles](../feature-forge/references/principles.md) and follow
[verification and release](../feature-forge/references/verification-and-release.md).

Use TDD for changed behavior, focused tests, integration checks, independent
review, and changed-flow proof. Do verification, always. Land when readiness and existing authority permit.
Keep progress documentation. Check durable docs and diagrams, record useful lessons,
and close the record and owned resources as authorized. Do not restart the full
document pipeline for a small change.
