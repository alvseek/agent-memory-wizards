# Implement Plan

Start implementing the approved plan. This command ensures the AI follows the Execution Protocol from the plan file strictly, even after context compaction.

## Arguments

`$ARGUMENTS`

```text
/implement-plan
/implement-plan --plan "<plan-path>" --rules "<rules-path>" --worktree "<worktree-path>" --branch "<branch-name>"
```

All arguments are optional:

- `--plan`: use this approved plan; otherwise use the approved plan established in the conversation.
- `--rules`: read this document fully as instructions for you, the agent running implement-plan, on how to implement the selected plan. Rules may add behavior beyond this procedure and override any argument except `--plan`. They may call for direct implementation or delegation. Without this argument, no rules document is required.
- `--worktree`: use this worktree if it exists; otherwise create it.
- `--branch`: use this branch if it exists; otherwise create it from the current HEAD. With `--worktree`, use the branch there; otherwise use it in the current working directory.

Resolve document and worktree paths from the invoking working directory before switching workspace, and keep those document paths for implementation. Without workspace arguments, keep the current working directory and branch. If an existing worktree conflicts with the requested branch, or an input is missing, unreadable or ambiguous, STOP and ask [USER-NAME]. Do not overwrite existing work or force a branch switch.

---

Let's start implementing now. Follow the **Execution Protocol for AI** from the plan file strictly:

1. **Read the plan file** first — load it fully into your context before doing anything
2. **Use the plan as the ONLY source of truth** — do NOT use TodoWrite, it lacks the context of what should be done
3. **Check the plan reference before each step** — re-read the relevant step from the plan before implementing it
4. **Execute steps in order** — implement one step at a time, sequentially
5. **Log each step's completion** — after finishing a step, go back to the plan's implementation log and fill in what was done before moving to the next step
6. **If blocked or unclear** — STOP and ask [USER-NAME] before proceeding, do not assume
7. **If there's no blocker or a STOP mark, continue until it's finished** — no need to stop and confirm at each phase

Start with Step 1 of the plan now.
