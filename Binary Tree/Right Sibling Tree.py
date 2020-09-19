'''
Take a binary tree and link nodes to their right sibling on the same level.
  From            1
              /       \
             2          3
           /  \        /  \
          4    5       6   7             
         / \    \     /    / \
        8   9   10   11  12  13
                    /
                   14
                   
   To           1 -> Null
              /       
             2 ----->   3
           /           /  
          4--> 5 ----> 6-->7
         /      \     /    / 
        8-->9   10-->11  12-->13
                    /
                   14
'''

# We have 2 patterns: 1) if current node is left from its parent -> left.right = parent.right
                    # 2) if current node is right from its parent -> right.right = parent.sibling(right).left <- for that find sibling of your parent first
# Explore in DFS all the way down along left, and in a sequence 
# reasign node.right to new nodes.

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    linkSiblings(root, None, False)
    return root


def linkSiblings(node, parent, isLeftNode):
    if node is None:
        return
    left = node.left
    right = node.right
    linkSiblings(left, node, True)
    if isLeftNode:
        node.right = parent.right
    elif parent is None:
        node.right = None
    else:
        node.right = parent.right.left if parent.right is not None else None
    linkSiblings(right, node, False)










