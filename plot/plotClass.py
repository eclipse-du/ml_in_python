
import pylab as pl
import numpy as np

X = np.array([[1,2],[2,2],[1,1],[0,0],[-1,1],[2,-1]])
y = np.array([1,2,1,2,1,2])
colorType = ['r','b']
#fig = pl.figure()
#ax = fig.add_subplot(111)
pl.scatter(X[:,0], X[:,1], 100.0*y, [colorType[i-1] for i in y])
#pl.legend( ('label1', 'label2') )
pl.show()

