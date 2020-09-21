'''
Blocks contains areas. Find the best place to live
by optimisation the distance to the farsest building (from the reqs) 
from your living area.

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

Answer = 3
'''

# Version 2. O(b * r) Time & O(1) space / if we can change the given input array


def apartmentHunting(blocks, reqs):
    updateDistancesFromBlocks(blocks, reqs)
	return getBlockWithMinDistance(blocks, reqs)


def updateDistancesFromBlocks(blocks, reqs):
	for req in reqs:
		last_seen_req_at_idx = -1
		for i in range(len(blocks)):
			if blocks[i][req]:
				blocks[i][req] = 0
				last_seen_req_at_idx = i
				continue
			if last_seen_req_at_idx == -1:
				blocks[i][req] = float("inf")
			else:
				blocks[i][req] = i - last_seen_req_at_idx
		last_seen_req_at_idx = -1
		for i in reversed(range(len(blocks))):
			if blocks[i][req] == 0:
				last_seen_req_at_idx = i
				continue
			if last_seen_req_at_idx != -1:
				blocks[i][req] = min(blocks[i][req], last_seen_req_at_idx - i)
		
		
def getBlockWithMinDistance(blocks, reqs):
	min_distance = float("inf")
	block_with_min_distance = -1
	for i in range(len(blocks)):
		block = blocks[i]
		block_min_distance = float("-inf")
		for req in reqs:
			block_min_distance = max(block_min_distance, block[req])
		if block_min_distance < min_distance:
			min_distance = block_min_distance
			block_with_min_distance = i
	return block_with_min_distance


'''
# Version 1. O(b * r) Time & O(b * r) space

def apartmentHunting(blocks, reqs):
    apartmentTable = {}
    for req in reqs:
        for i in range(2):  # in 2 direction -> and <-
            requirementUpdate(blocks, apartmentTable, req, i)
    return minDistance(blocks, apartmentTable, reqs)


def minDistance(blocks, apartmentTable, reqs):
    min_sum_distance = float('inf')
    min_sum_distance_idx = -1
    for i in range(len(blocks)):
        block_from_table = apartmentTable[i]
        sum_distance = 0
        for req in reqs:
            sum_distance = max(sum_distance, block_from_table[req])
        if sum_distance < min_sum_distance:
            min_sum_distance = sum_distance
            min_sum_distance_idx = i
    return min_sum_distance_idx


def requirementUpdate(blocks, apartmentTable, req, direction):
    if direction == 0:
        req_current_idx = -1
        for i in range(len(blocks)):
            if i not in apartmentTable:
                apartmentTable[i] = {}
            apartmentTable[i][req] = float('inf')
            block = blocks[i]
            if block[req] is True:
                req_current_idx = i
            if req_current_idx != -1:
                apartmentTable[i][req] = i - req_current_idx
    else:
        req_current_idx = -1
        for i in range(len(blocks) - 1, -1, -1):
            block = blocks[i]
            if block[req] is True:
                req_current_idx = i
            if req_current_idx != -1:
                apartmentTable[i][req] = min(apartmentTable[i][req], req_current_idx - i)

'''


print(apartmentHunting(blocks, reqs))
