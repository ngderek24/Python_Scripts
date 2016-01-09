# rmpdfpages.py Removes specified pages from a specified PDF in current directory
# inspired by "Automate the Boring Stuff"
# arg1 : name of pdf we want to edit
# arg2 : name of output pdf

import PyPDF2, os, sys

# get name of pdf we want to remove pages from
filename = sys.argv[1]

# create writer for new pdf and reader for specified pdf
pdfWriter = PyPDF2.PdfFileWriter()
fileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(fileObj)

# get page numbers to remove
maxNumToRemove = pdfReader.numPages - 1
pages = []
while len(pages) < maxNumToRemove:
    pg = raw_input('Enter a page number to remove: ')
    if pg == '':
        break
    pages.append(pg)

for pgNum in range(0, pdfReader.numPages):
    if str(pgNum) not in pages:
        pgObj = pdfReader.getPage(pgNum)
        pdfWriter.addPage(pgObj)

# save edited pdf
outputName = sys.argv[2]
editedPdf = open(outputName, 'wb')
pdfWriter.write(editedPdf)
editedPdf.close()
fileObj.close()
