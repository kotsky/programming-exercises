# O(N^2) T / O(1) S

def selectionSort(array):
    
	for j in range(len(array)-1):
		upper_pointer = j
		lower_pointer = j

		for i in range(lower_pointer, len(array)):
			if array[upper_pointer] > array[i]:
				upper_pointer = i

		array[lower_pointer], array[upper_pointer] = array[upper_pointer], array[lower_pointer]
	
	return array
