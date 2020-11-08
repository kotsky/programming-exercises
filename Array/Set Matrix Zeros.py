'''
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.

    >>> matrix = [[1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1]]
    >>> print(setZeroes(matrix))


Constraints:

    1 <= N, M <= 1000
    0 <= A[i][j] <= 1
    Examples:

    Input 1:
        [   [1, 0, 1],
            [1, 1, 1], 
            [1, 1, 1]   ]

    Output 1:
        [   [0, 0, 0],
            [1, 0, 1],
            [1, 0, 1]   ]

    Input 2:
        [   [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1]   ]

    Output 2:
        [   [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]   ]
'''
# O(R*C) Time / O(1) Space
# But 3 times R*C
# Using None as marker for zeros changes

def setZeroes_v2(matrix):

    def _setRowZeros(matrix, row):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                matrix[row][col] = None

    def _setColZeros(matrix, col):
        for row in range(len(matrix)):
            if matrix[row][col] != 0:
                matrix[row][col] = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                _setRowZeros(matrix, row)
                break
    print(matrix)

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                _setColZeros(matrix, col)
                break
    print(matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] is None:
                matrix[row][col] = 0

    return matrix

# O(R*C) Time / O(1) Space
# But 2 times R*C 
# Mark row and col on its zeros indies

def setZeroes(matrix):
    first_col_is_zero = False
    first_row_is_zero = False

    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            first_col_is_zero = True
            break

    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            first_row_is_zero = True
            break

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    if first_col_is_zero:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if first_row_is_zero:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    return matrix

''' Old version - my first code
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A[0])
        m = len(A)
        
        col = [1]*n
        row = [1]*m
        
        for i in range(m):
            for j in range(n):
                
                if A[i][j] == 0:
                    col[j] = 0
                    row[i] = 0
                
                A[i][j] = 0
                
        
        for i in range(m):
            if row[i] == 1:
                for j in range(n):
                    if col[j] == 1:
                        A[i][j] = 1
                        
        return A
        
'''
                    
                
