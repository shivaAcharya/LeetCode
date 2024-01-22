"""
arr = [100,-23,-23,404,100,23,23,23,3,404]
        ^


"""
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        num_idx = defaultdict(set)
        
        for idx, num in enumerate(arr):
            num_idx[num].add(idx)
            
        Q = deque([(0, 0)]) # (idx, steps)
        seen = set()
        
        while Q:
            idx, steps = Q.popleft()
            if idx == len(arr) - 1:
                return steps
            
            seen.add(idx)
            
            for nei in (idx + 1), (idx - 1):
                if 0 <= nei < len(arr) and nei not in seen:
                    Q.append((nei, steps + 1))
            
            for nei in num_idx[arr[idx]]:
                if nei not in seen:
                    Q.append((nei, steps + 1))
            
            del num_idx[arr[idx]]
        
        return 0
                    