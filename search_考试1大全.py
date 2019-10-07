'''
sequential search, w/ sentinel, string match, binary search, unique element,(intropolation search)
'''

def binary_search_recursion(a,l,r,k):
    '''
    更新的时候要原有基础+/-1 才能保证不会一直循环
    查不了最开始和结束的。。。。 qvq
    '''
    if r>=1:
        
        mid = int(l+ (r-l)/2) #middle不要小数点后的 round down using int() 
        print(l,r, mid)
        if a[mid] == k: #如果中间就是了
            return mid
        if l >= r:
            return -1
        elif a[mid] > k: #猜测太大了， 所以选左边的 
            return binary_search_recursion(a, l, mid-1, k)  #选择左边部分 更新的时候 原有基础-1

        else:
            return binary_search_recursion(a, mid+1, r, k) #选择左边部分 更新的时候 原有+1!!

def binary_search(a,l,r,k):
    '''
    一定要sort之后的array
    T(n) = T(n/2) + c 
    worst case, average: O(logn)
    best case: O(1)
    '''
    while l<= r:
        mid = int(l+ (r-l)/2)
        if a[mid] == k: #如果中间就是了
            return mid
        elif a[mid] > k: #猜测太大了， 所以选左边的 
            l = mid+1
        else:
            r = mid-1
    return -1

def BruteForceStringMatch(T, P):
    # //Implements brute-force string matching
    # //Input: An array T [0..n − 1] of n characters representing a text and // an array P [0..m − 1] of m characters representing a pattern //Output: The index of the first character in the text that starts a
    # // matching substring or −1 if the search is unsuccessful for i ← 0 to n − m do
    # j←0
    # while j < m and P [j ] = T [i + j ] do
    # j←j+1 ifj =mreturni
    # return −1
    n = len(T)
    m = len(P)
    for i in range(0, n-m):
        j = 0
        while j <m and P[j] == T[i+j]:
            j += 1
        if j == m:
            return i
    return -1


def SequentialSearch(A, k):
    # SequentialSearch(A[0..n − 1], K)
    # //Searches for a given value in a given array by sequential search
    # //Input: An array A[0..n − 1] and a search key K
    # //Output: The index of the first element in A that matches K // or −1 if there are no matching elements
    # i←0
    # while i < n and A[i] ̸= K do
    # i←i+1 if i < n return i
    # else return −1
    i = 0
    n = len(A)
    while i<n and A[i] != k:
        i += 1
    if i<n:
        return i
    else:
        return -1


def SequentialSearch2(A, K):
    # //Implements sequential search with a search key as a sentinel
    # //Input: An array A of n elements and a search key K
    # //Output: The index of the first element in A[0..n − 1] whose value is // equal to K or −1 if no such element is found
    # A[n]←K
    # i←0
    # while A[i]  != K do
    # i←i+1 if i < n return i
    # else return −1
    A.append(K)
    i = 0
    while A[i] != K:
        i = i+1
    if i<len(A)-1:
        return i
    else:
        return -1

def euclid(m,n):
    #Computes gcd(m, n) by Euclid’s algorithm
    #Input: Two nonnegative, not-both-zero integers m and n 
    #Output: Greatest common divisor of m and n
    # m mod n always < n
    # stop because n becomes smaller
    while (n != 0):
        r = m % n
        print(r)
        # print("m=",m,"n=",n)
        m = n
        n = r
    return m
    
def main():
    arr = [ 7, 8,1, 9, 10, 5]
    print(binary_search(arr, 0, len(arr)-1, 7))

main()