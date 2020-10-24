'''
Medium

Share
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
'''

class Solution:
    def minSetSize(self, array):
        arrayOfUniqueNumbers = self.countAllUniqueNumbers(array)
        arrayOfUniqueNumbers = list(reversed(sorted(arrayOfUniqueNumbers)))
        return self.getLenghtOfMinSet(arrayOfUniqueNumbers, array)
    
    def countAllUniqueNumbers(self, array):
        table = {}
        idx = 0
        for num in array:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        arrayOfNumbers = table.values()
        return arrayOfNumbers
    
    def getLenghtOfMinSet(self, array, initial_array):
        half = len(initial_array)/2
        lengthOfMinSet = 0
        sumOfSet = 0
        idx = 0
        while sumOfSet < half:
            sumOfSet += array[idx]
            idx += 1
            lengthOfMinSet += 1
        return lengthOfMinSet
