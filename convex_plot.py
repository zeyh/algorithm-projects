import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from convex_func import *

# global var to establish the axis
fig, ax = plt.subplots()
points = getData()
x = points[:,0]
y = points[:,1]
plt.scatter(x, y, s=10)
line, = ax.plot(x, np.sin(x))

def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def plot_line(a,c):
    x = [x for x in range(PLANE_SIZE)]
    y_pred = [a*x + c for x in range(PLANE_SIZE)]
    plt.plot(x, y_pred, color='r')

def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,

def main():
    global points, count 
    points = getData()
    # getConvexHull()
    ani = animation.FuncAnimation(
        fig, animate, init_func=init, interval=2, blit=True, save_count=50)


    plt.show()

main()