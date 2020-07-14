'''
Elements of the givem array are as jump count. Is the given array a single loop
according to those jumps?
'''

# Version 1
# O(N) T / O(1) S
def hasSingleCycle(array):
	counter_index = 0
	temp = array[counter_index]
	for i in range(len(array)):
		counter_index = ( temp + counter_index ) % len(array)
		if array[counter_index] is True:
			return False
		temp = array[counter_index]
		array[counter_index] = True
	return True
		
# Version 2
# O(N) TS
def hasSingleCycle(array):
	came_in = [0] * len(array)
	counter = len(array)
	current_index = 0
	came_in[current_index] = 0
	while counter > 0:
		jump = array[current_index]
		current_index = (current_index + jump) % len(array)
		if current_index < 0:
			current_index += len(array)
		came_in[current_index] += 1
		if came_in[current_index] > 1:
			return False
		counter -= 1
	return True
