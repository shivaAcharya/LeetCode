class Solution:
    def numOfMinutes(self, n: int, headID: int, managers, informTime):
        
        graph = self.buildGraph(managers)
        self.maxTime = 0

        def dfs(source, currentTime):
            self.maxTime = max(self.maxTime, currentTime)

            # Explore neighbors
            for neighbor in graph[source]:
                dfs(neighbor, currentTime + informTime[source])
        
        dfs(headID, 0)
        return self.maxTime

    # We Build a Directed Graph
    def buildGraph(self, managers):
        # Adjacency List
        G = defaultdict(list)

        for employee, manager in enumerate(managers):
            if manager != -1:
                G[manager].append(employee)
        
        return G