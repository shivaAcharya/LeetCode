class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        res = []
        lo, hi = toBeRemoved[0], toBeRemoved[1]
        
        for start, end in intervals:
            # Case 1 - No overlap       # [2, 4]  -> [5, 6] or [0, 1]
            if end < lo or start > hi:
                res.append([start, end])
                continue
            
            # Case 2 - Keep left        # [3, 7] -> [5, 8]
            if start < lo:
                res.append([start, lo])
            
            # Case 3 - Keep right       # [3, 7] -> [1, 5]
            if end > hi:
                res.append([hi, end])
            
        
        return res