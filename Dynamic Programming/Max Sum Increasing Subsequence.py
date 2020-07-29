'''
To find max sum and its elements of strictly increasing subarray.
Input: [10, 70, 20, 30, 50, 11, 30] => Output: [110, [10, 20, 30, 50]]
'''

# Create 1st additional array to remember max sum with the element on that index.
# Create 2nd array to remember index of last sequence, which is finished
# on the current index.
# From the example above:
# [10, 80, 30, 60, 110, 21, 60] 1st
# [0,  0,  0,  2,  3,   0,  2 ] 2nd

def maxSumIncreasingSubsequence(array):
    sums = []
    idx = []
    for i in range(len(array)):
        sums.append(array[i])
        idx.append(i)

    global_idx = []
    global_sum = float("-inf")

    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[i] > 0:
            if array[i] > array[j]:
                local_sum = array[i] + sums[j]
                if local_sum > sums[i]:
                    sums[i] = local_sum
                    idx[i] = j
                    if local_sum > global_sum:
                        global_sum = local_sum
                        global_idx = i
            j -= 1
            if array[i] > global_sum:
                global_sum = array[i]
                global_idx = i

    if global_sum >= 0:
        indexes = [array[global_idx]]
        while True:
            if global_idx == idx[global_idx]:
                break
            else:
                indexes.append(array[idx[global_idx]])
                global_idx = idx[global_idx]

        return [global_sum, indexes[::-1]]
    else:
        return [-1, [-1]]
