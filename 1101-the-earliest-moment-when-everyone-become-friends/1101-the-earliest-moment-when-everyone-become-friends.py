class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        # Base case
        if len(logs) < n - 1: return -1
        
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
        self.group = n
        
        # Find function with path compression optimization
        def find(x):
            if x != self.root[x]:
                self.root[x] = find(self.root[x])
            return self.root[x]
            
            
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX != rootY:
                if self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    if self.rank[rootX] == self.rank[rootY]:
                        self.rank[rootX] += 1
                self.group -= 1
        
        # Sort logs based on time-stamp
        logs.sort()
        
        for time, u, v in logs:
            union(u, v)
            
            if self.group == 1:
                return time
        
        return -1