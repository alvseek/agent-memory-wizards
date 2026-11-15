# Implement Plan

Start implementing the approved plan, optionally constrained by a custom implementation-rules document. Follow the plan's Execution Protocol for AI strictly, including after context compaction.

## Arguments

`$ARGUMENTS`

```text
/implement-plan
/implement-plan "<implementation-rules-path>"
/implement-plan --plan "<approved-plan-path>" --rules "<implementation-rules-path>"
```

These are procedure inputs interpreted by the invoking agent, not a shell command or a new parser.

- With no arguments, use the approved plan already established in the conversation and any implementation rules explicitly handed off for it. No rules document is required.
- A single positional path identifies the implementation-rules document; select the approved plan from the conversation. `--plan` and `--rules` explicitly identify their respective documents and may be used independently or together.
- Paths may have any filename. Quote paths containing spaces; resolve relative paths from the working project and honor absolute paths. Do not infer document roles from filenames alone.
- Rules are plain Markdown instructions. An optional YAML header works too; YAML is not required and no parser installation is needed. Read the prose and any header together.
- Explicit paths select the documents, never waive their requirements. If paths are missing or unreadable, the approved plan is not established, or document roles or selections conflict or remain ambiguous, STOP and ask [USER-NAME] before implementing. Do not silently ignore a requested rules document or fall back to another one.

## Before starting

Read the full approved plan and, when supplied, the full implementation-rules document in your own context. Recover any explicitly truncated output before proceeding. Confirm the working directory that owns the work. This invocation starts an already-approved plan; it does not approve a draft or clear an outstanding human gate.

The plan defines what to build, its success criteria, and progress. The rules constrain how to implement that plan; they are not a second progress tracker. A rules document cannot silently replace approved scope, waive a human STOP or sign-off, or bypass higher-priority instructions. If requirements conflict or are genuinely contradictory, STOP and ask [USER-NAME] rather than silently choosing one.

Keep the resolved plan and rules paths in the execution context and the plan's existing implementation log, when it has one, so resumption can find both. After context compaction or session resumption, reload both documents fully, inspect approval, pending gates and recorded progress, then continue with the next unfinished step. If no rules document was supplied, reload the plan alone; do not invent a rules file. Preserve verified completed work rather than restarting it without a reason.

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

Start with the next unfinished step whose approval and STOP gates are cleared. Continue in this session; this procedure does not select a model, spawn a worker or supervise another agent. Completion does not authorize archiving without human sign-off.
