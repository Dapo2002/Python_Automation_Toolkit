#!  python3
#  removeCsvHeader.py - Removes the header from all CSV files in the current
#  working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

#  Loop through every file in the current working directory
for csvFilename in os.listdir(r'.\removeCsvHeader'):
    if not csvFilename.endswith('.csv'):
        continue
    print(f'Removing header from {csvFilename}...')
    #  Read the CSV file in (skipping the first row).
    csvRows = []
    fullPath = os.path.join(r'.\removeCsvHeader', csvFilename)
    csvFileObj = open(fullPath)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip the first row
        csvRows.append(row)
    csvFileObj.close()

    #  Write out the cSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
