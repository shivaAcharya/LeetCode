class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        G = defaultdict(set)
        indegrees = {c : 0 for c in range(1, n+1)}
        
        for u, v in relations:
            G[u].add(v)
            indegrees[v] += 1
        
        Q = [k for k, v in indegrees.items() if not v]
        
        semesters = courses_taken = 0
        
        while Q:
            semesters += 1
            courses_taken += len(Q)
            courses = []
            for course in Q:
                
                for next_course in G[course]:
                    indegrees[next_course] -= 1
                    if indegrees[next_course] == 0:
                        courses.append(next_course)
            
            Q = courses
        
        return semesters if courses_taken == n else -1