'''
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not len(nums):
            return 0
        
        count = 0
        suma = 0
        table = {0: 1}
        for i in range(len(nums)):
            suma += nums[i]
            if suma-k in table:
                count += table[suma-k]
            if suma in table:
                table[suma] += 1
            else:
                table[suma] = 1
        return count 
