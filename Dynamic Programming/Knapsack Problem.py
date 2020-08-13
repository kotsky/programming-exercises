'''
You have items, each of them has its value and weight [v, w].
Also, you have a bag with its capacity. Try to reach the max value of items,
which can be placed in this bag.
Input: items = [[1, 2], [4, 3], [5, 6], [6, 7]], bag capacity = 10), 
Output: [ max value = 10, items # in the use = [1, 3]]
'''


# O(n*c) TS

def knapsackProblem(items, capacity):
    m = [0] * (capacity + 1)
    matrix = []
    for i in range(len(items) + 1):
        matrix.append(m.copy())

    # step 1: solve for each item
    for v in range(1, len(items)+1):
        value, cap = items[v - 1]
        for c in range(capacity+1):
            if cap <= c:
                matrix[v][c] = max(matrix[v - 1][c], value + matrix[v - 1][c - cap])
            else:
                matrix[v][c] = matrix[v - 1][c]

    # step 2: backtrack of items
    ver = len(matrix) - 1
    hor = len(matrix[0]) - 1
    items_in_use = []
    while matrix[ver][hor] != 0:
        if matrix[ver][hor] != matrix[ver - 1][hor]:
            item = items[ver - 1]
            items_in_use.append(ver - 1)
            hor -= item[1]
            ver -= 1
        else:
            ver -= 1

    return [matrix[-1][-1], list(reversed(items_in_use))]
    
    
    '''
# O(n*c*n) T / O(n*c) S

def knapsackProblem(items, capacity):
    matrix = [[0, {}]] * (capacity + 1)

    for item_idx, item in enumerate(items):
        item_capacity = item[1]
        item_value = item[0]
        for cap in range(1, capacity + 1):
            temp = [0, {}]
            if item_capacity <= cap:
                if item_idx not in matrix[cap - item_capacity][1]:
                    temp[0] = matrix[cap - item_capacity][0]+item_value
                    temp[1] = matrix[cap - item_capacity][1].copy()
                    temp[1][item_idx] = True
            matrix[cap] = max([matrix[cap], matrix[cap - 1], temp], key=lambda x: x[0])

    array = []
    for key in matrix[-1][1]:
        array.append(key)

    return [matrix[-1][0], array]
    '''
