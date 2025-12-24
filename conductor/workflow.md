# Development Workflow

## 1. Principles
- **Iterative:** We build in small, testable increments.
- **Reliable:** We verify every step with tests and checks.
- **Clean:** We leave the code better than we found it.

## 2. Phase Protocol

### Starting a Phase
1.  **Read the Plan:** Review the `plan.md` for the current phase.
2.  **Verify Context:** Ensure you have the necessary information (designs, requirements).

### Executing Tasks
1.  **Test First:** Create or update a test case that fails.
2.  **Implement:** Write the minimum code to pass the test.
3.  **Refactor:** Clean up the code while keeping tests green.
4.  **Verify:** Run the full test suite and linters.

### Completing a Phase
1.  **Review:** Check against the phase objectives.
2.  **Update Plan:** Mark the phase as complete in `plan.md`.
3.  **Checkpoint:**
    - Run the full test suite.
    - Run the linter.
    - Commit all changes.

## 3. Task Protocol

### Starting a Task
1.  **Update Plan:** Mark the task as `[in progress]` in `plan.md`.
2.  **Context Check:** Review relevant files and previous work.

### Execution Loop
1.  **Write/Update Test:** Ensure a failing test exists for the new functionality.
2.  **Implement:** Write code to pass the test.
3.  **Verify:** Run the specific test and ensure it passes.
4.  **Refactor:** Optimize and clean the code.
5.  **Coverage Check:** Ensure test coverage is >80%.

### Finishing a Task
1.  **Linter Check:** Run the project's linter (e.g., `ruff`, `eslint`).
2.  **Full Test Suite:** Run all tests to ensure no regressions.
3.  **Commit:**
    - Stage changes: `git add .`
    - Commit with standard message: `git commit -m "feat: <task description>"`
    - Add context (optional but recommended): `git notes add -m "<detailed summary>"`
4.  **Update Plan:** Mark the task as `[x]` (completed) in `plan.md`.
