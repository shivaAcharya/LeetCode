class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Build graph
        G = defaultdict(list)
        
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        seen = set()
        def search(node):
            if node == destination:
                return True

            if node in seen:
                return False

            seen.add(node)

            for nei in G[node]:
                if search(nei):
                    return True
            return False
        
        return search(source)