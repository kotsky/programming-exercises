'''
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''


def spiralTraverse(array):
	if type(array[0]) is None:
		return array
    	a = 0			# vertical pointer 1
	b = len(array[0])-1 	# vertiacal pointer 2
	c = 0			# horizontal pointer 1
	d = len(array)-1	# horizontal pointer 2
	direction = 0		# direction ->
	one_d = []	# answer: one dimension array
	
	while b >= a and c <= d:
		if direction == 0:
			nums = array[c][a:b+1]
			for num in nums:
				one_d.append(num)
			c += 1
			
		elif direction == 1:
			for index in range(c, d+1):
				one_d.append(array[index][b])
			b -= 1
			
		elif direction == 2:
			nums = array[d][a:b+1]
			for i in range(len(nums)):
				one_d.append(nums[-1-i])
			d -= 1
			
		else:
			for index in range(d, c-1, -1):
				one_d.append(array[index][a])
			a += 1
			
        direction = (direction + 1) % 4
	return one_d

			

                

