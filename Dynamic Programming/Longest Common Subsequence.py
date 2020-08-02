'''
To find a common subsequence for both input strings. 
They must be in the same order. 
Input: "ZXVVYZW", "XKYKZPW")
Output = ["X", "Y", "Z", "W"]
'''

# O(N*M) TS
# To build M*N matrix and go through solving
# each sub problem. Then, go from the end of 
# the matrix (right -> up) and collect all found letters,
# when adjacent elements are equivalent.


def longestCommonSubsequence(str1, str2):
    matrix = []  # memo matrix
	# I(N*M) S
    for x in range(len(str2) + 1):
        matrix.append([0] * (len(str1) + 1))

	# O(N*M) T
    for i in range(len(str2)):  # go down
        for j in range(len(str1)):  # go right
            if str2[i] == str1[j]:
                matrix[i + 1][j + 1] = 1 + matrix[i][j]
            else:
                matrix[i + 1][j + 1] = max(matrix[i][j + 1], matrix[i + 1][j])

    # find elements
    ver = len(str1)
    hor = len(str2)
    common_letters = []

	# O(N+M) T
    while matrix[hor][ver] != 0:
        if matrix[hor][ver - 1] == matrix[hor - 1][ver] and matrix[hor][ver] > matrix[hor - 1][ver]:
            common_letters.append(str2[hor-1])
            ver -= 1
        else:
            if matrix[hor][ver] == matrix[hor][ver - 1]:
                ver -= 1
            elif matrix[hor][ver] == matrix[hor - 1][ver]:
                hor -= 1

    return list(reversed(common_letters))
