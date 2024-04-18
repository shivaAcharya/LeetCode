class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        total_perimeter = 0
        def get_perimeter(row, col):
            perimeter = 0
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                    continue
                perimeter += 1
            
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    total_perimeter += get_perimeter(r, c)
        
        return total_perimeter
        
        