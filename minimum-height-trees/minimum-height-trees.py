class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        indegrees = [0] * n
        
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
            indegrees[u] += 1
            indegrees[v] += 1
        
        Q = [i for i, ind in enumerate(indegrees) if ind <= 1]
        
        remaining_nodes = n
        
        while remaining_nodes > 2:
            
            remaining_nodes -= len(Q)
            
            children = []
            
            for node in Q:
                
                for child in G[node]:
                    indegrees[child] -= 1
                    if indegrees[child] == 1:
                        children.append(child)
            Q = children
            
        return Q