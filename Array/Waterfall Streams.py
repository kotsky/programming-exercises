'''
Return how many water will be on the last row
of the given matrix.

Promt: https://www.algoexpert.io/questions/Waterfall%20Streams
'''


# array = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0],
# ]
# source = 3
# print(waterfallStreams(array, source))

# O(w^2 * h) Time / O(w + h) Space

def waterfallStreams(array, source):
    brackets_of_water = [0] * len(array[0])
    return water_flow_go_down(100, brackets_of_water, array, [0, source])


def water_flow_go_down(current_water, brackets, array, current_indexes):
    row, col = current_indexes

    while array[row][col] == 0:
        row += 1
        if row == len(array)-1:
            brackets[col] += current_water
            return brackets

    water_flow_go_sides(current_water/2, brackets, array, [row-1, col], -1)    # left
    water_flow_go_sides(current_water/2, brackets, array, [row-1, col], +1)    # right
    return brackets


def water_flow_go_sides(current_water, brackets, array, current_indexes, side):
    row, col = current_indexes

    while 0 <= col < len(array[0]) and array[row][col] == 0 and array[row+1][col] != 0:
        col += side
    if not 0 <= col < len(array[0]) or array[row][col] != 0:
        return brackets
    return water_flow_go_down(current_water, brackets, array, [row, col])
    
