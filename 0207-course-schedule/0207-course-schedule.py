class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        G = defaultdict(list)

        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
        
        Q = deque()

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                Q.append(course)
        
        # BFS
        course_taken = 0
        while Q:

            course = Q.popleft()
            course_taken += 1

            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return course_taken == len(G)