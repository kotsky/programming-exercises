"""

You have unsorted array, where each element is in the range
of k from its spot, if this array would be sorted.

Return sorted array with Time Complexity < O(N*log(N)).

The idea:
  We use MinHeap to identify array_helper of k length 
  to use its min value, and traverse through array and
  replacing native elements with elements from MinHeap.

Example:
  input = [3, 2, 1, 5, 4, 7, 6, 5]
  k = 3
  expected = [1, 2, 3, 4, 5, 5, 6, 7]
  actual = sortKSortedArray(input, k)
  print(actual)


"""

# O(N*log(k)) Time / O(k) Space

def sortKSortedArray(array, k):
	if not array or len(array) <= 1: 
		return array
	if k > len(array)-1:
		k = len(array)-1
	
    min_heap = MinHeap(array[:k+1].copy())

	for current_idx in range(len(array)):
		array[current_idx] = min_heap.pop()
		if current_idx+k+1 < len(array):
			min_heap.insert(array[current_idx+k+1])
	
    return array


class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap(self.heap)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index)
            child_index -= 2
            parent_index = (child_index - 1) // 2

    def head(self):
        return self.heap[0]

    def is_empty(self):
        return self.length() == 0

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, -1)
            value = self.heap.pop()
            self.siftDown(idx)
        return value

    def length(self):
        return len(self.heap)

    def siftDown(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
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

    def siftUp(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        parent_index = (start_index - 1) // 2
        while parent_index >= 0:
            if self.heap[parent_index] > self.heap[start_index]:
                self.swap(start_index, parent_index)
                start_index = parent_index
                parent_index = (start_index - 1) // 2
            else:
                break

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def printHeap(self):
        for num in self.heap:
            print(num, end=' ')
        print('', end='\n')
