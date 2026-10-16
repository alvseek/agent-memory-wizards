# Council of Wizards Plan

## **FEATURE INFO**
- **Project**: [Project Name]
- **Date**: [YYYY-MM-DD]
- **Agent**: [Agent Name]
- **Feature**: [Brief description of the feature being delivered]
- **Source Protocol**: `/council-of-wizards` — /council-of-wizards

*CRITICAL INSTRUCTION: To continue this plan: load the source protocol above, then inspect which sections below are filled vs unfilled to infer your current step.*

---

## **INHERITED CONTEXT**
*Filled at investigation step 0 with whatever was settled before this plan existed. The two sources are recorded separately and never merged — write "None" under a part that does not apply.*
*These decisions are **not yours to reopen**. If one looks wrong, STOP and surface it to [USER-NAME] — do not silently re-decide it here or in Confirmed Decisions below.*

### From the Parent Plan
- **Parent plan**: [path to the parent `core-plan.md` in the rite or covenant folder, or "None — not a sub-plan"]
- **Assigned scope**: [the milestone or phase this council owns, and what it must deliver]

| # | Inherited decision | Chosen | Parent's reason | Status |
|---|--------------------|--------|-----------------|--------|
| 1 | [Decision topic] | [Chosen option] | [Reason, verbatim from the parent] | Settled / My call |

- **Integration contracts**: [`contracts/*.yaml` paths this council must honor, and whether it produces or consumes each — or "None"]
- **Pushed-down open items**: [decisions the parent deliberately left to this council — or "None"]

### From Pre-Planning Discussion
- **Discussion**: ["Pre-planning discussion with [USER-NAME], YYYY-MM-DD", or "None — no pre-planning discussion"]
- **Agreed scope**: [what the discussion established this work covers]

| # | Settled decision | Chosen | His reason | Status |
|---|------------------|--------|------------|--------|
| 1 | [Decision topic] | [Chosen option] | [Reason, verbatim from the discussion] | Settled / My call |

- **Considered and rejected**: [option → why it lost — or "None"]
- **Left open**: [decisions the discussion deliberately did not make — or "None"]

---

## **REQUIREMENTS BREAKDOWN**
*Filled AFTER [USER-NAME] confirms the WAIT Options (Step 6). This table is the formal record of confirmed requirements that informs the scope gate and sub-plan decomposition.*

| # | Requirement | Description |
|---|-------------|-------------|
| R1 | [Requirement name] | [What needs to be built/changed] |
| R2 | [Requirement name] | [What needs to be built/changed] |
| R3 | [Requirement name] | [What needs to be built/changed] |

---

## **SCOPE GATE**
*Evaluate whether this feature truly needs multi-plan orchestration (council) or can be handled by a single `/high-wizard`.*

**Criteria** — council is needed when ANY of these are true:
- [ ] Feature has **independently shippable sub-deliverables** that build on each other
- [ ] Feature requires **integration contracts** between parts (one plan produces what another consumes)
- [ ] Scope is **too large for a single `/high-wizard`** to cover without losing detail

