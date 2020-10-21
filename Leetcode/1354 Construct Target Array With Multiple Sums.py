'''
Hard

Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
'''


class MaxHeap:
    def __init__(self, array):
        self.heap = array
        self.build()
        self.head = self.heap[0]

    def build(self):
        for idx in range(len(self.heap)):
            self.shiftUp(idx)


    def shiftDown(self, start_index):
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] >= self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] < self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def shiftUp(self, idx):
        idx_parent = (idx - 1) // 2
        while idx_parent >= 0:
            if self.heap[idx] > self.heap[idx_parent]:
                self.swap(idx, idx_parent)
                idx = idx_parent
                idx_parent = (idx - 1) // 2
            else:
                break

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def grabHead(self):
        self.head = self.heap[0]
        return self.head

    def setHead(self, value):
        self.heap[0] = value
        self.shiftDown(0)

class Solution:
    def isPossible(self, target):
        target_size = len(target)
        if not target_size:
            return False
        # case 1: if the length is 1, then the only element should be 1 itself. Otherwise it's invalid.
        if target_size == 1:
            return True if target[0] == 1 else False

        target_sum = sum(target)  # O(N) Time
        
        # We will use Max-heap to have the maximum element at the top so that we can subtract the sum of rest of the elements from it.
        target_max_heap = MaxHeap(target)  # O(N*log(N)) Time / O(N) Space
        if target_max_heap.grabHead() == 1:
            return True
        
        # cnt will be used to check if all elements in target[] are 1. If yes then we have a valid target[] array.
        count_of_ones = 0
        for num in target:
            if num == 1:
                count_of_ones += 1
                
        # at any point of time we want the sum to be exclusive of the highest element that can be possibly made by the given instructions.
        target_sum -= target_max_heap.grabHead()
        
        '''
        The idea here is as follows:
			  Extract the max element x and subtract from it the sum of all the smaller elements & let's call this difference diff. 
			  Obviously, for x to exist in the target array, whatever the rest of the element is there we need to add the diff to those elements.
			  This diff is valid only if diff>=1 , otherwise no point continuing.
			  If diff is valid, it's a valid member of our array which is to form the target[] eventually, so we add it to the max-heap.
			  Now since we need to consider a new x, our sum has to be updated accordingly so as to exclude this max element.
			  Like before, if the new sum is >= x then we can't continue since the minimum difference between the two should be at least 1.
        '''

        while count_of_ones != target_size:
            top_number = target_max_heap.grabHead()
            
            # instead of doing repeated subtraction, we can optimize it by doing modulo.
			      # But we must take of the remainder becoming 0. 
            # 0 remainder means either the sum value is 1 or the sum value equals to the highest element at some point of time during the repeated subtraction.
            
            diff = top_number % target_sum
            
            if diff==0:
            # if the sum value has been 1 it means the x can be formed by repeated addition of 1 in which case the min difference between x and sum will be 1.
                if target_sum==1:
                    diff=1
                else: 
                    return False
            
            target_max_heap.setHead(diff)
            target_sum = target_sum - target_max_heap.grabHead() + diff

            if target_max_heap.grabHead() == 1:
                break
            # if the highest element is already smaller than the sum of rest of the element then it is not a valid target[] array.
            if target_sum > target_max_heap.grabHead():
                return False

        return True 
        
        
'''
The % prevents the TLE from the case (e.g., target=[10000000, 1]) where the largest element is significantly bigger than the sum of other elements.

For example, target = [max, a1, a2]. Here is the standard backtracking:

Subtract the largest with the rest of the array, we have the previous array target = [max-(a1+a2), a1, a2].
But the value of max is so large, that max-(a1+a2) is still the largest number in the array.
So we continue to subtract the largest, and we have a new previous array target = [max-2*(a1+a2), a1, a2].
But the value of max is so large, that max-2*(a1+a2) is still the largest number in the array.
Repeat 1-4...

After n iterations, we have a new array target = [max-n*(a1+a2), a1, a2], where max-n*(a1+a2) is not the largest any more.

Can we accelerate the process?
Yes.
We have max-n*(a1+a2) = max % (a1+a2). That is how the % works.

For example, target = [10, 3].
Without %, we have [10, 3] -> [7, 3] -> [4, 3] -> [1, 3].
With %, we have [10, 3] -> [10 % 3, 3] = [1, 3] quickly.

Note that the case max % (a1+a2) == 0 is a special one. For example, target = [10000000, 1]. 
If we perform max % (a1+a2), we will have target = [0, 1]. 
We use the if-else structure to deal with the special case, as shown in the other top-voted answers.
'''
