# Verification scope

Run `python3 -m unittest discover -s tests -v` from the package root.
Tests cover dry-run and fresh install, overwrite refusal preserving local edits,
installed renderer assets, include cycle/escape/missing-source rejection, and
Pandoc dossier composition with review history and offline navigation.
Pandoc checks skip explicitly when the optional executable is unavailable.

The worked feature is illustrative, not an implemented application. Its
acceptance is pending; package smoke checks do not establish feature completion.
No browser review, non-Claude host installation, PR, merge or release is claimed.
