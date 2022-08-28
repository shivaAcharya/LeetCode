class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        indegrees = [0] * numCourses
        
        for u, v in prerequisites:
            G[v].add(u)
            indegrees[u] += 1
        
        Q = deque()
        # Populate Q
        for course, ind in enumerate(indegrees):
            if not ind:
                Q.append(course)
        
        res = []
        
        #print(G, indegrees, Q)
        while Q:
            course = Q.popleft()
            res.append(course)
            
            for nei in G[course]:
                indegrees[nei] -= 1
                if not indegrees[nei]:
                    Q.append(nei)
        
        return res if len(res) == numCourses else []