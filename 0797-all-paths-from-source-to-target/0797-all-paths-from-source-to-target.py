class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        cur_path = [0]
        
        def dfs(node):
            
            if node == len(graph) - 1:
                # Path found
                res.append(cur_path[:])
                return
            
            for nei in graph[node]:
                cur_path.append(nei)
                dfs(nei)
                cur_path.pop()
        
        dfs(0)
        
        return res
    