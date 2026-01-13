 Python Data Structures & Algorithmic Logic

A collection of scripts exploring the transition from basic syntax to complex data manipulation, covering everything from statistical simulations to cellular automata.



 📂 Featured Scripts

 1. Grid Transposer (`grid.py`)
 Concept: Matrix manipulation.
 Logic: Swaps X and Y coordinates in a nested list to render a 2D image correctly in the terminal.
 Learning: Navigating multidimensional arrays and coordinate mapping.

 2. Coin Flip Streak (`coin_streak.py`)
 Concept: Monte Carlo Simulation.
 Logic: Executes 10,000 trials to find the empirical probability of a 6unit streak in 100 flips.
 Learning: Using the `random` module for statistical modeling and lawoflargenumbers approximation.

 3. ListtoProse Formatter (`list_to_string.py`)
 Concept: String manipulation & Natural Language Generation.
 Logic: Slices lists and injects "and" for grammatical correctness.
 Learning: Handling edge cases (empty or singleitem lists) and list slicing (`[:1]`).

 4. Conway's Game of Life (`conway.py`)
 Concept: Cellular Automata.
 Logic: Implements toroidal (wraparound) geometry and neighborcounting rules.
 Learning: Using `copy.deepcopy` to manage generational updates without corrupting current state.

 5. Magic 8Ball (`magic8ball.py`)
 Concept: Abstracted Randomization.
 Logic: Compares manual indexing (`randint`) against the Pythonic `random.choice`.
 Learning: Identifying opportunities to reduce code complexity through builtin abstractions.

 6. Inventory Recall (`inventory.py`)
 Concept: Collection Comparison & Membership.
 Logic: Uses `enumerate` for indexed display and `set` comparison to check for completion.
 Learning: State tracking and unordered identity checks between two collections.



 🛠️ Technical Competencies

| Script | Primary Tool | Data Structure | Key Keyword |
| : | : | : | : |
| Grid | Nested Loops | `List[List[str]]` | `range()` |
| Coin Streak | Probability | `List[str]` | `append()` |
| Prose | Slicing / `.join()` | `List[str]` | `yield` / `return` |
| Game of Life | `copy.deepcopy()` | 2D Matrix | `%` (Modulo) |
| 8Ball | `random.choice()` | Flat String List | `choice()` |
| Inventory | `set()` / `enumerate()` | HashSet & List | `in` / `not in` |



 🚀 Execution
To run any of the scripts, ensure you have Python 3.x installed:
```bash
python grid.py
python coin_streak.py
python list_to_string.py
python conway.py
python magic8ball.py
python inventory.py