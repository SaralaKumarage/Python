import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


#read data from excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

#extract the features
date=df['Date']

open=df['Open']

close=df['Close']

high=df['High']

low=df['Low']


#creating list of lists consists of open,close,high and low prices
input_data=[]
for i in df.index:
	row=[open.values[i],close.values[i],high.values[i],low.values[i]]
	input_data.append(row)

#printing the list
#for x  in range(0,len(input_data)):
#	print(input_data[x])

#assigning weights to  the nodes
weights={
#hidden layer 1 
	#node 1 weights
	'h1_n1':np.array([1,1,1,1]),
	#node 2 weights
	'h1_n2':np.array([2,2,2,2]),
	#node 3 weights
	'h1_n3':np.array([3,3,3,3]),
	#node 4 weights
	'h1_n4':np.array([4,4,4,4]),
	#output for open weights
	'open_output':np.array([1,1,1,1]),
	#output for close weights
	'close_output':np.array([2,2,2,2]),
	#output for high weights
	'high_output':np.array([3,3,3,3]),
	#output for low weights
	'low_output':np.array([4,4,4,4])
	}

#node values
h1_n1_value=0
h1_n2_value=0
h1_n3_value=0
h1_n4_value=0

for a in range(0,len(input_data)):
	h1_n1_value=h1_n1_value+(input_data[a]*weights['h1_n1']).sum()
	h1_n2_value=h1_n2_value+(input_data[a]*weights['h1_n2']).sum()
	h1_n3_value=h1_n3_value+(input_data[a]*weights['h1_n3']).sum()
	h1_n4_value=h1_n4_value+(input_data[a]*weights['h1_n4']).sum()

h1_n1_avg=h1_n1_value/len(input_data)
print(h1_n1_avg)

h1_n2_avg=h1_n2_value/len(input_data)
print(h1_n2_avg)

h1_n3_avg=h1_n3_value/len(input_data)
print(h1_n3_avg)

h1_n4_avg=h1_n4_value/len(input_data)
print(h1_n4_avg)

#hidden layer values
hidden_layer_values=np.array([h1_n1_avg,h1_n2_avg,h1_n3_avg,h1_n4_avg])

print(hidden_layer_values)


open_output=(hidden_layer_values*weights['open_output']).sum()

close_output=(hidden_layer_values*weights['close_output']).sum()

high_output=(hidden_layer_values*weights['high_output']).sum()

low_output=(hidden_layer_values*weights['low_output']).sum()

print(open_output,close_output,high_output,low_output)

