from datetime import datetime
from typing import List, Optional, Dict
import uuid


class TodoItem:
    """Represents a single todo item with properties including description and completion status"""

    def __init__(self, description: str, completed: bool = False):
        if not description or not description.strip():
            raise ValueError("Description must be a non-empty string")

        self.id: int = int(uuid.uuid4().int)  # Using UUID to generate unique IDs
        self.description: str = description.strip()
        self.completed: bool = completed
        self.created_at: datetime = datetime.now()

    def __str__(self) -> str:
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}: {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"


class TodoList:
    """In-memory storage model for todo items with basic CRUD operations"""

    def __init__(self):
        self._todos: Dict[int, TodoItem] = {}

    def add(self, description: str) -> int:
        """Add a new todo item with the given description and return its ID"""
        todo = TodoItem(description)
        self._todos[todo.id] = todo
        return todo.id

    def get(self, todo_id: int) -> Optional[TodoItem]:
        """Get a todo item by its ID"""
        return self._todos.get(todo_id)

    def update(self, todo_id: int, new_description: str) -> bool:
        """Update the description of an existing todo item"""
        if todo_id not in self._todos:
            return False

        if not new_description or not new_description.strip():
            return False

        self._todos[todo_id].description = new_description.strip()
        return True

    def mark_complete(self, todo_id: int) -> bool:
        """Mark a todo item as complete"""
        if todo_id not in self._todos:
            return False

        self._todos[todo_id].completed = True
        return True

    def mark_incomplete(self, todo_id: int) -> bool:
        """Mark a todo item as incomplete"""
        if todo_id not in self._todos:
            return False

        self._todos[todo_id].completed = False
        return True

    def delete(self, todo_id: int) -> bool:
        """Delete a todo item by its ID"""
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True

    def list_all(self) -> List[TodoItem]:
        """Return a list of all todo items, sorted by ID"""
        return sorted(self._todos.values(), key=lambda x: x.id)

    def count(self) -> int:
        """Return the count of all todo items"""
        return len(self._todos)

    def clear(self) -> None:
        """Clear all todo items (for testing purposes)"""
        self._todos.clear()