'''
Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return index of B in array A, otherwise return -1
Constraints

1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.
For Example

Input 1:
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
Output 1:
    0
Explanation 1:
 Target 4 is found at index 0 in A.


Input 2:
    A = [5, 17, 100, 3]
    B = 6
Output 2:
    -1
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        l = 0
        r = len(A)-1
        mini = A[0]
        
        if A[0] >= A[-1]:
            while (r-l) >= 0:
                index = int((r+l)/2)
                temp = A[index]
                
                if temp > mini:
                    l = index+1
                elif temp < mini:
                    r = index-1
                    mini = min(mini, temp)
            
            if B >= A[0]:
                l = 0
                r = index
            elif B <= A[-1]:
                l = index+1
                r = len(A)-1
            else:
                return "-1"
            
        while (r-l) >= 0:
            index = int((r+l)/2)
            temp = A[index]
            
            if B == temp:
                return index
            elif B > temp:
                l = index+1
            elif B < temp:
                r = index-1 
            
        return "-1"
        
            
