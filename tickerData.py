import pandas
import datetime
import numpy as np
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

def tickerData(ticker):

    ts = TimeSeries(key='G393ZU9X9M9LVW63', output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(symbol=ticker,outputsize='full')
    for i in range(0,data.shape[0]-2):
        data.loc[data.index[i+2],'SMA_3'] = np.round(((data.iloc[i,0]+ data.iloc[i+1,0] +data.iloc[i+2,0])/3),2)
        data.loc[data.index[i+1],'dx'] = np.round(((data.iloc[i+1,0]- data.iloc[i+2,0])),2)
        data.loc[data.index[i+2],'day'] = data.index[i+2].weekday()
        data.loc[data.index[i+2],'deltaday'] = np.round(((data.iloc[i+2,3]- data.iloc[i+2,0])),2)

    #LIST [DAY,SUM OF CHANGE,NO OF DAYS]
    L = [['M',0,0],['T',0,0],['W',0,0],['T',0,0],['F',0,0]]

    for i in range(0,data.shape[0]-2):
        L[int(data.iloc[i+2,10])][1] += data.iloc[i+2,9]
        L[int(data.iloc[i+2,10])][2] += 1

    return data

