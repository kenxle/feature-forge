# Forge MVP alongside the pstack trial

The MVP is on main, and the local Claude and Codex development skills are updated. Claude supports symlinked skill folders. For cloud sessions, provision a Forge checkout in the cloud VM and link the skills there, or commit installed copies in the project. The pstack trial can run in parallel.

The default feature route is short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Agents adapt their path to the actual task. The package includes the selected principles, writing guidance, and scoped comment review, and keeps the documentation record without routine human document approval.

## Use in Claude Code cloud sessions

Claude supports symlinked skill folders. My earlier recommendation was too restrictive. A symlink works when its target exists in the session's filesystem. A laptop-only target is unavailable in a cloud VM. [Anthropic's symlink support](https://code.claude.com/docs/en/skills#choose-where-skills-load) and [cloud filesystem guidance](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup).

For maintaining one source, I recommend a shared Forge checkout with symlinks:

- Locally, link the skill folders to the shared Forge checkout. Updating that checkout updates what those links expose.
- In the cloud, bootstrap a separate checkout of the same Forge revision inside the VM and create the equivalent skill links there. Keep all sibling skills and supporting files together so their relative links resolve.
- Record the chosen revision. Refresh it when adopting an update, and keep it stable during a development run.

A cloud environment setup script can provision the checkout before Claude starts. Setup scripts can be cached, so they do not guarantee a fetch on every session. [Cloud setup scripts and caching](https://code.claude.com/docs/en/cloud-environments#environment-caching).

For refreshes at session start, use a repository SessionStart hook. If that hook creates or updates skills, return `reloadSkills: true` so Claude re-scans after the hook completes. Anthropic documents this exact shared-skills pattern. [Reload skills that a hook installs](https://code.claude.com/docs/en/hooks#reload-skills-that-a-hook-installs). Repository hooks in Anthropic-hosted sessions apply only to sessions with one repository. [Cloud hook limitations](https://code.claude.com/docs/en/cloud-environments#limitations-in-cloud-sessions).

Committed project copies remain an alternative when a project should carry its Forge version without a startup fetch. For that route, run the [existing installer](../../../scripts/install.py) from the Forge checkout. Replace the example path with the target project's actual path:

```sh
python3 scripts/install.py /absolute/path/to/your-project --dry-run
python3 scripts/install.py /absolute/path/to/your-project
```

Commit and push all installed skill folders and supporting files under `.claude/skills/`, then start the cloud session on that branch. The installer refuses existing destinations, so compare and preserve older copies before updating. [Anthropic's repository skill guidance](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions).

The skill instructions need no separate Forge service. For the optional HTML renderer, make Pandoc available in the cloud environment. Configure the project's build tools and test services there too. Cloud environment setup scripts install missing tools before Claude starts. [Cloud environment configuration](https://code.claude.com/docs/en/cloud-environments#setup-scripts).

The [shared bootstrap and update tool](../../BOARD.md) is follow-up work. The current installer copies files. The local installs have not been converted to shared-checkout links, and no cloud bootstrap or cloud run has been verified.

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
