'''
Bubble sort algo. O(N^2) T / O(1) S
'''

def bubbleSort(array):
    
	if array is None:
		return None
	
	lenArray = len(array)
	
	if lenArray == 1 or lenArray == 0:
		return array
	
	while True:
		wasSwap = False
		index = 0
		while index < (lenArray - 1):
			if array[index] > array[index + 1]:
				array[index], array[index+1] = array[index+1], array[index]
				wasSwap = True
			index += 1
			
		if wasSwap == False:
			return array
		lenArray -= 1
			
			
			
			
