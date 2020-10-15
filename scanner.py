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


#Read lines in the array, create dataframe with keywords, and amount columns
def parseLine(textList):
    data = pd.DataFrame(columns = ['index','keywords','amount'])
    for line in range(len(textList)):
        temp = textList[line].strip()
        if (temp != ''):
            data = data.append(pd.DataFrame({"index":[len(data)],
                                      "keywords":[temp],
                                      "amount":[parseAmount(temp)]
                                      }))
    return data

#return amount in a string
def parseAmount(lineItem):
    digit = ''
    for i in lineItem:
        if i.isdigit():
            digit = digit+ i
    try:
        digit = float(digit)
    except:
        print("no digits")
    if(lineItem.find('(')!= -1 and lineItem[lineItem.find('(')+1].isdigit()):
        digit *= -1
    return digit

data = parseLine(text)
print(data)