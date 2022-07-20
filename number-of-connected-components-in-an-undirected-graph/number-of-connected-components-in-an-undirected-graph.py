class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n
        
        def find(x):
            if x == self.root[x]:
                return x
            self.root[x] = find(self.root[x])
            
            return self.root[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY                
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                self.components -= 1
        
        for u, v in edges:
            union(u, v)
        
        return self.components