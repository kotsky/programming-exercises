'''
To find all quadruples from the given array, sum of which will give a target sum.
'''

# Version 1
# With array.sort()

def fourNumberSum(array, targetSum):
	if len(array) < 4:
		return []
  array.sort()
	quadruples = []
  
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			left = j+1
			right = len(array) - 1
			
			while right > left:
				if array[right] + array[left] == (targetSum - array[i] - array[j]):
					quadruples.append([array[i], array[j], array[left], array[right]])
					right -= 1
					left += 1
				elif array[right] + array[left] < (targetSum - array[i] - array[j]):
					left += 1
				else:
					right -= 1
	return quadruples
  
  
  
# Version 2
# Through H-table
def fourNumberSum(array, targetSum):
	if len(array) < 4:
		return []
	quadruples = []
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			locatl_target = targetSum - array[i] - array[j]
			table = {}
			for k in range(j+1, len(array)):
				if array[k] in table:
					quadruples.append([array[i], array[j], array[k], locatl_target - array[k]])
				else:
					table[locatl_target-array[k]] = array[k]
			
	return quadruples
