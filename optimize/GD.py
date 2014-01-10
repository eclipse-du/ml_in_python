#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
import math
import numpy as np

def error(u,v):
    return math.exp(u)+math.exp(2*v)+math.exp(u*v)+u*u-2*u*v+2*v*v-3*u-2*v

def error_prime(u,v):
    u_p = math.exp(u)+v*math.exp(u*v)+2*u-2*v-3
    v_p = 2*math.exp(2*v)+u*math.exp(u*v)-2*u+4*v-2
    return u_p,v_p

def create_hessian(u,v):
    u_p2 = math.exp(u)+v*v*math.exp(u*v)+2
    v_p2 = 4*math.exp(2*v)+u*u*math.exp(u*v)+4
    uv     = math.exp(u*v)+u*v*math.exp(u*v)-2
    return np.array([[u_p2,uv],[uv,v_p2]])

u=0
v=0
for i in xrange(0,5):
    u_p,v_p = error_prime(u,v)
    u = u - 0.01 *u_p
    v = v - 0.01 *v_p
    #print error(u,v)
    
u=0
v=0
for i in xrange(0,5):
    p_hess = np.linalg.pinv(create_hessian(u,v))
    e = np.array(list(error_prime(u,v)))
    update = np.dot(p_hess,e)
    u = u - update[0]
    v = v - update[1]
    print error(u,v)