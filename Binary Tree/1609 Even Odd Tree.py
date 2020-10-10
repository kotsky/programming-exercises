'''
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time / O(d) space, where n - number of nodes, and d - max deepth (level)
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return False
        return self.isEvenOddTreeHelper(root, [], 0)
    
    
    def isEvenOddTreeHelper(self, root, lastElementInLevel, currentLevel):
        if root is None:
            return True
        currentValue = root.val
        
        while len(lastElementInLevel) < currentLevel+1:
            lastElementInLevel.append(None)
                
        prevValue = lastElementInLevel[currentLevel]
        
        if currentLevel % 2 == 0:   # 0, 2, 4, ...
            if currentValue % 2 == 0:
                return False
            
            if prevValue is None:
                lastElementInLevel[currentLevel] = currentValue
            else:
                if prevValue >= currentValue:
                    return False
        else:
            if currentValue % 2 != 0:   # 1, 3, 5, ...
                return False

            if prevValue is None:
                lastElementInLevel[currentLevel] = currentValue
            else:
                if prevValue <= currentValue:
                    return False
            
        
        return self.isEvenOddTreeHelper(root.left, lastElementInLevel, currentLevel+1) and \
                    self.isEvenOddTreeHelper(root.right, lastElementInLevel, currentLevel+1)

        
