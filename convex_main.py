'''
zeyang huang
csc370 algorithm
project 1
sep 19. 2019

different trails in brute force of convex problem
'''
from convex_func import *

def getConvexHull():
    '''
    @return: a list (without duplicates) of points in the convex hull – calls checkLineSegment()
    order of the points in the convex hull is not important
    '''
    out = []
    for i in range(len(points)):
        for j in range(i,len(points)):
            if(i != j):
                # print("----",points[i],points[j])
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
    
    a,b,c = findLine(index1,index2)
    # count += 1 #check how many lines checked
    #*-1 because findLine() returns the form of ax + by = c, but checked using y = -a/bx + c/b (b=1)   
    result1 = []
    result2 = []
    for pt in points:
        if(pt != points[index1] and pt != points[index2]):
            count += 1 #count how many times chekced which side of a line a point lies
            result1.append(int(pt[1] > pt[0]*(-1*a)+c))
            result2.append(int(pt[1] < pt[0]*(-1*a)+c))
            # print("::",pt)
            # print(result1,result2)
            
            #early stoppping...
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
    a = (pt1[1] - pt2[1])/(pt1[0] - pt2[0]) # according to the line equation y = ax + c
    c = pt1[1] - a*pt1[0] 
    plot_line(points[index1],points[index2])  #plot the line using two pts given
    # plot_line_eqation(a,c) #plot the line using the equation coefficients
    return -a, 1, c # y = ax+c -> -ax + y = c


def plot_graphs(result):
    '''
    @param: result: 2d array for the convex points
    plot the graph accordingly
    '''
    #plot the graphs
    plot_convex(result)
    scatterplot(points)
    plt.show() 


def main():
    #repeated num for each trail
    repeat_num = 20 
    #creates the data with specific number
    data_num = 5
    # generate the arr of [ 5 10 20 40 80] by noticing the log scale of required input space using geometric space and round to nearest 10
    # insert the 5 again because of the mod 10 that would mod 5 to 0
    input_arr = np.insert(np.around(np.geomspace(data_num, 80, num=5, dtype=int)[1:], decimals=-1),0,data_num)

    for input_num in input_arr:
        count_list = [] #keep record of each count 
        for tmp in tqdm(range(repeat_num)):
            createData(input_num) #create new data for each iteration
            global points, count 
            count = 0 # the total number of points that are tested
            points = getData().tolist() # a list of the ordered pairs of the points    
            result = getConvexHull() # run the core algorithm
            # #plot the graphs
            # plot_graphs(result)
            count_list.append(count)

        print("-------->", input_num, count_list) 
        #if check all the points it is: n * (n-1) * (1/2) * (n-3) # num of points * num of lines * 1/repeated counts * num of rest points
        print("overall count of checking: ", int(input_num*(input_num-1)*(input_num-2)/2)) 
        print("optimized count of checking mean: ", np.mean(count_list), "sd: ", np.std(count_list))
        
    # plot_results()

    plt.show()
    print("fin")
    

if __name__ == '__main__':
    main()