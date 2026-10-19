# Better Feature Forge runbooks

Implementation plan and follow-up scope. Use this feature sequence: short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land. Automate well-understood board work and retain the full dossier review route as an option. Agents still write and maintain the documents. The human need not read and approve them before authorized work ships.

## Current status

The MVP is on main: principles, the revised default feature flow, adaptable routes, writing/comment guidance, and shared verification/release. The local Claude and Codex development skills are updated, with previous copies preserved in backups. Package checks pass and independent instruction review has no blockers. See the [MVP status](MVP.md) and [verification record](MVP_REVIEW.md).

Develop and use the Forge MVP in parallel with the maintainer's pstack trial. The [selection record](PSTACK_SELECTIONS.md) preserves the chosen sources and adaptations. The external architect skill is outside the MVP. Cloud board runners, other selected helper integrations, and update automation remain follow-up work. Consuming projects supply their own release authority and tools.

## What changes

- Feature Forge becomes a small router that loads the runbook relevant to the work.
- For a new user experience, write a short brief with target users, their context, the problem, and the desired outcome. Then build a clickable high-fidelity prototype. Derive the PRD's detailed requirements from the agreed experience.
- Use the prototype conversation to settle scope and record how far the agent may proceed. Documents then develop from that agreement and the agent continues through verified implementation and authorized shipping.
- Small understood work can begin from an existing request or board item. The agent writes and maintains its spec, decisions, and evidence without waiting for the human to read and approve those documents before authorized shipping.
- Keep the full dossier route for work that benefits from it or when the human explicitly wants it.
- Keep acceptance evidence and independent review. Remove human approvals and instead use confidence based auto-releases. No fixed reviewer chains, use judgment. Development prescriptions should become runbooks that allow agency and judgment.

The [product brief](../../ongoing/PRODUCT_BRIEF.md) establishes velocity, agent judgment, multiple runbooks, and robust verification as goals. [Feature Forge](../../../skills/feature-forge/SKILL.md) and [Whetstone](../../../skills/whetstone/SKILL.md) now separate document production from routine human approval gates. Agents keep the records complete while proceeding under existing authority.

## Proposed runbooks

| Runbook | When to use it | Minimum record | Human involvement |
|---|---|---|---|
| Direct change | Understood fixes, maintenance, and small behavior changes | Compact spec linked to the request or board item, decisions, acceptance, evidence, and outcome | Confidence-based automatic release under standing project authority; unresolved product decisions return to the human |
| Prototype first | A new or substantially changed user experience | Short brief, prototype decision, PRD, architecture, Plan, and concise progress | Early alignment and hands-on prototype review, followed by confidence-based automatic release; return for material product changes |
| Full dossier | Consequential or ambiguous work, or an explicit request for the existing process | Existing comprehensive dossier and review history | Human dossier approval only when explicitly selected; document depth alone does not require a gate |
| Board automation | A cloud or local runner picks up eligible work without a person present | Claimed board item, scope and authority, linked implementation record, evidence, and outcome | Eligibility and shipping policy established ahead of the run; unresolved items return to the board |

Board automation is an execution wrapper. It uses the direct-change route or resumes an already agreed feature. It cannot invent approval for a new product experience just because the task is on the board.

Keep `/whetstone` as a compatible entry point to the direct-change runbook. Preserve existing Whetstone records. This avoids breaking installed habits while removing a separate competing process.

Nonvisual work does not need a decorative prototype. Use a concrete example, executable spike, API interaction, or the dossier route when that better exposes the decision.

## Short brief, prototype, then detailed documents

Start with a short crucible conversation and a lightweight brief seed: target users, their context, the problem, desired outcome, and the decision the prototype must resolve. Include known constraints that would materially change the experience. Reuse what the request already answers. This seed supplies enough direction to prototype; detailed requirements, acceptance criteria, and implementation specifics come afterward.

Build the main flow with realistic content and the project's design language. Include the states that matter to the decision, such as an empty result, error, or permission boundary. Let the human click through it. Explore alternatives when there is a real choice, without making a fixed set of variants compulsory.

Record the chosen behavior and any unresolved questions. Label simulated data and interactions. State whether the prototype will be discarded or developed into production code. Reusing it does not exempt it from production checks.

Keep the short brief as the initial orientation. Write the PRD from the agreed experience, adding detailed requirements and failure cases while linking back to user context. Do not add a second comprehensive brief that repeats the PRD. Reuse the current brief skill's detailed product guidance for the PRD while preserving existing entry points and records.

