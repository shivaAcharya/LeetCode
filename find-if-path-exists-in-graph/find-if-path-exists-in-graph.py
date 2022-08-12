class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        visited = set()
        
        def dfs(s):
            if s == destination:
                return True
            
            if s in visited:
                return False
            
            visited.add(s)
            
            for nei in G[s]:
                if dfs(nei):
                    return True
                
            return False
        
        return dfs(source)