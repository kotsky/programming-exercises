'''
Insert given number and to have constant time complexity returning of the array median.
In {1, 3, 7} mediana is 3, in {1, 2, 7, 10} => (7+2)/2 = 3.5
To do with minHeap + maxHeap as 2 sides of the array from the middle.

The idea: by using heaps, we split array onto 2 parts, where we track its min and max values.
Then, by knowing length of the array, we can calculate its median by using min-max values
of our heaps.
We do rebalancing all time to keep max-heap and min-heap be one size +-1.

Example:
    def addNumber(value, test):
        test.insert(value)
        # "Median = ", test.median, "and sets are ",
        # , ' & ', test.max_heap.printHeap()
        print(test.median)

    test = ContinuousMedianHandler()
    addNumber(1, test)
    addNumber(10, test)
    addNumber(100, test)
    addNumber(6, test)
    addNumber(7, test)
    addNumber(8, test)
    addNumber(8, test)

'''
Output:
1
5.5
10
8.0
7
7.5
8
'''

'''

import heap from py-libs/tree

# Create: O(N) Space to save each element
# Insert: O(lon(N)) T  / O(1) S
# Mediana: O(1) TS

class ContinuousMedianHandler:
    def __init__(self):
        self.max_heap = MaxHeap([])
        self.min_heap = MinHeap([])
        self.median = None

    def insert(self, number):
        if not self.min_heap.length() or number < self.min_heap.peek():
            self.max_heap.insert(number)
        else:
            self.min_heap.insert(number)
        self.rebalance()
        self.updateMedian()

    def getMedian(self):
        return self.median

    def updateMedian(self):
        if self.min_heap.length() > self.max_heap.length():
            self.median = self.min_heap.peek()
        elif self.min_heap.length() < self.max_heap.length():
            self.median = self.max_heap.peek()
        else:
            self.median = (self.max_heap.peek() + self.min_heap.peek()) / 2

    def rebalance(self):
        while abs(self.min_heap.length() - self.max_heap.length()) > 1:
            if self.min_heap.length() > self.max_heap.length():
                head = self.min_heap.pop()
                self.max_heap.insert(head)
            else:
                head = self.max_heap.pop()
                self.min_heap.insert(head)
