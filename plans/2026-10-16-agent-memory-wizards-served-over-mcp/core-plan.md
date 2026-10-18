# Council of Wizards Plan

## **FEATURE INFO**
- **Project**: agent-memory-wizards
- **Date**: 2026-10-16
- **Agent**: meta
- **Feature**: Serve the wizard capability directly over MCP — judge whether the wizard set is cohesive, register it in `hermod-server`, expose all of it as MCP prompts and resources, and deploy so a client can use it with no local install.
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
| R1 | Cohesion verdict and repairs | The wizard set is judged cohesive, and anything incoherent is repaired in this release, so what gets served is one capability rather than eighteen loose procedures. Repairs stay inside this repo; a finding that lands in the core, the overlay or the fleet is written down and left. |
| R2 | Relationship map | A map of how the procedures, components and templates relate, derived from each component header's "Consumed by" line rather than hand-drawn, committed to this repo's `docs/`. |
| R3 | Served by `hermod-server` | `hermod-server` registers this repo as a second `ContentSource`, pinned as a submodule the way `agent-memory-project` is, and serves all 18 procedures as MCP Prompts and every template file as an MCP Resource, composing components at their reference point exactly as the compiler does. Every template reference becomes reachable for **download** rather than read-and-retyped, from `templates/` and `plan-templates/` alike. |
| R4 | Released on the MCP face | One deploy of the hosted hermod at the end of the batch, verified from a connected client with no local install. |

---

## **SCOPE GATE**
*Evaluate whether this feature truly needs multi-plan orchestration (council) or can be handled by a single `/high-wizard`.*

**Criteria** — council is needed when ANY of these are true:
- [x] The work holds **several deliverables, released together**, rather than one
- [ ] It requires **integration contracts** between parts (one plan produces what another consumes)
- [x] The scope is **too large for a single `/high-wizard`** to cover without losing detail

**Not needed when**: the work is one deliverable whose release finishes it (a single `/high-wizard`), or its parts must pass phases that gate each other (that is `/rite-of-creation`).

**Assessment**: Four deliverables across three repositories — this one, `hermod-server`, and `hermod-deploy` — released once at the end. There is no YAML-shaped contract between the parts: the interface that matters is this repo entering the server as a content source, and the served text composing the way the compiler composes it, which no schema can express. R1 gates everything downstream, so no single `/high-wizard` covers the work, and R4 is deliberately batched rather than run per deliverable.

**Decision**: [x] Proceed with Council | [ ] De-escalate to `/high-wizard`

*If de-escalating: delete this file, launch `/high-wizard` with the requirements already gathered above.*

---

## **CONFIRMED DECISIONS**
*These decisions were collected during decomposition investigation and confirmed by [USER-NAME]. The reasons serve as the analysis record for why the feature was decomposed this way.*

| # | Decision | Chosen | Reason |
|---|----------|--------|--------|
| 1 | When the deploy happens | One deploy at the end, after the other three are DONE | Batching is the point of this council, and one release means one verification rather than three |
| 2 | How this repo enters `hermod-server` | A second `ContentSource`, pinned as a submodule the way `agent-memory-project` is, serving all 18 procedures as Prompts and the templates as Resources | The shape the loader was written for, and a submodule pins the served text to a commit where a vendored copy would drift undetected |
| 3 | What a served copy does about its core dependency | Requires the core connection, as the framework already does | Preserves the property `hermod-server` exists to hold, that a served prompt and an installed command are the same instruction. MCP sits beside the per-harness installers, so the served set must equal the installed set |
| 4 | What the cohesion pass may change | Verdict, map, and the repairs in this release | Folds the "do not serve until cohesive" condition into SP-1's completion, so it is an ordinary dependency rather than a live conditional |
| 5 | Where the map lives | This repo's `docs/`, beside the ADRs | It describes this repo's own structure, so it is read by whoever changes the procedures |
| 6 | What a repair may reach | This repo only; a finding in the core, the overlay or the fleet is written down and left | Keeps the release bounded, and a defect in another repo is evidence about that repo rather than something to repair from here |
| 7 | Sub-plan grouping | Three, grouped by repository: SP-1 holds R1+R2, SP-2 holds R3, SP-3 holds R4 | The repository is where each deliverable is verified, and R1 and R2 come from one walk of the same 18 procedures |
| 8 | Where "served" ends and "released" begins | SP-2 is proven on a local server and is done when the served set matches the installed set; SP-3 is proven on `hermod.lok.quest` | Each plan is verified where it lives, and the hosted face is touched only at the release |
| 9 | Whether anything runs in parallel | Fully sequential; nothing enters `hermod-server` until SP-1 closes | Matches the constraint that the wizards do not move before the set is cohesive, and waiting keeps a half-installed source out of the server |
| 10 | Integration contracts | None. The layout is the interface, and served-equals-compiled is SP-2's acceptance criterion | The property is proven by comparing the served prompts to the compiled procedures, and no schema expresses a directory layout |
| 11 | Protocol per sub-plan | `/high-wizard` for all three | Each sub-plan is one coherent deliverable, and SP-3's production deploy would escalate out of `/quick-wizard` on its own rule |
| 12 | How a served client obtains a template | A download, not a read: every template file in `templates/` and `plan-templates/` is exposed for direct download, with the resolution rule stated in the server's own instructions | The template is a file to be copied, so re-typing it through the model risks the encoding and line-ending defects a byte copy avoids. MCP resources cannot be downloaded: they are registered `text/markdown` and return a string, so that exception does not apply |
| 13 | Who may fetch a template | A public route, like `/health` | The templates are already public in a public repo, and a token-gated route would not work in practice: the token lives with the MCP client, not with the agent making the shell call |

