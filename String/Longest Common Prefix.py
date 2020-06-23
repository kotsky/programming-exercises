'''
Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Input Format

The only argument given is an array of strings A.
Output Format

Return longest common prefix of all strings in A.
For Example

Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
'''

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 1:
            return A[0]
            
        n = len(A)
        k = 0
        
        exit = False

        while True:
            
            prefix = A[0][k]
            
            for i in range(0, n):
                
                if A[i][k] != prefix:
                    if k == 0:
                        return ""

                    return A[0][0:k]
                    
                lenght = len(A[i])
                
                if (lenght - 1) == k:
                    exit = True
            
            if exit == True:
                return A[0][0:k+1]
            
            k += 1
            
            
