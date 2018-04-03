import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
plt.style.use('ggplot')

#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

#extract the features
date=df['Date']

open=df['Open']

close=df['Close']

high=df['High']

low=df['Low']


#extract the labels
pred_open=df['Pred_Open']

pred_close=df['Pred_Close']

pred_high=df['Pred_High']

pred_low=df['Pred_Low']




#creating list of lists consists of open,close,high and low prices
X=[]
for i in df.index:
	row=[open.values[i],close.values[i],high.values[i],low.values[i]]
	X.append(row)


#creating list of lists consists of open,close,high and low prices
y=[]
for i in df.index:
	row=[pred_open.values[i],pred_close.values[i],pred_high.values[i],pred_low.values[i]]
	y.append(row)


#KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='minkowski',metric_params=None,n_jobs=1,n_neighbors=8,p=2,weights='uniform')
X=np.asarray(X)
y=np.asarray(y)
print(X.shape)
print(y.shape)


#split the features and labels train and test data
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=21,stratify=y)

knn= KNeighborsClassifier(n_neighbors=8)

#train the classifier with training data 
knn.fit(X_train,y_train)

#test the classifier with test data
y_pred=knn.predict(X_test)

#print the predictions
print("Test set predictions:\n {}".format(y_pred))

#print the accuracy of the classifier
print(knn.score(X_test,y_test))

