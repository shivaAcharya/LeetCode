class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        merged_intervals = [[intervals[0][0], intervals[0][1]]]
        
        for u, v in intervals[1:]:
            a, b = merged_intervals[-1][0], merged_intervals[-1][1]
            
            # When two intervals are disjoint
            if u > b:
                merged_intervals.append([u, v])
            # When second interval overlaps partially
            elif v > b:
                merged_intervals[-1][1] = v
        
        return merged_intervals
                