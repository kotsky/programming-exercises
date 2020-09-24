'''
Define all sums (as a total sum) of each root node based on its depth. 
                               1            # sum at root node 16
                            /    \
                           2      3         # sum at 2: 6; sum at 3: 2
                          / \    / \
                         4   5  6   7       # sum at 4: 2
                        / \
                       8   9                # total sum = 26                    
'''

# Version 2. Shorter style
# O(n) T / O(d) S
# The idea is to find out the formula of depth dependance on each root node.
# More descriptive info under Version 1.

def allKindsOfNodeDepths(root, depth=0):
	if root is None:
		return 0
	
  # Formula to calculate 1 + 2 + 3 + ... + depth - 1 + depth
	depth_sum = depth * (1 + depth) / 2
	return depth_sum + allKindsOfNodeDepths(root.left, depth + 1) + allKindsOfNodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
# Version 2. First try
# O(n) T / O(d) S
# 2 steps:
# 1: to find out how many node are on each level (depth)
# and write them down into its array, where each index 
# represents its depth.
# 2: to calculate the total sum as the following:
# total_sum += numbersPerDepth[d]*(d + prev_d) # (d + prev_d) -> is 
# depth_sum = depth * (1 + depth) / 2 from above as total_sum += numbersPerDepth[d]*(d * (1 + d)/2)

def allKindsOfNodeDepths(root):
        if root is None or (root.left is None and root.right is None):
            return 0
        numbersPerDepth = []
        countNumbersPerDepth(root, numbersPerDepth, -1)
        return getTotalSum(numbersPerDepth)


def getTotalSum(numbersPerDepth):
        total_sum = 0
        prev_d = 0
        for d in range(len(numbersPerDepth)):
            total_sum += numbersPerDepth[d]*(d + prev_d)
            prev_d = d + prev_d
        return total_sum


def countNumbersPerDepth(node, numbersPerDepth, depth):
        depth += 1
        if not len(numbersPerDepth) or depth >= len(numbersPerDepth):
            numbersPerDepth.append(0)
        numbersPerDepth[depth] += 1
        if node.left is not None:
            countNumbersPerDepth(node.left, numbersPerDepth, depth)
        if node.right is not None:
            countNumbersPerDepth(node.right, numbersPerDepth, depth)
'''


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
print(allKindsOfNodeDepths(root))
