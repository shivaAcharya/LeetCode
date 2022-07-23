class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countDays(capacity):
            
            day = cur_weight = 0
            
            for weight in weights:
                if cur_weight + weight <= capacity:
                    cur_weight += weight
                else:
                    cur_weight = weight
                    day += 1
                    
            return day
            
            
        
        lo, hi = max(weights), sum(weights)
        
        # Binary search
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if countDays(mid) < days:
                hi = mid
            else:
                lo = mid + 1
        
        return lo