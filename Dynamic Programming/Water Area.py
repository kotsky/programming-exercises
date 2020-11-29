'''
https://www.algoexpert.io/questions/Water%20Area
You have array of height pillars. There is poured water. Calculate water volume.
Assume, that width of the element is 1.

Input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]) 
Output: 48
'''


# Version 1 
# O(N) TS

def waterArea(heights):
	if len(heights) < 2:
		return 0
	
    	leftPointer = 0
	rightPoiner = len(heights) - 1
	area = 0
	rightMax = heights[rightPoiner]
	leftMax = heights[leftPointer]
	
	while leftPointer < rightPoiner:
		if leftMax < rightMax:
			leftPointer += 1
			leftMax = max(leftMax, heights[leftPointer])
			area += leftMax - heights[leftPointer]
		else:
			rightPoiner -= 1
			rightMax = max(rightMax, heights[rightPoiner])
			area += rightMax - heights[rightPoiner]
	return area


'''
# Version 2. Own
# O(N) - avg, O(N^2) - worst T / O(1) S

def waterArea(heights):
    startIdx = 0
    endIdx = 0
    area = 0

    while startIdx < len(heights):
        startIdx = endIdx
        maxIdx = -1
        local_max = -1
        endIdx += 1
        while endIdx < len(heights):
            if heights[endIdx] >= heights[startIdx]:
                area += waterCalculation(heights, startIdx, endIdx)
                break
            if heights[endIdx] >= local_max:
                local_max = heights[endIdx]
                maxIdx = endIdx
            if endIdx == len(heights) - 1:
                area += waterCalculation(heights, startIdx, maxIdx)
                endIdx = maxIdx
				        break
            endIdx += 1
    return area

			
def waterCalculation(array, startIdx, endIdx):
	area = min(array[startIdx], array[endIdx]) * (endIdx - startIdx - 1) - sum(array[startIdx+1:endIdx])
	return area if area > 0 else 0
  
'''
