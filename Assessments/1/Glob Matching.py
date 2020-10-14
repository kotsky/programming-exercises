# Failed: 1.4 hours / why: didn't realise DP method of solving and went through wrong recursive approach.

'''
Return True if fileName is possible to present by pattern, where '?' can mean only one any character, 
and '*' mean any amount of any character (quantity from 0 to ...). 

fileName = "abcdefg"
pattern = "a*e?g"
output = true
'''


def globMatching(fileName, pattern):
    matrix_of_truth = createMatrixOfTruth(fileName, pattern)
    return matrix_of_truth[-1][-1]
                                                       
	
def createMatrixOfTruth(fileName, pattern):
    matrix = [[False for x in range(len(pattern) + 1)] for x in range(len(fileName) + 1)]
    matrix[0][0] = True
	for j in range(1, len(pattern) + 1):
		if pattern[j-1] == '*':
			matrix[0][j] = matrix[0][j-1]
	
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if pattern[j-1] == fileName[i-1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            elif pattern[j-1] == '*':
                matrix[i][j] = matrix[i - 1][j] or matrix[i][j - 1]
            elif pattern[j-1] == '?':
                matrix[i][j] = matrix[i - 1][j - 1]
    return matrix
