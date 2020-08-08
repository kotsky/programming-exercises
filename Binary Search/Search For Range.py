'''
{"array": [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], "target": 45}
                         ^                    ^                 
                         |                    |
               output=[stIdx,            endIds]
'''

# 3 step binary search

def searchForRange(array, target):
    # 1 step: find target
	left = 0
	right = len(array)-1
	point = None
	while right - left >= 0 :
		middle = (right+left)//2
		if array[middle] == target:
			point = middle
			break
		elif array[middle] > target:
			right = middle-1
		else:
			left = middle+1
	if point is None:
		return [-1, -1]
	
	# 2 step: find beginning
	left = 0 
	right = point
	while right - left > 0:
		middle = (right+left)//2
		if array[middle] != target:
			left = middle+1
		else:
			right = middle
	start = right
	
	# 3 step: find ending
	left = middle
	right = len(array)-1
	if array[right] == target:
		return [start, right]
	while right - left > 0:
		middle = (right+left)//2
		if array[middle] != target:
			right = middle-1
		else:
			left = middle
			right -= 1
	end = left
	
	return [start, end]
