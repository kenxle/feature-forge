# Architecture: CSV export

## Reconnaissance

<!-- forge-include: parts/architecture/recon.md -->

## Design and flow

Use Python's standard csv writer and existing repository read interface.
Serialize into a temporary file in the destination directory, then finalize
through the project's safe file creation/replacement utility. Refusal preserves
existing files; failures remove only the temporary file created by this operation.

## Alternatives

<!-- forge-include: parts/architecture/alternatives.md -->

## Failure modes

Quoted/newline input, empty store, encoding and permission errors need proof.
Symlink and concurrent destination changes require investigation before choosing
the finalization utility. Do not treat a pre-write existence check as race safety.

See [Plan verification](03_plan_csv-export.md#verification) and
[questions](01_brief_csv-export.md#questions-and-decisions).
