class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Build Graph
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
            
        # Use BFS
        Q = deque([source])
        visited = set()
        
        while Q:
            node = Q.popleft()
            
            if node == destination:
                return True
            
            visited.add(node)
            
            for child in G[node]:
                if child not in visited:
                    Q.append(child)
        
        return False