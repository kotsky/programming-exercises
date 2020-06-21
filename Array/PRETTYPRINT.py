'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A  == 1:
            return "1"
        elif A < 1:
            return ""
        
        N = 2 * A - 1
        w, h = N, N
        res = [[A for x in range(w)] for y in range(h)]
    
        temp = res[0].copy()
    
        for i in range(1, int(N / 2)):
    
            for j in range(i, N - i):
                temp[j] = temp[j] - 1
    
            res[i] = temp.copy()
    
        temp = temp.copy()
    
        res2 = res[0:int(N/2)][:].copy()
        res2 = res2[::-1]
    
        temp[A - 1] = temp[A - 1] - 1
        res[int(N/2)] = temp
        res[int(N/2)+1::] = res2
        
        return res
                
        
        
