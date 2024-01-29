"""
route_bus = {
    1 : 0,
    2 : 0,
    7 : 0, 1,
    3 : 1,
    6 : 1,
}

bus_buses = {
    0 : 1,
    1 : 0,
}

Q = (source, bus_num, bus_count) # (1, 0, 1)


route_bus = {
    7 : 0, 4
   12 : 0,
    4 : 1,
    5 : 1,
   15 : 1,
    6 : 2,
   15 : 3,
   19 : 3,
    9 : 4,
   13 : 4,
}


"""
from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        
        Q = deque() #(bus_num, bus_count)
        target_buses = set()
        route_bus = defaultdict(set)
        
        for bus, route in enumerate(routes):
            for rt in route:
                route_bus[rt].add(bus)
                if rt == source:
                    Q.append((bus, 1))
                if rt == target:
                    target_buses.add(bus)
        
        bus_buses = defaultdict(set)
        
        for bus, route in enumerate(routes):
            for rt in route:
                for b in route_bus[rt]:
                    bus_buses[b].add(bus)
                    bus_buses[bus].add(b)
        # print(Q)
        visited_bus = set()
        while Q:
            bus, bus_count = Q.popleft()
            
            if bus in target_buses:
                return bus_count
            
            visited_bus.add(bus)
            
            for nxt_bus in bus_buses[bus]:
                if nxt_bus not in visited_bus:
                    Q.append((nxt_bus, bus_count + 1))
                    
        return -1
                        
            
        