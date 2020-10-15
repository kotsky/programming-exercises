'''
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. 
The road between 0 and 1 is only counted once.

Convert to graph problem. Calculate number of connection for each city. 
Find the max combination of 2 cities.
'''

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        infrusctraction = SpecialGraph(n, roads).infrusctraction
        return self.getMaxRankOfInfrusctraction(infrusctraction)
        
    def getMaxRankOfInfrusctraction(self, infrusctraction):
        max_rank = -1
        for city1 in list(infrusctraction.keys()):
            for city2 in list(infrusctraction.keys()):
                if city1 == city2:
                    continue
                if city2 in infrusctraction[city1].connections:
                    adjust = -1
                else:
                    adjust = 0
                max_rank = max(max_rank, infrusctraction[city1].rank + infrusctraction[city2].rank + adjust)
        return max_rank
        
        
class SpecialGraphNode:
    def __init__(self, city):
        self.city = city
        self.connections = {}
        self.rank = 0
        
        
class SpecialGraph:
    def __init__(self, number_of_cities, roads):
        self.infrusctraction = self.buildInfrustraction(number_of_cities, roads)
        
    def buildInfrustraction(self, number_of_cities, roads):
        infrusctraction = {}
        for x in range(number_of_cities):
            infrusctraction[x] = SpecialGraphNode(x)
        for road in roads:
            city1, city2 = road[0], road[1]
            infrusctraction[city1].connections[city2] = True
            infrusctraction[city2].connections[city1] = True
            infrusctraction[city1].rank += 1
            infrusctraction[city2].rank += 1
        return infrusctraction
