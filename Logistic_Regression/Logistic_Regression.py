#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def loadData(in_file):
    """
    Description:
    load from in_file,spliting with ','
    take it into array
    ****************************************
    Parameters:
    in_file   :data source
    ****************************************
    Return:
    dataArray:data in the type of Array(Numpy.Array)
    """

    with open(in_file) as f:
        data = [line.strip('\n').split(',') for line in f]
    dataArray = np.array(data, dtype=float)
    return dataArray

def getLine(xRange, theta):
    """
    Description  :
    get the line of our linear regression
    ****************************************
    Parameters:
    xRange       :x's range in the figure
    theta        :Parameter of the line,
                  ex:y=a+bx,lineParameter of X
    ****************************************
    Return       :
    line         :return a line in Type of Line2D in pylab
    """
    print [xRange[0] * theta[0, 1] + theta[0, 0],
                      xRange[1] * theta[0, 1] + theta[0, 0]]
    return plt.Line2D(xRange, [xRange[0] * theta[0, 1] + theta[0, 0],
                      xRange[1] * theta[0, 1] + theta[0, 0]])

def show_init_image(X, y, theta):
    '''
    Description:
    show the 2D data(X) with label y
    ****************************************
    Parameters:
    X   :       2D raw data
    y   :       2D data's label 
    ****************************************
    Return:
    None
    '''
    fig1 = plt.figure()
    fig1.figsize = (2, 2)
    ax = fig1.add_subplot(111)
    pos = np.array([X[i] for i in range(np.size(y)) if y[i] == 1])[:, 0]
    neg = np.array([X[i] for i in range(np.size(y)) if y[i] != 1])[:, 0]
    plt.plot(pos[:, 0], pos[:, 1], 'ro', label='positve', markersize=8)
    plt.plot(neg[:, 0], neg[:, 1], 'b^', label='negative', markersize=8)
    tmp = (float(-theta[0]/theta[2]),float(-theta[1]/theta[2]))
    print theta
    print list(ax.axis()[0:2])
    line1 = getLine(list(ax.axis()[0:2]), np.matrix(tmp))
    line1.set_color('g')
    line1.set_linewidth(4)
    ax.add_line(line1)
    plt.show()

def sigmoid(z):
	'''
	Description:
	sigmoid function for LR
	****************************************
	Parameters:
	z   :  input data(np.array)
	****************************************
	Return:
	g   :  data process by sigmoid(np.array)
	'''
	g = 1.0 / (1 + np.exp(-1*z));
	return g

def costFunction(X, y, theta):
    m = X.shape[0]
    J = 1.0 / m * np.sum(-y.T*np.log(sigmoid(np.dot(X,theta).T))-(1-y.T)*np.log(1-sigmoid(np.dot(X,theta).T)))
    grad = 1.0 / m * np.dot(X.T,(sigmoid(np.dot(X,theta).T)-y))
    return J,grad

def f(theta, X, y):
    J = 1.0 / m * np.sum(-y.T*np.log(sigmoid(np.dot(X,theta).T))-(1-y.T)*np.log(1-sigmoid(np.dot(X,theta).T)))
    return J

def f_prime(theta, X, y):
    
    grad = 1.0 / m * np.dot(X.T,(sigmoid(np.dot(X,theta).T)-y))
    return grad

def gradientDescent(
    X,
    y,
    theta,
    alpha,
    num_iters,
    ):
    """
    Description  :
    gradient descent to minimize the cost function
    ****************************************
    Parameters   :
    X            :input data
    y            :output data
    theta        :lineParameter of X
    alpha        :descent step
    num_iters    :Times of iteration
    ****************************************
    Return       :
    theta        :the best theta in this DG
    theta_history:all theta data
    """

    # Initialize some useful values

    m = X.shape[0]
    X = np.concatenate((np.ones([m, 1]), X), 1)
    for i in range(0, num_iters):
        J,grad = costFunction(X, y, theta)
        #print J
        theta = theta - alpha * grad.T 
    #print J
    return theta

if __name__ == '__main__':
    data = loadData('data1.txt')
    m = data.shape[0]
    n = data.shape[1]  # number of feature
    X = data[:, 0:2]
    y = data[:, 2]
    #theta = np.zeros([n ,1])
    iterations = 4000
    alpha = 0.0009
    #theta = gradientDescent(X, y, theta, alpha, iterations)
    X = np.concatenate((np.ones([m, 1]), X), 1)
    theta = np.ndarray([0]*n)
    optimLogit = scipy.optimize.fmin_bfgs(f,theta,f_prime,args=(X,y),gtol = 1e-3)
    
    #print costFunction(theta, X, y)
    #show_init_image(X, y, theta)

