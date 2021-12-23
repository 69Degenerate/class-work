#import pandas as pd

import numpy as num
import matplotlib.pyplot as plt

x=num.linspace(0,100,100)
y=x*num.linspace(100,150,100)
plt.plot(x,y,c='r',marker='*',markersize=4)
plt.grid(True)
plt.legend("sOME BoDy")
plt.title('gfskdj')
plt.xlabel('asd')
plt.ylabel('qwe')

print(plt.show())