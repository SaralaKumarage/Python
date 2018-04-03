from sklearn import datasets

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')


import matplotlib.pyplot as plt

date=df['Date']

open=df['Open']



#histogram
plt.plot(date,open)

#scatter plot
#plt.scatter(date,open)


plt.xlabel('Date')
plt.ylabel('Open Price')

plt.title('EUR/USD open price variations')
plt.show()