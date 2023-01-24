"""
Topological Sort
1. indegrees array = [0] * numCourses
2. Build G and maintain indegrees from prerequisites
    for u, v in prerequisites:
        G = {
            v : {u}
        }
        indegrees[u] += 1
3. Initialize course_taken to 0 and Q with 0 indegree courses
4. Perform BFS and maintain course_taken
5. Return course_taken == numCourses

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        G = defaultdict(set)

        for u, v in prerequisites:
            G[v].add(u)
            indegrees[u] += 1
        
        Q = deque([course for course, indegree in enumerate(indegrees) if indegree == 0])

        course_taken = 0
        while Q:
            course = Q.popleft()
            course_taken += 1

            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return course_taken == numCourses
"""
Time => O(V + E)  V => numCourses, E => len(prerequisites)
Space => O(V + E)
"""
