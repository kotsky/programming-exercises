'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):

        A = A.split('.')
        B = B.split('.')
        
        mini = min(len(A), len(B))
        
        for i in range(mini):
            
            if A[i] == '':
                temp_a = 0
            else:
                temp_a = int(A[i])
                
            if B[i] == '':
                temp_b = 0
            else:
                temp_b = int(B[i])
            
            if temp_a > temp_b:
                return "1"
            elif temp_a < temp_b:
                return "-1"
            else:
                if i == mini-1:
                    
                    if len(A) == len(B):
                        return "0"
                    else:
                        if len(A) > len(B):
                            
                            temp = A[i+1::]
                            temp = ''.join(temp)
                            
                            if int(temp) == 0:
                                return "0"
                            else:
                                return "1"
                        else:
                            temp = B[i+1::]
                            temp = ''.join(temp)
                            
                            if int(temp) == 0:
                                return "0"
                            else:
                                return "-1"

                
                
