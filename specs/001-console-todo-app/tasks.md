---
description: "Task list for console-based todo app implementation"
---

# Tasks: Console-Based Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with src/todo_app/ directory
- [x] T002 Initialize pyproject.toml for UV-based Python project
- [x] T003 [P] Create __init__.py files in src/todo_app/

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create TodoItem model in src/todo_app/models.py with id, description, completed, created_at fields
- [x] T005 Create in-memory TodoList container in src/todo_app/models.py with add, remove, update, get, list_all operations
- [x] T006 [P] Create main.py entry point in src/todo_app/main.py
- [x] T007 Create core business logic module in src/todo_app/core.py with validation functions
- [x] T008 Create CLI interface module in src/todo_app/cli.py with menu display functions

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list with validation

**Independent Test**: Can be fully tested by starting the console app, entering the add command, providing a task description, and verifying the task appears in the list.

### Implementation for User Story 1

- [x] T009 [P] [US1] Implement add_todo function in src/todo_app/core.py that validates description and adds to TodoList
- [x] T010 [P] [US1] Implement add_todo_command in src/todo_app/cli.py to handle user input for adding tasks
- [x] T011 [US1] Update main.py to include Add Todo command in the menu system
- [x] T012 [US1] Add input validation for empty descriptions in add flow
- [x] T013 [US1] Add success/error feedback for add operation in CLI

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Enable users to view all their todo items in a readable format

**Independent Test**: Can be fully tested by adding a few tasks and then viewing the complete list to verify all tasks are displayed correctly.

### Implementation for User Story 2

- [x] T014 [P] [US2] Implement list_todos function in src/todo_app/core.py that returns all todos from TodoList
- [x] T015 [P] [US2] Implement view_todos_command in src/todo_app/cli.py to display the todo list
- [x] T016 [US2] Update main.py to include View Todo List command in the menu system
- [x] T017 [US2] Add formatting for displaying todos with ID, description, and completion status
- [x] T018 [US2] Add message display when no todos exist

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Complete (Priority: P2)

**Goal**: Enable users to mark todo items as complete to track progress

**Independent Test**: Can be fully tested by adding a task, marking it as complete, and verifying its status changes in the view.

### Implementation for User Story 3

- [x] T019 [P] [US3] Implement mark_complete function in src/todo_app/core.py that updates completion status
- [x] T020 [P] [US3] Implement mark_complete_command in src/todo_app/cli.py to handle marking tasks complete
- [x] T021 [US3] Update main.py to include Mark Complete command in the menu system
- [x] T022 [US3] Add validation to ensure todo item exists before marking complete
- [x] T023 [US3] Add success/error feedback for mark complete operation

**Checkpoint**: User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo Description (Priority: P2)

**Goal**: Enable users to update the description of their existing todo items

**Independent Test**: Can be fully tested by adding a task, updating its description, and verifying the change persists when viewing the list.

### Implementation for User Story 4

- [x] T024 [P] [US4] Implement update_todo function in src/todo_app/core.py that validates and updates todo description
- [x] T025 [P] [US4] Implement update_todo_command in src/todo_app/cli.py to handle updating task descriptions
- [x] T026 [US4] Update main.py to include Update Todo command in the menu system
- [x] T027 [US4] Add validation to ensure todo item exists and new description is not empty
- [x] T028 [US4] Add success/error feedback for update operation

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Enable users to delete todo items that are no longer relevant

**Independent Test**: Can be fully tested by adding a task, deleting it, and verifying it no longer appears when viewing the list.

### Implementation for User Story 5

- [x] T029 [P] [US5] Implement delete_todo function in src/todo_app/core.py that removes todo from TodoList
- [x] T030 [P] [US5] Implement delete_todo_command in src/todo_app/cli.py to handle deleting tasks
- [x] T031 [US5] Update main.py to include Delete Todo command in the menu system
- [x] T032 [US5] Add validation to ensure todo item exists before deletion
- [x] T033 [US5] Add success/error feedback for delete operation

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T034 [P] Add comprehensive error handling for invalid user inputs across all commands
- [x] T035 [P] Add input validation for all user-facing functions to handle edge cases
- [x] T036 Add graceful handling of interruption signals (Ctrl+C) in main.py
- [x] T037 [P] Improve CLI user experience with better prompts and messages
- [x] T038 Add special character handling in todo descriptions
- [x] T039 [P] Add command not found handling in CLI interface
- [x] T040 Run quickstart validation to ensure all features work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_todo function in src/todo_app/core.py that validates description and adds to TodoList"
Task: "Implement add_todo_command in src/todo_app/cli.py to handle user input for adding tasks"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence