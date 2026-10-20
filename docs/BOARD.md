# Feature Forge Board

## Backlog

- **Assignment helper deferred:** The user chose to defer restoring the script that packages agent assignments to reduce token usage. Try the smaller dossier and selective reading first. Revisit tooling only if inspecting what workers actually receive shows avoidable context cost that remains. The [audit decision](features/runbooks/LEGACY_AUDIT.md#helper-for-preparing-agent-assignments) records the deferral.

- **Move to multiple runbooks:** [MVP landed on main and installed locally](features/runbooks/MVP.md), with principles, the revised feature flow, adaptable routes, and writing/comment guidance. Package checks, installed-renderer smoke checks, and independent instruction review pass. The pstack trial can run in parallel. Keep pstack architect and arena outside the MVP. The [selection record](features/runbooks/PSTACK_SELECTIONS.md) preserves follow-up work, including actual consumer trials and unattended board work. Preserve Whetstone and the explicit full dossier review option.

- **Auto-merge for low-risk features:** Follow the [unattended shipping plan](features/runbooks/README.md#unattended-work-and-shipping). Establish project authorization and verification before automatic merging; distinguish landing disabled code from enabling its feature flag. Runner setup and consumer validation remain pending.

- **Load global Forge skills into cloud sessions:** Keep the existing global local setup. Configure cloud environment setup to download Forge and install its skills globally inside the VM. No per-project Forge files or links are needed. Use the existing installer with the VM home directory as its target. Handle later updates and cached environments without overwriting consumer edits. Verify skill discovery in a real cloud session. See the [cloud setup recommendation](features/runbooks/MVP.md#use-in-claude-code-cloud-sessions).

- **Roll out the hard shipping rule to cloud agents:** Refresh cloud skill copies and any older shipping instructions. Confirm that a failing full suite blocks release even when failures predate the change or come from missing setup keys. The package and local copies are updated; existing cloud sessions have not been changed from here. See the [hard shipping rule](features/runbooks/MVP.md#hard-shipping-rule).

## Completed

- **Reviewed restorations implemented:** Focused references restore product thinking, environment readiness, progress, handoffs, modular authoring, UI fidelity and style checks, post-launch verification, closeout, and local principles. Evidence capture identifies working contents and setup. Dossiers render Mermaid as offline SVG with readable scrolling on narrow pages. Full package checks, real renderer and browser proof, fresh installation, and independent review pass. Local global skill copies were compared, backed up, updated, and checked. See [implementation progress](features/restoration/PROGRESS.md), [verification](features/restoration/PLAN.md#verification), and [review dispositions](features/restoration/REVIEW.md). The [audit](features/runbooks/LEGACY_AUDIT.md) preserves the agreed choices.

## Decisions

- **Leave operational review criteria out of the restoration plan:** The user declined the proposed checklist restoration. Preserve the [audit comparison and decision](features/runbooks/LEGACY_AUDIT.md#operational-review-criteria) as history. Existing verification and review requirements continue to apply.
