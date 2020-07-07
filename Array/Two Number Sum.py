'''
To find out if an array has 2 elements with target sum. Return those elements.
'''
def twoNumberSum(array, targetSum):
    
	d = {}
	ans = []
	
	if len(array) < 2:
		return ans
	
	for i in range(len(array)):
		try:					
			if (targetSum - array[i]) == d[array[i]]:
				ans = [targetSum-array[i], array[i]]
				return ans
		except:
			d[targetSum - array[i]] = array[i]
			
	return ans
  
  '''
  for i in range(len(array)):
    if (targetSum - array[i]) in d:
      return [targetSum - array[i], array[i]]
    else:
      d[array[i]] = True

    return ans
  '''
  
  
