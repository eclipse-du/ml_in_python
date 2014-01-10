#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
from scipy.optimize import check_grad
from scipy.optimize import fmin
from scipy.optimize import brute
from scipy.optimize import anneal
from scipy.optimize import fmin_cg
from scipy.optimize import fmin_ncg
from scipy.optimize import fmin_bfgs
from scipy.optimize import fmin_l_bfgs_b


import numpy as np
import datetime

def f(x):
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

def fprime(x):
    return np.array((-2*.5*(1 - x[0]) - 4*x[0]*(x[1] - x[0]**2), 2*(x[1] - x[0]**2)))

def hessian(x): # Computed with sympy
    return np.array(((1 - 4*x[1] + 12*x[0]**2, -4*x[0]), (-4*x[0], 2)))

print check_grad(f,fprime, [2, 2])

starttime = datetime.datetime.now()
opt_brute = brute(f, ((-1, 2), (-1, 2)))
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_anneal = anneal(f, [2, 2])
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_min = fmin(f, [2, 2])
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_cg = fmin_cg(f, [2, 2])
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_cg_p = fmin_cg(f, [2, 2], fprime=fprime)
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_ncg = fmin_ncg(f, [2, 2], fprime=fprime)
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_ncg = fmin_ncg(f, [2, 2], fprime=fprime, fhess=hessian)
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_bfgs = fmin_bfgs(f, [2, 2], fprime=fprime)
print (datetime.datetime.now() - starttime).microseconds

starttime = datetime.datetime.now()
opt_lbfgs = fmin_l_bfgs_b(f, [2, 2], fprime=fprime)
print (datetime.datetime.now() - starttime).microseconds


