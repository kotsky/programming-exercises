'''
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        
        h, w = A+1, B+1;
        viv = [[0 for x in range(w)] for y in range(h)] 
        
        if A == 1 or B == 1:
            return 1
        else:
            return way(A-1, B, viv) + way(A, B-1, viv)    
            
            
def way(A, B, viv):
    if viv[A][B] != 0:
        return viv[A][B]

    if A == 1 or B == 1:
        return 1
    else:
        return way(A-1, B, viv) + way(A, B-1, viv) 
