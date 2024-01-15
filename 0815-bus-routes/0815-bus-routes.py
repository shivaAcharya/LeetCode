class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If source and target is same no need for bus
        if source == target: return 0
        
        routes_buses = defaultdict(set) # route -> bus
        
        Q = deque()
        target_buses = set()
        for bus, route in enumerate(routes):
            for rt in route:
                if rt == source:
                    Q.append((bus, 1))
                if rt == target:
                    target_buses.add(bus)
                routes_buses[rt].add(bus)
        
        # Build Graph
        G = defaultdict(set) # Undirected buses
        
        for bus, route in enumerate(routes):
            for rt in route:
                buses = routes_buses[rt]
                for b in buses:
                    G[bus].add(b)
                    G[b].add(bus)
                
        
        seen = set()
        while Q:
            bus, bus_count = Q.popleft()
            if bus in target_buses:
                return bus_count
            
            seen.add(bus)
            
            for nei in G[bus]:
                if nei not in seen:
                    Q.append((nei, bus_count + 1))
        
        return -1
                        