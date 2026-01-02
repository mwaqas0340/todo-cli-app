"""
Integration tests for the CLI flow.

This module contains integration tests to verify the CLI flow works correctly
with the TodoManager service.
"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
from src.cli.main import main, get_user_input, get_integer_input, display_menu
from src.services.todo_manager import TodoManager


class TestCLIFlow(unittest.TestCase):
    """
    Integration tests for the CLI application flow.
    """

    def test_get_user_input_normal(self):
        """Test getting user input under normal conditions."""
        with patch('builtins.input', return_value='test input'):
            result = get_user_input("Enter something: ")
            self.assertEqual(result, 'test input')

    def test_get_user_input_empty(self):
        """Test getting empty user input."""
        with patch('builtins.input', return_value=''):
            result = get_user_input("Enter something: ")
            self.assertEqual(result, '')

    def test_get_integer_input_valid(self):
        """Test getting valid integer input."""
        with patch('builtins.input', return_value='42'):
            result = get_integer_input("Enter a number: ")
            self.assertEqual(result, 42)

    def test_get_integer_input_invalid(self):
        """Test handling invalid integer input."""
        with patch('builtins.input', side_effect=['invalid', '42']):
            # Capture stdout to check error message
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = get_integer_input("Enter a number: ")
                output = fake_out.getvalue()
                self.assertEqual(result, 42)
                # The function should print an error message for the invalid input
                # and continue to ask until valid input is provided
                self.assertIn("Error: Please enter a valid number.", output)

    def test_display_menu_no_exception(self):
        """Test that displaying menu doesn't raise an exception."""
        # Capture stdout to prevent menu from actually displaying
        with patch('sys.stdout', new=StringIO()):
            try:
                display_menu()
                success = True
            except Exception:
                success = False
        self.assertTrue(success)

    def test_add_todo_flow_success(self):
        """Test the add todo flow with valid inputs."""
        manager = TodoManager()

        # Mock user inputs for title and description
        with patch('builtins.input', side_effect=['New Todo', 'Description for new todo']):
            # Capture stdout to check output
            with patch('sys.stdout', new=StringIO()):
                from src.cli.main import add_todo_flow
                add_todo_flow(manager)

        # Verify the todo was added
        todos = manager.view_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['title'], 'New Todo')
        self.assertEqual(todos[0]['description'], 'Description for new todo')

    def test_view_todos_flow_empty(self):
        """Test the view todos flow when no todos exist."""
        manager = TodoManager()

        # Capture stdout to check output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            from src.cli.main import view_todos_flow
            view_todos_flow(manager)

            output = fake_out.getvalue()
            self.assertIn('No todos available', output)

    def test_view_todos_flow_with_todos(self):
        """Test the view todos flow when todos exist."""
        manager = TodoManager()
        manager.add_todo("Test Todo", "Test Description")

        # Capture stdout to check output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            from src.cli.main import view_todos_flow
            view_todos_flow(manager)

            output = fake_out.getvalue()
            self.assertIn('Test Todo', output)
            self.assertIn('Test Description', output)

    def test_update_todo_flow_success(self):
        """Test the update todo flow with valid inputs."""
        manager = TodoManager()
        manager.add_todo("Original Title", "Original Description")

        # Mock user inputs: ID, new title, new description
        with patch('builtins.input', side_effect=['1', 'Updated Title', 'Updated Description']):
            # Capture stdout to check output
            with patch('sys.stdout', new=StringIO()):
                from src.cli.main import update_todo_flow
                update_todo_flow(manager)

        # Verify the todo was updated
        todos = manager.view_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['title'], 'Updated Title')
        self.assertEqual(todos[0]['description'], 'Updated Description')

    def test_delete_todo_flow_success(self):
        """Test the delete todo flow with valid input."""
        manager = TodoManager()
        manager.add_todo("Test Todo")

        # Mock user input for ID
        with patch('builtins.input', return_value='1'):
            # Capture stdout to check output
            with patch('sys.stdout', new=StringIO()):
                from src.cli.main import delete_todo_flow
                delete_todo_flow(manager)

        # Verify the todo was deleted
        todos = manager.view_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_todo_flow_invalid_id(self):
        """Test the delete todo flow with invalid ID."""
        manager = TodoManager()
        manager.add_todo("Test Todo")

        # Mock user input for invalid ID
        with patch('builtins.input', return_value='999'):
            # Capture stdout to check output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                from src.cli.main import delete_todo_flow
                delete_todo_flow(manager)

                output = fake_out.getvalue()
                self.assertIn('does not exist', output)


if __name__ == "__main__":
    unittest.main()