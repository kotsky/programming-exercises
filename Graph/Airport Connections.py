'''
Write a function that returns the minimum number of airport connections (one-way flights) 
that need to be added in order for someone to be able to reach any airport in the list, 
starting at the starting airport.

Note that routes only allow you to fly in one direction => ["1", "2"] means 1 -> 2
'''

'''
Version 1:
The idea behind is 1) to define, which airports are unreacable from the start airport and 
2) to create routes from the start airport to unvisited airports (we say: let's we have route 
from the start airport to particular one -> add this particular airport to new_routes) and explore (DFS method),
where you can go from that particular airport:
we go out from the exploring when:
  1* if we meet the airport (airport B), which is in route -> we say that we don't need that route (which we just met)
  because we can come to that airport B from the airport A (reference airport -> look into visitAirportWithNewRoute())
  Take a note: we cannot overwride Airport A to False 
  if we come there in this inner loop => condition airport_node.airport_name != reference.
  2* if we meet visited airport
  3* all connections are finished

3) calculate from new_routes, how many routes were needed (by their property "True").

Easy.

Version 2:
Less optimal from the time complexity point of view.
The idea is to assign "value" to each unreached (unvisited) airport, which shows how many airports can be reached 
from that particular start airport. Then, sort these unreaced airports by their .value from max to min.
And Count how many new routes you need to go visit all airports.
'''

# Version 1.
# O(a + r) Time / O(a + r) Space, where a - airports, r - routes
def airportConnections(airports, routes, startingAirport):
    airport_connections = AirportsConnections(airports, routes, startingAirport)  # O(a + r) Time / O(a + r) Space
    visitAirports(airport_connections.start_airport)  # O(a + r) Time / O(a) Space
    return getMinNumbersOfNewRoutes(airport_connections, airports)


def getMinNumbersOfNewRoutes(airport_connections, airports):
    new_routes = {}
    
    # total # O(a + r) Time / O(a + r) Space
    # it's that time complexity because some nodes will be denied 
    # by its flag .visited.
    # Roughly, we will go throught each airport 2-3 times.
    for airport in airports:
        airport_node = airport_connections.airport_connections[airport]
        if airport_node.visited:
            continue
        if airport_node not in new_routes:
            visitAirportWithNewRoute(airport_node, new_routes, True, airport)
    return getNewRoutesCount(new_routes)

# O(a) Time / O(1) Space
def getNewRoutesCount(routes):
    count = 0
    for airport in routes.keys():
        if routes[airport]:
            count += 1
    return count

# O(a + r) Time / O(a + r) Space
def visitAirportWithNewRoute(airport_node, new_routes, visitingFromStartAirport, reference):
# reference - is the airport, on which we came from the start airport
# we need track it beacuse in case we return back to this airport -> to not overwrite its 
# route in new_routes. Otherwise, we would "delete" route and an answer would be wrong.
    if airport_node.airport_name in new_routes and airport_node.airport_name != reference:
        new_routes[airport_node.airport_name] = False
    if airport_node.visited:
        return

    if visitingFromStartAirport:
        new_routes[airport_node.airport_name] = True
    airport_node.visited = True
    for next_destination in airport_node.destination:
        visitAirportWithNewRoute(next_destination, new_routes, False, reference)

    # visit airports if you fly out from start_airport
    # O(a + r) Time / O(a) Space
def visitAirports(start_airport):
    if start_airport.visited:
        return
    start_airport.visited = True
    for next_destination in start_airport.destination:
        visitAirports(next_destination)


class AirportsConnections:
    def __init__(self, airports, routes, startingAirport):
        self.airport_connections = self.buildAirportsConnections(airports, routes)
        self.start_airport = self.getStartAirport(startingAirport)

    # O(a + r) Time / Space
    # build its class of airport's connections
    def buildAirportsConnections(self, airports, routes):
        airport_connections = {}
        for airport in airports:
            if airport not in airport_connections:
                airport_connections[airport] = AirportNode(airport)
        for route in routes:
            departure_airport = route[0]
            arival_airport = route[1]
            if departure_airport in airport_connections:
                arival_airport_node = airport_connections[arival_airport]
                airport_connections[departure_airport].destination.append(arival_airport_node)
        return airport_connections

    def getStartAirport(self, startingAirport):
        self.start_airport = self.airport_connections[startingAirport]
        return self.start_airport


