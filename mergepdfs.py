# mergepdfs.py Combines all the PDFs in the current direction into one PDF
# inspired by "Automate the Boring Stuff"

import PyPDF2, os

# get all files with pdf extension
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# sort names of PDF files
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# create reader for each file
for filename in pdfFiles:
    fileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fileObj)

    # add all pages of pdf
    for pgNum in range(0, pdfReader.numPages):
        pgObj = pdfReader.getPage(pgNum)
        pdfWriter.addPage(pgObj)

# save the merged pdf
outputName = raw_input('Enter a name for the merged pdf: ')
mergedPdf = open(outputName, 'wb')
pdfWriter.write(mergedPdf)
mergedPdf.close()
