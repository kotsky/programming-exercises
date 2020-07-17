'''
Matrix has sorted rows and coloums. Return indexes of target value.
'''

def searchInSortedMatrix(matrix, target):
    r = 0
	c = len(matrix[0])-1
	while r < len(matrix) and c >= 0:
		current_point = matrix[r][c]
		if current_point == target:
			return [r, c]
		elif current_point < target:
			r += 1
		else:
			c -= 1
	return [-1, -1]
