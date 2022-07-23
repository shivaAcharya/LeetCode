class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        """
        1. Create groups with union find
        2. For every group, sort chars with indices and update the res list.
        3. Join and return res list
        
        """
        
        root = [i for i in range(len(s))]
        rank = [1 for _ in s]
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            
            return root[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    if rank[rootX] == rank[rootY]:
                        rank[rootX] += 1
        
        
        for u, v in pairs:
            union(u, v)

            
        groups = defaultdict(list)
        
        for i in range(len(root)):
            rootI = find(i)
            groups[rootI].append(i)
            
            
        res = ['a'] * len(s)
        
        for indices in groups.values():
            sorted_chars = sorted([s[i] for i in indices])
            for i, c in zip(indices, sorted_chars):
                res[i] = c
        
        return "".join(res)
        
        
        