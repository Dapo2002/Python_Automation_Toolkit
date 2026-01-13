# A cloud-resident validation script that performs row-wise integrity checks to 
# ensure the product of the first two columns matches the value in the third.

import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

for row in range(2, sheet.rowCount + 1):
    rOw = sheet.getRow(row)
    if rOw[0] == '':
        continue
    elif int(rOw[0]) * int(rOw[1]) != int(rOw[2]):
        print(f'Row {row} values may be incorrect!')
