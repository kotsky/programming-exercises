"""

Is the loop in the given graph? -> True/False

The idea: 
  Mark visiting node as GREy, and visited before from another start
  point as BLACK.

"""

WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph(edges):
    
	visited = [WHITE for x in edges]
	
	for node in range(len(edges)):
		if visited[node] == BLACK:
			continue
		
		if is_loop_from_start_node(node, edges, visited) is True:
			return True
	return False	
	
		
def is_loop_from_start_node(node, edges, visited):
	
	visited[node] = GREY
	
	for next_node in edges[node]:
		
		if visited[next_node] == GREY:
			return True
		
		if visited[next_node] == BLACK:
			continue
		
		if is_loop_from_start_node(next_node, edges, visited) is True:
			return True
	
	visited[node] = BLACK
	
	return False
		
	
	
	
	
	
	

