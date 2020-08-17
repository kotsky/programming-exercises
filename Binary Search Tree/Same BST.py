'''
You are given 2 arrays. If to use insert method of building binary search tree from these arrays, will be your trees similar?
Don't use tree data structure.
Input:
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
Output: True
'''

# If heads are not equal = False, if lengths are not equal - False.
# Do recursively check for each subtree.

def sameBsts(arrayOne, arrayTwo):
    if arrayOne[0] != arrayTwo[0] or len(arrayOne) != len(arrayTwo):
        return False

    idx = 0
    parent_node = arrayOne[idx]

    return checkSubtree(float("-inf"), parent_node, arrayOne, arrayTwo, idx+1, idx+1) and \
           checkSubtree(parent_node, float("inf"), arrayOne, arrayTwo, idx+1, idx+1)


def checkSubtree(lower, upper, arrayOne, arrayTwo, idxOne, idxTwo):
    headOne = None
    headTwo = None

    while idxOne < len(arrayOne):
        if arrayOne[idxOne] < upper and arrayOne[idxOne] >= lower:
            headOne = arrayOne[idxOne]
            break
        idxOne += 1

    while idxTwo < len(arrayTwo):
        if arrayTwo[idxTwo] < upper and arrayTwo[idxTwo] >= lower:
            headTwo = arrayTwo[idxTwo]
            break
        idxTwo += 1

    if headOne != headTwo:
        return False

    if headOne is None:
        return True

    return checkSubtree(lower, headOne, arrayOne, arrayTwo, idxOne+1, idxTwo+1) and \
           checkSubtree(headOne, upper, arrayOne, arrayTwo, idxOne+1, idxTwo+1)
