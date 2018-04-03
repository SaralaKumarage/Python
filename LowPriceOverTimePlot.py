from sklearn import datasets

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')


import matplotlib.pyplot as plt

date=df['Date']

low=df['Low']



#histogram
plt.plot(date,low)

#scatter plot
#plt.scatter(date,low)


plt.xlabel('Date')
plt.ylabel('Low Price')

plt.title('EUR/USD low price variations')
plt.show()