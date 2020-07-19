# To check if given array is monotonic
def isMonotonic(array):
    if len(array) <= 1:
        return True
    direction = 0
    for i in range(len(array) - 1):
        if direction == 0 and array[i] != array[i + 1]:
            if array[i + 1] >= array[i]:
                direction = 1
            else:
                direction = -1
        elif direction == 1:
            if array[i + 1] < array[i]:
                return False
        else:
            if array[i + 1] > array[i]:
                return False
    return True
