from itertools import permutations 
import itertools 
  
def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 

def powerset(s):
    x = len(s)
    for i in range(1 << x):
        for j in range(x):
            if i & (1<< j):
                print(s[j])
        # print([s[j] for j in range(x) if (i & (1<< j))])

def lexicographical_permutation(str): 
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        print(x, end=" ") 

def binary_search(A, K):
    #     whilel≤r do
    # m ← ⌊(l + r)/2⌋
    # if K = A[m] return m elseifK<A[m] r←m−1 else l ← m + 1
    # return −1
    l = 0
    print(A)
    r = len(A) -  1
    while l<=r:
        m = int((l+r)/2)
        if K == A[m]:
            return m
        elif K<A[m]:
            # r = m -1 #-1
            r = m
        else:
            # l = m + 1#+1
            l = m
    return -1

def binary_exps(n):
    L = list(bin(n)[2:])
    L.reverse()
    L = [i for i,c in enumerate(L) if c == '1']
    return L
    
def multiply(x,y):
    if y > x:  x,y = y,x
    result = 0
    L = binary_exps(y)
    for e in L:
        result += x << e
    return result, L

def main():   
    # print(binary_search([1,2,4,5,9,6,3,12], 3))
    # # str ='431265'
    # # lexicographical_permutation(str)
    # # # Driver Code 
    # s = {1, 2, 3} 
    # n = 2

    print(multiply(1101, 10010))

    # print(powerset([4,5,6]))
    # print(findsubsets(s, n))  

main()