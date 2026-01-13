# Recursively encrypts PDFs with a 'verify-before-delete' safety check
# to ensure data integrity before removing original files.

import os
import sys
import PyPDF2

if len(sys.argv) != 2:
    print('Usage: PDFParaonia [your_password]')
    sys.exit()

folder = r"C:\Users\User\Documents\PDF Paranoia"
encryptedPDFsFolder = r"C:\Users\User\Documents\PDFFilesEncrypted"
os.makedirs(encryptedPDFsFolder, exist_ok=True)
password = sys.argv[1]

for folderName, subFolder, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(os.path.join(folderName, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)
            resultPdf = open(os.path.join(encryptedPDFsFolder, filename.removesuffix('.pdf') + '_encrypted.pdf'), 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()

            pdfFileAgain = open(os.path.join(encryptedPDFsFolder, filename.removesuffix(".pdf") + '_encrypted.pdf'),
                                'rb')
            pdfReaderAgain = PyPDF2.PdfFileReader(pdfFileAgain)
            if pdfReaderAgain.decrypt(password):
                print(f'{filename} encrypted correctly!')
                pdfFileAgain.close()
                pdfFile.close()
                os.remove(os.path.join(folderName, filename))
            else:
                print('Something wrong with your code, DUMMY!')
            pdfFileAgain.close()
            pdfFile.close()
