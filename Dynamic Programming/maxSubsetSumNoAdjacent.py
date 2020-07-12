'''
To define the max sum of non-adjacent elements.
'''

# O(N) T / O(1) S
def maxSubsetSumNoAdjacent(array):
    
	if len(array) <= 0:
		return 0
	elif len(array) <= 1:
		return array[0]
	
	max_sum = [array[0], max(array[0], array[1])]
	for i in range(2, len(array)):
		max_sum = [max_sum[1], max(max_sum[1], max_sum[0] + array[i])]
		
	return max(max_sum)
  
  '''
  # O(N) TS
  def maxSubsetSumNoAdjacent(array):
    
	if len(array) <= 0:
		return 0
	elif len(array) <= 2:
		return max(array)

	third_sum = array[0] + array[2]
	max_sum = max(array[0], array[1], third_sum)
	sums = array[:]
	sums[:3] = [array[0], array[1], third_sum]
	
	for i in range(3, len(array)):
		local_sum = max(array[i] + sums[i-2], array[i] + sums[i-3])
		max_sum = max(local_sum, max_sum)
		sums[i] = local_sum
	return max_sum
'''
