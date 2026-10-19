# pstack selections for Feature Forge

Build the Forge MVP in parallel with the pstack trial. Bring in the principles, writing guidance, and scoped comment review. The default feature route is short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Agents adapt the route to the actual task rather than forcing every task through it. The trial is not a prerequisite. Agents produce documents and evidence without routine human document approval. See the [MVP status](MVP.md).

## Status and source

Selections below reflect the maintainer's Lahe review. Original files are saved under [selected/pstack](selected/pstack/). Those archive copies are not installed or active instructions. The MVP packages principles, technical-writing, unslop, no-comments, and Comment Sicko, with local guidance for using them. Other selected integrations remain follow-up work. The source revision is `6b78e9f4e46c75d1697d837e51f07c2692e60b24`. The [upstream MIT license](selected/pstack/LICENSE) accompanies the copies. Copied skill directories and playbooks were compared byte-for-byte with that checkout.

The saved [Poteto mode source](selected/pstack/skills/poteto-mode/SKILL.md) preserves the context of selected passages. Saving it does not select every rule or every playbook in it. Unmarked passages remain unselected.

## Keep unchanged

| Material | Selection and integration |
|---|---|
| [Comment Sicko agent](selected/pstack/agents/comment-sicko.md) | Included exactly as written. The [local adapter](../../../skills/feature-forge/references/comment-review.md) provides the narrow how/why investigations it needs and maps delegation to the host. No general how/why workflow is imported. |
| [Principles section](selected/pstack/sections/principles.md) | Included in the MVP as individually loaded leaves. Archived originals remain unchanged under [selected skills](selected/pstack/skills/). The package redirects the optional benchmark-checklist link upstream rather than bundling that skill. See the [source record](../../../skills/feature-forge/vendor/pstack/UPSTREAM.md). |
| [Autonomy section](selected/pstack/sections/autonomy.md) | Keep the complete section unchanged as selected source. Integration must respect the host's action permissions and the consuming project's standing release authority. Its default deployment pause and session overrides must be reconciled with Forge's automatic release policy in the integration guidance. The source copy itself remains unchanged. |

## Keep the guidance and supporting sources

| Guidance | Source and disposition |
|---|---|
| Investigate nontrivial changes and architectural uncertainty | Defer general [how](selected/pstack/skills/how/SKILL.md) and [why](selected/pstack/skills/why/SKILL.md) integration. Keep the investigations needed for Comment Sicko through its local adapter. Forge already investigates the affected code in its existing architecture process. |
| Work observable questions before asking the human | Keep the selected Poteto mode guidance. Use experiments or prototypes for facts that can be observed. Keep read-only investigations focused on a cited answer. Genuine product preferences still belong to the human unless existing authority covers the decision. |
| Name the data shape before logic | Keep [Model the Domain](selected/pstack/skills/principle-model-the-domain/SKILL.md). |
| Explore design before implementation | Leave pstack [architect](selected/pstack/skills/architect/SKILL.md) out of the MVP. Keep the saved source for possible later evaluation. Forge's existing architecture skill remains part of the feature flow. |
| Skill authoring follows an established provider skill | Use the host's official skill-authoring guidance, such as OpenAI's skill-creator or Cursor's create-skill. Keep the package portable rather than making one host's built-in a universal dependency. |
| Clear technical documents | Included [technical-writing](selected/pstack/skills/technical-writing/SKILL.md) through the [writing guidance](../../../skills/feature-forge/references/writing.md). Preserve the consuming project's writing conventions. |
| Clear prose | Included [unslop](selected/pstack/skills/unslop/SKILL.md) through the writing guidance. |
| Comment review | Included [no-comments](selected/pstack/skills/no-comments/SKILL.md) as upstream source alongside Comment Sicko. The local adapter uses their guidance for scoped review without the external architect or model setup. |

## Adapt before integration

| Material | Decision |
|---|---|
| [swarm](selected/pstack/skills/swarm/SKILL.md) | Full workflow adaptation remains deferred. The MVP adopts shared principles: builders and reviewers receive the same index and relevant leaves through their contracts. Keep existing delegation judgment and separate writable outputs. |
| Arena | Excluded for now. Compare alternative designs in prototypes when useful without importing the arena workflow or a model competition. |
| [interrogate](selected/pstack/skills/interrogate/SKILL.md) | The MVP incorporates intent, common review scope, evidence-based findings, synthesis, disagreement, and reasoned dispositions in its [reviewer guidance](../../../skills/feature-forge/references/reviewers.md). The full skill and model configuration remain deferred. |
| Throughput checkpoint in the [feature playbook](selected/pstack/skills/poteto-mode/playbooks/feature.md) | Put it in the Plan's implementation strategy: blocking prerequisites, independent workstreams, shared writable state, and smallest safe decomposition. Update the Plan when the strategy changes; Progress links to it and records changes. It is not another human approval gate or a second acceptance table. |
| [Babysit](selected/pstack/skills/poteto-mode/playbooks/babysit.md) | Promising PR follow-through guidance. Merge with Forge's existing handling of CI, conflicts, and review feedback. This is not a request to import every host-specific polling rule. |
| [Shipping](selected/pstack/skills/poteto-mode/playbooks/shipping.md) | Compare against Forge's current shipping process and merge or replace it deliberately. Preserve independent verification of each PR, dependency-safe landing order, release evidence, and standing authority for automatic releases. |

## Smaller runbook set

Keep the main routes in the [refactor plan](README.md#proposed-runbooks) as useful starting points. Agents may combine or change paths for the actual task. Keep explicit user choices, useful documents, and shared verification outcomes. Reuse focused task guidance instead of forcing every task through a prescribed route or copying the entire Poteto playbook catalog.

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
- Arena, general how/why workflow integration, and pstack architect in this MVP. Prototype variants and narrow comment investigations cover the selected needs.

## Pilot observations to retain

Run the pstack trial and Forge MVP independently. Record which flows were used, where the agent needed human help, how verification caught or missed problems, whether the documents were useful, and where orchestration or review repeated work. Save evidence before making claims about velocity or cost. Use observations to refine later integration; do not restart the full Forge dossier just to report the pilot.
