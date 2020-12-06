""" Conversion

How many bit flips you need to
convert integer A to integer B?

Example:
    
    print(flip_count(29, 15)) # 2

"""


def flip_count(a, b):

    count = 0

    while max(a, b) > 0:
        remain_a = a % 2
        a //= 2
        remain_b = b % 2
        b //= 2
        if remain_a != remain_b:
            count += 1

    return count
