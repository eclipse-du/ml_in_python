#!/usr/bin/python
# -*- coding: utf-8 -*-

# author  : eclipse
# email   : adooadoo@163.com

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import sys

# global parameter

step = 0  # animation step


def loadData(in_file):
    """
    Description:
    load from in_file,spliting with ','
    take it into array
    ****************************************
    Parameters:
    in_file   :data source
    ****************************************
    Return:
    dataArray:data in the type of Array(Numpy.Array)
    """

    with open(in_file) as f:
        data = [line.strip('\n').split(',') for line in f]
    dataArray = np.matrix(data, dtype=float)
    return dataArray


def getLine(xRange, theta):
    """
    Description  :
    get the line of our linear regression
    ****************************************
    Parameters:
    xRange       :x's range in the figure
    theta        :Parameter of the line,
                  ex:y=a+bx,lineParameter of X
    ****************************************
    Return       :
    line         :return a line in Type of Line2D in pylab
    """

    return plt.Line2D(xRange, [xRange[0] * theta[0, 1] + theta[0, 0],
                      xRange[1] * theta[0, 1] + theta[0, 0]])


def press(event):
    """
    Description  :
    when press the KEY x,figure will repaint,
    using a new theta,saved in theta_history
    ****************************************
    Parameters:
    event        :key press event
    ****************************************
    """

    global step

    # print('press', event.key)

    sys.stdout.flush()

    # ignore other keys

    if event.key == 'x':
        ax.lines = []
        line2 = getLine(list(ax.axis()[0:2]), theta_history[step])
        line2.set_color('g')
        line2.set_linewidth(4)
        step = step + 1
        ax.add_line(line2)
        fig1.canvas.draw()


def computeCost(X, y, theta):
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

    return 1.0 / (2 * X.shape[0]) * np.sum(np.power(theta * X.T - y.T,
            2))


def gradientDescent(
    X,
    y,
    theta,
    alpha,
    num_iters,
    ):
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

    # Initialize some useful values

    m = X.shape[0]
    X = np.concatenate((np.ones([m, 1]), X), 1)

    # J_history = np.zeros(num_iters)

    theta_history = []

    for i in range(0, num_iters):
        theta = theta - alpha / m * ((theta * X.T - y.T) * X)
        theta_history.append(theta)

        # print computeCost(X, y, theta);

    return (theta, theta_history)


def update_line(num, data, line):
    """
    Description  :
    Automatic update line
    ****************************************
    Parameters   :
    num          :timer(inner function,don't need to feed)
    data         :inputdata(all 2D points)
    line         :line will be ploted
    ****************************************
    Return       :
    line         :line sequence
    """

    if num % 2 == 0:
        line.set_data(data[..., num - 2:num])
    return (line, )


# Main function
# load data into array(type is float)

data = loadData('ex1data1.txt')
m = data.shape[0]
n = data.shape[1]  # number of feature
X = data[:, 0:data.shape[1] - 1]
y = data[:, data.shape[1] - 1]

# compute the Gradian Descent

theta = np.matrix([0] * n)
computeCost(np.concatenate((np.ones([m, 1]), X), 1), y, theta)
iterations = 1500
alpha = 0.01
(theta, theta_history) = gradientDescent(X, y, theta, alpha, iterations)

# init the figure1,which need to press X to continue

fig1 = plt.figure()
fig1.figsize = (2, 2)
ax = fig1.add_subplot(111)
ax.scatter(X, y, s=50, marker='o', c='r')

# init the regression line

line1 = getLine(list(ax.axis()[0:2]), np.matrix([0, 0]))
line1.set_color('g')
line1.set_linewidth(4)
ax.add_line(line1)

# set figure1 paremeter

plt.title('Regression data')
plt.xlabel('Population of a city(Press X to continue)')
plt.ylabel('Profit of a food truck')

# set the Key Event

fig1.canvas.mpl_connect('key_press_event', press)
fig1.savefig('key_line.png')

# init the figure2,which is automatic run

fig2 = plt.figure()
fig2.figsize = (3, 3)
ax2 = fig2.add_subplot(111)
ax2.scatter(X, y, s=50, marker='o', c='r')
Xrange = list(ax2.axis()[0:2])
YPoint = []

[YPoint.append(t[0, 0] + Xrange[0] * t[0, 1]) or YPoint.append(t[0, 0]
 + Xrange[1] * t[0, 1]) for t in theta_history]  # it just get all the y in f(x)
data = np.array([Xrange * iterations, YPoint])
(l, ) = plt.plot([], [], 'b-', linewidth=3)
plt.title('Regression data(Auto)')
line_ani = animation.FuncAnimation(
    fig2,
    update_line,
    50,
    fargs=(data, l),
    interval=500,
    blit=True,
    )
fig2.savefig('auto_line.png')

# init the figure3,which is surfing

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)
J_vals = np.zeros([len(theta0_vals), len(theta1_vals)])
for i in range(0, len(theta0_vals)):
    for j in range(0, len(theta1_vals)):

    # print theta0_vals[i],theta1_vals[j]

        t = [theta0_vals[i], theta1_vals[j]]
        J_vals[i, j] = computeCost(np.concatenate((np.ones([m, 1]), X),
                                   1), y, t)

J_vals = J_vals.T
(theta0_vals, theta1_vals) = np.meshgrid(theta0_vals, theta1_vals)
fig3 = plt.figure()
ax3 = fig3.gca(projection='3d')
surf = ax3.plot_surface(theta0_vals, theta1_vals, J_vals)
fig3.savefig('3d_surf.png')

# init the figure4,which is contour

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
plt.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20))
fig4.savefig('contour_log.png')
plt.show()
