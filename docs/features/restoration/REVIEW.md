# Independent restoration review passes

The independent reviewer inspected the integrated code and selected audit scope.
No unresolved findings remain. The [Plan](PLAN.md#verification) owns acceptance
and evidence status. The reviewer reused the implementation owner's full-suite,
fresh-install, browser, validator, and portability evidence where it matched.

## Findings and dispositions

- **Symlinked ancestor traversal, corrected.** A tracked directory replaced by
  a symlink caused descendant hashes to read outside the repository. The
  [evidence helper](../../../skills/feature-forge/scripts/forge_support.py)
  records that boundary without reading targets. The reviewer independently
  reproduced the original failure and rechecked the fix.
- **Directory replaced by file, corrected.** Missing tracked descendants caused
  capture to abort before running the command. The helper now records them as
  missing. A [regression fixture](../../../tests/test_evidence.py) proves that the
  verification command still runs.
- **Narrow-page diagram readability, corrected.** Fitting diagrams to the page
  made labels too small. The [diagram helper](../../../skills/feature-forge/scripts/doc_diagrams.py)
  preserves intrinsic sizing inside a focusable scroll region. The reviewer
  inspected the updated desktop and narrow-page screenshots and browser record.
  Wrapper markup was corrected during this change.

## Scope and limits

The required guidance is linked from the relevant routes. Product thinking
precedes the prototype, UI review honors the approved baseline, and the hard
shipping rule remains intact. The deferred assignment helper, excluded
operational checklist, and unselected cross-document checklist were not restored.

Real Mermaid CLI output was inspected, not just stand-in output from unit tests.
Browser proof covers diagrams from the main source, an included leaf, and a
review sibling in house and plain styles. Labels, local keyboard scrolling,
navigation, disclosures, and offline operation pass.

Package tests do not prove a consumer deployment or agent compliance. Snapshots
do not lock files or establish ignored setup, symlink targets, submodule contents,
or external state. There is no automatic reuse of passing results.
