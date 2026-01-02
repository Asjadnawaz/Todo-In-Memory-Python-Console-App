# Quickstart Guide: Console-Based Todo App

## Project Setup

### Prerequisites
- Python 3.13+
- UV package manager

### Installation
1. Clone or create the project directory
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   uv run python -m src.todo_app
   ```

## Project Structure
```
todo-app/
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── main.py          # Application entry point
│       ├── models.py        # TodoItem data model
│       ├── core.py          # Business logic
│       └── cli.py           # Console interface
├── tests/                   # Test files (to be created)
├── pyproject.toml          # Project configuration
└── README.md
```

## Running the Application

### Basic Execution
```bash
# Run the console application
uv run python -m src.todo_app
```

### Expected Console Flow
1. Application starts and displays main menu
2. User selects an option (Add, View, Update, Delete, Mark Complete)
3. Application prompts for required input
4. Operation is performed and result is displayed
5. Return to main menu or exit

## Development Commands

### Running Tests
```bash
uv run pytest
```

### Running with Debug Mode
```bash
# To be configured based on implementation
```

## Key Components

### TodoItem Model
- Core data structure with id, description, completed status
- Validation for non-empty descriptions
- Auto-generated timestamps

### Core Business Logic
- In-memory storage using Python collections
- Operations: add, list, update, delete, mark complete/incomplete
- Input validation and error handling

### CLI Interface
- Menu-driven console interface
- Command parsing and routing
- User input validation
- Error message display

## First Steps for Implementation

1. Create the TodoItem model with validation
2. Implement the core in-memory storage operations
3. Build the CLI interface with menu system
4. Add error handling for edge cases
5. Write tests for each component