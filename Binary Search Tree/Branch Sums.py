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
    res = []
	s = 0
	func(root, s, res)
	return res
	
def func(node, s, res):

	s += node.value
	
	if node.left is None and node.right is None:
		res.append(s)
		
	if node.left is not None:
		func(node.left, s, res)
	
	if node.right is not None:
		func(node.right, s, res)
		
		
