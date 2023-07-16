#importing pandas,numpy, matplotlib.pyplot as pd,np,plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import data set in csv type as data
data=pd.read_csv("/content/dataset 1.csv",index_col=0)
#my data set is cleaned so,non preprocessing and cleening
#print(data.head())
#print(data.describe(include=[np.number]))
#print(data.dtypes)
#showing avg cost of all types
print("the avg cost inc between last and this year is",data['diff'].mean(),"among all types")
try:
  #taking n as no of beds
  n=int(input("enter no of bedrooms"))
  #taking m as tyoe of house
  m=int(input("enter house type (1 for individual 2 for portions)"))
  #taking max price as o
  o=int(input("enter prce upto"))
  #applying filter technique to get required set of results
  a=data[data['bedrooms']==n]
  a=data[data['house type']==m]
  a=data[data['cost']<=o]
  #if no data found than it cause 0 div exception than it will move to except block
  if(len(a)==0):
    print(2/0)
  #else shoes best house list
  print("the best houses under",o,"are:")
  print(a.sort_values("cost"))
  x=a['cost'].mean()
  print("the avg cost ",x,"for",n,"bedrooms")
  #visulization of resultent data
  # plt.plot(a['cost'])
  # plt.plot(x)
  # plt.title("graph for difference between avg price and actual price among choice")
  # plt.xlabel('cost')
  # plt.ylabel('avg cost')
  # plt.show()
  #again showing best houses
  print("best house is")
  z=data[data['cost']>=(o-3000)]
  print(z)
except:
  #if any error or exception it will print 
  print("Not avilable")