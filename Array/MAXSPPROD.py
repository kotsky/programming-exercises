'''
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9

Ex: [ 6, 7, 9, 5, 5, 8 ] 
specialLeft = [0,0,0,2,2,2] (these are the indices)
specialRight= [1,2,0,5,5,0] (also the indices)
specialLeft * specialRight= [0,0,0,10,10,0]
specialLeft and specialRight are matrices of the indices and we need to multiply those and get the maximum result of the multiplication as the output.
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxSpecialProduct(self, A):
        prod = 0
        mod = 1000000007
        
        for i in range(len(A)):
            j = i
            k = i
    
            max_l_index = 0
            max_r_index = 0
    
            #if A[max_l_index] > A[i]:
            while j >= 0:
                if A[j] > A[i]:
                    max_l_index = j
                    break
                j -= 1
                    
            while k < len(A):
                if A[k] > A[i]:
                    max_r_index = k
                    break
                k += 1
                
            local = (max_l_index * max_r_index)%mod
            if (local > prod):
                prod = local
    
        return prod
            
    def maxSpecialProduct2(self, A):
        n = len(A)
        if n<3:
            return 0
        rightspval = [0]*n
        leftspval = [0]*n
        stack = []
        
        stack.append(0)
        for i in range(1,n):
            while stack and A[stack[-1]] < A[i]:
                rightspval[stack.pop()] = i
            stack.append(i)
        stack.clear()
        
        stack.append(n-1)
        for i in range(n-1,-1,-1):
            while stack and A[stack[-1]] < A[i]:
                leftspval[stack.pop()] = i
            stack.append(i)
        del(stack)
        
        maxi = -1
        for i in range(n):
            maxi = max(maxi, leftspval[i]*rightspval[i])
        return maxi%1000000007
        
            