Use architecture to resolve implementation choices and hidden risks. Use the Plan to define coherent slices and own the verification table. Its implementation strategy includes the throughput checkpoint: blocking prerequisites, independent workstreams, shared writable state, and the smallest safe decomposition. Progress records changes and links to that strategy. This does not add another document or approval gate.

Continue without a second document gate when the existing agreement and project policy authorize it. Write and maintain the short brief, PRD, architecture, Plan, and progress as the work develops so the human can inspect them whenever useful. Their completion does not create a new requirement for the human to read or approve them. Build behavior changes with TDD, verify the integrated result, ship under standing authority, and follow through to landing and release evidence. Ask again only when new evidence changes a material product choice, scope, risk, or shipping authority. A prototype establishes the intended experience; it does not establish backend correctness or release safety.

## Verification is the common foundation

Use one acceptance and evidence record. The Plan owns it when a Plan exists. Otherwise it lives with the compact task record. Link to existing project verification instructions instead of reproducing them.

- Verify observable behavior through the real interface, including meaningful failure cases and side effects.
- Use TDD for behavior changes, focused checks during development, and the project's required integrated checks before shipping. Do not manufacture tests for prose or trivial reversible changes.
- Keep independent code review and acceptance review for behavior changes. A suitable reviewer can own both. Choose other specialist reviews for concrete risks, rather than a fixed roster.
- Walk changed user flows before PR. Use browser tools for browser flows and the appropriate real interface for CLI, API, or library work.
- Record the revision, relevant environment, commands or observations, and pass/fail/unverified status. Reuse evidence only when the code and conditions still match.
- If a required check cannot run, report the gap and stop at the permitted boundary. Do not turn missing verification into a passing result.

Allow the agent to choose implementation order, tools, delegation, and refactoring approach within project constraints. Keep PM and testing perspectives available and select them when they can resolve actual uncertainties. Do not turn those perspectives into a fixed sequence of reviewers or mandatory handoffs.

## Less code and less maintenance

Prefer existing capabilities and simpler data flow before adding another abstraction. Inspect actual callers before removing duplication or compatibility paths. Keep refactors related to the task, and separate unrelated cleanup.

Reducing lines is a useful direction, not a quota. Do not trade clarity, tests, accessibility, security checks, or useful domain explanations for a smaller diff. The review question is whether the change delivers the behavior with fewer concepts and less maintenance burden.

Apply the same standard to the skills themselves. Put shared rules in one place, avoid duplicated approval instructions, and load only the relevant runbook. Keep detailed alternatives in source leaves for later inspection.

## Unattended work and shipping

Make confidence-based automatic release the default under the consuming project's standing authority. Feature Forge should not add a per-release human approval gate. Record the release decision with evidence: acceptance results, independent review findings, remaining uncertainty, affected systems, and recovery options. Confidence must follow that evidence, rather than an unsupported score.

When confidence is insufficient, investigate, improve the implementation, or strengthen verification. Release when the evidence supports it. If a genuine product decision, missing permission, or unavailable prerequisite remains, record that specific blocker. Do not routinely send completed work to the human for approval. Existing project restrictions still apply until that project deliberately changes them.

Read the existing project board instead of adding a competing task system. Define the smallest eligibility contract that the runner needs:

- The intended behavior and measurable acceptance are clear.
- Dependencies and required inputs are available.
- The task is explicitly eligible for unattended work under project policy.
- Allowed actions are stated: implement, open a PR, merge, deploy, and enable a flag are distinct permissions.
- Verification commands and any necessary environment are available.
- Ownership and outcome can be recorded durably.

Claim work before starting. The adapter must prevent concurrent workers from claiming the same item. A Markdown edit alone is not an atomic lock. Use the scheduler or board service's ownership mechanism, or serialize workers until a safe claim mechanism exists.

Work in isolation. On restart, reconcile the claim with the branch, PR, and recorded evidence before retrying. Avoid duplicate PRs and repeated external side effects. Keep ambiguous or blocked items visible with the exact missing decision or prerequisite, then continue other eligible work within the run's scope.

Set a finite run budget and a stopping condition in the runner. Preserve useful progress when the budget ends. Do not let a stuck task retry indefinitely or expand into unrelated repair work.

The morning summary should link each attempted item to its outcome: landed, PR ready, blocked, or still in progress. Include evidence and anything the human must decide. Distinguish merged code from a verified deployment.

