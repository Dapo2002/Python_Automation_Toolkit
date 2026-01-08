 Input Validation & CLI Interface Design

This section explores the transition from "internal logic" to "userfacing applications." These scripts demonstrate how to use the `pyinputplus` library and manual logic to create robust, errorresistant Command Line Interfaces (CLIs).



 📂 Featured Scripts

 1. Recursive Logic Loop (`idiot_loop.py`)
 Concept: Interactive Flow Control.
 Logic: Uses `inputYesNo` to create a humorous infinite loop that only terminates upon specific user consent.
 Key Tool: Casenormalization and automatic reprompting.

 2. Manual Exception Handler (`age_check.py`)
 Concept: Defensive Programming.
 Logic: Replicates highlevel validation using `try/except` blocks to catch `ValueError` during typecasting.
 Technique: Implements boundary checking to ensure data is logically sound (Age > 0).

 3. Custom Logic Validator (`sum_ten.py`)
 Concept: Algorithmic Constraints.
 Logic: Uses `inputCustom` to pass user input into a specialized function that enforces a mathematical rule (digits must sum to 10).
 Key Tool: Raising custom `Exception` messages for granular user feedback.

 4. Timed Quiz Engine (`math_quiz.py`)
 Concept: Gamification & Concurrency.
 Logic: A multitry, timed arithmetic trainer using `timeout` and `limit` parameters to enforce speed and accuracy.
 Feature: Uses `allowRegexes` to whitelist only the correct mathematical product.

 5. Sandwich POS System (`sandwich_pos.py`)
 Concept: Decision Tree UI.
 Logic: A full ordering workflow using `inputMenu` and conditional branching to build a dynamic list of ingredients.
 Feature: Formatted receipt output using fstring alignment for professional terminal layouts.



 🛠️ Technical Competencies

| Feature | Implementation | Purpose |
| : | : | : |
| Input Normalization | `pyip.inputYesNo()` | Handling 'y', 'YES', 'No' etc., without manual string methods. |
| Timeout Logic | `timeout=8` | Terminating an input prompt based on a temporal threshold. |
| Retry Limits | `limit=3` | Preventing infinite attempts on a single data entry point. |
| Custom Auditing | `inputCustom(func)` | Injecting domainspecific logic into a validation framework. |
| Positional Formatting| `{i:<16}` | Creating vertically aligned columns for receipts/tables. |



 🚀 Execution
```bash
python sandwich_pos.py
python math_quiz.py