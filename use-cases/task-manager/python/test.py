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
    self.assertIn("", output)

class TestStatusCommand(unittest.TestCase):
  """Class to test the update status command."""
  @patch("cli.TaskManager.update_task_status", return_value="status")
  def test_update_status_success(self, mock_create):
    output = run_cli([
    "task_id", "1234adcc",
    "status", "in_progress"
    ])
    self.assertIn("", output)

class TestPriorityCommand(unittest.TestCase):
  """Class to test update priority command"""
  @patch("cli.TaskManager.update_task_priority", return_value="priority")
  def test_update_priority_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc",
      "priority", "2"
    ])
    self.assertIn("", output)

class TestDue_DateCommand(unittest.TestCase):
  """Class to test update due date command"""
  @patch("cli.TaskManager.update_task_due_date", return_value="due_date")
  def test_update_due_date_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc",
      "due_date", "2026-03-01"
    ])
    self.assertIn("", output)

class TestTagCommand(unittest.TestCase):
  """Class to test tag management"""
  @patch("cli.TaskManager.add_tag_to_task", return_value="added_tag")
  def test_tag_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc",
      "tag", "done"
    ])
    self.assertIn("", output)

class TestRemoveTagCommand(unittest.TestCase):
  """class to test removing a tag"""
  @patch("cli.TaskManager.remove_tag_from_task", return_value="tag_removed")
  def test_untag_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc"
      "tag", "done"
    ])
    self.assertIn("", output)

class TestDetailsCommand(unittest.TestCase):
  """Class to test getting the details of a task"""
  @patch("cli.TaskManager.get_task_details", return_value="details")
  def test_details_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc"
    ])
    self.assertIn("", output)

class TestDeleteCommand(unittest.TestCase):
  """Class to test the deleeting a tag"""
  @patch("cli.TaskManager.delete_tag", return_value="deleted")
  def test_delete_success(self, mock_create):
    output = run_cli([
      "task_id", "1234adcc"
    ])
    self.assertIn("", output)


    
if __name__ == "__main__":
    unittest.main()
  
      
