+++
format_version = 2
id = "quick-wizard"
kind = "procedure"
title = "Quick Wizard Protocol"
description = "Execute lightweight smart planning with decision collection and approval before execution — the same decision discipline as High Wizard, using the inline plan template below."
argument_name = "argument"
argument_description = "Input text in the format described by this procedure's Arguments section"
+++
# Quick Wizard Protocol

Execute lightweight smart planning with decision collection and approval before execution — the same decision discipline as High Wizard, using the inline plan template below. Keep the plan in IDE plan mode or conversation by default, or explicitly save the specification and compact execution log in one file. The scope gate escalates complex work to /high-wizard; saving a small plan does not make it complex.

## Arguments

`$ARGUMENTS`

- `/quick-wizard [context]` → Create Quick Wizard plan for the given context
- `/quick-wizard --save [context]` → Save the finished plan before approval and track execution in that file
- `/quick-wizard` → Will ask for context

Interpret a standalone `--save` option separately from the task context; do not treat quoted task text mentioning the flag as a request to save. If context is absent after interpreting the option, ask: "What feature or task should I create a Quick Wizard plan for?"

A **caller-supplied plan-file path** also requests saved mode, without requiring `--save`. If QW belongs to a parent or larger plan, follow that plan's saved-file location, regardless of which planning protocol launched it. Read the parent's plan or handoff to find the assigned location; if it is missing or ambiguous, ask rather than inventing a second location. Use that destination instead of the default `./plans/[YYYY-MM-DD]-[project]-[theme].md`; resolve relative destinations from the working project and honor absolute destinations. Keep the caller's inherited scope, decisions and contracts — a path is not a handoff.

Without `--save` or a caller-supplied destination, retain the existing unsaved flow: no plan file or execution log is required.

---

## Procedure

This is a **Level 0** wizard protocol: it owns the **change**, one small change below the deliverable. It is a leaf — it never orchestrates sub-plans — and it may itself be launched as a phase by `/rite-of-creation` or a sub-plan by `/council-of-wizards`. It is never a milestone, because it sits below the release boundary.

Level 0 is the concrete change, so that is what you collect decisions about — Step 3 presents the rounds `planning-rounds.md` declares, each under the condition it runs; at this size most will not run at all. Implementation nouns — entrypoints, core logic, execution touchpoints — are the right vocabulary to disclose in, because they are what this altitude is made of. (`/wait-options-coding` governs *how* you present a decision, never *which* decisions are yours — Step 3 is where that is decided.) Nothing gets pushed down; a decision that feels too large to settle here is not something to hand off, it is the scope gate in Step 2 telling you to escalate to `/high-wizard`.

*IMPORTANT: This procedure structurally enforces UUID f3a8b2c1 (VERIFY FIRST) - the agent MUST collect and confirm decisions BEFORE executing. Jumping directly into implementation is prohibited.*

### Step 1: Investigate and Collect Decisions

**First, if anything was settled before you started** — whether launched as a sub-plan or handed a design already agreed in conversation: read and follow the Inherited Context component. It tells you what you inherited, what you may not reopen, and where to find it when no payload was passed. Record it before investigating anything.

@start component id="quick-wizard.subplan-handoff-read" ref="procedures/components/subplan-handoff-read.md"
@end component

Then read and follow the Planning Investigation component — it runs the shared investigation checklist and produces the findings this plan's decisions are built from.

@start component id="quick-wizard.planning-investigation" ref="procedures/components/planning-investigation.md"
@end component

### Step 2: Scope Gate Assessment

After investigation, assess whether the task is a small Quick Wizard change or needs High Wizard's more detailed planning. Saved mode alone is not a reason to escalate.

**Escalate to /high-wizard when ANY of these apply:**
- Task likely spans multiple sessions or risks context compaction
- Multiple files with complex interdependencies need modification
- Task requires production deployment with audit trail
- Implementation has irreversible consequences requiring careful tracking
- You feel uncertain about completing within the current session
- Task involves bug investigation requiring hypothesis-driven debugging (high-wizard section E)
- Task requires evaluating multiple solution approaches with formal comparison (high-wizard section F)
- Task produces an architecture decision record (high-wizard sections F+G)

