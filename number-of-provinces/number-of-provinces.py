class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        #self.rank = [1] * size  # Rank for union by rank optimization
        #self.count = size
    
    # Find optimization with path compression
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x  
#         if x == self.root[x]:
#             return x
        
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]
    
    # Union optimization by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
        
        # if rootX != rootY:
        #     if self.rank[rootX] > self.rank[rootY]:
        #         self.root[rootY] = rootX
        #     elif self.rank[rootX] < self.rank[rootY]:
        #         self.root[rootX] = rootY
        #     else:
        #         self.root[rootY] = rootX
        #         self.rank[rootX] += 1
        #     self.count -= 1
    
    
    def getCount(self):
        return self.count

        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjoint_set = UnionFind(n)
        
        for x in range(n):
            for y in range(x+1, n):
                if isConnected[x][y]:
                    disjoint_set.union(x, y)
        
        provinces = 0
        for i in range(len(disjoint_set.root)):
            if i == disjoint_set.root[i]:
                provinces += 1
        return provinces
        
        
        
        