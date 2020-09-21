'''
Merge in sorted order into one array these sorted subarrays.
'''
arrays = [
    [-19, 33, 34],
    [-94, -53, -10, -3, 44, 73],
    [27, 42, 70, 86],
    [-28, 91],
    [-53, -27, 31, 77, 96, 99]
  ]
  
  # Use min heap as a buffer exchange and comparison
  # of smallest numbers from each subarray.

def mergeSortedArrays(arrays):
    if len(arrays) < 2:
        return arrays
    search_heap = createMinHeapFromFirstElement(arrays)
    merged_sorted_array = mergeAndSort(arrays, search_heap)
    return merged_sorted_array


def createMinHeapFromFirstElement(arrays):
    min_heap = MinHeap()
    for i in range(len(arrays)):
        min_heap.addNode(Node(arrays[i][0], i, 0, len(arrays[i])))
    for k in range(len(min_heap.heap)):
        min_heap.siftUp(k)
    min_heap.head = min_heap.heap[0]
    return min_heap


def mergeAndSort(arrays, min_heap):
    merged_array = []
    while min_heap.head is not None:
        head = min_heap.head
        merged_array.append(head.value)
        head.idx += 1
        if head.idx < head.limit:
            head.value = arrays[head.sub_array_idx][head.idx]
            min_heap.siftDown(0)
            min_heap.head = min_heap.heap[0]
        else:
            min_heap.removeHead()
    return merged_array


class MinHeap:
    def __init__(self):
        self.heap = []
        self.head = None

    def addNode(self, node):
        self.heap.append(node)

    def siftDown(self, start_index):
        heap = self.heap
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(heap):
            if child_two_index < len(heap):
                if heap[child_one_index].value <= heap[child_two_index].value and \
                        heap[start_index].value > heap[child_one_index].value:
                    new_index = child_one_index
                elif heap[child_one_index].value > heap[child_two_index].value and \
                        heap[start_index].value > heap[child_two_index].value:
                    new_index = child_two_index
                else:
                    break
            else:
                if heap[start_index].value > heap[child_one_index].value:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index, heap)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def removeHead(self):
        if self.head is not None:
            if len(self.heap) > 1:
                self.swap(0, len(self.heap) - 1, self.heap)
                self.heap.pop()
                self.siftDown(0)
                self.head = self.heap[0]
            else:
                self.head = None
                self.heap.pop()

    def siftUp(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx].value < self.heap[parent_idx].value:
                self.swap(idx, parent_idx, self.heap)
                idx = parent_idx
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


class Node:
    def __init__(self, value, sub_array_idx, idx, limit):
        self.value = value
        self.sub_array_idx = sub_array_idx
        self.idx = idx
        self.limit = limit


print(mergeSortedArrays(arrays))
