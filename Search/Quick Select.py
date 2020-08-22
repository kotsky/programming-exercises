'''
Find Kth smallest value in the given array:
Input: [8, 5, 2, 9, 7, 6, 3], k=3
Output: 5
'''

# Apply quick sort technic
# O(n) avg Time / O(1) Space
# O(n^2) worse Time

def quickselect(array, k):
    if k > len(array):
        return
        # quicksort method
    start_point = 0
    end_point = len(array) - 1

    while True:
        right = end_point
        pivot = start_point
        left = pivot + 1
        while right >= left:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(array, left, right)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1

        if right == k - 1:
            return array[pivot]
        swap(array, pivot, right)
        if right < k - 1:
            start_point = right + 1
        else:
            end_point = right - 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
