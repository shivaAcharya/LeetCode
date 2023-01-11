class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Base case
        if not prerequisites: return True
        
        indegrees = defaultdict(int)
        G = defaultdict(list)

        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
        
        Q = deque()

        # Initialize Q
        for course in range(numCourses):
            if course not in indegrees:
                Q.append(course)
        
        # BFS
        while Q:
            course = Q.popleft()
            # Take the course
            numCourses -= 1

            # Explore neighbors
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return numCourses == 0