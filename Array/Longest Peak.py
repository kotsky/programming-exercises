'''
To find the longest peak in the array. [1, 1, 2, 3, 2, 2] => [1, 2, 3, 2] = 4

First, to find it's peak, then go in left and right to find its range.
'''
def longestPeak(array):
	if len(array) < 3:
		return 0

	peak_lenght = 0
	i = 1
	while i < len(array)-1:
		if array[i-1] < array[i] and array[i+1] < array[i]: # if there is a peak
			j = i
			while j >= 1 and array[j-1] < array[j]:	# we move left
				j -= 1
			start_index = j
			j = i
			while array[j+1] < array[j]:	# we move right
				j += 1
				if j == len(array)-1:	# if we are at the boundary - break
					break
			peak_lenght = max(peak_lenght, j - start_index + 1)
			i = j
		i += 1
	return peak_lenght
