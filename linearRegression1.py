#Linear Regression and plotting using libraries

from __future__ import division
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math

df = pd.read_csv('ex1data1.txt', header = None, names = ['x','y'])
x = np.array(df.x)
y = np.array(df.y)
theta = np.zeros((2,1))

#scatterplot of data with option to save figure.
def scatterPlot(x,y,yp=None,savePng=False):
	plt.xlabel('Population of City in 10,000s')
	plt.ylabel('Profit in $10,000s')
	plt.scatter(x, y, marker='x')
	if yp != None:
		plt.plot(x,yp)
	if savePng==false:
		plt.show()
	else:
		name = raw_input('Name Figure File: ')
		plt.savefig(name+'.png')


scatterPlot(x,y)

#linear regression implementation using libraries
(m,b) = np.polyfit(x,y,1)
print 'Slope is ' + str(m)
print 'Y intercept is ' + str(b)
yp = np.polyval([m,b],x)
scatterPlot(x,y,yp)



