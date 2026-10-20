# Source identity needs filesystem boundary checks

A Git commit does not identify dirty working contents. A list of tracked paths
does not establish that those paths still lead to repository files either.

While restoring evidence capture, independent review found that replacing a
tracked directory with a symlink caused a descendant's hash to read outside the
repository. Replacing the directory with a regular file also caused capture to
fail before the verification command could run.

The [evidence helper](../../skills/feature-forge/scripts/forge_support.py) now
checks lexical ancestors before opening a candidate. It records symlink
boundaries as unfingerprinted and missing descendants as missing. The
[regression tests](../../tests/test_evidence.py) exercise both replacements.
Before and after manifests expose ordinary changes during a check, while the
[evidence contract](../../skills/feature-forge/references/tested-code-evidence.md)
states that snapshots are not a filesystem lock or proof of external state.

For future source collectors, distinguish a path's recorded name from the
filesystem object reached when it is opened. Test valid dirty states as well as
ordinary modified files. Keep tested work isolated from concurrent writers.
