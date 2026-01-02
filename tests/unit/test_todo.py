"""
Unit tests for the Todo model.

This module contains unit tests for the Todo class functionality.
"""

import unittest
from src.models.todo import Todo


class TestTodo(unittest.TestCase):
    """
    Unit tests for the Todo class.
    """

    def test_todo_creation_with_title_only(self):
        """Test creating a Todo with title only."""
        todo = Todo(1, "Test title")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test title")
        self.assertEqual(todo.description, "")

    def test_todo_creation_with_title_and_description(self):
        """Test creating a Todo with both title and description."""
        todo = Todo(1, "Test title", "Test description")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test title")
        self.assertEqual(todo.description, "Test description")

    def test_todo_creation_with_empty_title_raises_error(self):
        """Test that creating a Todo with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            Todo(1, "")

    def test_todo_creation_with_whitespace_only_title_raises_error(self):
        """Test that creating a Todo with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            Todo(1, "   ")

    def test_todo_creation_trims_whitespace(self):
        """Test that Todo creation trims whitespace from title and description."""
        todo = Todo(1, "  Test title  ", "  Test description  ")
        self.assertEqual(todo.title, "Test title")
        self.assertEqual(todo.description, "Test description")

    def test_todo_to_dict(self):
        """Test converting Todo to dictionary representation."""
        todo = Todo(1, "Test title", "Test description")
        expected_dict = {
            "id": 1,
            "title": "Test title",
            "description": "Test description"
        }
        self.assertEqual(todo.to_dict(), expected_dict)

    def test_todo_str_representation(self):
        """Test string representation of Todo."""
        todo = Todo(1, "Test title", "Test description")
        expected_str = "[1] Test title\n   Description: Test description"
        self.assertEqual(str(todo), expected_str)

    def test_todo_str_representation_empty_description(self):
        """Test string representation of Todo with empty description."""
        todo = Todo(1, "Test title", "")
        expected_str = "[1] Test title\n   Description: (no description)"
        self.assertEqual(str(todo), expected_str)

    def test_todo_repr_representation(self):
        """Test developer-friendly representation of Todo."""
        todo = Todo(1, "Test title", "Test description")
        expected_repr = "Todo(id=1, title='Test title', description='Test description')"
        self.assertEqual(repr(todo), expected_repr)


if __name__ == "__main__":
    unittest.main()