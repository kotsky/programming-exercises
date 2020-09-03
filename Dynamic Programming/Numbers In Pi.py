'''
Return the minimum amount of numbers (# of spaces between) from numbers[] to build PI. If there is no, "-1".

PI = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

Answer = 2  # 314159265 | 35897932384626433832 | 79

'''

# Recursion by checking each number in PI as its part.
# O(n * m * k) T / O(n) S, 
# where n = len(PI)
# m = len(numbers)
# k = len(longest number from numbers[])

# The version below is optimized with cache memorisation

def numbersInPi(pi, numbers):
    current_spaces = 0
    cache = {}
    spaces, current_spaces = checkByFirstNumber(pi, 0, current_spaces, numbers, float("inf"), cache)
    return -1 if spaces == float("inf") else spaces


def checkByFirstNumber(pi, start_idx, current_spaces, numbers, spaces, cache):
    if start_idx in cache:
        spaces = min(spaces, current_spaces + cache[start_idx] + 1)
        return spaces, current_spaces

    if start_idx == len(pi):
        spaces = min(spaces, current_spaces - 1)
        return spaces, current_spaces
    if start_idx > len(pi):
        return spaces, current_spaces

    for idx in range(len(numbers)):
        if pi[start_idx] == numbers[idx][0]:
            if start_idx + len(numbers[idx]) > len(pi):
                continue
            flag = False
            for j in range(1, len(numbers[idx])):
                if pi[start_idx + j] != numbers[idx][j]:
                    flag = True
                    break
            if flag:
                continue
            current_spaces += 1
            shift_by = len(numbers[idx])
            spaces, current_spaces = checkByFirstNumber(pi, start_idx + shift_by, current_spaces,
                                                        numbers, spaces, cache)
            if start_idx in cache:
                cache[start_idx] = min(spaces - current_spaces, cache[start_idx])
            else:
                cache[start_idx] = spaces - current_spaces
            current_spaces -= 1
    return spaces, current_spaces
