'''
Define min cuts needed to split the given string onto palindromes.
noonabbad -> noon | abba | d => 2
'''

# To build matrix of palindromes in O(n^2) time by 
# checking previous solved elements in matrix.
# Otherwise, O(n^3) if to generate each subsring and
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
