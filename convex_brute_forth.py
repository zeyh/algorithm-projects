'''
zeyang huang
csc370 algorithm
project 1
sep 19. 2019

different trails in brute force of convex problem
'''
import numpy as np
PLANE_SIZE = 1000

def getData(i):
    # Opens a file “data.txt” and creates the global list of points
    arr = np.loadtxt('convex_num_'+str(i)+'.txt')
    print(arr)
    pass

def createData(n,i):
    #generates a global list of n random points with no duplicates
    arr = np.random.choice(range(PLANE_SIZE), n*2, replace=False)
    arr = arr.reshape(n,2) #change the dimension
    arr = arr.astype(int)
    np.savetxt('convex_num_'+str(i)+'.txt', arr,header=str(n),fmt='%d')
    return arr

def check_distinct(arr):
    if(len(set(arr)) != len(arr)):
        return False
    else:
        return True

def find_line(a, b):
    pass

def check_line_seg(a,b):
    pass

def main():
    label = 1
    createData(300,label)
    getData(label)
    print("fin")

main()