# Feature Forge Board

## Backlog

- **Restore practical guidance around the new runbooks:** The [legacy audit inventory](features/runbooks/LEGACY_AUDIT.md) compares the pre-update installed skills, the earlier public package, and the current structure. Review proposed restoration of environment readiness, release checks, progress/handoff templates, authoring/rendering support, quality criteria, and closeout. Retain the new routes, agent judgment, and hard shipping rule. This is an inventory, not implemented restoration.

- **Restore environment readiness, selected for the plan:** Add shared guidance for required keys, services, migrations, data, and the running application before implementation and final proof. Use it across the feature and Whetstone routes. Keep missing setup visible as a shipping blocker. The [audit decision](features/runbooks/LEGACY_AUDIT.md#working-environment) records the selected scope; implementation is pending.

- **Restore automated post-launch verification, selected for the plan:** Use repeatable scripts and Playwright to check the live release. Have an LLM examine the launched feature or bug-fix flow using browser interaction and captured evidence. Record the deployed revision, operational checks, flag state, recovery, and findings. Missing required checks leave verification incomplete and require follow-through. The [audit decision](features/runbooks/LEGACY_AUDIT.md#verification-after-landing) records the selected scope; implementation is pending.

- **Move to multiple runbooks:** [MVP landed on main and installed locally](features/runbooks/MVP.md), with principles, the revised feature flow, adaptable routes, and writing/comment guidance. Package checks, installed-renderer smoke checks, and independent instruction review pass. The pstack trial can run in parallel. Keep pstack architect and arena outside the MVP. The [selection record](features/runbooks/PSTACK_SELECTIONS.md) preserves follow-up work, including actual consumer trials and unattended board work. Preserve Whetstone and the explicit full dossier review option.

- **Auto-merge for low-risk features:** Follow the [unattended shipping plan](features/runbooks/README.md#unattended-work-and-shipping). Establish project authorization and verification before automatic merging; distinguish landing disabled code from enabling its feature flag. Runner setup and consumer validation remain pending.

- **Load global Forge skills into cloud sessions:** Keep the existing global local setup. Configure cloud environment setup to download Forge and install its skills globally inside the VM. No per-project Forge files or links are needed. Use the existing installer with the VM home directory as its target. Handle later updates and cached environments without overwriting consumer edits. Verify skill discovery in a real cloud session. See the [cloud setup recommendation](features/runbooks/MVP.md#use-in-claude-code-cloud-sessions).

- **Roll out the hard shipping rule to cloud agents:** Refresh cloud skill copies and any older shipping instructions. Confirm that a failing full suite blocks release even when failures predate the change or come from missing setup keys. The package and local copies are updated; existing cloud sessions have not been changed from here. See the [hard shipping rule](features/runbooks/MVP.md#hard-shipping-rule).