---

## **SUB-PLANS TABLE**
*Single canonical table — all other sections reference sub-plans by their ID. Do NOT duplicate this table elsewhere.*

| ID | Sub-Plan Name | Description | Requirements | Protocol | Plan File |
|----|--------------|-------------|--------------|----------|-----------|
| SP-1 | Cohesion pass | Judge whether the wizard set is cohesive, repair what it finds inside this repo, and commit the derived relationship map to `docs/`. | R1, R2 | HW | `SP-1-cohesion-pass.md` |
| SP-2 | Served by hermod-server | Register this repo in `hermod-server` as a second content source pinned as a submodule, serve all 18 procedures as Prompts and the templates as Resources, and prove on a local server that the served set matches the installed set. | R3 | HW | `SP-2-served-by-hermod-server.md` |
| SP-3 | Release | Deploy the hosted hermod once and verify from a connected client with no local install. | R4 | HW | `SP-3-release.md` |

**How to fill**: Each sub-plan groups related requirements into a coherent deliverable. Protocol column indicates `/high-wizard` (complex), `/pixel-wizard` (design-driven, with a visual reference to match), or `/quick-wizard` (simple). `Plan File` links to the sub-plan's file inside this folder once created. A `/quick-wizard` sub-plan keeps its plan in plan mode or in conversation rather than on disk, so its finished plan is written to that path once approved.

**Status lives in the Execution Log and nowhere else.** A status column here would be a second owner for one value, and it would go stale, because the procedure only ever advances a sub-plan in the log.

**Each sub-plan launch carries a handoff payload** — the decisions, contracts, and scope that bind it. See the Subplan Handoff component; a path alone is not a handoff.

---

## **INTEGRATION CONTRACTS**
*References to separate YAML contract files that define the interfaces between sub-plans. Use industry-standard formats (OpenAPI, AsyncAPI, JSON Schema).*

**None — no contract file.** The interface between SP-1 and SP-2 is this repo's own layout (`procedures/`, `components/`, `templates/` and the component-link syntax), which `hermod-server` already consumes for `agent-memory-project`. The one property worth checking, that a served prompt equals the compiled procedure, is SP-2's acceptance criterion rather than a schema.

**How to fill**: Identify what data/interfaces flow between sub-plans. Create a YAML contract file for each integration point using the appropriate industry standard. File paths are relative to this plan's folder. The "Verified" column is checked during Feature Completion when both sides of the contract are confirmed working.

*If no integration contracts are needed (sub-plans are independent), write "None — sub-plans have no integration dependencies" and remove the table.*

---

## **DEPENDENCY GRAPH**
*Mermaid diagram showing sub-plan relationships. Identifies what can run in parallel and what must be sequential.*

```mermaid
graph LR
    SP-1[SP-1: Cohesion pass] --> SP-2[SP-2: Served by hermod-server]
    SP-2 --> SP-3[SP-3: Release]
```

**Parallel opportunities**: None. The gate chains SP-1 into SP-2 and the single release chains SP-2 into SP-3, so the three run strictly in order and no two can overlap.

**Critical path**: SP-1 → SP-2 → SP-3, which is all three sub-plans.

**How to fill**: Draw dependencies based on which sub-plans produce outputs that others consume (linked to Integration Contracts). Sub-plans with no dependency between them can run in parallel — highlight these opportunities. The critical path is the longest chain of sequential dependencies.

---

## **EXECUTION LOG**
*Track progress of each sub-plan. This is the single source of truth for master-level progress **and for every sub-plan's status** — the Sub-Plans Table deliberately carries no status column. Each sub-plan's own plan file has its own detailed execution log.*

**Execution Protocol for AI**:
I have to use this document as my **ONLY** source of truth to track which sub-plans are done and which are next. For each sub-plan, I launch `/high-wizard`, `/pixel-wizard` or `/quick-wizard` as specified in the Sub-Plans Table, then update this log. Sub-plans can be executed in parallel if the dependency graph allows.

| Sub-Plan | Status | Started | Completed | Agent/Session | Notes |
|----------|--------|---------|-----------|---------------|-------|
| SP-1 | DONE | 2026-10-17 | 2026-10-18 | meta | Plan file: `SP-1-cohesion-pass.md`, kept in this folder rather than moved to `plans/completed/` — see the note below. Verdict: cohesive. 7 findings repaired, 4 quality lows fixed |
| SP-2 | DONE | 2026-10-18 | 2026-10-18 | meta | Plan file: `SP-2-served-by-hermod-server.md`, kept in this folder for the same reason as SP-1's. 26 prompts, 10 resources, 18/18 byte-equal, 10/10 byte-exact. Two loader defects only a second source could expose, found by the proof and fixed |
| SP-3 | NOT STARTED | — | — | — | — |

**Status values**: NOT STARTED → IN PROGRESS → DONE → BLOCKED (with reason in Notes)

**Note on SP-1's plan file.** `/high-wizard`'s Step 18 archives its plan to `plans/completed/`. Doing that here would take the file out of this council folder while the council is still running, and the Sub-Plans Table's `Plan File` link would break before anyone could follow it. A sub-plan's archive therefore belongs to this council's own Step 19, which files the whole folder at once. Neither procedure says so, so it is recorded here as a gap for the next pass over `/council-of-wizards`.

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
