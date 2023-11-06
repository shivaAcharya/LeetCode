class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        Q = deque()
        seen = set()
        fresh_oranges = 0
        
        # Populate Q with rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    Q.append((r, c))
                    seen.add((r, c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
                    
        minutes = 0
        
        while Q:
            rotten_oranges = []
            for r, c in Q:
                for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == 1:
                        rotten_oranges.append((row, col))
                        seen.add((row, col))
                        fresh_oranges -= 1 
            minutes += 1 if rotten_oranges else 0
            Q = rotten_oranges
        
        return minutes if not fresh_oranges else -1
        