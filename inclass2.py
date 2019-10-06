'''
chap3 sorting algorithms
sep 10
'''
import numpy as np
import random

def qsort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i<=pivot]
    greater = [i for i in arr[1:] if i>pivot]
    return qsort(less) + [pivot] + qsort(greater)

def qselect(a, k):
    l = 0
    r = len(a)-1
    #return the smallest element
    s = qsort_lomuto(a)
    if s == k-1:
        return a[s]
    elif s > l+k-1:
        qselect(a,k)
    else:
        qselect(a[s+1:r], k-1-s)

def qsort_lomuto(a):
    l = 0
    r = len(a)-1
    p = a[l]
    s = l
    for i in range(l+1, r):
        if a[i] < p:
            s+= 1
            tmp = a[s]
            a[s] = a[i]
            a[i] = tmp
    tmp2 = a[l]
    a[l] = a[s]
    a[s] = tmp2
    print(a)
    return s

def BruteForceClosestPair(P):
    # //Finds distance between two closest points in the plane by brute force
    # //Input:AlistP ofn(n≥2)pointsp1(x1,y1),...,pn(xn,yn) //Output: The distance between the closest pair of points d←∞
    # for i ← 1 to n − 1 do
    # for j ← i + 1 to n do
    # d ← min(d, sqrt((xi − xj )2 + (yi − yj )2)) //sqrt is square root
    # return d
    # TODO: 
    for i in range(len(P)):
        for j in range(i+1, len(P))+1:
            # d = min(d, sqrt(x[i] - x[j])**2 + (y[i] - y[j])**2)
            pass

def hw4(n):
    if n==1:
        print("All")
    else:
        print("Going")
        hw4(n/2)
        hw4(n/2)



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



def bubbleSort(A):
    # ALGORITHM BubbleSort(A[0..n − 1]) //Sorts a given array by bubble sort
    # //Input: An array A[0..n − 1] of orderable elements //Output: Array A[0..n − 1] sorted in nondecreasing order for i ← 0 to n − 2 do
    # for j ← 0 to n − 2 − i do
    # ifA[j +1]<A[j] swapA[j]andA[j +1]
    
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if( A[j+1] < A[j]):
                #swap Aj Aj+1
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp
    return A



def selectionSort(A):
    # SelectionSort(A[0..n − 1]) 
    # //Sorts a given array by selection sort
    # //Input: An array A[0..n − 1] of orderable elements 
    # //Output: Array A[0..n − 1] sorted in nondecreasing order for i ← 0 to n − 2 do
    # min ← i
    # for j ← i + 1 to n − 1 do
    # ifA[j]<A[min] min←j swap A[i] and A[min]
    # TODO:seems to have too many swaps
    arrlen = len(A)
    print(A)
    for i in range(0, arrlen-2):
        min_idx = i
        for j in range(i+1,arrlen-2):
            if(A[j] < A[min_idx]):
                min_idx = j
                # print("min:",A[min_idx], "idx: ",min_idx)
                # print(i,min_idx)
                # print(A)
                # print("---")
                tmp = A[i]
                A[i] = A[min_idx]
                A[min_idx] = tmp
                # print(A[i], A[min_idx])
    print("-------")
    print(A)

def mult(m,n):
    # wtite a integer multiplication using recursion
    # m               if n=1
    # m + mult(m,n-1) if n>1

    if n==1:
        return m
    elif n>1:
        print(m,n)
        return m+mult(m,n-1)


def powerSet(str1, index, curr): 
    n = len(str1) 
  
    # base case 
    if (index == n): 
        return
    # First print current subset 
    # print(curr) 
    print(n)
  
    # Try appending remaining characters 
    # to current subset 
    for i in range(index + 1, n): 
        curr += str1[i] 
        powerSet(str1, i, curr) 
        # Once all subsets beginning with 
        # initial "curr" are printed, remove 
        # last character to consider a different 
        # prefix of subsets. 
        curr = curr.replace(curr[len(curr) - 1], "") 
  
    return


def main():
    arr = [ round(random.uniform(0, 10)) for i in range(10)]
    print(arr)
    arr = "abc"
    # print(qselect([5,2,1,3],2))
    # print(qsort_lomuto([5,2,1,3]))
    # powerSet(arr,0,"a")
    # print(mult(4,3))
    # print(BruteForceStringMatch("fdksljfsklasdnvdnkjfh","asd"))
    # arr = [5,2,3,1,4]
    # selectionSort(arr)
    # bubbleSort(arr)
    # print(SequentialSearch(arr, 2))
    # print(SequentialSearch2(arr,2))

    hw4(8)
    print("fin")

main()