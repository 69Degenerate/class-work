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
'''x=[20,54,64,76]
e=[0.1,0.1,0.1,0.1]
plt.title("pir chart")
plt.pie(x,labels=['a','s','d','f'],shadow=5,autopct='%1.1f%%',explode=e)
plt.legend()'''


#program for hystogram

'''x = [1,1,2,3,3,5,7,8,9,10,
     10,11,11,13,13,15,16,17,18,18,
     18,19,20,21,21,23,24,24,25,25,
     25,25,26,26,26,27,27,27,27,27,
     29,30,30,31,33,34,34,34,35,36,
     36,37,37,38,38,39,40,41,41,42,
     43,44,45,45,46,47,48,48,49,50,
     51,52,53,54,55,55,56,57,58,60,
     61,63,64,65,66,68,70,71,72,74,
     75,77,81,83,84,87,89,90,90,91
     ]

plt.hist(x, bins=10)'''


plt.show() 