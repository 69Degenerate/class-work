#import pandas as pd

import numpy as num
import matplotlib.pyplot as plt
#df=pd.read_csv('/home/student/vishal/class-work/vishal/new.csv')
#print(df.head())
'''print(df.describe())
print(df.info())
print(df.dtypes)
print(df.shape)
print(df.size)
#print (df['counrty'].value_counts())
print(df.sample(10))
print(df.drop_duplicates(inplace=True))
print(df.sort_values(by='Year',inplace=True))
print(df)
print(df.loc[1:4])
#print(df.drop ())
print(df.query('Year>2019'))
#print(df.insert(pos,'Year',values))
#print(df.isnull())
print(df.dropna())'''
'''a=list(df["index"])
z=list(df["Value"])
plt.title('practice')
plt.bar(a,z,color='r')
print(plt.show())'''
x=num.linspace(0,100,100)
y=x*num.linspace(100,150,100)
plt.plot(x,y,c='r',markersize=3)

print(plt.show())