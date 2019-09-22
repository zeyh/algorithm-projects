'''
zeyang huang
csc370 algorithm
project 1
sep 19. 2019

different trails in brute force of convex problem
'''
from convex_func import *



def getConvexHull():
    # returns the list (without duplicates) of points in the convex hull – calls checkLineSegment()
    # order of the points in the convex hull is not important
    out = []
    for i in tqdm(range(len(points))):
        for j in range(i,len(points)):
            temp_pt = []
            if(i != j):
                if (checkLineSegment(i,j)):
                    out.append([points[i],points[j]])
    print("num of edges: ",len(out))
    return out


def checkLineSegment(index1,index2):
    # the parameters are indices of two points in the list of points.  They are distinct
    # returns True or False depending on whether the remaining points all lie on one side of the
    # line through the two points;  Increments the global count for each point tested
    a,b,c = findLine(index1,index2)
    #*-1 because findLine() returns the form of ax + by = c, but checked using y = -a/bx + c/b (b=1)   
    result1 = []
    result2 = []
    for pt in points:
        if(pt != points[index1] and pt != points[index2]):
            result1.append(int(pt[1] > pt[0]*(-1*a)+c))
            result2.append(int(pt[1] < pt[0]*(-1*a)+c))

    # result = [sum(i) for i in zip(result1, result2)]
    # count = sum(result) #update the global variable count
    # print(points[index1], points[index2],result1,result2)
    # print(sum(result))
    if sum(result1) == len(points)-2 or sum(result2) == len(points)-2: 
        return True
    else:
        return False


def findLine(index1, index2):
    # the parameters are indices of two points in the list of points.  They are distinct
    # returns three values:  a,b,c  which are the constants in the line ax + by = c  which is the line through
    # these two points
    # return a line that pass those two indices of points
    pt1 = points[index1] #get the points
    pt2 = points[index2]
    a = (pt1[1] - pt2[1])/(pt1[0] - pt2[0]) # according to the line equation y = ax + c
    c = pt1[1] - a*pt1[0] 
    plot_line(points[index1],points[index2])  #plot the line using two pts given
    # plot_line_eqation(a,c) #plot the line using the equation coefficients
    return -a, 1, c # y = ax+c -> -ax + y = c


def main():
    
    createData(10)
    global points, count 
    points = getData().tolist() # a list of the ordered pairs of the points
    count = 0 # the total number of points that are tested
    
    print(points)
    # checkLineSegment(2,6)
    result = getConvexHull()
    plot_convex(result)
    scatterplot(points)
    plt.show()
    print("fin")
    

main()