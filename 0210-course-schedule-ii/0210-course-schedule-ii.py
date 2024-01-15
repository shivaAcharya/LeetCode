class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        """
        indegrees = [0, 0, 0, 2]
        G = {
            0 : {1, 2}
            1 : {3}
            2 : {3}
        }
        Q = [0] # Initialize with indegrees 0
        res = []
        seen = set()
        
        Q = [1, 2]
        # BFS
        # If cycle return []
        # Add node to res
        # Traverse nei of node, decrement indegrees, add to Q if indegree == 0
        
        """
        
        indegrees = [0] * numCourses
        G = defaultdict(set)
        
        for a, b in prerequisites:
            indegrees[a] += 1
            G[b].add(a)
        
        Q = deque()
        
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                Q.append(course)
        
        # print(indegrees, G, Q)
        res = []
        while Q:
            course = Q.popleft()
            res.append(course)
            
            for next_course in G[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    Q.append(next_course)
        
        return res if len(res) == numCourses else []
        