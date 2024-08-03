class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            area = 1
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and grid[r][c]:
                    area += dfs(r, c)
            return area            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
        