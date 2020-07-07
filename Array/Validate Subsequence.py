'''
To find out if given subsequence is in array in the same order. 
'''

def isValidSubsequence(array, sequence):
    j = 0
	for i in range(len(array)):
		
		if array[i] == sequence[j]:
			j += 1
			if j == len(sequence):
				return True
	
	return False
