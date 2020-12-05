"""

number = 1775

With only 1 option to flip 0 to 1,
count max possible adjacent 1s

Example:

    print(flip_bit(number))

"""


# O(log(number)) Time / O(1) Space

def flip_bit(number):
    idx = 0
    start_pointer = 0
    idx_zero = None
    count = 0
    max_count = 0

    while number > 0:
        remained = int(number % 2)
        number //= 2

        if remained == 0:
            if idx_zero is None:
                idx_zero = idx
            else:
                count -= (idx_zero + 1) - start_pointer
                start_pointer = idx_zero + 1
                idx_zero = idx
                # count = max(count, 0)
        count += 1
        max_count = max(max_count, count)
        idx += 1

    return max_count

# O(log(number)) Time / O(log(number)) Space

# def flip_bit(number):
#     array_of_bits = []
#
#     while number > 0:
#         remained = int(number % 2)
#         number //= 2
#         array_of_bits.append(remained)
#
#     start_pointer = 0
#     idx_zero = None
#     count = 0
#     max_count = 0
#
#     for idx in range(len(array_of_bits)):
#         if array_of_bits[idx] == 0:
#             if idx_zero is None:
#                 idx_zero = idx
#             else:
#                 count -= (idx_zero + 1) - start_pointer
#                 start_pointer = idx_zero + 1
#                 idx_zero = idx
#                 # count = max(count, 0)
#         count += 1
#         max_count = max(max_count, count)
#
#     return max_count
