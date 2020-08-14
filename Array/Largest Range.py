'''
To define boundaries of the longest sequence in the given array.
Numbers can be not in proper order or not adjacent.
Example:
Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7] => where sequence is {0, 1, 2, ... 7}
'''

# A way to solve it: use #-table to memo nums 
# and do searching as linkedlist technic.

def largestRange(array):
    table = {}  # table for element's memorization

    # step 1: ranges build
    for i in range(len(array)):
        value = array[i]
        # left side
        if (value - 1) in table:
            if table[value - 1] is True:
                table[value] = value - 1
            else:
                table[value] = table[value - 1]
        else:
            table[value] = True

        # right side
        if (value + 1) in table:
            if table[value] is True:
                table[value + 1] = value
            else:
                table[value + 1] = table[value]

    # step 2: max range
    indexes = []  # anser
    max_range = float("-inf")
    for end in table: # we start tracking from the end point to the start
        key = end
        while True:
            if table[key] is True:
                start = key
                break
            key = table[key]

        local_max = end - start
        if local_max > max_range:
            max_range = local_max
            indexes = [start, end]

    return indexes
