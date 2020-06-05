'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
1 <= A[i] <= 1e5
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]
    
Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
                n = len(A)

                global_max = -1
                new_global_max = global_max
            
                index_start = 0
                index_count = 0
            
                global_index_start = index_start
                global_index_count = index_count
            
                for i in range(n):
                    current_max = A[i]
                    if current_max < 0:
                        new_global_max = -1
                        index_start = i+1
                        index_count = 0
                    else:
                        new_global_max = max(current_max, new_global_max + current_max)
                        index_count += 1
            
                    if new_global_max > global_max:
                        global_max = new_global_max
                        global_index_start = index_start
                        global_index_count = index_count
                    elif current_max == 0:
                        global_index_count = max(global_index_count, index_count)
            
                if global_max <= -1:
                    return ""
                else:
                    A = A[global_index_start:]  # global_max, global_index_start, global_index_count
                    return A[0:global_index_count]
