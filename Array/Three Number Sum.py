'''
To find three elements in the given array, which can give in sum a targetSum.
Logic is to take each element, subtract it from the targetSum and with 2 pointers left-right to check sum of other 2 elements.
'''

def threeNumberSum(array, targetSum):
    
	if len(array) < 3:
		return []
	
	array.sort()	# 
	answer = []
	
	for numToCheck in range(len(array)):	# 
		targetLocalSum = targetSum - array[numToCheck]
		leftPointer = numToCheck + 1
		rightPointer = len(array)-1
		while (rightPointer - leftPointer) > 0:
			
			if targetLocalSum == (array[rightPointer] + array[leftPointer]):
				answer.append([array[numToCheck], array[leftPointer], array[rightPointer]])
				leftPointer += 1
			elif targetLocalSum < (array[rightPointer] + array[leftPointer]):
				rightPointer -= 1
			else:
				leftPointer += 1
	
	return answer
