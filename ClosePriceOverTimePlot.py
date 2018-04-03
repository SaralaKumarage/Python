from sklearn import datasets

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')


import matplotlib.pyplot as plt

date=df['Date']

close=df['Close']



#histogram
plt.plot(date,close)

#scatter plot
#plt.scatter(date,close)


plt.xlabel('Date')
plt.ylabel('Close Price')

plt.title('EUR/USD close price variations')
plt.show()