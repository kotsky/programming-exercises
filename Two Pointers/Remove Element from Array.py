'''
Remove Element

Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3] 
Try to do it in less than linear additional space complexity.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        A[:] = [x for x in A if x!=B]
        return len(A)
    
    def removeElement_v2(self, A, B):
        n = len(A)

        if n==1 and A[0]==B: # handlign edge cases
            return 0
        tracker = 0
        i=0
        
        while i<n: #moving all B's to end using 2 pointer approach
            if A[i]!=B:
                A[i],A[tracker] = A[tracker],A[i]
                tracker+=1
            else:
                A[i],A[tracker] = A[tracker],A[i]
            i+=1

        A=A[:tracker] 
        return (tracker)
