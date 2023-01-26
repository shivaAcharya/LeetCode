"""
1. Return False if len(edges) != n - 1
2. Build Graph.
3. Check for cycle Maintaining visited set.
4. Return len(visited) == n

"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        # Build Graph
        G = defaultdict(set)
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        

        def dfs(node):

            for nei in G[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        visited = set([0])
        dfs(0)

        return len(visited) == n

"""
Time => O(V + E)
Space => O(V + E)
"""