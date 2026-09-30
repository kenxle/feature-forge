Outcome: safe CSV export through the CLI.
Sources: Brief R1/R3, Architecture Design and Failure modes; read R2 for variants.
Scope: command registry, writer, destination utility and their tests.
Authority: implement slice, no shipping approval; independent reviewer owns completion.
Dependency: existing note reader. Integration owner: assigned feature lead.
Constraint: no telemetry or unrelated refactor. Uncertainty: stop and raise unsafe
destination finalization rather than guessing. Proof: Plan rows. Deliver code,
actual evidence, inspected revision, deviations and unresolved questions.
