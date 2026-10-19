# Legacy source excerpts

Exact excerpts from the preserved pre-update installed skills. The source manifest records file fingerprints. These excerpts are evidence for the audit, not active skill instructions.

## environment-readiness

A working environment before implementation and verification

Source: `feature-forge/SKILL.md`. Category: restore-first.

> Before dispatching implementation agents, confirm the infrastructure the feature needs, such as the dev servers, is still running.

Current gap: Isolation and final checks remain, but there is no practical readiness step for configuration keys, services, migrations, seed data, or a running app.

History: Already absent in this detail from the pre-runbook public package.

## production-verification

Concrete verification after landing

Source: `feature-forge/references/post-deploy-checklist.md`. Category: restore-first.

> - [ ] **Error monitoring:** No new errors in logs, error tracking, or monitoring dashboards
> - [ ] **Performance:** No significant degradation in response times or resource usage

Current gap: The new text says to verify the release and distinguish merged, deployed, and enabled. It no longer supplies the operational checks that make that statement useful.

History: The detailed checklist was not in the pre-runbook public package.

## visible-progress

A stable progress page with meaningful update events

Source: `feature-forge/references/document-templates.md`. Category: restore-first.

> The lede is rewritten on every update

Current gap: Progress is reduced to a list of topics. The creation/opening step, accountable writer, task owners, current blockers, and event-driven updates are no longer explained.

History: The public template was already compressed before the runbook rewrite.

## worker-handoffs

Separate worker detail and durable review history

Source: `feature-forge/references/agent-contracts.md`. Category: restore-first.

> outcome, changed files, verification commands and evidence paths, a quick screenshot when the work has a visible surface, deviations,
> blockers, follow-ups, and `## Cleanup needed`.

Current gap: Contracts still name completion evidence, and review siblings still compose. The practical return format and ownership of the detailed record disappeared.

History: The concrete templates were already missing from the public package.

## authoring-contract

Document authoring and source-to-render instructions

Source: `feature-forge/references/document-templates.md`. Category: restore-first.

> Write components as LAHE house components: small HTML blocks inside the Markdown

Current gap: Modular includes survive, but the component guidance, title/lede shape, source-versus-output editing rule, and practical composed-review instructions do not.

History: The detailed conventions were not carried into the pre-runbook public templates.

## renderer-compatibility

The document rendering capabilities behind the old conventions

Source: `feature-forge/scripts/build_feature_docs.py`. Category: restore-first.

> Diagrams:  ```mermaid fenced blocks (rendered client-side)

Current gap: The old installed renderer handled house components, legacy callouts, section layout, folded contents, review-finding links, and Mermaid. The bundled renderer keeps composition/navigation but uses a much smaller fallback stylesheet.

History: The simplified renderer dates to the public extraction, before the runbook rewrite. A fresh probe confirms the current output limitations.

## ui-quality

An explicit bar for the finished user experience

Source: `plan/SKILL.md`. Category: restore-first.

> Honest feedback. Toasts and status messages report what actually happened. Never an optimistic "done" for something still in flight, or something that failed.

Current gap: The new route retains high-fidelity prototypes, staff design, customer personas, and design-language references. The concrete acceptance floor for the integrated product is weaker.

History: The richer Plan acceptance criteria were already absent from the public baseline.

## review-operational-checks

Operational code-review prompts, especially the cost of writes

Source: `feature-forge/references/code-review-checklist.md`. Category: restore-first.

> - How often does it write? Per keystroke, per event, per poll, per commit? Name the trigger.
> - How much does each write carry? The changed part, or the whole record or file?

Current gap: Reviewer ownership and findings improved. Specific checks for write amplification, API compatibility, queries, idempotence, actionable errors, privacy, and operational logging are now mostly left to generic judgment or selected principles.

History: The concrete checklist did not exist in the pre-runbook public package.

## cleanup-and-lessons

A complete closeout, including small changes

Source: `feature-forge/SKILL.md`. Category: restore-first.

> Lessons are written as they happen

Current gap: Docs, diagrams, lessons, and owned cleanup remain in the new text. The explicit obligation to check them even for small changes, capture each surprise, and close the whole record has softened.

History: The detailed lifecycle was absent earlier. The small-change lesson requirement was softened specifically by the runbook rewrite; compare the earlier public Whetstone cleanup change.

## cross-doc-consistency

A compact document consistency and feasibility check

Source: `../.codex/feature-forge/references/doc-review-checklist.md`. Category: restore-later.

> - [ ] The plan covers every component described in the architecture. No architecture component is orphaned.

Current gap: Requirements, alternatives, contracts, and the Plan table remain. The explicit check that the documents describe the same scope and a feasible integrated build is no longer concrete.

History: This is from the older installed Codex copy, not an asserted contract of the recent public package.

## premise-no-build

Challenge the premise, including the option to build nothing

Source: `feature-forge/SKILL.md`. Category: restore-later.

> Challenge premise, force alternatives, answer "what if we do nothing,"

Current gap: The new route resolves the premise and explores prototype alternatives. The explicit no-build or existing-capability alternative has faded.

History: The pre-runbook public router explicitly mentioned doing nothing; that explicit option disappeared in the rewrite.

## packet-helper

Heading-selected dispatch packets

Source: `feature-forge/scripts/forge_support.py`. Category: restore-later.

> def packet(args):

Current gap: The current helper only captures verification runs. The old packet command selected source headings and validated the contract fields; the contract concept itself survives.

History: This command was already absent from the first public helper.

## evidence-provenance

Evidence identity beyond a commit hash

Source: `feature-forge/scripts/forge_support.py`. Category: restore-later.

> def fingerprint(repo,evidence):

Current gap: The current helper explicitly admits that its revision does not identify uncommitted or external state. The old helper recorded content and environment fingerprints, but also overwrote logs and used shell command parsing.

History: The simpler evidence implementation predates the runbook rewrite.

## local-principle-adapter

Local principle additions and the lesson-to-mechanism loop

Source: `feature-forge/references/principles.md`. Category: restore-later.

> - **Cheap checks first.** Order checks from cheapest to most expensive.

Current gap: The new package has the selected upstream leaves and better on-demand routing. The old installed collection also had local additions about repeated knowledge, broken tooling, check ordering, and routing lessons into mechanisms.

History: These local additions are not evidence that the selected upstream files were imported incorrectly.
