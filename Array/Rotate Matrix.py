'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''



class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        
        for i in xrange(1, n):
            for j in xrange(i, n):
                temp = A[i-1][j]
                A[i-1][j] = A[j][i-1]
                A[j][i-1] = temp
                
        for i in xrange(int(n/2)):
            for j in xrange(n):
                temp = A[j][i]
                A[j][i] = A[j][-1-i]
                A[j][-1-i] = temp
                
        return A
