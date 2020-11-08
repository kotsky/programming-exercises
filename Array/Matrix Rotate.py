''' Rotate matrix on 90 clockwise. In place.
Input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

The idea:
  1. Find a pattern. Write down the finale result.
  2. Flip it vertically/horizontally.
  3. How you can get this new matrix from input matrix? Search for diagonal swaps.
'''

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# O(N) Time / O(1) Space

def matrixRotate(matrix):   # matrix N*N with only integers
    print(matrix)

    def _swap_diagonal(row, col, matrix):
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def _swap_column(row, col, matrix):
        matrix[row][col], matrix[row][-1 - col] = matrix[row][-1 - col], matrix[row][col]

    # Swap by diagonal
    for row in range(len(matrix)):
        for col in range(row+1, len(matrix)):
            _swap_diagonal(row, col, matrix)
    print(matrix)

    # flip by vertical axis
    for row in range(len(matrix)):
        for col in range(len(matrix)//2):
            _swap_column(row, col, matrix)
    print(matrix)
    return matrix

matrixRotate(matrix)
