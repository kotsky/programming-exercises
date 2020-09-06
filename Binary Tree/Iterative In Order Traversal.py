
# O(N) T / O(1) S
# Iterate the binary tree witout recursion. But you have a parent property in the node.

class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

def iterativeInOrderTraversal(tree, callback):
    current = tree
    previous = None
    while current is not None:
        if previous is None or previous == current.parent:
            if current.left is None:
                callback(current)
                if current.right is not None:
                    nextNode = current.right
                else:
                    nextNode = current.parent
            else:
                nextNode = current.left
        elif previous == current.left:
            callback(current)
            if current.right is not None:
                nextNode = current.right
            else:
                nextNode = current.parent
        else:
            nextNode = current.parent
        previous = current
        current = nextNode




