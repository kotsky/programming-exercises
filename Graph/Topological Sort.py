'''
You are given jobs to be completed as [1, 2, 3, 4], where each number represent #job.
You also have dependencies as deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]],
where [1, 2] means job#2 can be done only after job#1 is completed : 1 -> 2
'''
# Graph problem with DFS

# Version 2. With using graphs. 
# O(j + d) TS

def topologicalSort(jobs, deps):

    jobGraph = createGraph(jobs, deps)

    visited = {}
    visiting = {}
    sequence = []
    flag = True

    nodes = jobGraph.nodes

    while len(nodes) > 0:
        if flag is False:
            return []
        flag = deepFirstSearch(nodes.pop(), visited, visiting, sequence, flag)
    return sequence


def deepFirstSearch(root, visited, visiting, sequence, flag):
    if root in visited:
        return True
	
    if root not in visiting:
        visiting[root] = True
    else:
        return False
	
    for dep in root.dependencies:
        flag = deepFirstSearch(dep, visited, visiting, sequence, flag)
		if flag is False:
            return False
		
    sequence.append(root.value)
    visited[root] = True
    return flag


def createGraph(values, deps):
    graph = Graph(values)
    for dep, value in deps:
        graph.addDep(value, dep)
    return graph


class Graph:
    def __init__(self, values):
        self.nodes = []
        self.graph = {}
        for value in values:
            self.addNode(value)

    def addNode(self, value):
        self.graph[value] = GraphNode(value)
        self.nodes.append(self.graph[value])

    def getNode(self, value):
        if value not in self.graph:
            self.addNode(value)
        return self.graph[value]

    def addDep(self, value, dep):
        valueNode = self.getNode(value)
        depNode = self.getNode(dep)
        valueNode.dependencies.append(depNode)


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.dependencies = []
        
        
        
'''
# Version 1. 
# O(jobs*deps) T / O(jobs + deps) S

def topologicalSort(jobs, deps):
    visited = {}
    visiting = {}
    sequence = []
    flag = True

    for job in jobs:
        if flag is False:
            return []
        flag = deepFirstSearch(job, deps, visited, sequence, flag, visiting)

    return list(reversed(sequence))


def deepFirstSearch(root, deps, visited, sequence, flag, visiting):
    if root in visited or flag is False:
        return flag

    if root not in visiting:
        visiting[root] = True
    else:
        flag = False
        return flag

    for dep in deps:
        if flag is False:
            break
        if dep[0] == root or dep[1] in visited:
            flag = deepFirstSearch(dep[1], deps, visited, sequence, flag, visiting)
    if flag:
        sequence.append(root)
        visited[root] = True

    return flag
'''
