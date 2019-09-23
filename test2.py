import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from convex_func import *


points = getData()
x = points[:,0] 
y = points[:,1] 


fig, ax = plt.subplots()
ax.set(xlim=(-200,1200),ylim=(-200,1200))
ax.scatter(x, y, s=10, color = 'r')
line, = ax.plot([], [], lw=2)
# def update_line(num, data, line):
#     line.set_data(data[..., :num])
#     return line,

def findLine(index1, index2):
    # the parameters are indices of two points in the list of points.  They are distinct
    # returns three values:  a,b,c  which are the constants in the line ax + by = c  which is the line through
    # these two points
    # return a line that pass those two indices of points
    pt1 = points[index1]
    pt2 = points[index2]
    a = (pt1[1] - pt2[1])/(pt1[0] - pt2[0])
    c = pt1[1] - a*pt1[0] 
    
    # sanity check, has some float rounding issue but for the current plane scale doesn't matter
    # print(a*pt1[0] + c, pt1[1])
    # print(a*pt2[0] + c, pt2[1])
    return -a, 1, c # y = ax+c -> -ax + y = c

def init():
    # a,b,c = findLine(1,2)
    # x = [x for x in range(PLANE_SIZE)]
    # y_pred = [a*x + c for x in range(PLANE_SIZE)]
    # line = ax.plot(x, y_pred, color='r')
    line.set_data([], [])
    return line,

def update_line(i):
    a,b,c = findLine(1,i)
    print(max(points[1],points[i]))
    x = [x for x in range(100)]
    y_pred = [a*x + c for x in range(PLANE_SIZE)]
    line.set_data(x, y_pred)
    return line,


line_ani = animation.FuncAnimation(
    fig, update_line, init_func=init, 
    interval=22,frames=200, blit=True)


plt.show()