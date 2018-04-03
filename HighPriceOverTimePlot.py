from sklearn import datasets

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')


import matplotlib.pyplot as plt

date=df['Date']

high=df['High']



#histogram
plt.plot(date,high)

#scatter plot
#plt.scatter(date,high)


plt.xlabel('Date')
plt.ylabel('High Price')

plt.title('EUR/USD high price variations')
plt.show()