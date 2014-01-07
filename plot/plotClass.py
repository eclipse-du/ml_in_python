#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author  : eclipse
# email   : adooadoo@163.com

import pylab as pl
import numpy as np

X = np.array([[1,2],[2,2],[1,1],[0,0],[-1,1],[2,-1]])
y = np.array([1,2,1,2,1,2])
colorType = ['r','b']
pl.scatter(X[:,0], X[:,1], 100.0*y, [colorType[i-1] for i in y])
#pl.legend( ('label1', 'label2') )
pl.show()

