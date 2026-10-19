# Feature Forge Board

## Backlog

- **Move to multiple runbooks:** [MVP landed on main and installed locally](features/runbooks/MVP.md), with principles, the revised feature flow, adaptable routes, and writing/comment guidance. Package checks, installed-renderer smoke checks, and independent instruction review pass. The pstack trial can run in parallel. Keep pstack architect and arena outside the MVP. The [selection record](features/runbooks/PSTACK_SELECTIONS.md) preserves follow-up work, including actual consumer trials and unattended board work. Preserve Whetstone and the explicit full dossier review option.

- **Auto-merge for low-risk features:** Follow the [unattended shipping plan](features/runbooks/README.md#unattended-work-and-shipping). Establish project authorization and verification before automatic merging; distinguish landing disabled code from enabling its feature flag. Runner setup and consumer validation remain pending.

- **Share and update Forge installations:** Add shared-checkout linking and a cloud bootstrap so local and cloud sessions can use the same chosen revision without maintaining separate skill copies in every project. Handle cached environments and skill discovery after startup hooks. Preserve existing local changes during adoption. Retain committed project copies as an option and keep the fresh installer's overwrite refusal. Verify discovery in a real cloud session. See the [cloud distribution recommendation](features/runbooks/MVP.md#use-in-claude-code-cloud-sessions).
