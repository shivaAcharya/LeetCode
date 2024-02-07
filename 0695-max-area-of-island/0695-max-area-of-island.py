class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c, area):
            # if (r, c) in visited:
            #     return 0
            
            visited.add((r, c))
            area = 1
            for ro, co in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= ro < ROWS and 0 <= co < COLS and (ro, co) not in visited and grid[ro][co] == 1:
                    area += dfs(ro, co, area + 1)
            return area
            
        
        res = 0
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    res = max(res, dfs(row, col, 1))
                    
        return res