**If escalating**: Tell [USER-NAME] "This task is complex enough to benefit from /high-wizard — escalating with the decisions I've already collected." Then execute /high-wizard starting from Step 7 (decisions already collected). STOP HERE — do not continue with Quick Wizard steps.

**If suitable for Quick Wizard**: Continue to Step 3.

### Step 3: Present Decisions — One Round per Category

Decisions are not presented in one block. Each category the planning rounds declare gets its own round, in their declared order, and every round is a gate: present, STOP, and wait for [USER-NAME] to clear it before building the next. The Planning Decision component governs what earns a place in a round and how a round is run — read and follow it before building the first round.

@start component id="quick-wizard.planning-decision" ref="procedures/components/planning-decision.md"
@end component

Present the planning rounds.

@start component id="quick-wizard.planning-rounds" ref="procedures/components/planning-rounds.md"
@end component

Do NOT proceed until every round that ran is confirmed.

### Step 4: Create Execution Plan

In **unsaved mode**, enter plan mode if available; otherwise present the plan in conversation. In **saved mode**, write the plan file at the resolved destination using the same inline template. Create the destination directory if needed, but never overwrite an unrelated existing plan: load an existing destination first, resume only when it clearly belongs to this work, and STOP to ask if ownership or intent is unclear.

Write the execution plan using the [Quick Wizard Plan Content Template](#quick-wizard-plan-content-template) structure:
- Objective (1-2 sentences)
- Confirmed decisions table
- Numbered execution steps with clear actions

For saved mode, also include the template's saved-only Plan State, Specification and Execution Log sections. The specification states required behavior, constraints and exclusions; keep it proportionate to the small change. Start approval as **PENDING**. Prepare a log entry per execution step, without marking any work done.

Write the complete saved plan **before presenting it for approval**. A saved file is a draft, not authorization to execute.

As you write the steps, mark any step that will cross a **real dependency the unit test would have to double** — a database, an HTTP service, a queue, the filesystem. One word is enough: `(crosses: DB)`. Most Quick Wizard changes cross nothing; that is the expected answer, and noticing it costs a glance rather than a decision.

### Step 5: Get Approval

Present the finished plan for [USER-NAME]'s approval, linking the file in saved mode. STOP. Do NOT execute until [USER-NAME] confirms. In saved mode, record **APPROVED** and the actual confirmation only after it arrives; if approval is absent or unclear, keep it **PENDING**. A substantive plan revision that invalidates approval returns here for confirmation.

**If any step was marked as crossing a boundary**, settle its coverage in the same breath as approval — call `/qa-status` and read its bench and stack lines.

- **Bench built and stack up** → those steps get an `/integration-test` run during Step 6.
- **Either missing** → say which check failed, and confirm that continuing means this change ships with no integration coverage.

Record the answer in the plan's `## QA Handoff` section under `Integration coverage`.

**If no step crosses a boundary, skip this entirely and say nothing.** A gate that fires on every trivial change is one people learn to wave through, and at this altitude most changes cross nothing.

### Step 6: Execute

Execute the steps from the plan in order. In unsaved mode, briefly report each step before moving on. In saved mode, follow the plan's **Execution Protocol for AI**: load the full plan at the start and after context compaction, inspect its approval and log, read the next step, implement it, verify it, then update that step's inline log before continuing. The saved plan is the only execution tracker, because a separate summary of the steps loses the detail they carry.

When resuming a saved plan, inspect the source protocol, approval record and unfinished steps first. An existing file or completed earlier step never bypasses a pending approval or another STOP gate. Preserve recorded results; do not repeat completed work without a reason. Mark a step complete only when its success criteria are met, and record blockers, failed or missing verification, and agreed deferrals honestly.

Each step closes on its own tests: unit tests wherever the step has testable logic, and — where Step 5's gate came back ready and the step was marked as crossing a boundary — an `/integration-test [boundary]` run, which builds the fixtures, writes the test, and runs it.

**CRITICAL**: If any NEW decision is discovered during execution that was not covered in Step 3, STOP immediately. Present the new decision to [USER-NAME] with the same format (options + confidence + reason) before continuing. Do NOT execute ahead on assumptions.

### Step 7: Quality Review (Delegated to `/analyze-code-quality`)

After all steps are executed, run **static** code quality review by delegating to `/analyze-code-quality` in embedded mode. Findings are embedded directly into the plan's Quality Review section (created at Step 4 from the Quick Wizard Plan Content Template) — the plan IS the audit trail.

1. **Collect scope**: Identify all files created or modified during execution (from the saved plan's Execution Log, or plan-mode/in-conversation tracking in unsaved mode). This file list is the **caller-passed scope** for the delegated procedure.

2. **Invoke `/analyze-code-quality`** following the /analyze-code-quality with these inputs:
   - `scope`: the file list collected above
   - `embedded_mode=true`: signals the procedure to skip standalone working-doc creation; findings get embedded into the QW plan's Quality Review section

The delegated procedure will:
- Run **Scope Reconciliation** (its Step 3) — surface any git-diff vs tracked-scope discrepancies for [USER-NAME] to reconcile
- **Discover quality standard** (its Step 4) — looks for `**/quality-standard.md`; if found, applies Dimension 8; if not, freeform
- Walk quality dimensions against the reconciled scope (its Steps 5-6)
- Present findings via /wait-options-coding (its Step 7) — preamble: *"Code quality review for implementation:"*
- **STOP** at the WAIT Options prompt — wait for [USER-NAME]'s response
- Apply approved fixes and update the QW plan's Quality Review section (its Step 8)

3. **Resume control** here after `/analyze-code-quality` completes. Proceed to Step 8 (Build QA Checklist).

### Step 8: Build QA Checklist (Delegated to `/generate-qa-checklist`)

After Quality Review is resolved, hand this plan off to QA by building its verification checklist. Static quality review (Step 7) answered *"is the code clean?"*; this step produces the artifact that will answer *"is it actually right?"* — **later, by a human, with the stack up.**

> **This step does not verify anything, and must never claim to.** A wizard sweep is a coding session: the QA stack is almost certainly down, so running the R/I/A/O loop here would mean a cold start plus a full seed restore on every sweep. Runtime verification belongs to a dedicated QA session (`/run-qa-test`). What this step guarantees is that the sweep never ends without a written plan for that verification.

1. **Collect scope**: Identify all files created or modified during execution (from the saved plan's Execution Log, or plan-mode/in-conversation tracking in unsaved mode). That list, plus this plan itself, is the **caller-passed scope**.

2. **Invoke `/generate-qa-checklist`** with this plan as the scope input.

The delegated procedure will:
- **Check the QA instrument is set up** — a `qa/qa-map.md` from `/map-qa-instrument`, and a built bench from `/build-qa-bench`. If either is absent it **notifies loudly and auto-skips** rather than inventing a `qa/` folder this project never opted into.
- Read the plan for **scope**, then derive **risk independently** — invariants to disprove, regression surface, boundaries, cross-module effects. The plan is input, never authority.
- Write `qa/checklists/{feature}.md`, marking each item automated vs manual

3. **Record the outcome in the plan's `## QA HANDOFF` section** — the checklist path, or the skip and its reason. Never leave it blank.

4. **Resume control** here after the delegated procedure completes. Proceed to Step 9 (Report Completion).

### Step 9: Report Completion

After all steps are executed and both Quality Review (Step 7) + QA Handoff (Step 8) are resolved, present a brief completion summary to [USER-NAME]:
- What was done
- Quality Review status (clean / N findings fixed)
- **QA Handoff**: `qa/checklists/{feature}.md` built, or skipped + reason
- **Integration coverage**: in scope and run, N/A because nothing crossed a boundary, or none + which check failed
- ⚠️ **State plainly: "Not runtime-verified."** Then the exact next action — *"run `/run-qa-test --checklist qa/checklists/{feature}.md` when the stack is up"*, or the instrument-setup commands if the step auto-skipped.
- Any issues encountered
- Any tech debts or follow-up items

In saved mode, update Quality Review and QA Handoff in the **same plan file**, and link that file in the completion report. If this is part of a larger plan, use its assigned saved-file location, not a second copy. Completion does not authorize archiving.

---

## Templates

### Quick Wizard Plan Content Template

Use this structure in either mode. Include the marked saved-only sections **only in saved mode**; omit them from an unsaved plan. This inline template remains the source — do not create a separate template or log file.

```markdown
# Quick Wizard Plan: [Theme]

<!-- Saved mode only: include this section in the saved plan. -->
## Plan State
- **Source Protocol**: `/quick-wizard`
- **Approval**: PENDING
- **Confirmation**: [Record the user's actual confirmation only after approval]

To resume: load the source protocol and this entire plan, inspect approval and the Execution Log, and continue with the next unfinished step only when its gates are cleared.

## Inherited Context
*Filled at investigation step 0 with whatever was settled before this plan existed — recorded separately by source, never merged. Write "None" under a part that does not apply.*
*Not yours to reopen. If an inherited decision looks wrong, STOP and surface it — do not silently re-decide it below.*

**From the parent plan**
- **Parent plan**: [path, or "None — not a sub-plan"]
- **Assigned scope**: [what this plan owns]
- **Inherited decisions**: [decision → chosen → parent's reason; mark each Settled or My call]
- **Contracts / pushed-down items**: [paths + produce/consume, and decisions left to this plan — or "None"]

**From pre-planning discussion**
- **Discussion**: ["Pre-planning discussion, YYYY-MM-DD", or "None"]
- **Agreed scope**: [what the discussion established]
- **Settled decisions**: [decision → chosen → his reason; mark each Settled or My call]
- **Considered and rejected**: [option → why it lost — or "None"]

## Objective
[1-2 sentence description of what we're doing and why]

<!-- Saved mode only: include this section in the saved plan. -->
## Specification
- **Required behavior**: [What this change must do]
- **Constraints**: [Rules and compatibility it must preserve]
- **Out of scope**: [What this change does not include]

## Confirmed Decisions
*Decisions made **by this plan** — both asked-and-confirmed by [USER-NAME] AND written-through (Zone A and B decisions, recorded with their reasoning). Inherited decisions belong above, not here.*

| # | Decision | Chosen | Reason |
|---|----------|--------|--------|
| 1 | [Topic] | [Choice] | [Why] |

## Success Criteria
- [ ] [How we know it's done]
- [ ] Unit tests written and passing for every step with testable logic (or the step says why it has none)
- [ ] Static quality review completed (Step 7 — delegated to `/analyze-code-quality`)
- [ ] QA Handoff completed (Step 8 — checklist built, or auto-skipped with reason recorded)

## Execution Steps
1. **[Step name]**: [What to do] → [How to verify]
2. **[Step name]**: [What to do] → [How to verify]
3. **[Step name]**: [What to do] → [How to verify]

<!-- Saved mode only: include this section in the saved plan. -->
## Execution Log
**Execution Protocol for AI**: Load this entire plan at the start and after compaction. Check approval and pending STOP gates, then read the next unfinished execution step. Implement in order, verify its success criteria, and update its entry below before moving on. This file is the only execution tracker; a second log or a summary of the steps loses the detail they carry. Record actual results, not intentions.

- [ ] **Step [N]: [Name]**
  - **Implementation**: [What changed, including files; not started initially]
  - **Verification / result**: [Checks and actual results; not run initially]
  - **Blockers / agreed deferrals**: [Unresolved blockers or explicitly agreed deferrals; none initially]

Repeat one entry per execution step. Keep failed or unverified work unfinished. File existence and earlier completed steps do not establish approval.

## Quality Review
*Filled by Step 7 (delegated to `/analyze-code-quality` in embedded mode). **Static** review — answers "is the code clean?".*

- **Scope**: [Files reviewed — reconciled against `git status --short`, which also sees a newly created file]
- **Quality Standard**: [found / not found — dimensions applied]
- **Findings**: [Issues found, or "No findings — implementation meets quality dimensions"]
- **Fixed**: [What was fixed from approved findings, or "N/A"]

## QA Handoff
*Filled by Step 8 after Quality Review is resolved. This plan is **not** runtime-verified — this section records the plan for that verification, which happens in a QA session with the stack up.*

- **Scope**: [Modules touched]
- **QA instrument**: [Set up (map + bench) / NOT SET UP — auto-skipped]
- **Integration coverage**: [N/A — no step crosses a real boundary | in scope — steps N, M | NONE — [which check failed], confirmed before execution]
- **Checklist**: [`qa/checklists/{feature}.md`, or "none — skipped, reason"]
- **Coverage split**: [N automated (named tests) / N manual — of which N are UI-bound]
- **Runtime verification**: **NOT DONE.** Next action: [`/run-qa-test --checklist qa/checklists/{feature}.md` once the stack is up | set up the instrument first: `/map-qa-instrument create` → `/build-qa-bench`]
```

---
