 Python Exploration: Math, Exceptions, and Animations

A collection of scripts focusing on mathematical conjectures, defensive programming (exception handling), and terminalbased visual output.



 📂 Scripts in this Section

 1. The Collatz Sequence (`collatz.py`)
An implementation of the "3n + 1" problem, a famous mathematical mystery. 
 Logic: If even, divide by 2; if odd, multiply by 3 and add 1.
 Feature: Includes input validation to ensure the sequence only runs on positive integers.
 Goal: Demonstrate how a simple algorithm can lead to complex, unpredictable paths before inevitably reaching 1.

 2. Defensive Division (`division_test.py`)
A study in program stability and handling the "unthinkable"—dividing by zero.
 Logic: A functional wrapper for division operations.
 Feature: Uses a `try/except` block to catch `ValueError` (bad input) and `ZeroDivisionError` (math error).
 Goal: Prevents the program from crashing when it encounters invalid data.

 3. ZigZag Animation (`zigzag.py`)
A script that turns the CLI into a dynamic canvas using basic physics logic.
 Logic: Uses an oscillating counter to "bounce" a string of asterisks across the screen.
 Feature: Handles `KeyboardInterrupt` (Ctrl+C) gracefully to exit with a custom message.
 Goal: Demonstrates timing control (`time.sleep`) and stateswitching for visual output.



 🛠️ Concepts Covered

 Mathematical Algorithms: Translating abstract theory into executable code.
 Defensive Programming: Using `try/except` to build crashresistant applications.
 Process Control: Managing loop timing and graceful system exits via `sys.exit`.
 State Toggling: Using booleans to flip directions in a sequence (the "bounce" effect).



 🚀 Usage
Run these scripts using Python 3:
```bash
python collatz.py
python division_test.py
python zigzag.py