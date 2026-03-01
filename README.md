# ⚛️ PROJECT CHRONOS: Local Intelligence

## PART 1: System Directives (Agent Manual)
- **Role**: Senior Python Engineer & Architect.
- **Language**: Python 3.11+ (Strict type hinting preferred).
- **Validation**: Every new function MUST have a corresponding test in the same file or a `tests/` directory.
- **Cleanup**: If you find `.tmp`, `.log`, or duplicate `.py` files that are not referenced in the main logic, DELETE them.
- **Git**: Use the format "Agent [Task Name]: [Brief Description]" for all commit messages.

## PART 2: Project Specifications (The Mission)
- **Objective**: Build a CLI tool that manages local Markdown notes and tracks "Pending" vs "Done" tasks within those notes.
- **Core Components**:
    1. `engine.py`: Logic to scan the workspace for `.md` files.
    2. `parser.py`: Functions to extract lines starting with `[ ]` (todo) and `[x]` (done).
    3. `reporting.py`: Generate a `status.json` that summarizes total tasks across all files.
- **Current Sprint**: 
    - Task 1: Create `engine.py` with a function `find_markdown_files(path)`.
    - Task 2: Create a basic test to verify it finds at least one file.
