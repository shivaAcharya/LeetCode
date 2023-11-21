class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        N = len(intervals)
        i = 0
        res = []
        # add non-overlapping intervals before new_interval to res
        while i < N and intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
            i += 1

        # merge overlapping intervals with new_interval
        res.append(new_interval)
        while i < N and min(res[-1][1], intervals[i][1]) >= max(intervals[i][0], res[-1][0]):
            res[-1] = min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])
            i += 1

        # add rest of the non-overlapping intervals to res
        while i < N:
            res.append(intervals[i])
            i += 1
        
        return res
    