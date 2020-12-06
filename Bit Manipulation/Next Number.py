"""

Find max and min number based on 1s
in bit format of the given number

Example:

    print(min_max_of_1s(9)) # => (3, 12) // 1001 => (11, 1100)

"""


def min_max_of_1s(number):
    def get_count_of_1s_from(number):
        count_of_1s = 0
        count = 0

        while number > 0:
            remain = int(number % 2)
            if remain == 1:
                count_of_1s += 1
            number //= 2
            count += 1

        return count_of_1s, count

    def get_min_number(count_1s):
        min_number = 0

        while count_1s > 0:
            min_number += pow(2, count_1s-1)
            count_1s -= 1

        return min_number

    def get_max_number(count_1s, total):
        max_number = 0

        zeros_bias = total - count_1s

        while count_1s > 0:
            max_number += pow(2, count_1s-1 + zeros_bias)
            count_1s -= 1

        return max_number

    bits_1s, total_bits = get_count_of_1s_from(number)
    return get_min_number(bits_1s), get_max_number(bits_1s, total_bits)
