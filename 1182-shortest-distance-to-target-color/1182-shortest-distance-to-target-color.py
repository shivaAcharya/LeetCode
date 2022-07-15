class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        
        for idx, color in enumerate(colors):
            groups[color].append(idx)
            
        res = []
        
        def bin_search(i, indices):
             
            left, right = 0, len(indices) - 1
            
            while left < right:
                mid = (left + right) // 2
                
                if indices[mid] < idx:
                    left = mid + 1
                else:
                    right = mid
            return left, right
        
        for idx, color in queries:
            if color not in groups:
                res.append(-1)
            
                # Binary search to find closest
            else:
                indices = groups[color]
                left, right = bin_search(idx, indices)
            
                # Check for neighbors
                r = 1
                if right == 0:
                    r = 0

                res.append(min(abs(indices[left] - idx), abs(indices[left - r] - idx)))
        
        return res