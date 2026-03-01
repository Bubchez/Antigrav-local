# ⚛️ PROJECT CHRONOS: Master Directives

## PART 1: System Directives (Agent Manual)
- **Role**: Senior Autonomous Engineer.
- **Permissions**: Refactor, Test, and DELETE redundant/junk files.
- **Protected**: README.md, app.py, and .gitignore are IMMUNE to deletion.
- **Git**: Every success must be pushed to 'main'.

## PART 2: Project Specifications (The Mission)
- **Objective**: Build a Python-based CLI tool to manage local notes.
- **Core Components**:
    1. `engine.py`: Scans workspace for markdown files.
    2. `parser.py`: Extracts `[ ]` tasks from those files.
    3. `reporting.py`: Saves a summary to `status.json`.
- **Current Task**: Initialize `engine.py` with a markdown file finder.
