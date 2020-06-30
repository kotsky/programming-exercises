'''
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A = 
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
    
'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        N = len(A)
    
        try:
            M = len(A[0])
            if M == 0:
                return "0"
        except:
            l = 0
            r = N - 1
    
            while r - l >= 0:
                index = int((r + l) / 2)
                temp = A[index]
                if B > temp:
                    l = index + 1
                elif B < temp:
                    r = index - 1
                else:
                    return "1"
            return "0"

        if B < A[0][0] or B > A[N - 1][M - 1]:
            return "0"
    
        while len(A) > 1:
    
            index = int(len(A) / 2)
            try:
                temp = A[index][M - 1]
            except:
                break
            temp_start = A[index][0]
    
            if B > A[-1][-1]:
                return "0"
    
            if B > temp:
                A = A[index + 1:]
            elif B < temp:
                if B > temp_start:
                    A = A[index]
                    A = [A]
                elif B == temp_start:
                    return "1"
                else:
                    A = A[:index]
            else:
                return "1"
    
        l = 0
        r = M - 1
    
        while r - l >= 0:
            index = int((r + l) / 2)
            temp = A[0][index]
            if B > temp:
                l = index + 1
            elif B < temp:
                r = index - 1
            else:
                return "1"
        return "0"
                
