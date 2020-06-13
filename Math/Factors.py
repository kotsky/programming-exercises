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
    
    # ----------------------- is N prime?
     def isPrime(self, A):
        res = []
        for i in range(1, int(m.sqrt(A) + 1)):
            if A % i == 0:
                res.append(i)
            if len(res) >= 2:
                return 0

        if A != 1:
            return 1
        else:
            return 0

        
    #--------------------------- list of prime numbers
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        size = A//2
        sieve = [1]*size
        limit = int(A**0.5)
        for i in range(1,limit):
            if sieve[i]:
                val = 2*i+1
                tmp = ((size-1) - i)//val 
                sieve[i+val::val] = [0]*tmp
        return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0] 
