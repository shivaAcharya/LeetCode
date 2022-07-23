class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        """
        1. Create groups with union find
        2. For every group, sort chars with indices and update the res list.
        3. Join and return res list
        
        """
        
        self.root = [i for i in range(len(s))]
        self.rank = [1 for _ in s]
        
        self.components = len(s)
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
                self.components -= 1
        
        
        for u, v in pairs:
            union(u, v)
        
#         print("Check 1 - self.root", self.root)
#         print("self.rank", self.rank)
        
#         if self.components == 1:
#             return "".join(sorted(s))
            
        groups = defaultdict(list)
        
        for i in range(len(self.root)):
            rootx = find(i)
            groups[rootx].append(i)
            
        # print("Check 2 - groups", groups)
            
        res = ['a'] * len(s)
        
        for indices in groups.values():
            sorted_chars = sorted([s[i] for i in indices])
            for i, c in zip(indices, sorted_chars):
                res[i] = c
        
        return "".join(res)
        
        
        