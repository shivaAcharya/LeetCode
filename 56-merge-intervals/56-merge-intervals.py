class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        #end = sorted(intervals, key=lambda x:x[1])
        res = [[intervals[0][0], intervals[0][1]]]
        
        for i in range(1, len(intervals)):
            #end = max(res[-1][1], intervals[i][1])
            
            # Check if merge is needed
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            
            if res[-1][1] < intervals[i][1]:
                res[-1][1] = intervals[i][1]

        return res