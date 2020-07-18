'''
Move given elements from the array to the end: [2, 1, 2, 3] => [1, 3, 2, 2] / [3, 1, 2, 2]
'''

def moveElementToEnd(array, toMove):
  left = 0
	right = len(array)-1
	while (right-left) > 0:
		if array[right] == toMove:
			right -= 1
		else:
			if array[left] != toMove:
				left += 1
			else:
				array[left], array[right] = array[right], array[left]
				right -= 1
				left += 1
	return array
