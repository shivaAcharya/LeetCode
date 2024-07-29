class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def dfs(r, c):
            visited.add((r, c))
            area = 1
            for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == 1:
                    area += dfs(row, col)
            return area
    
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    cur_area = dfs(r, c)
                    max_area = max(max_area, cur_area)
                    # print(cur_area)
        
        return max_area
    