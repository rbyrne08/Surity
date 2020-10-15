import tickerData as td
import pandas as pd
import os.path
from os import path
import time

AMD = td.tickerData('AMD')

AMD.to_csv(path_or_buf = 'tickerData\AMD.csv')

recentTick = pd.read_csv('recentIPOs.csv')

tickerDict = []

for i in range(len(recentTick)):
    tickerDict.append([recentTick.iloc[i]['Symbol'],recentTick.iloc[i]['Industry']])

for i in range(len(tickerDict)):
    print(tickerDict[i][0])
    if(path.exists('tickerData\Data'+tickerDict[i][0]) == False):
        temp = td.tickerData(tickerDict[i][0])
        temp.to_csv(path_or_buf = 'tickerData\Data' + tickerDict[i][0] + '.csv')
    if (i%5==0):
        time.sleep(60)