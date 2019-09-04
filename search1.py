the input size is n since it takes an integer n as input.
T1(2n) / T1(n) ≈ (log22+log2n)/(log2n) ≈ 1

T2(2n) / T2(n) ≈ ((2n)2) / 2n  ≈ 2n

y = log2X;  2y = x;   log102y=log10X;  

ylog102 = log10X;   log2X * log102 = log10X; 

K = log102

1) because the second condition will not be checked if i = n

2) because to differentiate the case between finding out the answer and running out the indices which mean the answer didn't being found.

1) the probability of finding out the answer in each index is the same. 

2) the n(1-p) is the cases for unsuccessful search with n being the occurrence time and (1-p) being the probability. 

3) (n+1)/2, n

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

def main():
    A = [0,1,2]
    print(SequentialSearch(A, 3))
    print("fin")

main()