# Focused reviewer perspectives

Select reviewers by need; each check has one owner independent of its builder.
A delegated lead may own checks explicitly; parents reuse evidence rather than
dispatching overlapping rosters. Choose supported models by ambiguity and quality.

| Perspective | Purpose |
|---|---|
| Product management | Substantial brief: user need, scope, outcomes, missing behavior and rollout |
| Architecture | Consequential/uncertain design: recon, contracts, alternatives and failure modes |
| Security | Changed trust boundaries, authorization, sensitive state, abuse and privacy |
| Testing | Plan checkpoint: measurable acceptance, variants, seams and release coverage |
| Staff design | Actual UI judgment when useful: interaction, hierarchy, accessibility and existing design conventions |
| Cross-model | Independent alternative-model judgment when useful for consequential code or ambiguous decisions |
| Code quality | Integrated code correctness, maintainability and conventions |
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
