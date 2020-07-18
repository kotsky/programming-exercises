'''
Find all permutations.
'''

# Version 1. O(N!*N) TS
def getPermutations(array):
	permutations = []
    helper(array, 0, permutations)
	return permutations
	
def helper(array, pointer, permutations):
	if pointer == len(array)-1:
		permutations.append(array.copy())
	else:
		for i in range(pointer, len(array)):
			swap(array, i, pointer)
			helper(array, pointer+1, permutations)
			swap(array, i, pointer)
				
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
	return array

'''
# Version 2
def getPermutations(array):
	if len(array) < 1:
		return []
	
	answer=[[array[0]]]
	for index in range(1, len(array)):
		reference = answer
		answer = []
		for i in range(len(reference)):
			for j in range(len(reference[0])+1):
				temp = reference[i].copy()
				temp.insert(j, array[index])
				answer.append(temp)
	return answer
    
# Version 3
def getPermutations(array):
    permutations = []
    helper(array, [], permutations)
    return permutations

def helper(array, perm, permutations):
    if not len(array) and len(perm):
        permutations.append(perm)
    else:
        for num in array:
            new_array = array.copy()
            new_array.remove(num)
            new_perm = perm.copy()
            new_perm.append(num)
            helper(new_array, new_perm, permutations)
'''
