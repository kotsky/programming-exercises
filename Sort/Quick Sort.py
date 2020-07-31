# Quick sort algo to sort an array. 
# Noted in notebook.

def quickSort(array):
	sortHelper(array, 0, len(array)-1)
    return array

def swap(array, idx1, idx2):
	array[idx1], array[idx2] = array[idx2], array[idx1]

def sortHelper(array, start_idx, end_idx):
	if end_idx <= start_idx:
		return 
    
	pivot = start_idx
	start_idx += 1
	list_range = [pivot, end_idx]
	
	while end_idx >= start_idx:
		if array[start_idx] > array[pivot] and array[end_idx] < array[pivot]:
			swap(array, start_idx, end_idx)
		if array[start_idx] <= array[pivot]:
			start_idx += 1
		if array[end_idx] >= array[pivot]:
			end_idx -= 1
	
	swap(array, pivot, end_idx)
  
  # for space complexity optimisation, bcos of recursion
	left_sub_isSmaller = list_range[0] - end_idx < end_idx+1, list_range[1] 
	
	if left_sub_isSmaller:
		sortHelper(array, list_range[0], end_idx)
		sortHelper(array, end_idx+1, list_range[1])
	else:
		sortHelper(array, end_idx+1, list_range[1])
		sortHelper(array, list_range[0], end_idx)
		

	
		
