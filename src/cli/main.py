"""
Main CLI interface for the In Memory Python Console App.

This module provides the menu-based user interface for todo management operations.
"""

import sys
import os
# Add the src directory to the Python path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.todo_manager import TodoManager


def get_user_input(prompt):
    """
    Get user input with proper handling of potential EOF or interruption.

    Args:
        prompt (str): Prompt message to display to user

    Returns:
        str: User input string, or None if interrupted
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled by user.")
        return None


def get_integer_input(prompt):
    """
    Get integer input from user with validation.

    Args:
        prompt (str): Prompt message to display to user

    Returns:
        int: Valid integer input, or None if interrupted
    """
    while True:
        user_input = get_user_input(prompt)
        if user_input is None:
            return None

        try:
            return int(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            # Continue the loop to ask for input again


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("         TODO APP - MAIN MENU")
    print("="*40)
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Exit")
    print("="*40)


def add_todo_flow(todo_manager):
    """
    Handle the Add Todo user flow.

    Args:
        todo_manager (TodoManager): Instance of TodoManager to use
    """
    print("\n--- Add New Todo ---")

    # Get title from user
    title = get_user_input("Enter todo title (required): ")
    if title is None:
        return

    if not title:
        print("Error: Title cannot be empty.")
        return

    # Get optional description
    description = get_user_input("Enter todo description (optional, press Enter to skip): ")
    if description is None:
        return

    try:
        todo = todo_manager.add_todo(title, description if description else "")
        print(f"Success: Todo added with ID {todo['id']}")
        print(f"  Title: {todo['title']}")
        print(f"  Description: {todo['description'] if todo['description'] else '(no description)'}")
    except ValueError as e:
        print(f"Error: {e}")


def view_todos_flow(todo_manager):
    """
    Handle the View Todos user flow.

    Args:
        todo_manager (TodoManager): Instance of TodoManager to use
    """
    print("\n--- View All Todos ---")
    todos = todo_manager.view_todos()

    if not todos:
        print("No todos available.")
        return

    print(f"Found {len(todos)} todo(s):")
    for todo in todos:
        print(f"\n  [{todo['id']}] {todo['title']}")
        print(f"      Description: {todo['description'] if todo['description'] else '(no description)'}")


def update_todo_flow(todo_manager):
    """
    Handle the Update Todo user flow.

    Args:
        todo_manager (TodoManager): Instance of TodoManager to use
    """
    print("\n--- Update Todo ---")

    # Get todo ID
    todo_id = get_integer_input("Enter the ID of the todo to update: ")
    if todo_id is None:
        return

    # Check if todo exists
    if not todo_manager.get_todo(todo_id):
        print(f"Error: Todo with ID {todo_id} does not exist.")
        return

    # Get new title (optional)
    current_todo = todo_manager.get_todo(todo_id)
    new_title = get_user_input(f"Enter new title (current: '{current_todo.title}', press Enter to keep current): ")
    if new_title is None:
        return

    # If user pressed Enter, keep current title; otherwise, use new title
    if new_title == "":
        new_title = None

    # Get new description (optional)
    new_description = get_user_input(f"Enter new description (current: '{current_todo.description}', press Enter to keep current): ")
    if new_description is None:
        return

    # If user pressed Enter, keep current description; otherwise, use new description
    if new_description == "":
        new_description = None

    try:
        updated_todo = todo_manager.update_todo(todo_id, new_title, new_description)
        print("Success: Todo updated!")
        print(f"  ID: {updated_todo['id']}")
        print(f"  Title: {updated_todo['title']}")
        print(f"  Description: {updated_todo['description'] if updated_todo['description'] else '(no description)'}")
    except ValueError as e:
        print(f"Error: {e}")


def delete_todo_flow(todo_manager):
    """
    Handle the Delete Todo user flow.

    Args:
        todo_manager (TodoManager): Instance of TodoManager to use
    """
    print("\n--- Delete Todo ---")

    # Get todo ID
    todo_id = get_integer_input("Enter the ID of the todo to delete: ")
    if todo_id is None:
        return

    # Attempt to delete todo
    success = todo_manager.delete_todo(todo_id)

    if success:
        print(f"Success: Todo with ID {todo_id} has been deleted.")
    else:
        print(f"Error: Todo with ID {todo_id} does not exist.")


def main():
    """
    Main application loop that provides the CLI menu interface.
    """
    print("Welcome to the In Memory Python Console App!")
    print("All data is stored in memory and will be lost when you exit.")

    todo_manager = TodoManager()

    while True:
        display_menu()
        choice = get_user_input("Select an option (1-5): ")

        if choice is None:
            print("\nGoodbye!")
            break

        if choice == "1":
            add_todo_flow(todo_manager)
        elif choice == "2":
            view_todos_flow(todo_manager)
        elif choice == "3":
            update_todo_flow(todo_manager)
        elif choice == "4":
            delete_todo_flow(todo_manager)
        elif choice == "5":
            print("\nThank you for using the Todo App!")
            print("All data has been lost as expected for in-memory storage.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

    print("Application terminated.")


if __name__ == "__main__":
    main()