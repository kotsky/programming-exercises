
# O(N^2) T worst / O(1) S

def insertionSort(array):

	for i in range(1,len(array)):
		
		second = i
		while second != 0:
			if array[second] < array[second-1]:
				array[second], array[second-1] = array[second-1], array[second]
				second -= 1
			else:
				break
				
	return array
