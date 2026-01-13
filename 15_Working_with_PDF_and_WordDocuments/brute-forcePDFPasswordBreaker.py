# A dictionary-based brute-force tool that iteratively tests uppercase
# and lowercase strings against PDFs encryption layer until a match is found.

import PyPDF2

dictionaryFile = open("dictionary.txt")
passwordList = dictionaryFile.readlines()
pdfFile = open("encryptedminutes.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

foundPassword = None

for password in passwordList:
    if pdfReader.decrypt(password.strip()) == 1:
        foundPassword = password.strip()
        print(f'{foundPassword}')
        break
    elif pdfReader.decrypt(password.strip().lower()) == 1:
        foundPassword = password.strip().lower()
        print(f'{foundPassword.lower()}')
        break
    else:
        continue

if not foundPassword:
    print('Password not found in dictionary.')
