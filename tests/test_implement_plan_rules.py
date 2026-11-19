"""Implementation-rules contracts survive compilation into installed instructions."""

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


def test_optional_rules_and_explicit_document_selection(procedure):
    assert "$ARGUMENTS" in procedure
    assert '--plan "<plan-path>" --rules "<rules-path>"' in procedure
    assert "All arguments are optional" in procedure
    assert "otherwise use the approved plan established in the conversation" in procedure
    assert "Without this argument, no rules document is required" in procedure


def test_full_plan_and_rules_reads(procedure):
    assert "**Read the plan file** first" in procedure
    assert "load it fully into your context" in procedure
    assert "read this document fully as instructions for you" in procedure


def test_rules_extend_execution_without_replacing_selected_plan(procedure):
    assert "Rules may add behavior beyond this procedure" in procedure
    assert "override any argument except `--plan`" in procedure
    assert "They may call for direct implementation or delegation" in procedure
    assert "**Use the plan as the ONLY source of truth**" in procedure
    assert "do NOT use TodoWrite" in procedure


def test_missing_inputs_and_human_gates_stop_implementation(procedure):
    assert "an input is missing, unreadable or ambiguous, STOP and ask [USER-NAME]" in procedure
    assert "**If blocked or unclear**" in procedure
    assert "**If there's no blocker or a STOP mark, continue until it's finished**" in procedure
