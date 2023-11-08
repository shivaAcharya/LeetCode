class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Construct Graph
        
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for nei in G[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            
            return False
        
        return dfs(source)