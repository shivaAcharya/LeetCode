class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0
        
        def dfs(r, c):
            grid[r][c] = '0'
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                    dfs(nr, nc)
        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    num_of_islands += 1
        
        return num_of_islands
        