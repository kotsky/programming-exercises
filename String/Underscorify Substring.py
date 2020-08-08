'''
underscorifySubstring("testthis is a testtest to see if testestest it works", "test"),
            "_test_this is a _testtest_ to see if _testestest_ it works"
'''

def underscorifySubstring(string, substring):
    special_symbol = '_'
    intervals = []
    lenSub = len(substring)
    # Step 1: find where we have substring
    for i in range(len(string)):
        if string[i:lenSub + i] == substring:
            intervals.append([i, (lenSub + i)])
    if intervals == []:
        return string
    # Step 2: merge intervals
    merged_interval = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i - 1][1] >= intervals[i][0]:
            merged_interval[-1][1] = intervals[i][1]
        else:
            merged_interval.append(intervals[i])

    # Step 3: create new string
    new_string = []
    counter = 0
    reference = merged_interval[0][0]
    for i in range(len(string)):
        if i == reference:
            new_string.append(special_symbol)
            new_string.append(string[i])
            counter += 1
            if counter > len(merged_interval) * 2 - 1:
                reference = -1
		new_string.append(string[i+1:])
                break
            reference = merged_interval[counter // 2][counter % 2]
        else:
            new_string.append(string[i])
    if reference != -1:
        new_string.append(special_symbol)

    return "".join(new_string)
