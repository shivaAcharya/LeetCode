class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build Graph
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        # Check cycle
        visited = set()
        def has_cycle(node, parent):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in G[node]:
                if nei != parent and has_cycle(nei, node):
                    return True
            return False
        
        if has_cycle(0, -1):
            return False
                
        return len(visited) == n