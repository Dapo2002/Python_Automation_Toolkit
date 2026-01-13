 Defensive Programming, Exception Handling & Diagnostics

This module focuses on "Code Reliability"—moving beyond basic logic to handle errors, validate data, and monitor execution state. These scripts demonstrate how to catch bugs during development and handle userinduced errors at runtime.



 📂 Featured Scripts

 1. Traffic Light Safety Controller (`stoplight_assert.py`)
 Concept: Invariant Enforcement.
 Logic: Uses `assert` to ensure that at least one direction in a 4way intersection is always 'red'. If the logic fails, the program halts to prevent a "virtual accident."
 Key Tool: `assert` statements for internal logic validation.

 2. Geometric Exception Handler (`box_print.py`)
 Concept: User Input Validation.
 Logic: Generates hollow ASCII boxes but "raises" custom exceptions if the input symbol is too long or the dimensions are too small to be physically possible.
 Key Tool: `raise Exception` and `try...except` blocks for graceful failure.

 3. Coin Toss Debugger (`coin_toss_fixed.py`)
 Concept: Type Parity & Logical Mapping.
 Logic: Fixes a "Silent Bug" where integers ($0, 1$) were compared to strings ($'heads', 'tails'$). Implements a logical bridge to synchronize computer state with user input.
 Key Tool: Boolean compound logic and input validation loops.

 4. Factorial Diagnostics Engine (`factorial_logging.py`)
 Concept: Execution Observability.
 Logic: Calculates $n!$ while maintaining a "Black Box" flight record of every variable change, timestamped and categorized by severity.
 Key Tool: `logging` module with custom `basicConfig` formatting.

 5. Call Stack Explorer (`stack_trace_demo.py`)
 Concept: Exception Propagation.
 Logic: Intentionally triggers an error in a nested function to demonstrate how exceptions "bubble up" through the call stack.
 Key Tool: Traceback analysis and function frame hierarchy.



 🛠️ Technical Competencies

| Feature | Implementation | Purpose |
| : | : | : |
| Assertions | `assert condition, message` | Catching developmenttime logic flaws. |
| Custom Exceptions | `raise Exception('msg')` | Preventing functions from running with invalid data. |
| Error Handling | `try...except Exception as e` | Keeping the program running even when an error occurs. |
| Logging | `logging.debug()` | Tracking program state without using `print()` clutter. |
| Data Normalization | `input().lower()` | Reducing user input errors (case sensitivity). |



 🚀 The Debugging Workflow
1. Assertion: Check that "impossible" states never happen.
2. Validation: Ensure user inputs meet geometric or logical requirements.
3. Logging: Observe the variables in their natural habitat as the code runs.
4. Handling: Wrap risky operations in safety nets to ensure system uptime.