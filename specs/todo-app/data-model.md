# Data Model: Todo App

**Feature**: Todo App
**Date**: 2026-01-02
**Input**: Feature specification from `/specs/todo-app/spec.md`

## Todo Entity

### Attributes

- **id**: Integer
  - Type: int
  - Constraints: Auto-incremented, unique, positive
  - Required: Yes
  - Description: Unique identifier for each todo item

- **title**: String
  - Type: str
  - Constraints: Required, non-empty
  - Required: Yes
  - Description: Title of the todo item

- **description**: String
  - Type: str
  - Constraints: Optional
  - Required: No
  - Default: Empty string
  - Description: Optional description of the todo item

### In-Memory Storage Structure

The todos will be stored in a Python dictionary where:
- Keys: Integer IDs (auto-incremented)
- Values: Todo objects or dictionaries containing the todo attributes

Example structure:
```python
{
    1: {"id": 1, "title": "Sample todo", "description": "Sample description"},
    2: {"id": 2, "title": "Another todo", "description": ""},
    3: {"id": 3, "title": "Third todo", "description": "Detailed description here"}
}
```

### Auto-Increment ID Management

- Start ID counter at 1
- Increment by 1 for each new todo
- Track the next available ID in memory
- Ensure ID uniqueness across all operations

## Data Operations

### Create
- Accept title (required) and description (optional)
- Generate next available ID
- Create new todo entry in storage
- Return created todo with assigned ID

### Read (All)
- Return all todos from storage
- Format for display to user

### Read (Single by ID)
- Accept todo ID
- Return specific todo if exists
- Return None/error if ID not found

### Update
- Accept todo ID and new values
- Update only non-empty values (preserve existing if empty)
- Return updated todo or error if ID not found

### Delete
- Accept todo ID
- Remove from storage if exists
- Return success/failure status