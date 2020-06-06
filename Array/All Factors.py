'''
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.

Problem Approach:

Complete code in the hint.
'''


import math as m

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        res = []
        add = []
        for i in range(1, int(m.sqrt(A)+1)):
            if A%i == 0:
                res.append(i)
                if i != (A/i):
                    add.append(int(A/i))
                    
        for i in range(len(add)):
            res.append(add[-1-i])
            
        return res
