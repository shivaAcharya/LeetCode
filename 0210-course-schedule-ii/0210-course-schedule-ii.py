class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # if not prerequisites: return []
        
        G = defaultdict(list)
        indegrees = [0] * numCourses
        
        # Build G
        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
        
        Q = deque([idx for idx, course in enumerate(indegrees) if course == 0])
        res = []
        
        while Q:
            course = Q.popleft()
            res.append(course)
            
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return res if len(res) == numCourses else []
        