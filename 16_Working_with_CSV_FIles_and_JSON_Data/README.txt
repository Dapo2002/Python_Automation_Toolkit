 Data Automation and Processing Suite

A collection of Python utilities designed to automate repetitive data engineering tasks, including spreadsheet transformation, dataset cleaning, and realtime API integration.



 🛠 Project Components

 1. ExceltoCSV Converter (`excelToCsvConverter.py`)
Description: Automates the highvolume conversion of Microsoft Excel workbooks into standardized CSV files.
 Workflow: Scans a source directory for `.xlsx` files and iterates through every internal worksheet.
 Output: Generates individual CSV files for each sheet, following the naming convention: `<OriginalFileName>_<SheetTitle>.csv`.
 Business Value: Eliminates the manual overhead associated with "Save As" operations for multisheet workbooks.

 2. CSV Header Optimization (`removeCsvHeader.py`)
Description: A datacleaning utility used to prepare raw CSV files for programmatic consumption or database ingestion.
 Workflow: Systematically removes the first row (header) from all CSV files within a designated folder.
 Output: Saves processed files into a `headerRemoved` directory, ensuring original data remains untouched.
 Business Value: Facilitates seamless batch processing of datasets where metadata headers interfere with calculation or appending logic.

 3. Realtime Weather CLI (`getOpenWeather.py` & `gow.bat`)
Description: A commandline tool that interfaces with the OpenWeatherMap API to provide localized meteorological intelligence.
 Workflow: Accepts city/country input via the terminal and retrieves a 3day forecast in JSON format.
 Integration: Includes a `.bat` wrapper for instant execution via the Windows Command Prompt (via the `gow` alias).
 Business Value: Enables quick environmental data checks for logistical planning without leaving the development environment.



 📊 Sample Data Support
 `example.tsv`: Provides a baseline TabSeparated Values file for testing crossformat parser reliability and script validation.



 🚀 Getting Started

 Technical Specifications
 Python Version: 3.10+
 Primary Modules: `openpyxl` (Excel parsing), `csv` (Data writing), `requests` (API communication).

 Installation
1. Install required dependencies:
   ```bash
   pip install openpyxl requests