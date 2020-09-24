'''
print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
output =  [-24, 2, 3, 5, 6, 35] # find the longest chain of increasing numbers in the given order
'''

# Version 2. Binary Search tech
# O(N * log(N)) Time / O(N) Space

# The idea behind is to create 2 arrays:
# 1) indices - to store at each index i the idx of the last smallest number in the increasing subsequence of length i
# 2) sequences - to track the idx of the last element in chain, which was right before current one at idx i
# and then, apply binary search to find out where we can kind of insert our new index i into indices -> update subsequence
# at each length i by minimum possible from array[i]

def longestIncreasingSubsequence(array):
    if len(array) < 2:
        return array

    indices = [None for i in range(2)]
    sequences = [None for i in array]
    indices[1] = 0
    for i in range(1, len(array)):
        exploreNumber(i, array, indices, sequences)
    return buildSequence(array, indices, sequences)


def buildSequence(array, indices, sequences):
    sequence = [array[indices[-1]]]
    i = sequences[indices[-1]]
    while i is not None:
        sequence.append(array[i])
        i = sequences[i]
    return list(reversed(sequence))


def exploreNumber(i, array, indices, sequences):
    if array[i] > array[indices[-1]]:
        sequences[i] = indices[-1]
        indices.append(i)
    else:
        binarySearchAndIndicesUpdate(i, array, indices, sequences)


def binarySearchAndIndicesUpdate(i, array, indices, sequences):
    start_idx = 1
    end_idx = len(indices)
    mid_idx = (start_idx + end_idx) // 2
    while start_idx <= end_idx:
        if array[i] < array[indices[mid_idx]]:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1
        mid_idx = (start_idx + end_idx) // 2
    indices[start_idx] = i
    sequences[i] = indices[start_idx-1]


'''
# Version 1
# O(N) -> O(N^2) Time depends on the given input array / O(N) Space
# Dymnamic style + recursion on each num -> dive deeper to explore possible chains.
# Track its depth (length of chain) + next number

def longestIncreasingSubsequence(array):
    sub_sequences = [{"length": None, "next_idx": None} for a in array]
    sequence_start_idx = -1
    max_length = -1

    for i in range(len(array)):
        if sub_sequences[i]["length"] is None:
            sub_sequences[i]["length"] = exploreSequenceFromIdx(array, sub_sequences, i)
        if sub_sequences[i]["length"] is not None and sub_sequences[i]["length"] > max_length:
            max_length = sub_sequences[i]["length"]
            sequence_start_idx = i
    return buildLongestSequence(array, sub_sequences, sequence_start_idx)

# Version 1. From left to right
def exploreSequenceFromIdx(array, sub_sequences, i):
    if sub_sequences[i]["length"] is not None:
        return sub_sequences[i]["length"]
    sub_sequences[i]["length"] = 0
    for j in range(i + 1, len(array)):
        if array[i] >= array[j]:
            continue
        possible_longest_length = exploreSequenceFromIdx(array, sub_sequences, j) + 1
        if possible_longest_length > sub_sequences[i]["length"]:
            sub_sequences[i]["length"] = possible_longest_length
            sub_sequences[i]["next_idx"] = j
    return sub_sequences[i]["length"]
    
# Version 2. From the end
'''
def exploreSequenceFromIdx(array, sub_sequences, i):
    if sub_sequences[i]["length"] is not None:
        return sub_sequences[i]["length"]
    sub_sequences[i]["length"] = 0
    for j in range(i + 1, len(array)):
        possible_longest_length = exploreSequenceFromIdx(array, sub_sequences, j) + 1
        if array[i] >= array[j]:
            continue
        if possible_longest_length > sub_sequences[i]["length"]:
            sub_sequences[i]["length"] = possible_longest_length
            sub_sequences[i]["next_idx"] = j
    return sub_sequences[i]["length"]
'''


def buildLongestSequence(array, sub_sequences, sequence_start_idx):
    sequence = [array[sequence_start_idx]]
    next_node_idx = sub_sequences[sequence_start_idx]["next_idx"]
    while next_node_idx is not None:
        node = array[next_node_idx]
        next_node_idx = sub_sequences[next_node_idx]["next_idx"]
        sequence.append(node)
    return sequence
'''
