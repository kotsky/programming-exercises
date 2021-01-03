'''
       Input:
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        
       Output:
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
'''

def three_number_sort(array, order):
	p1 = 0
	for idx in range(len(order)):
		p2 = p1
		while p2 < len(array) and p1 < len(array):
			if array[p1] == order[idx] and array[p2] == order[idx]:
				p1 += 1
				p2 += 1
			elif array[p2] != order[idx]:
				p2 += 1
			elif array[p1] == order[idx]:
				p1 += 1
			else:
				swap(array, p1, p2)
				p1 += 1
				p2 += 1
	return array
		
def swap(array, p1, p2):
	array[p1], array[p2] = array[p2], array[p1]
