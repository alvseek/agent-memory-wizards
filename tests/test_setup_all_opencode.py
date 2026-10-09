"""Tests for setup-all-opencode.py — the OpenCode entry point.

Loaded by file path (hyphenated name). ``main()`` is never called, since it writes to the real
OpenCode config; the constants it feeds the shared installer are asserted directly.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SCRIPT = ROOT / "setup-scripts" / "setup-all-opencode.py"

_spec = importlib.util.spec_from_file_location("overlay_setup_opencode", _SCRIPT)
so = importlib.util.module_from_spec(_spec)
sys.modules["overlay_setup_opencode"] = so
_spec.loader.exec_module(so)


def test_manifest_name_is_the_wizards_one() -> None:
    assert so.MANIFEST_NAME == ".agent-memory-wizards-opencode-manifest"


def test_siblings_cover_every_other_repo() -> None:
    """All four installers share one skills directory, so every sibling must be protected."""
    assert so.SIBLING_MANIFEST_NAMES == [
        ".agent-memory-opencode-manifest",
        ".agent-memory-coding-skill-opencode-manifest",
        ".agent-memory-fleet-opencode-manifest",
    ]
    assert so.MANIFEST_NAME not in so.SIBLING_MANIFEST_NAMES


def test_config_base_is_the_opencode_dir(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    assert so._config_base() == tmp_path / "opencode"
