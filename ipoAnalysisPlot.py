import tickerData as td
import pandas as pd
import os.path
from os import path
import time
import matplotlib.pyplot as plt
import numpy as np

AMD = td.tickerData('AMD')

AMD.to_csv(path_or_buf = 'tickerData\AMD.csv')

tickers = pd.read_csv('recentIPOs.csv')


def writeTickers(tickers):
    tickerDict = []

    for i in range(len(tickers)):
        tickerDict.append([tickers.iloc[i]['Symbol'],tickers.iloc[i]['Industry']])

    for i in range(len(tickerDict)):
        print(tickerDict[i][0])
        if(path.exists('tickerData\Data'+tickerDict[i][0]) == False):
            temp = td.tickers(tickerDict[i][0])
            temp.to_csv(path_or_buf = 'tickerData\Data' + tickerDict[i][0] + '.csv')
        if (i%5==0):
            time.sleep(60)


def readTickers(tickers):
    dataset = []
    for i in range(len(tickers)):
        dataset.append(pd.read_csv('tickerData\Data'+tickers.iloc[i]['Symbol']+'.csv').tail(100))
    return dataset

def testmax(testdata):
    maxi = 0
    for i in testdata:
        if maxi < len(i):
            maxi = len(i)
            a = i
    return maxi, a

testdata = readTickers(tickers)
for i in range(len(testdata)):    
    testdata[i]['log'] = np.log(testdata[i]['5. adjusted close'].astype('float64')/testdata[i]['5. adjusted close'].astype('float64').shift(1))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

for i in range(len(testdata)):
    testdata['log']

for i in range(len(testdata)):
    ax1.plot(testdata[i]['log'])