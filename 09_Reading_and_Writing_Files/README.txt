 File I/O, Persistent Storage & Template Automation

This module focuses on "The Persistence Layer"—moving data out of volatile RAM and into longterm storage. These scripts demonstrate how to manage file hierarchies, parse document templates, and build CLIbased search engines.



 📂 Featured Scripts

 1. Interactive Mad Libs Engine (`mad_libs.py`)
 Concept: Nondestructive Template Parsing.
 Logic: Uses iterative regex substitution (`re.sub` with `count=1`) to fill placeholders without overwriting the original template.
 Key Tool: `with` context managers for secure file writing.

 2. MultiClipboard Manager (`mcb.pyw`)
 Concept: KeyValue Database Management.
 Logic: Extends the system clipboard by storing multiple text snippets in a `shelve` database.
 Key Tool: `sys.argv` for commandline instructions (save, list, delete).

 3. Bulk Quiz Generator (`quiz_gen.py`)
 Concept: MassProduction & Randomization.
 Logic: Generates 35 unique quiz forms and answer keys by shuffling both question order and multiplechoice distractors.
 Key Tool: `pathlib` for automated directory orchestration and crossplatform pathing.

 4. Local Grep Utility (`grep_clone.py`)
 Concept: Data Mining & Discovery.
 Logic: Performs a "Deep Scan" of all `.txt` files in a directory, reporting the exact file and line number for any regex match.
 Key Tool: Path globbing (`p.glob('.txt')`) for targeted file iteration.



 🛠️ Technical Competencies

| Feature | Implementation | Purpose |
| : | : | : |
| Object Persistence | `shelve.open()` | Saving Python objects (lists/dicts) directly to disk. |
| Path Manipulation | `Path.cwd() / 'dir'` | Crossplatform directory navigation using `pathlib`. |
| Directory Creation | `p.mkdir(exist_ok=True)` | Programmatically building folder structures. |
| Clipping/Pasting | `pyperclip` | Bridging the gap between Python and the OS clipboard. |
| Iterative Search | `file.readlines()` | Scanning large datasets linebyline to preserve context. |



 🚀 Workflow Summary
1. Extraction: Read data from files or the clipboard.
2. Transformation: Randomize, substitute, or filter data using Regex.
3. Persistence: Commit results back to new files or a `shelve` database.