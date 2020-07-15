'''
Sum up all depths of given tree.
'''

def nodeDepths(root, depth=0):
    if root is None:
		return 0
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

'''
# Version 2
def nodeDepths(root):
	factor = 0
	return nodeWay(root, -1, 0)

def nodeWay(root, factor, total_depth):
	factor += 1
	if root.left is not None:
		total_depth = nodeWay(root.left, factor, total_depth)
		
	if root.right is not None:
		total_depth = nodeWay(root.right, factor, total_depth)
	
	total_depth += factor
	return total_depth

'''
