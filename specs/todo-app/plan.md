# Implementation Plan: Todo App

**Branch**: `todo-app` | **Date**: 2026-01-02 | **Spec**: [link to spec]
**Input**: Feature specification from `/specs/todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a menu-based Todo CLI application that stores all data in memory. The application will provide functionality to add, view, update, and delete todo items with proper validation and error handling, following the constitution principles of clean code, separation of concerns, and in-memory storage only.

## Technical Context

**Language/Version**: Python 3.x
**Primary Dependencies**: Standard library only (sys, os, etc.)
**Storage**: In-memory only (dict/list data structures)
**Testing**: unittest module for unit tests
**Target Platform**: Cross-platform console application
**Project Type**: Single console application
**Performance Goals**: Fast in-memory operations, <100ms response time
**Constraints**: No external dependencies, PEP 8 compliance, beginner-friendly code structure
**Scale/Scope**: Single user, local todo management

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. **Clean and Readable Python Code**: Implementation must follow PEP 8 guidelines with consistent formatting and clear documentation
2. **Beginner-Friendly Structure**: Code organization must be intuitive and include comprehensive comments for complex logic
3. **Separation of Concerns**: CLI interface must be strictly separated from business logic with independent testability
4. **Defensive Programming**: All user inputs must be validated with appropriate error handling
5. **In-Memory Storage Only**: No files or databases allowed - all data storage must be in-memory
6. **No External Libraries**: Only standard Python library functions permitted
7. **Explicit Feature Scope**: Only features explicitly defined in requirements may be implemented

## Project Structure

### Documentation (this feature)

```text
specs/todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── todo.py          # Todo class definition
├── services/
│   └── todo_manager.py  # Business logic for todo operations
└── cli/
    └── main.py          # Main CLI interface

tests/
├── unit/
│   ├── test_todo.py     # Todo model tests
│   └── test_todo_manager.py  # Todo manager tests
└── integration/
    └── test_cli_flow.py # CLI integration tests
```

**Structure Decision**: Single project structure with clear separation between models, services, and CLI components as defined above.

## Detailed Implementation Plan

### Core Modules and Responsibilities

1. **Todo Model** (`src/models/todo.py`)
   - Represents a single todo item
   - Contains id, title, and description attributes
   - Provides validation for required fields
   - Includes string representation for display

2. **Todo Manager** (`src/services/todo_manager.py`)
   - Manages in-memory storage of todos
   - Provides CRUD operations (add, view, update, delete)
   - Handles ID auto-increment logic
   - Implements business logic validation

3. **CLI Interface** (`src/cli/main.py`)
   - Provides menu-based user interface
   - Handles user input and validation
   - Coordinates with Todo Manager for operations
   - Formats and displays output to user

### In-Memory Data Structure

Todos will be stored in a Python dictionary where:
- Keys: Integer IDs (auto-incremented starting from 1)
- Values: Todo objects containing id, title, and description

```python
{
    1: {"id": 1, "title": "Sample todo", "description": "Sample description"},
    2: {"id": 2, "title": "Another todo", "description": ""},
    3: {"id": 3, "title": "Third todo", "description": "Detailed description here"}
}
```

The next available ID will be tracked separately to ensure uniqueness.

### Function-Level Design

#### add_todo(title: str, description: str = "") -> dict
- **Purpose**: Create a new todo item with auto-incremented ID
- **Parameters**:
  - title (str): Required title of the todo
  - description (str): Optional description (defaults to empty string)
- **Returns**: Dictionary representation of created todo
- **Validation**:
  - Title must not be empty or None
  - If validation fails, raise ValueError with appropriate message
- **Logic**:
  - Validate title is not empty
  - Generate next available ID
  - Create new todo with provided data
  - Store in in-memory dictionary
  - Return created todo

#### view_todos() -> list
- **Purpose**: Retrieve all existing todo items
- **Parameters**: None
- **Returns**: List of all todos as dictionaries
- **Logic**:
  - Return all todos from in-memory storage
  - If no todos exist, return empty list
  - Format for display (e.g., sorted by ID)

#### update_todo(todo_id: int, new_title: str = None, new_description: str = None) -> dict
- **Purpose**: Update an existing todo item
- **Parameters**:
  - todo_id (int): ID of the todo to update
  - new_title (str): New title (optional, None means no change)
  - new_description (str): New description (optional, None means no change)
- **Returns**: Dictionary representation of updated todo
- **Validation**:
  - Todo ID must exist in storage
  - If title is provided, it must not be empty
- **Logic**:
  - Verify todo exists
  - Update only non-None values (preserve existing if None provided)
  - If new title is empty, raise ValueError
  - Update todo in storage
  - Return updated todo

#### delete_todo(todo_id: int) -> bool
- **Purpose**: Remove an existing todo item
- **Parameters**:
  - todo_id (int): ID of the todo to delete
- **Returns**: Boolean indicating success (True if deleted, False if ID not found)
- **Validation**: Todo ID must exist in storage
- **Logic**:
  - Verify todo exists
  - Remove from in-memory storage
  - Return success status

### CLI Menu Flow and User Interaction

The main CLI flow will be a loop that:
1. Displays the main menu with options:
   - 1. Add Todo
   - 2. View Todos
   - 3. Update Todo
   - 4. Delete Todo
   - 5. Exit
2. Prompts user for menu selection
3. Validates input is a number 1-5
4. Executes corresponding function based on selection
5. Displays results or error messages appropriately
6. Returns to main menu unless exit is selected

#### Add Todo Flow:
- Prompt user for title
- Validate title is not empty
- Prompt for optional description (press Enter to skip)
- Call add_todo function
- Display success message with created todo details

#### View Todos Flow:
- Call view_todos function
- If list is empty, display "No todos available"
- Otherwise, display formatted list with ID, title, and description

#### Update Todo Flow:
- Prompt for todo ID
- Validate ID exists
- Prompt for new title (press Enter to keep current)
- Prompt for new description (press Enter to keep current)
- Call update_todo function
- Display success message with updated todo details

#### Delete Todo Flow:
- Prompt for todo ID
- Validate ID exists
- Call delete_todo function
- Display success message

#### Exit Flow:
- Break out of main loop
- Display goodbye message
- Terminate program

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [No violations identified] | [All requirements align with constitution] |