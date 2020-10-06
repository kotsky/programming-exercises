'''
Return True or False if there is a Zero Square (which is created only from "0" as bounder and more or equal than 2x2 size) 
in the given matrix.

matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1],
        ]
Output = True
'''
# n - number by row
# m - number by column

'''
The idea is traverse through each element of the matrix 
and assume, that it might be a start point of our valid zero square, 
we call function checkValidZeroSquare at that point [n,m].

At version 2, checkValidZeroSquare was done by traversing each line
of possible zero square and try to validate it (when every element in the line is "0").
To check its square, 4 line traversing were needed, which took O(n) time complexity each.
Also, each element of the matrix can be start point for other n squares.
In total it brings O(n^2) time complexity just for checkValidZeroSquare.

The idea in Version 3 was to build hash table of special intervals,
which will optimize line verification -> reduca time complexity to constant.
When we want to validate line in the matrix from point start_n -> end_n,
we look its values in the table and check, if we had "1" on the interval 
start_n -> end_n.

intervalsOfZeros does converting like row#1 = [0, 0, 1, 1, 0, 0, 0, 1, 0] from the matrix line
into intervals_of_zeros[1_c] = [0, 0, -1, -1, 2, 2, 2, -1, 3], where intervals shown
as a positive integers for "0" and as a "-1" for "1". If positive integers are same,
it means that "0"s are from the same adjacent interval of just zeros.
All of this gives faster line validation.
'''



# Version 3. O(n^3) Time / O(n^2) Space
# Square check method with pre-computation
def squareOfZeroes(matrix):
    if len(matrix) <= 1:
        return False

    # O(n^2) Time / O(n^2) Space
    intervals_of_zeros = intervalsOfZeros(matrix)

    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[n][m] == 1:
                continue
            isZeroSquare = checkValidZeroSquare(matrix, n, m, intervals_of_zeros)
            if isZeroSquare:
                return True
    return False


def checkValidZeroSquare(matrix, start_n, start_m, intervals_of_zeros):
    n = start_n + 1
    m = start_m + 1

    while n < len(matrix) and m < len(matrix[0]):
        if checkLine(start_n, start_m, n, m, "hor", intervals_of_zeros) \
                and checkLine(n, start_m, n, m, "hor", intervals_of_zeros) \
                and checkLine(start_n, start_m, n, m, "ver", intervals_of_zeros) \
                and checkLine(start_n, m, n, m, "ver", intervals_of_zeros):
            return True
        n += 1
        m += 1
    return False


def checkLine(start_n, start_m, n, m, direction, intervals_of_zeros):
    if direction == "hor":
        return checkIntoIntervalOfZeros(str(start_n), "c", start_m, m, intervals_of_zeros)
    else:
        return checkIntoIntervalOfZeros("r", str(start_m), start_n, n, intervals_of_zeros)

	
# Constant time check if interval form start_idx to end_idx has "1"
def checkIntoIntervalOfZeros(str_row, str_col, start_idx, end_idx, intervals_of_zeros):
    key = createKeyFromMatrixIdx(str_row, str_col)
    interval_of_zeros = intervals_of_zeros[key]
    if interval_of_zeros[start_idx] != -1 and interval_of_zeros[end_idx] != -1:
        if interval_of_zeros[start_idx] == interval_of_zeros[end_idx]:
            return True
    return False


def intervalsOfZeros(matrix):
    intervals = {}
    # rows hashing
    for row in range(len(matrix)):
        createRelevantIntervals(intervals, matrix, row, -1)
    # cols hashing
    for col in range(len(matrix)):
        createRelevantIntervals(intervals, matrix, -1, col)
    return intervals


