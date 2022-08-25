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
            
            rankX, rankY = self.rank[rootX], self.rank[rootY]
            
            if rankX > rankY:
                self.root[rootY] = rootX
            
            elif rankY < rankX:
                self.root[rootX] = rootY
                
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            
            return True
        
        return False
    
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Kruskal's algorithm
        1. Sort edges in non-decreasing order.
        2. Construct a tree by adding edges as long as it does not form a cycle.
        3. Repeat 2 until n - 1 edges are added.
        
        '''
        Edges = [] # key => edge, value => list of vertices
        # Edges = {1 : [(0, 1), (1, 3)]}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                xi, yi, xj, yj = points[i][0], points[i][1], points[j][0], points[j][1]

                man_distance = abs(xi - xj) + abs(yi - yj)

                Edges.append([man_distance, i, j])
            
        Edges.sort()
        uf = UnionFind(len(points))
        
        #print(Edges)
        edges = 0
        cost = 0
        for edge, u, v in Edges:
            if uf.union(u, v):
                cost += edge
                edges += 1

                if edges == len(points) - 1:
                    #print(Edges)
                    break
        
        return cost
              