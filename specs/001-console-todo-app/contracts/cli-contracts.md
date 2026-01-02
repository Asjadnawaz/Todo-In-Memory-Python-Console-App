# CLI Contracts: Console-Based Todo App

## Command Interface Specifications

### Add Todo Command
- **Interface**: `add(description: str) -> Result[int, Error]`
- **Input**: Non-empty string description of the todo task
- **Output**: Success with new todo item ID, or Error with validation message
- **Side effects**: Adds new TodoItem to in-memory collection
- **Preconditions**: Description is non-empty string
- **Postconditions**: TodoItem exists in collection with completed=False

### View Todos Command
- **Interface**: `list_all() -> List[TodoItem]`
- **Input**: None
- **Output**: List of all TodoItems in collection, sorted by ID
- **Side effects**: None (read-only operation)
- **Preconditions**: None
- **Postconditions**: Returns current state of collection

### Update Todo Command
- **Interface**: `update(todo_id: int, new_description: str) -> Result[bool, Error]`
- **Input**: Valid todo ID and non-empty new description
- **Output**: Success boolean if update succeeded, or Error with validation message
- **Side effects**: Modifies description field of existing TodoItem
- **Preconditions**: TodoItem with ID exists, new description is non-empty
- **Postconditions**: TodoItem description updated in collection

### Delete Todo Command
- **Interface**: `delete(todo_id: int) -> Result[bool, Error]`
- **Input**: Valid todo ID
- **Output**: Success boolean if deletion succeeded, or Error with validation message
- **Side effects**: Removes TodoItem from collection
- **Preconditions**: TodoItem with ID exists
- **Postconditions**: TodoItem no longer exists in collection

### Mark Complete Command
- **Interface**: `mark_complete(todo_id: int) -> Result[bool, Error]`
- **Input**: Valid todo ID
- **Output**: Success boolean if operation succeeded, or Error with validation message
- **Side effects**: Sets completed field to True for specified TodoItem
- **Preconditions**: TodoItem with ID exists
- **Postconditions**: TodoItem completed field is True

### Mark Incomplete Command
- **Interface**: `mark_incomplete(todo_id: int) -> Result[bool, Error]`
- **Input**: Valid todo ID
- **Output**: Success boolean if operation succeeded, or Error with validation message
- **Side effects**: Sets completed field to False for specified TodoItem
- **Preconditions**: TodoItem with ID exists
- **Postconditions**: TodoItem completed field is False

## Error Handling Contracts

### Validation Errors
- **Empty Description**: Return error when description is empty or whitespace-only
- **Invalid ID**: Return error when specified todo_id does not exist
- **Type Mismatch**: Return error when incorrect data types provided

### User Input Processing
- **Interface**: `process_user_input(input: str) -> Command | Error`
- **Responsibility**: Parse user input and route to appropriate command handler
- **Error Handling**: Provide clear error messages for invalid inputs