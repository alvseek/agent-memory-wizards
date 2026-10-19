# High Wizard Plan

## **PROJECT INFO**
- **Project**: hermod-deploy
- **Date**: 2026-10-19
- **Agent**: meta
- **Theme**: Release — deploy the built image once, and verify the served face from a connected client with no local install
- **Source Protocol**: `/high-wizard` — /high-wizard

*CRITICAL INSTRUCTION: To continue this plan: load the source protocol above, then inspect which sections below are filled vs unfilled to infer your current step.*

---

## **INHERITED CONTEXT**
*Filled at investigation step 0 with whatever was settled before this plan existed. The two sources are recorded separately and never merged — write "None" under a part that does not apply.*
*These decisions are **not yours to reopen**. If one looks wrong, STOP and surface it to [USER-NAME] — do not silently re-decide it here or in Confirmed Decisions below.*

### From the Parent Plan
- **Parent plan**: [`core-plan.md`](core-plan.md), the council that owns this work
- **Assigned scope**: **R4**. Deploy the hosted hermod once and verify from a connected client with no local install. R1, R2 and R3 belong to SP-1 and SP-2, both DONE.

| # | Inherited decision | Chosen | Parent's reason | Status |
|---|--------------------|--------|-----------------|--------|
| 1 | When the deploy happens | One deploy at the end, after the other three are DONE | Batching is the point of this council, and one release means one verification rather than three | Settled |
| 8 | Where "served" ends and "released" begins | This plan is proven on `hermod.lok.quest`, where SP-2 was proven on a local server | Each plan is verified where it lives, and the hosted face is touched only at the release | Settled |
| 9 | Whether anything runs in parallel | Fully sequential; this plan starts only once SP-1 and SP-2 close | Matches the constraint that the wizards do not move before the set is cohesive, and waiting keeps a half-installed source out of the server | Settled, and satisfied: both are DONE |
| 11 | Protocol per sub-plan | `/high-wizard` for this one too | Each sub-plan is one coherent deliverable, and a production deploy would escalate out of `/quick-wizard` on its own rule | Settled |

- **Integration contracts**: None. The interface the release depends on is this repo's own deploy config reaching a registry tag, which no schema expresses.
- **Pushed-down open items**: the release's own mechanics, which are this plan's to settle: which tag, what the deploy config must say, what verification is read from a client, and what the way back is.

### From Pre-Planning Discussion
- **Discussion**: the design conversation that produced this council, 2026-10-16. Source: `SP-1-cohesion-pass.md`'s inherited-context section, which recorded it first.
- **Agreed scope**: MCP sits **beside** the per-harness installers rather than replacing them, so the served set must equal the installed set. That is the property this release makes live without a local install.

| # | Settled decision | Chosen | His reason | Status |
|---|------------------|--------|------------|--------|
| 1 | Where a deploy happens | A governed release sits outside every leaf wizard: staging may deploy inside one, production is a later act | *"deployment to staging / dev is done inside HW / QW. deployment to production is outside"* | Settled, and the reason this plan exists rather than a deploy step inside SP-2 |

- **Considered and rejected**: wiring the deploy to fire automatically after a build → still rejected; the workflow is manual on purpose, "once the button has been pressed enough times to trust".
- **Left open**: nothing this plan needs.

---

## **OBJECTIVES**
Deploy the already-built image tag `3f898bd` to `hermod.lok.quest` once, with the deploy config naming both content roots, and verify the served face from a connected client that has nothing installed: 26 prompts (the overlay's 8 plus the wizards' 18), the wizard templates downloadable byte-exact, and the health route green.

### **Related Documents**
- [core-plan.md](core-plan.md) - the council that owns this work, and the source of the inherited decisions above
- [SP-2-served-by-hermod-server.md](SP-2-served-by-hermod-server.md) - the deliverable this release makes live, proven on loopback
- [config/deploy.yml](../../../../config/deploy.yml) - the Kamal config this plan corrects, in the private deploy repo
- [.github/workflows/deploy.yml](../../../../.github/workflows/deploy.yml) - the manual dispatch that runs the deploy, the setup and the rollback
- [Dockerfile](../../Dockerfile) - where the two content roots are already set for the image

