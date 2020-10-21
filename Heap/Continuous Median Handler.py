'''
Insert given number and to have constant time complexity returning of the array median.
In {1, 3, 7} mediana is 3, in {1, 2, 7, 10} => (7+2)/2 = 3.5
To do with minHeap + maxHeap as 2 sides of the array from the middle.
'''
'''
#Test

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


# Insert: O(lon(N)) T  / O(N) S to save each element
# Mediana: O(1) TS

class ContinuousMedianHandler:
    def __init__(self):
        self.max_heap = maxHeap()
        self.min_heap = minHeap()
        self.stack = []
        self.median = None

    def insert(self, number):
        if self.min_heap.length() < 1:
            self.stack.append(number)
            if len(self.stack) == 1:
                self.median = number
            else:
                self.min_heap.insert(max(self.stack))
                self.max_heap.insert(min(self.stack))
                self.median = (self.max_heap.head() + self.min_heap.head()) / 2
        else:
            if number <= self.min_heap.head():
                self.max_heap.insert(number)
            else:
                self.min_heap.insert(number)

            self.balance()

            if self.min_heap.length() > self.max_heap.length():
                self.median = self.min_heap.head()
            elif self.min_heap.length() < self.max_heap.length():
                self.median = self.max_heap.head()
            else:
                self.median = (self.max_heap.head() + self.min_heap.head()) / 2

    def getMedian(self):
        return self.median

    def balance(self):
        while abs(self.min_heap.length() - self.max_heap.length()) > 1:
            if self.min_heap.length() > self.max_heap.length():
                head = self.min_heap.popHead()
                self.max_heap.insert(head)
            else:
                head = self.max_heap.popHead()
                self.min_heap.insert(head)


class minHeap:
    def __init__(self):
        self.heap = []

    def head(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap)-1)

    def shiftDown(self, start_index):
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] <= self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] > self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] > self.heap[child_one_index]:
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
            if self.heap[idx] < self.heap[idx_parent]:
                self.swap(idx, idx_parent)
                idx = idx_parent
                idx_parent = (idx - 1) // 2
            else:
                break

    def pop(self):
        return self.heap.pop()

    def popHead(self):
        self.swap(0, -1)
        head = self.pop()
        self.shiftDown(0)
        return head

    def length(self):
        return len(self.heap)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def printHeap(self):
        for num in self.heap:
            print(num, end=' ')
        # print('', end='\n')


class maxHeap:
    def __init__(self):
        self.heap = []

    def head(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap)-1)

    def shiftDown(self, idx):
        while self.heap[idx] < max(self.heap[2 * idx + 1], self.heap[2 * idx + 2]):
            if self.heap[2 * idx + 1] < self.heap[2 * idx + 2]:
                idx_child = 2 * idx + 2
            else:
                idx_child = 2 * idx + 1
            self.swap(idx, idx_child)
            idx = idx_child

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

    def pop(self):
        return self.heap.pop()

    def popHead(self):
        self.swap(0, -1)
        head = self.pop()
        self.shiftDown(0)
        return head

    def length(self):
        return len(self.heap)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def printHeap(self):
        for num in self.heap:
            if type(num) == int:
                print(num, end=' ')
        #print('', end='\n')
