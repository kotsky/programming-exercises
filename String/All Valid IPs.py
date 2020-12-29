'''All possible valid IPs 

Find all valid IPv4 from a given IP string address
ip = "1921680". 

The idea:
Simply split by 4 parts and validate them step by step
Take a note, that "00" part is not valid. Also, 
part range is from 0 to 255 inclusively.

There are 2 methods. The 2nd one works in 2 times faster:

ip = "1921680"
avg1 = 0
for i in range(10000):
    start1 = time.time()
    r1 = valid_ip_addresses_v1(ip)
    end1 = time.time()
    time1 = end1 - start1
    avg1 += time1
print("Method 1: integer. its time: ", avg1/10000)

avg2 = 0
for i in range(10000):
    start2 = time.time()
    r2 = valid_ip_addresses_v2(ip)
    end2 = time.time()
    time2 = end2 - start2
    avg2 += time2
print("Method 2: string. its time: ", avg2/10000)

#==============
# Method 1: integer. its time:  0.00011989948749542236
# Method 2: string. its time:  4.899656772613525e-05


'''

import time


def valid_ip_addresses_v1(string):

    def _list_of_valid_ips(ip_array, dots_holder):
        valid_ips = []
        for dots in dots_holder:
            new_valid_ip = []
            count = 0
            for idx in range(len(ip_array)):
                new_valid_ip.append(str(ip_array[idx]))
                if count < 3 and idx == dots[count]:
                    new_valid_ip.append(".")
                    count += 1
            valid_ips.append("".join(new_valid_ip))
        return valid_ips

    def _is_part_valid(array, start_idx, end_idx):

        def __generate_number(array, start_idx, end_idx):
            number = 0
            factor = 1
            while end_idx - start_idx >= 0:
                number += factor * array[end_idx]
                end_idx -= 1
                factor *= 10
            return number

        if not start_idx <= len(array) - 1 or not end_idx <= len(array) - 1:
            return False

        if end_idx - start_idx > 2:
            return False
        if array[start_idx] == 0 and end_idx - start_idx != 0:
            return False
        number = __generate_number(array, start_idx, end_idx)
        if number > 255:
            return False
        return True

    if not 4 <= len(string) <= 12:
        return []

    ip_array = []
    for letter in string:
        ip_array.append(int(letter))

    max_part_length = 3
    dots_holder = []

    for i in range(max_part_length):
        if _is_part_valid(ip_array, 0, i):

            for j in range(max_part_length):
                if _is_part_valid(ip_array, i + 1, i + 1 + j):

                    for k in range(max_part_length):
                        if _is_part_valid(ip_array, i + j + 2, i + j + 2 + k):
                            if _is_part_valid(ip_array, i + j + k + 3, len(ip_array)-1):
                                dots_holder.append([i, i + 1 + j, i + j + 2 + k])

    return _list_of_valid_ips(ip_array, dots_holder)


def valid_ip_addresses_v2(string):

    def _is_part_valid(part_string):
        if len(part_string) > 3 or part_string == '':
            return False
        if len(part_string) > 1 and part_string[0] == "0":
            return False
        if int(part_string) > 255:
            return False
        return True

    if not 4 <= len(string) <= 12:
        return []

    max_part_length = 3
    valid_ips = []
    parts = [""] * 4

    for i in range(max_part_length):
        parts[0] = string[:i+1]
        if _is_part_valid(parts[0]):

            for j in range(i+1, min(i+1+max_part_length, len(string))):
                parts[1] = string[i+1:j+1]
                if _is_part_valid(parts[1]):

                    for k in range(j+1, min(j+1+max_part_length, len(string))):
                        parts[2] = string[j+1:k+1]
                        if _is_part_valid(parts[2]):
                            parts[3] = string[k+1:]
                            if _is_part_valid(parts[3]):
                                valid_ips.append(".".join(parts))
    return valid_ips
