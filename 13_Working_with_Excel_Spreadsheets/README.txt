 📊 Spreadsheet Automation & Data Engineering

This module focuses on "Data Transformation"—utilizing Python to interface with Microsoft Excel for bulk editing, mathematical modeling, and structural reorganization.



 📂 Featured Scripts

 1. Spreadsheet Structural Inserter (`blank_row_inserter.py`)
 Concept: MemoryBuffered Migration.
 Logic: Creates a new workbook and uses a variable pointer to "jump" row indices, effectively injecting $M$ blank rows at position $N$.
 Key Tool: `sys.argv` for CLI parameters and coordinate translation.

 2. Multiplication Table Generator (`multiplication_table.py`)
 Concept: Dynamic Formula Injection.
 Logic: Generates an $N \times N$ grid where cells contain live Excel formulas ($=A2B1$) rather than static values.
 Key Tool: `openpyxl.styles.Font` and `freeze_panes`.

 3. Census Data Aggregator (`readCensusExcel.py`)
 Concept: Data Serialization & Hierarchical Mapping.
 Logic: Collapses thousands of rows of flat data into a nested dictionary (State > County > Stats) and saves it as a reusable Python module.
 Key Tool: `pprint.pformat()` and dictionary `setdefault()`.

 4. Matrix Transposer (`transpose_excel.py`)
 Concept: Coordinate Inversion.
 Logic: Flips the axes of a spreadsheet ($X, Y \rightarrow Y, X$), turning columns into rows and viceversa using a 2D list buffer.
 Key Tool: Nested loop orchestration and listoflists mapping.

 5. TexttoSpreadsheet Bridge (`text_to_excel.py` / `excel_to_text.py`)
 Concept: Batch File I/O & Parallelization.
 Logic: Orchestrates the movement of data between fragmented `.txt` files and centralized Excel columns.
 Key Tool: `pathlib.glob()` and `readlines()` for bulk processing.

 6. Surgical Price Updater (`update_produce.py`)
 Concept: DictionaryDriven Maintenance.
 Logic: Performs targeted cell updates by mapping product names to a master update dictionary, skipping irrelevant records.
 Key Tool: `.cell(row, column)` integerbased navigation.



 🛠️ Technical Competencies

| Competency | Implementation | Purpose |
| : | : | : |
| Formula Scripting | `sheet[cell] = '=SUM(...)'` | Offloading computation to the Excel engine. |
| Coordinate Mapping | `get_column_letter()` | Translating integer indices to Excel's alphanumeric system. |
| Serialization | `pprint.pformat()` | Converting runtime data into persistent, importable code. |
| Matrix Operations | `[row][col] > [col][row]` | Reorienting datasets for different analytical requirements. |
| Style Management | `openpyxl.styles` | Enhancing readability through UI/UX improvements (Bold, Freezing). |



 🚀 Data Engineering Workflow
1. Ingestion: Load source data using `load_workbook` or `glob`.
2. Buffering: Store complex transformations in nested Python lists or dictionaries.
3. Processing: Apply mathematical offsets, formula injections, or lookupbased updates.
4. Verification: Ensure record integrity (Maintaining Haqq) by saving to a new "Output" file.