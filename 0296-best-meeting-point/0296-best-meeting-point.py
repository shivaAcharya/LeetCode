class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/best-meeting-point/solution/
        '''  
        
        def min_distance(points, origin):
            distance = 0
            
            for point in points:
                distance += abs(point - origin)
            
            return distance
        
        rows, cols = [], []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
                    
        row = rows[len(rows) // 2]
        cols.sort()
        col = cols[len(cols) // 2]
        
        return min_distance(rows, row) + min_distance(cols, col)