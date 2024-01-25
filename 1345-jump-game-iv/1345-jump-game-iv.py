"""
Initialize val_idx hashmap
Intialize Queue with start idx and step being 0
Initialize a visited set to keep track of visited indices.
Use BFS

"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        val_idx = defaultdict(set)
        
        for i, num in enumerate(arr):
            val_idx[num].add(i)
            
        Q = deque([(0, 0)])
        visited = set()
        visited.add(0)
        while Q:
            idx, steps = Q.popleft()
            # print(idx, steps)
            if idx == len(arr) - 1:
                return steps
            
            visited.add(idx)
            
            for i in (idx + 1), (idx - 1):
                if 0 <= i < len(arr) and i not in visited:
                    Q.append((i, steps + 1))
                    visited.add(i)
                
            for i in val_idx[arr[idx]]:
                if i not in visited:
                    Q.append((i, steps + 1))
                    visited.add(i)
            
            del val_idx[arr[idx]]
                    
        