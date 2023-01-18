class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        G = defaultdict(set)

        for a, b in prerequisites:
            G[b].add(a)
            indegree[a] += 1
        
        Q = deque([course for course, indegree in enumerate(indegree) if indegree == 0])
        
        #print(indegree, G)
        courses_taken = 0
        while Q:
            course = Q.popleft()
            courses_taken += 1

            for nxt_course in G[course]:
                indegree[nxt_course] -= 1
                if indegree[nxt_course] == 0:
                    Q.append(nxt_course)
        
        return courses_taken == numCourses