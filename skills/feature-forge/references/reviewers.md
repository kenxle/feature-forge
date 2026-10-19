# Focused reviewer perspectives

## Dispatch instruction for a fresh reviewer

Give the reviewer its assigned perspective and criteria, authoritative source
headings, integrated revision/worktree, relevant evidence and permission to inspect
code or run checks. Ask it to investigate rather than rubber-stamp builder claims.
Require concrete findings with severity, source location, requirement affected,
observed behavior, recommended correction and evidence limits. It may read adjacent
sources where needed. It must not edit outside assigned authority or ship code.
The reviewer returns pass/fail/unverified per assigned criterion; the orchestrator
integrates dispositions and assigns rechecks. These are generic agent instructions,
not dependencies on named private agents or plugins.

Select reviewers by need; each check has one owner independent of its builder.
A delegated lead may own checks explicitly; parents reuse evidence rather than
dispatching overlapping rosters. Choose supported models by ambiguity and quality.

Give reviewers the [shared principles index](principles.md) and a clear statement
of the intended behavior. Independent reviewers judge the same scope from their
assigned perspective. Cross-model review is useful when it adds signal, not a
mandatory model roster.

Synthesize findings instead of applying every suggestion. Verify each claim
against the code and evidence, combine duplicates, and preserve disagreements.
Separate issues to fix from useful suggestions, contextual observations, and
dismissed findings. Give a concrete reason for each disposition. Agreement can
strengthen a finding, but a defect proven by one reviewer still needs attention.

| Perspective | Purpose |
|---|---|
| Product management | Substantial brief: user need, scope, outcomes, missing behavior and rollout |
| Architecture | Consequential/uncertain design: recon, contracts, alternatives and failure modes |
| Security | Changed trust boundaries, authorization, sensitive state, abuse and privacy |
| Testing | Optional Plan perspective: measurable acceptance, variants, seams and release coverage |
| Staff design | Actual UI judgment when useful: interaction, hierarchy, accessibility and existing design conventions |
| Cross-model | Independent alternative-model judgment when useful for consequential code or ambiguous decisions |
| Code quality | Required before PR: integrated code correctness, maintainability and conventions |
| Completion evaluator | Required before PR: integrated implementation vs requirements and Plan acceptance |

One suitable independent reviewer may own both code quality and completion.
Orchestrator self-review cannot substitute. Inspect actual code and behavior;
tests alone do not establish full implementation. Map each criterion to evidence
and pass/fail/unverified; resolve required gaps and recheck affected behavior.
Record inspected revision, commands, findings, disposition and limits. Never
fabricate reviewers, approval or execution evidence.

Changed user workflows receive one final independent flow walk before PR. It may
share an explicitly assigned completion owner. Use tool/browser proof during
iteration, rather than dispatching a flow walker for every build loop.
