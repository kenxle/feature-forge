# Package shipping facts

## Base branch

main

## CI command

`python3 -m unittest discover -s tests -v`

This is the local verification gate. No CI workflow is checked in.

## PR conventions

Keep each change focused. Include relevant proof. Separate wording changes from behavior changes.

## Merge method

Not specified in the repository. Follow the user's authorization and remote repository policy.

## Deploy platform and how to watch it

No hosted runtime is shipped. Pushing publishes repository content; it does not establish consumer installation or rollout.

## Health check

Run the package tests and inspect the private-reference scan described in [repository instructions](../AGENTS.md).

## Migration verification

Installed skills are copies. Compare before updating and preserve consumer edits. The installer refuses existing destinations.

## Smoke command

`python3 scripts/install.py /absolute/path/to/an-existing-project --dry-run`

Supply an actual existing destination when running this example.

## Browser walkthrough entry points

The optional renderer produces local dossier HTML from the [CSV fixture](../tests/fixtures/csv-export/README.md). There is no running product UI.

## Refuse list

Do not overwrite installed local changes, publish private references, or claim consumer feature completion from package tests.
