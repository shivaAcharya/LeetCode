class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If source is target, no bus needed
        if source == target: return 0
        
        # Initialization
        routes_buses = defaultdict(set) # routes -> buses
        Q = deque() # (bus, bus_count)
        target_buses = set()
        
        # Build routes_buses
        for bus, route in enumerate(routes):
            for rt in route:
                if rt == source:
                    Q.append((bus, 1))
                if rt == target:
                    target_buses.add(bus)
                routes_buses[rt].add(bus)
                
        # Build undirected graph for buses
        G = defaultdict(set)
        for bus, route in enumerate(routes):
            for rt in route:
                buses = routes_buses[rt]
                for b in buses:
                    G[bus].add(b)
                    G[b].add(bus)
        
        # BFS
        seen = set() # To avoid cycle
        while Q:
            bus, bus_count = Q.popleft()
            
            if bus in target_buses:
                return bus_count
            
            seen.add(bus)
            for next_bus in G[bus]:
                if next_bus not in seen:
                    Q.append((next_bus, bus_count + 1))
        
        return -1
        