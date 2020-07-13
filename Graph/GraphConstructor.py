
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(v + e) T / O(v) S
    def depthFirstSearch(self, array):
		array.append(self.name)
		for name in self.children:
			name.depthFirstSearch(array)	
		return array
