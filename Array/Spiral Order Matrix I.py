'''
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''


class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        n = len(A[0])
        count = 0
        m = len(A)
        res = []
        t = 0
        d = n
        b = m
        g = 0
        dir = 0
        if (len(A) >= 0 ):
            while (count < (n*m)):
                if dir == 0:
                    for i in range(t, d):
                        res.append(A[t][i])
                        count += 1
                    t += 1
                elif dir == 1:
                    for i in range(t, b):
                        res.append(A[i][d-1])
                        count += 1
                    d -= 1
                elif dir == 2:
                    for i in range(g, d):
                        res.append(A[b-1][d-1 - i])
                        count += 1
                    b -= 1
                elif dir == 3:
                    for i in range(t, b):
                        res.append(A[b-i][g])
                        count += 1
                    g += 1

                dir = (dir + 1) % 4
        else:
            res = A[0]
            
        return res
