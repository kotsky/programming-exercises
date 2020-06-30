'''
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
'''

import math as m

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        if A == 0:
            return "0"
        elif A < 4:
            return "1"
        
        l = 1
        r = A
        while r - l >= 1:
            
            temp = (r + l) / 2

            if (temp - m.floor(temp) != 0):
                temp = m.floor(temp) + 1

            temp_2 = (pow(temp, 2))
            
            if temp_2 == A:
                return m.floor(temp)
            elif temp_2 < A:
                l = temp
            else:
                r = temp - 1
 
        return m.floor(l)
            
