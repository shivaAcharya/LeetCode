class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        val_idx = defaultdict(set)
        
        for i, val in enumerate(arr):
            val_idx[val].add(i)
            
        Q = deque([(0, 0)]) # (idx, step)
        
        seen = set()
        while Q:
            i, step = Q.popleft()
            
            if i == len(arr) - 1:
                return step
            
            seen.add(i)
            
            if i + 1 < len(arr) and i + 1 not in seen:
                Q.append((i + 1, step + 1))
            
            if i - 1 >= 0 and i - 1 not in seen:
                Q.append((i - 1, step + 1))
        
            
            for nei in val_idx[arr[i]]:
                if nei not in seen:
                    Q.append((nei, step + 1))
            
            # Clear the key in dictionary to prevent redundant search
            del val_idx[arr[i]]
                    