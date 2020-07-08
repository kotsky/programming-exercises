'''
To find 3 largest elements in given array. 
Output is sorted array of largest elements.
'''


# Solution 1 O(N)

def findThreeLargestNumbers(array):
	
	if len(array) < 3:
		return []
	
    ans = [None]*3
	
	
	for i in range(3):
		gl = -10000000
		for num in array:

			if gl < num:
				gl = num
		
		array.remove(gl)
		ans[-1-i] = gl
	
	return ans
		

# Solution 2 O(N) (without "remove" func - faster )

def findThreeLargestNumbers(array):
	
	if len(array) < 3:
		return []
	
    ans = [None]*3
	index = [None]*3
	gl = -9999999
	for i in range(len(array)):
		
		if gl < array[i]:
			gl = array[i]
			index[2] = i
			
	ans[2] = gl
	
	gl = -9999999
	for i in range(len(array)):
		
		if gl < array[i] and i != index[2]:
			gl = array[i]
			index[1] = i
			
	ans[1] = gl
	
	gl = -9999999
	for i in range(len(array)):
		
		if gl < array[i]  and i != index[2] and i != index[1] :
			gl = array[i]
			index[0] = i
			
	ans[0] = gl

	return ans

