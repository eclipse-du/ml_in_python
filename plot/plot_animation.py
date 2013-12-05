import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
    if num%2==0:
        line.set_data(data[...,num-2:num])
    return line,

fig1 = plt.figure()

#data = np.random.rand(2, 5)
data = np.array([[0,10,0,10,10,0],[0,10,4,5,6,1]])

l, = plt.plot([], [], 'r-')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 7, fargs=(data, l),interval=500,blit=True)
plt.show()
