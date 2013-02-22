

def cost(x, y, theta=[0,0]):
	"""Computes the cost of linear regression
	theta = parameter for linear regression
	x and y are the data points
	This is done to monitor the cost of gradient descent"""
	J = 1/(2*m) * sum([((theta[0]+theta[1]*x) - y)**2 for (x,y) in zip(x,y)])
	return J

def gradientDesc(x, y, theta=[0,0], alpha=.01,iterations=1500):
	""""Gradient Descent implementation of 
	linear regression with one variable"""
	#might need to add another for loop to do iterations
	for numbers in range(iterations):
		theta[0] = theta[0] - alpha*1/m*sum([((theta[0]+theta[1]*xi) - yi)**2 for (xi,yi) in zip(x,y)])
		theta[1] = theta[1] - alpha*1/m*sum([(((theta[1]+theta[1]*xi) - yi)**2)*xi for (xi,yi) in zip(x,y)])		
	return theta

# iterations = 1500
# alpha = .01
