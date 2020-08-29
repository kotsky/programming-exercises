'''
(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger")) => ["go", "powerranger"]
TO define patterns as x = "go" and y = "powerrangers" in the given string.

Count of x and y. Then calculate len of possible substrings. And check every time for new substring of x.
'''


def patternMatcher(pattern, string):
    if pattern == "" or len(pattern) > len(string):
        return []

    new_pattern = separartion(pattern)
    flag = None
    if new_pattern[0] != 'x':
        flag = 1
        for idx in range(len(new_pattern)):
            if new_pattern[idx] == 'x':
                new_pattern[idx] = 'y'
            else:
                new_pattern[idx] = 'x'

    count_x = 0
    count_y = 0
    position_y = None
    for idx in range(len(new_pattern)):
        if new_pattern[idx] == 'x':
            count_x += 1
        else:
            count_y += 1
            if position_y is None:
                position_y = idx

    if count_x == 0 or count_y == 0:
        count = count_x if count_x != 0 else count_y
        if len(string) % count != 0:
            return []
        length = len(string)
        substring_range = length//count
        substring = string[0:substring_range]
        for i in range(1, count):
            if substring != string[i*substring_range:(i*substring_range+substring_range)]:
                return []

        return [substring, ""] if flag is None else ["", substring]

    else:

        for end in range(1, len(string)):
            x = string[0:end]
            len_x = len(x)
            len_y = (len(string) - len_x*count_x)//count_y if (len(string) - len_x*count_x) % count_y == 0 else -1
            if len_y == -1:
                continue
            y = string[len_x*position_y:(len_y + len_x*position_y)]

            check_list = new_pattern.copy()
            for idx in range(len(check_list)):
                if check_list[idx] == 'x':
                    check_list[idx] = x
                else:
                    check_list[idx] = y

            if "".join(check_list) == string:
                return [x, y] if flag is None else [y, x]

        return []


def separartion(string):
    array = []
    for letter in string:
        array.append(letter)
    return array



print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))

