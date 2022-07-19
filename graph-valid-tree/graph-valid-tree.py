class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        root = [i for i in range(n)]
        
        def find(x):
            while x != root[x]:
                x = root[x]
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX == rootY:
                return False
            root[rootX] = rootY
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return True
        
        