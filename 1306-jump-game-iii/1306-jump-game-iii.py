class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        Q = deque([start])
        
        while Q:
            node = Q.popleft()
            
            if arr[node] == 0:
                return True
            
            if arr[node] < 0:
                continue
                
            # Mark node visited
            arr[node] = -arr[node]
            
            for nei in node + arr[node], node - arr[node]:
                if 0 <= nei < len(arr):
                    Q.append(nei)
        
        return False
        