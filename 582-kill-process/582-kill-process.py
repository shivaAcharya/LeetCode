class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        G = defaultdict(list)
        
        for parent, child in zip(ppid, pid):
            G[parent].append(child)
        
        # DFS
        res = []
        
        def dfs(node):
            res.append(node)
            
            for nei in G[node]:
                dfs(nei)
        
        dfs(kill)
        return res