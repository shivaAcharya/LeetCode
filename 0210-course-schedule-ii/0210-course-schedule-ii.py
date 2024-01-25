"""
Prerequisite = [a, b], take b before a

Initialize a Graph, adjacency list of courses
Initialize an indegree counter
Perform Topological sorting
Add all courses with 0 indegrees into a Q
Initialize res to accumulate courses
While Q
    popleft Q, and add it to res
    Traverse the graph and decrement the indegrees
    If indegrees == 0, add it to the queue

return res if len(res) == n else []
    

"""
from collections import Counter, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        indegrees = Counter()
        
        for a, b in prerequisites:
            G[b].add(a)
            indegrees[a] += 1
            
        Q = deque()
        for n in range(numCourses):
            if n not in indegrees:
                Q.append(n)
                
        res = []
        while Q:
            course = Q.popleft()
            res.append(course)
            
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return res if len(res) == numCourses else []
        