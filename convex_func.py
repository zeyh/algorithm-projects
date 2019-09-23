import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from tqdm import tqdm
import random
import os

PLANE_SIZE = 100 #the max value that a random point would be
# global points = []
# global count = 0

def scatterplot(points):
    '''
    @param: 2d integer list points contains the axis values of each point
    plot the whole dataset readed in into a scatter plot
    '''
    points = np.asarray(points) #into numpy array
    x = points[:,0] #get the first and second column seperatively
    y = points[:,1] 
    plt.scatter(x, y, s=10) 

def plot_convex(arr):
    '''
    @param: arr, 2d list geneated by the getConvexHull()
    mark and plot the convex boundary as blue
    '''
    arr = np.concatenate(arr) #stacked into numpy matrix
    x = arr[:,0] #get the first and second column seperatively
    y = arr[:,1]
    rgb = random_color()
    for i in range(0, len(x), 2): #plot every pair of points in the array
        plt.plot(x[i:i+2], y[i:i+2], 'bo-')

def getData():
    '''
    @return: numpy 2d array containing the x y value of the points
    Opens a file called “data.txt” and creates the global list of points
    '''
    arr = np.loadtxt('data.txt')
    return arr

def random_color():
    '''
    @return: a tuple of generated rgb values
    generate random numbers between 0-255 for ploting
    '''
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def plot_line_eqation(a,c):
    '''
    @param: a,c float number indicating the line equation: y=ax+c
    plot the line based on the input equation y=ax+c
    '''
    x = [x for x in range(PLANE_SIZE)] #generate x in the range of plane size
    y_pred = [(1)*a*x + c for x in range(PLANE_SIZE)] #generate y accordingly
    plt.plot(x,y_pred)
  

def plot_line(pt1,pt2):
    '''
    @param: pt1, pt2 1d list of the [x,y] value of a point
    plot a line between those two points based on their location information
    '''
    x = [pt1[0], pt2[0]] #get the position value
    y = [pt1[1], pt2[1]]
    rgb = random_color()
    for i in range(0, len(x), 2): #plot the line with red dot
        plt.plot(x[i:i+2], y[i:i+2], 'ro-')

def check_distinct(arr):
    '''
    @param: arr a 2d list of integers
    @return: True is all elements are distinct inside the list, False otherwise
    check if the 2d list's elements are all distinct
    '''
    if(len(set(arr)) != len(arr)): # if the distinct set's length is the same
        return False
    else:
        return True

def browsefolder_newname(path, filestartname, filetype):
    '''
    @param: path: string of folder name, 
            filestartname: the common name that all saved file has to diff with others
            filetype: string of file type
    @return: a string that is a number which is current max+1
    traverse the all the files satisfy the type within a given folder
    return an approprate name for dealing with duplicates
    '''
    approx_name = "" #the approprate name that will be returned 
    filenames = [] # the temp list hold all qualified filenames
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((filetype)) and name.startswith((filestartname)): 
                name_temp = name.replace("."+filetype,"") # remove  .txt from string
                name_temp = name_temp.replace(filestartname,"") #remove data from string 
                if name_temp != "":
                    filenames.append(name_temp) #only get the number label
    if filenames != []:
        intnames = []
        for name in filenames:
            try:
                intname = int(name) #see if its a valid int label
                intnames.append(intname)
            except:
                pass
        maxint = max(intnames) #find out the curr max label
        approx_name = str(maxint+1) #get the one for the next file saved
    else:
        approx_name = "1" # if only data.txt exists
    return approx_name


def createData(n):
    '''
    @param: n number of points that will be generated. 
    Note: need to be less than the PLANE_SIZE
    create a random non-repeated points with x,y integer value within the range of PLANE_SIZE
    ref: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html
    '''
    arr = np.random.choice(range(PLANE_SIZE), n*2, replace=False)
    arr = arr.reshape(n,2) #change the dimension
    arr = arr.astype(int)
    if os.path.exists('data.txt'):
        #deal with duplicated files
        # replace = input('data.txt already exists, do you want to replace it? (y/n):  ')
        replace = 'y' 
        if (replace == 'y'):
            np.savetxt('data.txt', arr,header=str(n),fmt='%d')
        else:
            name = browsefolder_newname("./",'data',"txt") #./ indicates to browse the all files under current directory
            np.savetxt('data'+name+'.txt', arr,header=str(n),fmt='%d')
    return arr








