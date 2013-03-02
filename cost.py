

def cost(x, y, theta=[0,0]):
	"""Computes the cost of linear regression
	theta = parameter for linear regression
	x and y are the data points
	This is done to monitor the cost of gradient descent"""
	m = len(x)
	J = 1/(2*m) * sum([((theta[0]+theta[1]*x) - y)**2 for (x,y) in zip(x,y)])
	return J

def gradientDesc(x, y, theta=[0,0], alpha=.01,iterations=1500):
	""""Gradient Descent implementation of 
	linear regression with one variable"""
	#might need to add another for loop to do iterations
	m = len(x)
	assert len(x) == len(y), 'number of x\'s and y\'s doesn\'t match' 
	J = []
	for numbers in range(iterations):
		a = theta[0] - alpha*1/m*sum([(((theta[0]+theta[1]*xi) - yi)**2)/2 for (xi,yi) in zip(x,y)])
		b = theta[1] - alpha*1/m*sum([((theta[1]+theta[1]*xi) - yi)*xi for (xi,yi) in zip(x,y)])
		theta[0],theta[1]=a,b
		print theta[0]
		print theta[1]
		J.append(cost(x,y,theta))
		print 'Cost: ' + str(J[-1])
	return theta

def gradientDescJ(x, y, theta=[0,0], alpha=.01,iterations=1500):
	""""Gradient Descent implementation of 
	linear regression with one variable"""
	#might need to add another for loop to do iterations
	m = len(x)
	assert len(x) == len(y), 'number of x\'s and y\'s doesn\'t match' 
	J = [999,998]
	while J[-1] < J[-2]:
		theta[0] = theta[0] - alpha*1/m*sum([((theta[0]+theta[1]*xi) - yi) for (xi,yi) in zip(x,y)])
		theta[1] = theta[1] - alpha*1/m*sum([((theta[1]+theta[1]*xi) - yi)*xi for (xi,yi) in zip(x,y)])
		print theta[0]
		print theta[1]
		J.append(cost(x,y,theta))
		print 'Cost: ' + str(J[-1])
	return theta

# iterations = 1500
# alpha = .01
