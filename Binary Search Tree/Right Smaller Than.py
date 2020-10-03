'''
You are given array of integers.
Return an array of the same size, where on each idx there is an quantity of numbers, which are smaller than array[idx] from its right side.
array = [8, 5, 11, -1, 3, 4, 2]
expected = [5, 4, 4, 0, 1, 1, 0]


It's easy to do by double "for" loop, which will gives time complexity O(n^2).
To optimize it, we might use BST property to achieve in average O(n*log(n)) time.
Build the BST from the end of array and at each node count its size of left subtree, which
you can use to calculate total counts of others nodes, which will go by the right side.

To handle duplicates, use self.counts[idx] += node.left_count + (1 if nodeToInsert.value > node.value else 0) formula,
because we can calculate numbers, which where before first duplicate, but not its duplicate as an additional number.

'''

def rightSmallerThan(array):
    if not len(array):
        return []
    bst = SpecialBST(array)
    return bst.counts


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left_count = 0
        self.left = None
        self.right = None


class SpecialBST:
    def __init__(self, array):
        self.root = None
        self.counts = [0] * len(array)
        self.buildSpecialBST(array)

    def buildSpecialBST(self, array):
        if self.root is None:
            self.root = BSTNode(array[-1])
        for idx in reversed(range(0, len(array) - 1)):
            nodeToInsert = BSTNode(array[idx])
            node = self.root
            while node is not None:
                if nodeToInsert.value >= node.value:
                    self.counts[idx] += node.left_count + (1 if nodeToInsert.value > node.value else 0)
                    if node.right is None:
                        node.right = nodeToInsert
                        break
                    node = node.right
                else:
                    node.left_count += 1
                    if node.left is None:
                        node.left = nodeToInsert
                        break
                    node = node.left
