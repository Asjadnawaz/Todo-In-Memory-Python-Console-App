# Console-Based Todo App

A simple, in-memory todo application built with Python for educational purposes. This application demonstrates spec-driven development and provides core todo functionality through a console interface.

## Features

- Add new todo items
- View all todo items
- Mark todo items as complete
- Update todo descriptions
- Delete todo items
- All data stored in-memory (no persistence)

## Requirements

- Python 3.13+
- UV package manager

## Installation

1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Usage

Run the application:
```bash
uv run python -m src.todo_app
```

## Project Structure

```
src/
└── todo_app/
    ├── __init__.py
    ├── main.py          # Application entry point
    ├── models.py        # TodoItem data model
    ├── core.py          # Business logic for todo operations
    └── cli.py           # Console interface and user interaction
```

## Architecture

- **Models**: TodoItem and TodoList classes handle data representation and storage
- **Core**: TodoService provides business logic for todo operations
- **CLI**: TodoAppCLI handles user interface and command routing
- **In-Memory Storage**: All data is stored in memory and cleared when the application exits

## Design Principles

- Clean separation of concerns
- Modular architecture
- Input validation and error handling
- Beginner-friendly code structure