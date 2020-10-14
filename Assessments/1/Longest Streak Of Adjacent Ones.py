# Pass

# Version 2
def longestStreakOfAdjacentOnes(array):
  longest_streak = 0
	main_zero_replace = -1
	current_streak = 0
	current_zero_replace = -1
	
	for i in range(len(array)):
		if array[i] == 1:
			current_streak += 1
		else:
			current_streak = i - current_zero_replace
			current_zero_replace = i
			
		if current_streak > longest_streak:
			longest_streak = current_streak
			main_zero_replace = current_zero_replace

	return main_zero_replace
  
  
# Version 1
'''
def longestStreakOfAdjacentOnes(array):
	zero_idx = -1
	start = 0
	end = 0
	global_zero_idx = -1
	max_length = -1
	
	for i in range(len(array)):
		if array[i] == 1:
			end = i
		else:
			start = zero_idx + 1
			zero_idx = i
			end += 1
		max_length, global_zero_idx= updateParameters(start, end, global_zero_idx, zero_idx, max_length)
	
	return global_zero_idx
			
			
def updateParameters(start, end, global_zero_idx, zero_idx, max_length):
	if end - start > max_length:
		max_length = end - start
		global_zero_idx = zero_idx
	return max_length, global_zero_idx		
	
	
'''
