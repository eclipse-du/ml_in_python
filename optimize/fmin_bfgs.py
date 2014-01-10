#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
from scipy.optimize import fmin_cg
from scipy.optimize import fmin_bfgs
from scipy.optimize import fmin_l_bfgs_b
import numpy as np
import datetime

def loadData(in_file):
    with open(in_file) as f:
        data = [line.strip('\n').strip(' ').split(',') for line in f]
    dataArray = np.array(data, dtype=float)
    return dataArray

def sigmoid(z):
        g = 1.0 / (1 + np.exp(-1*z))
        return g

def f(theta, X, y):
    J = 1.0 / m * np.sum(-y.T*np.log(sigmoid(np.dot(X,theta).T))-(1-y.T)*np.log(1-sigmoid(np.dot(X,theta).T)))
    return J

def f_prime(theta, X, y):
    grad = 1.0 / m * np.dot(X.T,(sigmoid(np.dot(X,theta).T)-y))
    return grad

def featureNormalize(X):
    X_norm = X
    mu = np.zeros([1, X.shape[0]])
    sigma = np.zeros([1, X.shape[0]])
    mu = np.mean(X,0)
    sigma = np.std(X,0)
    X_norm = (X - mu)/sigma
    return X_norm,mu,sigma

if __name__ == '__main__':
    data = loadData('data1.txt')
    m = data.shape[0]
    n = data.shape[1]  # number of feature
    X = data[:, 0:-1]
    y = data[:, -1]
    Xnew = featureNormalize(X)[0]
    Xnew = np.concatenate((np.ones([m, 1]), Xnew), 1)
    theta = [0]*n
    
    starttime = datetime.datetime.now()
    optimLogit = fmin_cg(f,theta,f_prime,args=(Xnew,y),gtol=1e-10,norm=0.00000000001,epsilon=1.4901161193847656e-08)
    print optimLogit
    print (datetime.datetime.now() - starttime).microseconds/1000000.0
    
    starttime = datetime.datetime.now()
    theta = [0]*n
    optimLogit = fmin_bfgs(f,theta,f_prime,args=(Xnew,y),gtol=1e-10,norm=0.00000000001,epsilon=1.4901161193847656e-08)
    print optimLogit
    print (datetime.datetime.now() - starttime).microseconds/1000000.0

    starttime = datetime.datetime.now()
    theta = [0]*n
    optimLogit = fmin_l_bfgs_b(f,theta,f_prime,args=(Xnew,y))
    print optimLogit
    print (datetime.datetime.now() - starttime).microseconds/1000000.0