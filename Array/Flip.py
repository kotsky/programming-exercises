'''
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001
'''

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        global_sum = 0
        suma = 0
        st = 0
        end = 0
        
        
        for i in range(len(A)):
            
            if A[i] == "0":
                temp = -1
            else:
                temp = 1
                
            suma = suma + temp
            if suma < global_sum:
                global_sum = suma
                gl_st = st
                end = i
            elif suma >= 1:
                suma = 0
                st = i+1
                
        if global_sum == 0:
            answer = ""
        else:
            answer = [gl_st+1, end+1]

        return answer
                
                
                
