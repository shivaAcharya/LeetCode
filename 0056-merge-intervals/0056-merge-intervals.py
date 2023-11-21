class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        merged_intervals = []
        
        for u, v in intervals:
            # When two intervals are disjoint | not merged_intervals
            if not merged_intervals or u > merged_intervals[-1][1]:
                merged_intervals.append([u, v])
            # When second interval overlaps partially
            elif v > merged_intervals[-1][1]:
                merged_intervals[-1][1] = v
        
        return merged_intervals
                