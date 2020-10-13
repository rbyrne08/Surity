import PyPDF2 as pdf
import pandas as pd


pdfFileObj = open('ISTest.pdf','rb')
pdfReader = pdf.PdfFileReader(pdfFileObj)
numpages = pdfReader.numPages
text = []
for page in range(numpages):
    pageObj = pdfReader.getPage(page)
    text = text.append(pageObj.extractText().split('\n'))
print(text)

