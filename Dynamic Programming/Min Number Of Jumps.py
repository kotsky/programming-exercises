'''
Defind minimum number of jumps to reach the finale value in the array
input = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3], output = 4, where 
arr[0] = "3" tells how many steps in 1 jump we can do.
'''


# Version 1.
# O(N) T / O(1) S
# We try to defind the max possible reachable index 
# by going through each element. Then, when our steps 
# finished, we do max_reach - currentIdx to defind 
# how many steps we left

def minNumberOfJumps(array):
  if len(array) < 2:
  return 0
	
	currentIdx = 0
	jumps = 0
	max_reach = array[currentIdx]
	steps = max_reach
	
	while currentIdx < len(array)-1:	
		currentIdx += 1
		steps -= 1
		if currentIdx == len(array)-1:
			return jumps+1
		max_reach = max(max_reach, array[currentIdx] + currentIdx)
		if steps == 0:
			steps = max_reach - currentIdx
			jumps += 1
	return jumps+1
		
			
# Version 2
def minNumberOfJumps(array):
	if len(array) < 2:
		return 0
  matrix = [0] * len(array)
  matrix[-1] = 1

  for current_idx in range(len(array)-2, -1, -1):
      current_value = array[current_idx]

      if current_idx + current_value < len(array)-1:
          idx = current_idx
          current_idx += 1
          local_min = matrix[current_idx]
          while current_idx < len(array) and current_value > 0:
              local_min = min(local_min, matrix[current_idx])
              current_value -= 1
              current_idx += 1

          matrix[idx] = local_min+1
      else:
          matrix[current_idx] = 1

  return matrix[0]
