class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            grid[r][c] = '0' # mark visited
            
            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '1':
                    dfs(row, col)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands
        