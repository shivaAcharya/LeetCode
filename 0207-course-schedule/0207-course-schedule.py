class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        G = defaultdict(set)

        for a, b in prerequisites:
            G[b].add(a)
            indegree[a] += 1
        
        Q = deque([course for course, indegree in enumerate(indegree) if indegree == 0])
        visited = set()
        
        #print(indegree, G)
        while Q:
            course = Q.popleft()
            visited.add(course)

            for nxt_course in G[course]:
                if nxt_course not in visited:
                    indegree[nxt_course] -= 1
                    if indegree[nxt_course] == 0:
                        Q.append(nxt_course)
        
        return len(visited) == numCourses