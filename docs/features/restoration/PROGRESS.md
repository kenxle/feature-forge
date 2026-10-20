# The selected restorations are implemented

The selected guidance is restored, tested-content evidence is recorded, and
Mermaid diagrams render offline. Local Claude and Codex skill copies are updated.
Package checks and independent review pass. The implementation is pushed to main.

## Attention needed

None. Diagram builds require separately installed Mermaid CLI and compatible
Node and browser dependencies. Direct Markdown review remains available.

## Work and evidence

- Instructions: focused references are linked from the relevant routes. The
  approved prototype and feedback remain the UI acceptance baseline.
- Evidence helper: before and after file manifests, described setup, preserved
  output, and explicit limits are implemented. Dirty filesystem states and
  capture errors are covered by behavior tests.
- Renderer: real Mermaid CLI builds flowcharts, graphs, and sequence diagrams
  from main documents, includes, and review history. Offline browser checks pass
  for house and plain styles. Wide diagrams scroll with keyboard support.
- Verification: the full suite and skill validators pass. Fresh installation,
  private-reference scan, and [independent review](REVIEW.md) pass. The
  [Plan](PLAN.md#verification) owns the verification table.
- Local installation: existing copies matched known package revisions. Both host
  copies were backed up and updated. Packaged files match source; extra consumer
  files are preserved. Existing agent sessions may still hold previously loaded
  instructions until they read the updated files or start a new session.

## Documents

- [Agreed audit scope](../runbooks/LEGACY_AUDIT.md)
- [Implementation plan](PLAN.md)
- [Source entry point](../../../skills/feature-forge/SKILL.md)
- [Review findings and dispositions](REVIEW.md)
- [Filesystem boundary lesson](../../lessons/tested-source-boundaries.md)

## Release and closeout

Published to main. No consumer application is deployed by this package change.
The existing board retains cloud installation, unattended board work, and the
deferred assignment helper. The operational checklist and unselected
cross-document checklist remain outside this restoration. The implementation
worktree is retained while its live review remains available.
