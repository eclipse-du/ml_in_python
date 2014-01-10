#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
from scipy.optimize import fmin
from scipy.optimize import fmin_powell
import datetime

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
starttime = datetime.datetime.now()
xopt = fmin_powell(rosen, x0, xtol=1e-8)
print xopt
endtime = datetime.datetime.now()
interval=(endtime - starttime)
print interval


starttime = datetime.datetime.now()
xopt = fmin(rosen, x0, xtol=1e-8)
print xopt
endtime = datetime.datetime.now()
interval=(endtime - starttime)
print interval

