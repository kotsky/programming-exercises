'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
'''

'''
    def gcd(self, A, B):
        return self.gcd(B,A%B) if A and B else max(A,B)
'''

import math as m

def allFactors(A):
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


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == 0 or B == 0:
            return A+B
        elif A == B:
            return A
        elif A > B:
            maxi = A
            mini = B
        else:
            maxi = B
            mini = A
        
        mini_factors = allFactors(mini)    
        
        for i in range(len(mini_factors)):
            
            if maxi % mini_factors[-1-i] == 0:
                return mini_factors[-1-i]
            
                
            
                    
                    
                    
                    
                    
                    
                    
