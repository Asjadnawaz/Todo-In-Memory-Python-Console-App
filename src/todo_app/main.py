#!/usr/bin/env python3
"""
Console-based Todo Application
A simple todo app with in-memory storage only
"""

from .cli import TodoAppCLI


def main():
    """Main entry point for the todo application"""
    app = TodoAppCLI()
    app.run()


if __name__ == "__main__":
    main()