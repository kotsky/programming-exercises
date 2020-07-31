'''
You are given a head of tree, and 2 nodes. Each node has property of child nodes. 
Find lowest common node for two given nodes in this tree.
'''

# Version 1. 
# Find path to each element. Like [E, B, A], where A is a head node, E is 1st node.
# Then compare those path as arrays, traversing from the end of arrays.

def getLowestCommonManager(topManager, reportOne, reportTwo):
    _, path1 = findPath(reportOne, topManager, [], False)
    _, path2 = findPath(reportTwo, topManager, [], False)
    pointer = 1
    while pointer < min(len(path1), len(path2)) + 1:
        if path1[-pointer] != path2[-pointer]:
            return path1[-pointer + 1]
        pointer += 1
    return path1[0] if len(path1) < len(path2) else path2[0]

def findPath(node_to_find, node, path, flag):
    if node == []:
        return flag, path
    if node.name == node_to_find.name:
        flag = True
    for child in node.directReports:
        if flag:
            break
        flag, path = findPath(node_to_find, child, path, flag)
    if flag:
        path.append(node)
    return flag, path
    
    
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
