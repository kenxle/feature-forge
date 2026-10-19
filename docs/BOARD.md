# Feature Forge Board

## Backlog

- **Move to multiple runbooks:** [MVP landed on main and installed locally](features/runbooks/MVP.md), with principles, the revised feature flow, adaptable routes, and writing/comment guidance. Package checks, installed-renderer smoke checks, and independent instruction review pass. The pstack trial can run in parallel. Keep pstack architect and arena outside the MVP. The [selection record](features/runbooks/PSTACK_SELECTIONS.md) preserves follow-up work, including actual consumer trials and unattended board work. Preserve Whetstone and the explicit full dossier review option.

- **Auto-merge for low-risk features:** Follow the [unattended shipping plan](features/runbooks/README.md#unattended-work-and-shipping). Establish project authorization and verification before automatic merging; distinguish landing disabled code from enabling its feature flag. Runner setup and consumer validation remain pending.

- **Update installed Forge copies together:** Add a repeatable update command for selected project and global installations. Record the source revision, detect consumer edits before replacement, preserve conflicts for review, and commit project copies so cloud sessions receive the chosen version. Keep the existing fresh installer's overwrite refusal. See the [cloud distribution recommendation](features/runbooks/MVP.md#use-in-claude-code-cloud-sessions).
