'''
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):

        for i in range(len(A)):
            
            if A[i] == B[0]:

                k = 0
                while (k+i) < len(A):
                    
                    if B[k] != A[i+k]:
                        break
                    elif B[k] == A[i+k] and k >= (len(B)-1):
                        if len(A) == len(B):
                            return 0
                        else:
                            return i
                    
                    k += 1                    
            
        return "-1"
                    
                    
                
