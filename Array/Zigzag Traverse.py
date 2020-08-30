'''
Change 2d matrix into 1d matrix in zigzag manner:
 [[1, 3, 4, 10], 
  [2, 5, 9, 11], 
  [6, 8, 12, 15], 
  [7, 13, 14, 16]] 
  => [1, 2, 3, ..., 15, 16]
'''

def zigzagTraverse(array):
    try:
        zigzag = []
    except:
        return array

    dl = "down_left"
    ur = "up_right"
    direction = dl
    row = 0
    col = 0
    while len(zigzag) < len(array[0] * len(array)):
        zigzag.append(array[row][col])
        if direction == dl:
            if row < len(array) - 1 and col == 0:
                row += 1
                direction = ur
            elif row == len(array) - 1:
                col += 1
                direction = ur
            else:
                row += 1
                col -= 1
        else:
            if col < len(array[0]) - 1 and row == 0:
                col += 1
                direction = dl
            elif col == len(array[0]) - 1:
                row += 1
                direction = dl
            else:
                row -= 1
                col += 1
    return zigzag


test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(zigzagTraverse(test))
