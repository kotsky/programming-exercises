'''
To calculate how many rectangles we can have from those coords:
coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
Take a note, that rectangles lines have to be parallel to X or Y axis.
'''

# Version 1. To define if we have other 2 dots (left_top + right_bot) by diagonal.
# O(n^2) T / o(n) S

def rectangleMania(coords):
    search_table = convert_to_hash_table(coords)
    search_table['count'] = 0
    for coord_one in coords:
        for coord_two in coords:
            if coord_two == coord_one:
                continue
            rectangle_check(coord_one, coord_two, search_table)
    return search_table['count']


def rectangle_check(p1, p2, table):
    if p1[0] >= p2[0] or p1[1] >= p2[1]:
        return

    p3 = [p1[0], p2[1]]
    p4 = [p2[0], p1[1]]
    key_p3 = get_key_from_coord(p3)
    key_p4 = get_key_from_coord(p4)
    if key_p4 in table and key_p3 in table:
        table['count'] += 1


def convert_to_hash_table(coords):
    table = {}
    for coord in coords:
        key = get_key_from_coord(coord)
        if key not in table:
            table[key] = True
    return table


def get_key_from_coord(coord):
    x, y = coord
    return str(x) + ',' + str(y)
    
    
    
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
