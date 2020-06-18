'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        A = sorted(A, reverse = True)
        if A[0] == 0:
            res = -1
        else:
            count = 0
            res = -1
            for i in range(1, len(A)):
                
                if A[i] == A[i-1]:
                    count = 0
                else:
                    count += 1
                    
                if i == A[i] and count != 0:
                    res = 1
                    break
        
        return res
