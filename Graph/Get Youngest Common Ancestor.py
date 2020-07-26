'''
To define the youngest common root node for two given nodes.
At first we compare their deepth. Shift up to the same root level.
Then, we compare their root nodes every time we go up.
'''

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d_one = descendantOne
    d_two = descendantTwo
    deepth1 = 0
    deepth2 = 0

    while d_one is not None:
        deepth1 += 1
        d_one = d_one.ancestor
    while d_two is not None:
        deepth2 += 1
        d_two = d_two.ancestor

    if deepth2 <= deepth1:
        deepest = descendantOne
        short = descendantTwo
        difference = deepth1 - deepth2
    else:
        deepest = descendantTwo
        short = descendantOne
        difference = deepth2 - deepth1

    while difference:
        deepest = deepest.ancestor
        difference -= 1
    while short.name != topAncestor.name:
        if short.name == deepest.name:
            break
        else:
            short = short.ancestor
            deepest = deepest.ancestor
    return short
    
'''
# Version 2
# With using additional arrays to save pass of each node to the root,
# and then to compare thise arrays.

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d_one = descendantOne
    d_two = descendantTwo
    d_one_way = []
    d_two_way = []
    while d_one is not None:
        d_one_way.append(d_one)
        d_one = d_one.ancestor
    while d_two is not None:
        d_two_way.append(d_two)
        d_two = d_two.ancestor

    ancestor = None
    while len(d_two_way) and len(d_one_way):
        d_one = d_one_way.pop()
        d_two = d_two_way.pop()
        if d_one.name == d_two.name:
            ancestor = d_one
        else:
            break
    return ancestor
	'''
