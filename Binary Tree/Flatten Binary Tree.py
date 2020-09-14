'''
To flat binary tree into double linked list style from the most left to the most right.
As an example of flatting, Binary search tree must become into sorted linked list. 
'''


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    if root is None or (root.left is None and root.right is None):
        return root
    new_head = None
    new_head, _ = flattenBinaryTreeHelper(root, new_head, None)
    return new_head


def flattenBinaryTreeHelper(node, head, left_node):
    if node.left is not None:
        head, left_node = flattenBinaryTreeHelper(node.left, head, left_node)
    if head is None:
        head = node
    node.left = left_node
    if left_node is not None:
        left_node.right = node
    left_node = node
    if node.right is not None:
        head, left_node = flattenBinaryTreeHelper(node.right, head, left_node)

    return head, left_node


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes


root = BinaryTree(1).insert([2, 3, 4, 5, 6])
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)

# actual function is below--------
leftMostNode = flattenBinaryTree(root)
# --------------------------------

leftToRightToLeft = leftMostNode.leftToRightToLeft()
print(leftMostNode)
print(leftToRightToLeft)

expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]




