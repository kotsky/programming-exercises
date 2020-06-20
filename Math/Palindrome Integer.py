'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False

'''


import math

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A < 0:
            return "0"

        n = int(math.log10(A)+1)
 
        for i in range(int(n / 2)):
            temp_l = int(A / pow(10, n - 1 - 2 * i))
            temp_r = A % 10
    
            if temp_l != temp_r:
                return "0"
    
            A = int((A - temp_l*pow(10, n - 1 - 2 * i) - temp_r) / 10)
    
        return "1"
