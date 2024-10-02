class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS  = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def dfs(r, c):
            visited.add((r, c))
            
            area = 1
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc]:
                    area += dfs(nr, nc)
            return area
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
        