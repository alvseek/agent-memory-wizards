"""Worktree instruction contracts, not proof of an agent executing them."""

from pathlib import Path

import pytest
from test_compile_procedures import cc

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=["authored", "compiled"])
def procedure(request, tmp_path):
    if request.param == "authored":
        return (ROOT / "procedures" / "implement-plan.md").read_text(encoding="utf-8")
    reports = cc.compile_all(ROOT, tmp_path, verbose=False)
    return next(r for r in reports if r.name == "implement-plan").out_path.read_text(
        encoding="utf-8"
    )


def test_optional_workspace_inputs_reuse_or_create(procedure):
    assert "All arguments are optional" in procedure
    assert "use this worktree if it exists; otherwise create it" in procedure
    assert "use this branch if it exists; otherwise create it from the current HEAD" in procedure
    assert "With `--worktree`, use the branch there" in procedure
    assert "otherwise use it in the current working directory" in procedure


def test_document_paths_resolve_before_workspace_switch(procedure):
    assert "from the invoking working directory before switching workspace" in procedure
    assert "keep those document paths for implementation" in procedure


def test_no_workspace_inputs_preserve_current_workspace(procedure):
    assert "Without workspace arguments, keep the current working directory and branch" in procedure


def test_conflicts_stop_without_overwriting(procedure):
    assert "If an existing worktree conflicts with the requested branch" in procedure
    assert "STOP and ask [USER-NAME]" in procedure
    assert "Do not overwrite existing work or force a branch switch" in procedure
