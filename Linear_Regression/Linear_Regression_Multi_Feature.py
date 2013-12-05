#!/usr/bin/python
#-*- coding:utf-8 -*-
# author  : eclipse
# email   : adooadoo@163.com
# filename: Linear_Regression_Multi_Feature.py

import matplotlib.pyplot as plt
import numpy as np

def loadData(in_file):
    """
    Description  :
    load from in_file,spliting with ','
    take it into array
    ****************************************
    Parameters   :
    in_file      :data source
    ****************************************
    Return:
    dataArray    :data in the type of Array(Numpy)
    """
    with open(in_file) as f:
        data = [line.strip('\n').split(',') for line in f]
    dataArray = np.matrix(data,dtype=float)
    return dataArray

def computeCost(X,y,theta):   
    """
    Description  :
    compute the cost function
    ****************************************
    Parameters   :
    X            :input data
    y            :output data
    theta        :lineParameter of X
    ****************************************
    Return       :
    cost         :return the error cost 
    """ 
    return 1.0/(2*X.shape[0])*np.sum(np.power(theta*X.T-y.T,2))

def featureNormalize(X):
    """
    Description  :
    Normalize the feature((x-mean(x))/sigma(x))
    ****************************************
    Parameters   :
    X            :input data
    ****************************************
    Return       :
    X_norm       :feature(normalized)
    mu           :mean of feature
    sigma        :sigma of feature
    """
    X_norm = X
    mu = np.zeros([1, X.shape[0]])
    sigma = np.zeros([1, X.shape[0]])
    mu = np.mean(X,0)
    sigma = np.std(X,0)
    X_norm = (X - mu)/sigma
    return X_norm,mu,sigma

def gradientDescent(X, y, theta, alpha, num_iters):
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
    #Initialize some useful values
    m = X.shape[0]; 
    X = np.concatenate((np.ones([m,1]), X),1)
    
    J_history = []
    for i in range(0, num_iters):
        theta = theta - (alpha / m * ((theta*X.T-y.T)*X))
        J_history.append(computeCost(X,y,theta))
    return theta,J_history

def normalEqn(X, y):
    """
    Description  :
    use normal equaltion to slove LR problem
    ****************************************
    Parameters   :
    X            :input data
    y            :output data
    ****************************************
    Return       :
    theta        :return the theta of line
    """ 
    return ((np.linalg.pinv(X.T * X)) * X.T * y).T


#Main function
#load data into array(type is float)
data = loadData('ex1data2.txt')
m = data.shape[0] #number of data
n = data.shape[1] #number of feature
X = data[:,0:data.shape[1]-1]
y = data[:,data.shape[1]-1]

#init parameter
iterations = 400
#normalize all feature
X_norm,mu,sigma = featureNormalize(X) 

#init figure parameter
fig1 = plt.figure()
ax1=fig1.add_subplot(111) 

#draw four line with different alpha in gradien descent
alpha1 = 0.01
theta = np.matrix([0]*n)
theta,J_history = gradientDescent(X_norm, y, theta, alpha1, iterations)
ax1.plot(J_history,'b',linewidth=4,label=u'α:0.01');
#print computeCost(np.concatenate((np.ones([m,1]), X_norm),1),y,theta)

alpha2 = 0.05
theta = np.matrix([0]*n)
theta,J_history = gradientDescent(X_norm, y, theta, alpha2, iterations)
ax1.plot(J_history,'g',linewidth=4,label=u'α:0.05')

alpha3 = 0.15
theta = np.matrix([0]*n)
theta,J_history = gradientDescent(X_norm, y, theta, alpha3, iterations)
ax1.plot(J_history,'pink',linewidth=4,label=u'α:0.15')

alpha4 = 0.55
theta = np.matrix([0]*n)
theta,J_history = gradientDescent(X_norm, y, theta, alpha4, iterations)
ax1.plot(J_history,'r',linewidth=4,label=u'α:0.55');

plt.legend()
plt.show()
fig1.savefig('alpha_rate.png')

#Another way to slove this problem
#use normal equaltion()
theta1 = normalEqn(np.concatenate((np.ones([m,1]), X_norm),1), y)
#print computeCost(np.concatenate((np.ones([m,1]), X_norm),1),y,theta1)


