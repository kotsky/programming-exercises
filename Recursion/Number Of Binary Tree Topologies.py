'''
Return number of all possible BInary Trees, which you can create from input n positive integer.
Example:
  input = 3
  output = 5
  
 Take a note, that n = 0 or 1 will give 1 output result (as None node for 0 and 1 for 1 node).
 
The idea here is to check how many nodes "x" we can place from the left side of root node, and how many are left (n - 1 - x) for right side.
And then go through each subtree as new tree with its number of nodes (n - 1 - x).
Formula to solve: T(n) = TLeft(x) * TRight(n - 1 - x) where x: 0->(n-1). 
'''


# Version 3. O(n^2) T / S
# Iterrative way
def numberOfBinaryTreeTopologies(n):
	if n <= 1:
		return 1
	memo = [0] * (n + 1)
	memo[0:2] = [1, 1]
	for i in range(2, n+1):
		for x in range(i):
			memo[i] += memo[x] * memo[i-1-x]
	return memo[-1]

'''
# Version 1. O((n*(2n)!)/(n!(n+1)!)) T / O(n) S
# Pure recursion
# def numberOfBinaryTreeTopologies(n):
#     if n <= 1:
# 		return 1
# 	total_sum = 0
# 	for x in range(n):
# 		total_sum += numberOfBinaryTreeTopologies(x) * numberOfBinaryTreeTopologies(n-1-x)
# 	return total_sum
'''

'''
# Version 2. O(n^2) T / S
# Recursion with memorisation
# def numberOfBinaryTreeTopologies(n):
# 	memo = {}
# 	memo[0] = 1
# 	memo[1] = 1
# 	return numberOfBinaryTreeTopologiesHelper(n, memo)

# def numberOfBinaryTreeTopologiesHelper(n, memo):
#     if n in memo:
# 		return memo[n]
# 	total_sum = 0
# 	for x in range(n):
# 		total_sum += numberOfBinaryTreeTopologiesHelper(x, memo) * numberOfBinaryTreeTopologiesHelper(n-1-x, memo)
# 	memo[n] = total_sum
# 	return total_sum
'''
	
	




