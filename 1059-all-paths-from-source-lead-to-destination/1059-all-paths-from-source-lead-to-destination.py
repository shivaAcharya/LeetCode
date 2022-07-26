class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Create a graph
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)                
        
        visited = set()
        def dfs(s):
            
            # Check if s is end node and not destination
            if not G[s] and s != destination:
                return False
            
            # Check for cycle
            if s in visited:
                return False
            
            visited.add(s)
            
            for node in G[s]:
                if not dfs(node):
                    return False
                visited.remove(node)
            
            return True
            
        
        return dfs(source)