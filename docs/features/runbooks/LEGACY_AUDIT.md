# Restore the practical guidance around the new runbooks

The new structure kept the main development and verification duties, but lost useful detail about doing them well. I recommend restoring focused references for setup, release checks, progress, document authoring, UI quality, and closeout. Keep the router small and the prototype-first route intact. This is an inventory for review; this audit has not changed any skills.

The most important distinction is historical. The pre-update installed skill was much richer than the public package before this rewrite. Many gaps already existed in that public package. Git history alone would have missed them. Keeping a full-dossier route preserved its approval option, but did not preserve all the templates and presentation support behind it.

Choose the scope beside each item. **Include in plan** adds it to the restoration scope; **Defer** keeps it as a follow-up; **Leave out** records that it should stay out. I will record your choices here and on the project board. The buttons decide the plan; implementation follows that agreed scope.

**Chosen scope:**

- [Working-environment readiness](#working-environment): check setup before implementation and final proof. Missing prerequisites remain shipping blockers.
- [Automated verification after launch](#verification-after-landing): check the live release with scripts and Playwright, and have an LLM examine the deployed feature or bug-fix flow. Missing required proof remains a blocker.
- [Visible progress](#visible-progress): restore a stable progress page with an accountable writer, meaningful update events, and links to current work and evidence.
- [Worker handoffs and review history](#worker-handoffs-and-review-history): restore optional return and review-round templates, with one writer per detail file and a durable record of evidence, findings, and decisions.
- [Document authoring](#document-authoring): keep focused source files for agents to read on demand, and build those same files into a complete document for the user.
- [Rendering compatibility](#rendering-compatibility), a priority: preserve Lahe's visual quality, components, graphs, and rendered diagrams in the composed documents. Build on the house-style support that has now landed.
- [Finished UI quality](#finished-ui-quality): honor the reviewed prototype and user feedback, use an agent design review when that baseline is absent, and enforce repeatable style rules with tooling.
- [Complete closeout](#complete-closeout): finish the release record, durable docs, diagrams, lessons, board, progress, and owned cleanup, proportionally for small changes too.

**Left out of the restoration plan:** [Operational review criteria](#operational-review-criteria).

Other proposals await your choice.

## Restore first

### Working environment

The old process checked that servers and other infrastructure were running. The new rules require final proof but offer little practical setup guidance. [Old setup check](audit/legacy-excerpts.md#environment-readiness); [current verification](../../../skills/feature-forge/references/verification-and-release.md).

Add a shared readiness reference for required keys, services, migrations, data, and the actual running app. Check prerequisites before implementation and again before final proof. Missing setup remains a shipping blocker.

<div class="choice" data-choice="environment-readiness">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Verification after landing

"Verify the release" survived. Specific checks for production errors, performance, migrations, health, the deployed flow, and recovery became much less concrete. [Old operational checks](audit/legacy-excerpts.md#production-verification); [current release guidance](../../../skills/feature-forge/references/verification-and-release.md#ship-and-land).

Add a short release reference that automates post-launch verification as far as possible. Use repeatable scripts for operational checks and Playwright to exercise the live site. Have an LLM examine the launched feature or bug-fix flow using the actual browser interaction and captured evidence. This complements the checks before release.

Verify the actual deployed revision and record applicable health, migration, error, performance, flag-state, and recovery checks. Keep script output, browser evidence, and the LLM's findings with the release record. Missing required checks leave verification incomplete and require follow-through. Do not restore a routine human approval step.

<div class="choice" data-choice="production-verification">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Visible progress

The current template names the topics but no longer explains who creates the page, how the user finds it, or which events update it. [Old progress guidance](audit/legacy-excerpts.md#visible-progress); [current template](../../../skills/feature-forge/references/templates.md#progress).

Restore a usable progress template and update triggers. Show current work, owners, blockers, document links, proof, and next action. Use tool timestamps. Keep a stable page without freezing the old phase numbers or heading count.

<div class="choice" data-choice="visible-progress">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Worker handoffs and review history

Contract fields and review-sibling composition remain. Concrete worker-return and review-round templates are gone. [Old return record](audit/legacy-excerpts.md#worker-handoffs); [current contracts](../../../skills/feature-forge/references/contracts-and-slices.md).

Add optional templates for changed files, evidence, deviations, surprises, follow-ups, and cleanup. Give each detail file one writer. Preserve earlier review rounds and record dispositions in their owning sources. This makes resumed and unattended work easier to reconstruct.

<div class="choice" data-choice="worker-handoffs">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Document authoring

The new templates list content, but omit much of the guidance for components, title/lede, source editing, composed review, and rebuilding. [Old authoring contract](audit/legacy-excerpts.md#authoring-contract); [current templates](../../../skills/feature-forge/references/templates.md).

Restore the authoring guidance around modular documentation. Keep focused, authoritative source files so each agent consumes only the sections relevant to its work. Build those same files into a complete document for the user to read. Edit the source and rebuild the composed document so the agent and human views stay in sync. The existing includes and review-sibling composition already support this structure.

Add an authoring reference that uses the review tool's component catalog and explains source versus generated output. Keep direct Markdown review for simple pages. Preserve existing conventions and repair tools when they cannot render them.

<div class="choice" data-choice="authoring-contract">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Rendering compatibility

The old installed renderer supported house components, legacy callouts, section layout, folded contents, finding links, and Mermaid. The audited baseline kept includes, review composition, and navigation, but lost much of that presentation contract. [Old renderer evidence](audit/legacy-excerpts.md#renderer-compatibility); [current renderer](../../../skills/feature-forge/scripts/build_feature_docs.py).

**Priority:** Restore the visual quality of the documentation we make with Lahe. Preserve its typography, page layout, components, graphs, and rendered diagrams in the composed human document. Judge the actual rendered pages, including representative components and graphs; preserving their source markup alone is not enough.

**Already landed since the audit baseline:** [House-style support](https://github.com/kenxle/feature-forge/commit/8a17636) now finds the local Lahe style, bundles its CSS and fonts, and restores the expected page layout and legacy callout presentation. The [current style guide](../../ongoing/STYLE_GUIDE.md) describes that support. Mermaid still appears as code in bundled output, so graph and diagram rendering remains restoration work. The recorded probe below describes the older baseline, not this newer implementation.

Complete the remaining compatibility through portable tooling. Keep source containment and offline output, using local assets or build-time rendering for diagrams as appropriate. Do not reintroduce private machine dependencies or a hidden network requirement. Preserve existing document conventions and repair the renderer when it cannot display them faithfully.

<div class="choice" data-choice="renderer-compatibility">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Finished UI quality

High-fidelity prototypes, staff design, and customer personas remain. The integrated product's explicit acceptance floor has weakened. [Old honest-feedback criterion](audit/legacy-excerpts.md#ui-quality); [current reviewer guidance](../../../skills/feature-forge/references/reviewers.md).

Add a concise UI-quality reference that starts with the design already agreed with the user. When a prototype or styles have been reviewed, use that result and the user's feedback as the acceptance baseline. Review the implementation for fidelity and fix drift. Do not use later design reviews to replace approved aesthetic choices with a reviewer's preferences. Surface a material new issue or conflict rather than silently redesigning the approved experience.

When there is no reviewed prototype or style baseline, the agent should do its own design review. Consider hierarchy, shared components/tokens, responsive and accessible states, honest feedback, meaningful motion, brand voice, and consistency across contributors. Keep this proportional to the change, without another mandatory reviewer chain. Functional, accessibility, and required verification checks still apply when the design has been approved.

Enforce repeatable design rules with linters or equivalent automated checks. Start with the consuming project's existing checks and style policy. Useful candidates include raw values that bypass design tokens, prohibited inline styles, and drift between documented tokens and their source. Where component use can be checked reliably, enforce the project's shared-component rules too. Keep legitimate exceptions explicit and narrow.

Run these checks through the project's normal verification command, with hooks where useful. Verify the checks themselves against fixtures that contain violations and valid examples. Browser review verifies the actual experience and fidelity to the agreed design. Use independent design judgment when no reviewed baseline exists. This applies the existing [encode-lessons-in-structure principle](../../../skills/feature-forge/vendor/pstack/skills/principle-encode-lessons-in-structure/SKILL.md).

<div class="choice" data-choice="ui-quality">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Operational review criteria

**Decision: Leave this restoration out of the plan.** The comparison below remains as the audit record.

The reviewer contract improved, but the old checklist supplied useful prompts that generic review can miss. The cost-of-writes questions are especially distinctive. [Old write-cost check](audit/legacy-excerpts.md#review-operational-checks); [current reviewer guidance](../../../skills/feature-forge/references/reviewers.md).

Add risk-triggered prompts for write frequency/payload/flushes, API compatibility, queries, idempotence, privacy, logging, and actionable errors. Restore an explicit check for secrets before publishing. Link existing principles where they already cover the topic.

<div class="choice" data-choice="review-operational-checks">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include">Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out" data-chosen>Leave out</button>
</div>

### Complete closeout

Docs, diagrams, lessons, and owned cleanup remain, but "record useful lessons" is weaker than the old small-change obligation to capture surprises and close the full record. [Old lesson capture](audit/legacy-excerpts.md#cleanup-and-lessons); [earlier public Whetstone cleanup change](https://github.com/kenxle/feature-forge/commit/81a8471665d6a72c4866fedecb16a37146c8aae1); [current Whetstone](../../../skills/whetstone/SKILL.md).

Add a portable closeout reference for release evidence, commits/push, durable docs/diagrams, lessons, the existing board, progress, and owned worktrees. Keep the lesson distinct from a bug ticket. Apply it proportionally to small changes too.

<div class="choice" data-choice="cleanup-and-lessons">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended data-chosen>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

## Restore selectively

### Cross-document consistency

Restore a brief author self-check: scope and terminology agree, the Plan implements the chosen architecture, components have owners, assumptions are supported, and failure cases have proof. The older Codex checklist was concrete here. Do not restore its reviewer chain or confidence cutoff. [Old consistency check](audit/legacy-excerpts.md#cross-doc-consistency); [current Plan](../../../skills/plan/SKILL.md).

<div class="choice" data-choice="cross-doc-consistency">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### The no-build alternative

The previous public router explicitly considered doing nothing. The new route resolves the premise, but that option is less visible. Add a discovery prompt for uncertain requests: existing capability, smaller change, or no change. Do not restore a compulsory interview phase. [Old premise check](audit/legacy-excerpts.md#premise-no-build); [current prototype route](../../../skills/feature-forge/references/runbooks/prototype-first.md#brief-to-prototype).

<div class="choice" data-choice="premise-no-build">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Dispatch packet helper

The old helper could assemble selected source headings into a validated work contract. The current helper only captures verification runs. Restore a small optional packet builder if repeated delegation justifies it. The contract itself already survives; a tool is an aid, not another required step. [Old packet command](audit/legacy-excerpts.md#packet-helper); [current helper](../../../skills/feature-forge/scripts/forge_support.py).

<div class="choice" data-choice="packet-helper">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include">Include in plan</button>
  <button type="button" value="defer" data-recommended>Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Stronger evidence identity

The old helper fingerprinted content and environment. The new helper records a revision and explicitly admits its limits for dirty or external state. Restore reliable identity first, without exposing secrets. Keep immutable evidence folders and argument-list execution. Do not restore log overwriting, shell-string execution, or an unproven reuse cache. [Old fingerprinting](audit/legacy-excerpts.md#evidence-provenance); [current evidence helper](../../../skills/feature-forge/scripts/forge_support.py).

<div class="choice" data-choice="evidence-provenance">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

### Local principle additions

Compare the old local additions with the selected upstream leaves. Retain distinct guidance about repeated knowledge, broken tooling, cheap checks first, and converting lessons into mechanisms in a local adapter. Keep vendored originals unchanged. The newer behavioral-test principle is more nuanced than the old assertion blacklist, so keep it. [Old local additions](audit/legacy-excerpts.md#local-principle-adapter); [current principles](../../../skills/feature-forge/references/principles.md).

<div class="choice" data-choice="local-principle-adapter">
  <p class="choice-q">Include this proposal in the restoration plan?</p>
  <button type="button" value="include" data-recommended>Include in plan</button>
  <button type="button" value="defer">Defer</button>
  <button type="button" value="leave-out">Leave out</button>
</div>

## What was retained

These need useful examples or better discoverability at most, rather than a second implementation:

- The Plan owns the single requirement-to-acceptance/evidence table. Architecture and workstreams reference it.
- Modular source leaves, review-sibling composition, source containment, and dossier navigation still work in the bundled renderer.
- Coherent end-to-end slices, explicit integration ownership, dependency order, and a working application after each landing remain in the contracts guidance.
- TDD, focused iteration checks, integrated proof, independent code and acceptance review, and the final changed-flow walk remain. One named independent owner may cover related checks.
- Open and resolved questions, alternatives, findings, dispositions, and the comprehensive human record are still required at a high level.
- Reviewer/model judgment, agent reuse, bounded source selection, and the distinction between agents, workstreams, slices, and PRs survive.
- Prototype-first development, project design language, and voice-of-customer personas are explicit in the new structure.
- The hard no-errors shipping rule is already restored in the package and local instructions. It must not be diluted while restoring anything else. [Current hard rule](../../../skills/feature-forge/references/verification-and-release.md#hard-shipping-rule).

## What should stay removed

- Routine dossier and merge approval gates. Keep consolidated dossier approval only for the explicitly selected full route or a real project requirement.
- A compulsory interview, rigid phase numbering, mandatory agent-only implementation, fixed reviewer rosters, prescribed model names, reviewer-run caps, and file-count thresholds.
- Fixed test-type ratios and blanket bans based on assertion shape. The current behavioral-test principle judges what a test actually proves.
- Named private tools, machine paths, and a mandatory local style-loader dependency. Restore outcomes through the host's actual tools.
- Re-running unchanged reviews and the full documentation pipeline for every PR. Preserve the current evidence/recheck rules and the passing-full-suite requirement.
- The old evidence helper's log overwriting and automatic reuse behavior. Its useful provenance ideas can return without those risks.

The board runner, cloud installation, upstream sync, and deferred pstack integrations are planned follow-up work. Their absence is not evidence that this rewrite deleted an implemented feature.

## Evidence and historical limits

The audit compared the preserved pre-update Claude installation, the older Codex installation, the public package immediately before the runbook change, and current source at `93c35d1`. The installed backups are not assumed to match a Git revision.

[Public extraction](https://github.com/kenxle/feature-forge/commit/c076849), [runbook rewrite](https://github.com/kenxle/feature-forge/commit/5a450e5), and [later hard shipping correction](https://github.com/kenxle/feature-forge/commit/93c35d1) establish the public history. Where a capability never appeared in that history, the conclusion is a gap between installed and public versions. We cannot tell from this repo whether it was omitted during extraction or added to the local copy afterward. The small-change cleanup wording and the explicit no-build alternative do have a traceable rewrite change.

The [inventory data](audit/inventory.json) gives each proposed restoration its category, source, current comparison, and recommendation. The [collection script](audit/collect_evidence.py) verifies every quoted legacy excerpt, records [source fingerprints and headings](audit/sources.json), and runs the [renderer probe](audit/renderer-probe.json).

The recorded probe of source at `93c35d1` preserved the source and house markup, but emitted Mermaid as code, included no diagram SVG, and bundled no house-component CSS. Dossier navigation remained present. This is evidence about that baseline's bundled offline output, not a test of Lahe's direct Markdown renderer or the house-style support that landed afterward.

I would start with environment readiness and release proof, then restore the records and quality references. Treat renderer compatibility as its own tested tooling change. Keep packet generation and evidence reuse optional until their value is demonstrated in real work. No old gates or reviewer rosters need to come back with these additions.
