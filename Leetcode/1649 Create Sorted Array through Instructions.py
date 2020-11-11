'''
Link: https://leetcode.com/problems/create-sorted-array-through-instructions

array = [4, 3, 2, 6, 5] 
print(createSortedArray(array))
'''
def createSortedArray(instructions):
    m = max(instructions)
    c = [0] * (m + 1)

    def update(x):
        while x <= m:
            c[x] += 1
            x += x & -x

    def get(x):
        res = 0
        while x > 0:
            res += c[x]
            x -= x & -x
        return res

    res = 0
    for i, a in enumerate(instructions):
        res += min(get(a - 1), i - get(a))
        update(a)
    return res % (10 ** 9 + 7)

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.count_left = 0
#         self.count_right = 0


# class BST:
#     def __init__(self, value):
#         self.root = TreeNode(value)
#
#     def insert(self, value):
#         numbers_to_the_left = 0
#         numbers_to_the_right = 0
#         node_to_insert = TreeNode(value)
#         node = self.root
#         while node is not None:
#             if node.value <= node_to_insert.value:
#                 node.count_right += 1
#                 numbers_to_the_right = max(numbers_to_the_right, node.count_right)
#                 if node.right is not None:
#                     node = node.right
#                 else:
#                     node.right = node_to_insert
#                     break
#             else:
#                 node.count_left += 1
#                 numbers_to_the_left = max(numbers_to_the_left, node.count_left)
#                 if node.left is not None:
#                     node = node.left
#                 else:
#                     node.left = node_to_insert
#                     break
#         return min(numbers_to_the_left, numbers_to_the_right)
# class BST:
#     def __init__(self, value):
#         self.root = TreeNode(value)
#
#     def insert(self, value):
#         numbers_to_the_left = 0
#         numbers_to_the_right = 0
#         node_to_insert = TreeNode(value)
#         node = self.root
#         isDuplicate = False
#         while node is not None:
#             if node.value == node_to_insert.value and isDuplicate is False:
#                 isDuplicate = True
#                 local_duplicate_result = min(numbers_to_the_left + node.count_left,
#                                              numbers_to_the_right + node.count_right)
#
#             if node.value <= node_to_insert.value:
#                 node.count_right += 1
#                 numbers_to_the_left += node.count_left + 1
#                 if node.right is not None:
#                     node = node.right
#                 else:
#                     node.right = node_to_insert
#                     break
#             else:
#                 node.count_left += 1
#                 numbers_to_the_right += node.count_right + 1
#                 if node.left is not None:
#                     node = node.left
#                 else:
#                     node.left = node_to_insert
#                     break
#
#         if isDuplicate:
#             return local_duplicate_result
#         else:
#             return min(numbers_to_the_left, numbers_to_the_right)
#
#
# def createSortedArray(instructions):
#     if len(instructions) <= 2:
#         return 0
#     total_cost = 0
#     for i, num in enumerate(instructions):
#         if i == 0:
#             bst = BST(num)
#             continue
#         total_cost += bst.insert(num)
#     return total_cost
