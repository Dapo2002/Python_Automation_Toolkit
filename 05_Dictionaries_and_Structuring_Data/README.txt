 Dictionary Structures & Data Validation

A collection of scripts demonstrating the versatility of Python Dictionaries (Hash Maps) for state management, domainspecific validation, and data aggregation.



 📂 Featured Scripts

 1. Birthday Database (`birthdays.py`)
 Concept: Runtime Data Persistence.
 Logic: Uses a dictionary to store and retrieve personal dates, allowing for dynamic updates during execution.

 2. Chess Board Validator (`chess_validator.py`)
 Concept: Structural & Domain Validation.
 Logic: Audits a dictionarybased board to ensure it follows legal chess rules (piece counts, king existence, and coordinate validity).
 Technique: Coordinate parsing and constraint checking.

 3. RPG Inventory Tracker (`inventory.py`)
 Concept: Data Aggregation.
 Logic: Iterates through items to produce a clean summary report and a cumulative "Total Item" count.

 4. Dynamic Loot Adder (`add_to_inventory.py`)
 Concept: Collection Merging.
 Logic: Processes a list of new items and updates an existing inventory.
 Learning: Using the `.get()` method to handle nonexistent keys safely.

 5. Picnic Item Counter (`picnic.py`)
 Concept: Nested Dictionary Traversal.
 Logic: Aggregates values across a `Guest > Item > Quantity` hierarchy.
 Technique: Chained indexing and crosssectional data retrieval.

 6. Character Frequency Analyzer (`character_count.py`)
 Concept: Frequency Analysis & Pretty Printing.
 Logic: Maps the frequency of every character in a string using a dictionary.
 Learning: Utilizing `setdefault` for atomic initialization and `pprint` for organized output.



 🛠️ Technical Competencies

| Script | Primary Tool | Technique | Key Feature |
| : | : | : | : |
| Chess | Domain Logic | Coordinate Parsing | Multilayered `if` checks |
| Loot | `.get()` | Safe Incrementing | Prevents `KeyError` |
| Picnic | Nested Dicts | Chained Indexing | `dict[x][y]` access |
| Count | `setdefault()` | Atomic Setup | Efficient key creation |
| PPrint | `pprint` module | Data Visualization | Alphabetical sorting |



 🚀 Execution
```bash
python birthdays.py
python chess_validator.py
python inventory.py
python add_to_inventory.py
python picnic.py
python character_count.py