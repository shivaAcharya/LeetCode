"""
a, b => first take b to take a

numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
start => indegrees 0 => [0]

G
0 -> 1, 2
2 -> 3
3 -> 2

[0, 1, 2, 3]

Initialize indegrees array.
Intialize Q with indegrees 0 nodes
Create Graph from prerequisites
Initialize res array
While Q:
    decrement indegrees of next courses
    Add new course with indegrees 0 to Q.
Return res array if length of res == numCourses, otherwise []


"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegrees = [0] * numCourses
        G = defaultdict(set)
        for a, b in prerequisites:
            G[b].add(a)
            indegrees[a] += 1
        
        Q = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                Q.append(course)
                
        res = []
        while Q:
            course = Q.popleft()
            res.append(course)
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
                    
        return res if len(res) == numCourses else []
        