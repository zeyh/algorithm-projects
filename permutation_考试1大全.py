def remove_perm(n):
    '''
    decrease and conquer
    每次循环减去一个值 然后在解决n-1的问题， 递归， 最后把之前除掉的单独的再加回来
    先找第一个with n choices， 然后第二个n-1 ...
    Remove each element from the n elements one at a time, 
    then append it to the (n-1)! remaining permutations.
    递归式:在每一次的递归层次中求出$(n-1)$个元素的全排列。
    递归边界条件:当元素个数为1的时候，直接返回该元素。
    '''


    pass

def insert_perm(arg):
    '''
    已有n-1个数的全排列之后， 将第n个数插入到这些排列所有的可能个数里面
                    1
            21              12
    321 231 213        312 132 123

    minimal change
    '''
    if len(arg)==0:
        return [[]]
    else:
	#得到n-1的排列
        t = insert_perm(arg[1:])
        order = []
        #遍历每一个排列
        for item in t:
            print("item",item)
            #在每一个排列的可能位置中插入当前元素
            for (index,i) in enumerate(item):
                print(index)
                tmp = item[:] #a shallow copy
                tmp.insert(index,arg[0])
                order.append(tmp)
            tmp = item[:]
            tmp.append(arg[0])
            order.append(tmp)
        return order



def lexographic(n):
    '''
    从字典序中最小的序列开始，一直不停寻找下一个仅比上一个序列大的序列，直到到达最大的序列
    试图寻找一种所有排列情况中的顺序关系，
    Find the largest x such that P[x]<P[x+1] - 在x右侧的所有元素都是从大到小排列的. 
    Find the largest y such that P[x]<P[y] - a[x]是仅次于a[y]的数。而将他们交换之后，能保证整个序列是最小增长的。
    P=(5,1,7,6,3,9,8,4,2) x is 5. (For this x we have P[x]=3 and P[x+1]=9.) y=8. 
      (5,1,7,6,4,9,8,3,2) By swapping P[x] and P[y]
      (5,1,7,6,4,2,3,8,9) By reversing the part from index x+1 to the end
      由于a[x+1: n]$中是从大到小排列的，因此需要将这部分倒序，来使得序列进一步减小，使其成为仅大于原始序列的序列。
    '''


    pass


def johnson_trotter(n):
    '''
    arrows! 是寻找一种相邻元素相互交换的顺序
    每次循环都进行一次满足条件的相邻元素的交换，直到不存在满足条件的可交换的元素，此时说明所有排列的情况均已输出，算法结束
    1. 初始化所有元素的移动方向为左，输出序列本身
    2. 移动最大的可移动的元素(当元素移动方向上的元素比自己小时，才能移动) （可能一直在这一步移动）
    3. 反转所有比移动元素大的所有元素的移动方向
    4. 重复2~3步，直到不能移动为止
    123 132 312 321 231 213
    ''' 


    pass


def binary_string_subsets(n):
    '''
    000 001   010     011   100   101        110      111
    ∅   {a3}  {a2} {a2, a3} {a1} {a1, a3} {a1, a2} {a1, a2, a3}
    '''
    pass


def generate_binary(ones, zeroes, str, len1): 
    '''
    1111  1110  1101  1100  1011  1010
    '''
    # If length of current string becomes same as desired length 
    if (len1 == len(str)): 
        print(str,end =" ") 
        return
      
    # Append a 1 and recur 
    generate_binary(ones+1, zeroes, str+"1", len1) 

    # If there are more 1's, append a 0 as well, and recur 
    if (ones > zeroes): 
        generate_binary(ones, zeroes+1, str+"0", len1) 


def main():
    print(insert_perm([1,2,3]))

main()



