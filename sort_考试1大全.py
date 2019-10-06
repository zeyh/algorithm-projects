'''
小黄加油！！d=ԾvԾ
oct 6, 19

lomuto, hoare partition, quick sort, quick select
merge sort, insertion sort
selection sort, bubble sort
'''

def lomuto(a, low, high):
    '''
    更easy to implement， semistable
    '''
    #high从前向后滑动交换
    #每次high碰到小于pivot就合low换 每换一下就增加low
    pivot = a[high] #最后一个是pivot
    i = low - 1 #提前减掉 这样时候不会多一个
    
    for j in range(low, high): #j从前向后滑动
        if a[j] <= pivot: #一旦当前位置小于pivot 等于是因为让他stable　
            i += 1 #把i换了 提前加一是因为 一开始可能是-1 
            a[i],a[j]=a[j],a[i]

    a[i+1],a[high]=a[high],a[i+1]  #停的时候low多算了一个
    return i+1 

def hoare(array, low, high):
    '''
    更efficient， three times fewer swaps on average, unstable
    bidirectionality
    '''
    pivot = array[low] #第一个是pivot 如果最后一个，可能∞
    i=low-1
    j=high+1
    while 1:
        i = i + 1
        while array[i] < pivot:
            i = i + 1

        j = j - 1
        while array[j] > pivot:
            j = j - 1
       
        if i >= j:
            return j
        array[i],array[j]=array[j],array[i]
      

def quick_select(a, low, high, k):
    '''
    divide and conquer
    和quick sort很像， 但是只用循环一边儿
    如果pivot一边比k多， 只用选多的那一边， 正好的话就是了
    average: o(nlogn) - o(n)
    worst case: o(n^2) 实战的话worst case太差了就
    '''
    #找出第k小的数字！
    if (k > 0 and k <= high-low+1): #合理的k输入 因为input是从1开始计数的！
        pivot = lomuto(a,low,high) #hoare一样的 返回的是pivot index, 和改过的数组， 左边比他小， 右边比他大

        if k-1 == pivot - low: #在中间正好分到了
            print("equal",a[k],k)
            return a[pivot] #返回pivot的数值 因为正好分到了
        if k-1 < pivot - low: #左边的比较多
            return quick_select(a,low, pivot-1,k)
        else: #右边的多 
            return quick_select(a,pivot+1, high,k-1 - pivot + low ) #因为array右边的 k的index也要变！！


def quick_sort(a,low,high):
    '''
    divide and conquer
    partition 可以最前的 最后的 （random 或者median）
    worst case： already sorted, duplicate- O(n^2)
    best case： pivot总是在中间 - O(nlogn)
    average case： T(n) = T(n/9) + T(9n/10) + Theta(n) -> O(nlogn)
    实战： 比merge sort更快一点， 因为worst case可以通过选各种pivot策略 避免发生太多
          subarray很小的时候可以call insertion sort
    '''
    if low < high:  #合理的输入，小大分别在左右
        pivot = hoare(a,low, high)
        # quick_sort(a, low, pivot-1) #for lumoto 减1是因为把最后一个当成了pivot 如果不减，左边的始终是最后一个，没有更新，就会一直循环
        quick_sort(a, low, pivot) #not pivot -1 for hoare 递归排序右边 小的部分 没减是因为第一个是默认pivot i，j两边向中间逼近
        quick_sort(a, pivot+1, high) #递归排序右边 大的部分
    return a

def merge_sort(arr):
    '''
    divide and conquer 
    分成每个数成一组， 两两 有序 合并， 直到只剩下一组
    '''
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
        
        i = j = k = 0 #k记录所有的分好了没
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1       
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1     
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def insertion_sort(a):
    '''
    decrease and conquer
    扑克牌排序 新的牌 按顺序 插到老的牌堆里面
    time： O(n^2)
    space： O(1)
    worst case: reversed order 
    best case: already sorted O(n)
    适用：小数组 或者 快sort好了的时候 只有几个错位
    增进：可以和binary search一起用，用他寻找位置， 这样里面就是O(logn)时间了
         linked list: 新建一个新的result list， 把当前i插入到result list里面， 最后直接改head 从input list到result list
    '''
    for i in range(1,len(a)):
        key = a[i]
        #i已经存到key里面了 把i前面的所有向后挪一个位置，覆盖掉i, 直到key的位置空出来了
        j = i-1
        while j>= 0 and key < a[j]: #j >= 0因为第一个插入的不用搜索位置， 或者倒着搜索到第一个了 要停了
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key #加1因为 循环最后 多减了一个
    return a

def selection_sort(a):
    '''
    brute force
    分成两个部分 排好的 和没排的
    0 到 n-1 找最小的和0交换
    1 到 n-1 找最小的和1交换
    ......
    排好了
    time: O(n^2) comparisons, O(n) (n-1)swaps for all cases
    '''
    for i in range(len(a)):
        #找最小的
        min_idx = i
        for j in range(i+1, len(a)): #在没排的范围内找最小的 所以是从i+1开始loop
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] #找着相对最小的了 就交换
    return a

def bubble_sort(a):
    '''
    brute force
    以第一个人为基准，如果没排好，那就换临近俩人， 然后再来n-2遍 直到排好了， 因为每走一遍， 就能确保至少最后是最大的
    需要多走一遍 发现没换 才知道排好了
    time O(n^2) 
    best case: O(n) if sorted 需要改进， 如果没有swap 那么提前结束
    worst case O(n^2)reverse sorted
    '''
    for i in range(len(a)):
        for j in range(len(a)-i-1): #优化了已经
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def main():
    arr = [ 7, 8,1, 9, 10, 5]
    # print("after sorting: ",qsort(arr,0, len(arr)-1)) 
    # print('kth smallest element is ', qselect(arr, 0, len(arr)-1,5))
    # print("insertion sort: ", insertion_sort(arr))
    # print("merge sort: ", merge_sort(arr))
    # print("selection sort: ", selection_sort(arr))
    print("bubble sort: ", bubble_sort(arr))
main()
