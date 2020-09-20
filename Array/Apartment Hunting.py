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




print(apartmentHunting(blocks, reqs))