def createRelevantIntervals(intervals, matrix, row, col):
    if row == -1:
        key = createKeyFromMatrixIdx("r", str(col))
        intervals[key] = [-1] * len(matrix)
        flag = 0
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                intervals[key][row] = flag
            else:
                flag += 1
    else:
        key = createKeyFromMatrixIdx(str(row), "c")
        intervals[key] = [-1] * len(matrix)
        flag = 0
        for col in range(len(matrix)):
            if matrix[row][col] == 0:
                intervals[key][col] = flag
            else:
                flag += 1


def createKeyFromMatrixIdx(str_row, str_col):
    return str_row + "_" + str_col
	

'''
# Version 2. O(n^4) Time / O(1) Space
# Square check method: traversing through each line 
# through each element and check if this line is valid
def squareOfZeroes(matrix):
    if len(matrix) <= 1:
        return False

    # Step 1: traverse through:
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[n][m] == 1:
                continue
			# Step 2: check if matrix[n][m] can be start of
			# zero square
            isZeroSquare = checkValidZeroSquare(matrix, n, m)
            if isZeroSquare:
                return True
    return False


def checkValidZeroSquare(matrix, start_n, start_m):
    n = start_n + 1
    m = start_m + 1

    while n < len(matrix) and m < len(matrix[0]):
        if checkLine(matrix, start_n, start_m, n, m, "hor") \
                and checkLine(matrix, n, start_m, n, m, "hor") \
                and checkLine(matrix, start_n, start_m, n, m, "ver") \
                and checkLine(matrix, start_n, m, n, m, "ver"):
            return True
        n += 1
        m += 1
    return False


def checkLine(matrix, start_n, start_m, n, m, direction):
    if direction == "hor":
        for c in range(start_m, m + 1):
			# Save in cache st_x -> x !!!
            if matrix[start_n][c] == 1:
                return False
        return True
    else:
        for r in range(start_n, n + 1):
            if matrix[r][start_m] == 1:
                return False
        return True
'''

	
'''
# Version 1. O(n^6) Time / O(n^2) Space
# Recursively check if we can have valid zero square
# from each point in the matrix
def squareOfZeroes(matrix):
    if len(matrix) <= 1:
        return False

    visited = [[False for n in matrix] for n in matrix]

    # Step 1: traverse through:
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[n][m] == 1:
                continue
            # Step 2: assuming that matrix[n][m] is start of
            # valid zero square, explore it
            isZeroSquare = exploreFromPoint(matrix, n, m, visited, "right")
            if isZeroSquare:
                return True
    return False


def exploreFromPoint(matrix, n, m, visited, direction):
    st_n = n
    st_m = m
    isValidZeroSquare = False
    if direction == "right":
        if m == len(matrix):
            return False
        visited[n][m] = True
        m += 1
        while m < len(matrix) and matrix[n][m] == 0:
            isValidZeroSquare = exploreFromPoint(matrix, n, m, visited, "down")
            visited[n][m] = False
            m += 1
            if isValidZeroSquare:
                break
        visited[st_n][st_m] = False
        return isValidZeroSquare
    elif direction == "down":
        if n == len(matrix):
            return False
        visited[n][m] = True
        n += 1
        while n < len(matrix) and matrix[n][m] == 0:
            isValidZeroSquare = exploreFromPoint(matrix, n, m, visited, "left")
            visited[n][m] = False
            n += 1
            if isValidZeroSquare:
                break
        visited[st_n][st_m] = False
        return isValidZeroSquare
    elif direction == "left":
        if m < 0:
            return False
        visited[n][m] = True
        m -= 1
        while m >= 0 and matrix[n][m] == 0:
            isValidZeroSquare = exploreFromPoint(matrix, n, m, visited, "up")
            visited[n][m] = False
            m -= 1
            if isValidZeroSquare:
                break
        visited[st_n][st_m] = False
        return isValidZeroSquare
    else:
        if n < 0:
            return False
        visited[n][m] = True
        n -= 1
        while n >= 0 and matrix[n][m] == 0:
            if visited[n][m]:
                return True
            n -= 1
        return False
'''
