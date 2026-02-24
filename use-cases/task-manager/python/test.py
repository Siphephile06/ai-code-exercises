import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import cli

def run_cli(args):
  """Helper to run CLI with given args and capture stdout"""
  sys.argv = ["cli.py"] + args
  buffer = StringIO()
  with patch("sys.stdout", buffer):
    try:
      cli.main()
    except SystemExit:
      # argparse calls sys.exit() on errors
      pass
  return buffer.getvalue().strip()


class TestCreateCommand(unittest.TestCase):
  """Class to test the create command."""
  @patch("cli.TaskManager.create_task", return_value="1234adcc")
  def test_create_succes(self, mock_create):
    output = run_cli([
    "create", "New Task",
    "-d", "New Description",
    "-p", "3",
    "-u", "2026-02-024",
    "-t", "work,urgent"
    ])
    self.assertIn("Created task with ID: 1234adcc", output)

class TestListCommand(unittest.TestCase):
  """Class to test the list command."""
  @patch("cli.TaskManager.list_tasks", return_value="list")
  def test_list_success(self, mock_create):
    output = run_cli([
    "list", "list all tasks"
    ])
    self.assertIn("Tasks listed successfully", output)

if __name__ == "__main__":
    unittest.main()
  
      
