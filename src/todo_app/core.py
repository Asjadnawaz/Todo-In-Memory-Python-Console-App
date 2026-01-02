"""
Core business logic for the todo application
Handles all operations related to todo items with validation
"""

from typing import List, Optional
from todo_app.models import TodoList, TodoItem


class TodoService:
    """Core business logic service for todo operations"""

    def __init__(self):
        self.todo_list = TodoList()

    def add_todo(self, description: str) -> Optional[int]:
        """
        Add a new todo item with validation
        Returns the ID of the new todo item or None if validation fails
        """
        if not description or not description.strip():
            raise ValueError("Description must be a non-empty string")

        return self.todo_list.add(description)

    def list_todos(self) -> List[TodoItem]:
        """Return all todo items in the list"""
        return self.todo_list.list_all()

    def get_todo(self, todo_id: int) -> Optional[TodoItem]:
        """Get a specific todo item by ID"""
        return self.todo_list.get(todo_id)

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of a todo item with validation
        Returns True if successful, False otherwise
        """
        if not new_description or not new_description.strip():
            raise ValueError("New description must be a non-empty string")

        return self.todo_list.update(todo_id, new_description)

    def mark_complete(self, todo_id: int) -> bool:
        """Mark a todo item as complete"""
        return self.todo_list.mark_complete(todo_id)

    def mark_incomplete(self, todo_id: int) -> bool:
        """Mark a todo item as incomplete"""
        return self.todo_list.mark_incomplete(todo_id)

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item by ID"""
        return self.todo_list.delete(todo_id)

    def count_todos(self) -> int:
        """Return the count of all todo items"""
        return self.todo_list.count()

    def clear_all_todos(self) -> None:
        """Clear all todo items (for testing purposes)"""
        self.todo_list.clear()