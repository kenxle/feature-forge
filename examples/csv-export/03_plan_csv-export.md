# Plan: CSV export

## Slices

| Slice | Outcome | Dependencies | Integration and landing |
|---|---|---|---|
| Basic export | Real CLI exports new output safely, including empty data and failures | Existing read interface | Builder owns CLI/writer seam; land additive behavior with R1/R3 proof |
| Quoting variants | Required character cases verified and fixed if needed | Basic export | Same builder may continue; integration owner verifies all rows before release |

The first slice must use correct quoting from the start; the second expands
proof of variants rather than landing known broken behavior. Workstreams and
PRs are chosen independently. Do not repeat Brief/Architecture/Plan per slice.

## Contract

<!-- forge-include: parts/plan/export-contract.md -->

## Verification

| Requirement | Acceptance/failure case | Proof | Owner | Evidence/status |
|---|---|---|---|---|
| R1 | UTF-8 columns, values and empty store | Project CLI integration test plus independent CSV reader | Builder; completion evaluator judges result | Pending: no app exists |
| R2 | Commas, quotes and line breaks round-trip | Targeted writer tests and integrated CLI round-trip | Builder; completion evaluator | Pending |
| R3 | Existing files preserved; authorized replacement; race/symlink/permission failure | Destination safety tests and changed-flow walk | Independent evaluator | Pending |

## Testing checkpoint

Illustrative finding: include empty store and concurrent destination changes.
Accepted into the table. This is not an executed reviewer record.

## Human gate and completion review

Human dossier approval is not yet obtained for this illustrative feature.
Before PR an independent reviewer, distinct from builder and orchestrator, inspects
the integrated revision and maps every table row to actual tests and observations.
An independent final CLI flow walk verifies export, refusal and replacement.
These scopes may share one suitable owner. Current verdict: all rows unverified;
no PR may claim completion. Record revision, commands, outputs and remaining gaps.

## Rollout

Additive command; verify existing CLI help/commands and installation after landing.
