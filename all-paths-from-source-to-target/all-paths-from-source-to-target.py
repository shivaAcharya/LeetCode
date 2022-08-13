class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        path = []
        
        def dfs(s):
            path.append(s)
                        
            if s == len(graph) - 1:
                res.append(path[:] )
                return
        
            
            for nei in graph[s]:
                dfs(nei)
                path.pop()     
        
        
        dfs(0)
        
        return res