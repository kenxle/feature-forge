# Verification scope

Run `python3 -m unittest discover -s tests -v` from the package root.
Tests cover dry-run and fresh install, overwrite refusal preserving local edits,
installed renderer assets, include cycle/escape/missing-source rejection, and
Pandoc dossier composition with review history and offline navigation.
Pandoc checks skip explicitly when the optional executable is unavailable.

The CSV dossier under `tests/fixtures/` is renderer test data, not an implemented
application. Package checks do not establish completion of a consumer's feature.
Non-Claude host installation has not been tested.

## Local extraction verification

Package tests passed locally, including Pandoc rendering. A fresh temporary clone
of the committed package also passed the suite, installed into a new temporary
consumer project, rendered the dossier through the installed renderer, and
resolved every generated local HTML navigation link. The installer refused a
second install and preserved a deliberately edited local skill. Evidence capture
recorded a deliberately failing command's actual output and nonzero status and
refused reuse of its evidence directory.

Private-reference scan found no machine paths or private skill dependencies in
the package; the sole shared-assets mention is its exclusion in the research credits.
The existing LICENSE was inspected and retained. Old renderer/header dependencies
were inspected rather than copied; no vendor assets are included. Tests verify
files and helper behavior, not Claude Code's runtime skill selection or an actual
LAHE review session in a consumer project.
