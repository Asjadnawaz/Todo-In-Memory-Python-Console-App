#!/usr/bin/env python3
"""
Basic test script to verify the todo application functionality
"""

import sys
import os

# Add src to path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.models import TodoItem, TodoList
from todo_app.core import TodoService
from todo_app.cli import TodoAppCLI


def test_models():
    """Test the basic models functionality"""
    print("Testing models...")

    # Test TodoItem creation
    try:
        item = TodoItem("Test task")
        assert item.description == "Test task"
        assert item.completed == False
        print("✓ TodoItem creation works")
    except Exception as e:
        print(f"✗ TodoItem creation failed: {e}")
        return False

    # Test TodoList operations
    try:
        todo_list = TodoList()

        # Add item
        id1 = todo_list.add("First task")
        assert todo_list.count() == 1
        print("✓ TodoList add works")

        # Get item
        item = todo_list.get(id1)
        assert item is not None
        assert item.description == "First task"
        print("✓ TodoList get works")

        # Update item
        success = todo_list.update(id1, "Updated task")
        assert success == True
        item = todo_list.get(id1)
        assert item.description == "Updated task"
        print("✓ TodoList update works")

        # Mark complete
        success = todo_list.mark_complete(id1)
        assert success == True
        item = todo_list.get(id1)
        assert item.completed == True
        print("✓ TodoList mark_complete works")

        # Delete item
        success = todo_list.delete(id1)
        assert success == True
        assert todo_list.count() == 0
        print("✓ TodoList delete works")

        print("✓ All model tests passed!")
        return True
    except Exception as e:
        print(f"✗ TodoList test failed: {e}")
        return False


def test_core_service():
    """Test the core service functionality"""
    print("\nTesting core service...")

    try:
        service = TodoService()

        # Test adding a todo
        todo_id = service.add_todo("Test task for service")
        assert todo_id is not None
        print("✓ Service add_todo works")

        # Test listing todos
        todos = service.list_todos()
        assert len(todos) == 1
        print("✓ Service list_todos works")

        # Test getting a specific todo
        todo = service.get_todo(todo_id)
        assert todo is not None
        assert todo.description == "Test task for service"
        print("✓ Service get_todo works")

        # Test updating a todo
        success = service.update_todo(todo_id, "Updated test task")
        assert success == True
        todo = service.get_todo(todo_id)
        assert todo.description == "Updated test task"
        print("✓ Service update_todo works")

        # Test marking complete
        success = service.mark_complete(todo_id)
        assert success == True
        todo = service.get_todo(todo_id)
        assert todo.completed == True
        print("✓ Service mark_complete works")

        # Test deleting a todo
        success = service.delete_todo(todo_id)
        assert success == True
        assert service.count_todos() == 0
        print("✓ Service delete_todo works")

        print("✓ All core service tests passed!")
        return True
    except Exception as e:
        print(f"✗ Core service test failed: {e}")
        return False


def test_cli_creation():
    """Test that CLI can be instantiated"""
    print("\nTesting CLI creation...")

    try:
        cli = TodoAppCLI()
        assert cli is not None
        print("✓ CLI instantiation works")
        print("✓ All CLI tests passed!")
        return True
    except Exception as e:
        print(f"✗ CLI test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("Running basic functionality tests for Todo App...\n")

    results = []
    results.append(test_models())
    results.append(test_core_service())
    results.append(test_cli_creation())

    print(f"\n{'='*50}")
    print(f"Test Results: {sum(results)}/{len(results)} passed")

    if all(results):
        print("🎉 All tests passed! The application is working correctly.")
        print("\nTo run the application, use:")
        print("  python -m src.todo_app")
        print("or")
        print("  uv run python -m src.todo_app")
    else:
        print("❌ Some tests failed. Please check the implementation.")

    return all(results)


if __name__ == "__main__":
    main()