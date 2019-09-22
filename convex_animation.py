import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from convex_func import *

# global var to establish the axis
fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def checkLineSegment(index1,index2):
    # the parameters are indices of two points in the list of points.  They are distinct
    # returns True or False depending on whether the remaining points all lie on one side of the
    # line through the two points;  Increments the global count for each point tested
    a,b,c = findLine(index1,index2)
                               
    result = [ int(pt[1] > pt[0]*a+c) for pt in points]
    count = sum(result)
    # print(sum(result))
    if sum(result) == len(points):
        return True
    else:
        return False

def findLine(index1, index2):
    # the parameters are indices of two points in the list of points.  They are distinct
    # returns three values:  a,b,c  which are the constants in the line ax + by = c  which is the line through
    # these two points
    # return a line that pass those two indices of points
    pt1 = points[index1]
    pt2 = points[index2]
    a = (pt1[1] - pt2[1])/(pt1[0] - pt2[0])
    c = pt1[1] - a*pt1[0] 
    return a,1,c

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,


def main():
    global points, count 
    points = getData()
    # getConvexHull()
    ani = animation.FuncAnimation(
        fig, animate, init_func=init, interval=2, blit=True, save_count=50)

    # To save the animation, use e.g.
    #
    # ani.save("movie.mp4")
    #
    # or
    #
    # from matplotlib.animation import FFMpegWriter
    # writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save("movie.mp4", writer=writer)

    plt.show()

main()