'''
Given an array of integers arr, 
a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. 
If there are multiple lucky integers return the largest of them. 
If there is no lucky integer return -1.
'''

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        memo = self.calculateFrequenciesOfEachNumber(arr)   # O(N) Time / Space
        return self.getLuckyNumber(memo)    # O(N) Time / O(1) Space
        
    def calculateFrequenciesOfEachNumber(self, arr):
        memo = {}
        for num in arr:
            if num not in memo:
                memo[num] = 0
            memo[num] += 1
        return memo
            
    def getLuckyNumber(self, memo):
        lucky_number = None
        for num in list(memo.keys()):
            if num == memo[num]:
                if lucky_number is None:
                    lucky_number = num
                else:
                    lucky_number = max(lucky_number, num)
        return lucky_number if lucky_number is not None else -1
