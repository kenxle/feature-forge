# Lighter Feature Forge runbooks

Plan for the next implementation session. Make prototype-first work the normal route for new user experiences, automate well-understood board work, and retain the full dossier as an option. Keep verification strong while giving agents more freedom over how they build.

## Current status

Planning only. No packaged skills or installed copies have changed. The product direction below comes from the maintainer's request. The implementation details are recommendations, not an approved shipping policy for consuming projects.

No decision is needed to start the package refactor. Additional pstack files can be evaluated when supplied. Cloud scheduling, project credentials, board adapters, and permission to merge belong to each consuming project and require separate setup.

## What changes

- Feature Forge becomes a small router that loads the runbook relevant to the work.
- For a new user experience, clarify the idea briefly, then build a clickable high-fidelity prototype before writing the brief. Skip wireframes.
- Use the prototype conversation to settle scope and record how far the agent may proceed. Documents then develop from that agreement and the agent continues through verified implementation and authorized shipping.
- Small understood work can begin from an existing request or board item. It should not require a new Whetstone spec that repeats the same information.
- Keep the full dossier route for work that benefits from it or when the human explicitly wants it.
- Keep acceptance evidence and independent review. Remove repeated approvals, fixed reviewer chains, and development prescriptions that do not improve those outcomes.

The [product brief](../../ongoing/PRODUCT_BRIEF.md) already establishes velocity, agent judgment, multiple runbooks, and robust verification as goals. The [current orchestrator](../../../skills/feature-forge/SKILL.md) still requires a dossier and approval before implementation. The [current Whetstone skill](../../../skills/whetstone/SKILL.md) still requires a compact spec. Those are the main constraints this refactor changes.

## Proposed runbooks

| Runbook | When to use it | Minimum record | Human involvement |
|---|---|---|---|
| Direct change | Understood fixes, maintenance, and small behavior changes | Existing request or board item, acceptance, evidence, and outcome | Only unresolved product decisions or approval the project actually requires |
| Prototype first | A new or substantially changed user experience | Prototype decision, brief, architecture, Plan, and concise progress | Early alignment and hands-on prototype review; return only for material changes or required shipping permission |
| Full dossier | Consequential or ambiguous work, or an explicit request for the existing process | Existing comprehensive dossier and review history | Consolidated dossier review before build |
| Board automation | A cloud or local runner picks up eligible work without a person present | Claimed board item, scope and authority, linked implementation record, evidence, and outcome | Eligibility and shipping policy established ahead of the run; unresolved items return to the board |

Board automation is an execution wrapper. It uses the direct-change route or resumes an already agreed feature. It cannot invent approval for a new product experience just because the task is on the board.

Keep `/whetstone` as a compatible entry point to the direct-change runbook. Preserve existing Whetstone records. This avoids breaking installed habits while removing a separate competing process.

Nonvisual work does not need a decorative prototype. Use a concrete example, executable spike, API interaction, or the dossier route when that better exposes the decision.

## Prototype first, then documents

Start with a short crucible conversation: the problem, intended user, desired outcome, constraints, and the decision the prototype must resolve. Reuse what the request already answers.

Build the main flow with realistic content and the project's design language. Include the states that matter to the decision, such as an empty result, error, or permission boundary. Let the human click through it. Explore alternatives when there is a real choice, without making a fixed set of variants compulsory.

Record the chosen behavior and any unresolved questions. Label simulated data and interactions. State whether the prototype will be discarded or developed into production code. Reusing it does not exempt it from production checks.

From the agreed experience, derive the brief's requirements. Use architecture to resolve implementation choices and hidden risks. Use the Plan to define coherent slices and own the verification table. Documents should preserve useful reasoning without repeating the prototype narrative in every file.

Continue without a second document gate when the existing agreement and project policy authorize it. Ask again only when new evidence changes a material product choice, scope, risk, or shipping authority. A prototype establishes the intended experience; it does not establish backend correctness or release safety.

## Verification is the common foundation

Use one acceptance and evidence record. The Plan owns it when a Plan exists. Otherwise it lives with the compact task record. Link to existing project verification instructions instead of reproducing them.

- Verify observable behavior through the real interface, including meaningful failure cases and side effects.
- Use focused tests during development and the project's required integrated checks before shipping. Prefer test-first work when it helps establish the contract; do not manufacture tests for prose or trivial reversible changes.
- Keep independent code review and acceptance review for behavior changes. A suitable reviewer can own both. Choose other specialist reviews for concrete risks, rather than a fixed roster.
- Walk changed user flows before PR. Use browser tools for browser flows and the appropriate real interface for CLI, API, or library work.
- Record the revision, relevant environment, commands or observations, and pass/fail/unverified status. Reuse evidence only when the code and conditions still match.
- If a required check cannot run, report the gap and stop at the permitted boundary. Do not turn missing verification into a passing result.

