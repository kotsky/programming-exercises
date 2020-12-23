"""

Input:
    1) array of positive integers
    2) k - some positive value

Output: count - number of examples when numbers
        from the array can give k sum.

Example:
    [2, 3, 6, 9, 3, 5, 2, 1], 8
    [[2, 3, 3], [2, 3, 2, 1], [2, 6], [2, 3, 2, 1], [2, 5, 1], [3, 3, 2], [3, 5], [6, 2], [3, 5], [5, 2, 1]]

"""


def count_target_sum_combination(array, target_sum):
    combinations = []
    helper_count_target_sum_combination(array, 0, target_sum, combinations, [])
    return combinations


def helper_count_target_sum_combination(array,
                                        current_idx,
                                        current_target_sum,
                                        storage, temp_storage):

    if current_target_sum == 0:
        storage.append(temp_storage.copy())
        return
    elif current_target_sum < 0:
        return
    else:
        for idx in range(current_idx, len(array)):
            temp_storage.append(array[idx])
            helper_count_target_sum_combination(array, idx+1, current_target_sum - array[idx], 
                                                storage, temp_storage)
            temp_storage.pop()
        return


count = count_target_sum_combination([2, 3, 6, 9, 3, 5, 2, 1], 8)
print(count)
