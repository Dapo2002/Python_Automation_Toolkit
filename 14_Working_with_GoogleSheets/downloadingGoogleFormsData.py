# A robust cloud-data harvester that dynamically locates the 'Email Address' 
# column via header-row inspection and aggregates all non-empty entries into a 
# list.

import ezsheets

ss = ezsheets.Spreadsheet('1rQoBOdJAf8aGxeemHK1glF6uywKWD0aNKB22Rn0wjU4')
sheet = ss[0]

row1 = sheet.getRow(1)
try:
    emailColumnIndex = row1.index('Email Address')
    emailColumnList = sheet.getColumn(emailColumnIndex + 1)
    emailList = []
    for email in emailColumnList[1:]:
        if email != '':
            emailList.append(email)
    print(emailList)
except ValueError:
    print('Email Address not Found')