Feature flags can let authorized changes land disabled. Check the disabled and enabled paths, migrations, startup behavior, background jobs, and side effects. Record the flag's name, actual state, owner, activation prerequisites, and cleanup condition in the project's existing durable documentation. This makes disabled features discoverable by a later documentation audit without building a private integration into this portable package.

## pstack candidates

Inspected the upstream repository at revision `6b78e9f4e46c75d1697d837e51f07c2692e60b24`. These are candidates to reference or adapt, not files already imported. The source repository identifies Lauren Tan as pstack's author. [Upstream repository](https://github.com/cursor/plugins/tree/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack).

| Source | Proposed use |
|---|---|
| [Subtract before you add](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/principle-subtract-before-you-add/SKILL.md) | Inform concise guidance on reducing unnecessary code and instructions |
| [Test behavior, not implementation](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) | Strengthen the standard for tests that detect broken behavior and survive internal refactoring |
| [Prove it works](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/principle-prove-it-works/SKILL.md) | Ground completion in direct observation and repeatable evidence |
| [Create a verification skill](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/create-verification-skill/SKILL.md) | Recommend project-local launch, drive, evidence, and cleanup instructions when a project lacks them |
| [Maintain a verification skill](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/maintain-verification-skill/SKILL.md) | Inform upkeep of the project's behavior map and verification harness |
| [Blast radius](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/blast-radius/SKILL.md) | Check downstream effects and execute a test of the assumption that makes the change safe |
| [Prototype playbook](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/skills/poteto-mode/playbooks/prototype.md) | Compare decision-focused prototyping; retain our option to keep and harden the prototype |

Start with references and narrowly adapted principles. Do not import pstack's whole orchestration stack, fixed delegation rules, or host-specific paths. Compare further files supplied by the maintainer before selecting imports. Substantial copied material must retain the upstream [MIT notice](https://github.com/cursor/plugins/blob/6b78e9f4e46c75d1697d837e51f07c2692e60b24/pstack/LICENSE).

Use the [complete pstack source index](pstack-index.md) to mark any additional files for consideration.

## Selected pstack material and updates

The maintainer selected [Comment Sicko](selected/pstack/agents/comment-sicko.md) for import exactly as written. The saved file is byte-for-byte identical to the upstream agent at revision `6b78e9f4e46c75d1697d837e51f07c2692e60b24`. Its [MIT license](selected/pstack/LICENSE) is preserved alongside it. This is the selected source for later integration; it has not been installed or invoked.

Recommendation: keep selected upstream files in Forge with their source revision recorded, rather than requiring the entire pstack plugin. Preserve each selected original unchanged. Put Forge's routing and integration guidance beside it so updates remain easy to compare.

During implementation, add an upstream update check that compares each selected file and its license against the recorded revision. Report changed files with their diffs for review. Apply accepted updates in a focused commit and advance the recorded revision. A scheduled check can open an update PR when the project's automation is configured; it should not silently replace the agent's instructions. Consumers receive accepted updates through Forge's normal copy-and-compare installation process.

Comment Sicko calls the pstack `/how` and `/why` skills. Resolve those dependencies before invoking the unchanged agent. Their supporting files must be considered during integration; selecting this agent does not automatically select the whole plugin. Keep reviewer selection based on judgment rather than making this agent a compulsory gate.

The subsequent review selected the complete principles and Autonomy section, supporting skills, and a smaller runbook set. See the [selection record](PSTACK_SELECTIONS.md) for what to keep unchanged, adapt, or leave out. Original source copies are preserved there; these selections do not install the whole pstack orchestrator.

## Implementation slices

Each slice should leave the package usable. Reuse this plan across slices rather than restarting the documentation process.

