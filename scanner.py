import PyPDF2 as pdf
import pandas as pd


pdfFileObj = open('ISTest.pdf','rb')
pdfReader = pdf.PdfFileReader(pdfFileObj)
numpages = pdfReader.numPages
text = []
for page in range(numpages):
    pageObj = pdfReader.getPage(page)
    obj = pageObj.extractText().split('\n')
    for a in obj:
        text.append(a)
for i in range(len(text)):
    print(text[i])

