"""
Todo model for the In Memory Python Console App.

This module defines the Todo class which represents a single todo item
with id, title, and description attributes.
"""

class Todo:
    """
    Represents a single todo item with id, title, and description.

    Attributes:
        id (int): Unique identifier for the todo
        title (str): Required title of the todo
        description (str): Optional description of the todo
    """

    def __init__(self, id, title, description=""):
        """
        Initialize a Todo instance.

        Args:
            id (int): Unique identifier for the todo
            title (str): Required title of the todo
            description (str, optional): Optional description of the todo. Defaults to "".

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""

    def to_dict(self):
        """
        Convert the Todo instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the Todo with id, title, and description
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }

    def __str__(self):
        """
        String representation of the Todo for display purposes.

        Returns:
            str: Formatted string representation of the Todo
        """
        return f"[{self.id}] {self.title}\n   Description: {self.description if self.description else '(no description)'}"

    def __repr__(self):
        """
        Developer-friendly string representation of the Todo.

        Returns:
            str: Detailed string representation of the Todo
        """
        return f"Todo(id={self.id}, title='{self.title}', description='{self.description}')"