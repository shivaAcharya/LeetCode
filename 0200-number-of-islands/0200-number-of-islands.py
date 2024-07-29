class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0
        visited = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return 
            visited.add((r, c))
            
            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
            
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    dfs(r, c)
        
        return island_count
        