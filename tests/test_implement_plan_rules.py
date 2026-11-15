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
    assert '/implement-plan "<implementation-rules-path>"' in procedure
    assert '--plan "<approved-plan-path>" --rules "<implementation-rules-path>"' in procedure
    assert "With no arguments" in procedure
    assert "No rules document is required" in procedure
    assert "single positional path identifies the implementation-rules document" in procedure
    assert "independently or together" in procedure
    assert "Paths may have any filename" in procedure
    assert "Do not infer document roles from filenames alone" in procedure
    assert "Quote paths containing spaces" in procedure
    assert "resolve relative paths from the working project" in procedure
    assert "honor absolute paths" in procedure


def test_full_loads_and_resumption_keep_rules(procedure):
    assert "Read the full approved plan" in procedure
    assert "full implementation-rules document in your own context" in procedure
    assert "Recover any explicitly truncated output" in procedure
    assert (
        "After context compaction or session resumption, reload both documents fully" in procedure
    )
    assert "Keep the resolved plan and rules paths" in procedure
    assert "reload the plan alone; do not invent a rules file" in procedure
    assert "Preserve verified completed work" in procedure


def test_rules_constrain_execution_not_scope_or_progress(procedure):
    assert "plain Markdown instructions" in procedure
    assert "optional YAML header" in procedure
    assert "no parser installation is needed" in procedure
    assert "Read the prose and any header together" in procedure
    assert "ONLY source of truth for scope and progress" in procedure
    assert "do NOT use TodoWrite or track progress in the rules document" in procedure
    assert "cannot silently replace approved scope" in procedure
    assert "waive a human STOP or sign-off" in procedure
    assert "bypass higher-priority instructions" in procedure
    assert "STOP and ask [USER-NAME] rather than silently choosing one" in procedure


def test_missing_inputs_and_human_gates_stop_implementation(procedure):
    assert "paths are missing or unreadable" in procedure
    assert "roles or selections conflict or remain ambiguous" in procedure
    assert "Do not silently ignore a requested rules document" in procedure
    assert "does not approve a draft or clear an outstanding human gate" in procedure
    assert "verify the step's success criteria" in procedure
    assert "record failures, missing verification and agreed deferrals honestly" in procedure
    assert "does not select a model, spawn a worker or supervise another agent" in procedure
    assert "does not authorize archiving without human sign-off" in procedure
