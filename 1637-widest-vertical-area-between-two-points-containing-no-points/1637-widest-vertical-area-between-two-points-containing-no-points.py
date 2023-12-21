class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        x_points = [x for x, _ in points]        
        x_points.sort()
        
        max_diff = 0
        
        for i in range(len(x_points)):
            cur_diff = x_points[i] - x_points[i - 1]
            if cur_diff > max_diff:
                max_diff = cur_diff
        
        return max_diff
        