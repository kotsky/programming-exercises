'''
You are given array as = [[1, 0, 0, 1, 0], 
                          [1, 0, 1, 0, 0], 
                          [0, 0, 1, 0, 1], 
                          [1, 0, 1, 0, 1], 
                          [1, 0, 1, 1, 0]]
1 - is river pard, 0 - land part. To defind lenght of each river. 
River can go only in non-diagonal way.

Expected output = [1, 2, 2, 2, 5]
'''

# To use DFS through each element in matrix. 
# To overwrite matrix with visited elements, or 
# to create new matrix to remind, which element we
# visited before

def riverSizes(matrix):
	sizes = []
	for m in range(len(matrix)):  
		for n in range(len(matrix[0])):
			river_size = deepFirstSearch(matrix, m, n, river_size=0)
			if river_size != 0:
				sizes.append(river_size)
	return sizes

		
def deepFirstSearch(matrix, row, col, river_size):
	if matrix[row][col] != 1:
		return river_size
	
	river_size += 1
	matrix[row][col] = 2
	
	if row >= 1:
		river_size = deepFirstSearch(matrix, row-1, col, river_size)
	if row < len(matrix)-1:
		river_size = deepFirstSearch(matrix, row+1, col, river_size)
	if col >= 1:
		river_size = deepFirstSearch(matrix, row, col-1, river_size)
	if col < len(matrix[0])-1:
		river_size = deepFirstSearch(matrix, row, col+1, river_size)
		
	return river_size
	
