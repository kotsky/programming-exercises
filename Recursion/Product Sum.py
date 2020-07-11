'''
To find sum of each element of given array. [x, [y, z]] => x + 2 * (y + z)
'''

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, factor=1):
    suma = 0
	for i in range(len(array)):
		if type(array[i]) is list:
			suma += productSum(array[i], factor+1)
		else:
			suma += array[i]
	return suma * factor
		
