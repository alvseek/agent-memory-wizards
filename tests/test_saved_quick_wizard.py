"""Saved-plan instruction contracts, checked in source and installed command output."""

from pathlib import Path

import pytest
from test_compile_procedures import cc

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=["authored", "compiled"])
def qw(request, tmp_path):
    if request.param == "authored":
        return (ROOT / "procedures" / "quick-wizard.md").read_text(encoding="utf-8")
    reports = cc.compile_all(ROOT, tmp_path, verbose=False)
    return next(r for r in reports if r.name == "quick-wizard").out_path.read_text(
        encoding="utf-8"
    )


def section(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0]


def test_saved_mode_is_explicit_and_keeps_task_arguments(qw):
    arguments = section(qw, "## Arguments", "## Procedure")
    assert "$ARGUMENTS" in arguments
    assert "/quick-wizard --save [context]" in arguments
    assert "standalone `--save`" in arguments
    assert "quoted task text" in arguments
    assert "no plan file or execution log is required" in arguments


def test_caller_destination_requests_saved_mode_and_overrides_default(qw):
    arguments = section(qw, "## Arguments", "## Procedure")
    assert "caller-supplied plan-file path" in arguments
    assert "without requiring `--save`" in arguments
    assert "instead of the default `./plans/" in arguments
    assert "relative destinations from the working project" in arguments
    assert "a path is not a handoff" in arguments
    assert "regardless of which planning protocol launched it" in arguments
    assert "Read the parent's plan or handoff" in arguments
    assert "missing or ambiguous, ask" in arguments


def test_saving_is_not_an_escalation_criterion(qw):
    gate = section(qw, "### Step 2:", "### Step 3:")
    assert "Saved mode alone is not a reason to escalate" in gate
    assert "production deployment with audit trail" in gate
    assert "Multiple files with complex interdependencies" in gate


def test_saved_file_precedes_approval_and_does_not_grant_it(qw):
    creation = section(qw, "### Step 4:", "### Step 5:")
    approval = section(qw, "### Step 5:", "### Step 6:")
    assert "never overwrite an unrelated existing plan" in creation
    assert "load an existing destination first" in creation
    assert "before presenting it for approval" in creation
    assert "draft, not authorization" in creation
    assert "linking the file in saved mode. STOP." in approval
    assert "Do NOT execute until" in approval
    assert "only after it arrives" in approval
    assert "revision that invalidates approval" in approval


def test_resumption_honors_approval_and_logs_verified_steps(qw):
    execution = section(qw, "### Step 6:", "### Step 7:")
    assert "load the full plan" in execution
    assert "after context compaction" in execution
    assert "verify it, then update" in execution
    assert "only execution tracker" in execution
    assert "never bypasses a pending approval" in execution
    assert "complete only when its success criteria are met" in execution


def test_inline_template_marks_saved_only_sections(qw):
    template = qw.split("```markdown", 1)[1]
    for heading in ("Plan State", "Specification", "Execution Log"):
        assert (
            "<!-- Saved mode only: include this section in the saved plan. -->\n"
            f"## {heading}"
        ) in template
    assert "**Approval**: PENDING" in template
    assert "**Execution Protocol for AI**" in template
    assert "**Verification / result**" in template
    assert "**Blockers / agreed deferrals**" in template
    assert "omit them from an unsaved plan" in qw


def test_review_and_handoff_use_the_saved_log(qw):
    for start, end in (("### Step 7:", "### Step 8:"), ("### Step 8:", "### Step 9:")):
        assert "saved plan's Execution Log" in section(qw, start, end)
    completion = section(qw, "### Step 9:", "## Templates")
    assert "same plan file" in completion
    assert "not a second copy" in completion
    assert "does not authorize archiving" in completion
