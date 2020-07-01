'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result. 
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        res = []
        N = len(B)
        M = len(A)
        n = 0
        m = 0
    
        while n < N or m < M:
    
            if A[m] >= B[n]:
                res.append(B[n])
                n += 1
            else:
                res.append(A[m])
                m += 1
    
            if n == N:
                for i in range(m, M):
                    res.append(A[i])
                A = res.copy()
                m = M

            if m == M:
                for i in range(n, N):
                    res.append(B[i])
                A = res.copy()
                n = N
                
        return A
