def invertBinaryTree(tree):
    nodeInvert(tree)
	if tree.left is not None:
		invertBinaryTree(tree.left)
	if tree.right is not None:
		invertBinaryTree(tree.right)

def nodeInvert(tree):
	tree.left, tree.right = tree.right, tree.left
