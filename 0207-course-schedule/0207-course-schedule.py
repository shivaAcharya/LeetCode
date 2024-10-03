"""
[1, 0] => 1 -> 0
will there be a cycle? => yes?

Build a graph
    G = {
        1 -> [0]
    }
Indegrees = {
    0 : 1
    1 : 0
}
Q = [1]
courses_taken = set()
while Q
    course = popleft()

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = defaultdict(list)
        indegrees = defaultdict(int)
        
        for u, v in prerequisites:
            G[v].append(u)
            indegrees[u] += 1
        
        Q = deque()
        for course in range(numCourses):
            if course not in indegrees:
                Q.append(course)
            
        courses_taken = set()
        while Q:
            course = Q.popleft()
            courses_taken.add(course)
            for new_course in G[course]:
                if new_course in courses_taken:
                    return False
                indegrees[new_course] -= 1
                if indegrees[new_course] == 0:
                    Q.append(new_course)
        
        return len(courses_taken) == numCourses
        