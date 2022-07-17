class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort
        
        
        # Build Graph and indegrees
        G = defaultdict(list)
        indegrees = defaultdict(int)
        
        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
            
        Q = deque()
        
        # Populate Q with 0 indegree nodes
        for i in range(numCourses):
            if i not in indegrees:
                Q.append(i)
        
        res = []
        
        while Q:
            course = Q.popleft()
            res.append(course)
            
            for nei in G[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
        
        return res if len(res) == numCourses else []
            
        