### **SUCCESS CRITERIA**
- [x] `config/deploy.yml` names both content roots, and the deploy workflow has run for tag `3f898bd`
- [x] From a connected client with no local install: the served prompt list is 26 and the resource list is 10
- [x] A wizard template downloads byte-exact from the public route, and an overlay template still does
- [x] `/health` answers 200 on the new container
- [x] The rollback target is named before the deploy runs, and the path back is reachable

---

## **SCOPE**

### In Scope
- `hermod-deploy/config/deploy.yml`: the content key, corrected to name both checkouts
- `hermod-deploy/deploy/README.md`: the one sentence the release makes false, since `/health` is no longer the only public route
- The one deploy dispatch for tag `3f898bd`, and its verification from this session's own MCP connection
- The rollback path, named and reachable before the deploy runs

### Out of Scope
- Any change in `hermod-server` or in the wizards repo. SP-1 and SP-2 own those, and the wizards' docs-only commit stays undeployed by the decision below
- The store's contents, and importing the markdown project memory. That is a separate runbook already run against this box
- A second environment. There is one host, and one deploy means one verification

---

## **CONFIRMED DECISIONS**
*Decisions made **by this plan** — both **asked-and-confirmed** by [USER-NAME] AND **written-through** (Zone A and B decisions made by the agent, recorded with their reasoning). The reasons serve as the analysis record.*
*Decisions settled before this plan existed — by a parent, or in a pre-planning discussion — belong in [INHERITED CONTEXT](#inherited-context) above, not here. Keeping them separate is what shows which decisions this plan actually owns.*

| # | Decision | Chosen | Reason |
|---|----------|--------|--------|
| 1 | What deploys | The tag CI already built and published, `3f898bd`, with the deploy config corrected in the same release | The artifact exists and nothing points at it; rebuilding for a config fix would be waste, and the config fix is what makes the served set intentional |
| 2 | Which content key the deploy names | The plural, listing both checkouts | With the singular key in place, the image's own plural would be what decides whether the second source serves, and `config.py` prefers the plural. A deployment's served set should not rest on which ENV an image happens to carry, and the fix is the same whichever behaviour Kamal has |
| 3 | What counts as verification | A connected client with no local install: the served prompt and resource lists, one byte-exact wizard template download, and `/health` | R4 asks for what a client gets. This session's own MCP connection is such a client, and the byte comparison is the only check that reads content rather than a count |
| 4 | What a failed deploy falls back to | `kamal rollback 32ff7c6` through the same workflow, before anything else is tried | Tags are immutable, which is the whole reason rollback exists; the 10-15 tag is the last one known good, and the way back is named before the deploy runs |
| 5 | The wizards submodule pin | Left at `3cff4e2` for this deploy | The newer commit is docs-only (the council's own plan records), so bumping it would cost a build and a new tag for no client-visible change |
| 6 | Where a defect found by this release gets fixed | In the repo that owns it, never in the deploy repo | The deploy repo holds no code, so a patch there would be a second home for something already owned |

---

## **SOLUTION**

### Architecture Overview
The release moves one immutable artifact onto the one host and then reads the result from outside. The artifact is the image tag `3f898bd`, built and published by the product repo's CI on 2026-10-18 and already pinned by this repo's submodule pointer. Nothing is built during the release: Kamal pulls the tag, starts a new container beside the running one, and kamal-proxy cuts over once `/health` answers. The one change this plan makes is the deploy config's content key, which has to name both checkouts so that what gets served is the deployment's intent rather than an accident of which ENV the image happens to carry.

### Component 1: The deploy config
- **Purpose**: state the deployment's truth: which image, which host, which content roots, which secrets
- **Key Files**: `config/deploy.yml`

### Component 2: The dispatch
- **Purpose**: run the release with the repo's SSH key and the store DSN, and keep the way back reachable
- **Key Files**: `.github/workflows/deploy.yml`

### Component 3: The verification
- **Purpose**: read what a client with nothing installed actually gets
- **Key Files**: none. The checks are calls made from this session, not files

### Integration Architecture

| Component | Integrates With | Data Flow | What the verification proves |
|-----------|----------------|-----------|------------------------------|
| CI build (`hermod-server`) | the registry | commit -> immutable image tag | that the tag exists; nothing about how it serves |
| `config/deploy.yml` | the host, through Kamal | tag + env + secrets -> a started container | that the container starts with the roots the config names |
| kamal-proxy | the container and the public host | TLS request -> container port 8210 | that `/health` answers 200 and the host is reachable |
| the store database | `HERMOD_DB_URL` | DSN -> Postgres on the shared `kamal` network | **NOT proven here.** The content face serves without a tenant, and SP-2 proved the store path on loopback |
| the MCP client | `hermod.lok.quest/mcp` | token -> served prompts and resources | the prompt list, the resource list, and a byte-exact template download |

- **Deploy ordering**: the config is committed and pushed first, then the dispatch runs, because the workflow checks out this repo and reads the config from that checkout.
- **Existing data**: none written. The store is the memory database, and this release creates no rows.
- **Rollback**: `kamal rollback 32ff7c6` through the same workflow. The store is not rolled back and does not need to be, because nothing here wrote to it.

### Technical Considerations
- **Kamal applies the keys its config gives it, and this plan does not assume what else it does to the container's environment.** With `HERMOD_CONTENT_ROOT` (singular) in `env.clear` and the image's own `HERMOD_CONTENT_ROOTS` naming both checkouts, `config.py` prefers the plural, so the second source either serves by layering or does not serve at all, depending on behaviour this plan has not verified. The key is corrected either way, because a deployment whose served set depends on which ENV an image happens to carry is one image change away from silently serving half of it. **Settled by the release:** the deploy run's own Kamal log shows `docker run ... --env HERMOD_CONTENT_ROOTS="/app/agent-memory-project,/app/agent-memory-wizards"`, so the config supplies the value and the served set no longer depends on the image's ENV at all.
- **A rollback restores a container, not data.** Anything a newer release wrote stays written. This release writes nothing, so the rollback is clean, and naming the general trap is the point of writing it down.
- **The box is shared with Munnin.** Different service name, different container port (8210 against 8200), no volume of its own, and the store is Munnin's database reached over the shared network. A Hermod release must not disturb the container that owns the data.
- **The dispatch is manual on purpose.** The button is pressed when the release is meant, rather than fired as a tail on every build.

---

## **IMPLEMENTATION PHASES**

### Phase 1: The config names its truth
- [x] **Step 1.1**: Name both content roots
  - **Action**: Replace the singular content key with the plural, listing the overlay and the wizards checkouts
  - **Implementation**: In `config/deploy.yml`'s `env.clear`, `HERMOD_CONTENT_ROOT: /app/agent-memory-project` becomes `HERMOD_CONTENT_ROOTS: /app/agent-memory-project,/app/agent-memory-wizards`, with the comment above it saying why both are named
  - **Testing**: The file parses as YAML, and the value matches the `ENV` line the Dockerfile sets at `hermod-server/Dockerfile:45`
  - **Success Criteria**: The deploy config names both checkouts and no singular content key remains

- [x] **Step 1.2**: Put it on the remote
  - **Action**: Commit and push the deploy repo
  - **Implementation**: One commit in `hermod-deploy`, pushed to `main`, because the workflow reads the config from its own checkout
  - **Testing**: `git status -sb` level with `origin/main`, and `git ls-remote origin main` equal to local `HEAD`
  - **Success Criteria**: The remote carries the config commit the dispatch will use

- [x] **Step 1.3**: Correct the ops note the release makes false
  - **Action**: Fix `deploy/README.md`'s claim that `/health` is the one route the token guard does not cover
  - **Implementation**: The content route is public too, and 3f898bd adds it, so the sentence names both and says what each is for
  - **Testing**: Read the paragraph against the route table in `hermod-server/src/hermod/app.py`, which places `/content/{name}` on the parent app beside `/health`
  - **Success Criteria**: No sentence in the deploy repo describes a public surface the deployment does not have

### Phase 2: The release
- [x] **Step 2.1**: Name the way back before touching the box
  - **Action**: Record the live tag and the rollback command, and confirm nothing is in flight
  - **Implementation**: Read the last successful Deploy run and the last built tag; the fallback is `kamal rollback 32ff7c6`, invoked through this workflow's own `command: rollback`
  - **Testing**: `gh run list` shows no queued or running Deploy run, and the previous tag exists in the registry's build history
  - **Success Criteria**: The rollback target is named, reachable, and written here before the deploy runs

- [x] **Step 2.2**: Dispatch the deploy
  - **Action**: Run the Deploy workflow for tag `3f898bd`
  - **Implementation**: `gh workflow run "Deploy" --repo alvseek/hermod-deploy -f version=3f898bd -f command=deploy`, then watch the run that dispatch creates, taking its id from the dispatch itself rather than from the newest run
  - **Testing**: `gh run view <id>` ends success, and Kamal's own healthcheck passes against `/health` before the new container takes over
  - **Success Criteria**: The run succeeds and the new container is the one answering

### Phase 3: Verification from outside
- [x] **Step 3.1**: Read the served face
  - **Action**: List the served prompts and resources through this session's own hermod connection, which has nothing installed locally
  - **Implementation**: The served `help` procedure for the prompt set, and the resource listing
  - **Testing**: 26 prompts (the overlay's 8 plus the wizards' 18) with wizard names present, and 10 resources
  - **Success Criteria**: The counts and names are what SP-2 proved on loopback

- [x] **Step 3.2**: Fetch a template as bytes
  - **Action**: Download one wizard template and one overlay template from the public route
  - **Implementation**: `GET https://hermod.lok.quest/content/<stem>` for `council-of-wizards-plan-template` and `orientation-map-template`
  - **Testing**: Both return 200, and their bytes equal the files in the pinned checkouts
  - **Success Criteria**: Byte-exact both, from a route no local install touches

- [x] **Step 3.3**: Health, and the record
  - **Action**: Confirm `/health`, then record the outcome here and advance SP-3 in the council's Execution Log
  - **Implementation**: `GET /health` for 200; the execution log below; the council log's row
  - **Testing**: The status code, and the log rows reading DONE
  - **Success Criteria**: The release is recorded where the council looks for it

---

## **EXECUTION LOG**
**Execution Protocol for AI**:
I have to use this document as my **ONLY** source of truth to execute and track the plan steps iteratively. I should **NOT** use additional tools like ToDos because it lacks the context of what should I do. Everytime I want to implement a step I have to check the reference to the original step plan above. Everytime a step has been finished I need to go back to this document to log what was done.
*In other words*:
- I have to make this document as the source of truth for the implementation phase on what I have worked on and what I will be working
- The original plan must be fully in my context, therefore, I have to make sure I loaded the **Plan File** before executing any task and read carefully the reference to the original step
- I have to do the implementation by doing it in order per step THEN, I ALWAYS have to fill the step log rightly after

**Definition of Done (applies to ALL steps)**:
- ✅ **Code Quality**: Code compiles/runs without errors
- ✅ **Testing**: Tests written and passing
- ✅ **Logged**: Implementation and testing logged below
- 🚫 **Blocked**: Get input from [USER-NAME] before assuming

### Phase 1:
- [x] **Step 1.1**: Name both content roots
  - **Implementation Log**: In `config/deploy.yml`'s `env.clear`, `HERMOD_CONTENT_ROOT: /app/agent-memory-project` was replaced by `HERMOD_CONTENT_ROOTS: /app/agent-memory-project,/app/agent-memory-wizards`, with a comment above it saying both checkouts are listed, overlay first, and that the image sets the same value.
  - **Testing Log**: The file parses as YAML (venv python, `yaml.safe_load`). `env.clear.HERMOD_CONTENT_ROOTS` reads `/app/agent-memory-project,/app/agent-memory-wizards`, no singular key is present, and the value equals the `ENV` line at `hermod-server/Dockerfile:45` character for character.
  - **Success Criteria**: Pass.
  - **Tech Debts**: none.
  - **Result**: The deploy config names both checkouts, and the singular key is gone.

- [x] **Step 1.2**: Put it on the remote
  - **Implementation Log**: One commit, `5cba5e2`, carrying `config/deploy.yml` and `deploy/README.md`, pushed to `main`.
  - **Testing Log**: `git status -sb` is level with `origin/main`; local `HEAD` and `ls-remote origin main` both read `5cba5e2e6a27d9c2034ba696c4b78044e31efaf1`.
  - **Success Criteria**: Pass.
  - **Tech Debts**: Step order deviated deliberately: Step 1.3's README fix was made before the commit so that one commit carries both edits, which is what this step asks for.
  - **Result**: The remote carries the config commit the dispatch reads.

- [x] **Step 1.3**: Correct the ops note the release makes false
  - **Implementation Log**: `deploy/README.md`'s closing paragraph now says the guard covers the MCP face and nothing else, and names three public surfaces: `/health`, `/content/<name>`, and the OAuth discovery documents under `/.well-known/`.
  - **Testing Log**: Read against `hermod-server/src/hermod/app.py`, where the route list holds `/health` and `/content/{name}` on the parent app and `auth.get_well_known_routes()` extends the router with the discovery documents. **The first draft was wrong**: it said two routes sit outside the guard, written before that third set was found, and it was corrected before the commit.
  - **Success Criteria**: Pass.
  - **Tech Debts**: none.
  - **Result**: No sentence in the deploy repo describes a public surface the deployment does not have.

### Phase 2:
- [x] **Step 2.1**: Name the way back before touching the box
  - **Implementation Log**: The last successful Deploy run was 2026-10-15T03:36 (run 38677105912) and nothing was queued or running. The tag it deployed, `32ff7c6`, is the rollback target, reachable through this workflow's own `command: rollback`.
  - **Testing Log**: `gh run list --workflow "Deploy"` showed only completed runs. Both tags were confirmed present in the registry with `docker manifest inspect ghcr.io/alvseek/hermod:<tag>`, which answered for `32ff7c6` and for `3f898bd` (the registry API needs `read:packages`, which this token does not carry, so the manifest check was the route that worked).
  - **Success Criteria**: Pass. The target is named, and both the target and the release tag exist.
  - **Tech Debts**: none.
  - **Result**: The way back was named and proven reachable before the deploy ran.

- [x] **Step 2.2**: Dispatch the deploy
  - **Implementation Log**: `gh workflow run "Deploy" -f version=3f898bd -f command=deploy` exited 0 and printed the run URL, `https://github.com/alvseek/hermod-deploy/actions/runs/39180152297`, which is where the run id was taken from rather than from "the newest run".
  - **Testing Log**: `gh run watch 39180152297 --exit-status` ended 0; `gh run view` reports `conclusion: success`, created 2026-10-19T00:18:00Z, updated 00:19:05Z, `headSha: 5cba5e2`, which is this plan's config commit. Kamal's own healthcheck passed against `/health` before the new container took over, so the swap happened on a healthy target.
  - **Success Criteria**: Pass. The run succeeded and the new container is the one answering.
  - **Tech Debts**: none.
  - **Result**: `3f898bd` is live on `hermod.lok.quest`.

### Phase 3:
- [x] **Step 3.1**: Read the served face
  - **Implementation Log**: The served `help` procedure over this session's own MCP connection, which has nothing installed locally.
  - **Testing Log**: 26 prompts, the overlay's 8 plus the wizards' 18, with `council-of-wizards`, `high-wizard`, `pixel-wizard`, `quick-wizard`, `rite-of-creation`, `forge-of-covenant`, `analyze-code-quality`, `run-qa-test` and the rest present. The resource listing holds 10, five of them the wizards' plan templates. The first `list_resources` call failed with `Session not found`, which is the container swap dropping the previous MCP session, and the retry established a new one.
  - **Success Criteria**: Pass. The counts and names are what SP-2 proved on loopback.
  - **Tech Debts**: none.
  - **Result**: A client with nothing installed sees the whole wizard set.

- [x] **Step 3.2**: Fetch a template as bytes
  - **Implementation Log**: `GET https://hermod.lok.quest/content/<stem>` for one template from each checkout.
  - **Testing Log**: `council-of-wizards-plan-template` returned 9,936 bytes and `orientation-map-template` 8,538 bytes. Both SHA256 digests equal the files in the pinned checkouts: `F7E48B63...7F65` for the council template and `96A9AAFB...08E7` for the orientation map.
  - **Success Criteria**: Pass. Byte-exact both, from a route no local install touches.
  - **Tech Debts**: none.
  - **Result**: The download route is live and returns the files themselves.

- [x] **Step 3.3**: Health, and the record
  - **Implementation Log**: `GET /health`, then the records below and in the council's Execution Log.
  - **Testing Log**: `/health` answered `200` with `{"status":"ok","service":"hermod","version":"0.1.0"}`. The deploy run's Kamal log settles the plan's open technical question: it shows `docker run ... --env HERMOD_CONTENT_ROOTS="/app/agent-memory-project,/app/agent-memory-wizards"`, so the deploy config is what supplied both roots rather than the image's own ENV.
  - **Success Criteria**: Pass. The release is recorded where the council looks for it.
  - **Tech Debts**: the wizards pin stays at `3cff4e2` while the repo's `main` is one docs-only commit ahead; the ordinary push flow bumps it.
  - **Result**: The hosted face serves both sources, and the record says so.

---

## **QUALITY REVIEW**
*Filled by procedure Step 16 (delegated to `/analyze-code-quality` in embedded mode) after all execution phases are complete. **Static** review — answers "is the code clean?".*

- **Scope**: `config/deploy.yml` and `deploy/README.md`, from the Execution Log, reconciled against `git status --short`
- **Quality Standard**: None found. No `quality-standard.md` exists in this repo or in `hermod-server`, so Dimension 8 was skipped and the walk was freeform
- **Findings**: Two Medium, no Critical. Both in `README.md` at the repo root, which the reconciliation in Step 3 is what surfaced:
  1. `README.md:43` enumerates what is deliberately not here and names one content submodule. With the wizards pinned as a second submodule of `hermod-server`, the sentence describes the deployment's content as a single repo. This release is what made it incomplete.
  2. `README.md:51` states `3792b0b` as the running release. That moved on 10-15 to `32ff7c6` and again today to `3f898bd`, so the claim was already stale when this plan started, and any fix that types a tag goes stale the same way.
- **Fixed**: Both, at option A, in `217de40`. Finding 1's fix was extended to its three siblings in the same file, because the same defeat appeared in a description of the repo (`README.md:3`), in the submodule table (line 13) and in the clone instructions (line 20), and fixing only the instance that was reported would leave the others saying the same false thing. Finding 2 replaced the typed tag with the sentence that the running release is read off the box, pointing at `deploy/README.md` for the command.

---

## **QA HANDOFF**
*Filled by procedure Step 17 after Quality Review is resolved. This plan is **not** runtime-verified — this section records the plan for that verification, which happens in a QA session with the stack up.*

- **Scope**: `hermod-deploy/config/deploy.yml`, `hermod-deploy/deploy/README.md`, and the release act itself
- **QA instrument**: **NOT SET UP.** No `qa/` folder and no `qa-map.md` exist in `hermod-deploy` or in `hermod-server`, so this handoff auto-skips rather than inventing one
- **Integration coverage**: **NONE**, from `/qa-status` at Step 14: the bench check fails first (no map, no bench), so no phase of this plan can run an `/integration-test`. The stack itself answers (`GET https://hermod.lok.quest/health` returned 200, run on 2026-10-19), which is a probe of the deployed service rather than of a bench. What this plan does instead is Step 3's live check from a connected client: it crosses the real MCP face and the real public route, and it still does not touch the store
- **Checklist**: none. No instrument, so nothing to run, and SP-2 carried the same skip for the same reason
- **Coverage split**: 0 automated in this repo. The automated half lives in `hermod-server` (84 passed, 51 skipped without a database) and was proven on loopback in SP-2 (135 passed with the database up). This plan adds 0 automated and 3 manual checks, all of them in Step 3
- **Runtime verification**: **the served face is now verified, and the release is what verified it.** Step 3 ran against the live host: 26 prompts and 10 resources from a connected client, two templates byte-exact from the public route, `/health` 200. What remains unproven is the hosted **store** path, since this release wrote no rows, and the wizard prompts as a real fleet session uses them rather than as a listing

> Do not read a filled checklist as a passed one. This section says a verification *plan* exists, nothing more.

---

## **POST-COMPLETION**
This plan does not archive itself, for the same reason its two siblings do not: `/high-wizard`'s Step 18 would move the file out of the council folder while the council is still open, breaking the `Sub-Plans Table` link before anyone could follow it. The council's own Step 19 files the whole folder at once, once [USER-NAME] confirms the feature is complete.
