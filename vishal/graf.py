#import pandas as pd

from matplotlib import colors, legend
import numpy as num
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean


# program for line space
'''x=num.linspace(0,100,100)
y=x*num.linspace(100,150,100)
plt.plot(x,y,c='r',marker='*',markersize=4)
plt.grid(True)
plt.legend("sOME BoDy")
plt.title('gfskdj')
plt.xlabel('asd')
plt.ylabel('qwe')
'''

#program for bar chart 
'''x=[2,4,6,8]
y=[10,20,30,40]
plt.bar(x,y)
plt.title("BAR CHART")
plt.xlabel('asd')
plt.ylabel('qwe')
'''


#program for pie chart
x=[20,54,64,76]
e=[0.1,0.1,0.1,0.1]
plt.title("pir chart")
plt.pie(x,labels=['a','s','d','f'],shadow=5,autopct='%1.1f%%',explode=e)
plt.legend()


print(plt.show())
