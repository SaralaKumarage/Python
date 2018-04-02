import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
plt.style.use('ggplot')

#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

#extract the features
date=df['Date']

#slicing data frames to omit null values
date=date[:99]

open=df['Open']

#slicing data frames to omit null values
open=open[:99]

close=df['Close']

#slicing data frames to omit null values
close=close[:99]


high=df['High']

#slicing data frames to omit null values
high=high[:99]

low=df['Low']
#slicing data frames to omit null values
low=low[:99]

#extract the labels
pred_open=df['Pred_Open']
#slicing data frames to omit null values
pred_open=pred_open[:99]

pred_close=df['Pred_Close']
#slicing data frames to omit null values
pred_close=pred_close[:99]

pred_high=df['Pred_High']
#slicing data frames to omit null values
pred_high=pred_high[:99]

pred_low=df['Pred_Low']
#slicing data frames to omit null values
pred_low=pred_low[:99]





X=[]
for i in df.index-1:
	row=[open.values[i],close.values[i],high.values[i],low.values[i]]
	X.append(row)

X=np.asarray(X)

#creating list of lists consists of open,close,high and low prices
y=[]
for i in df.index-1:
	row=[pred_open.values[i],pred_close.values[i],pred_high.values[i],pred_low.values[i]]
	y.append(row)


y=np.asarray(y)


#split the features and labels train and test data
#X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.5,random_state=21,stratify=y)
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.5)

lr= LinearRegression(n_jobs=-1)

#train the classifier with training data 
lr.fit(X_train,y_train)

#test the classifier with test data
y_pred=lr.predict(X_test)

#print the predictions
print("Test set predictions:\n {}".format(y_pred))

#print the accuracy of the classifier
print(lr.score(X_test,y_test))

print(y_pred.shape)