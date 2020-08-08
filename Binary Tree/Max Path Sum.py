'''
Find max path sum in binary tree. Path can be created by nodes with onlu <= 2 connected nodes.
{"array": [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], "target": 45}
'''

# Create maxSum as sum, and maxPath to defind next possible maxSum,
# once you go above.

def maxPathSum(tree):
	output = maxPathSumHelper(tree, maxSum=float("-inf"), maxPath=0)
	return output[0] if tree is not None \
							else None


def maxPathSumHelper(node, maxSum, maxPath):
	if node is None:
		return maxSum, maxPath
	
	maxSum, left = maxPathSumHelper(node.left, maxSum, maxPath)
	maxSum, right = maxPathSumHelper(node.right, maxSum, maxPath)
	
	maxPath = max(max(left, right) + node.value, node.value)
	if (left >= 0 and right >= 0) or (left < 0 and right < 0):
		maxSum = max(node.value + left + right, maxSum)
	else:
		maxSum = max(node.value + max(left, right), maxSum)
	
	return maxSum, maxPath
