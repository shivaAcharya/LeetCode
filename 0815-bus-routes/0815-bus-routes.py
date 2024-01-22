"""
routes = [[1,2,7],[3,6,7]], source = 1, target = 6


bus_stops

0   =>  1 -> 2 -> 7
1   =>  3 -> 6 -> 7


stop_buses
1 -> 0
2 -> 1
7 -> 0, 1
3 -> 1
6 -> 1

visited_buses = {0}
Q = [(1, 0, 0)] # stop, bus, bus_count
    [(2, 1, 1), (7, 1, 1)]
    
    
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12

bus_stops = {
    0 -> (7, 12),
    1 -> (4, 5, 15),
    2 -> (6),
    3 -> (15, 19),
    4 -> (9, 12, 13),
}

stop_buses = {
    7 -> 0,
    12 -> 0,
    4 -> 1,
    5 -> 1,
    15 -> 1,3
    6 -> 2,
    19 -> 3,
    9 -> 4,
    13 -> 4,
}
buses_taken = {1}
Q = [(1, 1), (3, 1)] #bus, bus_count
    [(3, 2)]

"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # Edge case
        if source == target: return 0
        
        stop_buses = defaultdict(set)
        Q = deque() #(bus, bus_count)
        visited_buses = set()
        target_buses = set()
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop == source:
                    Q.append((bus, 1))
                if stop == target:
                    target_buses.add(bus)
                stop_buses[stop].add(bus)
        
        # Bus_buses connection
        bus_buses = defaultdict(set)
        
        for bus, stops in enumerate(routes):
            for stop in stops:
                buses = stop_buses[stop]
                for b in buses:
                    bus_buses[b].add(bus)
                    bus_buses[bus].add(b)
        
        while Q: #[(0, 1)]
            bus, bus_count = Q.popleft()
            if bus in target_buses:
                return bus_count
            
            # print(bus, bus_count)
            visited_buses.add(bus)
            
            for next_bus in bus_buses[bus]:          
                if next_bus not in visited_buses:
                    Q.append((next_bus, bus_count + 1))
    
        return -1        
        