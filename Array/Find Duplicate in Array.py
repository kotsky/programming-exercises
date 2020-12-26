'''
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1

The idea:
    Once we find some number1, we multiply another number2 at index = (number1-1) by "-1",
    when we again find the same number1 and its index = {(number1-1)} < 0, then we know 
    that we already found number1 before => return number1

'''

# O(n) Time / O(1) Space

def firstDuplicateValue(array):
    
	for idx in range(len(array)):
		number = abs(array[idx])
		if array[number-1] < 0:
			return number
		array[number-1] *= -1
	return -1
		


# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def repeatedNumber(self, A):
#         if len(A) <= 1:
#             return "-1"
            
#         B = [0] * (len(A)-1)
        
#         for i in range(1, len(A)+1):
        
#             if B[A[i-1]-1] == -1:
#                 return A[i-1]
#             else:
#                 B[A[i-1]-1] = -1
                
#         return "-1"
