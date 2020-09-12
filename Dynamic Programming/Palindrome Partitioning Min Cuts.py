'''
Define min cuts needed to split the given string onto palindromes.
noonabbad -> noon | abba | d => 2
'''

# To build matrix of palindromes in O(n^2) time/space by 
# checking previous solved elements in matrix.
# Otherwise, O(n^3) T if to generate each subsring and
# check if it's palindrome. Below is O(n^2) solution.
# Then, build 1D array "spaces" of mins cuts, and on each index 0->i
# we check, if sub_string from j to i is palindrom (if matrix[j][i])
# and compare with the value before at idx [i-1] + 1(cut). 
# If j=0 -> i is palindrom, then spaces[i] = 0

def palindromePartitioningMinCuts(string):
    matrix = [[True if i == j else False for i in range(len(string))] for j in range(len(string))]
    definePalindromes(matrix, string)
    spaces = [0] * len(string)
    defineMinSpaces(matrix, spaces, string)
    return None if not len(spaces) else spaces[-1]


def definePalindromes(matrix, string):
    for i in range(1, len(string)):
        for j in range(i):
            if string[j] == string[i]:
                if i == j + 1 or matrix[j + 1][i - 1]:
                    matrix[j][i] = True
                    
# Version 2 of definePalindromes (simplified) O(n^2) as well TS
'''
def definePalindromes(matrix, string):
	matrix[0][0] = True
	for i in range(1, len(string)):
		explorePolindrom(string, i, i, matrix)
		explorePolindrom(string, i-1, i, matrix)

		
def explorePolindrom(string, p1, p2, matrix):
	# p1 - start index
	# p2 - end index inclusively
	while p1 >= 0 and p2 < len(string):
		if string[p1] == string[p2]:
			matrix[p1][p2] = True
			p1 -= 1
			p2 += 1
		else:
			break
'''


def defineMinSpaces(matrix, spaces, string):
    for i in range(1, len(spaces)):
        spaces[i] = spaces[i - 1] + 1
        for j in range(i):
            if matrix[j][i]:
                if j == 0:
                    spaces[i] = 0
                    break
                else:
                    spaces[i] = min(spaces[i], spaces[j - 1] + 1)
                    
print(palindromePartitioningMinCuts("noonabbad"))
