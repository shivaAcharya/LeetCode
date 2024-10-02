class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0
        visited = set()
        
        def dfs(r, c):
            visited.add((r, c))
            
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1
        
        return island_count
        