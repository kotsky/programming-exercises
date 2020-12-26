"""
Remove all islands inside given matrix. Island is a land of 1s, which
is not connected to bourder of matrix.

matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1]
  ]
  
Find with DFS which 1s is from the land (bourders), and then
flip other 1s on 0.
"""

def removeIslands(matrix):

    visited = [[[False] for x in matrix[0]] for y in matrix]

    for row in range(1, len(matrix)-1):
        for col in range(1, len(matrix[0])-1):
            if matrix[row][col] == 0 or visited[row][col] is True:
                continue

            if is_island(matrix, row, col, visited):
                remove_island(matrix, row, col)
    return matrix

def is_island(matrix, row, col, visited):

    if matrix[row][col] == 0 or visited[row][col] is True:
        return True

    if matrix[row][col] == 1 and at_boundary(matrix, row, col):
        # it's not an island
        return False

    visited[row][col] = True

    return is_island(matrix, row-1, col, visited) and is_island(matrix, row+1, col, visited) \
           and is_island(matrix, row, col-1, visited) and is_island(matrix, row, col+1, visited)


def at_boundary(matrix, row, col):
    at_row = row == 0 or row == len(matrix) - 1
    at_col = col == 0 or col == len(matrix[0]) - 1

    return at_col or at_row


def remove_island(matrix, row, col):
    if matrix[row][col] == 0:   # or at_boundary(matrix, row) or at_boundary(matrix, col)
        return

    matrix[row][col] = 0
    remove_island(matrix, row-1, col)
    remove_island(matrix, row, col-1)
    remove_island(matrix, row+1, col)
    remove_island(matrix, row, col+1)
    return
