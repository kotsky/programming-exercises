'''
To calculate each branch sum of BST.
'''


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    res = []	# contains sums
	s = 0	# local sum
	branchSumsHelper(root, s, res)
	return res
	
def branchSumsHelper(node, s, res):

	s += node.value
	
	if node.left is None and node.right is None:
		res.append(s)
		
	if node.left is not None:
		branchSumsHelper(node.left, s, res)
	
	if node.right is not None:
		branchSumsHelper(node.right, s, res)
		
		
