"""
Todo Manager service for the In Memory Python Console App.

This module provides business logic for todo operations including
adding, viewing, updating, and deleting todos with in-memory storage.
"""

from src.models.todo import Todo


class TodoManager:
    """
    Manages in-memory storage of todos and provides CRUD operations.
    """

    def __init__(self):
        """
        Initialize the TodoManager with empty storage and next ID counter.
        """
        self.todos = {}  # Dictionary to store todos: id -> Todo object
        self.next_id = 1  # Counter for auto-incrementing IDs

    def add_todo(self, title, description=""):
        """
        Create a new todo item with auto-incremented ID.

        Args:
            title (str): Required title of the todo
            description (str, optional): Optional description. Defaults to "".

        Returns:
            dict: Dictionary representation of created todo

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        # Create new todo with next available ID
        new_todo = Todo(self.next_id, title.strip(), description.strip() if description else "")
        self.todos[self.next_id] = new_todo

        # Increment next ID for future todos
        self.next_id += 1

        return new_todo.to_dict()

    def view_todos(self):
        """
        Retrieve all existing todo items.

        Returns:
            list: List of all todos as dictionaries, sorted by ID
        """
        # Return all todos as dictionaries, sorted by ID
        todos_list = [todo.to_dict() for todo in self.todos.values()]
        return sorted(todos_list, key=lambda x: x['id'])

    def update_todo(self, todo_id, new_title=None, new_description=None):
        """
        Update an existing todo item.

        Args:
            todo_id (int): ID of the todo to update
            new_title (str, optional): New title (None means no change)
            new_description (str, optional): New description (None means no change)

        Returns:
            dict: Dictionary representation of updated todo

        Raises:
            ValueError: If todo ID doesn't exist or if new title is empty
        """
        if todo_id not in self.todos:
            raise ValueError(f"Todo with ID {todo_id} does not exist")

        todo = self.todos[todo_id]

        # Update title if provided and not empty
        if new_title is not None:
            if not new_title.strip():
                raise ValueError("Title cannot be empty")
            todo.title = new_title.strip()

        # Update description if provided
        if new_description is not None:
            todo.description = new_description.strip() if new_description else ""

        return todo.to_dict()

    def delete_todo(self, todo_id):
        """
        Remove an existing todo item.

        Args:
            todo_id (int): ID of the todo to delete

        Returns:
            bool: True if deleted successfully, False if ID not found
        """
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False

    def get_todo(self, todo_id):
        """
        Get a specific todo by ID.

        Args:
            todo_id (int): ID of the todo to retrieve

        Returns:
            Todo: Todo object if found, None otherwise
        """
        return self.todos.get(todo_id)