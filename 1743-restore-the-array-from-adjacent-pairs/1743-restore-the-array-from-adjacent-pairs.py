class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        G = defaultdict(list)
        
        for u, v in adjacentPairs:
            G[u].append(v)
            G[v].append(u)
            
        root = None
        
        for node in G:
            if len(G[node]) == 1:
                root = node
                break
        
        res = []
        
        def dfs(node, prev):
            res.append(node)
            
            for nei in G[node]:
                if nei != prev:
                    dfs(nei, node)
        
        dfs(root, None)
        return res
        