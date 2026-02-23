# tests/test_cli_create.py
import pytest
import subprocess
from unittest.mock import patch

CLI_PATH = "task_manager/cli.py"

def run_cli(args):
    """Helper to run the CLI with subprocess and capture output."""
    result = subprocess.run(
        ["python", CLI_PATH] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


# --- High Priority Tests ---

@patch("task_manager.cli.TaskManager.create_task", return_value="1234abcd")
def test_create_minimal_success(mock_create):
    stdout, stderr, code = run_cli(["create", "Test Task"])
    assert "Created task with ID: 1234abcd" in stdout
    assert code == 0


@patch("task_manager.cli.TaskManager.create_task", return_value="abcd1234")
def test_create_with_all_fields_success(mock_create):
    stdout, stderr, code = run_cli([
        "create", "Full Task",
        "-d", "Detailed description",
        "-p", "3",
        "-u", "2026-02-23",
        "-t", "work,urgent"
    ])
    assert "Created task with ID: abcd1234" in stdout
    assert code == 0


def test_create_invalid_priority():
    stdout, stderr, code = run_cli([
        "create", "Bad Priority Task",
        "-p", "5"
    ])
    assert "invalid choice" in stderr.lower()
    assert code != 0


def test_create_invalid_date_format():
    stdout, stderr, code = run_cli([
        "create", "Bad Date Task",
        "-u", "23-02-2026"
    ])
    # argparse won't catch this, but TaskManager should fail
    # Expect failure message from CLI
    assert "Failed to create" in stdout or "invalid date" in stdout


# --- Medium Priority Tests ---

@patch("task_manager.cli.TaskManager.create_task", return_value="xyz987")
def test_create_empty_description(mock_create):
    stdout, _, code = run_cli(["create", "No Description"])
    assert "Created task with ID: xyz987" in stdout
    assert code == 0


@patch("task_manager.cli.TaskManager.create_task", return_value="tag123")
def test_create_with_tags(mock_create):
    stdout, _, code = run_cli([
        "create", "Tagged Task",
        "-t", "backend,api"
    ])
    assert "Created task with ID: tag123" in stdout
    assert code == 0


# --- Low Priority Tests ---

def test_create_missing_title():
    stdout, stderr, code = run_cli(["create"])
    assert "error" in stderr.lower()
    assert code != 0


def test_create_help_message():
    stdout, _, code = run_cli(["create", "-h"])
    assert "usage:" in stdout.lower()
    assert "Task title" in stdout
    assert code == 0

