'''
1. Build Graph
2. Initialize components to 0.
3. Perform DFS and mark the nodes visited for node in range(n)
4. Increment components by one for every dfs.
5. Return components

'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        G = defaultdict(set)

        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        
        def dfs(node):
            
            for nei in G[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        
        components, visited = 0, set()

        for node in range(n):
            if node not in visited:
                components += 1
                visited.add(node)
                dfs(node)
        
        return components
"""
Time => O(V + E)
Space => O(V + E)
"""