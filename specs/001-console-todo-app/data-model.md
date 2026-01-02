# Data Model: Console-Based Todo App

## Core Entity: TodoItem

### Fields
- **id**: int - Unique identifier for the todo item (auto-generated)
- **description**: str - Text description of the task (required, non-empty)
- **completed**: bool - Completion status (default: False)
- **created_at**: datetime - Timestamp when item was created (auto-generated)

### Validation Rules
- **description**: Must be a non-empty string (length > 0)
- **id**: Must be unique within the collection
- **completed**: Boolean value only (True/False)

### State Transitions
- **Initial State**: completed = False
- **Mark Complete**: completed transitions from False → True
- **Mark Incomplete**: completed transitions from True → False (optional functionality)

## In-Memory Storage Model

### TodoList Container
- **data structure**: List[TodoItem] or Dict[int, TodoItem]
- **operations**: add, remove, update, get, list all
- **persistence**: None (in-memory only, cleared on application exit)

### Collection Constraints
- **size limit**: Up to 1000 items (per success criteria)
- **access pattern**: Index-based operations for updates/deletes
- **uniqueness**: Each TodoItem has unique id