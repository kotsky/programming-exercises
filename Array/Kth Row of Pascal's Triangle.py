'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
'''

class Solution:
    
    def factorial(number):
        res = 1
        
        if number >= 2:
            for i in range(2,number+1):
                res *= i

        return res
    
    # @param A : integer
    # @return a list of integers
    def getRow(self, line):
        
        res = []
        for i in range(line+1):
            
            if i == 0 or i == line:
                res.append(1)
            else:
                temp = (factorial(line))/(factorial(i)*(factorial(line - i)))
                res.append(temp)
                
        return res
        
def factorial(number):
    res = 1
    
    if number >= 2:
        for i in range(2,number+1):
            res *= i

    return res
        
