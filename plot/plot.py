#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author  : eclipse
# email   : adooadoo@163.com
# method  : to plot things using pylab
#           with two classes 

import pylab as pl
import numpy as np

X = np.array([[1,2],[2,2],[1,1],[0,0],[-1,1],[2,-1]])
y = np.array([1,1,1,-1,-1,-1])
pos = np.array([X[i] for i in range(np.size(y)) if y[i]==1])
neg = np.array([X[i] for i in range(np.size(y)) if y[i]==-1])
#print y1
#y2 = np.array([0 if i==1 else 1 for i in y])
pl.axis([-4,4,-4,4])
pl.plot(pos[:,0],pos[:,1],'ro',label='positve',markersize=10)
pl.plot(neg[:,0],neg[:,1],'gv',label='negative',markersize=10)

#pl.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
#pl.plot([1,2,3], [-1,-2,-2.5], 'rs',  label='line 2')
pl.legend()
pl.show()

