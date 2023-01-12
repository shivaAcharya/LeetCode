class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(r, c):
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr, nc)
        

        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands