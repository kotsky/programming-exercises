''' Find Next Node In-Order Traversal

You have the node with .parent. Find its next node,
which will follow given node if you do in-order traversal.

The idea:
  In-order => left_node->node->right_node - use this property.
  1. If there is a right node => find there the most left child
  and it is your solution.
  2. Else, your next node if somewhere in parent nodes above.
  Go there until you find that you come to the parent node from
  the left branch -> this parent is your solution.

'''



class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	
	if node.right is not None:
		return get_left_most_child(node.right)
	else:
		return get_right_most_parent(node)
				
	return None


def get_left_most_child(node):
	while node.left is not None:
		node = node.left
	return node


def get_right_most_parent(node):
	while node.parent is not None:
		prev_node = node
		node = node.parent

		if node.left == prev_node:
			return node
	return None
			
