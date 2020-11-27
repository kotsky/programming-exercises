'''
Define a subarray (@start-@end) which has to be sorted 
to full-fill sorted array.

input = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] 
return = [3, 9]

The idea:
1. Move from the left to define first wrong order (element).
2. Return and again from the left define, 
where this wrong element must be placed. It's your @start.
3. Repeat 1-2 for @end, but from the right side.

'''


def subarraySort(array):
    flagMin = False
    flagMax = False
    for i in range(1, len(array)):
        if array[i - 1] > array[i] and flagMin is False:
            local_min = array[i]
            flagMin = True
        elif flagMin:
            local_min = min(local_min, array[i])
    if flagMin is False:
        return [-1, -1]
    i = 0
    while i < len(array):
        if local_min < array[i]:
            startIdx = i
            break
        i += 1

    for j in range(1, len(array)):
        if array[-j] < array[-1 - j] and flagMax is False:
            local_max = array[-j - 1]
            flagMax = True
        elif flagMax:
            local_max = max(local_max, array[-j - 1])

    j = len(array) - 1
    while j >= 0:
        if array[j] < local_max:
            endIdx = j
            break
        j -= 1

    return [startIdx, endIdx]
