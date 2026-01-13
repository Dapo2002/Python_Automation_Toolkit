#!  python3
#  combinePdfs.py - Combines all the PDFs in the current working directory
#  into a single PDF.

import PyPDF2, os
#  Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
if 'allminutes.pdf' in pdfFiles:
    pdfFiles.remove('allminutes.pdf')
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#  Loop through all the PDF files.
for filename in pdfFiles:
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if pdfReader.isEncrypted:
            if not pdfReader.decrypt('rosebud') and not pdfReader.decrypt('swordfish'):
                print(f'Unable to decrypt {filename}')
                continue

#  Loop through all the pages (except the first) and add them.
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

#  Save the resulting PDF to a file.
        with open('allminutes.pdf', 'wb') as pdfOutput:
            pdfWriter.write(pdfOutput)
print('Done!')