class AirportNode:
    def __init__(self, airport):
        self.airport_name = airport
        self.destination = []
        self.visited = False




AIRPORTS = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

STARTING_AIRPORT = "LGA"

routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "SIN"],
            ["CDG", "BUD"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["TLV", "DEL"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["HND", "JFK"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]

print(airportConnections(AIRPORTS, routes, STARTING_AIRPORT))


'''
# Version 2.
# O(a * (a + r) + (a + r) + a * log(a)) Time / O(a + r) Space
def airportConnections(airports, routes, startingAirport):
    airport_connections = SpecialGraphAirportConnections(airports, routes, startingAirport)
    airport_connections.markUnreachableAirports(airport_connections.starting_airport)
    list_of_unreachable_airports = assignValueToUnreachableAirports(airport_connections)
    list_of_unreachable_airports.sort(key=lambda x: -x.value)
    return countNewRoutes(list_of_unreachable_airports, airport_connections)


def countNewRoutes(airport_nodes, airport_connections):
    number_of_new_routes = 0
    # output_list = []
    for airport_node in airport_nodes:
        if airport_node.reachable:
            continue
        number_of_new_routes += 1
        # output_list.append(airport_node.airport_name)
        airport_connections.markUnreachableAirports(airport_node)
        airport_node.reachable = False
    return number_of_new_routes     # , output_list


def assignValueToUnreachableAirports(airport_connections):
    airport_connections = airport_connections.airport_connections
    list_of_unreachable_airports = []
    for airport in airport_connections.keys():
        airport_node = airport_connections[airport]
        if airport_node.reachable:
            continue
        assignValueToAirport(airport_node, airport_node, True)
        list_of_unreachable_airports.append(airport_node)
    return list_of_unreachable_airports


def assignValueToAirport(airport_node, start_airport_node, reference):
    if not reference and airport_node == start_airport_node:  # mark initial start point as a reserence 
        return -1                                             # to avoid wrong assigment in inner loops

    if airport_node.reachable:
        return 0

    airport_node.reachable = True # mark it to avoid infinite loop

    local_value = 0
    for next_airport in airport_node.routesTo:
        local_value += assignValueToAirport(next_airport, start_airport_node, False) + 1

    if reference:
        start_airport_node.value = local_value

    airport_node.reachable = False  # unmark for further processing to build new routes

    return local_value


class AirportConnectionNode:
    def __init__(self, airport):
        self.airport_name = airport
        self.routesTo = []
        self.reachable = False
        self.value = None


class SpecialGraphAirportConnections:
    def __init__(self, airports, routes, startingAirport):
        self.airport_connections = self.buildAirportConnections(airports, routes)
        self.starting_airport = self.airport_connections[startingAirport]

    def buildAirportConnections(self, airports, routes):
        airport_connections = {}
        for airport in airports:
            if airport not in airport_connections:
                airport_connections[airport] = AirportConnectionNode(airport)
        for route in routes:
            start_airport, end_airport = route[0], route[1]
            if start_airport not in airport_connections:
                airport_connections[start_airport] = AirportConnectionNode(start_airport)
            if end_airport not in airport_connections:
                airport_connections[end_airport] = AirportConnectionNode(end_airport)
            airport_connections[start_airport].routesTo.append(airport_connections[end_airport])
        return airport_connections

    def markUnreachableAirports(self, start_node):
        if start_node.reachable:
            return
        start_node.reachable = True
        start_node.value = 0
        for next_airport in start_node.routesTo:
            self.markUnreachableAirports(next_airport)
'''
