class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        destination = len(graph) - 1
        Q = deque([[0]])
        res = []
                
        while Q:
            path = Q.popleft()
            node = path[-1]
            
            if node == destination:
                res.append(path)
                #continue
            
            for nei in graph[node]:
                Q.append(path + [nei])
        
        return res
                
                