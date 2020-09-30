
# Version 1. 
# O(b + s) TS
# Method "window" from left to right pointer.
# We track total number of unique symbols from smallString,
# and we track how many unique numbers and their quantity 
# we have in bigString between left and right pointers

def smallestSubstringContaining(bigString, smallString):
    table_smallString, unique_chr = hashingSmallString(smallString)
    # unique_chr shows have many unique letter are in smallString
    return getSmallestSubstringContaining(bigString, table_smallString, unique_chr)


def getSmallestSubstringContaining(string, table, unique_chr):
    left = 0  # pointer from the left
    current_unique_chr = 0  # current counting of unique smallString letters
                            # in frame left-right pointers
    smallestSubstringContainingIdx = [-1, -1]
    lengthSS = float("inf")

    while left < len(string) and string[left] not in table:
        left += 1
    right = left  # pointer from the right

    while left <= right < len(string):
        letter = string[right]
        if letter in table:
            current_unique_chr = updateUniqueCounter(current_unique_chr, letter, table, 1)
        else:
            right += 1
            continue

        while current_unique_chr >= unique_chr:
            letter = string[left]
            lengthSS, smallestSubstringContainingIdx = updateSmallestSubstringContaining(left, right, lengthSS, smallestSubstringContainingIdx)
            current_unique_chr = updateUniqueCounter(current_unique_chr, letter, table, -1)
            left += 1
            while left < len(string) and string[left] not in table:
                left += 1
            if left == len(string):
                break

        right += 1

    if smallestSubstringContainingIdx[0] == -1:
        return ""
    else:
        p1, p2 = smallestSubstringContainingIdx
        return string[p1:p2+1]


def updateUniqueCounter(current_unique_chr, letter, table, increment):
    table[letter]["current_count"] += increment
    letter_count, letter_current_count = table[letter]["count"], table[letter]["current_count"]
    if increment > 0:
        if letter_current_count == letter_count:
            current_unique_chr += 1
    else:
        if letter_current_count < letter_count:
            current_unique_chr -= 1
    return current_unique_chr


def updateSmallestSubstringContaining(left, right, length, idx):
    if right - left < length:
        length = right - left
        idx = [left, right]
    return length, idx


def hashingSmallString(smallString):
    table = {}
    unique_chr = 0
    for idx, letter in enumerate(smallString):
        if letter not in table:
            table[letter] = {"count": 1, "current_count": 0}
            unique_chr += 1
        else:
            table[letter]["count"] += 1
    return table, unique_chr


bigString = "abcdef"
smallString = "d"

print(smallestSubstringContaining(bigString, smallString))


# Version 2. O(b^2 * s) T / O(b + s) S
# Check if we have all our letters from smallString 
# in bigString from 0 - len(bigString) in double for loop

'''
def smallestSubstringContaining(bigString, smallString):
    table_ss = hashingSmallString(smallString)
    assignIdxFromBigString(bigString, table_ss)
    min_substring_len = float("inf")
    substring_idx = [-1, -1]
    for start_idx in range(len(bigString)):
        for end_idx in range(len(smallString) - 1 + start_idx, len(bigString)):
            if checkSmallInBig(start_idx, end_idx, table_ss):
                if (end_idx - start_idx) < min_substring_len:
                    min_substring_len = end_idx - start_idx
                    substring_idx = [start_idx, end_idx]
    if substring_idx[0] == -1:
        return ""
    else:
        return bigString[substring_idx[0]:substring_idx[1]+1]


def checkSmallInBig(start_idx, end_idx, table_ss):
    for key in table_ss.keys():
        if not checkKeyInRange(start_idx, end_idx, table_ss, key):
            return False
    return True


def checkKeyInRange(start_idx, end_idx, table_ss, key):
    count = table_ss[key]["count"]
    idxs = table_ss[key]["idx"]
    for i in idxs:
        if start_idx <= i <= end_idx:
            count -= 1
        if count <= 0:
            return True
    return False


def hashingSmallString(smallString):
    table = {}
    for idx, letter in enumerate(smallString):
        if letter not in table:
            table[letter] = {"count": 1, "idx": []}
        else:
            table[letter]["count"] += 1
        # table[letter]["idx"].append(idx)
    return table


def assignIdxFromBigString(bigString, table):
    for idx, letter in enumerate(bigString):
        if letter in table:
            table[letter]["idx"].append(idx)
'''


