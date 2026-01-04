"""
CLI interface module for the todo application
Handles user input and output, menu display, and command routing
"""

from typing import Optional
import signal
import sys
from .core import TodoService


class TodoAppCLI:
    """Command Line Interface for the todo application"""

    def __init__(self):
        self.service = TodoService()
        self.running = True
        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signum, frame):
        """Handle interruption signals (Ctrl+C)"""
        print("\n\nReceived interrupt signal. Goodbye!")
        sys.exit(0)

    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Mark Todo Complete")
        print("4. Update Todo")
        print("5. Delete Todo")
        print("6. Exit")
        print("="*50)

    def get_user_choice(self) -> str:
        """Get user's menu choice"""
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return "6"  # Exit choice

    def handle_add_todo(self):
        """Handle adding a new todo"""
        try:
            description = input("Enter todo description: ").strip()
            if not description:
                print("Error: Description cannot be empty.")
                return

            # Validate special characters if needed (though Python handles them well)
            todo_id = self.service.add_todo(description)
            print(f"Todo added successfully with ID: {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error adding todo: {e}")

    def handle_view_todos(self):
        """Handle viewing all todos"""
        try:
            todos = self.service.list_todos()

            if not todos:
                print("\nNo todos found.")
                return

            print(f"\nTotal todos: {len(todos)}")
            print("-" * 50)
            for todo in todos:
                print(todo)
        except Exception as e:
            print(f"Unexpected error viewing todos: {e}")

    def handle_mark_complete(self):
        """Handle marking a todo as complete"""
        try:
            if self.service.count_todos() == 0:
                print("No todos available to mark complete.")
                return

            todo_id = input("Enter todo ID to mark complete: ").strip()
            if not todo_id:
                print("Error: Please enter a valid todo ID.")
                return

            try:
                todo_id = int(todo_id)
            except ValueError:
                print("Error: Please enter a valid todo ID (number).")
                return

            success = self.service.mark_complete(todo_id)
            if success:
                print(f"Todo {todo_id} marked as complete.")
            else:
                print(f"Error: Todo with ID {todo_id} not found.")
        except Exception as e:
            print(f"Unexpected error marking todo complete: {e}")

    def handle_update_todo(self):
        """Handle updating a todo description"""
        try:
            if self.service.count_todos() == 0:
                print("No todos available to update.")
                return

            todo_id = input("Enter todo ID to update: ").strip()
            if not todo_id:
                print("Error: Please enter a valid todo ID.")
                return

            try:
                todo_id = int(todo_id)
            except ValueError:
                print("Error: Please enter a valid todo ID (number).")
                return

            todo = self.service.get_todo(todo_id)
            if not todo:
                print(f"Error: Todo with ID {todo_id} not found.")
                return

            new_description = input(f"Enter new description (current: {todo.description}): ").strip()
            if not new_description:
                print("Error: Description cannot be empty.")
                return

            success = self.service.update_todo(todo_id, new_description)
            if success:
                print(f"Todo {todo_id} updated successfully.")
            else:
                print(f"Error updating todo {todo_id}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error updating todo: {e}")

    def handle_delete_todo(self):
        """Handle deleting a todo"""
        try:
            if self.service.count_todos() == 0:
                print("No todos available to delete.")
                return

            todo_id = input("Enter todo ID to delete: ").strip()
            if not todo_id:
                print("Error: Please enter a valid todo ID.")
                return

            try:
                todo_id = int(todo_id)
            except ValueError:
                print("Error: Please enter a valid todo ID (number).")
                return

            success = self.service.delete_todo(todo_id)
            if success:
                print(f"Todo {todo_id} deleted successfully.")
            else:
                print(f"Error: Todo with ID {todo_id} not found.")
        except Exception as e:
            print(f"Unexpected error deleting todo: {e}")

    def run(self):
        """Main application loop"""
        print("Welcome to the Todo Application!")

        while self.running:
            try:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == "1":
                    self.handle_add_todo()
                elif choice == "2":
                    self.handle_view_todos()
                elif choice == "3":
                    self.handle_mark_complete()
                elif choice == "4":
                    self.handle_update_todo()
                elif choice == "5":
                    self.handle_delete_todo()
                elif choice == "6":
                    print("Goodbye!")
                    self.running = False
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
                    print("Available commands: 1-Add, 2-View, 3-Mark Complete, 4-Update, 5-Delete, 6-Exit")

                if choice != "6":
                    input("\nPress Enter to continue...")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Unexpected error in main loop: {e}")
                input("\nPress Enter to continue...")