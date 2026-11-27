# agent-memory-wizards

The **wizards add-on** of the [agent-memory](https://github.com/alvseek/agent-memory-system) framework, and a member of the **Hermod family** beside the coding overlay ([agent-memory-project](https://github.com/alvseek/agent-memory-project)) and the fleet ([agent-memory-fleet](https://github.com/alvseek/agent-memory-fleet)).

This repo holds the planning-and-verification cluster: the wizard protocols (`/quick-wizard`, `/high-wizard`, `/pixel-wizard`, `/council-of-wizards`, `/rite-of-creation`, `/forge-of-covenant`), `/implement-plan`, the QA pipeline (`/map-qa-instrument`, `/build-qa-bench`, `/integration-test`, `/run-qa-test`, `/qa-status`, `/generate-qa-checklist`, `/analyze-code-quality`, `/generate-standard`, `/setup-qa-visual-instrument`), the coding decision format `/wait-options-coding`, and `/dockerize`. They run by writing and executing plan artifacts, which the coding overlay composes but does not own, so the cluster is its own capability.

## Relationship to the family

- **Standalone, independent repo**: a peer of the core (`agent-memory-system`), the coding overlay (`agent-memory-project`), and the fleet (`agent-memory-fleet`).
- **One-way dependency**: this repo reads the core (`wait-options-coding` invokes the core `/wait-options`). Nothing calls this repo, so it declares **no** access.
- **No data**: it holds only operations; it writes plan artifacts into the working project's `plans/`.

## Contents

- **procedures/**: the six wizards, `implement-plan`, the QA pipeline, `wait-options-coding`, `dockerize`
- **procedures/components/**: the shared planning / handoff / review fragments plus `archive-plan` and `build-riao-mechanisms`
- **templates/**: `adr-template`, `qa-readme-template`, `quality-standard-template`
- **plan-templates/**: the wizard plan templates plus `code-quality-analysis-template`

## Setup

Install the **memory core first**, then use Python 3.12+ and Git to install the
composer into the Python environment that will run the scripts:

```bash
python -m pip install -r requirements.txt
python setup-scripts/setup-all-opencode.py
```

You can also run `setup-scripts\setup-all-opencode.bat` on Windows. If you installed
the requirements into a virtual environment, activate it before running the wrapper.

> **OpenCode only for now.** The other harnesses (Claude Code, Codex, Antigravity) get the cluster once their installers are added.

## Authoring procedures

Use [Format 2](https://github.com/alvseek/agent-memory-system/blob/4f1dab49ecebfd54a27ebcfcd681b3cbb032756d/packages/procedure-composer/README.md).
Each procedure and component starts with `+++`-delimited TOML metadata. Its `id`
matches the filename, and `kind` is `procedure` or `component`. Put rendered
instructions after the closing `+++`. Keep these Markdown sources in LF: the
composer preserves authored line endings and blank lines.

For example, [`build-qa-bench`](procedures/build-qa-bench.md) keeps the caller's
`missing` phase and its `#templates` link in prose, then references the recipes:

```markdown
For a `missing` phase, follow the Build R/I/A/O Mechanisms component — the per-part (RESET / INJECT / ACT / OBSERVE) scaffold recipes — and shape the files per the [Templates](#templates) below.

@start component id="build-qa-bench.build-riao-mechanisms" ref="procedures/components/build-riao-mechanisms.md"
@end component
```

Edit the recipes in [`build-riao-mechanisms.md`](procedures/components/build-riao-mechanisms.md).
The reference interior stays empty. This component is shared by Markdown and DB;
wizard sources have no backend storage instructions to duplicate. Template links
stay in the rendered procedure because the procedure copies those files by path.

Preview the installed Markdown and check its references with:

```bash
python setup-scripts/compile-procedures.py --strict
```

## License

Licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE). See [MIGRATION.md](MIGRATION.md) for where this came from.
