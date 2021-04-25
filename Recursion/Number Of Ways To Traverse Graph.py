'''
You have grid width x height.
Find out, how many ways you have from left up cell to down right cell,
if you can move only right or down.

Idea:

v1: Recursion + memorization
v2: Combinatorics - return all possible orders of right(R)/down(D) moves as
return (R + D)!/(R! * D!) based on width(R) and height(D)
'''

def numberOfWaysToTraverseGraph(width, height):
    info = {}
	initial_coort = get_token(1, 1)
	info[initial_coort] = 1
    return traverse_grid(width, height, info)

def get_token(x, y):
	return str(x) + ',' + str(y)

def traverse_grid(x, y, info):
	
	if x < 0 or y < 0:
		return 0
		
	coord = get_token(x, y)
	
	if coord in info:
		return info[coord]
	
    number_of_ways = traverse_grid(x - 1, y, info) + \
                     traverse_grid(x, y - 1, info)

	info[coord] = number_of_ways
	return number_of_ways
