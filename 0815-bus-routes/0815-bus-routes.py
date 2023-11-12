class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If source and target is same no need for bus
        if source == target: return 0
        
        routes_buses = defaultdict(set) # route -> bus
        
        Q = deque()
        targets = set()
        for bus, route in enumerate(routes):
            for rt in route:
                if rt == source:
                    Q.append((bus, 1))
                if rt == target:
                    targets.add(bus)
                routes_buses[rt].add(bus)
        
        # Build Graph
        G = defaultdict(set)
        
        for bus, route in enumerate(routes):
            for rt in route:
                rts = routes_buses[rt]
                for r in rts:
                    G[bus].add(r)
                    G[r].add(bus)
                
        
        seen = set()
        while Q:
            node, bus = Q.popleft()
            if node in targets:
                return bus
            
            seen.add(node)
            
            for nei in G[node]:
                if nei not in seen:
                    Q.append((nei, bus + 1))
        
        return -1
                        