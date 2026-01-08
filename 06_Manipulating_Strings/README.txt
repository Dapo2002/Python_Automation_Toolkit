 OS Integration, Layout Engines & OOP Agents

This collection marks the transition from internal data manipulation to interacting with the Operating System and building autonomous, decisionmaking classes.



 📂 Featured Scripts

 1. Clipboard Controller (`clipboard.py`)
 Concept: InterProcess Communication (IPC).
 Logic: Programmatically interacts with the systemwide copypaste buffer.
 Key Tool: `pyperclip` module for crossplatform clipboard access.

 2. Tabular Layout Engine (`table_printer.py`)
 Concept: Dynamic Terminal UI (TUI) Design.
 Logic: Twopass algorithm that calculates maximum column widths before rendering data with rightjustified padding.
 Key Tool: `.rjust()` for uniform vertical alignment.

 3. Zombie Dice AI Tournament (`zombie_bots.py`)
 Concept: ObjectOriented Programming (OOP) & Heuristics.
 Logic: Defines multiple "Zombie" classes, each with a unique riskassessment algorithm to compete in a stochastic game simulation.
 The Agents:
     Randee: Purely stochastic (random) choices.
     TriggerTim/Wayne: Thresholdbased stopping.
     ParanoidPete: Comparative successtofailure ratio analysis.



 🛠️ Technical Competencies

| Competency | Implementation | Purpose |
| : | : | : |
| Encapsulation | `class BotName:` | Wrapping logic and state into reusable objects. |
| Heuristics | `if shotguns > brains:` | Implementing "rules of thumb" for complex decisionmaking. |
| Data Transposition| `range(len(list[0]))` | Converting horizontal data structures into vertical columns. |
| External Dependencies| `pip install ...` | Integrating thirdparty code for OSlevel functionality. |



 🚀 Execution
To run the tournament or view the UI:
```bash
python table_printer.py
python zombie_bots.py