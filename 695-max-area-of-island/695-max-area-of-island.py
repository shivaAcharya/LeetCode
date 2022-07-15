class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            area = 1
            
            for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col]:
                    area += dfs(row, col)
            return area            
        
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area