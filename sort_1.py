'''
chap3 sorting algorithms
sep 10
'''
import numpy as np
import random

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
    for i in range(arrlen):
        min_idx = i
        for j in range(arrlen):
            if(A[j] < A[min_idx]):
                min_idx = j
                print("min:",A[min_idx], "idx: ",min_idx)
                print(i,min_idx)
                print(A)
                print("---")
                tmp = A[i]
                A[i] = A[min_idx]
                A[min_idx] = tmp
                # print(A[i], A[min_idx])
    print("-------")
    print(A)



def main():
    # arr = [ round(random.uniform(0, 100)) for i in range(10)]
    arr = [5,2,3,1,4]
    # selectionSort(arr)
    bubbleSort(arr)
    print("fin")

main()