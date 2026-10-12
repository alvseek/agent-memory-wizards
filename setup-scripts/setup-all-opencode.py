"""Install the agent-memory-wizards procedures as OpenCode **Agent Skills**.

OpenCode discovers global skills as folders holding a ``SKILL.md`` with ``name`` and
``description`` frontmatter in ``~/.config/opencode/skills/`` (``$XDG_CONFIG_HOME/opencode/skills``
when ``XDG_CONFIG_HOME`` is set). Skills are **model-invoked**: the agent sees each skill's name
and description at every step and loads the body itself when a task matches — which is why
skills fit this repo better than slash commands here. Commands have to be typed (``/name``); no
user is going to type ``/council-of-wizards`` from memory, so the procedures would sit idle. With
skills, the agent reaches for them on its own.

Installed folders carry the repo's ``agent-wizards-`` prefix — deliberately distinct from the
core's ``agent-memory-``, the coding overlay's ``agent-coding-`` and the fleet's ``agent-fleet-``
ones — so the skill catalog stays legible and each installer's manifest claims an unambiguous
set: that prefix separation is what keeps a same-named procedure from ever sharing (and
clobbering) another repo's folder.

This repo composes ON TOP OF the memory core (agent-memory-system); install the core too by
running its own installer. Each installer owns its manifest and cleans up independently, so they
coexist in one skills directory and none deletes a skill another claims.

Cross-platform: run directly on macOS/Linux, or via the ``.bat`` wrapper on Windows.

Usage:        python setup-scripts/setup-all-opencode.py
Env override: AGENT_MEMORY_TARGET_DIR (default: ~/.config/opencode/skills)
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "overlay_install_skills", _ROOT / "setup-scripts" / "install-skills.py"
)
_skills = importlib.util.module_from_spec(_spec)
sys.modules["overlay_install_skills"] = _skills
_spec.loader.exec_module(_skills)

MANIFEST_NAME = ".agent-memory-wizards-opencode-manifest"
CORE_MANIFEST_NAME = ".agent-memory-opencode-manifest"
PROJECT_MANIFEST_NAME = ".agent-memory-project-opencode-manifest"
LOCAL_MANIFEST_NAME = ".agent-memory-local-opencode-manifest"
FLEET_MANIFEST_NAME = ".agent-memory-fleet-opencode-manifest"
DOC_MANIFEST_NAME = ".agent-memory-doc-opencode-manifest"

# Protect every sibling's skills: all four installers share one skills directory, so a stale
# wizards entry must never delete a skill the core, overlay or fleet owns.
SIBLING_MANIFEST_NAMES = [
    CORE_MANIFEST_NAME,
    PROJECT_MANIFEST_NAME,
    LOCAL_MANIFEST_NAME,
    FLEET_MANIFEST_NAME,
    DOC_MANIFEST_NAME,
]


def _config_base() -> Path:
    """Base dir for OpenCode global state (respects XDG on Linux/macOS)."""
    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg) / "opencode"
    return Path.home() / ".config" / "opencode"


def main(argv: list[str] | None = None) -> int:
    base = _config_base()
    target = Path(os.environ.get("AGENT_MEMORY_TARGET_DIR") or base / "skills")

    return _skills.run(
        platform="OpenCode",
        target_dir=target,
        manifest_name=MANIFEST_NAME,
        sibling_manifest_names=SIBLING_MANIFEST_NAMES,
        instructions_file=base / "AGENTS.md",
    )


if __name__ == "__main__":
    raise SystemExit(main())
