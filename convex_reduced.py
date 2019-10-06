'''
zeyang huang
csc370 algorithm
project 1
oct 4. 2019

different trails in improved brute force of convex hull problem
'''

PLANE_SIZE = 1000
import random

def createData(n):
    '''
    @param: n number of points that will be generated. 
    Note: need to be less than the PLANE_SIZE
    create a random non-repeated points with x,y integer value within the range of PLANE_SIZE
    ref: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html
    '''
    arr = [ [random.randint(0,PLANE_SIZE),random.randint(0,PLANE_SIZE)] for i in range(n)]
    random.shuffle(arr) #make sure no duplicates
    with open('data.txt', 'w') as f:
        f.write("%s\n" % n)
        for pt in arr:
            f.write(str(pt[0])+"\t"+str(pt[1])+"\n")
    return arr


def getData():
    '''
    @return: numpy 2d array containing the x y value of the points
    Opens a file called “data.txt” and creates the global list of points
    '''
    infile = open("data.txt", "r")
    lines = infile.read().split('\n')
    lines = lines[1:-1]  #rm the first size number and the last \n
    out = [[int(line.split('\t')[0]),int(line.split('\t')[1])] for line in lines ] #split by \t for x and y axis of each pt and change str to int
    return out


def getConvexHull():
    '''
    @return: a list (without duplicates) of points in the convex hull – calls checkLineSegment()
    order of the points in the convex hull is not important
    '''
    out = [] #the output result
    for i in range(len(points)):
        for j in range(i,len(points)):
            if(i != j):
                if (checkLineSegment(i,j)):
                    out.append([points[i],points[j]])
    # print("num of edges: ",len(out))
    return out


def checkLineSegment(index1,index2):
    '''
    @param: index1, index2 distinct integers that are indices of two points in the list of points.
    @return: True or False depending on whether the remaining points all lie on one side of the
    line through the two points;  Increments the global count for each point tested
    '''
    global count 
    a,b,c = findLine(index1,index2) #found the line equation
    #*-1 because findLine() returns the form of ax + by = c, but checked using y = -a/bx + c/b (b=1)   
    result1 = []
    result2 = []
    for pt in points:
        if(pt != points[index1] and pt != points[index2]):
            count += 1 #count how many times chekced which side of a line a point lies
            result1.append(int(pt[1] > pt[0]*(-1*a)+c)) #see which side a pt's in
            result2.append(int(pt[1] < pt[0]*(-1*a)+c)) #could just write an if else statement than computing it again

            #early stoppping when criteria met...
            if sum(result1) != 0 and sum(result2) != 0: #if already found lines on both side
                return False

    # result = [sum(i) for i in zip(result1, result2)]
    # count = sum(result) #update the global variable count

    if sum(result1) == len(points)-2 or sum(result2) == len(points)-2: #check if all point lies on the same side besides the two point as bases 
        return True
    else:
        return False


def findLine(index1, index2):
    '''
    @param: index1, index2 distinct integers that are indices of two points in the list of points.
    @return:  a,b,c  which are the constants in the line ax + by = c  which is the line through these two points
    return a line that pass those two indices of points
    '''
    pt1 = points[index1] #get the points
    pt2 = points[index2]
    try:
        a = (pt1[1] - pt2[1])/(pt1[0] - pt2[0]) # according to the line equation y = ax + c
    except ZeroDivisionError:
        a = 0
    c = pt1[1] - a*pt1[0] 

    # plot_line_eqation(a,c) #plot the line using the equation coefficients
    return -a, 1, c # y = ax+c -> -ax + y = c


def main():
    #creates the data with specific number
    data_num = 80

    createData(data_num) #create new data for each iteration
    global points, count 
    count = 0 # the total number of points that are tested
    points = getData()

    result = getConvexHull() # run the core algorithm
    print("results:", result) #3d array returned, eg. [[pt1,pt2],...,[pt2,pt3]]indicate the line segments created by the point's on the convex hull 
        

    # print("fin")
    

if __name__ == '__main__':
    main()