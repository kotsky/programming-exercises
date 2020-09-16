'''
To calculate how many rectangles we can have from those coords:
coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
Take a note, that rectangles lines have to be parallel to X or Y axis.
'''

# Version 1. To define if we have other 2 dots (left_top + right_bot) by diagonal.
# O(n^2) T / o(n) S

def rectangleMania(coords):
    table = coordToHashTable(coords)
    rectangles = 0
    for i in range(len(coords)):
        left_top = coords[i]
        for j in range(len(coords)):
            if j == i:
                continue
            right_bot = coords[j]
            if checkRectangle(left_top, right_bot, table):
                rectangles += 1
    return rectangles


def checkRectangle(p1, p3, table):
    if p1[0] >= p3[0] or p1[1] <= p3[1]:
        return False
    p2 = [p3[0], p1[1]]
    p4 = [p1[0], p3[1]]
    if coordToKey(p2) in table and coordToKey(p4) in table:
        return True
    else:
        return False


def coordToHashTable(coords):
    table = {}
    for coord in coords:
        table[coordToKey(coord)] = coord
    return table


def coordToKey(coord):
    return str(coord[0]) + ',' + str(coord[1])
    
    
    
'''
# Version 2. Pure graph problem

def rectangleMania(coords):
    if len(coords) < 4:
        return 0
    graphs = convertToGraphs(coords)
    linkGraphs(graphs)
    count = 0
    visited = {}
    for graph in graphs:
        count = exploreGraph(graph, 'x', count, 0, visited, None)
    return count


def exploreGraph(graph, direction, count, depth, visited, start_point):
    if graph in visited:
        return count
    if depth == 0:
        start_point = graph
        visited[graph] = True
    depth += 1
    to_explore = graph.byX if direction == 'x' else graph.byY
    direction = 'y' if direction == 'x' else 'x'
    if depth == 4:
        if start_point in to_explore:
            count += 1
        return count
    for edge in to_explore:
        count = exploreGraph(edge, direction, count, depth, visited, start_point)
    return count


class Node:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.byX = []
        self.byY = []


# O(n) TS
def convertToGraphs(coords):
    graphs = []
    for coord in coords:
        graphs.append(Node(coord))
    return graphs


# O(n^2) TS
def linkGraphs(graphs):
    for i in range(len(graphs)):
        graph = graphs[i]
        for j in range(len(graphs)):
            next_graph = graphs[j]
            if j == i or (graph.x == next_graph.x and graph.y == next_graph.y):
                continue
            if graph.x == next_graph.x:
                graph.byY.append(next_graph)
            if graph.y == next_graph.y:
                graph.byX.append(next_graph)


'''
