'''
Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at time t.
3. getAverageTime(string startStation, string endStation) 

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. 
That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
'''

  # All methods are O(1) Time
  # Total class memory is up to O(S^2 + ID), where
  # S - number of stations, 
  # and ID - number of customers who are in the 
  # underground system (didn't check out)
class UndergroundSystem:

    def __init__(self):
        self.avg_track_from_particular_stations = {}
        self.customer_track = {}

    def checkIn(self, customer_id, stationName, timeIn):
        if customer_id not in self.customer_track:
            self.customer_track[customer_id] = ['', -1]
        self.customer_track[customer_id] = [stationName, timeIn]

    def checkOut(self, customer_id, stationName, timeOut):
        if stationName not in self.avg_track_from_particular_stations:
            self.avg_track_from_particular_stations[stationName] = {}
        current_station_node = self.avg_track_from_particular_stations[stationName]
        
        startStation, timeIn = self.customer_track.pop(customer_id)
        
        if startStation not in current_station_node:
            current_station_node[startStation] = [timeOut - timeIn, 1]
        else:
            total_time, customers = current_station_node[startStation] 
            current_station_node[startStation] = [total_time + (timeOut - timeIn), customers + 1]
        
        #del self.customer_track[customer_id]

    def getAverageTime(self, startStation, endStation):     # float output
        total_time, customers = self.avg_track_from_particular_stations[endStation][startStation]
        return total_time/customers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
