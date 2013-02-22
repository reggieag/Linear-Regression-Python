import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math
 

df = pd.read_csv('ex1data1.txt', header = None, names = ['x','y'])
x = np.array(df.x)
y = np.array(df.y)
theta = np.zeros((2,1))
#scatterplot of data 
def scatterPlot(x,y,yp=None):
	plt.xlabel('Population of City in 10,000s')
	plt.ylabel('Profit in $10,000s')
	plt.scatter(x, y, marker='x')
	if yp != None:
		plt.plot(x,yp)
	plt.show()

scatterPlot(x,y)

#linear regression implementation using libraries
#y = mx + b
(m,b) = np.polyfit(x,y,1)
print 'Slope is ' + str(m)
print 'Y intercept is ' + str(b)
yp = np.polyval([m,b],x)
scatterPlot(x,y,yp)

#Linear Regression from scratch using Gradient Descent
#cost function

#convert x and y into numpy arrays
x = x.values
y = y.values

#work in progress...
def cost(x, y, theta):
	"""Computes the cost of linear regression
	theta = parameter for linear regression
	x and y are the data points
	J is the cost"""
	m = len(y)
	counter = 0 
	i = 0
	while counter < m:
		i += math.sqrt(theta.transpose()*x[counter] - y[counter])
		counter += 1
	J = 1/(2*m) * i
	return J
print cost(x,y,theta)