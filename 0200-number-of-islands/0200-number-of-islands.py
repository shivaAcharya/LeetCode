class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()
        
        def dfs(r, c):
            seen.add((r, c)) # mark visited
            
            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '1' and (row, col) not in seen:
                    dfs(row, col)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
        
        return islands
        