| Slice | Change | Completion evidence |
|---|---|---|
| Routing and compatibility | Make the Feature Forge entry point a router. Add direct-change and full-dossier runbooks. Make Whetstone a compatible entry point. Keep shared verification and shipping rules authoritative. | Package suite and independent scenario review of route selection and existing behavior |
| Prototype-first development | Add the short brief, prototype, PRD, architecture, Plan, TDD, verification, ship, and land sequence. Update skills and templates so the agreed route determines approval timing. Put the throughput checkpoint in the Plan. | Walk a representative new UI request through the complete sequence without routine document approval |
| Verification and maintainability | Revise the build loop and reviewer guidance around outcomes. Add selected pstack references and practical simplification guidance. Preserve independent acceptance checks. | Review a small fix, a nonvisual change, and a consequential change for adequate proof without redundant process |
| Unattended board contract | Add the board runbook, eligibility and claim requirements, resumable outcomes, confidence-based automatic release decisions, and flag records. Keep scheduler implementation outside the package. | Dry-run eligible, ambiguous, already-claimed, interrupted, and verification-blocked tasks against a representative project; demonstrate automatic release under standing authority |
| Consumer pilot | Compare installed copies before updating one chosen project. Exercise the routes with that project's real tools. Record friction and revise the package first. | Observed end-to-end work and honest limits; no velocity claim based only on package tests |

Update the [overview](../../../README.md), [product brief](../../ongoing/PRODUCT_BRIEF.md), [architecture](../../ongoing/ARCHITECTURE.md), [testing guidance](../../ongoing/TESTING.md), and [Lahe pairing guidance](../../lahe.md) with the slices that change their claims. Keep the installer and renderer unchanged unless an actual runbook need requires code changes.

The Lahe pairing document currently tells agents to read lifecycle rules from review data. Reconcile that with the installed Lahe skill, which treats the skill as authority and review data as feedback. Keep this correction separate from the runbook design where practical.

## Verification table

This is the authoritative verification table for the refactor. Evidence remains pending until implementation runs it.

| Requirement | Acceptance and failure case | Check | Owner | Evidence/status |
|---|---|---|---|---|
| Match process to work | A small understood fix retains its spec, decisions, and evidence while proceeding without routine human document approval; ambiguous work gets appropriate discovery | Independent route scenarios using the actual revised skills | Independent acceptance reviewer | Instruction review passed; [record](MVP_REVIEW.md) |
| Prototype before detailed specification | A new UI request uses a short brief with target users and context, then reaches a clickable high-fidelity prototype before the PRD; architecture and Plan follow, then TDD, verification, ship, and land | Representative feature walkthrough | Independent acceptance reviewer | Instructions reviewed and dossier rendering passes; actual consumer walkthrough unverified |
| Preserve the full route | Full-dossier requests retain comprehensive records; consolidated human approval remains available when explicitly selected | Full-route scenario and package tests | Independent acceptance reviewer | Instruction review and existing dossier fixture pass |
| Continue under existing authority | Agreed work proceeds without repeated gates; material changes and forbidden shipping actions stop at the correct boundary | Authorization scenarios for each route | Independent acceptance reviewer | Instruction review passed; actual consumer execution unverified |
| Release on evidence-based confidence | Sufficiently verified work releases automatically under standing authority; missing proof prompts further work or a specific blocker, not a routine human approval request | Release scenarios with strong evidence, failed checks, unresolved uncertainty, and restricted authority | Independent acceptance reviewer | Instruction review passed; actual consumer merge/deploy unverified |
| Retain meaningful proof | Changed behavior has real evidence and independent review; unavailable required checks remain unverified | Inspect an integrated example and its acceptance record | Independent acceptance reviewer | Package red/green and independent review recorded; consumer feature proof unverified |
| Keep unattended ownership safe | Concurrent or resumed runs do not duplicate ownership, PRs, or side effects | Consumer adapter tests or serialized-run demonstration | Consumer runner owner | Deferred beyond MVP; no runner implemented |
| Separate landing from activation | Disabled flags preserve current behavior; activation follows recorded authority | Consumer flag and release checks | Consumer release owner | Shared instructions present; consumer verification pending |
| Keep the package portable | Relative links resolve, installation preserves local changes, private references are absent | Full package suite and private-reference scan | Implementer | Passed; [verification record](MVP_REVIEW.md) |
| Reduce process burden | Representative work shows which human reading and approval interruptions were avoided, while documents remain complete and quality outcomes are recorded | Record pilot actions and evidence; compute any counts from saved run data | Pilot owner | Pending; no measured improvement claimed |

## Resume here

Read this plan, the [selection record](PSTACK_SELECTIONS.md), and the repository instructions. Review observations from the maintainer's pstack pilot when available. Check current work and fetch remotes before choosing the implementation branch. Begin with routing and compatibility. Keep installed copies unchanged until their local differences have been compared.

The branch is `runbooks`. The [MVP status](MVP.md) describes implemented scope and proof. The broader plan remains the handoff for subsequent integrations and the overnight runner.
