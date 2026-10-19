# Forge MVP alongside the pstack trial

The MVP is on main, and the local Claude and Codex development skills are updated. Keep the current global setup locally. For cloud sessions, install Forge globally inside the VM through its environment setup. The project needs no Forge files or links. The pstack trial can run in parallel.

The default feature route is short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Agents adapt their path to the actual task. The package includes the selected principles, writing guidance, and scoped comment review, and keeps the documentation record without routine human document approval.

## Use in Claude Code cloud sessions

Yes. Keep the global setup on your laptop and load Forge into the cloud VM's global skills folder. The project needs no Forge copies, symlinks, or update commits. I added unnecessary project setup to the recommendation.

The intended setup is:

- Keep the current local global installations.
- Add commands to the cloud environment's Setup script that download this Forge repository and install its skills into the VM's global skills folder before Claude starts.
- Use that environment for your cloud development sessions. Confirm that Claude discovers Feature Forge in a fresh session.

By "bootstrap" I meant those setup commands. No additional service is involved. Anthropic documents [setup scripts that run before Claude starts](https://code.claude.com/docs/en/cloud-environments#setup-scripts) and [global skill folders](https://code.claude.com/docs/en/skills#choose-where-skills-load). Loading skills installed into the VM this way is the setup to verify in an actual cloud session.

The [existing installer](../../../scripts/install.py) can target the VM's home directory. From a downloaded Forge checkout in a fresh VM, the install command is:

```sh
python3 scripts/install.py "$HOME"
```

This creates the global skill folders inside that VM. It does not copy anything from your laptop. The installer refuses existing destinations, so a later update must preserve or compare those copies first.

Cloud environments cache installed files. Updating Forge on GitHub does not immediately update an existing VM or cached environment. Refreshing that environment is a separate update step. [Environment caching](https://code.claude.com/docs/en/cloud-environments#environment-caching).

The [cloud setup work](../../BOARD.md) is recorded on the board. Your local setup remains as installed. The cloud environment has not been configured or tested yet.

## What is ready

- [Feature Forge](../../../skills/feature-forge/SKILL.md) selects the default [prototype-first route](../../../skills/feature-forge/references/runbooks/prototype-first.md), [Whetstone](../../../skills/whetstone/SKILL.md), or the explicit [full dossier review](../../../skills/feature-forge/references/runbooks/full-dossier.md).
- The [brief](../../../skills/brief/SKILL.md), [architecture](../../../skills/architecture/SKILL.md), [Plan](../../../skills/plan/SKILL.md), and [templates](../../../skills/feature-forge/references/templates.md) agree on the short brief and later PRD. The throughput checkpoint lives in the Plan.
- [Verification and release](../../../skills/feature-forge/references/verification-and-release.md) retains TDD, independent code and acceptance review, real changed-flow evidence, and release under existing authority.
- The [principles index](../../../skills/feature-forge/references/principles.md) loads the vendored pstack leaves. Their [source record and license](../../../skills/feature-forge/vendor/pstack/UPSTREAM.md) preserve provenance. The optional benchmark checklist points upstream instead of becoming a dependency.
- Delegated agents receive the same principles index through [work contracts](../../../skills/feature-forge/references/contracts-and-slices.md). The [reviewer guidance](../../../skills/feature-forge/references/reviewers.md) incorporates intent, evidence, synthesis, disagreements, and reasoned dispositions.
- The consuming project's existing voice-of-customer persona judges remain available for prototype and user-facing review alongside specialist reviewers. Their own persona definitions and research stay with the project.
- [Writing guidance](../../../skills/feature-forge/references/writing.md) loads technical-writing and unslop. The [comment adapter](../../../skills/feature-forge/references/comment-review.md) dispatches the unchanged Comment Sicko prompt and supplies narrow how/why investigations. Its upstream no-comments source is preserved.

## Verification

The full package suite passes, including the Pandoc renderer check. Fresh installation carries the principles index and license and preserves overwrite refusal. Maintained Markdown links resolve. Frozen upstream review snapshots are excluded from link assertions because their original examples and unselected references remain intact. Empty reports and lessons folders now have tracked placeholders so their existing links resolve in fresh checkouts.

Independent instruction review found and resolved the renderer's previous filename limit: Plan and Progress are now retained in the longer dossier. The new regression test failed before that fix and passes afterward. Missing required review or evidence now explicitly blocks release readiness. The reviewer also passed the writing/comment adapter by inspection. No blocking findings remain. See the [verification record](MVP_REVIEW.md). Consumer use, adapter execution, cloud execution, real deployment, and productivity improvement remain unverified.

The OpenAI generic skill validator rejects the existing Claude-specific user-invocable frontmatter on all entry points. That host compatibility limitation is unchanged; it is not reported as a passing validation. The package's own installation, link, evidence, and rendering checks pass.

## Follow-up scope

Pstack architect and arena are outside this MVP. The [selection record](PSTACK_SELECTIONS.md) retains other saved sources for later evaluation. The full plugin, general how/why workflows, full swarm/interrogate adaptations, board runner, upstream update automation, and wholesale Autonomy-section integration remain follow-up work.

## Local adoption

The global Feature Forge, brief, architecture, Plan, and Whetstone skills now match the landed package. The existing installations were compared first and preserved in backups outside skill discovery. Codex's user-skill directory points to its updated copies. No project-local copies were found in the workspace scan. The existing cleanup skill's Progress-template link was updated to the new template location.

Content checks confirmed that the installed package files match source. Both installed renderers built the sample dossier successfully. The package suite passed with Pandoc and no optional skips. These checks establish installation and rendering, rather than completion of a real feature using the new process. The package installer still refuses existing destinations.
