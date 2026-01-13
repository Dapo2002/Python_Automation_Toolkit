# Traverses folders to find and decrypt PDFs using a CLI password;
# safely handles file locks for success, failure, and unencrypted cases.

import os
import sys
import PyPDF2

if len(sys.argv) != 2:
    print('Usage: PDFParanoia2 [password]')
    sys.exit()
password = sys.argv[1]

folder = r"C:\Users\User\OneDrive\User\PycharmProjects\automate_online-materials"
folder_copy = r"C:\Users\User\Desktop\experiment"
os.makedirs(folder_copy, exist_ok=True)

for folderName, subFolders, filenames in os.walk(folder):
    for file in filenames:
        if file.endswith('.pdf'):
            pdfFile = open(os.path.join(folderName, file), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted:
                if pdfReader.decrypt(password):

                    resultFile = open(os.path.join(folder_copy, file.removesuffix('.pdf') +
                                      "_decrypted.pdf"), 'wb')
                    pdfWriter = PyPDF2.PdfFileWriter()

                    for page in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(page))
                    pdfWriter.write(resultFile)
                    print(f'{file} decrypted successfully')
                    resultFile.close()
                else:
                    print(f'Password Incorrect for {file}! Moving on...')
                    pdfFile.close()
                    continue
            else:
                print(f'{file} is not encrypted')
            pdfFile.close()