**Assessment**: [Explain why this feature meets/doesn't meet the criteria above]

**Decision**: [ ] Proceed with Council | [ ] De-escalate to `/high-wizard`

*If de-escalating: delete this file, launch `/high-wizard` with the requirements already gathered above.*

---

## **CONFIRMED DECISIONS**
*These decisions were collected during decomposition investigation and confirmed by [USER-NAME]. The reasons serve as the analysis record for why the feature was decomposed this way.*

| # | Decision | Chosen | Reason |
|---|----------|--------|--------|
| 1 | [Decision topic] | [Chosen option] | [Evidence-based reason] |
| 2 | [Decision topic] | [Chosen option] | [Evidence-based reason] |

---

## **SUB-PLANS TABLE**
*Single canonical table — all other sections reference sub-plans by their ID. Do NOT duplicate this table elsewhere.*

| ID | Sub-Plan Name | Description | Requirements | Protocol | Plan File |
|----|--------------|-------------|--------------|----------|-----------|
| SP-1 | [Name] | [What this sub-plan delivers] | R1, R2 | HW / PW / QW | `SP-1-[name].md` |
| SP-2 | [Name] | [What this sub-plan delivers] | R3 | HW / PW / QW | `SP-2-[name].md` |
| SP-3 | [Name] | [What this sub-plan delivers] | R4, R5 | HW / PW / QW | `SP-3-[name].md` |

**How to fill**: Each sub-plan groups related requirements into a coherent deliverable. Protocol column indicates `/high-wizard` (complex), `/pixel-wizard` (design-driven, with a visual reference to match), or `/quick-wizard` (simple). `Plan File` links to the sub-plan's file inside this folder once created. A `/quick-wizard` sub-plan keeps its plan in plan mode or in conversation rather than on disk, so its finished plan is written to that path once approved.

**Status lives in the Execution Log and nowhere else.** A status column here would be a second owner for one value, and it would go stale, because the procedure only ever advances a sub-plan in the log.

**Each sub-plan launch carries a handoff payload** — the decisions, contracts, and scope that bind it. See the Subplan Handoff component; a path alone is not a handoff.

---

## **INTEGRATION CONTRACTS**
*References to separate YAML contract files that define the interfaces between sub-plans. Use industry-standard formats (OpenAPI, AsyncAPI, JSON Schema).*

| Contract ID | Between | Format | File Path | Verified |
|------------|---------|--------|-----------|----------|
| C-1 | SP-1 ↔ SP-2 | [OpenAPI / AsyncAPI / JSON Schema / other] | `contracts/[contract-name].yaml` | [ ] |
| C-2 | SP-2 ↔ SP-3 | [OpenAPI / AsyncAPI / JSON Schema / other] | `contracts/[contract-name].yaml` | [ ] |

**How to fill**: Identify what data/interfaces flow between sub-plans. Create a YAML contract file for each integration point using the appropriate industry standard. File paths are relative to this plan's folder. The "Verified" column is checked during Feature Completion when both sides of the contract are confirmed working.

*If no integration contracts are needed (sub-plans are independent), write "None — sub-plans have no integration dependencies" and remove the table.*

---

## **DEPENDENCY GRAPH**
*Mermaid diagram showing sub-plan relationships. Identifies what can run in parallel and what must be sequential.*

```mermaid
graph LR
    SP-1[SP-1: Name] --> SP-2[SP-2: Name]
    SP-1 --> SP-3[SP-3: Name]
    SP-2 --> SP-4[SP-4: Name]
    SP-3 --> SP-4
```

**Parallel opportunities**: [List which sub-plans can run concurrently, e.g., "SP-2 and SP-3 can run in parallel after SP-1 completes"]

**Critical path**: [Identify the longest sequential chain that determines minimum total time]

**How to fill**: Draw dependencies based on which sub-plans produce outputs that others consume (linked to Integration Contracts). Sub-plans with no dependency between them can run in parallel — highlight these opportunities. The critical path is the longest chain of sequential dependencies.

---

## **EXECUTION LOG**
*Track progress of each sub-plan. This is the single source of truth for master-level progress **and for every sub-plan's status** — the Sub-Plans Table deliberately carries no status column. Each sub-plan's own plan file has its own detailed execution log.*

**Execution Protocol for AI**:
I have to use this document as my **ONLY** source of truth to track which sub-plans are done and which are next. For each sub-plan, I launch `/high-wizard`, `/pixel-wizard` or `/quick-wizard` as specified in the Sub-Plans Table, then update this log. Sub-plans can be executed in parallel if the dependency graph allows.

| Sub-Plan | Status | Started | Completed | Agent/Session | Notes |
|----------|--------|---------|-----------|---------------|-------|
| SP-1 | NOT STARTED | — | — | — | — |
| SP-2 | NOT STARTED | — | — | — | — |
| SP-3 | NOT STARTED | — | — | — | — |

**Status values**: NOT STARTED → IN PROGRESS → DONE → BLOCKED (with reason in Notes)

---

## **QA HANDOFF**
*Filled at Step 18. This council is **not** runtime-verified — this section records the plan for that verification, which happens in a QA session with the stack up. Each sub-plan owns the checklist for its own change; this section owns the batch, which no sub-plan can see.*

- **Sub-plan checklists**: [`qa/checklists/{feature}.md` for each sub-plan that produced one, with the skip and its reason for each that did not]
- **Cross-plan integration**: [exercised — what ran it (an `/integration-test` run, or a named test) | NOT covered — why]
- **Runtime verification**: **NOT DONE.** Next action: [run each sub-plan's checklist with the stack up — `/run-qa-test --checklist <path>` per checklist]
- **Release**: [the sub-plans this batch releases together — one deployment for the batch, not one per sub-plan]

---

## **FEATURE COMPLETION CHECKLIST**
*Final verification before marking the feature complete.*

- [ ] All sub-plans have status DONE in Execution Log
- [ ] All integration contracts verified (Verified column checked)
- [ ] Cross-plan integration settled, and the `## QA HANDOFF` section filled: the sub-plan checklists listed, and the batch marked **not runtime-verified** with its next action
- [ ] No BLOCKED sub-plans remaining
- [ ] Documentation updated (if applicable)
- [ ] The sub-plans that shipped together are released **once** — batch them into a single deployment rather than deploying per sub-plan
- [ ] [USER-NAME] confirms feature is complete

---

## **POST-COMPLETION**
After feature is complete and checklist passes, move the entire council folder to `plans/completed/`:
`mkdir -p ./plans/completed && mv ./plans/[this-folder] ./plans/completed/[this-folder]`
