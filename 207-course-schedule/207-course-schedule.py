class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = collections.defaultdict(list)
        indegrees = [0] * numCourses
        
        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
        
        Q = deque([])
        res = 0
        
        for i, n in enumerate(indegrees):
            if n == 0: Q.append(i)
                
        while Q:
            node = Q.popleft()
            res += 1
            
            for nei in G[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
                    
        return res == numCourses