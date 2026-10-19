# Forge MVP alongside the pstack trial

The MVP is on main, and the local Claude and Codex development skills are updated. For Claude Code cloud sessions, install and commit the package in each project repository, as described below. The local update alone does not reach the cloud. The pstack trial can run in parallel.

The default feature route is short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Agents adapt their path to the actual task. The package includes the selected principles, writing guidance, and scoped comment review, and keeps the documentation record without routine human document approval.

## Use in Claude Code cloud sessions

I recommend committing the installed package in each project that uses it. Cloud sessions load the cloned repository's `.claude/skills/` and cannot read the skills installed only on your laptop. [Anthropic's cloud skill guidance](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions) confirms this distinction.

From your up-to-date Feature Forge checkout, run the [installer](../../../scripts/install.py) against the target project. Replace the example path with that project's actual path:

```sh
python3 scripts/install.py /absolute/path/to/your-project --dry-run
python3 scripts/install.py /absolute/path/to/your-project
```

Then complete the setup in that project:

- Commit and push the installed `feature-forge`, `brief`, `architecture`, `plan`, and `whetstone` folders under `.claude/skills/`. Keep their supporting files, including vendored sources and license. The installer refuses existing destinations, so compare and preserve older copies before updating.
- Check that Git tracks those folders. Use real committed files rather than links to folders on your laptop.
- Start a new cloud session on the branch containing that commit. Ask Claude to read `.claude/skills/feature-forge/SKILL.md` to confirm the installed version, then invoke `/feature-forge` or `/whetstone`. Cloud sessions launched from the terminal clone the remote branch, so push first. [Anthropic's cloud launch guidance](https://code.claude.com/docs/en/claude-code-on-the-web#start-a-cloud-session-from-your-terminal).

The skill instructions need no separate Forge service. For the optional HTML renderer, make Pandoc available in the cloud environment. Configure the project's build tools and test services there too. Cloud environment setup scripts install missing tools before Claude starts. [Cloud environment configuration](https://code.claude.com/docs/en/cloud-environments#setup-scripts).

Account-wide skills enabled through claude.ai are another supported distribution route. For this linked package, I recommend repository copies first so each project records its chosen version. [Anthropic's account skill guidance](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions).

This explains the setup. No consuming project's cloud installation has been changed yet, and no cloud run has been verified.

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
