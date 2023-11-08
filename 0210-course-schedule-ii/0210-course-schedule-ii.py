class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courses = []
        Q = deque()
        
        indegrees = defaultdict(int)
        G = defaultdict(list)
        
        # Build G
        for u, v in prerequisites:
            indegrees[u] += 1
            G[v].append(u)
        
        # Populate Q
        for i in range(numCourses):
            if i not in indegrees:
                Q.append(i)
                
        while Q:
            course = Q.popleft()
            courses.append(course)
            for nei in G[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
        
        return courses if len(courses) == numCourses else []
        