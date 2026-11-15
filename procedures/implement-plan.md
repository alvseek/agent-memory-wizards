# Implement Plan

Start implementing the approved plan, optionally constrained by a custom implementation-rules document. Follow the plan's Execution Protocol for AI strictly, including after context compaction.

## Arguments

`$ARGUMENTS`

```text
/implement-plan
/implement-plan "<implementation-rules-path>"
/implement-plan --plan "<approved-plan-path>" --rules "<implementation-rules-path>"
/implement-plan "<implementation-rules-path>" --worktree "<new-path>" --branch "<new-branch>" [--base "<ref>"]
```

These are procedure inputs interpreted by the invoking agent, not a shell command or a new parser.

- With no arguments, use the approved plan already established in the conversation and any implementation rules explicitly handed off for it. No rules document is required.
- A single positional path identifies the implementation-rules document; select the approved plan from the conversation. `--plan` and `--rules` explicitly identify their respective documents and may be used independently or together.
- Paths may have any filename. Quote paths containing spaces; resolve relative paths from the working project and honor absolute paths. Do not infer document roles from filenames alone.
- Rules are plain Markdown instructions. An optional YAML header works too; YAML is not required and no parser installation is needed. Read the prose and any header together.
- Explicit paths select the documents, never waive their requirements. If paths are missing or unreadable, the approved plan is not established, or document roles or selections conflict or remain ambiguous, STOP and ask [USER-NAME] before implementing. Do not silently ignore a requested rules document or fall back to another one.
- `--worktree` and `--branch` must be supplied together to request a new worktree and new branch. `--base` optionally selects their starting ref; default to the source repository's current `HEAD`. Reject a partial pair or `--base` without the pair. Without these options or a recorded workspace to resume, keep the existing working directory and branch.

## Before starting

Read the full approved plan and, when supplied, the full implementation-rules document in your own context. Recover any explicitly truncated output before proceeding. Confirm the working directory that owns the work. This invocation starts an already-approved plan; it does not approve a draft or clear an outstanding human gate.

The plan defines what to build, its success criteria, and progress. The rules constrain how to implement that plan; they are not a second progress tracker. A rules document cannot silently replace approved scope, waive a human STOP or sign-off, or bypass higher-priority instructions. If requirements conflict or are genuinely contradictory, STOP and ask [USER-NAME] rather than silently choosing one.

Keep the resolved plan and rules paths in the execution context and the plan's existing implementation log, when it has one, so resumption can find both. After context compaction or session resumption, reload both documents fully, inspect approval, pending gates and recorded progress, then continue with the next unfinished step. If no rules document was supplied, reload the plan alone; do not invent a rules file. Preserve verified completed work rather than restarting it without a reason.

## Prepare the implementation workspace

When a new worktree is requested, do the setup below after reading the documents and clearing their approval gates, but before any implementation. For a recorded or dispatcher-prepared workspace, use the resumption checks below instead. With neither, skip worktree setup and implement in the existing directory and branch. An explicit worktree request authorizes setup, not a new scope or a release.

1. **Anchor the inputs before switching.** Resolve the original plan and any rules to absolute paths from the invoking working directory. Keep those originals authoritative: update only the original plan's execution log, never a checkout copy. Resolve implementation-file references from the selected implementation workspace, not from the original plan's directory.
2. **Inspect the source repository.** Use `git rev-parse --show-toplevel`, `git status --short` and `git worktree list --porcelain`. Target that repository, including when it is itself a submodule; do not silently choose its parent. Uncommitted changes are not carried into the new worktree. Leave them untouched: no automatic stash, commit or copy. If implementation needs uncommitted source code, STOP and ask.
3. **Validate a new workspace.** Resolve the requested worktree path to an absolute path from the invoking working directory; quote paths containing spaces. Validate the branch with `git check-ref-format --branch`. Refuse an existing destination, existing local branch or conflicting registered worktree; never overwrite, reset or force. Resolve the requested base (or source `HEAD`) with `git rev-parse --verify --end-of-options "<base>^{commit}"`, retaining the exact commit. Do not fetch or substitute a default branch.
4. **Create and record.** Run `git -C "<source-root>" worktree add -b "<new-branch>" "<absolute-worktree-path>" "<resolved-base-commit>"`. Check success, then record the source root, worktree path, branch, exact starting commit and original document paths in the execution context and existing plan log. Record them before further setup so a partial failure can be recovered.
5. **Initialize and verify.** Run `git -C "<absolute-worktree-path>" submodule update --init --recursive` to materialize pinned submodules, not newer remote tips. Verify the registered worktree, repository identity, actual branch and starting commit before implementation, and check recursive submodule status for incomplete initialization or mismatched pins. Do not automatically copy secrets, `.env` files or dependency folders. Worktrees do not isolate databases or ports; use project-approved setup and ask if required environment configuration is missing.
6. **Switch the implementation context.** Use the harness's supported session-directory switch when available; otherwise explicitly base every implementation read, edit and command on the worktree. A shell-only `cd` does not move the agent session. Only the original plan log may be updated in the source checkout; implementation files belong in the worktree.

For a recorded worktree or one supplied as already prepared by a dispatcher, verify its source repository, registered path, branch, original document paths and recorded starting commit before resuming. Compare the source and target's absolute `git rev-parse --path-format=absolute --git-common-dir` results to establish repository identity, and check the actual branch with `git branch --show-current`. The current `HEAD` may have advanced through implementation commits; do not reset it to the starting commit. Reuse the verified workspace rather than repeating creation. A new request that conflicts with the recorded assignment requires clarification, not a second worktree. If creation or submodule setup fails, report the actual artifacts and remaining setup, STOP before implementation, and never automatically remove the worktree or branch.

---

## Execute

Follow the **Execution Protocol for AI** from the plan file and the resolved implementation rules:

1. **Read the plan file** first — load it and any supplied implementation-rules document fully before implementing
2. **Use the plan as the ONLY source of truth for scope and progress** — do NOT use TodoWrite or track progress in the rules document
3. **Check the plan reference before each step** — re-read the relevant step from the plan before implementing it
4. **Execute steps in order** — implement one step at a time, sequentially
5. **Log each step's completion** — verify the step's success criteria, then fill in the plan's implementation log before moving on; record failures, missing verification and agreed deferrals honestly
6. **If blocked or unclear** — STOP and ask [USER-NAME] before proceeding, do not assume
7. **If there's no blocker or a STOP mark, continue until it's finished** — no need to stop and confirm at each phase

Start with the next unfinished step whose approval and STOP gates are cleared, using the prepared workspace when requested. Continue in this session; this procedure does not select a model, spawn a worker or supervise another agent. Completion does not authorize archiving, merging, worktree removal or branch deletion without human sign-off.
