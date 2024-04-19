class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            grid[r][c] = '0'
            
            for new_r, new_c in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)
            
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    island_count += 1
        
        return island_count
                