Allow the agent to choose implementation order, tools, delegation, and refactoring approach within project constraints. Preserve valued PM review for substantial briefs and the Plan testing checkpoint; select their scope to answer actual uncertainties.

## Less code and less maintenance

Prefer existing capabilities and simpler data flow before adding another abstraction. Inspect actual callers before removing duplication or compatibility paths. Keep refactors related to the task, and separate unrelated cleanup.

Reducing lines is a useful direction, not a quota. Do not trade clarity, tests, accessibility, security checks, or useful domain explanations for a smaller diff. The review question is whether the change delivers the behavior with fewer concepts and less maintenance burden.

Apply the same standard to the skills themselves. Put shared rules in one place, avoid duplicated approval instructions, and load only the relevant runbook. Keep detailed alternatives in source leaves for later inspection.

## Unattended work and shipping

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

## Implementation slices

Each slice should leave the package usable. Reuse this plan across slices rather than restarting the documentation process.

| Slice | Change | Completion evidence |
|---|---|---|
| Routing and compatibility | Make the Feature Forge entry point a router. Add direct-change and full-dossier runbooks. Make Whetstone a compatible entry point. Keep shared verification and shipping rules authoritative. | Package suite and independent scenario review of route selection and existing behavior |
| Prototype-first development | Add the prototype runbook. Update brief, architecture, Plan, and templates so the agreed route determines approval timing. Record prototype decisions and reusable-code status. | Walk a representative new UI request through alignment, prototype, documents, and build authorization |
| Verification and maintainability | Revise the build loop and reviewer guidance around outcomes. Add selected pstack references and practical simplification guidance. Preserve independent acceptance checks. | Review a small fix, a nonvisual change, and a consequential change for adequate proof without redundant process |
| Unattended board contract | Add the board runbook, eligibility and claim requirements, resumable outcomes, shipping boundaries, and flag records. Keep scheduler implementation outside the package. | Dry-run eligible, ambiguous, already-claimed, interrupted, and verification-blocked tasks against a representative project |
| Consumer pilot | Compare installed copies before updating one chosen project. Exercise the routes with that project's real tools. Record friction and revise the package first. | Observed end-to-end work and honest limits; no velocity claim based only on package tests |

Update the [overview](../../../README.md), [product brief](../../ongoing/PRODUCT_BRIEF.md), [architecture](../../ongoing/ARCHITECTURE.md), [testing guidance](../../ongoing/TESTING.md), and [Lahe pairing guidance](../../lahe.md) with the slices that change their claims. Keep the installer and renderer unchanged unless an actual runbook need requires code changes.

The Lahe pairing document currently tells agents to read lifecycle rules from review data. Reconcile that with the installed Lahe skill, which treats the skill as authority and review data as feedback. Keep this correction separate from the runbook design where practical.

## Verification table

This is the authoritative verification table for the refactor. Evidence remains pending until implementation runs it.

| Requirement | Acceptance and failure case | Check | Owner | Evidence/status |
|---|---|---|---|---|
| Match process to work | A small understood fix proceeds without a redundant dossier; ambiguous work gets appropriate discovery | Independent route scenarios using the actual revised skills | Independent acceptance reviewer | Pending |
| Prototype before documents | A new UI request reaches a clickable high-fidelity prototype before its brief; simulated behavior is disclosed | Representative prototype-first walkthrough | Independent acceptance reviewer | Pending |
| Preserve the full route | Explicit full-dossier requests still receive comprehensive records and consolidated review | Full-route scenario and package tests | Independent acceptance reviewer | Pending |
| Continue under existing authority | Agreed work proceeds without repeated gates; material changes and forbidden shipping actions stop at the correct boundary | Authorization scenarios for each route | Independent acceptance reviewer | Pending |
| Retain meaningful proof | Changed behavior has real evidence and independent review; unavailable required checks remain unverified | Inspect an integrated example and its acceptance record | Independent acceptance reviewer | Pending |
| Keep unattended ownership safe | Concurrent or resumed runs do not duplicate ownership, PRs, or side effects | Consumer adapter tests or serialized-run demonstration | Consumer runner owner | Pending; package prose cannot enforce this |
| Separate landing from activation | Disabled flags preserve current behavior; activation follows recorded authority | Consumer flag and release checks | Consumer release owner | Pending |
| Keep the package portable | Relative links resolve, installation preserves local changes, private references are absent | Full package suite and private-reference scan | Implementer | Pending |
| Reduce process burden | Representative work shows which human interruptions and repeated documents were avoided, alongside quality outcomes | Record pilot actions and evidence; compute any counts from saved run data | Pilot owner | Pending; no measured improvement claimed |

## Resume here

Read this plan and the repository instructions. Check current work and fetch remotes before choosing the implementation branch. Begin with routing and compatibility. Inspect any additional pstack materials the maintainer has supplied. Keep installed copies unchanged until their local differences have been compared.

The planning branch is `runbooks`. This record is the handoff, not a claim that the new workflows or overnight runner are implemented.
