# Feature Forge Board

## Backlog

- **Move to multiple runbooks:** [MVP landed on main and installed locally](features/runbooks/MVP.md), with principles, the revised feature flow, adaptable routes, and writing/comment guidance. Package checks, installed-renderer smoke checks, and independent instruction review pass. The pstack trial can run in parallel. Keep pstack architect and arena outside the MVP. The [selection record](features/runbooks/PSTACK_SELECTIONS.md) preserves follow-up work, including actual consumer trials and unattended board work. Preserve Whetstone and the explicit full dossier review option.

- **Auto-merge for low-risk features:** Follow the [unattended shipping plan](features/runbooks/README.md#unattended-work-and-shipping). Establish project authorization and verification before automatic merging; distinguish landing disabled code from enabling its feature flag. Runner setup and consumer validation remain pending.

- **Load global Forge skills into cloud sessions:** Keep the existing global local setup. Configure cloud environment setup to download Forge and install its skills globally inside the VM. No per-project Forge files or links are needed. Use the existing installer with the VM home directory as its target. Handle later updates and cached environments without overwriting consumer edits. Verify skill discovery in a real cloud session. See the [cloud setup recommendation](features/runbooks/MVP.md#use-in-claude-code-cloud-sessions).
