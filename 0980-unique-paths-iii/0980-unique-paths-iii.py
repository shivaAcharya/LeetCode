class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        # Find start_row, start_col, and non_obstacles
        start_row = start_col = non_obstacles = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                
                if grid[r][c] >= 0:
                    non_obstacles += 1
        
        path_count = 0
        
        def backtrack(row, col, remain):
            nonlocal path_count
            
            if grid[row][col] == 2 and remain == 1:
                path_count += 1
                return
            
            # Mark visited
            temp = grid[row][col]
            grid[row][col] = -2
            remain -= 1
            
            for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr, nc = row + r, col + c
                
                # Continue only if valid
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] >= 0:
                    backtrack(nr, nc, remain)             
            
            grid[row][col] = temp
        
        
        backtrack(start_row, start_col, non_obstacles)
        return path_count