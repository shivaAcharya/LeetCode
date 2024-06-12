class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        indegrees = Counter()
        
        for a, b in prerequisites:
            G[b].add(a)
            indegrees[a] += 1
            
        Q = deque([course for course in range(numCourses) if course not in indegrees])
        res = []
        
        while Q:
            course = Q.popleft()
            res.append(course)
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        return res if len(res) == numCourses else []
        