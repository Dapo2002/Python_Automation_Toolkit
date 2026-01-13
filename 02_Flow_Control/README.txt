 Python Fundamentals: Loop Logic & Game State

This repository contains three foundational Python scripts that explore different methods of program flow control. Each script demonstrates a unique approach to handling user input, managing loops, and implementing gamewinning conditions.



 📂 Project Overview

 1. Guessing Game (`for` loop)
An implementation of a numeric search game where the iteration count is strictly defined.
 Logic: Uses a deterministic `for` loop with a `range` object.
 Key Concept: Early termination via the `break` keyword when the winning condition is met.

 2. Guessing Game (`while` loop)
A refactored version of the guessing game utilizing conditional state management.
 Logic: The loop runs based on a compound Boolean expression (`while guess != secretNumber and guessTaken < 6`).
 Key Concept: Maintaining state variables outside the loop scope.

 3. Rock, Paper, Scissors
A robust, persistent CLI game featuring an "infinite" game loop and score tracking.
 Logic: Employs nested `while True` loops—one for the game session and one for input validation.
 Key Concept: Use of `sys.exit()` for clean process termination and randomized AI decisionmaking via `random.randint`.



 🛠️ Logic Comparison Table

| Feature | Guessing Game (For) | Guessing Game (While) | Rock, Paper, Scissors |
| : | : | : | : |
| Primary Loop | `for i in range()` | `while condition:` | `while True:` |
| Input Handling | Integer Casting | Integer Casting | String Validation |
| Exit Strategy | Countbased / Break | Conditionbased | `sys.exit()` / Manual |
| Randomness | `randint(1, 20)` | `randint(1, 20)` | `randint(1, 3)` |



 🚀 Execution
To run any of the scripts, ensure you have a Python 3 environment configured:

```bash
python guessing_game_for.py
python guessing_game_while.py
python rps_game.py