class UnionFind:
    
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        
        if rootX != rootY:
            #rankX, rankY = self.rank[rootX], self.rank[rootY]
            
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
                
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            
            return True
        
        return False
        
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's Algorithm
        edges = []        
        N = len(points)
        for i in range(N - 1):
            for j in range(i + 1, N):
                xi, yi, xj, yj = points[i][0], points[i][1], points[j][0], points[j][1]
                
                man_distance = abs(xi - xj) + abs(yi - yj)
                edges.append((man_distance, i, j))
        #print(edges)
        edges.sort()
        
        uf = UnionFind(N)
        edges_used = 0
        cost = 0
        
        #print(edges)
        for edge, u, v in edges:
            if uf.union(u, v):
                edges_used += 1
                cost += edge
                if edges_used == N - 1:
                    break
                    
        return cost
                
        