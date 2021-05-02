'''
Find out if given BT is height balanced (height if its left subtree is
the same or +-1 as heights of its right subtree).

The idea behind: just DFS and backtrack its depth of left and right subtrees
and check if every node is balanced. Once is not -> backtrack to the end with it.
'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time and O(h) Space
        
def heightBalancedBinaryTree(tree):
	_, _, flag = subtree_balance_check(tree, 0, True)
	return flag

def subtree_balance_check(node, current_depth, is_balanced):
	
	if is_balanced is False:
		return 0, 0, False
	
	if node is None:
		return current_depth-1, current_depth-1, True
		
	left, _, is_balanced = subtree_balance_check(node.left,
												current_depth+1,
												is_balanced)
	_, right, is_balanced = subtree_balance_check(node.right,
												 current_depth+1,
												 is_balanced)

	if is_balanced is True and abs(left - right) <= 1:
		return max(left, right), max(left, right), True

	return 0, 0, False

