import pylab as pl
import numpy as np
import sys

step=1

def getLine(xRange,lineParameter):
    return pl.Line2D(xRange,[xRange[0]*lineParameter[0]+lineParameter[1],xRange[1]*lineParameter[0]+lineParameter[1]],linewidth=3,color='g')

def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key=='x':
	ax.lines=[]
	line2 = getLine(xRange,np.random.rand(2))
	ax.add_line(line2)
        fig.canvas.draw()

fig = pl.figure()
fig.figsize=(2,2)
fig.canvas.mpl_connect('key_press_event', press)
ax=fig.add_subplot(111)
  
#ax = fig.add_axes([0.1,0.1,0.8,0.8])
#line1 = pl.Line2D([0,1],[0.5,-0.5],transform=fig.transFigure,figure=fig,color='r')


X = np.array([[1,2],[2,2],[1,1],[0,0],[-1,1],[2,-1]])
lineParameter = [-1,0.3]
ax.scatter(X[:,0], X[:,1],50,'r','o')
xRange = list(ax.axis()[0:2])
line1 = getLine(xRange,lineParameter)
ax.add_line(line1)
pl.show()

