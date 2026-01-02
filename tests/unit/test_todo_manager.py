"""
Unit tests for the TodoManager service.

This module contains unit tests for the TodoManager class functionality.
"""

import unittest
from src.services.todo_manager import TodoManager


class TestTodoManager(unittest.TestCase):
    """
    Unit tests for the TodoManager class.
    """

    def setUp(self):
        """Set up a fresh TodoManager instance for each test."""
        self.manager = TodoManager()

    def test_add_todo_with_title_only(self):
        """Test adding a todo with title only."""
        result = self.manager.add_todo("Test title")
        expected = {
            "id": 1,
            "title": "Test title",
            "description": ""
        }
        self.assertEqual(result, expected)
        self.assertEqual(len(self.manager.todos), 1)

    def test_add_todo_with_title_and_description(self):
        """Test adding a todo with both title and description."""
        result = self.manager.add_todo("Test title", "Test description")
        expected = {
            "id": 1,
            "title": "Test title",
            "description": "Test description"
        }
        self.assertEqual(result, expected)
        self.assertEqual(len(self.manager.todos), 1)

    def test_add_todo_auto_increment_id(self):
        """Test that IDs are auto-incremented."""
        self.manager.add_todo("First todo")
        self.manager.add_todo("Second todo")
        self.manager.add_todo("Third todo")

        # Check that IDs are 1, 2, 3
        self.assertIn(1, self.manager.todos)
        self.assertIn(2, self.manager.todos)
        self.assertIn(3, self.manager.todos)
        self.assertEqual(len(self.manager.todos), 3)

    def test_add_todo_empty_title_raises_error(self):
        """Test that adding a todo with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_todo("")

    def test_view_todos_empty(self):
        """Test viewing todos when no todos exist."""
        result = self.manager.view_todos()
        self.assertEqual(result, [])

    def test_view_todos_with_todos(self):
        """Test viewing todos when todos exist."""
        self.manager.add_todo("First todo", "Description 1")
        self.manager.add_todo("Second todo", "Description 2")

        result = self.manager.view_todos()
        expected = [
            {"id": 1, "title": "First todo", "description": "Description 1"},
            {"id": 2, "title": "Second todo", "description": "Description 2"}
        ]
        self.assertEqual(result, expected)

    def test_view_todos_sorted_by_id(self):
        """Test that todos are returned sorted by ID."""
        # Add todos in reverse order to test sorting
        self.manager.add_todo("Third todo", "Description 3")
        self.manager.add_todo("First todo", "Description 1")
        self.manager.add_todo("Second todo", "Description 2")

        result = self.manager.view_todos()
        expected = [
            {"id": 1, "title": "Third todo", "description": "Description 3"},
            {"id": 2, "title": "First todo", "description": "Description 1"},
            {"id": 3, "title": "Second todo", "description": "Description 2"}
        ]
        self.assertEqual(result, expected)

    def test_update_todo_valid_id(self):
        """Test updating an existing todo."""
        self.manager.add_todo("Original title", "Original description")

        result = self.manager.update_todo(1, "New title", "New description")
        expected = {
            "id": 1,
            "title": "New title",
            "description": "New description"
        }
        self.assertEqual(result, expected)
        self.assertEqual(self.manager.todos[1].title, "New title")
        self.assertEqual(self.manager.todos[1].description, "New description")

    def test_update_todo_partial_update_title_only(self):
        """Test updating only the title of a todo."""
        self.manager.add_todo("Original title", "Original description")

        result = self.manager.update_todo(1, new_title="New title")
        expected = {
            "id": 1,
            "title": "New title",
            "description": "Original description"
        }
        self.assertEqual(result, expected)

    def test_update_todo_partial_update_description_only(self):
        """Test updating only the description of a todo."""
        self.manager.add_todo("Original title", "Original description")

        result = self.manager.update_todo(1, new_description="New description")
        expected = {
            "id": 1,
            "title": "Original title",
            "description": "New description"
        }
        self.assertEqual(result, expected)

    def test_update_todo_invalid_id_raises_error(self):
        """Test that updating a non-existent todo raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.update_todo(999, "New title")

    def test_update_todo_empty_title_raises_error(self):
        """Test that updating with empty title raises ValueError."""
        self.manager.add_todo("Original title")
        with self.assertRaises(ValueError):
            self.manager.update_todo(1, "")

    def test_delete_todo_valid_id(self):
        """Test deleting an existing todo."""
        self.manager.add_todo("Test todo")
        self.assertIn(1, self.manager.todos)

        result = self.manager.delete_todo(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.manager.todos)

    def test_delete_todo_invalid_id(self):
        """Test deleting a non-existent todo."""
        result = self.manager.delete_todo(999)
        self.assertFalse(result)

    def test_get_todo_valid_id(self):
        """Test getting an existing todo."""
        self.manager.add_todo("Test todo")
        todo = self.manager.get_todo(1)
        self.assertIsNotNone(todo)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test todo")

    def test_get_todo_invalid_id(self):
        """Test getting a non-existent todo."""
        todo = self.manager.get_todo(999)
        self.assertIsNone(todo)


if __name__ == "__main__":
    unittest.main()