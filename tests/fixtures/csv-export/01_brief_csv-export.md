# Brief: CSV export

<!-- forge-include: parts/brief/context.md -->

## Requirements

R1: A user exports notes as UTF-8 CSV with title and body columns.
R2: CSV quoting preserves commas, quotes and line breaks.
R3: Existing output is preserved unless the user explicitly authorizes replacement.

## Analytics and rollout

No new telemetry: this local CLI handles potentially sensitive notes. Errors
use existing stderr behavior. No flag: the command is additive; existing commands
remain compatible.

## Questions and decisions

<!-- forge-include: parts/brief/questions.md -->

## PM findings

Illustrative PM finding: clarify overwrite behavior. Accepted into R3.
Full illustrative review is appended by the renderer.

See [verification](03_plan_csv-export.md#verification).
