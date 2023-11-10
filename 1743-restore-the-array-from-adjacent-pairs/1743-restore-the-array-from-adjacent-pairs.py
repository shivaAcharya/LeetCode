class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        Add first two elements to res.
        Iterate over intervals and compare with last two elem of res:
            If all four different add both elem.
            If mutual found, add non-mutual from the first.
        
        [2, 1, 4, 3]
        3, 4, 3, 2
        
        -2, 4, 1
        
        """
        
        graph = defaultdict(list)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        root = None
        
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        res = []
        
        def dfs(node, prev):
            res.append(node)
            
            for nei in graph[node]:
                if nei != prev:
                    dfs(nei, node)
        
        dfs(root, None)
        return res
    