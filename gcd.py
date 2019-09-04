# chap 1.1 - 2.4
# Sep 1, 19
import math
import time, tqdm


def UniqueElements(A):
    # UniqueElements(A[0..n − 1])
    # //Determines whether all the elements in a given array are distinct
    # //Input: An array A[0..n − 1]
    # //Output: Returns “true” if all the elements in A are distinct // and “false” otherwise
    # for i ← 0 to n − 2 do
    # for j ← i + 1 to n − 1 do
    # if A[i ] = A[j ] return false
    # return true
    pass

def MaxElement(A):
    # ALGORITHM MaxElement(A[0..n − 1])
    # //Determines the value of the largest element in a given array
    # //Input: An array A[0..n − 1] of real numbers //Output: The value of the largest element in A maxval ← A[0]
    # for i ← 1 to n − 1 do
    # if A[i] > maxval maxval ← A[i]
    # return maxval
    maxval = A[0]
    for i in range(len(A)):
        if A[i] > maxval:
            maxval = A[i]
        return maxval

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

def ComparisonCountingSort(l):
    '''
    //Sorts an array by comparison counting
    //Input: Array A[0..n − 1] of orderable values //Output: Array S[0..n − 1] of A’s elements sorted // in nondecreasing order
    for i ← 0 to n − 1 do
    Count[i]←0 for i ← 0 to n − 2 do
    for j ← i + 1 to n − 1 do if A[i ] < A[j ]
    Count[j]←Count[j]+1 else Count[i] ← Count[i] + 1
    for i ← 0 to n − 1 do S[Count[i]]←A[i]
    return S
    '''
    pass


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

def consecutive_check(m,n):
    # not work correctly when one of its input numbers is zero
    t = min(m,n)
    while (t >= 0):   
        print(t, end = ",")
        r = m % t
        print(r)
        if r == 0:
            r2 = n % t
            if r2 == 0:
                return t
        t = t-1

def middle_school(m,n):
    m1 = primeFactors(m)   
    n1 = primeFactors(n)   
    # print(m1)
    # print(n1)
    out = common_member(m1,n1)
    return multiplyList(out)

def multiplyList(myList) : 
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  

def common_member(a, b): 
    out = []
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        out = a_set & b_set
    else: 
        print("No common elements")  
    return out

def primeFactors(n):   
    out = [] 
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        out.append(2)
        n = n / 2    
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):    
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            out.append(i)
            n = n / i          
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        out.append(n)
    return out

def main():
    start_time = time.time()
    print(euclid(0,12))
    elapsed_time = time.time() - start_time
    print("1", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), "- time for match_freq()")
    
    start_time = time.time()
    print(consecutive_check(12,0))
    elapsed_time = time.time() - start_time
    print("2",time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), "- time for match_freq()")
 
    start_time = time.time()
    print(middle_school(1221,1234567891011121314151617181920212223242526272829))
    elapsed_time = time.time() - start_time
    print("3",time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), "- time for match_freq()")
 
    print("fin")

main()