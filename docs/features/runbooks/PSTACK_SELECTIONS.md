# pstack selections for Feature Forge

Next: try pstack on real features and record what works before implementing the Forge integration. The intended Forge sequence is short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Agents produce the documents and evidence; routine human document approval is removed in favor of releases supported by verification and standing authority.

## Status and source

Selections below reflect the maintainer's Lahe review. Original files are saved for integration under [selected/pstack](selected/pstack/). They are source material, not installed or active instructions. The source revision is `6b78e9f4e46c75d1697d837e51f07c2692e60b24`. The [upstream MIT license](selected/pstack/LICENSE) accompanies the copies. Copied skill directories and playbooks were compared byte-for-byte with that checkout.

The saved [Poteto mode source](selected/pstack/skills/poteto-mode/SKILL.md) preserves the context of selected passages. Saving it does not select every rule or every playbook in it. Unmarked passages remain unselected.

## Keep unchanged

| Material | Selection and integration |
|---|---|
| [Comment Sicko agent](selected/pstack/agents/comment-sicko.md) | Import the agent exactly as written. Resolve its how/why dependencies before invoking it. |
| [Principles section](selected/pstack/sections/principles.md) | Keep the complete section. All upstream principle leaf directories are saved unchanged under [selected skills](selected/pstack/skills/). This includes domain modeling, simplification, real proof, verifiable units, context management, and lessons. |
| [Autonomy section](selected/pstack/sections/autonomy.md) | Keep the complete section unchanged as selected source. Integration must respect the host's action permissions and the consuming project's standing release authority. Its default deployment pause and session overrides must be reconciled with Forge's automatic release policy in the integration guidance. The source copy itself remains unchanged. |

## Keep the guidance and supporting sources

| Guidance | Source and disposition |
|---|---|
| Investigate nontrivial changes and architectural uncertainty | Keep [how](selected/pstack/skills/how/SKILL.md). Read the affected system before choosing a change. [why](selected/pstack/skills/why/SKILL.md) is also saved for Comment Sicko's dependency. |
| Work observable questions before asking the human | Keep the selected Poteto mode guidance. Use experiments or prototypes for facts that can be observed. Keep read-only investigations focused on a cited answer. Genuine product preferences still belong to the human unless existing authority covers the decision. |
| Name the data shape before logic | Keep [Model the Domain](selected/pstack/skills/principle-model-the-domain/SKILL.md). |
| Explore design before implementation | Keep [architect](selected/pstack/skills/architect/SKILL.md). Fit it into Forge's architecture work so it supplies evidence and alternatives without creating a duplicate document pipeline. |
| Skill authoring follows an established provider skill | Use the host's official skill-authoring guidance, such as OpenAI's skill-creator or Cursor's create-skill. Keep the package portable rather than making one host's built-in a universal dependency. |
| Clear technical documents | Keep [technical-writing](selected/pstack/skills/technical-writing/SKILL.md) as selected source. Preserve the consuming project's writing conventions. |
| Clear prose | Keep [unslop](selected/pstack/skills/unslop/SKILL.md) as selected source. |
| Comment review | Keep [no-comments](selected/pstack/skills/no-comments/SKILL.md) alongside Comment Sicko. Define their distinct jobs or use one to invoke the other so the same check is not repeated. |

## Adapt before integration

| Material | Decision |
|---|---|
| [swarm](selected/pstack/skills/swarm/SKILL.md) | Useful and close to Forge's existing delegation. Adapt model names, host APIs, cloud assumptions, and reporting. Preserve task contracts, separate writable outputs, and evidence. Use judgment about whether delegation helps. |
| Arena | Optional experiment, not a default or a required dependency. Consider lower-cost model candidates and combine their useful parts when the comparison earns its cost. No automatic arena use for ordinary implementation. |
| [interrogate](selected/pstack/skills/interrogate/SKILL.md) | Useful foundation. Combine with Forge's reviewer perspectives where they add value. Adapt model configuration and keep independent judgment without a fixed reviewer chain. |
| Throughput checkpoint in the [feature playbook](selected/pstack/skills/poteto-mode/playbooks/feature.md) | Put it in the Plan's implementation strategy: blocking prerequisites, independent workstreams, shared writable state, and smallest safe decomposition. Update the Plan when the strategy changes; Progress links to it and records changes. It is not another human approval gate or a second acceptance table. |
| [Babysit](selected/pstack/skills/poteto-mode/playbooks/babysit.md) | Promising PR follow-through guidance. Merge with Forge's existing handling of CI, conflicts, and review feedback. This is not a request to import every host-specific polling rule. |
| [Shipping](selected/pstack/skills/poteto-mode/playbooks/shipping.md) | Compare against Forge's current shipping process and merge or replace it deliberately. Preserve independent verification of each PR, dependency-safe landing order, release evidence, and standing authority for automatic releases. |

## Smaller runbook set

Keep the main routes in the [refactor plan](README.md#proposed-runbooks). Reuse focused task guidance within them rather than copying the entire Poteto playbook catalog.

- [Bug fix](selected/pstack/skills/poteto-mode/playbooks/bug-fix.md): selected. Integrate reproduction, root-cause work, and evidence into the direct-change route.
- [Feature](selected/pstack/skills/poteto-mode/playbooks/feature.md): merge selected parts into Forge's core feature route. Preserve Forge's documents and the revised prototype-first sequence.
- [Refactoring](selected/pstack/skills/poteto-mode/playbooks/refactoring.md): selected source for behavior-preserving work and proof.
- [Prototype](selected/pstack/skills/poteto-mode/playbooks/prototype.md): selected source. Preserve Forge's option to retain and harden the prototype.
- [Eval](selected/pstack/skills/poteto-mode/playbooks/eval.md): selected source for checking skill and workflow changes before promotion.

## Leave out

- The cursor-team-kit deslop dependency and mandatory pre-commit invocation.
- The host-specific control-ui/control-cli requirement. Keep Forge's general requirement to verify behavior through the appropriate actual interface using the project's available tools.
- The benchmark-checklist integration for now. Keep it in pstack; this is not a current Forge focus. The separately selected principles remain intact.
- The complete playbook catalog and automatic copying of every step into a todo list.

## Pilot observations to retain

Record which pstack flows were used, where the agent needed human help, how verification caught or missed problems, whether the documents were useful, and where orchestration or review repeated work. Save evidence before making claims about velocity or cost. Use those observations to refine the selected integration; do not restart the full Forge dossier just to report the pilot.
