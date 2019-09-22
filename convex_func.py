import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from tqdm import tqdm
import random

PLANE_SIZE = 100
# global points, counts
# global points = []
# global count = 0

def scatterplot(points):
    points = np.asarray(points)
    x = points[:,0] 
    y = points[:,1] 
    plt.scatter(x, y, s=10)

def plot_convex(arr):
    print(arr)
    arr = np.concatenate(arr) #into numpy matrix
    print(arr)
    pass

def getData():
    # Opens a file “data.txt” and creates the global list of points
    arr = np.loadtxt('data.txt')
    return arr

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def plot_line_eqation(a,c):
    x = [x for x in range(PLANE_SIZE)]
    y_pred = [(1)*a*x + c for x in range(PLANE_SIZE)]
    plt.plot(x,y_pred)
  

def plot_line(pt1,pt2):
    x = [pt1[0], pt2[0]]
    y = [pt1[1], pt2[1]]
    rgb = random_color()
    for i in range(0, len(x), 2):
        plt.plot(x[i:i+2], y[i:i+2], 'ro-')

def check_distinct(arr):
    if(len(set(arr)) != len(arr)):
        return False
    else:
        return True


def createData(n):
    #generates a global list of n random points with no duplicates
    #ref: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html
    arr = np.random.choice(range(PLANE_SIZE), n*2, replace=False)
    arr = arr.reshape(n,2) #change the dimension
    arr = arr.astype(int)
    np.savetxt('data.txt', arr,header=str(n),fmt='%d')
    return arr








