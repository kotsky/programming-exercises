'''
Find all possible paths to reach the given end node from start node.

The idea: recursively with DFS explore every possible path.

vertices = [1, 2, 3, 4, 5, 6]
edges = [[2, 1], [4, 2], [3, 2], [3, 4], [4, 5], [5, 1], [3, 1], [5, 4], [2, 3], [3, 6], [4, 6], [6, 2], [6, 1]]
graph = Graph(vertices, edges)
all_paths = get_all_paths(graph, 1, 3)
print(all_paths)
'''

import graph from py-libs/data_structures

def get_all_paths(graph, start_node_value, end_node_value):
    start_node = graph.get_node(start_node_value)
    end_node = graph.get_node(end_node_value)
    current_path = [start_node.value]
    return get_all_paths_helper(start_node, end_node, current_path, [])


def get_all_paths_helper(start_node, end_node, current_path, paths):
    if start_node == end_node:
        paths.append(current_path.copy())
        return paths
    if start_node.visited:
        return paths
    start_node.visited = True
    for child in start_node.dependencies:
        current_path.append(child.value)
        paths = get_all_paths_helper(child, end_node, current_path, paths)
        current_path.pop()
    start_node.visited = False
    return paths
