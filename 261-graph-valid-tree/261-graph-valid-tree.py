class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        
        # Build Graph
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        # Check cycle
        visited = set()
        def dfs(node):
            if node in visited:
                return      
            visited.add(node)
            for nei in G[node]:
                dfs(nei)
        
        dfs(0)
                
        return len(visited) == n