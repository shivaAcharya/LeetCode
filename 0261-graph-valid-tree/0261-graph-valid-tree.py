class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        # Build Graph
        G = defaultdict(set)

        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        
        # Initialize Q with 0
        Q = deque([0])
        visited = set([0])

        while Q:
            node = Q.popleft()
            
            for nei in G[node]:
                if nei not in visited:
                    visited.add(nei)
                    Q.append(nei)
        
        return len(visited) == n
        
        