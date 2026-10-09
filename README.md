# agent-memory-wizards

The **wizards add-on** of the [agent-memory](https://github.com/alvseek/agent-memory-system) framework, and a member of the **Hermod family** beside the coding overlay ([agent-memory-project](https://github.com/alvseek/agent-memory-project)) and the fleet ([agent-memory-fleet](https://github.com/alvseek/agent-memory-fleet)).

This repo holds the planning-and-verification cluster: the wizard protocols (`/quick-wizard`, `/high-wizard`, `/pixel-wizard`, `/council-of-wizards`, `/rite-of-creation`, `/forge-of-covenant`), `/implement-plan`, the QA pipeline (`/map-qa-instrument`, `/build-qa-bench`, `/integration-test`, `/run-qa-test`, `/qa-status`, `/generate-qa-checklist`, `/analyze-code-quality`, `/generate-standard`, `/setup-qa-visual-instrument`), and the coding decision format `/wait-options-coding`. They run by writing and executing plan artifacts, which the coding overlay composes but does not own, so the cluster is its own capability.

## Relationship to the family

- **Standalone, independent repo**: a peer of the core (`agent-memory-system`), the coding overlay (`agent-memory-project`), and the fleet (`agent-memory-fleet`).
- **One-way dependency**: this repo reads the core (`wait-options-coding` invokes the core `/wait-options`). Nothing calls this repo, so it declares **no** access.
- **No data**: it holds only operations; it writes plan artifacts into the working project's `plans/`.

## Contents

- **procedures/**: the six wizards, `implement-plan`, the QA pipeline, `wait-options-coding`
- **components/**: the shared planning / handoff / review fragments plus `archive-plan` and `build-riao-mechanisms`
- **templates/**: `adr-template`, `qa-readme-template`, `quality-standard-template`
- **plan-templates/**: the wizard plan templates plus `code-quality-analysis-template`

## Setup

Install the **memory core first**, then this repo:

```bash
python setup-scripts/setup-all-opencode.py
```

On Windows, run `setup-scripts\setup-all-opencode.bat`.

> **OpenCode only for now.** The other harnesses (Claude Code, Codex, Antigravity) get the cluster once their installers are added.

## License

Licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE). See [MIGRATION.md](MIGRATION.md) for where this came from.
