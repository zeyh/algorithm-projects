import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from tqdm import tqdm
import random
import os

PLANE_SIZE = 1000 #the max value that a random point would be
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
    for i in range(0, len(x), 2): #plot every pair of points in the array
        plt.plot(x[i:i+2], y[i:i+2], 'bo--')

def getData():
    '''
    @return: numpy 2d array containing the x y value of the points
    Opens a file called “data.txt” and creates the global list of points
    '''
    arr = np.loadtxt('data.txt')
    return arr

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

def plot_results():
    '''
    plot the result's trend lines and compare to see if its O(n^3)
    '''
    #dont want to run the whole process again so just pasting the terminal output here directly...
    a_5 = [26, 26, 27, 27, 25, 27, 27, 27, 25, 26, 25, 26, 27, 27, 27, 26, 26, 25, 25, 24]
    a_10 = [191, 169, 193, 176, 175, 206, 185, 149, 166, 199, 167, 156, 185, 193, 205, 188, 203, 179, 181, 176]
    a_20 = [807, 714, 910, 823, 861, 1098, 1025, 930, 724, 971, 834, 663, 775, 908, 1082, 950, 1008, 895, 743, 1105]
    a_40 = [3771, 4838, 5370, 3225, 4834, 3402, 3601, 3923, 4929, 3981, 3959, 3170, 3526, 4500, 4036, 4061, 4790, 3972, 4250, 4135]
    a_80 = [16512, 14982, 23892, 13341, 19379, 15445, 14981, 14778, 13921, 15792, 14949, 16311, 15316, 25922, 15988, 21935, 16734, 17693, 19431, 19435]


    # fig, ax = plt.subplots()

    data_num = np.array([5,10,20,40,80])
    #create the first column of total number of points for the 20 trails
    x_col = np.repeat(data_num, 20)
    #concat the results together
    y_col = np.concatenate((a_5, a_10,a_20,a_40,a_80))
    #stack the two column together to plot
    table = np.stack((x_col, y_col), axis=-1)
    scatterplot(table)

    mean = [27, 182, 891, 4114, 17337]
    plt.scatter(data_num, mean, s=10, c="r", label="Average Count") 
    plt.plot(data_num, mean, '-ro', label= "Actual Points")
    plt.xlabel('total num of points')
    plt.ylabel('num of times checking')
    

    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(0, 80, 1000)
    y = x**2
    z = x**3
    k = x*np.log(x)
    actual = [30, 360, 3420, 29640, 246480]
    # fig, ax = plt.subplots()
    plt.plot(x, y, "y", label="O(n^2)", linestyle="--")
    plt.plot(x, z, "y", label="O(n^3)",linestyle=":")
    plt.plot(x, k, "y", label="O(nlogn)",linestyle="-.")
    plt.plot(data_num, actual, "bo-", label="Worst Case")

    plt.legend(["Average Case","O(nlogn)","O(n^3)" ,"O(n^2)","Worst Case","Actual Points"])

def worst_case_plot(data_num):
    # data_num = 20
    out = []
    angle = [random.uniform(0,1)*(np.pi*2) for i in range(data_num)]
    x = [ (np.cos(angle[i])+1)*PLANE_SIZE/2 for i in range(data_num)]
    y = [ (np.sin(angle[i])+1)*PLANE_SIZE/2 for i in range(data_num)]
    x = np.asarray(x).astype(int)
    y = np.asarray(y).astype(int)
    # plt.scatter(x.T, y, s=10) 
    out = np.stack((x, y), axis=-1)
    print(out)
    return out.tolist()









