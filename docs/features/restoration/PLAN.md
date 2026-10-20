# Restore the agreed guidance and rendering support

Implement the selected [audit restorations](../runbooks/LEGACY_AUDIT.md) while
keeping the new routes lightweight. The assignment helper stays deferred, the
operational checklist stays excluded, and unselected cross-document consistency
stays outside scope. No new approval gates or fixed reviewer rosters.

## Implementation strategy

Use one implementation owner and separate commits for instructions, evidence
capture, and rendering behavior. The source references can be written together.
Evidence capture and diagram rendering are independent behavior changes with
their own tests. Integrate and check the complete installed package before landing.
Shared writable state is limited to this worktree. Existing reviews and installed
consumer copies remain separate until compared and deliberately updated.

## Verification

| Requirement | Acceptance and failure case | Command or observation | Owner | Evidence and status |
|---|---|---|---|---|
| Practical references | Product thinking, readiness, progress, handoffs, modular authoring, UI fidelity and style automation, post-launch proof, closeout, local principles are discoverable from relevant routes | Read installed entry points and links against selected audit scope | Implementation owner | Pass. Entry points validated; [independent scope review](REVIEW.md) passes. |
| Tested-code identity | Dirty, untracked, deleted, executable and symlink state identified before and after a command; setup and limits recorded; old runs preserved | Behavior tests and real helper invocation | Implementation owner | Pass. [Behavior tests](../../../tests/test_evidence.py) and independent filesystem probes pass. Capture errors preserve results and fail visibly. |
| Faithful diagrams | Mermaid from main docs, includes and review siblings becomes readable offline SVG in house and plain output; invalid or missing tooling fails before overwriting pages | Renderer tests, real Mermaid CLI, browser inspection | Implementation owner | Pass. [Diagram tests](../../../tests/test_diagrams.py), fresh-install real CLI builds, and desktop and narrow-page browser checks pass. Diagram labels retain intrinsic size, with keyboard scrolling. Network requests blocked; no scripts or page overflow. |
| Package compatibility | Source containment, navigation, components, installation refusal, portable text, full suite pass | Package suite, install smoke, private-reference scan | Implementation owner | Pass. Full suite passes without skips. Fresh installed renderer builds; skill validators pass; scan contains only established generic examples and the test pattern. Local copies matched known revisions before backup and update. |
| Integrated review | Independent review of code and agreed restoration coverage, with real rendered flow inspection | Focused review and dispositions | Independent reviewer | Pass. [Findings corrected and rechecked](REVIEW.md), with no unresolved finding. |

## Authority and limits

The user requested implementation of the reviewed plan. Repository instructions
authorize publication of completed work. Run all required checks before landing.
There is no deployed product runtime in this package, so consumer post-launch
verification and actual agent compliance remain outside package proof.

See [Progress](PROGRESS.md) for current work and outcomes.
