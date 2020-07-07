'''
Need to find the closest value to given target in the BST.
'''


def findClosestValueInBst(tree, target):
    # Write your code here.
	
	closest = tree.value
    return func(tree, target, closest)

def func(tree, target, closest):
	
	if tree is None:
		return closest
	
	if abs(tree.value - target) < abs(target - closest):
		closest = tree.value
	
	if tree.value == target:
		return closest
	elif tree.value < target:
		return func(tree.right, target, closest)
	else:
		return func(tree.left, target, closest)
	
