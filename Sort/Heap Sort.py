'''
Sort with max heap method.
1. Divide by 2 parts: sorted and unsorted.
2. Convert the given array into max heap.
3. Swap head with the last one element of unsorted part. (Because head in max heap is the max value)
4. Increase sorted range (in the end of the array).
5. SiftDown new head.
6. Repeat 2-6 until sorted range reachs index 0.
'''

# O(N*log(N)) T

def heapSort(array):
    if len(array) < 2:
        return array
    array = buildHeap(array)
    start_idx = 0
    end_idx = len(array)-1
    while (end_idx - start_idx) > 0:  
        siftDown(array, start_idx, end_idx) # O(log(N)) T
        swap(array, start_idx, end_idx)
        end_idx -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# O(N) T
def buildHeap(array):
    for i in range(len(array) - 1, 0, -2):
        parent_idx = (i - 1) // 2
        siftDown(array, parent_idx, len(array) - 1)
    return array

# O(log(N)) T
def siftDown(array, parent_idx, end_idx):
    while parent_idx >= 0:
        child_one = 2 * parent_idx + 1
        child_two = 2 * parent_idx + 2
        if child_one > end_idx:
            break
        if child_two > end_idx:
            if array[parent_idx] < array[child_one]:
                swap(array, parent_idx, child_one)
            break
        if array[parent_idx] < max(array[child_one], array[child_two]):
            if array[child_one] >= array[child_two]:
                swap(array, parent_idx, child_one)
                parent_idx = child_one
            else:
                swap(array, parent_idx, child_two)
                parent_idx = child_two
        else:
            break



print(heapSort([8, 5, 2, 9, 5, 6, 3]))
