'''
Move given elements from the array to the end: [2, 1, 2, 3] => Ver1 - [1, 3, 2, 2] / Ver2 - [3, 1, 2, 2]
Ver1: Swapping with remembering of toMove starting point.
Ver2: 2 pointers at the start/end. At first check end, then move left.
'''

def moveElementToEnd(array, toMove):
	start_point = -1
	for i in range(len(array)):
		if array[i] != toMove and start_point >= 0:
			array[i], array[start_point] = array[start_point], array[i]
			start_point += 1
			if array[start_point] != toMove:
				start_point = -1
		else:
			if array[i] == toMove and start_point == -1:
				start_point = i
	return array

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
