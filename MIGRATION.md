# Migration Note - extracted from the coding overlay (2026-10-09)

The wizard + QA + implement-plan cluster was **moved out of** the coding overlay
(`agent-memory-coding-skill` / Hermod-coding) into this standalone repo, extending the
**Hermod family**: `hermod-coding` + `hermod-fleet` + `hermod-wizards`.

## What moved

- **procedures**: `high-wizard`, `quick-wizard`, `council-of-wizards`, `rite-of-creation`,
  `forge-of-covenant`, `pixel-wizard`, `implement-plan`, `analyze-code-quality`,
  `build-qa-bench`, `generate-qa-checklist`, `integration-test`, `map-qa-instrument`,
  `qa-status`, `run-qa-test`, `setup-qa-visual-instrument`, `generate-standard`,
  `wait-options-coding`
- **components**: `archive-plan`, `build-riao-mechanisms`, `plan-final-review`,
  `plan-self-review`, `planning-decision`, `planning-investigation`, `planning-rounds`,
  `subplan-handoff-read`, `subplan-handoff-write`
- **templates**: `adr-template.md`, `qa-readme-template.md`, `quality-standard-template.md`
- **plan-templates**: `high-wizard-plan-template.md`, `council-of-wizards-plan-template.md`,
  `rite-of-creation-plan-template.md`, `forge-of-covenant-plan-template.md`,
  `code-quality-analysis-template.md`

## What did not move

- The overlay keeps the shell (`awaken-coder`, `project-wrap-up`, `dockerize`, push/pull) and
  the project / doc surface (orientation map, project context, doc generators, localization).
- `generate-standard` moved with the cluster because its template
  (`code-quality-analysis-template`) and its consumer (`analyze-code-quality`) live here.

## The doc generators

The three doc generators (`generate-architecture-docs`, `generate-domain-docs`,
`generate-flow-docs`) used `wait-options-coding` only on their rare ambiguous-scope branch;
they now fall back to the core `/wait-options`. Nothing else in the overlay referenced the
cluster.

## History

Per-file commit history remains in `agent-memory-coding-skill`. This repo starts with a
**fresh initial commit**, mirroring the fleet and the coding overlay's own extraction.

## Access declarations

This repo declares **no** access: nothing calls it. It reads the core (its `wait-options-coding`
invokes the core `/wait-options`). See the overlay's `docs/adr/` for the family model.
