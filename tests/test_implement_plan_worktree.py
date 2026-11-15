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


def test_optional_paired_flags_and_committed_base(procedure):
    for phrase in (
        "--worktree",
        "--branch",
        "--base",
        "must be supplied together",
        "Reject a partial pair or `--base` without the pair",
        "current `HEAD`",
        "skip worktree setup",
        "git rev-parse --verify --end-of-options",
        "Do not fetch or substitute a default branch",
    ):
        assert phrase in procedure


def test_original_documents_remain_authoritative(procedure):
    for phrase in (
        "before switching",
        "absolute paths from the invoking working directory",
        "update only the original plan's execution log, never a checkout copy",
        "references from the selected implementation workspace",
        "not from the original plan's directory",
    ):
        assert phrase in procedure


def test_creation_checks_collisions_and_pinned_submodules(procedure):
    for phrase in (
        "git status --short",
        "git worktree list --porcelain",
        "including when it is itself a submodule",
        "Uncommitted changes are not carried",
        "no automatic stash, commit or copy",
        "git check-ref-format --branch",
        "Refuse an existing destination, existing local branch",
        "never overwrite, reset or force",
        'worktree add -b "<new-branch>"',
        "submodule update --init --recursive",
        "incomplete initialization or mismatched pins",
        "Do not automatically copy secrets",
        "Worktrees do not isolate databases or ports",
    ):
        assert phrase in procedure


def test_resume_and_partial_failure_preserve_the_workspace(procedure):
    for phrase in (
        "Record them before further setup",
        "already prepared by a dispatcher",
        "For a recorded worktree",
        "--path-format=absolute --git-common-dir",
        "git branch --show-current",
        "do not reset it to the starting commit",
        "Reuse the verified workspace rather than repeating creation",
        "STOP before implementation",
        "never automatically remove the worktree or branch",
        "A shell-only `cd` does not move the agent session",
        "branch deletion without human sign-off",
    ):
        assert phrase in procedure
