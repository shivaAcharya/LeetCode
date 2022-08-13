class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            
        visited = set()
        
        def dfs(s):
            
            if not G[s] and s != destination:
                return False
            
            if s in visited:
                return False
            
            visited.add(s)
            
            for nei in G[s]:
                if not dfs(nei):
                    return False
                visited.remove(nei)
            
            return True
        
        return dfs(source)