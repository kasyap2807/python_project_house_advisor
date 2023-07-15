import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:\Users\kanup\OneDrive\Desktop\my works\sample\dataset 1.csv", index_col=0)
#print(data.head())
#print(data.describe(include=[np.number]))
#print(data.dtypes)
print("the avg cost inc between last and this year is",data['diff'].mean(),"among all types")
n=int(input("enter no of bedrooms"))
m=int(input("enter house type (1 for individual 2 for portions"))
o=int(input("enter prce upto"))
a=data[data['bedrooms']==n]
a=data[data['house type']==m]
a=data[data['cost']<=o]
print("the best houses under",o,"are:")
print(a.sort_values("cost"))
x=a['cost'].mean()
print("the avg cost ",x,"for",n,"bedrooms")
plt.plot(a['cost'])
plt.plot(x)
plt.title("graph for difference between avg price and actual price among choice")
plt.xlabel('cost')
plt.ylabel('avg cost')
plt.show()