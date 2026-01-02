# Quickstart Guide: Todo App

**Feature**: Todo App
**Date**: 2026-01-02

## Getting Started

The Todo App is a simple console-based application that allows you to manage your todo items in memory. All data is stored temporarily and will be lost when you exit the application.

### Running the Application

1. Make sure you have Python 3.x installed
2. Navigate to the project directory
3. Run the application:
   ```bash
   python src/cli/main.py
   ```

### Available Commands

Once the application starts, you'll see a menu with the following options:

1. **Add Todo** - Create a new todo item
2. **View Todos** - See all your current todo items
3. **Update Todo** - Modify an existing todo item
4. **Delete Todo** - Remove a todo item
5. **Exit** - Quit the application

### Basic Usage

#### Adding a Todo
1. Select option 1 from the menu
2. Enter a title for your todo (required)
3. Optionally enter a description
4. Your todo will be saved with an auto-generated ID

#### Viewing Todos
1. Select option 2 from the menu
2. All todos will be displayed with their ID, title, and description
3. If no todos exist, you'll see a message indicating this

#### Updating a Todo
1. Select option 3 from the menu
2. Enter the ID of the todo you want to update
3. Enter a new title (or press Enter to keep the current one)
4. Enter a new description (or press Enter to keep the current one)

#### Deleting a Todo
1. Select option 4 from the menu
2. Enter the ID of the todo you want to delete
3. Confirm the deletion

#### Exiting the Application
1. Select option 5 from the menu
2. The application will terminate and all data will be lost

### Important Notes

- All data is stored in memory only and will be lost when you exit
- Todo IDs are auto-incremented starting from 1
- Titles are required for all todos
- Descriptions are optional
- The application validates all inputs and provides error messages for invalid operations