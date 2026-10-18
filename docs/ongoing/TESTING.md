# Testing

## Charter

**What belongs:** How testing works: what runs, how to run it and what counts as green. The commands for each test layer. What the CI gate runs. Setup a new builder needs.

**What does not:** Why a feature was built a certain way. Test cases for one feature.

**Level of detail:** Commands and short notes. Enough to run every suite.

**Describes:** `tests/`, `scripts/`, `skills/feature-forge/scripts/`

**Sources:** [package tests](../../tests/test_package.py), [verification scope](../verification.md), [repository instructions](../../AGENTS.md). No CI configuration is present.
## Run the package checks

Use Python from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

No Python third-party dependencies are needed. Install Pandoc to exercise HTML composition. Without it, the rendering test reports a skip. Treat that as incomplete renderer verification when changing rendering behavior.

## What the suite covers

The [package tests](../../tests/test_package.py) check fresh and dry-run installation, conflict refusal preserving edits, installed renderer assets, local Markdown link targets, include escape/cycle/missing-source rejection, dossier composition with review history and navigation, and evidence failure reporting with prior-run preservation.

The [CSV fixture](../../tests/fixtures/csv-export/README.md) is synthetic renderer input. It is not evidence of an implemented consumer application.

## What counts as green

Run the full suite after changing skills, helpers or tests. Resolve failures. Report optional skips explicitly. Before pushing, scan tracked content for private paths and dependencies using the command in [repository instructions](../../AGENTS.md). Inspect each hit rather than treating an empty test log as proof of portability.

The repository currently has no checked-in CI workflow. The command above is the local verification gate; branch protection and remote checks are not established by these files.

## Limits and change-specific checks

The suite does not prove agent compliance, review independence, consumer feature completion, LAHE runtime integration, non-Claude installation, browser behavior or deployment success. Follow the consuming project's own checks for those outcomes. A process refactor needs observed use of the changed workflow in addition to package tests. Do not present a prose instruction as an enforced runtime guarantee.

See [verification scope](../verification.md) for the earlier extraction checks. Keep historical observations separate from a new run's evidence.
